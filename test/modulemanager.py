from modulepy import ModuleManager, ModuleBase, ModuleInformation, ModuleVersion
from time import sleep


class InlineModule(ModuleBase):
    information = ModuleInformation("InlineModule", ModuleVersion(1, 0, 0))

    def work(self):
        print("InlineModule.work()")
        sleep(1)


if __name__ == '__main__':
    mm = ModuleManager()
    mm.module_directory_path = "test_modules"
    mm.reload()
    print(mm.get_module_count())
    mm.add_module(InlineModule())
    print(mm.get_module_count())
    mm.start()
    sleep(10)
    mm.remove_module("InlineModule")
    sleep(3)
    print(mm.get_module_count())
    mm.stop()
    mm.join()
