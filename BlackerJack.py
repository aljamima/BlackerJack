# pip install matplotlib PyQt6 pygame
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PyQt6.QtWidgets import (QApplication, QComboBox, QFrame, QLCDNumber,
    QLabel, QLineEdit, QListView, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

import re
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
import pygame
from PyQt6.QtCore import QStringListModel

## pip install matplotlib PyQt6 pygame


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Blacker Jacker - Card Counter")
        MainWindow.resize(520, 500)

        """
        self.centralwidgetaroni = QWidget(MainWindow)
        self.centralwidgetaroni.setObjectName(u"centralwidgetaroni")
        self.centralwidgetaroni.setMaximumSize(QSize(16777215, 16777215))
        """

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #self.deckCount = QtWidgets.QSpinBox(self.centralwidget)

        self.deckCount = QSpinBox(self.centralwidget)
        self.deckCount.setObjectName(u"deckCount")
        self.deckCount.setGeometry(QtCore.QRect(30, 170, 131, 31))
        font = QtGui.QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(9)
        self.deckCount.setFont(font)
        self.deckCount.setMinimum(1)
        self.deckCount.setValue(6)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QtCore.QRect(30, 150, 131, 16))
        self.label.setFont(font)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QtCore.QRect(20, 20, 131, 16))
        font1 = QtGui.QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(9)
        font1.setBold(False)
        self.label_2.setFont(font1)
        
        #self.label_2.setAlignment(Qt.Alignment(Qt.AlignLeft | Qt.AlignVCenter))
        #self.label_2.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        #self.label_2.setAlignment(Qt.Alignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter))

        #self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        
        
        self.label_2.setWordWrap(False)
        self.shuffled = QtWidgets.QPushButton(self.centralwidget)
        self.shuffled.setObjectName(u"shuffled")
        self.shuffled.setGeometry(QtCore.QRect(20, 220, 151, 31))
        self.shuffled.setFont(font)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QtCore.QRect(270, 20, 41, 16))
        self.label_3.setFont(font)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QtCore.QRect(240, 40, 81, 31))
        self.lcdNumber.setFont(font)
        self.lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.lcdNumber.setDigitCount(6)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Flat)
        self.lcdNumber.setProperty(u"value", 0.000000000000000)
        self.textInput = QtWidgets.QLineEdit(self.centralwidget)
        self.textInput.setObjectName(u"textInput")
        self.textInput.setGeometry(QtCore.QRect(20, 40, 151, 31))
        self.textInput.setFont(font)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QtCore.QRect(30, 90, 131, 16))
        self.label_4.setFont(font)


        self.countingSystem = QtWidgets.QComboBox(self.centralwidget)
        self.countingSystem.addItem("")
        self.countingSystem.addItem("")
        self.countingSystem.addItem("")
        self.countingSystem.setObjectName(u"countingSystem")

        
        self.countingSystem.setGeometry(QtCore.QRect(30, 110, 131, 31))
        self.countingSystem.setFont(font)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QtCore.QRect(20, 80, 151, 131))
        font2 = QtGui.QFont()
        font2.setPointSize(9)
        self.frame.setFont(font2)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QtCore.QRect(20, 270, 171, 16))
        self.label_5.setFont(font)
        self.trueCountWidget = QtWidgets.QWidget(self.centralwidget)
        self.trueCountWidget.setObjectName(u"trueCountWidget")
        self.trueCountWidget.setGeometry(QtCore.QRect(240, 80, 251, 171))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.trueCountWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.remainingCardWidget = QtWidgets.QWidget(self.centralwidget)
        self.remainingCardWidget.setObjectName(u"remainingCardWidget")
        self.remainingCardWidget.setGeometry(QtCore.QRect(20, 289, 471, 171))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.remainingCardWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lcdNumber2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber2.setObjectName(u"lcdNumber_2")
        self.lcdNumber2.setGeometry(QtCore.QRect(330, 40, 81, 31))
        self.lcdNumber2.setFont(font)
        self.lcdNumber2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lcdNumber2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.lcdNumber2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.lcdNumber2.setDigitCount(6)
        self.lcdNumber2.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Flat)
        self.lcdNumber2.setProperty(u"value", 0.000000000000000)
        self.lcdNumber3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber3.setObjectName(u"lcdNumber_3")
        self.lcdNumber3.setGeometry(QtCore.QRect(420, 40, 81, 31))
        self.lcdNumber3.setFont(font)
        self.lcdNumber3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lcdNumber3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.lcdNumber3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.lcdNumber3.setDigitCount(6)
        self.lcdNumber3.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Flat)
        self.lcdNumber3.setProperty(u"value", 0.000000000000000)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QtCore.QRect(340, 20, 61, 16))
        self.label_6.setFont(font)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QtCore.QRect(440, 20, 61, 16))
        self.label_7.setFont(font)

        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QtCore.QRect(180, 41, 51, 231))
        
        self.listView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.listView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QtCore.QRect(180, 20, 51, 16))
        self.label_8.setFont(font1)
        
        #self.label_8.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        
        self.label_8.setWordWrap(False)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame.raise_()
        self.deckCount.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.shuffled.raise_()
        self.label_3.raise_()
        self.lcdNumber.raise_()
        self.textInput.raise_()
        self.label_4.raise_()
        self.countingSystem.raise_()
        self.label_5.raise_()
        self.trueCountWidget.raise_()
        self.remainingCardWidget.raise_()
        self.lcdNumber2.raise_()
        self.lcdNumber3.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.listView.raise_()
        self.label_8.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Blacker Jacker - Card Counter", u"Blacker Jacker - Card Counter", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Number of Decks", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Card Values (2-10, J-A)", None))
        self.shuffled.setText(QCoreApplication.translate("MainWindow", u"Shuffled", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Hi-Lo", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Card Counting System", None))
        self.countingSystem.setItemText(0, QCoreApplication.translate("MainWindow", u"Wong Halves", None))
        self.countingSystem.setItemText(1, QCoreApplication.translate("MainWindow", u"Omega II", None))
        self.countingSystem.setItemText(2, QCoreApplication.translate("MainWindow", u"Hi-Lo", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Remaining Card Probabilities", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Wong Halves", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Omega II", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Previous:", None))



cardValues = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
groupedCardValues = ["2","3","4","5","6","7","8","9","10 - K","A"]



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)

        self.remainingCardCount = 312
        self.individualCardCount = {}
        self.individualCardCount.update(dict.fromkeys(cardValues, 24))
        self.totalRunningCount = 0
        self.trueCount = 0
        self.hiloCount = 0
        self.omegaCount = 0
        self.wongCount = 0
        self.trueCountHistory = [0]

        self.mousePressEvent = self.deselect
        self.keyPressEvent = self.inputCardValues
        self.countingSystem.currentTextChanged.connect(self.reset)
        self.deckCount.valueChanged.connect(self.reset)
        self.shuffled.clicked.connect(self.reset)

        # Initialize the list model for the listView
        self.list_model = QStringListModel()
        self.list_items = []  # A Python list to store the items
        self.listView.setModel(self.list_model)

        # Connect signals
        self.textInput.returnPressed.connect(self.add_to_list)
        self.countingSystem.currentTextChanged.connect(self.reset)
        self.deckCount.valueChanged.connect(self.reset)
        self.shuffled.clicked.connect(self.reset)

        self.valid_cards_pattern = r"(10|[2-9]|A|K|Q|J|T)"

        self.textInput.setFocus()

    def add_to_list(self):
        """Append the text from textInput to the listView."""
        input_text = self.textInput.text().upper().strip()
        formattedInputList = re.findall(self.valid_cards_pattern, input_text)

        #this part probably isnt necessary
        if not formattedInputList:
            print("No valid card values found.")
            #self.play_sound("no_input.wav")
        else:
            # Group valid inputs into lines of 4 items each
            grouped_input = [" ".join(formattedInputList[i:i+4]) for i in range(0, len(formattedInputList), 4)]

            # Add each group to the top of the list
            for group in reversed(grouped_input):  # Reverse so the first group appears at the top
                self.list_items.insert(0, group)

            # Update the model
            self.list_model.setStringList(self.list_items)

            """
            valid_input_string = " ".join(formattedInputList)  # Join with spaces
            self.list_items.insert(0, valid_input_string)  # Add to the top of the list
            self.list_model.setStringList(self.list_items)  # Update the model
            """


    def play_sound(self, file_path):
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        # Wait until the sound finishes playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)


    def inputCardValues(self, event):
        if event.key() == Qt.Key.Key_Return:
            inputText = self.textInput.text().upper()
            if not inputText:
                print('Thats NOT Valid Input, Dude!')
                #self.play_sound("no_input.wav")
                return

            inputFormattedText = inputText.replace(",", " ")
            inputCardValueList = re.split(r"\s+", inputFormattedText)

            # Filter out valid card values
            # but lets try this way where all valid inputs are collected regardless of delimiters
            formattedCardValueList = re.findall(self.valid_cards_pattern, inputText)
            #formattedCardValueList = [v for v in inputCardValueList if v in cardValues]

            #this part probably isnt necessary
            if not formattedCardValueList:
                print("No valid card values found.")
                #self.play_sound("no_input.wav")

            # Decrement from self.individualCardCount
            for value in formattedCardValueList:
                self.individualCardCount[value] -= 1

            # Now update *all three* systems at once:
            for value in formattedCardValueList:
                # Hi-Lo
                if value in ["2","3","4","5","6"]:
                    self.hiloCount += 1
                elif value in ["10","J","Q","K","A"]:
                    self.hiloCount -= 1

                # Omega II
                if value in ["2","3","7"]:
                    self.omegaCount += 1
                elif value in ["4","5","6"]:
                    self.omegaCount += 2
                elif value == "9":
                    self.omegaCount -= 1
                elif value in ["10","J","Q","K"]:
                    self.omegaCount -= 2

                # Wong Halves
                if value in ["2","7"]:
                    self.wongCount += 0.5
                elif value in ["3","4","6"]:
                    self.wongCount += 1
                elif value == "5":
                    self.wongCount += 1.5
                elif value == "9":
                    self.wongCount -= 0.5
                elif value in ["10","J","Q","K","A"]:
                    self.wongCount -= 1

            # Update the number of cards gone
            cardCount = len(formattedCardValueList)
            self.remainingCardCount -= cardCount

            # Compute your “remaining decks” so far
            decksRemaining = self.remainingCardCount / 52.0

            # Compute True Counts
            # (hiLoCount, omegaCount, wongCount) are separate counters
            trueCountHilo  = self.hiloCount  / decksRemaining
            trueCountOmega = self.omegaCount / decksRemaining
            trueCountWong  = self.wongCount  / decksRemaining

            self.displayAllSystems(trueCountHilo, trueCountOmega, trueCountWong)

            # Update charts and remaining card probabilities
            self.trueCountHistory.append(trueCountHilo)  # Update history for Hi-Lo (or choose one system)
            self.updateCountsPlot()
            self.updateremainingCardHist()

            self.textInput.setText("")

    def hiLo(self, formattedCardValueList):
        cardCount = 0
        runningCount = 0
        for value in formattedCardValueList:
            if value in ["2","3","4","5","6"]:
                runningCount += 1
            elif value in ["10","J","Q","K","A"]:
                runningCount -= 1
            cardCount += 1
        self.textInput.setText("")
        self.updateOutput(cardCount, runningCount)

    def omega(self, formattedCardValueList):
        cardCount = 0
        runningCount = 0
        for value in formattedCardValueList:
            if value in ["2","3","7"]:
                runningCount += 1
            elif value in ["4","5","6"]:
                runningCount += 2
            elif value in ["9"]:
                runningCount -= 1
            elif value in ["10","J","Q","K"]:
                runningCount -= 2
            cardCount += 1
        self.textInput.setText("")
        self.updateOutput(cardCount, runningCount)

    def wong(self, formattedCardValueList):
        cardCount = 0
        runningCount = 0
        for value in formattedCardValueList:
            if value in ["2","7"]:
                runningCount += 0.5
            elif value in ["3","4","6"]:
                runningCount += 1
            elif value in ["5"]:
                runningCount += 1.5
            elif value in ["9"]:
                runningCount -= 0.5
            elif value in ["10","J","Q","K","A"]:
                runningCount -= 1
            cardCount += 1
        self.textInput.setText("")
        self.updateOutput(cardCount, runningCount)

    def addCountsPlot(self):
        self.trueCountFigure = Figure()
        self.trueCountFigure.subplots_adjust(left=0.13,right=0.94,bottom=0.1,top=0.9)
        self.trueCountPlot = self.trueCountFigure.add_subplot(1,1,1)
        self.trueCountPlot.axhline(0, linewidth=0.6, color='black')
        self.trueCountPlot.plot(self.trueCountHistory, "C0-")
        self.trueCountPlot.axes.set_ylim([-10,10])
        self.trueCountPlot.tick_params(labelsize=7)
        self.trueCountPlot.axes.get_xaxis().set_visible(False)
        self.trueCountCanvas = FigureCanvas(self.trueCountFigure)
        self.trueCountWidget.layout().addWidget(self.trueCountCanvas)
        self.trueCountCanvas.draw()

    def updateCountsPlot(self):
        self.trueCountPlot.remove()
        self.trueCountPlot = self.trueCountFigure.add_subplot(1,1,1)
        self.trueCountPlot.axhline(0, linewidth=0.6, color='black')
        self.trueCountPlot.plot(self.trueCountHistory, "C0-")
        self.trueCountPlot.axes.set_ylim([-10,10])
        self.trueCountPlot.tick_params(labelsize=7)
        self.trueCountPlot.axes.get_xaxis().set_visible(False)
        self.trueCountCanvas.draw()

    def addremainingCardHist(self):
        self.remainingCardFigure = Figure()
        self.remainingCardFigure.subplots_adjust(left=0.08,right=0.965,bottom=0.16,top=0.9)
        self.remainingCardBar = self.remainingCardFigure.add_subplot(1,1,1)
        defaultRemainingCardProbabilities = [1.0/13,1.0/13,1.0/13,1.0/13,1.0/13,1.0/13,1.0/13,1.0/13,4.0/13,1.0/13]
        self.remainingCardBar.bar(groupedCardValues, height=defaultRemainingCardProbabilities)
        for cardValue, probability in enumerate(defaultRemainingCardProbabilities):
            self.remainingCardBar.text((groupedCardValues[cardValue]), probability+max(defaultRemainingCardProbabilities)*0.05, str(probability)[:5], ha='center', fontsize=6)
        self.remainingCardBar.set_ylim(top=max(defaultRemainingCardProbabilities)*1.2)
        self.remainingCardBar.tick_params(labelsize=7)
        self.remainingCardCanvas = FigureCanvas(self.remainingCardFigure)
        self.remainingCardWidget.layout().addWidget(self.remainingCardCanvas)
        self.remainingCardCanvas.draw()

    def updateremainingCardHist(self):
        groupedCardCountList = [ self.individualCardCount["2"],
                                self.individualCardCount["3"],
                                self.individualCardCount["4"],
                                self.individualCardCount["5"],
                                self.individualCardCount["6"],
                                self.individualCardCount["7"],
                                self.individualCardCount["8"],
                                self.individualCardCount["9"],
                                self.individualCardCount["10"] + self.individualCardCount["J"] + self.individualCardCount["Q"] + self.individualCardCount["K"],
                                self.individualCardCount["A"] ]
        remainingCardProbabilities = [ count / self.remainingCardCount for count in groupedCardCountList]
        self.remainingCardBar.remove()
        self.remainingCardBar = self.remainingCardFigure.add_subplot(1,1,1)
        self.remainingCardBar.bar(groupedCardValues, height=remainingCardProbabilities)
        for cardValue, probability in enumerate(remainingCardProbabilities):
            self.remainingCardBar.text((groupedCardValues[cardValue]), probability+max(remainingCardProbabilities)*0.05, str(probability)[:5], ha='center', fontsize=6)
        self.remainingCardBar.set_ylim(top=max(remainingCardProbabilities)*1.2)
        self.remainingCardBar.tick_params(labelsize=7)
        self.remainingCardCanvas.draw()

    def updateOutput(self, cardCount, runningCount):
        self.remainingCardCount -= cardCount
        remainingCardDeckCount = self.remainingCardCount / 52.0
        self.totalRunningCount += runningCount
        self.trueCount = self.totalRunningCount / remainingCardDeckCount
        self.trueCountHistory.append(self.trueCount)
        roundedTrueCount = round(self.trueCount, 3)
        if roundedTrueCount > 0:
            self.lcdNumber.setStyleSheet("QLCDNumber { background-color: white; color: green; }")
            self.lcdNumber2.setStyleSheet("QLCDNumber { background-color: white; color: green; }")
            self.lcdNumber3.setStyleSheet("QLCDNumber { background-color: white; color: green; }")
        elif roundedTrueCount < 0:
            self.lcdNumber.setStyleSheet("QLCDNumber { background-color: white; color: red; }")
            self.lcdNumber2.setStyleSheet("QLCDNumber { background-color: white; color: red; }")
            self.lcdNumber3.setStyleSheet("QLCDNumber { background-color: white; color: red; }")
        else:
            self.lcdNumber.setStyleSheet("QLCDNumber { background-color: white; color: black; }")
            self.lcdNumber2.setStyleSheet("QLCDNumber { background-color: white; color: black; }")
            self.lcdNumber3.setStyleSheet("QLCDNumber { background-color: white; color: black; }")

        self.lcdNumber.display(roundedTrueCount)
        self.lcdNumber2.display(roundedTrueCount)
        self.lcdNumber3.display(roundedTrueCount)

        self.updateCountsPlot()
        self.updateremainingCardHist()

    def deselect(self, event):
        self.textInput.clearFocus()
        self.countingSystem.clearFocus()
        self.deckCount.clearFocus()

    def reset(self):
        self.remainingCardCount = self.deckCount.value() * 52.0
        individualCardCount = self.deckCount.value() * 4
        self.individualCardCount.update(dict.fromkeys(cardValues, individualCardCount))
        self.totalRunningCount = 0
        self.trueCount = 0
        self.hiloCount  = 0
        self.omegaCount = 0
        self.wongCount  = 0

        # Clear displays
        self.lcdNumber.display(0)
        self.lcdNumber2.display(0)
        self.lcdNumber3.display(0)
        self.trueCountHistory = [0]
        self.textInput.setText("")
        self.lcdNumber.setStyleSheet("QLCDNumber { background-color: white; color: black; }")
        self.lcdNumber.display(0)

        self.lcdNumber2.setStyleSheet("QLCDNumber { background-color: white; color: black; }")
        self.lcdNumber2.display(0)

        self.lcdNumber3.setStyleSheet("QLCDNumber { background-color: white; color: black; }")
        self.lcdNumber3.display(0)

        # Clear the listView
        self.list_items.clear()  # Clear the Python list
        self.list_model.setStringList(self.list_items) 

        self.updateCountsPlot()
        self.updateremainingCardHist()

        self.textInput.clear()  # Clear the text input.


    def displayAllSystems(self, hiloTC, omegaTC, wongTC):
        # Round or do whatever final formatting
        hiloRounded  = round(hiloTC, 2)
        omegaRounded = round(omegaTC, 2)
        wongRounded  = round(wongTC, 2)

        # Send each to its own LCD
        self.lcdNumber.display(hiloRounded)    # Suppose lcdNumber is for Hi-Lo
        
        self.lcdNumber2.display(omegaRounded)  # Suppose lcdNumber2 is for Omega
        self.lcdNumber3.display(wongRounded)   # Suppose lcdNumber3 is for Wong

        # Apply color logic if you want:
        self.updateLCDColor(self.lcdNumber,  hiloRounded)
        self.updateLCDColor(self.lcdNumber2, omegaRounded)
        self.updateLCDColor(self.lcdNumber3, wongRounded)

        # Optionally track each system’s history if you want to plot them
        # (You’d need separate lists for each system’s historical values)
        # self.trueCountHistoryHilo.append(hiloRounded)
        # self.trueCountHistoryOmega.append(omegaRounded)
        # self.trueCountHistoryWong.append(wongRounded)
        # Then do something to plot them.

    def updateLCDColor(self, lcd, value):
        if value > 0:
            lcd.setStyleSheet("QLCDNumber { background-color: white; color: green; }")
        elif value < 0:
            lcd.setStyleSheet("QLCDNumber { background-color: white; color: red; }")
        else:
            lcd.setStyleSheet("QLCDNumber { background-color: white; color: black; }")



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()

    MainWindow.addCountsPlot()
    MainWindow.addremainingCardHist()

    MainWindow.setFixedSize(MainWindow.size())
    MainWindow.show()
    sys.exit(app.exec())
