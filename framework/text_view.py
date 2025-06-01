from framework.view import View


class TextView(View):
    def __init__(self, layout_params):
        super().__init__(layout_params)
        self.text = None

    def on_measure(self, width, height):
        super().on_measure(width, height)

    def set_text(self, text):
        self.text = text

    def on_draw(self, canvas):
        canvas.draw_rectangle(
            self,
            self.origin[0],
            self.origin[1],
            self.layout_params.width,
            self.layout_params.height,
            self.layout_params.background_color,
        )
        x = self.origin[0] + self.layout_params.width / 2
        y = self.origin[1] + self.layout_params.height / 2
        canvas.draw_text(self, x, y, self.text)
