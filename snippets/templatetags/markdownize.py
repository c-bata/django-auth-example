from django.template import Library
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from markdown import markdown

register = Library()


@register.filter
@stringfilter
def markdownize(value):
    return mark_safe(markdown(value, safe_mode='escape'))
