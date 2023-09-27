import random #importa a classe que cria numeros randomicos
from Alunos import Aluno #importamos a classe de Alunos

class Matricula_secretaria:
    def __init__(self) -> None:
        """Cria uma matricula aleatoria para algum aluno
        """
        self.Matricula = random.randint(1,200)


    def AlterarMatriculaAluno(self,Aluno:Aluno):
        """Modifica a matricula do aluno escolhido, para o numero gerado aqui dentro
        Args:
            Aluno (Aluno): Chame um objeto do tipo Aluno e sua matricula sera alterada 
            automaticamente
        """
        Aluno.MatriculaAluno = self.Matricula
        
