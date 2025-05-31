from framework.vsync import VSync


class ChoreGrapher:
    def __init__(self):
        def vsync_callback():
            self.vsync_callback()

        VSync.register_callback(vsync_callback)
        self.callbacks = {}

    def register_callback(self, category, callback):
        if category not in self.callbacks.keys():
            self.callbacks[category] = [callback]
        else:
            self.callbacks[category].append(callback)

    def vsync_callback(self):
        for category in self.callbacks.keys():
            callbacks = self.callbacks[category]
            for callback in callbacks:
                callback()


choreGrapher = ChoreGrapher()
