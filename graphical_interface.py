# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'random_melody_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#

from PyQt5 import QtCore, QtGui, QtWidgets
from melody_generator import Melody, MelodyPlayer, OSCILLATOR


class Ui_MainWindow(object):
    def __init__(self):
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.user_feedback = QtWidgets.QLabel(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.bars_input = QtWidgets.QLineEdit(self.centralwidget)
        self.interval_input = QtWidgets.QLineEdit(self.centralwidget)
        self.bpm_input = QtWidgets.QLineEdit(self.centralwidget)
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.play_btn = QtWidgets.QPushButton(self.centralwidget)
        self.generate_melody_btn = QtWidgets.QPushButton(self.centralwidget)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)

        self.melody_bar = Melody()
        self.melody_player = MelodyPlayer(OSCILLATOR)

    def setup_ui(self, window):
        window.setObjectName("MainWindow")
        window.resize(359, 495)

        self.centralwidget.setObjectName("centralwidget")

        self.generate_melody_btn.setGeometry(QtCore.QRect(90, 270, 171, 27))
        self.generate_melody_btn.setObjectName("generate_melody_btn")
        self.generate_melody_btn.clicked.connect(self.generate_melody)

        self.play_btn.setGeometry(QtCore.QRect(29, 410, 111, 27))
        self.play_btn.setObjectName("play_btn")
        self.play_btn.clicked.connect(self.play_melody)

        self.save_btn.setGeometry(QtCore.QRect(229, 410, 111, 27))
        self.save_btn.setObjectName("save_btn")
        self.save_btn.clicked.connect(self.save_melody)

        self.bpm_input.setGeometry(QtCore.QRect(210, 100, 41, 27))
        self.bpm_input.setObjectName("bpm_input")

        self.bars_input.setGeometry(QtCore.QRect(210, 140, 41, 27))
        self.bars_input.setObjectName("bars_btn")

        self.interval_input.setGeometry(QtCore.QRect(210, 180, 41, 27))
        self.interval_input.setObjectName("interval_btn")

        self.label.setGeometry(QtCore.QRect(90, 100, 121, 20))
        self.label.setObjectName("label")

        self.label_2.setGeometry(QtCore.QRect(100, 140, 111, 21))
        self.label_2.setObjectName("label_2")

        self.label_3.setGeometry(QtCore.QRect(110, 180, 101, 31))
        self.label_3.setObjectName("label_3")

        self.label_4.setGeometry(QtCore.QRect(9, 10, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Sawasdee")
        font.setPointSize(19)
        self.label_4.setFont(font)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_4.setObjectName("label_4")

        self.user_feedback.setGeometry(QtCore.QRect(100, 340, 250, 20))
        self.user_feedback.setText("")
        self.user_feedback.setObjectName("user_feedback")
        window.setCentralWidget(self.centralwidget)

        self.statusbar.setObjectName("statusbar")
        window.setStatusBar(self.statusbar)

        self.retranslate_ui(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslate_ui(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("MainWindow", "Melody Genereator"))
        self.generate_melody_btn.setText(_translate("MainWindow", "Generate Melody"))
        self.play_btn.setText(_translate("MainWindow", "Play Melody"))
        self.save_btn.setText(_translate("MainWindow", "Save as WAV"))
        self.label.setText(_translate("MainWindow", "Beats Per Minute"))
        self.label_2.setText(_translate("MainWindow", "Number of Bars"))
        self.label_3.setText(_translate("MainWindow", "Max Interval"))
        self.label_4.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:20pt;\""
                                        ">Random Melody Generator</span></p></body></html>"))

    def generate_melody(self):
        try:
            interval = int(self.interval_input.text())
            bars = int(self.bars_input.text())
        except ValueError:
            self.user_feedback.setGeometry(QtCore.QRect(118, 340, 250, 20))
            self.user_feedback.setText("Invalid parameter.")
            return

        self.melody_bar.generate_melody(bars, interval)
        self.user_feedback.setGeometry(QtCore.QRect(90, 340, 250, 20))
        self.user_feedback.setText("Melody created succesfully.")

    def play_melody(self):
        try:
            bpm = int(self.bpm_input.text())
        except ValueError:
            self.user_feedback.setGeometry(QtCore.QRect(118, 340, 250, 20))
            self.user_feedback.setText("Invalid parameter.")
            return

        if self.melody_bar.notes:
            self.user_feedback.setText("Playing Melody")
            self.melody_player.play_melody(self.melody_bar, bpm)
            self.user_feedback.setText("")
        else:
            self.user_feedback.setGeometry(QtCore.QRect(68, 340, 250, 20))
            self.user_feedback.setText("You must generate the melody frist.")

    def save_melody(self):
        try:
            bpm = int(self.bpm_input.text())
        except ValueError:
            self.user_feedback.setGeometry(QtCore.QRect(118, 340, 250, 20))
            self.user_feedback.setText("Invalid parameter.")
            return

        if self.melody_bar.notes:
            self.melody_player.save_melody(self.melody_bar, bpm)
            self.user_feedback.setGeometry(QtCore.QRect(130, 340, 250, 20))
            self.user_feedback.setText("Saved as WAV")
        else:
            self.user_feedback.setGeometry(QtCore.QRect(68, 340, 250, 20))
            self.user_feedback.setText("You must generate the melody frist.")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setup_ui(main_window)
    main_window.show()
    sys.exit(app.exec_())


