# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PywolfLanchermainui.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QTextBrowser, QWidget)
import PywolfLancher_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(800, 600)
        icon = QIcon()
        icon.addFile(u":/picture/PywolfLancher.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_7 = QAction(MainWindow)
        self.action_7.setObjectName(u"action_7")
        self.action_directory = QAction(MainWindow)
        self.action_directory.setObjectName(u"action_directory")
        self.action_pwpack = QAction(MainWindow)
        self.action_pwpack.setObjectName(u"action_pwpack")
        self.action_indev = QAction(MainWindow)
        self.action_indev.setObjectName(u"action_indev")
        self.actionwolfstore = QAction(MainWindow)
        self.actionwolfstore.setObjectName(u"actionwolfstore")
        self.actionglobalnetwork = QAction(MainWindow)
        self.actionglobalnetwork.setObjectName(u"actionglobalnetwork")
        self.actionQt = QAction(MainWindow)
        self.actionQt.setObjectName(u"actionQt")
        self.actionQt.setMenuRole(QAction.MenuRole.AboutQtRole)
        self.actionUser_Manual = QAction(MainWindow)
        self.actionUser_Manual.setObjectName(u"actionUser_Manual")
        self.actionabout = QAction(MainWindow)
        self.actionabout.setObjectName(u"actionabout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 368, 38))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.layoutWidget)
        self.label_13.setObjectName(u"label_13")
        font = QFont()
        font.setPointSize(20)
        self.label_13.setFont(font)

        self.horizontalLayout.addWidget(self.label_13)

        self.label_14 = QLabel(self.layoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.horizontalLayout.addWidget(self.label_14)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(0, 220, 441, 341))
        self.textBrowser.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(186, 117, 16, 16))
        self.label_8.setPixmap(QPixmap(u":/picture/circle-fill(not_installed).svg"))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QRect(1, 117, 179, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(1, 95, 176, 16))
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(282, 139, 64, 16))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(1, 73, 174, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(186, 73, 16, 16))
        self.label_5.setPixmap(QPixmap(u":/picture/circle-fill(online).svg"))
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(1, 139, 176, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(282, 73, 64, 16))
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(186, 139, 16, 16))
        self.label_11.setPixmap(QPixmap(u":/picture/circle-fill(online).svg"))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(282, 117, 178, 16))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(186, 95, 16, 16))
        self.label_6.setPixmap(QPixmap(u":/picture/circle-fill(online).svg"))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(282, 95, 64, 16))
        self.LogonButton = QPushButton(self.centralwidget)
        self.LogonButton.setObjectName(u"LogonButton")
        self.LogonButton.setGeometry(QRect(600, 0, 200, 50))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_8 = QMenu(self.menu_2)
        self.menu_8.setObjectName(u"menu_8")
        self.menu_8.setToolTipsVisible(True)
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        self.menu_5 = QMenu(self.menubar)
        self.menu_5.setObjectName(u"menu_5")
        self.menu_6 = QMenu(self.menubar)
        self.menu_6.setObjectName(u"menu_6")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_6.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menu_2.addAction(self.menu_8.menuAction())
        self.menu_2.addSeparator()
        self.menu_8.addAction(self.action_7)
        self.menu_8.addAction(self.action_directory)
        self.menu_8.addSeparator()
        self.menu_8.addAction(self.action_pwpack)
        self.menu_8.addSeparator()
        self.menu_8.addAction(self.actionwolfstore)
        self.menu_8.addAction(self.action_indev)
        self.menu_8.addSeparator()
        self.menu_8.addAction(self.actionglobalnetwork)
        self.menu_4.addAction(self.actionQt)
        self.menu_4.addAction(self.actionUser_Manual)
        self.menu_4.addAction(self.actionabout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PywolfLancher Ver b0.0.01 \u4f5c\u696d\u30d5\u30a9\u30eb\u30c0\uff1aC:\\dev\\PyWolf", None))
#if QT_CONFIG(statustip)
        MainWindow.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u30b2\u30fc\u30e0\u306e\u30a4\u30f3\u30b9\u30c8\u30fc\u30eb", None))
        self.action_7.setText(QCoreApplication.translate("MainWindow", u"\u5727\u7e2e\u30d5\u30a1\u30a4\u30eb\u304b\u3089", None))
        self.action_directory.setText(QCoreApplication.translate("MainWindow", u"\u30c7\u30a3\u30ec\u30af\u30c8\u30ea\u304b\u3089", None))
        self.action_pwpack.setText(QCoreApplication.translate("MainWindow", u".pwpack\u30d5\u30a1\u30a4\u30eb\u304b\u3089", None))
        self.action_indev.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u5206\u306eindev\u30ea\u30dd\u30b8\u30c8\u30ea\u304b\u3089", None))
        self.actionwolfstore.setText(QCoreApplication.translate("MainWindow", u"Wolfstore\u304b\u3089", None))
        self.actionglobalnetwork.setText(QCoreApplication.translate("MainWindow", u"WolfStore\u4ee5\u5916\u306e\u30b0\u30ed\u30fc\u30d0\u30eb\u30cd\u30c3\u30c8\u30ef\u30fc\u30af\u304b\u3089", None))
        self.actionQt.setText(QCoreApplication.translate("MainWindow", u"Qt\u306b\u3064\u3044\u3066", None))
        self.actionUser_Manual.setText(QCoreApplication.translate("MainWindow", u"\u30e6\u30fc\u30b6\u30fc\u30de\u30cb\u30e5\u30a2\u30eb", None))
#if QT_CONFIG(tooltip)
        self.actionUser_Manual.setToolTip(QCoreApplication.translate("MainWindow", u"\u30e6\u30fc\u30b6\u30fc\u30de\u30cb\u30e5\u30a2\u30eb\u3092\u53c2\u7167\u3057\u307e\u3059\u3002", None))
#endif // QT_CONFIG(tooltip)
        self.actionabout.setText(QCoreApplication.translate("MainWindow", u"Pywolf\u306b\u3064\u3044\u3066", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u3053\u306ePC\u306ePC\u540d\uff1a", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"CCSLIKEER", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Yu Gothic UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 0;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u3053\u306ePC\u306ePywolf\u306f\u30ed\u30fc\u30ab\u30ebID\u3067\u52d5\u4f5c\u3057\u3066\u3044\u307e\u3059\u3002	</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u79fb\u884c\u3092\u3059\u308b\u5834\u5408"
                        "\u306f\u30e6\u30fc\u30b6\u30fc\u30e1\u30cb\u30e5\u30fc\u3092\u4f7f\u7528\u3057\u3066\u304f\u3060\u3055\u3044\u3002	</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u9ad8\u5ea6\u306a\u6a5f\u80fd\u306f\u5f8c\u304b\u3089\u8ffd\u52a0\u3067\u304d\u307e\u3059\u3002	</li>\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u306a\u304a\u3001\u73fe\u5728\u306e\u30a2\u30ab\u30a6\u30f3\u30c8\u3067\u306f\u5fdc\u7528\u958b\u767a\u6a5f\u80fd\u3092\u4f7f\u7528\u3067\u304d\u307e\u305b\u3093\u3002	</li>\n"
"<li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pywolf\u306e\u5fdc\u7528\u958b\u767a\u6a5f\u80fd\u306b\u3064\u3044\u3066\u306fhttps://pywolf.org/about/indev\u3092\u3054\u89a7\u304f\u3060\u3055\u3044\u3002</li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right"
                        ":0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_8.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"PyWolf\u30d5\u30a9\u30eb\u30c0\u4fdd\u8b77\u3000\u3000\u3000\u3000\u3000   \uff1a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Pywolf\u5185\u90e8\u30d7\u30ed\u30ad\u30b7\u30b5\u30fc\u30d0\u30fc\u306e\u72b6\u614b\uff1a</p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u30aa\u30f3\u30e9\u30a4\u30f3\u3067\u3059", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Pywolf\u5185\u90e8HTTPS\u30b5\u30fc\u30d0\u30fc\u306e\u72b6\u614b\uff1a", None))
        self.label_5.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Pywolf\u5185\u90e8\u30d7\u30ed\u30ad\u30b7\u30b5\u30fc\u30d0\u30fc\u306e\u72b6\u614b\uff1a</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u30aa\u30f3\u30e9\u30a4\u30f3\u3067\u3059", None))
        self.label_11.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u5fc5\u8981\u306a\u30b5\u30fc\u30d3\u30b9\u304c\u6709\u52b9\u306b\u306a\u3063\u3066\u3044\u307e\u305b\u3093", None))
        self.label_6.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u30aa\u30f3\u30e9\u30a4\u30f3\u3067\u3059", None))
        self.LogonButton.setText(QCoreApplication.translate("MainWindow", u"\u30ed\u30b0\u30a4\u30f3", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u30d5\u30a1\u30a4\u30eb", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u30b2\u30fc\u30e0\u7ba1\u7406", None))
#if QT_CONFIG(tooltip)
        self.menu_8.setToolTip(QCoreApplication.translate("MainWindow", u"\u30ed\u30b0\u30a4\u30f3\u4e2d\u306ePywolfLancher\u30ed\u30fc\u30ab\u30eb\u30e6\u30fc\u30b6\u30fc\u7528\u306b\u65b0\u3057\u3044\u30b2\u30fc\u30e0\u3092\u30a4\u30f3\u30b9\u30c8\u30fc\u30eb\u3059\u308b", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.menu_8.setStatusTip(QCoreApplication.translate("MainWindow", u"\u30ed\u30b0\u30a4\u30f3\u4e2d\u306ePywolfLancher\u30ed\u30fc\u30ab\u30eb\u30e6\u30fc\u30b6\u30fc\u7528\u306b\u65b0\u3057\u3044\u30b2\u30fc\u30e0\u3092\u30a4\u30f3\u30b9\u30c8\u30fc\u30eb\u3059\u308b", None))
#endif // QT_CONFIG(statustip)
        self.menu_8.setTitle(QCoreApplication.translate("MainWindow", u"\u30b2\u30fc\u30e0\u306e\u30a4\u30f3\u30b9\u30c8\u30fc\u30eb", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u30a2\u30ab\u30a6\u30f3\u30c8", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u30d8\u30eb\u30d7", None))
        self.menu_5.setTitle(QCoreApplication.translate("MainWindow", u"\u958b\u767a\u8005\u6a5f\u80fd", None))
        self.menu_6.setTitle(QCoreApplication.translate("MainWindow", u"\u30b5\u30fc\u30d0\u30fc", None))
    # retranslateUi

