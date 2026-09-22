from dataclasses import dataclass
from enum import Enum

class Status(str, Enum):
    PENDENTE = "pendente"
    CAPTURADO = "capturado"
    ERRO = "erro"

@dataclass
class Consulta:
    identificador: str
    referencia: str
    status: Status = Status.PENDENTE

def processar(item: Consulta) -> Consulta:
    # Demonstração: em produção, a consulta dependeria de acesso autorizado.
    print(f"Processando {item.identificador} | {item.referencia}")
    item.status = Status.CAPTURADO
    return item

if __name__ == "__main__":
    fila = [Consulta("CLIENTE-DEMO-001", "09/2026")]
    for consulta in fila:
        print(processar(consulta))
