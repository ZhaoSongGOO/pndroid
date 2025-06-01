from framework.button_view import ButtonView
from framework.linear_layout import LinearLayout
from framework.text_view import TextView
from framework.view import LayoutParams

TagToView = {"TextView": TextView, "LinearLayout": LinearLayout, "Button": ButtonView}


class Attributes:
    def __init__(self):
        self.values = {}

    def set_value(self, k, v):
        self.values[k] = v

    def get_value(self, k):
        if k not in self.values.keys():
            return None
        return self.values[k]


def view_factory(tag, attributes: Attributes):
    if tag not in TagToView.keys():
        return None

    lp = LayoutParams()
    width = attributes.get_value("layout_width")
    if width is not None:
        lp.width = int(width)
    height = attributes.get_value("layout_height")
    if height is not None:
        lp.height = int(height)
    background = attributes.get_value("background_color")
    if background is not None:
        lp.background_color = f"{background}"

    id_value = attributes.get_value("id")
    if id_value is not None:
        lp.id = id_value

    view = TagToView[tag](lp)

    if tag == "TextView" or tag == "Button":
        text = attributes.get_value("text")
        view.set_text(text)

    return view
