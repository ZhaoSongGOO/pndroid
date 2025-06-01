from framework.text_view import TextView


class ButtonView(TextView):
    def __init__(self, layout_params):
        super().__init__(layout_params)
        self.click_handler = None
        self.rect = None
        self.canvas = None

    def on_measure(self, width, height):
        super().on_measure(width, height)

    def on_draw(self, canvas):
        super().on_draw(canvas)
        self.canvas = canvas
        if self.click_handler is not None:
            self.canvas.bind_click_handler(self, self.click_handler)

    def set_on_click_listener(self, click_handler):
        if self.canvas is None:
            self.click_handler = click_handler
            return
        self.canvas.bind_click_handler(self.rect, click_handler)
