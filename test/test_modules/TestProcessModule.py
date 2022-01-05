from modulepy import ModuleBase, ModuleInformation, ModuleVersion
from time import sleep


class TestProcessModule(ModuleBase):
    information = ModuleInformation("TestProcessModule", ModuleVersion(1, 0, 0))
    c = 0

    def on_start(self):
        print("TestProcessModule.on_start()")
        self.c = 0

    def on_stop(self):
        print("TestProcessModule.on_stop()")

    def work(self):
        self.c += 1
        print("TestProcessModule.work()")
        if self.c > 5:
            print("TestProcessModule.work() - stop")
            self.stop()
        sleep(1)
