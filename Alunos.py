
from Materias import materia

#Criação da Classe de Alunos
#Classe será responsavel por fazer o ingresso de novos alunos
class Aluno:

    def __init__(self,NomeAluno:str,MatriculaAluno:int=0) -> None:
        """Classe responsavel por criar os alunos que serão matriculados dentro do 
        sistema.

        Args:
            NomeAluno (str): Metodo principal e obrigatorio 
            MatriculaAluno (int, optional): Opcional caso não utilize a matricula do aluno será 0.
        """
        self.Nome =NomeAluno #Propriedade da classe Nome
        self.Aulas =[] #Propriedade da classe Aula do Aluno
        self.Notas=[] #Propriedade da classe Notas dos Alunos
        self.MatriculaAluno = MatriculaAluno #Propriedade da classe Matricula do aluno
    

    def ExibirBoletim(self,IndiceMateria:int):
        """Função Responsavel por exibir a nota selecionada dentro do vetor de 
        Nota e de Aulas dos Alunos

        Args:
            IndiceMateria (int): Indice (ou posição) que você deseja acessar da materia escolhida
        """
        print(f"O aluno {self.Nome}, possui nota {self.Nota[IndiceMateria]} na aula {self.Aulas[IndiceMateria]}" )

    def NovaAula(self,Aula):
        """Criar uma nova Aula para o Aluno 

        Args:
            Aula (string): Cria uma nova aula para o Aluno
        """
        self.Aulas.append(Aula)
    def LancarNota(self,Nota:str=0,Indice:int=None):
        """Lanca uma nova nota para a materia escolhida

        Args:
            Nota (str, optional): Cria uma nova nota
            Indice (int, optional): Escolha o indice da materia que será acessado nesse caso usamos o 
            self.Notas[Indice], caso a nota ainda não exista utilize valor como None para criar uma nota, 
            e se quiser alterar a nota coloque o indice que deseja alterar
        """
        if(Indice == None):
            self.Notas.append(Nota)
        else:
            self.Notas[Indice] = Nota

    def AdicionarMaterias(self,materias:materia = materia):
        """Cria uma nova materia para o aluno, essas materias vão cair no formato de dicionario
        onde cada aula terá suas materiais especificas

        Args:
            materias (materia, optional): Chamar um objeto que seja do tipo materia
        """
        self.Aulas.append(materias.Materias)