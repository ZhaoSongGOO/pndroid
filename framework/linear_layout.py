from framework.view_group import ViewGroup


class LinearLayout(ViewGroup):
    def __init__(self, layout_params):
        super().__init__(layout_params)

    def on_measure(self, width, height):
        super().on_measure(width, height)

    def on_layout(self, left, top):
        x = left
        y = top
        for view in self.children:
            view.layout(x, y)
            y += view.layout_params.height
