from models.delivery import Delivery
import controllers as ctr
import json

@ctr.handle_error
def get_completed_delivery_by_customer_email(customer_email, start=None, limit=None):
    _start = int(start) if start is not None else None
    _limit = int(limit) if limit is not None else None
    # This is Bad, double query but simple to understand
    count = Delivery.objects(customer__email=customer_email,
                            trackingHistory__status='COMPLETED').count()
    data = Delivery.objects(customer__email=customer_email,
                            trackingHistory__status='COMPLETED')[_start:_limit].to_json()
    return json.dumps({'length':count, 'data': json.loads(data)})

@ctr.handle_error
def get_uncompleted_delivery_by_customer_email(customer_email, start=None, limit=None):
    _start = int(start) if start is not None else None
    _limit = int(limit) if limit is not None else None
    # This is Bad, double query but simple to understand
    count = Delivery.objects(customer__email=customer_email,
                            trackingHistory__status__ne='COMPLETED').count()
    data = Delivery.objects(customer__email=customer_email,
                            trackingHistory__status__ne='COMPLETED')[_start:_limit].to_json()
    return json.dumps({'length':count, 'data': json.loads(data)})