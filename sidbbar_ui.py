# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sidbbar.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(995, 647)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.menu = QPushButton(self.widget)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"border:none;")
        icon = QIcon()
        icon.addFile(u":/images/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu.setIcon(icon)
        self.menu.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.menu)

        self.acc = QPushButton(self.widget)
        self.acc.setObjectName(u"acc")
        icon1 = QIcon()
        icon1.addFile(u":/images/acceu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.acc.setIcon(icon1)
        self.acc.setCheckable(True)
        self.acc.setAutoExclusive(True)

        self.horizontalLayout_4.addWidget(self.acc)

        self.horizontalSpacer_2 = QSpacerItem(210, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton_16 = QPushButton(self.widget)
        self.pushButton_16.setObjectName(u"pushButton_16")
        icon2 = QIcon()
        icon2.addFile(u":/images/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_16.setIcon(icon2)

        self.horizontalLayout.addWidget(self.pushButton_16)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(210, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.p = QPushButton(self.widget)
        self.p.setObjectName(u"p")
        self.p.setMinimumSize(QSize(20, 20))
        self.p.setMaximumSize(QSize(20, 20))
        self.p.setStyleSheet(u"border:none;")
        icon3 = QIcon()
        icon3.addFile(u":/images/image.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.p.setIcon(icon3)
        self.p.setCheckable(True)
        self.p.setAutoExclusive(True)

        self.horizontalLayout_4.addWidget(self.p)


        self.verticalLayout_5.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.profile_page = QWidget()
        self.profile_page.setObjectName(u"profile_page")
        self.label_4 = QLabel(self.profile_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 90, 331, 61))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(0, 85, 255);")
        self.layoutWidget = QWidget(self.profile_page)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 180, 671, 181))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_10.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_10)

        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_11)

        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_12)


        self.horizontalLayout_5.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.name = QLineEdit(self.layoutWidget)
        self.name.setObjectName(u"name")

        self.verticalLayout_7.addWidget(self.name)

        self.email_p = QLineEdit(self.layoutWidget)
        self.email_p.setObjectName(u"email_p")

        self.verticalLayout_7.addWidget(self.email_p)

        self.password_p = QLineEdit(self.layoutWidget)
        self.password_p.setObjectName(u"password_p")
        self.password_p.setMinimumSize(QSize(10, 10))

        self.verticalLayout_7.addWidget(self.password_p)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.modname = QPushButton(self.layoutWidget)
        self.modname.setObjectName(u"modname")
        self.modname.setFont(font1)

        self.verticalLayout_8.addWidget(self.modname)

        self.modemail = QPushButton(self.layoutWidget)
        self.modemail.setObjectName(u"modemail")
        self.modemail.setFont(font1)

        self.verticalLayout_8.addWidget(self.modemail)

        self.modpass = QPushButton(self.layoutWidget)
        self.modpass.setObjectName(u"modpass")
        self.modpass.setFont(font1)

        self.verticalLayout_8.addWidget(self.modpass)


        self.horizontalLayout_5.addLayout(self.verticalLayout_8)

        self.stackedWidget.addWidget(self.profile_page)
        self.automatique_page = QWidget()
        self.automatique_page.setObjectName(u"automatique_page")
        self.label_5 = QLabel(self.automatique_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 40, 451, 111))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.autoactvate = QPushButton(self.automatique_page)
        self.autoactvate.setObjectName(u"autoactvate")
        self.autoactvate.setGeometry(QRect(290, 450, 131, 41))
        self.autoactvate.setFont(font1)
        self.stop = QPushButton(self.automatique_page)
        self.stop.setObjectName(u"stop")
        self.stop.setGeometry(QRect(310, 510, 93, 28))
        self.stop.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.stop.setCheckable(True)
        self.label_13 = QLabel(self.automatique_page)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(60, 190, 111, 31))
        self.label_13.setFont(font1)
        self.layoutWidget_2 = QWidget(self.automatique_page)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(410, 220, 251, 221))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_18 = QLabel(self.layoutWidget_2)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_11.addWidget(self.label_18)

        self.label_19 = QLabel(self.layoutWidget_2)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_11.addWidget(self.label_19)

        self.label_20 = QLabel(self.layoutWidget_2)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_11.addWidget(self.label_20)

        self.label_21 = QLabel(self.layoutWidget_2)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_11.addWidget(self.label_21)


        self.horizontalLayout_7.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.checkBox_5 = QCheckBox(self.layoutWidget_2)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.verticalLayout_12.addWidget(self.checkBox_5)

        self.checkBox_6 = QCheckBox(self.layoutWidget_2)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.verticalLayout_12.addWidget(self.checkBox_6)

        self.checkBox_7 = QCheckBox(self.layoutWidget_2)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.verticalLayout_12.addWidget(self.checkBox_7)

        self.checkBox_8 = QCheckBox(self.layoutWidget_2)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.verticalLayout_12.addWidget(self.checkBox_8)


        self.horizontalLayout_7.addLayout(self.verticalLayout_12)

        self.label_22 = QLabel(self.automatique_page)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(420, 190, 111, 31))
        self.label_22.setFont(font1)
        self.layoutWidget1 = QWidget(self.automatique_page)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(60, 220, 251, 221))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_14 = QLabel(self.layoutWidget1)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_9.addWidget(self.label_14)

        self.label_15 = QLabel(self.layoutWidget1)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_9.addWidget(self.label_15)

        self.label_16 = QLabel(self.layoutWidget1)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_9.addWidget(self.label_16)

        self.label_17 = QLabel(self.layoutWidget1)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_9.addWidget(self.label_17)


        self.horizontalLayout_6.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.checkBox = QCheckBox(self.layoutWidget1)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_10.addWidget(self.checkBox)

        self.checkBox_3 = QCheckBox(self.layoutWidget1)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_10.addWidget(self.checkBox_3)

        self.checkBox_2 = QCheckBox(self.layoutWidget1)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_10.addWidget(self.checkBox_2)

        self.checkBox_4 = QCheckBox(self.layoutWidget1)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout_10.addWidget(self.checkBox_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_10)

        self.stackedWidget.addWidget(self.automatique_page)
        self.manuel_page = QWidget()
        self.manuel_page.setObjectName(u"manuel_page")
        self.label_6 = QLabel(self.manuel_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 20, 451, 111))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.label_28 = QLabel(self.manuel_page)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(50, 190, 111, 31))
        self.label_28.setFont(font1)
        self.layoutWidget_5 = QWidget(self.manuel_page)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(50, 240, 251, 221))
        self.horizontalLayout_11 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_34 = QLabel(self.layoutWidget_5)
        self.label_34.setObjectName(u"label_34")

        self.verticalLayout_18.addWidget(self.label_34)

        self.label_35 = QLabel(self.layoutWidget_5)
        self.label_35.setObjectName(u"label_35")

        self.verticalLayout_18.addWidget(self.label_35)

        self.label_36 = QLabel(self.layoutWidget_5)
        self.label_36.setObjectName(u"label_36")

        self.verticalLayout_18.addWidget(self.label_36)

        self.label_37 = QLabel(self.layoutWidget_5)
        self.label_37.setObjectName(u"label_37")

        self.verticalLayout_18.addWidget(self.label_37)


        self.horizontalLayout_11.addLayout(self.verticalLayout_18)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.checkBox_13 = QCheckBox(self.layoutWidget_5)
        self.checkBox_13.setObjectName(u"checkBox_13")

        self.verticalLayout_19.addWidget(self.checkBox_13)

        self.checkBox_14 = QCheckBox(self.layoutWidget_5)
        self.checkBox_14.setObjectName(u"checkBox_14")

        self.verticalLayout_19.addWidget(self.checkBox_14)

        self.checkBox_15 = QCheckBox(self.layoutWidget_5)
        self.checkBox_15.setObjectName(u"checkBox_15")

        self.verticalLayout_19.addWidget(self.checkBox_15)

        self.checkBox_16 = QCheckBox(self.layoutWidget_5)
        self.checkBox_16.setObjectName(u"checkBox_16")

        self.verticalLayout_19.addWidget(self.checkBox_16)


        self.horizontalLayout_11.addLayout(self.verticalLayout_19)

        self.layoutWidget_4 = QWidget(self.manuel_page)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(390, 240, 251, 221))
        self.horizontalLayout_10 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_29 = QLabel(self.layoutWidget_4)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_16.addWidget(self.label_29)

        self.label_30 = QLabel(self.layoutWidget_4)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_16.addWidget(self.label_30)

        self.label_31 = QLabel(self.layoutWidget_4)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_16.addWidget(self.label_31)

        self.label_32 = QLabel(self.layoutWidget_4)
        self.label_32.setObjectName(u"label_32")

        self.verticalLayout_16.addWidget(self.label_32)


        self.horizontalLayout_10.addLayout(self.verticalLayout_16)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.checkBox_9 = QCheckBox(self.layoutWidget_4)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.verticalLayout_17.addWidget(self.checkBox_9)

        self.checkBox_10 = QCheckBox(self.layoutWidget_4)
        self.checkBox_10.setObjectName(u"checkBox_10")

        self.verticalLayout_17.addWidget(self.checkBox_10)

        self.checkBox_11 = QCheckBox(self.layoutWidget_4)
        self.checkBox_11.setObjectName(u"checkBox_11")

        self.verticalLayout_17.addWidget(self.checkBox_11)

        self.checkBox_12 = QCheckBox(self.layoutWidget_4)
        self.checkBox_12.setObjectName(u"checkBox_12")

        self.verticalLayout_17.addWidget(self.checkBox_12)


        self.horizontalLayout_10.addLayout(self.verticalLayout_17)

        self.label_33 = QLabel(self.manuel_page)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(390, 190, 111, 31))
        self.label_33.setFont(font1)
        self.layoutWidget2 = QWidget(self.manuel_page)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(0, 490, 721, 35))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.place = QPushButton(self.layoutWidget2)
        self.place.setObjectName(u"place")
        self.place.setFont(font1)

        self.horizontalLayout_8.addWidget(self.place)

        self.evacute = QPushButton(self.layoutWidget2)
        self.evacute.setObjectName(u"evacute")
        self.evacute.setFont(font1)

        self.horizontalLayout_8.addWidget(self.evacute)

        self.take = QPushButton(self.layoutWidget2)
        self.take.setObjectName(u"take")
        self.take.setFont(font1)

        self.horizontalLayout_8.addWidget(self.take)

        self.pompage = QPushButton(self.layoutWidget2)
        self.pompage.setObjectName(u"pompage")
        self.pompage.setFont(font1)
        self.pompage.setStyleSheet(u"color: rgb(170, 85, 255);")

        self.horizontalLayout_8.addWidget(self.pompage)

        self.home = QPushButton(self.layoutWidget2)
        self.home.setObjectName(u"home")
        self.home.setFont(font1)
        self.home.setStyleSheet(u"color: rgb(0, 170, 127);")

        self.horizontalLayout_8.addWidget(self.home)

        self.stackedWidget.addWidget(self.manuel_page)
        self.notifications_page = QWidget()
        self.notifications_page.setObjectName(u"notifications_page")
        self.label_7 = QLabel(self.notifications_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 30, 251, 111))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.affichage = QTableWidget(self.notifications_page)
        if (self.affichage.columnCount() < 2):
            self.affichage.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.affichage.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.affichage.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.affichage.rowCount() < 1):
            self.affichage.setRowCount(1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.affichage.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.affichage.setItem(0, 0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.affichage.setItem(0, 1, __qtablewidgetitem4)
        self.affichage.setObjectName(u"affichage")
        self.affichage.setGeometry(QRect(50, 140, 281, 211))
        self.historic = QPushButton(self.notifications_page)
        self.historic.setObjectName(u"historic")
        self.historic.setGeometry(QRect(280, 440, 111, 28))
        self.historic.setFont(font1)
        self.stackedWidget.addWidget(self.notifications_page)
        self.sitting_page = QWidget()
        self.sitting_page.setObjectName(u"sitting_page")
        self.label_25 = QLabel(self.sitting_page)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(40, 50, 291, 71))
        self.label_25.setFont(font)
        self.label_25.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.label_8 = QLabel(self.sitting_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(50, 155, 481, 31))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.label_8.setFont(font2)
        self.posrobot = QLineEdit(self.sitting_page)
        self.posrobot.setObjectName(u"posrobot")
        self.posrobot.setGeometry(QRect(40, 200, 511, 41))
        self.submit = QPushButton(self.sitting_page)
        self.submit.setObjectName(u"submit")
        self.submit.setGeometry(QRect(590, 200, 93, 41))
        self.submit.setStyleSheet(u"background-color: rgb(0, 170, 127);")
        self.submit.setCheckable(True)
        self.name_id = QLineEdit(self.sitting_page)
        self.name_id.setObjectName(u"name_id")
        self.name_id.setGeometry(QRect(50, 370, 201, 41))
        self.add = QPushButton(self.sitting_page)
        self.add.setObjectName(u"add")
        self.add.setGeometry(QRect(260, 430, 93, 41))
        self.add.setStyleSheet(u"background-color: rgb(0, 170, 127);")
        self.add.setCheckable(True)
        self.label_23 = QLabel(self.sitting_page)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(50, 270, 481, 31))
        self.label_23.setFont(font2)
        self.position_id = QLineEdit(self.sitting_page)
        self.position_id.setObjectName(u"position_id")
        self.position_id.setGeometry(QRect(350, 370, 201, 41))
        self.label_24 = QLabel(self.sitting_page)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(50, 320, 141, 31))
        self.label_24.setFont(font2)
        self.label_26 = QLabel(self.sitting_page)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(350, 320, 141, 31))
        self.label_26.setFont(font2)
        self.stackedWidget.addWidget(self.sitting_page)
        self.help_page = QWidget()
        self.help_page.setObjectName(u"help_page")
        self.label_9 = QLabel(self.help_page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 10, 721, 521))
        font3 = QFont()
        font3.setPointSize(8)
        font3.setBold(True)
        self.label_9.setFont(font3)
        self.stackedWidget.addWidget(self.help_page)
        self.user_page = QWidget()
        self.user_page.setObjectName(u"user_page")
        self.user_firstname = QLineEdit(self.user_page)
        self.user_firstname.setObjectName(u"user_firstname")
        self.user_firstname.setGeometry(QRect(100, 110, 311, 41))
        self.user_lastname = QLineEdit(self.user_page)
        self.user_lastname.setObjectName(u"user_lastname")
        self.user_lastname.setGeometry(QRect(100, 190, 311, 41))
        self.user_email = QLineEdit(self.user_page)
        self.user_email.setObjectName(u"user_email")
        self.user_email.setGeometry(QRect(100, 270, 311, 41))
        self.label_27 = QLabel(self.user_page)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(90, 80, 131, 21))
        self.label_38 = QLabel(self.user_page)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(90, 160, 121, 21))
        self.label_39 = QLabel(self.user_page)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(90, 235, 131, 31))
        self.user_cin = QLineEdit(self.user_page)
        self.user_cin.setObjectName(u"user_cin")
        self.user_cin.setGeometry(QRect(100, 360, 311, 41))
        self.label_40 = QLabel(self.user_page)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(90, 320, 131, 31))
        self.change = QPushButton(self.user_page)
        self.change.setObjectName(u"change")
        self.change.setGeometry(QRect(280, 450, 121, 31))
        self.change.setFont(font2)
        self.change.setStyleSheet(u"background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.change.setCheckable(True)
        self.change.setAutoExclusive(True)
        self.stackedWidget.addWidget(self.user_page)
        self.first = QWidget()
        self.first.setObjectName(u"first")
        self.label_41 = QLabel(self.first)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(0, 0, 831, 571))
        self.label_41.setStyleSheet(u"border-image:url(:/images/robot.jpg);\n"
"border-radius:20px;")
        self.label_42 = QLabel(self.first)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(310, 40, 231, 41))
        self.label_42.setFont(font1)
        self.label_42.setStyleSheet(u"background-color: rgba(200, 200, 200, 128); /* Gris avec 50% de transparence */\n"
"border: 2px solid rgba(0, 0, 255, 128); /* Bleu avec 50% de transparence */")
        self.stackedWidget.addWidget(self.first)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)

        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(31, 149, 239);\n"
"}\n"
"QPushButton{\n"
"	color:white;\n"
"	border:none;\n"
"	height:30px;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:checked{\n"
"background-color:#f5fafe;\n"
"color:#f5e4ff;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 40))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/images/king.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.profile1 = QPushButton(self.icon_only_widget)
        self.profile1.setObjectName(u"profile1")
        icon4 = QIcon()
        icon4.addFile(u":/images/profile.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.profile1.setIcon(icon4)
        self.profile1.setCheckable(True)
        self.profile1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.profile1)

        self.auto1 = QPushButton(self.icon_only_widget)
        self.auto1.setObjectName(u"auto1")
        icon5 = QIcon()
        icon5.addFile(u":/images/auto.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.auto1.setIcon(icon5)
        self.auto1.setCheckable(True)
        self.auto1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.auto1)

        self.man1 = QPushButton(self.icon_only_widget)
        self.man1.setObjectName(u"man1")
        icon6 = QIcon()
        icon6.addFile(u":/images/manuel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.man1.setIcon(icon6)
        self.man1.setCheckable(True)
        self.man1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.man1)

        self.noti1 = QPushButton(self.icon_only_widget)
        self.noti1.setObjectName(u"noti1")
        icon7 = QIcon()
        icon7.addFile(u":/images/noti.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.noti1.setIcon(icon7)
        self.noti1.setCheckable(True)
        self.noti1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.noti1)

        self.sitt1 = QPushButton(self.icon_only_widget)
        self.sitt1.setObjectName(u"sitt1")
        icon8 = QIcon()
        icon8.addFile(u":/images/sttin.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.sitt1.setIcon(icon8)
        self.sitt1.setCheckable(True)
        self.sitt1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.sitt1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 213, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.help1 = QPushButton(self.icon_only_widget)
        self.help1.setObjectName(u"help1")
        icon9 = QIcon()
        icon9.addFile(u":/images/help.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.help1.setIcon(icon9)
        self.help1.setCheckable(True)
        self.help1.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.help1)

        self.cl1 = QPushButton(self.icon_only_widget)
        self.cl1.setObjectName(u"cl1")
        icon10 = QIcon()
        icon10.addFile(u":/images/log.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cl1.setIcon(icon10)
        self.cl1.setCheckable(True)

        self.verticalLayout_3.addWidget(self.cl1)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(31, 149, 239);\n"
"}\n"
"QPushButton{\n"
"	color:white;\n"
"	text-align:left;\n"
"	height:30px;\n"
"	border:none;\n"
"	padding-left:10px;\n"
"	border-top-left-raduis:10px;\n"
"	border-buttom-left-raduis:10px;\n"
"}\n"
"QPushButton:checked{\n"
"background-color: #f5fafe;\n"
"color:#000000;\n"
"font-weight:bold;\n"
"\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 20, -1)
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/images/king.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_name_widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.profile2 = QPushButton(self.icon_name_widget)
        self.profile2.setObjectName(u"profile2")
        self.profile2.setIcon(icon4)
        self.profile2.setCheckable(True)
        self.profile2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.profile2)

        self.auto2 = QPushButton(self.icon_name_widget)
        self.auto2.setObjectName(u"auto2")
        self.auto2.setIcon(icon5)
        self.auto2.setCheckable(True)
        self.auto2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.auto2)

        self.man2 = QPushButton(self.icon_name_widget)
        self.man2.setObjectName(u"man2")
        self.man2.setIcon(icon6)
        self.man2.setCheckable(True)
        self.man2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.man2)

        self.noti2 = QPushButton(self.icon_name_widget)
        self.noti2.setObjectName(u"noti2")
        self.noti2.setIcon(icon7)
        self.noti2.setCheckable(True)
        self.noti2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.noti2)

        self.sitt2 = QPushButton(self.icon_name_widget)
        self.sitt2.setObjectName(u"sitt2")
        self.sitt2.setIcon(icon8)
        self.sitt2.setCheckable(True)
        self.sitt2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.sitt2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 230, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.help2 = QPushButton(self.icon_name_widget)
        self.help2.setObjectName(u"help2")
        self.help2.setIcon(icon9)
        self.help2.setCheckable(True)
        self.help2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.help2)

        self.cl2 = QPushButton(self.icon_name_widget)
        self.cl2.setObjectName(u"cl2")
        self.cl2.setIcon(icon10)
        self.cl2.setCheckable(True)

        self.verticalLayout_4.addWidget(self.cl2)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menu.toggled.connect(self.icon_only_widget.setHidden)
        self.menu.toggled.connect(self.icon_name_widget.setVisible)
        self.sitt1.toggled.connect(self.sitt2.setChecked)
        self.noti1.toggled.connect(self.noti2.setChecked)
        self.man1.toggled.connect(self.man2.setChecked)
        self.auto1.toggled.connect(self.auto2.setChecked)
        self.profile1.toggled.connect(self.profile2.setChecked)
        self.profile2.toggled.connect(self.profile1.setChecked)
        self.auto2.toggled.connect(self.auto1.setChecked)
        self.man2.toggled.connect(self.man1.setChecked)
        self.noti2.toggled.connect(self.noti1.setChecked)
        self.sitt2.toggled.connect(self.sitt1.setChecked)
        self.help1.toggled.connect(self.help2.setChecked)
        self.help2.toggled.connect(self.help1.setChecked)
        self.cl1.toggled.connect(MainWindow.close)
        self.cl2.toggled.connect(MainWindow.close)
        self.cl2.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu.setText("")
        self.acc.setText("")
        self.pushButton_16.setText("")
        self.p.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"you can chage your id ", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"name", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"email-adress", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"password", None))
        self.modname.setText(QCoreApplication.translate("MainWindow", u"modify", None))
        self.modemail.setText(QCoreApplication.translate("MainWindow", u"modify", None))
        self.modpass.setText(QCoreApplication.translate("MainWindow", u"modify", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"you can use automatic", None))
        self.autoactvate.setText(QCoreApplication.translate("MainWindow", u"activate", None))
        self.stop.setText(QCoreApplication.translate("MainWindow", u"stop", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Bloc A", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"****", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"***", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"***", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"***", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"B1", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"B2", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"B3", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"B4", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Bloc B", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"*****", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"****", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"*****", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"**", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"A1", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"A2", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"A3", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"A4", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"you can change manuel ", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Bloc A", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"*****", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"****", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"*****", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"**", None))
        self.checkBox_13.setText(QCoreApplication.translate("MainWindow", u"A1", None))
        self.checkBox_14.setText(QCoreApplication.translate("MainWindow", u"A2", None))
        self.checkBox_15.setText(QCoreApplication.translate("MainWindow", u"A3", None))
        self.checkBox_16.setText(QCoreApplication.translate("MainWindow", u"A4", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"****", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"***", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"***", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"***", None))
        self.checkBox_9.setText(QCoreApplication.translate("MainWindow", u"B1", None))
        self.checkBox_10.setText(QCoreApplication.translate("MainWindow", u"B2", None))
        self.checkBox_11.setText(QCoreApplication.translate("MainWindow", u"B3", None))
        self.checkBox_12.setText(QCoreApplication.translate("MainWindow", u"B4", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Bloc B", None))
        self.place.setText(QCoreApplication.translate("MainWindow", u"place", None))
        self.evacute.setText(QCoreApplication.translate("MainWindow", u"evacuate", None))
        self.take.setText(QCoreApplication.translate("MainWindow", u"take", None))
        self.pompage.setText(QCoreApplication.translate("MainWindow", u"pompage", None))
        self.home.setText(QCoreApplication.translate("MainWindow", u"home", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"notifications", None))
        ___qtablewidgetitem = self.affichage.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"date", None));
        ___qtablewidgetitem1 = self.affichage.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"notification", None));
        ___qtablewidgetitem2 = self.affichage.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"1", None));

        __sortingEnabled = self.affichage.isSortingEnabled()
        self.affichage.setSortingEnabled(False)
        ___qtablewidgetitem3 = self.affichage.item(0, 0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"none", None));
        ___qtablewidgetitem4 = self.affichage.item(0, 1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"none", None));
        self.affichage.setSortingEnabled(__sortingEnabled)

        self.historic.setText(QCoreApplication.translate("MainWindow", u"historic", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"you can change ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Add new position robot(you can only chage +-4\u00b0)", None))
        self.submit.setText(QCoreApplication.translate("MainWindow", u"submit", None))
        self.add.setText(QCoreApplication.translate("MainWindow", u"add", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"add new carte (name & position)", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"name (id)", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"position", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Here are some resources that might be useful to you:\n"
"\n"
"Frequently Asked Questions (FAQ)\n"
"How to create an account?\n"
"Visit our account creation guide for detailed instructions.\n"
"\n"
"How to reset my password?\n"
"If you have forgotten your password, follow the steps outlined in our password reset section.\n"
"\n"
"How to contact technical support?\n"
"You can contact us via our contact form or by email at support@your-company.com.\n"
"\n"
"Guides and Tutorials\n"
"User Guide:\n"
"Check out our user guide for detailed instructions on how to use the application.\n"
"\n"
"Video Tutorials:\n"
"Watch our video tutorials for step-by-step demonstrations.\n"
"\n"
"Personalized Assistance\n"
"If you need personalized assistance, our support team is at your service:\n"
"\n"
"Email: support@your-company.com\n"
"Phone: +1 800 123 4567 (Monday - Friday, 9 AM - 6 PM)\n"
"Live Chat: Available on our website during business hours.\n"
"Additional Resources\n"
"Blog: Stay informed about the latest news and update"
                        "s by visiting our blog.\n"
"Community Forum: Join our community forum to connect with other users and find solutions to your problems.\n"
"We hope you find these resources helpful. Thank you for using our application!", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"first name", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"laste name", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"email", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"CIN", None))
        self.change.setText(QCoreApplication.translate("MainWindow", u"change", None))
        self.label_41.setText("")
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"welcome to our world", None))
        self.label.setText("")
        self.profile1.setText("")
        self.auto1.setText("")
        self.man1.setText("")
        self.noti1.setText("")
        self.sitt1.setText("")
        self.help1.setText("")
        self.cl1.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Sidebar", None))
        self.profile2.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.auto2.setText(QCoreApplication.translate("MainWindow", u"Automatic", None))
        self.man2.setText(QCoreApplication.translate("MainWindow", u"Manuel", None))
        self.noti2.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.sitt2.setText(QCoreApplication.translate("MainWindow", u"Sittings robot", None))
        self.help2.setText(QCoreApplication.translate("MainWindow", u"help", None))
        self.cl2.setText(QCoreApplication.translate("MainWindow", u"sign out", None))
    # retranslateUi

