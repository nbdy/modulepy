from time import sleep
from unittest import TestCase

from modulepy.SharedDict import LocalSharedDict, RemoteSharedDict
from modulepy.Base import Base, Information, Version


class TestModuleOne(Base):
    information = Information("ModuleOne", Version(0, 0, 1))

    def loop(self):
        value = self.data.get("value")
        print("ModuleOne", value)
        if value == "first":
            self.data.set("value", "second")
        sleep(0.2)


class TestModuleTwo(Base):
    information = Information("ModuleTwo", Version(0, 0, 1))

    dependencies = [Information("ModuleOne", Version(0, 0, 1))]

    def loop(self):
        value = self.clients["ModuleOne"].get("value")
        print("ModuleTwo", value)
        if value == "second":
            self.data.set("value", "third")
        sleep(0.2)


class SharedDataTest(TestCase):
    def test_equal(self):
        lsd = LocalSharedDict("sd")
        rsd = RemoteSharedDict("sd")

        lsd.set("test", "test")
        rsd.update()
        self.assertEqual(lsd.get("test"), rsd.get("test"))

        lsd.set("test", "tset")
        self.assertNotEqual(lsd.get("test"), rsd.get("test"))
        rsd.update()
        self.assertEqual(lsd.get("test"), rsd.get("test"))

    def test_modules(self):
        mod_one = TestModuleOne()
        mod_two = TestModuleTwo()

        storage = RemoteSharedDict("ModuleOne")

        mod_one.start()
        mod_two.start()

        storage.set("value", "first")

        while storage.get("value") != "third":
            sleep(0.5)

        self.assertTrue(True)
