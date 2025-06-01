from framework.canvas import Canvas
from framework.chore_grapher import choreGrapher
from framework.linear_layout import LinearLayout
from framework.view import LayoutParams


class ViewRootImpl:
    def __init__(self, canvas):
        lp = LayoutParams()
        lp.width = 400
        lp.height = 1200
        lp.background_color = "yellow"
        self.root = LinearLayout(lp)
        self.canvas = canvas

        def do_traversal():
            self.do_traversal()

        choreGrapher.register_callback("traversal", do_traversal)

    def do_traversal(self):
        self.perform_measure()
        self.perform_layout()
        self.perform_draw()

    def perform_measure(self):
        self.root.measure(400, 1200)

    def perform_layout(self):
        self.root.layout(0, 0)

    def perform_draw(self):
        self.root.draw(self.canvas)
