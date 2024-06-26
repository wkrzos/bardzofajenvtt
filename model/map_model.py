from backend.character_sheets.sheets import Character
from backend.mechanics.token import Token

class MapViewModel:
    def __init__(self):
        self.grid_size = 50
        self.offset = (0, 0)
        self.tokens = []
        self.selected_tokens = []
        self.zoom_level = 1.0
        self.dragging = False
        self.measuring = False
        self.measure_start = None
        self.measure_end = None
        self.selecting = False
        self.selection_start = None
        self.selection_end = None

    def get_tokens(self):
        return self.tokens

    def set_offset(self, offset):
        self.offset = offset

    def get_offset(self):
        return self.offset

    def set_zoom_level(self, zoom_level):
        self.zoom_level = zoom_level

    def get_zoom_level(self):
        return self.zoom_level

    def set_selected_tokens(self, tokens):
        self.selected_tokens = tokens

    def get_selected_tokens(self):
        return self.selected_tokens

    def set_measurement(self, start, end):
        self.measure_start = start
        self.measure_end = end

    def get_measurement(self):
        return self.measure_start, self.measure_end

    def set_selection(self, start, end):
        self.selection_start = start
        self.selection_end = end

    def get_selection(self):
        return self.selection_start, self.selection_end
