import re

from django.core import validators
from django.utils.deconstruct import deconstructible


@deconstructible
class UsernameValidator(validators.RegexValidator):
    regex = r'^[a-z0-9-]+$'
    message = (
        'Enter a valid username. This value may contain only'
        ' English small letters, numbers and hyphen.'
    )
    flags = re.ASCII
