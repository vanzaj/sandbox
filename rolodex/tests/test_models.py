# [x] test for empty first name
# [x] contact has type friend, family, colleague, client, other
# contact can have multiple phone numbers
# contact can have multiple emails

import pytest
from pydantic import ValidationError
from rolodex.contact import Contact


def test_make_contact():
    a_contact = Contact(first_name="John", last_name="Doe", category="family")
    assert a_contact.name == "John Doe"
    assert a_contact.category == "family"


def test_make_contact_from_first_name_only():
    a_contact = Contact(first_name="John")
    assert a_contact.name == "John"
    assert a_contact.category == "other"


def test_make_contact_from_empty_first_name_throws_error():
    with pytest.raises(ValidationError) as exception:
        Contact(first_name=" ")
    assert "should have at least 1 character" in str(exception.value)
