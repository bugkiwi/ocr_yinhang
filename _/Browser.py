

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *
import webbrowser

class WebPage(QWebPage):
    def __init__(self):
        super(WebPage, self).__init__()
 
    def acceptNavigationRequest(self, frame, request, type):
        
        if(type == QWebPage.NavigationTypeLinkClicked):
            if(frame == self.mainFrame()):
                self.view().load(request.url())
                print "local window"
            else:
                #webbrowser.open(request.url().toString())
                self.view().load(request.url())
                return False
        return QWebPage.acceptNavigationRequest(self, frame, request, type)

class MyBrowser(QWidget):

    def __init__(self, parent = None):
        super(MyBrowser, self).__init__(parent)
        self.createLayout()
        self.createConnection()

    def search(self):
        address = str(self.addressBar.text())
        if address:
            if address.find('://') == -1:
                address = 'http://' + address
            url = QUrl(address)
            self.webView.load(url)
            
            self.webView.show()
    def linkClicked(self, url):
        self.webView.load(url)
        
    def createLayout(self):
        self.setWindowTitle("keakon's browser")

        self.addressBar = QLineEdit()
        self.goButton = QPushButton("&GO")
        self.sendButton = QPushButton("&Send")
        bl = QHBoxLayout()
        bl.addWidget(self.addressBar)
        bl.addWidget(self.goButton)
        bl.addWidget(self.sendButton)

        self.webView = QWebView()
        self.webView.setPage(WebPage())
        self.webSettings = self.webView.settings()
        self.webSettings.setAttribute(QWebSettings.PluginsEnabled,True)
        self.webSettings.setAttribute(QWebSettings.JavascriptEnabled,True)
        self.webView.page().setLinkDelegationPolicy(QWebPage.DelegateAllLinks)
        self.webView.page().linkClicked.connect(self.linkClicked)


        layout = QVBoxLayout()
        layout.addLayout(bl)
        layout.addWidget(self.webView)

        self.setLayout(layout)

    def createConnection(self):
        self.connect(self.addressBar, SIGNAL('returnPressed()'), self.search)
        self.connect(self.addressBar, SIGNAL('returnPressed()'), self.addressBar, SLOT('selectAll()'))
        self.connect(self.goButton, SIGNAL('clicked()'), self.search)
        self.connect(self.goButton, SIGNAL('clicked()'), self.addressBar, SLOT('selectAll()'))

        self.connect(self.sendButton, SIGNAL('clicked()'), self.sendtest)


    def sendtest(self):
        f = open('1.txt','wb')
        f.write(self.webView.page().mainFrame().toHtml().encode('UTF-8'))
        f.close()
        

app = QApplication(sys.argv)

browser = MyBrowser()
browser.show()

sys.exit(app.exec_())

