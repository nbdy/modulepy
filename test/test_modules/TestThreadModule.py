from modulepy import ThreadModule, ModuleInformation, ModuleVersion
from time import sleep


class TestThreadModule(ThreadModule):
    information = ModuleInformation("TestThreadModule", ModuleVersion(1, 0, 0))
    c = 0

    def on_start(self):
        print("TestThreadModule.on_start()")
        self.c = 0

    def on_stop(self):
        print("TestThreadModule.on_stop()")

    def work(self):
        self.c += 1
        print("TestThreadModule.work()")
        if self.c > 5:
            print("TestThreadModule.work() - stop")
            self.stop()
        sleep(1)
