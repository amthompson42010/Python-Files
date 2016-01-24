from pb import Phonebook
from contact import Contact
import unittest

class Test_Phonebook(unittest.TestCase):
    def setUp(self):
        self.pb = Phonebook()
        self.contacts = [ Contact("Taco McCat", "205-011-2358"),
                          Contact("Burrito D'Leeto", "256-011-2358"),
                        ]
        self.pb._entries = list(self.contacts)

    def test_init(self):
        self.assertEqual(type(self.pb._entries), list)
        self.assertEqual(type(self.pb._entries[0]), Contact)
        self.assertEqual(type(self.pb._entries[1]), Contact)

    def test_addentry(self):
        self.assertEqual(len(self.pb._entries), 2)

        self.pb.add_entry("Taco McCat", "256-011-2358")
        self.assertEqual(len(self.pb._entries), 3)

    def test_lookup(self):
        self.assertEqual(self.pb.lookup("Taco McCat"), "205-011-2358")
        self.assertEqual(self.pb.lookup("Burrito D'Leeto"), "256-011-2358")

        self.assertEqual(self.pb.lookup("blah"), "Private Number")

    def test_reverse_lookup(self):
        self.assertEqual("Taco McCat", self.pb.reverse_lookup("205-011-2358"))
        self.assertEqual("Burrito D'Leeto", self.pb.reverse_lookup("256-011-2358"))

        self.assertEqual("Unknown", self.pb.reverse_lookup("205-555-5555"))
        self.assertEqual("Unknown", self.pb.reverse_lookup("Taco McCat"))

    def test_size(self):
        self.assertEqual(self.pb.size(), 2)

    def test_str(self):
        expected = "Taco McCat 205-011-2358\nBurrito D'Leeto 256-011-2358\n"

        self.assertEqual(str(self.pb), expected)

if __name__ == '__main__':
    unittest.main()
