from dataclasses import dataclass

# Stub agent class to illustrate fix
@dataclass
class EPUBIngestorAgent:
    @staticmethod
    def run(entrada):
        # Real implementation would process the input
        return f"processed {entrada}"


def executar_traducao(entrada, saida):
    # Using the correct method name `run` instead of `function`
    raw = EPUBIngestorAgent.run(entrada)
    # Example placeholder for additional logic
    with open(saida, 'w', encoding='utf-8') as f:
        f.write(raw)


if __name__ == "__main__":
    # Example usage
    executar_traducao('entrada.epub', 'saida.epub')
