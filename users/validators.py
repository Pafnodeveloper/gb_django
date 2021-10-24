from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def validate_email(value):
    if not ("email@ivan.com" in value):
        raise ValidationError(_("Not a valid email. Try one more time"))
    return value
