from collections import deque

class Cola:
    def __init__(self):
        self.items = deque()  
    def encolar(self, item):
        self.items.append(item)  
        print(f"Encolando {item}. Cola actual: {list(self.items)}")

    def desencolar(self):
        if not self.vacia():
            item = self.items.popleft()  
            print(f"Desencolando {item}. Cola actual: {list(self.items)}")
            return item
        else:
            print("La cola está vacía, no se puede desencolar.")
            return None

    def tamano(self):
        return len(self.items)  
    def vercola(self):
        return list(self.items) 

    def vacia(self):
        return len(self.items) == 0  

def sumarcolas(cola_b, cola_a):
    cola_resultado = Cola()
    while not cola_a.vacia() and not cola_b.vacia():
        valor_b = cola_b.desencolar()  
        valor_a = cola_a.desencolar()  
        suma = valor_b + valor_a  
        cola_resultado.encolar(suma) 
    return cola_resultado

cola_a = Cola()
cola_b = Cola()

for num in [32, 4, 2, 4, 12]:
    cola_a.encolar(num)

for num in [6, 2, 7, 115, 3]:
    cola_b.encolar(num)

print("\nSumando las colas...\n")
cola_resultado = sumarcolas(cola_b, cola_a)

print("\nCola Resultado:", cola_resultado.vercola())

