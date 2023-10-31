import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from pytube import YouTube


class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.browser = QWebEngineView(self)
        self.browser.setUrl(QUrl("https://www.youtube.com"))
        self.setCentralWidget(self.browser)

        self.download_button = QPushButton("Download Video", self)
        self.download_button.clicked.connect(self.download_video)

        navbar = QToolBar()
        navbar.addWidget(self.download_button)
        self.addToolBar(navbar)

        self.statusBar()
        self.setGeometry(100, 100, 1024, 768)
        self.setWindowTitle("YouTube Video Downloader")
        self.show()

    def download_video(self):
        current_url = self.browser.url().toString()  # Lấy URL hiện tại từ trình duyệt
        if "youtube.com" in current_url:
            try:
                yt = YouTube(current_url)
                # Lấy video có chất lượng tốt nhất
                video_stream = yt.streams.get_highest_resolution()
                save_path = "your_directory"  # Thay thế bằng thư mục lưu trữ thực tế trên hệ thống của bạn
                video_stream.download(output_path=save_path)
                print("Video đã được tải xuống thành công.")
            except Exception as e:
                print(f"Lỗi: {e}")
        else:
            print("Không thể tải video từ trang web khác YouTube.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BrowserWindow()
    sys.exit(app.exec_())
