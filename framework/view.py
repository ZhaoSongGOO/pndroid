class LayoutParams:
    def __init__(self):
        self.width = None
        self.height = None
        self.background_color = None
        self.origin = None
        self.id = None


class View:
    def __init__(self, layout_params: LayoutParams):
        self.layout_params = layout_params
        self.origin = self.layout_params.origin

    def measure(self, width, height):
        if self.layout_params.width is None:
            self.layout_params.width = width
        if self.layout_params.height is None:
            self.layout_params.height = height
        self.on_measure(width, height)

    def on_measure(self, width, height):
        pass

    def set_origin(self, origin):
        self.origin = origin

    def layout(self, left, top):
        self.layout_params.origin = (left, top)
        if self.origin is None:
            self.origin = self.layout_params.origin
        self.on_layout(left, top)

    def on_layout(self, left, top):
        pass

    def draw(self, canvas):
        self.on_draw(canvas)

    def on_draw(self, canvas):
        pass

    def add_view(self, view):
        pass
