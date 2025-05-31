from framework.text_view import TextView
from framework.view_root_impl import ViewRootImpl
from framework.vsync import VSync


VSync.start()
root_impl = ViewRootImpl()
root_impl.root.add_view(TextView("HelloWorld"))
root_impl.root.add_view(TextView("ByeWorld"))
