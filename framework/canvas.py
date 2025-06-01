class Canvas:
    def __init__(self, canvas, root):
        self.canvas = canvas
        self.root = root
        self.map = {}

    def draw_rectangle(self, v, x, y, w, h, bg):
        print(f"Draw in {x}, {y}, {w}, {h}, {bg}")

        def handler_internal():
            graph = self.canvas.create_rectangle(x, y, x + w, y + h, fill=bg)
            self.map[f"{id(v)}"] = graph

        self.run_on_ui(handler_internal)

    def draw_text(self, v, x, y, text):
        def handler_internal():
            graph = self.canvas.create_text(x, y, text=text, fill="white")
            self.map[f"{id(v)}"] = graph

        self.run_on_ui(handler_internal)

    def run_on_ui(self, handler):
        self.root.after(0, handler)

    def bind_click_handler(self, v, handler):
        def handler_internal():
            key = f"{id(v)}"
            if key not in self.map.keys():
                return
            graph = self.map[key]
            self.canvas.tag_bind(graph, "<Button-1>", handler)

        self.run_on_ui(handler_internal)
