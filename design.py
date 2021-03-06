# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CustomRPC(object):
    def setupUi(self, CustomRPC):
        CustomRPC.setObjectName("CustomRPC")
        CustomRPC.resize(521, 474)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../home/kurozero/Downloads/Wind.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CustomRPC.setWindowIcon(icon)
        CustomRPC.setWindowOpacity(1.0)
        CustomRPC.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(238, 238, 236);")
        self.centralwidget = QtWidgets.QWidget(CustomRPC)
        self.centralwidget.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"color: rgb(238, 238, 236);")
        self.centralwidget.setObjectName("centralwidget")
        self.update_rpc_btn = QtWidgets.QPushButton(self.centralwidget)
        self.update_rpc_btn.setEnabled(False)
        self.update_rpc_btn.setGeometry(QtCore.QRect(150, 400, 171, 29))
        self.update_rpc_btn.setObjectName("update_rpc_btn")
        self.details_tb = QtWidgets.QLineEdit(self.centralwidget)
        self.details_tb.setGeometry(QtCore.QRect(20, 50, 481, 29))
        self.details_tb.setToolTip("")
        self.details_tb.setMaxLength(127)
        self.details_tb.setObjectName("details_tb")
        self.state_tb = QtWidgets.QLineEdit(self.centralwidget)
        self.state_tb.setGeometry(QtCore.QRect(20, 90, 481, 29))
        self.state_tb.setToolTip("")
        self.state_tb.setMaxLength(127)
        self.state_tb.setObjectName("state_tb")
        self.appid_tb = QtWidgets.QLineEdit(self.centralwidget)
        self.appid_tb.setGeometry(QtCore.QRect(20, 280, 481, 29))
        self.appid_tb.setToolTip("")
        self.appid_tb.setMaxLength(18)
        self.appid_tb.setObjectName("appid_tb")
        self.id_secret_lbl = QtWidgets.QLabel(self.centralwidget)
        self.id_secret_lbl.setGeometry(QtCore.QRect(20, 250, 131, 17))
        self.id_secret_lbl.setObjectName("id_secret_lbl")
        self.rpc_data_lbl = QtWidgets.QLabel(self.centralwidget)
        self.rpc_data_lbl.setGeometry(QtCore.QRect(20, 20, 141, 17))
        self.rpc_data_lbl.setObjectName("rpc_data_lbl")
        self.largeimgname_tb = QtWidgets.QLineEdit(self.centralwidget)
        self.largeimgname_tb.setGeometry(QtCore.QRect(20, 320, 481, 29))
        self.largeimgname_tb.setMaxLength(31)
        self.largeimgname_tb.setObjectName("largeimgname_tb")
        self.smallimgname_tb = QtWidgets.QLineEdit(self.centralwidget)
        self.smallimgname_tb.setGeometry(QtCore.QRect(20, 360, 481, 29))
        self.smallimgname_tb.setMaxLength(31)
        self.smallimgname_tb.setObjectName("smallimgname_tb")
        self.largeimgtext_tb = QtWidgets.QLineEdit(self.centralwidget)
        self.largeimgtext_tb.setGeometry(QtCore.QRect(20, 130, 481, 29))
        self.largeimgtext_tb.setMaxLength(127)
        self.largeimgtext_tb.setObjectName("largeimgtext_tb")
        self.smallimgtext_tb = QtWidgets.QLineEdit(self.centralwidget)
        self.smallimgtext_tb.setGeometry(QtCore.QRect(20, 170, 481, 29))
        self.smallimgtext_tb.setMaxLength(127)
        self.smallimgtext_tb.setObjectName("smallimgtext_tb")
        self.timer_cb = QtWidgets.QCheckBox(self.centralwidget)
        self.timer_cb.setGeometry(QtCore.QRect(20, 210, 98, 22))
        self.timer_cb.setObjectName("timer_cb")
        self.stop_rpc_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_rpc_btn.setEnabled(False)
        self.stop_rpc_btn.setGeometry(QtCore.QRect(330, 400, 171, 29))
        self.stop_rpc_btn.setAutoDefault(False)
        self.stop_rpc_btn.setDefault(False)
        self.stop_rpc_btn.setFlat(False)
        self.stop_rpc_btn.setObjectName("stop_rpc_btn")
        CustomRPC.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CustomRPC)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 521, 27))
        self.menubar.setObjectName("menubar")
        CustomRPC.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CustomRPC)
        self.statusbar.setObjectName("statusbar")
        CustomRPC.setStatusBar(self.statusbar)

        self.retranslateUi(CustomRPC)
        QtCore.QMetaObject.connectSlotsByName(CustomRPC)

    def retranslateUi(self, CustomRPC):
        _translate = QtCore.QCoreApplication.translate
        CustomRPC.setWindowTitle(_translate("CustomRPC", "Custom RPC"))
        self.update_rpc_btn.setText(_translate("CustomRPC", "Update Rich Presence"))
        self.details_tb.setPlaceholderText(_translate("CustomRPC", "details"))
        self.state_tb.setPlaceholderText(_translate("CustomRPC", "state"))
        self.appid_tb.setPlaceholderText(_translate("CustomRPC", "app id"))
        self.id_secret_lbl.setText(_translate("CustomRPC", "Custom:"))
        self.rpc_data_lbl.setText(_translate("CustomRPC", "Rich Presence data:"))
        self.largeimgname_tb.setPlaceholderText(_translate("CustomRPC", "large image name"))
        self.smallimgname_tb.setPlaceholderText(_translate("CustomRPC", "small image name"))
        self.largeimgtext_tb.setPlaceholderText(_translate("CustomRPC", "large image text"))
        self.smallimgtext_tb.setPlaceholderText(_translate("CustomRPC", "small image text"))
        self.timer_cb.setText(_translate("CustomRPC", "Timer"))
        self.stop_rpc_btn.setText(_translate("CustomRPC", "Stop Rich Presence"))

