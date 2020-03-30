from mongoengine_goodjson import Document, EmbeddedDocument
from mongoengine import StringField, DateTimeField, FloatField, EmbeddedDocumentField, BooleanField, IntField, EmbeddedDocumentListField, ListField

# Definizione modelli DB delivery
class TrackingPoint(EmbeddedDocument):
    owner = StringField()
    status = StringField()
    updateAt = DateTimeField()

class geoPoint(EmbeddedDocument):
	latitude = FloatField()
	longitude = FloatField()

class address(EmbeddedDocument):
	description = StringField()
	geoPoint = EmbeddedDocumentField(geoPoint)
	normalized = BooleanField()

class BillingAddress(EmbeddedDocument):
	description = StringField()
	geoPoint = EmbeddedDocumentField(geoPoint)
	normalized = BooleanField()

class Customer(EmbeddedDocument):
    address = EmbeddedDocumentField(address)
    billingAddress = EmbeddedDocumentField(BillingAddress)
    name = StringField()
    surname = StringField()
    email = StringField()
    phoneNumber = StringField()
    fiscalCode = StringField()
    businessName = StringField()
    vatNumber = StringField()
    note = StringField()

class Receiver(EmbeddedDocument):
    address = EmbeddedDocumentField(address)
    name = StringField()
    surname = StringField()
    email = StringField()
    phoneNumber = StringField()
    note = StringField()

class dimension(EmbeddedDocument):
	height = IntField()
	width = IntField()
	depth = IntField()

class package(EmbeddedDocument):
	weight = FloatField()
	dimension = EmbeddedDocumentField(dimension)
	unstackable = BooleanField()
	unflippable = BooleanField()
	fragile = BooleanField()
	permeable = BooleanField()
	note= StringField()

class ServiceOption(EmbeddedDocument):
	_id = StringField()
	deliveryDatetime = DateTimeField()
	width = IntField()
	type = StringField()
	price = FloatField()
	lsp2Services = ListField(StringField())

class Delivery(Document):
	trackingNumber = StringField()
	deliveryNote = StringField()
	trackingHistory = EmbeddedDocumentListField(TrackingPoint)
	customer = EmbeddedDocumentField(Customer)
	receiver = EmbeddedDocumentField(Receiver)
	packages = EmbeddedDocumentListField(package)
	shippingLabel = StringField()
	createdAt = DateTimeField()
	lastUpdateAt = DateTimeField()
	serviceOption = EmbeddedDocumentField(ServiceOption)
	meta = {'collection': 'delivery'}
	_class = StringField()
