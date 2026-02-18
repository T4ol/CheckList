import sys
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QWidgetAction
from PySide6.QtGui import Qt, QAction
from TaskUI import Ui_MainWindow
from WindowForAddTask import Ui_Form
import json

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

    def closeEvent(self, event):
        #Для закрытия всех окн приложения
        QApplication.closeAllWindows()
        event.accept()

class WindowAddTask(QWidget):
    """Окно для создания задач"""
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.buttonCancel.clicked.connect(lambda: self.close())
        self.ui.textEdit.textChanged.connect(self.buttonEnabled)
        self.ui.buttonAdd.clicked.connect(self.addTask)

    def buttonEnabled(self):
        """Переводит кнопку add в активное состояние если есть тект в textedit"""
        text = bool(self.ui.textEdit.toPlainText().strip())
        self.ui.buttonAdd.setEnabled(text)

    def addTask(self):
        """Ф-ция добавляет задачи в json"""
        new_task = {"task": self.ui.textEdit.toPlainText()}
        all_task = []

        with open("Task.json", "r") as file_json:
            all_task = json.load(file_json)
            all_task.append(new_task)

        with open("Task.json", "w") as file_json:
            json.dump(all_task, file_json)

        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())