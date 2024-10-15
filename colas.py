class colas:
    def __init__(self):
        self.items = []
    def desencolar(self):
        if not self.vacia():
            return self.items.pop()
        else:
            return None
    def encolar(self, item):
        self.items.insert(0, item)
    def tamano(self):
        return len(self.items)
    def vercola(self):
        return self.items
    def vacia(self):
        return len(self.items) == 0
def sumarcolas(cola_b, cola_a):
    cola_resultado = colas()
    while not cola_a.vacia() and not cola_b.vacia():
        valor_b = cola_b.desencolar()
        valor_a = cola_a.desencolar()
        cola_resultado.encolar(valor_b + valor_a)
    return cola_resultado
cola_a = colas()
cola_b = colas()
for num in [32, 4, 2, 4, 12]:
    cola_a.encolar(num)
for num in [6, 2, 7, 115, 3]:
    cola_b.encolar(num)
cola_resultado = sumarcolas(cola_b, cola_a)
print("Cola Resultado:", cola_resultado.vercola())
