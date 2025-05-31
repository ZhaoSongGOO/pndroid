from framework.canvas import Canvas
from framework.chore_grapher import choreGrapher
from framework.linear_layout import LinearLayout


class ViewRootImpl:
    def __init__(self):
        self.root = LinearLayout()
        self.canvas = Canvas()

        def do_traversal():
            self.do_traversal()

        choreGrapher.register_callback("traversal", do_traversal)

    def do_traversal(self):
        self.perform_measure()
        self.perform_layout()
        self.perform_draw()

    def perform_measure(self):
        self.root.measure(100, 100)

    def perform_layout(self):
        self.root.layout(0, 0)

    def perform_draw(self):
        self.root.draw(self.canvas)
