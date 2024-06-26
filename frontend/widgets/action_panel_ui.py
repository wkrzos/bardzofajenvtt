from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QListWidget, QListWidgetItem
from PySide6.QtCore import Qt

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton
from PySide6.QtCore import Qt
from frontend.util.font import DEFAULT_FONT

class ActionPanelUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel(self.tr("Actions"))
        self.label.setFont(DEFAULT_FONT)
        layout.addWidget(self.label)

        self.action_list = QListWidget()
        self.action_list.setFont(DEFAULT_FONT)
        layout.addWidget(self.action_list)

        self.execute_button = QPushButton(self.tr("Execute Action"))
        self.execute_button.setFont(DEFAULT_FONT)
        layout.addWidget(self.execute_button)

        self.setLayout(layout)

    def clear_actions(self):
        self.action_list.clear()

    def add_action(self, name, func):
        item = QListWidgetItem(self.tr(name))
        item.setFont(DEFAULT_FONT)
        item.setData(Qt.UserRole, func)
        self.action_list.addItem(item)

    def get_selected_action(self):
        selected_items = self.action_list.selectedItems()
        if selected_items:
            return selected_items[0].data(Qt.UserRole)
        return None

