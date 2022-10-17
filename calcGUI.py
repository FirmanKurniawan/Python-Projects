from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.numberLabel = QtWidgets.QLabel(self.centralwidget)
        self.numberLabel.setGeometry(QtCore.QRect(10, 20, 431, 91))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(36)
        font.setUnderline(False)
        self.numberLabel.setFont(font)
        self.numberLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.numberLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.numberLabel.setLineWidth(2)
        self.numberLabel.setMidLineWidth(0)
        self.numberLabel.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.numberLabel.setObjectName("numberLabel")
        self.persenButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("%"))
        self.persenButton.setGeometry(QtCore.QRect(10, 120, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(16)
        self.persenButton.setFont(font)
        self.persenButton.setObjectName("persenButton")
        self.bagiButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("/"))
        self.bagiButton.setGeometry(QtCore.QRect(340, 120, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(16)
        self.bagiButton.setFont(font)
        self.bagiButton.setObjectName("bagiButton")
        self.arrowButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.remove_it())
        self.arrowButton.setGeometry(QtCore.QRect(230, 120, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(16)
        self.arrowButton.setFont(font)
        self.arrowButton.setObjectName("arrowButton")
        self.clearButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("C"))
        self.clearButton.setGeometry(QtCore.QRect(120, 120, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(16)
        self.clearButton.setFont(font)
        self.clearButton.setObjectName("clearButton")
        self.sembilanButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("9"))
        self.sembilanButton.setGeometry(QtCore.QRect(230, 180, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(16)
        self.sembilanButton.setFont(font)
        self.sembilanButton.setObjectName("sembilanButton")
        self.tujuhButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("7"))
        self.tujuhButton.setGeometry(QtCore.QRect(10, 180, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(16)
        self.tujuhButton.setFont(font)
        self.tujuhButton.setObjectName("tujuhButton")
        self.kaliButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("*"))
        self.kaliButton.setGeometry(QtCore.QRect(340, 180, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(16)
        self.kaliButton.setFont(font)
        self.kaliButton.setObjectName("kaliButton")
        self.delapanButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("8"))
        self.delapanButton.setGeometry(QtCore.QRect(120, 180, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(16)
        self.delapanButton.setFont(font)
        self.delapanButton.setObjectName("delapanButton")
        self.tigaButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("3"))
        self.tigaButton.setGeometry(QtCore.QRect(230, 300, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(16)
        self.tigaButton.setFont(font)
        self.tigaButton.setObjectName("tigaButton")
        self.enamButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("6"))
        self.enamButton.setGeometry(QtCore.QRect(230, 240, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(16)
        self.enamButton.setFont(font)
        self.enamButton.setObjectName("enamButton")
        self.satuButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("1"))
        self.satuButton.setGeometry(QtCore.QRect(10, 300, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(16)
        self.satuButton.setFont(font)
        self.satuButton.setObjectName("satuButton")
        self.empatButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("4"))
        self.empatButton.setGeometry(QtCore.QRect(10, 240, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(16)
        self.empatButton.setFont(font)
        self.empatButton.setObjectName("empatButton")
        self.kurangButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("-"))
        self.kurangButton.setGeometry(QtCore.QRect(340, 240, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(16)
        self.kurangButton.setFont(font)
        self.kurangButton.setObjectName("kurangButton")
        self.tambahButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("+"))
        self.tambahButton.setGeometry(QtCore.QRect(340, 300, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(16)
        self.tambahButton.setFont(font)
        self.tambahButton.setObjectName("tambahButton")
        self.limaButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("5"))
        self.limaButton.setGeometry(QtCore.QRect(120, 240, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(16)
        self.limaButton.setFont(font)
        self.limaButton.setObjectName("limaButton")
        self.duaButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("2"))
        self.duaButton.setGeometry(QtCore.QRect(120, 300, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(16)
        self.duaButton.setFont(font)
        self.duaButton.setObjectName("duaButton")
        self.nolButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("0"))
        self.nolButton.setGeometry(QtCore.QRect(120, 360, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(16)
        self.nolButton.setFont(font)
        self.nolButton.setObjectName("nolButton")
        self.titikButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.dot_it())
        self.titikButton.setGeometry(QtCore.QRect(230, 360, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(16)
        self.titikButton.setFont(font)
        self.titikButton.setObjectName("titikButton")
        self.plusminusButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.plus_minus_it())
        self.plusminusButton.setGeometry(QtCore.QRect(10, 360, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(16)
        self.plusminusButton.setFont(font)
        self.plusminusButton.setObjectName("plusminusButton")
        self.hasilButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.math_it())
        self.hasilButton.setGeometry(QtCore.QRect(340, 360, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(16)
        self.hasilButton.setFont(font)
        self.hasilButton.setObjectName("hasilButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.numberLabel.setText(_translate("MainWindow", "0"))
        self.persenButton.setText(_translate("MainWindow", "%"))
        self.bagiButton.setText(_translate("MainWindow", "/"))
        self.arrowButton.setText(_translate("MainWindow", "<<"))
        self.clearButton.setText(_translate("MainWindow", "C"))
        self.sembilanButton.setText(_translate("MainWindow", "9"))
        self.tujuhButton.setText(_translate("MainWindow", "7"))
        self.kaliButton.setText(_translate("MainWindow", "X"))
        self.delapanButton.setText(_translate("MainWindow", "8"))
        self.tigaButton.setText(_translate("MainWindow", "3"))
        self.enamButton.setText(_translate("MainWindow", "6"))
        self.satuButton.setText(_translate("MainWindow", "1"))
        self.empatButton.setText(_translate("MainWindow", "4"))
        self.kurangButton.setText(_translate("MainWindow", "-"))
        self.tambahButton.setText(_translate("MainWindow", "+"))
        self.limaButton.setText(_translate("MainWindow", "5"))
        self.duaButton.setText(_translate("MainWindow", "2"))
        self.nolButton.setText(_translate("MainWindow", "0"))
        self.titikButton.setText(_translate("MainWindow", "."))
        self.plusminusButton.setText(_translate("MainWindow", "+/-"))
        self.hasilButton.setText(_translate("MainWindow", "="))

    def math_it(self):
        # Semua Tampilan angka
        screen = self.numberLabel.text()
        try:
            # Hitung pakai eval()
            hasil = eval(screen)
            # print hasil
            self.numberLabel.setText(str(hasil))
        except:
            # jika terjadi kesalahan ketika menjumlahkan
            self.numberLabel.setText("ERROR")

    # hapus
    def remove_it(self):
        screen = self.numberLabel.text()
        screen = screen[:-1]
        self.numberLabel.setText(screen)

        if screen == "":
            self.numberLabel.setText("0")

    def plus_minus_it(self):
        screen = self.numberLabel.text()
        if "-" in screen:
            self.numberLabel.setText(screen.replace("-", ""))
        else:
            self.numberLabel.setText(f"-{screen}")

    # titik
    def dot_it(self):
        screen = self.numberLabel.text()

        if screen[-1] == ".":
            pass
        else:
            self.numberLabel.setText(f"{screen}.")

    # plus / minus add
    def press_it(self, pressed):
        if pressed == "C":
            self.numberLabel.setText("0")
        else:
            # Cek jika label mulai dengan 0 maka hapus
            if self.numberLabel.text() == "0":
                self.numberLabel.setText("")
            self.numberLabel.setText(f"{self.numberLabel.text()}{pressed}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
