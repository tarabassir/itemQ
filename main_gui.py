#!/usr/bin/python3
import sys
from PyQt4 import QtGui, QtCore
from rbfn_gui import Ui_main_window
import datetime
import trained

rbfn_instance = trained.RBFN(195, 2)
#rbfn_instance.train()


class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_main_window()
        self.ui.setupUi(self)
        self.ui.item_dd.addItem('Chicken')	
        self.ui.item_dd.addItem('Milk')
        self.ui.item_dd.addItem('Beef')
        self.ui.item_dd.addItem('Brocolli')
        self.ui.quantity_dd.addItem('1')
        self.ui.quantity_dd.addItem('2')
        self.ui.quantity_dd.addItem('3')
        self.ui.quantity_dd.addItem('4')
        self.ui.quantity_dd.addItem('5')
        self.ui.quantity_dd.addItem('6')
        self.ui.quantity_dd.addItem('7')
        self.ui.quantity_dd.addItem('8')
        self.ui.quantity_dd.addItem('9')
        self.ui.quantity_dd.addItem('10')
        self.ui.consumer_count_dd.addItem('1')
        self.ui.consumer_count_dd.addItem('2')
        self.ui.consumer_count_dd.addItem('3')
        self.ui.consumer_count_dd.addItem('4')
        self.ui.consumer_count_dd.addItem('5')
        self.ui.consumer_count_dd.addItem('6')

        self.ui.item_table.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

        self.__row = 0

        QtCore.QObject.connect(self.ui.store_button, QtCore.SIGNAL("clicked()"),self.store)


    def store(self):
        self.ui.item_table.insertRow(self.__row)
        self.ui.item_table.setItem(self.__row, 0, QtGui.QTableWidgetItem(self.ui.item_dd.currentText()))
        self.ui.item_table.setItem(self.__row, 1, QtGui.QTableWidgetItem(self.ui.quantity_dd.currentText()))
        self.ui.item_table.setItem(self.__row, 2, QtGui.QTableWidgetItem(self.ui.consumer_count_dd.currentText()))

        date = datetime.datetime.today()
        date_string = str(date.month) + "/" + str(date.day) + "/" + \
                str(date.year)
        self.ui.item_table.setItem(self.__row, 3, QtGui.QTableWidgetItem(date_string))
        item_name = self.ui.item_dd.currentIndex() + 1
        item_quantity = self.ui.quantity_dd.currentIndex() + 1
        consumer_count = self.ui.consumer_count_dd.currentIndex() + 1
        day = datetime.datetime.now().timetuple().tm_yday
	
        inputs = [[item_name, item_quantity, consumer_count, day]]
        output = rbfn_instance.predict(inputs)
        self.ui.item_table.setItem(self.__row, 4, QtGui.QTableWidgetItem(str(output[0][0])))

        self.__row += 1

	
	
        
	

if __name__ == "__main__":


    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
