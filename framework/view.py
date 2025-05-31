class LayoutParams:
    def __init__(self):
        self.width = None
        self.height = None
        self.background_color = None
        self.origin = None


class View:
    def __init__(self):
        self.layout_params = LayoutParams()

    def measure(self, width, height):
        self.layout_params.width = width
        self.layout_params.height = height
        self.layout_params.background_color = "green"
        self.on_measure(width, height)

    def on_measure(self, width, height):
        pass

    def layout(self, left, top):
        self.layout_params.origin = (left, top)
        self.on_layout(left, top)

    def on_layout(self, left, top):
        pass

    def draw(self, canvas):
        self.on_draw(canvas)

    def on_draw(self, canvas):
        pass
