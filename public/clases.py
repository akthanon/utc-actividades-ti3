from dataclasses import dataclass
from abc import ABC, abstractmethod

# ----------------------------------------------------------
# 🧾 Lista global que guardará automáticamente a todos
# los combatientes creados (ya sean predefinidos o personalizados)
# ----------------------------------------------------------
combatientes = []

# ----------------------------------------------------------
# 🧩 CLASE BASE ABSTRACTA: Combatiente
# ----------------------------------------------------------
# Esta clase define el "molde" que todos los combatientes deben seguir.
# No se puede instanciar directamente porque es abstracta (ABC).
# Obliga a todas las subclases a implementar el método atacar().
# ----------------------------------------------------------
class Combatiente(ABC):
    def __init__(self):
        # Cada vez que se crea un combatiente, se agrega automáticamente
        # a la lista global. Así no hay que añadirlos manualmente.
        combatientes.append(self)

    @abstractmethod
    def atacar(self):
        # Método que todas las subclases DEBEN definir.
        pass


# ----------------------------------------------------------
# 🧙‍♂️ CLASES HIJAS: Combatientes predefinidos
# ----------------------------------------------------------
# Cada clase hereda de Combatiente y define su propio ataque.
# ----------------------------------------------------------

class Mago(Combatiente):
    def lanzar_hechizo(self):
        print("💥 El mago lanza un hechizo: Expeliarmus!")

    def atacar(self):
        # Cumple el contrato del método abstracto
        self.lanzar_hechizo()


class Arquero(Combatiente):
    def lanzar_flecha(self):
        print("🏹 El arquero dispara una flecha: Pium Pium!")

    def atacar(self):
        self.lanzar_flecha()


class Guerrero(Combatiente):
    def lanzar_golpe(self):
        print("⚔️ El guerrero lanza un golpe: ZASCA!!!")

    def atacar(self):
        self.lanzar_golpe()


class Abuela(Combatiente):
    def lanzar_zapatilla(self):
        print("👵 La abuela lanza su zapatilla: ¡Chanclazo!")

    def atacar(self):
        self.lanzar_zapatilla()


# ----------------------------------------------------------
# 🧍‍♂️ CLASE HIJA: Personaje personalizado
# ----------------------------------------------------------
# Permite crear combatientes con nombre y ataque definidos por el jugador.
# Hereda de Combatiente, por lo que también se registra automáticamente.
# ----------------------------------------------------------
class Personaje(Combatiente):
    def __init__(self, nombre, ataque):
        # *IMPORTANTE* llamar a super().__init__() para registrarse
        super().__init__()
        self.nombre = nombre
        self.ataque = ataque

    def ejecutar_ataque(self):
        print(f"{self.nombre} usa su ataque: {self.ataque}!")

    def atacar(self):
        # Cumple el método abstracto con su propio comportamiento
        self.ejecutar_ataque()


# ----------------------------------------------------------
# ⚔️ CLASE Equipo
# ----------------------------------------------------------
# Representa a un grupo de combatientes listos para pelear.
# Al atacar, recorre la lista global "combatientes"
# y ejecuta el ataque de cada uno.
# ----------------------------------------------------------
@dataclass
class Equipo:
    def atacar(self):
        print("\n🔥 El equipo entra en combate!\n")
        for combatiente in combatientes:
            combatiente.atacar()


# ----------------------------------------------------------
# 💡 EJEMPLO DE USO
# ----------------------------------------------------------
# Se crean personajes personalizados y predefinidos.
# Todos se agregan automáticamente al equipo global.
# ----------------------------------------------------------

philip = Personaje("Philipino", "Cuackeado")
martinator = Personaje("Martinator", "Super salto")

Mago()
Arquero()
Guerrero()
Abuela()

# Verificamos qué combatientes se registraron
print("\n📜 Lista de combatientes registrados:")
print([type(c).__name__ for c in combatientes])

# Creamos el equipo y los hacemos atacar
equipo = Equipo()
equipo.atacar()



##############################################
#Fragmento de codigo para eliminar instancias#
##############################################
#Opcion 1
class MiClase:
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"Instancia {self.nombre} creada")
    
    def __del__(self):
        # Este método se llama cuando el objeto está a punto de ser destruido
        print(f"Instancia {self.nombre} destruida")

# Crear una instancia
objeto = MiClase("Objeto1")

# Eliminar la referencia al objeto
del objeto


#Opcion 2
class Coche:
    def __init__(self, marca):
        self.marca = marca
    def __repr__(self):
        return f"Coche('{self.marca}')"
    # __eq__ permite comparar objetos por su valor si es necesario, 
    # aunque .remove() usualmente funciona por identidad de objeto si no se define.

coche_a_eliminar = Coche("Ford") 
lista_coches = [Coche("Toyota"), coche_a_eliminar, Coche("BMW")]

print(f"Antes: {lista_coches}")

# Elimina el objeto específico al que apunta 'coche_a_eliminar'
lista_coches.remove(coche_a_eliminar)

print(f"Después: {lista_coches}")
# Resultado: Después: [Coche('Toyota'), Coche('BMW')]

