# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtCore import pyqtSlot, QUrl
from PyQt4.QtGui import QMainWindow

from UI.Ui_mainwindowform import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super().__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_btnNavigate_released(self):
        """
        Slot documentation goes here.
        """
        self.webView.setUrl(QUrl(self.txtURL.text()))
       
       # raise NotImplementedError
