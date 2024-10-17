from collections import deque

class Cliente:
    def __init__(self, nombre, servicio, es_prime=False):
        self.nombre = nombre
        self.servicio = servicio
        self.es_prime = es_prime

    def __repr__(self):
        return f"{self.nombre} (Prime)" if self.es_prime else self.nombre

class Cola:
    def __init__(self):
        self.normales = deque()
        self.prime = deque()

    def encolar(self, cliente):
        (self.prime if cliente.es_prime else self.normales).append(cliente)

    def desencolar(self):
        return self.prime.popleft() if self.prime else self.normales.popleft() if self.normales else None

    def ver_colas(self):
        return list(self.prime), list(self.normales)

    def vacia(self):
        return not self.prime and not self.normales

class SistemaAtencion:
    def __init__(self):
        self.servicios = {
            1: "Consulta General",
            2: "Reclamaciones",
            3: "Nuevas Pólizas",
            4: "Renovaciones",
            5: "Asesoría Financiera"
        }
        self.colas = {s: Cola() for s in self.servicios}

    def agregar_cliente(self, nombre, servicio, es_prime=False):
        if servicio in self.colas:
            cliente = Cliente(nombre, servicio, es_prime)
            self.colas[servicio].encolar(cliente)
            self.mostrar_colas()
        else:
            print("Servicio inválido.")

    def atender_cliente(self, servicio):
        if servicio in self.colas:
            cliente = self.colas[servicio].desencolar()
            if cliente:
                print(f"Atendiendo a: {cliente}")
            else:
                print(f"No hay clientes en la cola de {self.servicios[servicio]}.")
            self.mostrar_colas()

    def mostrar_colas(self):
        for s, cola in self.colas.items():
            prime, normales = cola.ver_colas()
            print(f"Cola {s} - {self.servicios[s]}:\n   Prime: {prime}\n   Normal: {normales}")
        print()

    def mostrar_servicios(self):
        print("\n".join([f"{k}: {v}" for k, v in self.servicios.items()]))

def main():
    sistema = SistemaAtencion()

    while True:
        sistema.mostrar_servicios()
        entrada = input("Ingrese 'C nombre servicio [P]' para agregar o 'A servicio' para atender ('salir' para terminar): ").strip().split()
        if entrada[0].lower() == 'salir':
            break
        if entrada[0].upper() == 'C' and len(entrada) >= 3:
            nombre, servicio = entrada[1], int(entrada[2])
            es_prime = len(entrada) == 4 and entrada[3].upper() == 'P'
            sistema.agregar_cliente(nombre, servicio, es_prime)
        elif entrada[0].upper() == 'A' and len(entrada) == 2:
            sistema.atender_cliente(int(entrada[1]))
        else:
            print("Entrada no válida.")

if __name__ == "__main__":
    main()
