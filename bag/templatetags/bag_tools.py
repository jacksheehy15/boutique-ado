from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
<<<<<<< HEAD
    return price * quantity
=======
    return price * quantity
>>>>>>> 5dc7bd346f33bb77d3fff5ded7b9b3ec79c5b32e
