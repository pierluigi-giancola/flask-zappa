import utils.auth as auth
import flask
import routes as r
import controllers.delivery_controller as controller


def get_incompleted_delivery():
    def _get_incompleted_delivery():
        start = flask.request.args.get('start')
        limit = flask.request.args.get('limit')
        return controller.get_uncompleted_delivery_by_customer_email(flask.g.jwt['username'], start=start, limit=limit)
    return r.Route('/deliveries/incompleted', 'GET', [auth.protected, _get_incompleted_delivery])
    

def get_completed_delivery():
    def _get_completed_delivery():
        start = flask.request.args.get('start')
        limit = flask.request.args.get('limit')
        return controller.get_completed_delivery_by_customer_email(flask.g.jwt['username'], start=start, limit=limit)
    return r.Route('/deliveries/completed', 'GET', [auth.protected, _get_completed_delivery])