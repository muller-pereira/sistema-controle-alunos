class Aluno:
    def __init__(self, nome, matricula, turma):
        self.nome = nome
        self.matricula = matricula
        self.turma = turma

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Matrícula: {self.matricula}")
        print(f"Turma: {self.turma}")


# Exemplo de cadastro
aluno1 = Aluno("João Silva", "2026001", "7º A")
aluno1.exibir_dados()