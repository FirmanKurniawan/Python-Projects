import pyqtgraph as pg
from pathlib import Path
from pyqtgraph.Qt import QtCore, QtGui, QtWidgets
try:
    from Lifetime_analysis.read_ph_phd import read_picoharp_phd, get_x_y    
except Exception as e:
    print(e)
import matplotlib.pyplot as plt

"""Recylce params for plotting"""
plt.rc('xtick', labelsize = 20)
plt.rc('xtick.major', pad = 3)
plt.rc('ytick', labelsize = 20)
plt.rc('lines', lw = 2.5, markersize = 7.5)
plt.rc('legend', fontsize = 20)
plt.rc('axes', linewidth=3.5)

pg.mkQApp()

base_path = Path(__file__).parent
file_path = (base_path / "Multi_Trace_Exporter.ui").resolve()

uiFile = file_path

WindowTemplate, TemplateBaseClass = pg.Qt.loadUiType(uiFile)

class MainWindow(TemplateBaseClass):

    def __init__(self):
        super(TemplateBaseClass, self).__init__()
        
        # Create the main window
        self.ui = WindowTemplate()
        self.ui.setupUi(self)

        self.temp_layout = pg.GraphicsLayoutWidget()

        # file system tree
        self.fs_model = QtWidgets.QFileSystemModel()
        self.fs_model.setRootPath(QtCore.QDir.currentPath())
        self.ui.treeView.setModel(self.fs_model)
        self.ui.treeView.setIconSize(QtCore.QSize(25,25))
        self.ui.treeView.setSortingEnabled(True)

        self.tree_selectionModel = self.ui.treeView.selectionModel()
        self.tree_selectionModel.selectionChanged.connect(self.on_treeview_selection_change)

        self.ui.comboBox.currentIndexChanged.connect(self.add_trace_to_temp_plot)
        self.ui.add_pushButton.clicked.connect(self.add_trace_to_mem)
        self.ui.export_pushButton.clicked.connect(self.pub_ready_plot_export)

        self.x_i = []
        self.y_i = []
        self.x_mem = []
        self.y_mem = []
        self.legend = []

        self.show()

    def on_treeview_selection_change(self):
        try:
            fname = self.fs_model.filePath(self.tree_selectionModel.currentIndex())
            _ , ext = fname.rsplit('.',1)

            self.ui.comboBox.clear()
            self.ui.textBrowser.clear()
            self.x_i = []
            self.y_i = []

            if ext in ['phd']:
                self.parser = read_picoharp_phd(fname)
                curve_list = []
                
                for i in range(self.parser.no_of_curves()):
                    curve_list.append("Curve "+str(i))
                    x, y = get_x_y(i, self.parser, smooth_trace=self.ui.smooth_checkBox.isChecked(), boxwidth=self.ui.smooth_spinBox.value())
                    self.x_i.append(x)
                    self.y_i.append(y)
                
                self.ui.comboBox.addItems(curve_list)
                self.ui.textBrowser.setText(str(self.parser.info()))
            
            else:
                self.ui.textBrowser.setText(str("Select a PicoHarp File"))
        except Exception as e:
            print(e)
    
    def add_trace_to_temp_plot(self):
        try:
            #self.temp_layout = pg.GraphicsLayoutWidget()
            self.temp_layout.clear()
            self.temp_plot = self.temp_layout.addPlot(title = "Current Selection")
            self.temp_plot.plot(self.x_i[self.ui.comboBox.currentIndex()], self.y_i[self.ui.comboBox.currentIndex()], pen='r')
            self.temp_plot.setLogMode(False, True)
            self.temp_layout.show()
        except Exception as e:
            print(e)
    
    def add_trace_to_mem(self):
        try:
            self.x_mem.append(self.x_i[self.ui.comboBox.currentIndex()])
            self.y_mem.append(self.y_i[self.ui.comboBox.currentIndex()])
            self.legend.append(self.ui.lineEdit.text())
        except Exception as e:
            print(e)
    
    def pub_ready_plot_export(self):
        try:
            filename = QtWidgets.QFileDialog.getSaveFileName(self,caption="Filename with EXTENSION")
            
            plt.figure(figsize=(8,6))
            plt.tick_params(direction='out', length=8, width=3.5)
            for i in range(len(self.x_mem)):
                if self.ui.Normalize_checkBox.isChecked():
                    plt.plot(self.x_mem[i], self.y_mem[i]/max(self.y_mem[i]), label=str(self.legend[i]))
                else:
                    plt.plot(self.x_mem[i], self.y_mem[i], label=str(self.legend[i]))

            plt.yscale('log')
            plt.xlabel("Time (ns)", fontsize=20, fontweight='bold')
            plt.ylabel("Intensity (norm.)", fontsize=20, fontweight='bold')
            plt.legend()
            plt.tight_layout()
            
            plt.savefig(filename[0],bbox_inches='tight', dpi=300)
            plt.close()

            self.clear_memory()
        
        except Exception as e:
            print(e)
            pass

    def clear_memory(self):
        self.x_mem = []
        self.y_mem = []
        self.legend = []




def run():
    win = MainWindow()
    QtGui.QApplication.instance().exec_()
    return win

#run()