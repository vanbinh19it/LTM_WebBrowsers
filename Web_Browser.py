import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from bs4 import BeautifulSoup
import requests


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction("Back", self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction("Forward", self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction("Reload", self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction("Home", self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.get_btn = QAction("GET", self)
        self.get_btn.triggered.connect(self.send_get_request)
        navbar.addAction(self.get_btn)

        self.post_btn = QAction("POST", self)
        self.post_btn.triggered.connect(self.send_post_request)
        navbar.addAction(self.post_btn)

        self.head_btn = QAction("HEAD", self)
        self.head_btn.triggered.connect(self.send_head_request)
        navbar.addAction(self.head_btn)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://tiki.vn"))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

    def send_get_request(self):
        url = self.browser.url().toString()
        response = requests.get(url)
        self.display_response_info(response)
        self.analyze_html_content(response.text)

    def send_post_request(self):
        url = self.browser.url().toString()
        response = requests.post(url)
        self.display_response_info(response)
        self.analyze_html_content(response.text)

    def send_head_request(self):
        url = self.browser.url().toString()
        response = requests.head(url)
        self.display_response_info(response)

    def display_response_info(self, response):
        print("Request Response:")
        print("Status Code:", response.status_code)
        print("Content Length:", response.headers.get("Content-Length"))
        print("Content Type:", response.headers.get("Content-Type"))
        print()

    def analyze_html_content(self, html):
        soup = BeautifulSoup(html, "html.parser")

        p_tags = soup.find_all("p")
        div_tags = soup.find_all("div")
        span_tags = soup.find_all("span")
        img_tags = soup.find_all("img")

        print("HTML Content Analysis:")
        print("Number of <p> tags:", len(p_tags))
        print("Number of <div> tags:", len(div_tags))
        print("Number of <span> tags:", len(span_tags))
        print("Number of <img> tags:", len(img_tags))


app = QApplication(sys.argv)
QApplication.setApplicationName("Sagar's Browser")
window = MainWindow()
app.exec_()
