from django.template import Library

register = Library()


@register.filter("add_class")
def add_class(field, cls_name):
    cls_attr = field.field.widget.attrs.get("class", "") + " " + cls_name
    field.field.widget.attrs.update({"class": cls_attr})
    return field
