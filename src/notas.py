class Nota:
    def __init__(self, aluno, nota):
        self.aluno = aluno
        self.nota = nota

    def exibir_nota(self):
        print(f"Aluno: {self.aluno}")
        print(f"Nota: {self.nota}")


# Exemplo de registro de nota
registro = Nota("João Silva", 8.5)
registro.exibir_nota()