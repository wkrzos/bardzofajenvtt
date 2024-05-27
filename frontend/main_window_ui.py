import os
from PySide6.QtWidgets import QHBoxLayout, QWidget, QSplitter, QTabWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from frontend.widgets.mapview import MapView
from frontend.widgets.chatview import ChatView, CharactersView, ItemsView, CreaturesView, MusicPlayerView, OptionsView
from frontend.widgets.actionpanel import ActionPanel
from models.toolbar_model import ToolbarModel
from frontend.widgets.toolbar_ui import ToolbarUI
from controlers.toolbar import ToolbarController

class MainWindowUI:
    def __init__(self, main_window):
        self.main_window = main_window
        self.music_player_view = None
        self.toolbar_model = ToolbarModel()
        self.toolbar_view = ToolbarUI(self.main_window)
        self.toolbar_controller = ToolbarController(self.toolbar_model, self.toolbar_view)

    def create_music_player_view(self):
        return MusicPlayerView()

    def setup_ui(self):
        self.main_window.setWindowTitle(self.main_window.tr("BFVTT Application"))
        self.main_window.setGeometry(100, 100, 1200, 800)

        icon_path = os.path.join(os.path.dirname(__file__), 'frontend/resources/logo/bfvtt_icon_no_bg.png')
        self.main_window.setWindowIcon(QIcon(icon_path))

        self.initUI()

    def initUI(self):
        main_layout = QHBoxLayout()

        self.toolbar_view.setFixedWidth(60)

        self.map_view = MapView(self.main_window)

        right_tab_widget = QTabWidget()
        right_tab_widget.setFixedWidth(300)

        chat_view = ChatView()
        characters_view = CharactersView()
        creatures_view = CreaturesView()
        items_view = ItemsView()
        options_view = OptionsView()
        
        right_tab_widget.addTab(chat_view, self.main_window.tr("Chat"))
        right_tab_widget.addTab(characters_view, self.main_window.tr("Characters"))
        right_tab_widget.addTab(creatures_view, self.main_window.tr("Creatures"))
        right_tab_widget.addTab(items_view, self.main_window.tr("Items"))
        right_tab_widget.addTab(self.music_player_view, self.main_window.tr("Music Player"))
        right_tab_widget.addTab(options_view, self.main_window.tr("Options"))

        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.map_view)
        splitter.addWidget(right_tab_widget)
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 0)

        self.action_panel = ActionPanel(self.main_window)
        self.action_panel.setFixedWidth(200)

        main_layout.addWidget(self.toolbar_view)
        main_layout.addWidget(splitter)
        main_layout.addWidget(self.action_panel)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.main_window.setCentralWidget(central_widget)