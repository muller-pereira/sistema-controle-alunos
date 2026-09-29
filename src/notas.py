class Nota:
    def __init__(self, aluno):
        self.aluno = aluno
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def exibir_notas(self):
        print(f"Aluno: {self.aluno}")
        print(f"Notas: {self.notas}")
        print(f"Média: {self.calcular_media():.2f}")


# Exemplo de registro de várias notas
registro = Nota("João Silva")

registro.adicionar_nota(8.5)
registro.adicionar_nota(7.0)
registro.adicionar_nota(9.0)

registro.exibir_notas()
