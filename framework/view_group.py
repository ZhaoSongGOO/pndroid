from framework.view import View, LayoutParams


class ViewGroup(View):
    def __init__(self):
        super().__init__()
        self.children = []

    def add_view(self, view: View):
        self.children.append(view)

    def on_measure(self, width, height):
        for view in self.children:
            view.measure(width, height)

    def on_draw(self, canvas):
        canvas.display(
            f"Draw view in ({self.layout_params.origin}) with ({self.layout_params.width}, {self.layout_params.height})"
        )
        for view in self.children:
            view.draw(canvas)

    def on_layout(self, left, top):
        pass
