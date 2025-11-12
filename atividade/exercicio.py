def somar(a: int, b: int) -> int:
    return a + b

def subtrair(a: int, b: int) -> int:
    return a - b

def multiplicar(a: int, b: int) -> int:
    return a * b

def dividir(a: int, b: int) -> int:
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a // b  # divisão inteira (use / se quiser float)


from typing import Callable

def operar(a: int, b: int, funcao: Callable[[int, int], int]) -> int:
    return funcao(a, b)

# Exemplo de uso
print("Soma:", operar(10, 5, somar))
print("Subtração:", operar(10, 5, subtrair))
print("Multiplicação:", operar(10, 5, multiplicar))
print("Divisão:", operar(10, 5, dividir))


def somar_float(a: int | float, b: int | float) -> float:
    return float(a + b)

# Exemplo
print("Soma float:", somar_float(5, 2.5))


from abc import ABC, abstractmethod
from typing import List

class InstrumentoMusical(ABC):
    @abstractmethod
    def tocar(self) -> None:
        pass

class Violao(InstrumentoMusical):
    def tocar(self) -> None:
        print("🎸 Tocando violão acústico...")

class Guitarra(InstrumentoMusical):
    def tocar(self) -> None:
        print("🎶 Tocando guitarra elétrica...")

class Bateria(InstrumentoMusical):
    def tocar(self) -> None:
        print("🥁 Tocando bateria com energia!")

class Baixo(InstrumentoMusical):
    def tocar(self) -> None:
        print("🎵 Tocando baixo marcante...")

class Piano(InstrumentoMusical):
    def tocar(self) -> None:
        print("🎹 Tocando piano suave...")

# Criar lista de instrumentos
instrumentos: List[InstrumentoMusical] = [
    Violao(), Guitarra(), Bateria(), Baixo(), Piano(),
    Guitarra(), Violao(), Bateria(), Piano(), Baixo()
]

# Tocar todos
for instrumento in instrumentos:
    instrumento.tocar()


class Veiculo(ABC):
    @abstractmethod
    def mover(self) -> None:
        pass

class Carro(Veiculo):
    def mover(self) -> None:
        print("🚗 O carro está andando na estrada.")

class Moto(Veiculo):
    def mover(self) -> None:
        print("🏍️ A moto está acelerando na pista.")

class Bicicleta(Veiculo):
    def mover(self) -> None:
        print("🚴 A bicicleta está pedalando no parque.")

class Aviao(Veiculo):
    def mover(self) -> None:
        print("✈️ O avião está voando pelos céus.")

class Barco(Veiculo):
    def mover(self) -> None:
        print("🚤 O barco está navegando no mar.")

# Lista com 10 veículos
veiculos: List[Veiculo] = [
    Carro(), Moto(), Bicicleta(), Aviao(), Barco(),
    Carro(), Moto(), Bicicleta(), Aviao(), Barco()
]

# Mover todos
for veiculo in veiculos:
    veiculo.mover()
    
