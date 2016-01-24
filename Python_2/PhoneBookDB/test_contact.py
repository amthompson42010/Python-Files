from contact import Contact
import unittest

class Test_Contact(unittest.TestCase):
    def setUp(self):
        self.k = Contact("Taco McCat", "205-011-2358")

    def test_init(self):
        self.assertEqual(self.k._name, "Taco McCat")
        self.assertEqual(self.k._number, "205-011-2358")

    def test_get_name(self):
        self.assertEqual(self.k.get_name(), "Taco McCat")

    def test_get_number(self):
        self.assertEqual(self.k.get_number(), "205-011-2358")

    def test_set_name(self):
        self.k.set_name("💩")

        self.assertEqual(self.k._name, "💩")
        self.assertNotEqual(self.k._name, ":)")

        self.k.set_name(":)")
        self.assertEqual(self.k._name, ":)")

    def test_set_number(self):
        self.k.set_number("asdfsdfdsfsdfsdf")
        self.assertNotEqual(self.k._number, "205-011-2358")
        self.assertEqual(self.k._number, "asdfsdfdsfsdfsdf")

if __name__ == '__main__':
    unittest.main()
