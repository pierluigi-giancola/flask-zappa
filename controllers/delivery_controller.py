from models.delivery import Delivery
import controllers as ctr

@ctr.handle_error
def get_completed_delivery_by_customer_email(customer_email, start=None, limit=None):
    return Delivery.objects(customer__email=customer_email,
                            trackingHistory__status='COMPLETED')[int(start):int(limit)]

@ctr.handle_error
def get_uncompleted_delivery_by_customer_email(customer_email, start=None, limit=None):
    return Delivery.objects(customer__email=customer_email,
                            trackingHistory__status__ne='COMPLETED')[int(start):int(limit)]
