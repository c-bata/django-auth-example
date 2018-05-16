from django.template import Library, Node
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name

register = Library()


class PygmentsCss(Node):
    def __init__(self, css_class=".highlight"):
        self.css_class = css_class

    def render(self, context):
        html_formatter = HtmlFormatter()
        styles = html_formatter.get_style_defs(self.css_class)
        return mark_safe(styles)


@register.tag
def pygments_css(parser, token):
    return PygmentsCss()


# register.filter(is_safe=True) はダメ。タグを全て消してしまう。 -> 当然では？
# mark_safeでいいのかちゃんと調べる。攻撃してみる
# https://docs.djangoproject.com/en/2.0/howto/custom-template-tags/

# https://simpleisbetterthancomplex.com/series/2017/10/09/a-complete-beginners-guide-to-django-part-6.html#adding-markdown
# ここもmark_safeだけだな
# そういえばたしかにtemplate_filterじゃなくて、property methodにする手もある
@register.filter
@stringfilter
def pygmentize(value, lexer_name):
    formatter = HtmlFormatter()
    try:
        lexer = get_lexer_by_name(lexer_name)
    except ValueError:
        lexer = get_lexer_by_name('text')
    parsed = highlight(value, lexer, formatter)
    return mark_safe(parsed)
