from unittest import IsolatedAsyncioTestCase

from modulepy.Information import Information, Version


class InformationTests(IsolatedAsyncioTestCase):
    async def test_equal(self):
        info_a = Information("Test", Version(1, 0, 0))
        info_b = Information("Test", Version(1, 0, 0))
        self.assertEqual(info_a, info_b)

    async def test_not_equal(self):
        info_a = Information("Test", Version(1, 0, 0))
        info_b = Information("Test", Version(1, 0, 1))
        self.assertNotEqual(info_a, info_b)
