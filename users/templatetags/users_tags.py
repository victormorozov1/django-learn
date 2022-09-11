from django import template

from users.models import User

register = template.Library()


@register.simple_tag()
def get_all_users():
    return User.objects.all()
