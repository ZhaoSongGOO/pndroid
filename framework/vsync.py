import threading
from time import sleep

VSYNC_INTERVAL = 0.2


class _VSync:
    def __init__(self):
        self.callbacks = []
        self.loop_enable = True

        def sync_loop():
            while self.loop_enable:
                self.loop()
                sleep(VSYNC_INTERVAL)

        self.thread = threading.Thread(target=sync_loop)

    def loop(self):
        for callback in self.callbacks:
            callback()

    def register_callback(self, callback):
        self.callbacks.append(callback)

    def start(self):
        self.loop_enable = True
        self.thread.start()

    def stop(self):
        self.loop_enable = False
        self.thread.join()


VSync = _VSync()
