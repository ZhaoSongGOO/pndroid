from framework.view import View


class TextView(View):
    def __init__(self, text):
        super().__init__()
        self.text = text

    def on_measure(self, width, height):
        super().on_measure(width, height)

    def on_draw(self, canvas):
        canvas.display(
            f"Draw view in ({self.layout_params.origin}) with ({self.layout_params.width}, {self.layout_params.height}): TextView {self.text}"
        )
