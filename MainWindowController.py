from PyQt5 import QtWidgets
from MainWindow import Ui_MainWindow
import sys

from Get_numbers_v2 import get_numbers
from PlaceNember import getPlaceNumberList
import clusters


class MainWindowController(QtWidgets.QMainWindow):
    P = list()
    N = list()
    numbers = list()
    dop_number = int()

    def __init__(self):
        super(MainWindowController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.startPushButton.clicked.connect(self.startAnalyse)
        self.ui.kmeansPushButton.clicked.connect(self.kmeansClustering)
        self.ui.graphResultPushButton.clicked.connect(self.graphResult)

    def startAnalyse(self):
        del self.P[:]
        del self.N[:]
        del self.numbers[:]
        # print('start analyse')
        self.dop_number = self.ui.dopNumberSpinBox.text()
        self.numbers = get_numbers(int(self.ui.countSpinBox.text()))
        self.P, self.N = getPlaceNumberList(self.numbers, self.dop_number)
        self.ui.kmeansPushButton.setEnabled(True)
        self.ui.graphResultPushButton.setEnabled(True)
        print('P = ', self.P)
        print('N = ', self.N)
        print('Numbers = ', self.numbers)
        #тут функция из файла PlaceNember

    def kmeansClustering(self):
        print('kmeans clustering')
        cluster0, cluster1, cluster2, cluster3 = clusters.clustering(self.numbers, self.dop_number)
        if cluster0.empty:
            print('do exeption')
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Kmeans warning")
            msg.setInformativeText("Не удалось поделить выборку на 4 кластера")
            msg.setWindowTitle("Guess Numbers warning")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        else:
            clusters.visualization_clusters(cluster0, cluster1, cluster2, cluster3)
        #тут функция из файла clusters

    def graphResult(self):
        print('graph result')

        #тут функция из файла clusters


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MainWindowController()
    application.show()

    sys.exit(app.exec())
