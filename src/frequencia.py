class Frequencia:
    def __init__(self, aluno):
        self.aluno = aluno
        self.presencas = 0
        self.faltas = 0

    def registrar_presenca(self):
        self.presencas += 1

    def registrar_falta(self):
        self.faltas += 1

    def exibir_frequencia(self):
        print(f"Aluno: {self.aluno}")
        print(f"Presenças: {self.presencas}")
        print(f"Faltas: {self.faltas}")


# Exemplo de registro de frequência
frequencia = Frequencia("João Silva")

frequencia.registrar_presenca()
frequencia.registrar_presenca()
frequencia.registrar_falta()

frequencia.exibir_frequencia()