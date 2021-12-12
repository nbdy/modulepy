from modulepy import ModuleLoader


if __name__ == '__main__':
    testModule = ModuleLoader.load_module_in_directory("test_modules/TestModule.py")()
    print(testModule.information)
    testModule.start()
    testModule.join()
