class Cola:
    def __init__(self):
        self.items = []
    
    def encolar(self, item):
        self.items.append(item)  
    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0) 
        return None
    
    def esta_vacia(self):
        return len(self.items) == 0

class SistemaColas:
    def __init__(self):
        self.servicios = {} 
    def llegada_cliente(self, numero_servicio):
        if numero_servicio not in self.servicios:
            self.servicios[numero_servicio] = Cola()  
        numero_atencion = len(self.servicios[numero_servicio].items) + 1
        self.servicios[numero_servicio].encolar(numero_atencion)
        print(f"Cliente {numero_atencion} en el servicio {numero_servicio}")

    def atender_cliente(self, numero_servicio):
        if numero_servicio in self.servicios and not self.servicios[numero_servicio].esta_vacia():
            cliente_atendido = self.servicios[numero_servicio].desencolar()
            print(f"Atendiendo al cliente {cliente_atendido} del servicio {numero_servicio}")
        else:
            print(f"No hay clientes en la cola del servicio {numero_servicio}")


sistema = SistemaColas()

while True:
    entrada = input("Ingrese 'C' +  el número de servicio para llegada o 'A' + el número para atender (o 'Salir' para terminar): ").upper().strip()
    
    if entrada.startswith('C'):
        numero_servicio = int(entrada[1:])
        sistema.llegada_cliente(numero_servicio)
    
    elif entrada.startswith('A'):
        numero_servicio = int(entrada[1:])
        sistema.atender_cliente(numero_servicio)
    
    elif entrada == 'Salir':
        break
    else:
        print("Entrada invalida")