from django import template

register = template.Library()

@register.filter
def format_duration(value):
    try:
        total_seconds = int(value.total_seconds())
        minutes, seconds = divmod(total_seconds, 60)
        return f"{minutes}:{seconds:02}"
    except:
        return ""
