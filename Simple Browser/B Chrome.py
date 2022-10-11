import sys
from PyQt5.QtCore import * # For Url
from PyQt5.QtWidgets import * # For Widgets
from PyQt5.QtWebEngineWidgets import * # For WebEngine

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.browser = QWebEngineView() # To make a browser look
        self.browser.setUrl(QUrl('https://www.google.com/'))
        self.setCentralWidget(self.browser)
        self.showMaximized() # Browser screen will be maximized i.e. Full screen

        # Navbar

        navbar = QToolBar()
        self.addToolBar(navbar) # TO add navigation bar

        # Back Button
        back_btn = QAction('<',self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # Forward Button
        next_btn = QAction('>',self)
        next_btn.triggered.connect(self.browser.forward)
        navbar.addAction(next_btn)

        # Reload Button
        reload_btn = QAction('⟳',self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)


        # Home Button
        home_btn = QAction('Home',self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # URL Bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        # URL Changing
        self.browser.urlChanged.connect(self.update_url)

    def update_url(self, q):
        self.url_bar.setText(q.toString())
    
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://www.google.com/'))

app = QApplication(sys.argv)
QApplication.setApplicationName('B Chrome')
window = MainWindow()
app.exec_()
