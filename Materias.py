#criando a classe de Materias ou aulas apenas de back end
class aulas_backEnd:
    def __init__(self) -> None:
        """
        Classe com as materias base de back end
        """
        self.materias_backEnd = {"Orientacao a objeto":"backEnd","Banco de dados":"backEnd","Python":"backEnd"}

    def TrasnferirParaMaterias(self,materia):
        """Função para transforar uma lista de materiais apenas para back end
        Args:
            materia (materia, optional): Passando o objeto que você deseja alterar.
        """
        materia.Materias = self.materias

#Criando a classe de materias 
class materia(aulas_backEnd): 
    def __init__(self,NovaMateria:str,gradeCurricular:str="Backend") -> None:
        super().__init__()
        """Classe responsavel por criar novas materiais e adicionar nos
        objetos dos alunos

        Args:
            NovaMateria (str): Nome da materia que deseja criar
            gradeCurricular (str, optional): A qual curso essa materia pertence.
        """
        self.Materias ={NovaMateria:gradeCurricular}

    def AdicionarNovaMateria(self,materia,Grade):
        """Criar uma nova materia para que você possa adicionar para os alunos

        Args:
            materia (str): Nome da materia
            Grade (str): A qual grade curricular ela pertence
        """
        self.Materias[materia]=Grade