# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 20:43:12 2019

@author: sarth
"""
from pathlib import Path
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui

"""Export Images GUI"""
base_path = Path(__file__).parent
ui_file_path = (base_path / "export_fig_gui.ui").resolve()
exportFig_WindowTemplate, exportFig_TemplateBaseClass = pg.Qt.loadUiType(ui_file_path)

class ExportFigureWindow(exportFig_TemplateBaseClass):
    
    export_fig_signal = QtCore.pyqtSignal()
    
    def __init__(self):
        exportFig_TemplateBaseClass.__init__(self)
        
        self.ui = exportFig_WindowTemplate()
        self.ui.setupUi(self)
        self.ui.cmap_comboBox.addItems(['viridis', 'plasma', 'inferno', 'magma',
                                        'cividis','Greys', 'Purples', 'Blues', 
                                        'Greens', 'Oranges', 'Reds', 'YlOrBr', 
                                        'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu', 
                                        'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 
                                        'YlGn', 'binary', 'gist_yarg', 'gist_gray', 
                                        'gray', 'bone', 'pink', 'spring', 'summer', 
                                        'autumn', 'winter', 'cool', 'Wistia', 'hot', 
                                        'afmhot', 'gist_heat', 'copper', 'rainbow', 'jet'])
        self.ui.cbar_checkBox.stateChanged.connect(self.cbar_title_state)
        self.ui.exportFig_pushButton.clicked.connect(self.export)
        self.show()
    
    def cbar_title_state(self):
        if self.ui.cbar_checkBox.isChecked():
            self.ui.cbar_label.setEnabled(True)
        else:
            self.ui.cbar_label.setEnabled(False)
    
    def export(self):
        self.export_fig_signal.emit()
        self.close()

"""Export plot GUI"""
ui_file_path = (base_path / "export_plot.ui").resolve()
export_WindowTemplate, export_TemplateBaseClass = pg.Qt.loadUiType(ui_file_path)

class ExportPlotWindow(export_TemplateBaseClass):
    
    export_fig_signal = QtCore.pyqtSignal()
    
    def __init__(self):
        export_TemplateBaseClass.__init__(self)
        
        self.ui = export_WindowTemplate()
        self.ui.setupUi(self)
        #self.ui.traceColor_comboBox.addItems(["C0","C1","C2","C3","C4","C5","C6","C7", "r", "g", "b", "y", "k"])
        #self.ui.fitColor_comboBox.addItems(["k", "r", "b", "y", "g","C0","C1","C2","C3","C4","C5","C6","C7"])
        self.ui.export_pushButton.clicked.connect(self.export)
        #self.ui.legend_checkBox.stateChanged.connect(self.legend_title)
        self.show()
    
    #def legend_title(self):
    #    if self.ui.legend_checkBox.isChecked():
    #        self.ui.legend1_lineEdit.setEnabled(True)
    #        self.ui.legend2_lineEdit.setEnabled(True)
    #    else:
    #        self.ui.legend1_lineEdit.setEnabled(False)
    #        self.ui.legend2_lineEdit.setEnabled(False)
    
    def export(self):
        self.export_fig_signal.emit()
        self.close()