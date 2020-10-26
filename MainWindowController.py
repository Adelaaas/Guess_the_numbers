from PyQt5 import QtWidgets


from MainWindow import Ui_MainWindow
import sys


class MainWindowController(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindowController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.startPushButton.clicked.connect(self.startAnalyse)
        self.ui.kmeansPushButton.clicked.connect(self.kmeansClustering)
        self.ui.graphResultPushButton.clicked.connect(self.graphResult)

    def startAnalyse(self):
        print('start analyse')
        #тут функция из файла PlaceNember

    def kmeansClustering(self):
        print('kmeans clustering')
        #тут функция из файла clusters

    def graphResult(self):
        print('graph result')
        #тут функция из файла clusters


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MainWindowController()
    application.show()

    sys.exit(app.exec())
