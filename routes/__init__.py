"""
Quando da fuori si importa routes si possono importare tutte le funzioni definite nei file
.py di routes.

Questo permette di scrivere le routes con semplicità dividendole per i vari dati e senza preoccuparsi
di come il server le crea.

COSA MOLTO MOLTO IMPORTANTE:
nei file definiti in routes evitare assolutamente di usare:
from package import <qualcosa che sia una funzione>
perchè questa verrà messa nella variabile routes e usata impropriamente.
"""
import os, inspect, importlib

__module = []

for module in os.listdir(os.path.dirname(__file__)):
    if module[-3:] != '.py' or module.startswith('_'):
        continue
    __module.append(importlib.import_module('.'+module[:-3], __name__))

__temp = []
for i in range(len(__module)):
    __temp = __temp + [val for key, val in inspect.getmembers(__module[i]) if inspect.isfunction(val)]

#This allow to export all function using the name of the folder: from folder import folder which i think is super duper cool
#BUT the pylint can't detect dynami variable so it's gona report this as false positive, for semplicity I'll comment this and manually
#create the variable
# vars()[__name__] = __temp
routes = __temp

class Route:
    """
    Parameters
    ----------
    path : str
        the path of the endpoint.
        eg: '/path'
        For declare path params do:
        '/path/<path_param>'
        note that they should match the handler function:
        def handler(path_param):...
    method : str
        [GET, PUT, POST, DELETE]
    handler : list(function)
        list of function. the last function is the handler and all the other must be decorators.
        in normal Flask you should do
        @app.route
        @private
        def handler():...
        the equivalent with this is:
        [private, handler]
        Just as a note: the first decorators is applied for last.
    """
    def __init__(self, path, method, handler):
        self.path = path
        self.method = [method]
        handler.reverse()
        self.handler = handler[0]
        for fun in handler[1:]:
            self.handler = fun(self.handler)

    def register(self, app):
        """
        Given an app 
        """
        app.route(self.path, methods=self.method)(self.handler)