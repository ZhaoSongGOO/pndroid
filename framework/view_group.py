from framework.view import View, LayoutParams


class ViewGroup(View):
    def __init__(self, layout_params):
        super().__init__(layout_params)
        self.children = []

    def add_view(self, view: View):
        self.children.append(view)

    def on_measure(self, width, height):
        for view in self.children:
            view.measure(width, height)

    def on_draw(self, canvas):
        canvas.draw_rectangle(
            self,
            self.origin[0],
            self.origin[1],
            self.layout_params.width,
            self.layout_params.height,
            self.layout_params.background_color,
        )
        for view in self.children:
            view.draw(canvas)

    def on_layout(self, left, top):
        pass
