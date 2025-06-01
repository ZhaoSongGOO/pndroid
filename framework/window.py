from framework.canvas import Canvas
from framework.layout_loader import get_root
from framework.view_factory import view_factory, Attributes
from framework.view_root_impl import ViewRootImpl
from framework.vsync import VSync
import tkinter as tk
from datetime import datetime


class Window:
    def __init__(self):
        self.vsync = VSync
        self.impls = None
        self.width = 400
        self.height = 1200
        self.title = "Pndroid"
        self.display = tk.Tk()
        self.display.title(self.title)
        self.canvas = tk.Canvas(
            self.display, width=self.width, height=self.height, bg="white"
        )
        self.canvas.pack()
        self.vsync.start()

        def on_close():
            self.close()

        self.display.protocol("WM_DELETE_WINDOW", on_close)

    def run(self):
        self.display.mainloop()

    def find_view_by_id_aux(self, view, id_value: str):
        if view.layout_params.id == id_value:
            return view
        if hasattr(view, "children"):
            children = view.children
            if children is not None:
                for child in children:
                    v = self.find_view_by_id_aux(child, id_value)
                    if v is not None:
                        return v
        return None

    def find_view_by_id(self, id_value: str):
        if self.impls is None:
            return None
        return self.find_view_by_id_aux(self.impls.root, id_value)

    def _get_sub_view(self, root):
        attributes = Attributes()
        for k in root.attrib.keys():
            attributes.set_value(k, root.attrib[k])
        root_view = view_factory(root.tag, attributes)

        if root_view is None:
            return
        for child in root:
            sub_view = self._get_sub_view(child)
            if sub_view is not None:
                root_view.add_view(sub_view)
        return root_view

    def load(self, layout_file):
        root_impl = ViewRootImpl(Canvas(self.canvas, self.display))
        content = get_root(layout_file)
        content_view = self._get_sub_view(content)
        if content_view is None:
            return
        root_impl.root.add_view(content_view)
        self.impls = root_impl

        def click_handler(event):
            v = self.find_view_by_id("hello")
            text = f"{datetime.now()}"
            v.set_text(text)
            v = self.find_view_by_id("bye")
            origin = v.origin
            v.set_origin((origin[0] + 10, origin[1]))

        self.find_view_by_id("button").set_on_click_listener(click_handler)

    def close(self):
        self.vsync.stop()
        self.display.destroy()
