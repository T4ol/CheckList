# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WindowForAddTask.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(264, 300)
        self.buttonAddTask = QPushButton(Form)
        self.buttonAddTask.setObjectName(u"buttonAddTask")
        self.buttonAddTask.setGeometry(QRect(10, 260, 81, 31))
        self.buttonCancelTask = QPushButton(Form)
        self.buttonCancelTask.setObjectName(u"buttonCancelTask")
        self.buttonCancelTask.setGeometry(QRect(180, 260, 71, 31))
        self.lineForNameTask = QLineEdit(Form)
        self.lineForNameTask.setObjectName(u"lineForNameTask")
        self.lineForNameTask.setGeometry(QRect(10, 20, 241, 91))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.buttonAddTask.setText(QCoreApplication.translate("Form", u"Add", None))
        self.buttonCancelTask.setText(QCoreApplication.translate("Form", u"Cancel", None))
    # retranslateUi

