from modulepy import ModuleLoader
from time import sleep


def test_module(module, seconds: int = 2):
    print(f"Testing: {module.information}")
    module.start()
    sleep(seconds)
    module.stop()


def test_process_module():
    test_module(ModuleLoader.load_module_in_directory("test_modules/TestProcessModule.py")())


def test_thread_module():
    test_module(ModuleLoader.load_module_in_directory("test_modules/TestThreadModule.py")())


if __name__ == '__main__':
    test_process_module()
    test_thread_module()
