from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_order_total_on_save(sender, instance, **kwargs):
    """
    Update order total on lineitem save.
    """
    order = instance.order
    order.total_cost = sum(item.line_total for item in order.line_items.all())
    order.final_price = max(order.total_cost - order.discount_amount + order.delivery_fee, 0)
    order.save()


@receiver(post_delete, sender=OrderLineItem)
def update_order_total_on_save(sender, instance, **kwargs):
    """
    Update order total when a line is deleted. 
    """
    order = instance.order
    order.total_cost = sum(item.line_total for item in order.line_items.all()) if order.line_items.exists() else 0
    order.final_price = max(order.total_cost - order.discount_amount + order.delivery_fee, 0)
    order.save()
