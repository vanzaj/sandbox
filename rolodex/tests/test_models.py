# [x] test for empty first name
# [x] contact has type friend, family, colleague, client, other
# contact can have multiple phone numbers
# contact can have multiple emails

import pytest
from pydantic import ValidationError
from rolodex.contact import Contact, ContactCategory


def test_make_contact_from_valid_dict():
    data = dict(first_name="John", last_name="Doe", category="family")
    a_contact = Contact(**data)
    assert a_contact.name == "John Doe"
    assert a_contact.category == "family"


def test_make_contact_from_first_name_only():
    data = dict(first_name="John")
    a_contact = Contact(**data)
    assert a_contact.name == "John"
    assert a_contact.category == "other"


def test_fail_contact_from_empty_first_name():
    data = dict(first_name=" ")
    with pytest.raises(ValidationError) as exception:
        Contact(**data)
    assert "String should have at least 1 character" in str(exception.value)
