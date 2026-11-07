
from spyne import Application, rpc, ServiceBase, Unicode, Integer, Boolean
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

CATALOGO = {
    "LIB-001": {"titulo": "Diario de una pasión","ejemplares": 3},
    "LIB-002": {"titulo": "La cabaña negra","ejemplares": 0},
}


class BibliotecaService(ServiceBase):

    @rpc(Unicode, _returns=Unicode)
    def buscar_titulo(ctx, codigo):
        libro = CATALOGO.get(codigo)
        return libro["titulo"] if libro else "No encontrado"

    @rpc(Unicode, _returns=Integer)
    def ejemplares_disponibles(ctx, codigo):
        libro = CATALOGO.get(codigo)
        return libro["ejemplares"] if libro else 0

    @rpc(Unicode, _returns=Boolean)
    def hay_disponibilidad(ctx, codigo):
        libro = CATALOGO.get(codigo)
        return bool(libro and libro["ejemplares"] > 0)


application = Application(
    [BibliotecaService],
    tns="biblioteca.soa",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11()
)

wsgi_application = WsgiApplication(application)


if __name__ == "__main__":
    server = make_server("127.0.0.1", 8000, wsgi_application)

    print("Servidor SOAP de biblioteca iniciado.")
    print("WSDL disponible en: http://127.0.0.1:8000/?wsdl")
    print("Presiona Ctrl+C para detener el servidor.")

    server.serve_forever()
