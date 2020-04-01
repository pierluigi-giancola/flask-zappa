from models.delivery import Delivery
import controllers as ctr

@ctr.handle_error
def get_completed_delivery_by_customer_email(customer_email, start=None, limit=None):
    _start = int(start) if start is not None else None
    _limit = int(limit) if limit is not None else None
    return Delivery.objects(customer__email=customer_email,
                            trackingHistory__status='COMPLETED')[_start:_limit]

@ctr.handle_error
def get_uncompleted_delivery_by_customer_email(customer_email, start=None, limit=None):
    _start = int(start) if start is not None else None
    _limit = int(limit) if limit is not None else None
    return Delivery.objects(customer__email=customer_email,
                            trackingHistory__status__ne='COMPLETED')[_start:_limit]
