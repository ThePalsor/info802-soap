import logging
import os

from spyne.decorator import srpc
from spyne.service import ServiceBase
from spyne.model.complex import ComplexModel
from spyne.model.complex import Iterable
from spyne.model.primitive import Float
from spyne.model.primitive import Unicode

from spyne.util.simple import wsgi_soap_application


class DeliveryFeesService(ServiceBase):
    @srpc(Float, Float, _returns=Float)
    def compute_fees(distance, weight):
        return distance * weight * 0.1


if __name__=='__main__':
    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    port = os.environ['PORT']
    logging.info('Binding to port : ' + str(port))


    wsgi_app = wsgi_soap_application([DeliveryFeesService], 'com.marketplace.delivery')
    server = make_server('127.0.0.1', port, wsgi_app)
    server.serve_forever()