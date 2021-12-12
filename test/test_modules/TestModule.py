from modulepy import ModuleBase, ModuleInformation, ModuleVersion
from time import sleep


class TestModule(ModuleBase):
    information = ModuleInformation("TestModule", ModuleVersion(1, 0, 0))
    c = 0

    def on_start(self):
        print("TestModule.on_start()")
        self.c = 0

    def on_stop(self):
        print("TestModule.on_stop()")

    def work(self):
        self.c += 1
        print("TestModule.work()")
        if self.c > 5:
            print("TestModule.work() - stop")
            self.stop()
        sleep(1)
