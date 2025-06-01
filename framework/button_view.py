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
        canvas.draw_rectangle(
            self,
            self.origin[0],
            self.origin[1],
            self.layout_params.width,
            self.layout_params.height,
            self.layout_params.background_color,
        )
        x = self.layout_params.origin[0] + self.layout_params.width / 2
        y = self.layout_params.origin[1] + self.layout_params.height / 2
        canvas.draw_text(self, x, y, self.text)
        self.canvas = canvas
        if self.click_handler is not None:
            self.canvas.bind_click_handler(self, self.click_handler)

    def set_on_click_listener(self, click_handler):
        if self.canvas is None:
            self.click_handler = click_handler
            return
        self.canvas.bind_click_handler(self.rect, click_handler)
