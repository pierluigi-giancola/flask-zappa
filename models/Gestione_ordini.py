# ### Gestionale ordini ###

# # Questo scrpt deve scaricare gli ordini da consegnare il giorno successivo
# # Gli ordini sono caratterizzati da un numero di pacchi

# # in base al numero di pacchi standard trasportabili, lo script deve raggruppare gli ordini
# # in modo da avere la minima distanza tra gli ordini di uno stesso gruppo e il numero di 
# # pacchi trasportati non superiore al numero di pacchi trasportabili

# # Per ogni gruppo viene calcolato il tragitto minimo, quindi l'ordine di consegna e
# # dic onseguenza l'ordine di carico.

# from mongoengine import *
# import datetime


# # Connessione al DB "Deliveries"
# connect(
#     db='test',
#     username='specificato nell host',
#     password='specificato nell host',
#     host='mongodb+srv://marco:ArUo8AQbWunTmIxn@sandbox-n7cux.mongodb.net/test?retryWrites=true&w=majority'
# )


# # Definizione modelli DB delivery
# class TrackingPoint(EmbeddedDocument):
#     owner = StringField()
#     status = StringField()
#     updateAt = DateTimeField()

# class geoPoint(EmbeddedDocument):
# 	latitude = FloatField()
# 	longitude = FloatField()

# class address(EmbeddedDocument):
# 	description = StringField()
# 	geoPoint = EmbeddedDocumentField(geoPoint)
# 	normalized = BooleanField()

# class BillingAddress(EmbeddedDocument):
# 	description = StringField()
# 	geoPoint = EmbeddedDocumentField(geoPoint)
# 	normalized = BooleanField()

# class Customer(EmbeddedDocument):
#     address = EmbeddedDocumentField(address)
#     billingAddress = EmbeddedDocumentField(BillingAddress)
#     name = StringField()
#     surname = StringField()
#     email = StringField()
#     phoneNumber = StringField()
#     fiscalCode = StringField()
#     businessName = StringField()
#     vatNumber = StringField()
#     note = StringField()

# class Receiver(EmbeddedDocument):
#     address = EmbeddedDocumentField(address)
#     name = StringField()
#     surname = StringField()
#     email = StringField()
#     phoneNumber = StringField()
#     note = StringField()

# class dimension(EmbeddedDocument):
# 	height = IntField()
# 	width = IntField()
# 	depth = IntField()

# class package(EmbeddedDocument):
# 	weight = FloatField()
# 	dimension = EmbeddedDocumentField(dimension)
# 	unstackable = BooleanField()
# 	unflippable = BooleanField()
# 	fragile = BooleanField()
# 	permeable = BooleanField()
# 	note= StringField()

# class ServiceOption(EmbeddedDocument):
# 	_id = StringField()
# 	deliveryDatetime = DateTimeField()
# 	width = IntField()
# 	type = StringField()
# 	price = FloatField()
# 	lsp2Services = ListField(StringField())

# class Delivery(Document):
# 	trackingNumber = StringField()
# 	deliveryNote = StringField()
# 	trackingHistory = EmbeddedDocumentListField(TrackingPoint)
# 	customer = EmbeddedDocumentField(Customer)
# 	receiver = EmbeddedDocumentField(Receiver)
# 	packages = EmbeddedDocumentListField(package)
# 	shippingLabel = StringField()
# 	createdAt = DateTimeField()
# 	lastUpdateAt = DateTimeField()
# 	serviceOption = EmbeddedDocumentField(ServiceOption)
# 	meta = {'collection': 'delivery'}
# 	_class = StringField()

# # Query su ordini per il giorno successivo a nome di uno specifico cliente

# today = datetime.datetime.now().date()
# yesterday = today - datetime.timedelta(days=1)
# tomorrow = today + datetime.timedelta(days=1)
# day_after_tomorrow = today + datetime.timedelta(days=2)
# print('oggi: ', today)
# print('dopodomani: ', day_after_tomorrow)
# print('ieri: ', yesterday)

# query = Delivery.objects(
# 	Q(customer__businessName = "Ok Sigma") #&
# 	#(Q(createdAt__gte = yesterday) | Q(createdAt__gte = today)) &
# 	#Q(serviceOption__deliveryDatetime__gt = today - datetime.timedelta(days=2)) &
# 	#Q(serviceOption__deliveryDatetime__lt = today - datetime.timedelta(days=1))
# 	)

# print('Total available orders: ', query.count())

# for obj in query:
# 	print(obj.receiver.name, ' ', obj.receiver.surname, ' - ', obj.receiver.address.description, obj.receiver.note)
# 	print('Creato: ', obj.createdAt)
# 	print('Stati: ')
# 	print([(item.status, item.updateAt.isoformat()) for item in obj.trackingHistory])
# 	print('Delivery time: ', obj.serviceOption.deliveryDatetime.isoformat())
# 	print('note: ', obj.packages[0].note, '\n')


# # TODO: Raggruppamento ordini in cluster

# # TODO: Ordina spedizioni per sequenza di carico
# # NB: Tenere conto della 

# # TODO:Crea PDF

# # WORKAROUND
# # title = str()
# # file1 = open("Lista spedizioni.txt","w") 

# # date_title = "LISTA SPEDIZIONI - Data: " + str(today) + " \n"
# # file1.write(date_title)

# # stringa_totale = "Totale ordini: " + str(query.count()) +"\n"
# # file1.write(stringa_totale)
# # file1.write("-----------------------------------------------------------------------\n")
# # for obj in query:
# # 	L = ["Nome Cognome: " + obj.receiver.name + " " + obj.receiver.surname + "\n",
# # 		 "Indirizzo: " + obj.receiver.address.description + obj.receiver.note + "\n",
# # 		 "Note spedizione: " + obj.packages[0].note + "\n",
# # 		 "-----------------------------------------------------------------------\n"]

# # 	file1.writelines(L) 

# # file1.close() 


# ####################################

# ### APPUNTI ###

# """

# {
#   "_id": {
#     "$oid": "5e7cd1b7a2d9311a4b566e07"
#   },
#   "trackingNumber": "fPthd9hF108",
#   "trackingHistory": [
#     {
#       "owner": "SYSTEM",
#       "status": "CREATED",
#       "updateAt": {
#         "$date": {
#           "$numberLong": "1585238454765"
#         }
#       }
#     }
#   ],
#   "customer": {
#     "address": {
#       "description": "Viale Romagna, 23, 20133 Milano MI",
#       "geoPoint": {
#         "latitude": {
#           "$numberDouble": "45.472122"
#         },
#         "longitude": {
#           "$numberDouble": "9.223516"
#         }
#       },
#       "normalized": false
#     },
#     "billingAddress": {
#       "description": "Viale Romagna, 23, 20133 Milano MI",
#       "geoPoint": {
#         "latitude": {
#           "$numberDouble": "45.472122"
#         },
#         "longitude": {
#           "$numberDouble": "9.223516"
#         }
#       },
#       "normalized": false
#     },
#     "name": "Simone e Matteo",
#     "surname": "Salvini",
#     "email": "simatsnc@outlook.it",
#     "phoneNumber": "0270105892",
#     "fiscalCode": "09746990960",
#     "businessName": "Ok Sigma",
#     "vatNumber": "09746990960",
#     "note": "8:00-13:30, 15:00-20:00"
#   },
#   "receiver": {
#     "address": {
#       "description": "Piazza Ermete Novelli, 10, Milano, MI, Italia",
#       "geoPoint": {
#         "latitude": {
#           "$numberDouble": "45.47042940000001"
#         },
#         "longitude": {
#           "$numberDouble": "9.2198941"
#         }
#       }
#     },
#     "name": " ",
#     "surname": "Cozzarini",
#     "email": "simatsnc@outlook.it",
#     "phoneNumber": "3318535708",
#     "note": "citofono Cozzarini"
#   },
#   "packages": [
#     {
#       "weight": "10",
#       "dimension": {
#         "height": "60",
#         "width": "40",
#         "depth": "40"
#       },
#       "unstackable": true,
#       "unflippable": true,
#       "fragile": true,
#       "permeable": true,
#       "note": "2 collo, di cui 1 acqua"
#     }
#   ],
#   "shippingLabel": "https://elasticbeanstalk-eu-west-1-099241352156.s3.eu-west-1.amazonaws.com/Etichetta/fPthd9hF108.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20200326T160055Z&X-Amz-SignedHeaders=host&X-Amz-Expires=547144&X-Amz-Credential=AKIAROGZ63POK7MKL65P%2F20200326%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Signature=1025c81e38e66f76d1892a261a9549cb6ff93a0c473aa0db68767d70ec351d2b",
#   "createdAt": {
#     "$date": {
#       "$numberLong": "1585238454765"
#     }
#   },
#   "lastUpdateAt": {
#     "$date": {
#       "$numberLong": "1585238454765"
#     }
#   },


#   "serviceOption": {
#     "_id": {
#       "$oid": "5e7b9a3b14bba9716ef7d8e7"
#     },
#     "deliveryDatetime": {
#       "$date": {
#         "$numberLong": "1585339200000"
#       }
#     },
#     "width": {
#       "$numberInt": "11"
#     },
#     "type": "STD",
#     "price": {
#       "$numberDouble": "8.49"
#     },
#     "lsp2Services": [
#       "CDM_STD_w10_dim[120, 40, 40]_dist18_Af1_At1"
#     ]
#   },
#   "_class": "com.blink.blinkapi.domain.model.DeliveryDTO"
# }

# """
