from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
import sys, browser

ui = tray_icon = None

def add_tab(url = "", label = "Blank"):
	browser = QtWebEngineWidgets.QWebEngineView()
	browser.setUrl(QtCore.QUrl(url))
	ui.tabs.setCurrentIndex(ui.tabs.addTab(browser, label))

def hide():
	MainWindow.hide()
	tray_icon.showMessage(
		"Duino-Coin Browser",
		"Chương trình đã ẩn, tác vụ vẫn đang chạy ngầm",
		QtWidgets.QSystemTrayIcon.Information,
		2000
	)

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = browser.Ui_MainWindow()
ui.setupUi(MainWindow)
ui.button.clicked.connect(hide)

tray_icon = QtWidgets.QSystemTrayIcon(MainWindow)
icon = QtGui.QIcon()
icon.addPixmap(QtGui.QPixmap(":/logo/Resources/duco.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
tray_icon.setIcon(icon)

show_action = QtWidgets.QAction("Hiện cửa sổ")
quit_action = QtWidgets.QAction("Thoát")
show_action.triggered.connect(lambda: MainWindow.show())
quit_action.triggered.connect(app.quit)

tray_menu = QtWidgets.QMenu()
tray_menu.addAction(show_action)
tray_menu.addAction(quit_action)
tray_icon.setContextMenu(tray_menu)
tray_icon.show()

urls_data = open("urls.txt", "r")
urls = urls_data.readlines()
i = 1
for url in urls:
	add_tab(url, "Miner %d" % i)
	i += 1

MainWindow.show()
sys.exit(app.exec_())
