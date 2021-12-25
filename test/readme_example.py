from modulepy import ThreadModule, ProcessModule, ModuleInformation, ModuleVersion, SharedData, ModuleManager


class ModuleA(ThreadModule):
    information = ModuleInformation("A", ModuleVersion(1, 0, 0))
    dependencies = [ModuleInformation("B", ModuleVersion(1, 0, 0))]

    def work(self):
        self.enqueue({"A": 0})

    def process_input_data(self, data: SharedData):
        print(data)


class ModuleB(ProcessModule):
    information = ModuleInformation("B", ModuleVersion(1, 0, 0))

    def work(self):
        self.enqueue({"B": 1})


if __name__ == '__main__':
    manager = ModuleManager()
    manager.add_module(ModuleA())
    manager.add_module(ModuleB())
    manager.start()
    manager.join()
