# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RCchannelsetupWindow.ui'
#
# Created: Tue Mar 26 16:51:39 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(749, 557)
        self.cancel = QtGui.QPushButton(Form)
        self.cancel.setGeometry(QtCore.QRect(190, 500, 101, 31))
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 10, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(90, 70, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(90, 130, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(90, 190, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(90, 250, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setScaledContents(False)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(90, 310, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setScaledContents(False)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(90, 370, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setScaledContents(False)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(90, 430, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setScaledContents(False)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.commLog = QtGui.QTextBrowser(Form)
        self.commLog.setGeometry(QtCore.QRect(380, 20, 341, 461))
        self.commLog.setFrameShadow(QtGui.QFrame.Sunken)
        self.commLog.setObjectName(_fromUtf8("commLog"))
        self.start = QtGui.QPushButton(Form)
        self.start.setGeometry(QtCore.QRect(70, 500, 100, 31))
        self.start.setObjectName(_fromUtf8("start"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "RC channel setup", None))
        self.cancel.setText(_translate("Form", "Cancel", None))
        self.label.setText(_translate("Form", "Roll", None))
        self.label_2.setText(_translate("Form", "Pitch", None))
        self.label_3.setText(_translate("Form", "Yaw", None))
        self.label_4.setText(_translate("Form", "Throttle", None))
        self.label_5.setText(_translate("Form", "Mode", None))
        self.label_6.setText(_translate("Form", "Aux1", None))
        self.label_7.setText(_translate("Form", "Aux2", None))
        self.label_8.setText(_translate("Form", "Aux3", None))
        self.start.setText(_translate("Form", "Start", None))
