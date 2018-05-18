from django.core.exceptions import ValidationError
from django.test import TestCase

from ..validators import UsernameValidator


class UsernameValidatorsTests(TestCase):
    def test_username_validator(self):
        valid_usernames = ['glenn', 'jean-marc001', 'c-bata']
        invalid_usernames = ['c_bata_', 'GLEnN', "o'connell", 'Éric', 'jean marc', "أحمد"]
        v = UsernameValidator()

        for valid in valid_usernames:
            with self.subTest(valid=valid):
                v(valid)

        for invalid in invalid_usernames:
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValidationError):
                    v(invalid)
