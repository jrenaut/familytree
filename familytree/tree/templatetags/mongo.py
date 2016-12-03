from django import template
register = template.Library()

@register.filter(name="mongo_id")
def mongo_id(dict_rep):
    return dict_rep["_id"]
