# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pyvisa
import csv
import time
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 500)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 10, 121, 20))
        self.label.setObjectName("label")
        # self.label_1 = QtWidgets.QLabel(Dialog)
        # self.label_1.setGeometry(QtCore.QRect(350, 60, 121, 20))
        # self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(28, 60, 121, 20))
        self.label_2.setObjectName("label_2")

        self.radio_button = QtWidgets.QRadioButton(Dialog)
        self.radio_button.setGeometry(QtCore.QRect(350, 10, 121, 20))
        self.radio_button_1 = QtWidgets.QRadioButton(Dialog)
        self.radio_button_1.setGeometry(QtCore.QRect(450, 100, 121, 20))
        self.radio_button_2 = QtWidgets.QRadioButton(Dialog)
        self.radio_button_2.setGeometry(QtCore.QRect(450, 120, 121, 20))
        self.radio_button_3 = QtWidgets.QRadioButton(Dialog)
        self.radio_button_3.setGeometry(QtCore.QRect(450, 140, 121, 20))






        self.SpinBox = QtWidgets.QSpinBox(Dialog)
        self.SpinBox.setGeometry(QtCore.QRect(420, 10, 121, 20))

        self.toolButton = QtWidgets.QToolButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(80, 440, 61, 21))
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(Dialog)
        self.toolButton_2.setGeometry(QtCore.QRect(200, 440, 61, 21))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(Dialog)
        self.toolButton_3.setGeometry(QtCore.QRect(310, 100, 80, 30))
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4 = QtWidgets.QToolButton(Dialog)
        self.toolButton_4.setGeometry(QtCore.QRect(28, 100, 80, 30))
        self.toolButton_4.setObjectName("toolButton_3")



        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(100, 10, 161, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_1 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_1.setGeometry(QtCore.QRect(350, 60, 240, 20))
        self.lineEdit_1.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 60, 161, 20))
        self.lineEdit_2.setObjectName("lineEdit")


        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(50, 290, 500, 141))
        self.textEdit.setObjectName("textEdit")




        self.retranslateUi(Dialog)
        # self.toolButton_3.clicked.connect(self.duoci)
        self.toolButton.clicked.connect(self.danci)
        self.toolButton_2.clicked.connect(self.textEdit.clear)
        self.toolButton_3.clicked.connect(self.chushi)
        self.toolButton_4.clicked.connect(self.huoqu)


        QtCore.QMetaObject.connectSlotsByName(Dialog)

#定义控件的文本信息
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("test", "E4980专用自动测试软件"))
        self.label.setText(_translate("Dialog", "输入批号"))
        # self.label_1.setText(_translate("Dialog", "输入测试次数"))
        self.label_2.setText(_translate("Dialog", "测试延时时间"))
        self.toolButton.setText(_translate("Dialog", "测试"))
        self.toolButton_2.setText(_translate("Dialog", "清除"))
        self.toolButton_3.setText(_translate("Dialog", "初始化仪表"))
        self.radio_button.setText(_translate("Dialog", "多次测试"))
        self.radio_button_1.setText(_translate("Dialog", "120HZ"))
        self.radio_button_2.setText(_translate("Dialog", "1KHZ"))
        self.radio_button_3.setText(_translate("Dialog", "1MHZ"))
        self.lineEdit_1.setText(_translate("Dialog", "输入设备通讯地址"))
        self.toolButton_4.setText(_translate("Dialog", "获取地址"))


    def danci(self):
        if self.radio_button.isChecked():
            def perform_tests(instrument, test_count):
                """
                执行测试并将结果保存到CSV文件中
                :param instrument: 已通过pyvisa连接的仪器资源管理器
                :param test_count: 测试次数
                """
                # 打开CSV文件进行写入
                with open(pihao + '.csv', 'w', newline='') as csvfile:
                    csv.writer(csvfile)
                    writer = csv.writer(csvfile)
                    writer.writerow(['电容值', '损耗'])  # 写入标题行
                    for test_num in range(1, test_count + 1):
                        # 执行测试并获取读数
                        instrument.write("TRIG")
                        time.sleep(yanshi)
                        reading = instrument.query('FETCH?')
                        self.textEdit.append(reading)
                        writer.writerow(reading.split(','))  # 写入测试结果

            rm = pyvisa.ResourceManager()
            dizhi = self.lineEdit_1.text()
            instrument = rm.open_resource(f'{dizhi}')
            instrument.write(f':TRIGger:SOURce BUS')
            test_count1 = self.SpinBox.text()
            test_count = int(test_count1)
            # 执行测试
            yanshi1 = self.lineEdit_2.text()
            yanshi = float(yanshi1)  # 转换为整数型
            pihao = self.lineEdit.text()
            perform_tests(instrument, test_count)

            self.textEdit.append(f"CSV文件已生成: {pihao}.csv")
        else:
            rm = pyvisa.ResourceManager()
            dizhi = self.lineEdit_1.text()
            instrument = rm.open_resource(f'{dizhi}')
            instrument.write(f':TRIGger:SOURce BUS')
            instrument.write("TRIG")
            reading = instrument.query('FETCH?')
            self.textEdit.append(reading)


    def chushi(self):
        rm = pyvisa.ResourceManager()
        dizhi = self.lineEdit_1.text()
        instrument = rm.open_resource(f'{dizhi}')
        fanhui = instrument.query('*IDN?')
        self.textEdit.append(fanhui)




    def huoqu(self):
        try:
            # 创建PyVISA资源管理器
            rm = pyvisa.ResourceManager()

            # 获取所有可用的设备地址
            resources = rm.list_resources()

            # 筛选出网口和串口设备地址
            network_addresses = [addr for addr in resources if 'TCPIP' in addr]
            serial_addresses = [addr for addr in resources if 'ASRL' in addr or 'COM' in addr]

            # 显示设备地址
            self.textEdit.append("网口设备地址：")
            for addr in network_addresses:
                self.textEdit.append(addr)
            self.textEdit.append("\n串口设备地址：")
            for addr in serial_addresses:
                self.textEdit.append(addr)

        except pyvisa.VisaIOError as e:
            self.textEdit.append(f"获取设备地址时出错: {e}")
    #
    # def pinglv(self):
    #     if self.radio_button_1.isChecked():





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #QMainWindow窗口也带有最大化最小化和退出，另外窗口最下面有statusbar可以显示设置的消息
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
