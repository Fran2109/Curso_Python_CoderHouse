from paquete1.modulo2 import Cliente

cliente = Cliente("Francisco", "Filosi", 21, 250, "francisco.filosi3@gmail.com", ["Autos", "Motos", "Tecnologia"])

print(cliente)

cliente.compra(254)
cliente.enviar_mail("Hola hay ofertas en lacteos")
cliente.validar_gusto("Motos")
cliente.validar_gusto("Musica")
cliente.agregar_gusto("Deportes")
cliente.quitar_gusto("Autos")

print(cliente)