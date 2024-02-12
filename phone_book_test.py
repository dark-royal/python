import unittest
from phone_book_1 import contacts


def test_add_contact():
    phone_book_1 = contacts()
    contacts.add_contact('praise', '09028979349')
    assert contacts.add_contact('praise') == '09028979349'
