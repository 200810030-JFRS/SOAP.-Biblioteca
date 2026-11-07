
from zeep import Client

WSDL_URL = "http://127.0.0.1:8000/?wsdl"

CODIGOS = ["LIB-001", "LIB-002", "LIB-999"]

try:
    cliente = Client(WSDL_URL)

    print("Cliente conectado al WSDL:", WSDL_URL)
    print()

    print(f"{'Código':<10} | {'buscar_titulo':<25} | {'Ejempl.':<8} | {'Disp.'}")
    print("-" * 65)

    for codigo in CODIGOS:
        titulo = cliente.service.buscar_titulo(codigo)

        ejemplares = cliente.service.ejemplares_disponibles(codigo)

        disponibilidad = cliente.service.hay_disponibilidad(codigo)

        print(
            f"{codigo:<10} | {titulo:<25} | "
            f"{ejemplares:<8} | {disponibilidad}"
        )

except Exception as error:
    print("No fue posible consumir el servicio SOAP.")
    print("Verifica que Server.py esté ejecutándose y que la URL del WSDL sea correcta.")
    print("Detalle del error:", error)
