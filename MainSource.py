import sys
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QWidgetAction
from PySide6.QtGui import Qt, QAction
from TaskUI import Ui_MainWindow
from WindowForAddTask import Ui_Form

class MainWindow(QMainWindow):
    """Главное окно с задачами"""
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionAdd.triggered.connect(self.winAdd)

    def winAdd(self):
        self.win = WindowAddTask()
        self.win.show()

class WindowAddTask(QMainWindow):
    """Окно для создания задач"""
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.buttonCancelTask.clicked.connect(lambda: self.close())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())