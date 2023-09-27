import os #importa o modulo do sistema operacional
from Alunos import Aluno #importa do arquivo alunos a class alunos
from matricula import Matricula_secretaria #importa a classe matricula da secretaria
from Materias import materia #importa a classe materia

#Vetor que iremos guardar os nossos Alunos
Alunos = []
#Criamos um loop eterno para manter o programa rodando
while(True):
    #Pedimos o usuario o nome do aluno
    NomeAluno = input("Nome do Aluno se não quiser criar novo aluno digite n: ")
    #Pedimos para o usuario a sua matricula
    if(NomeAluno!="n"):
        Matricula = int(input("Digite sua matricula, caso não tenha coloque 0 : "))
        #Agora ela cria um novo aluno como objeto com as informações passadas
        NovoAluno = Aluno(NomeAluno,Matricula)
        #Insere no vetor Alunos 
        Alunos.append(NovoAluno)
    
    #Faz um laço de repetição para mostrar o nome dos alunos cadastrados
    for aluno_lista in Alunos:
        print("Nome do Aluno "+aluno_lista.Nome+"\n "+"Matricula aluno:" +str(aluno_lista.MatriculaAluno))

    #verifica outras Tarefas para o programa executar
    print("Qual tarefa deseja Executar agora?")
    tarefa = input("> ") #insira qual sera o proximo comando que o usuario ira executar
    
    if(tarefa == "matricula alt"): # se for EXATAMENTE igual matricula alt cai aqui para alterar matricula
       
        mat = Matricula_secretaria() #chamamos um objeto de matricula da secretaria
        Nome = input("Qual aluno  deseja alterar a matricula? > ") #Agora digitamos o aluno que queremos alterar
        
        for Aluno_mat in Alunos: #busca o aluno dentro do laço de repetição for
           
            if(Aluno_mat.Nome == Nome): #se o nome for EXATAMENTE o mesmo cai aqui
                mat.AlterarMatriculaAluno(Aluno_mat)  #chama o metodo de alterar a matricula
                print(Aluno_mat.Nome +" Foi alterada sua matricula para "+str(Aluno_mat.MatriculaAluno))
                os.system("cls") #verificamos o resultado e limpamos o terminal
                break
    
    if(tarefa == "nova aula"): #caso queira adicionar uma nova aula
        materia_nova = input("Qual a materia que será adicionada? > ") #nome da materia a ser adicionada
        grade = input("Ela é de qual grade? coloque 0 se for de backend > ") #a qual grade ela esta relacionada
        if(grade !="0"): #se a grade não for zero ela não é de back end
            materia_aluno = materia(materia_nova,grade) #criamos o objeto de materia
        else:
            materia_aluno = materia(materia_nova) #se for 0 é de back end

        _Aluno = input("Deseja atualizar as aulas de algum aluno? digite ?  para ver os alunos cadastrados ou  n para cancelar >")
        if(_Aluno == "?"): #Pergunta quais alunos existem
            for a in Alunos: #Mostra todos os alunos cadastrados
                print(a.Nome)
            _Aluno = input("Deseja atualizar as aulas de algum aluno?") #repete a pergunta
        if(_Aluno !="n"): #se não for igual a n atualiza a grade do aluno
            for al in Alunos:
                if(al.Nome == _Aluno): #se localizar o aluno
                    al.Aulas.append(materia_aluno.Materias) #adiciona a materia as suas aulas atraves do objeto de materias
                    print(f"Agora o aluno {al.Nome} .\n possui as materias de: {al.Aulas} ")
                    input(">..")
                    os.system("cls")

    if(tarefa == "lancar nota"):
        _Aluno = input("Deseja lançar nota? digite ?  para ver os alunos cadastrados ou  n para cancelar >")
        if(_Aluno == "?"): #Pergunta quais alunos existem
            for a in Alunos: #Mostra todos os alunos cadastrados
                print(a.Nome)
            _Aluno = input("Deseja alançar nota de qual aluno?") #repete a pergunta
        if(_Aluno !="n"): #se não for igual a n atualiza a grade do aluno
            for al in Alunos:
                if(al.Nome == _Aluno): #se localizar o aluno
                    _materia =input("Qual  aula para nota você quer lançar, coloque ? para ver as materias") #qual materia ira lancar a nota
                    if(_materia =="?"): #caso deseje ver as materias cadastradas
                        for aula_aluno_cad in NovoAluno.Aulas: #faz um laço para desocbrir  quais aulas o aluno esta cadastrado
                            print(str(aula_aluno_cad.keys()).replace("dict_keys(['","").replace("'])","")) #limpa o dado "isso é bem comum, se quiser saber o porque pode me perguntar :D"
                        _materia =input("Qual aula para nota você quer lançar?") #a materia nota que sera lançada
                    for aula_aluno_cad_up in NovoAluno.Aulas: #Itera o loop para verificar se a aula existe
                        if(_materia ==str(aula_aluno_cad_up.keys()).replace("dict_keys(['","").replace("'])","")): #verifica se a aula digitada existe
                            NovoAluno.LancarNota(input("Qual a nota que deseja lançar?")+" "+_materia) #se  existir pergunta a nota e lança no sistema
                            for notas in al.Notas:  #faz um loop para mostras as notas do aluno
                                print("Essas são as notas do Aluno : "+notas)
                    input(">..")
                    os.system("cls")     

    #limpa o terminal 
    else:   
        os.system("cls")

        
#para fazer o programa para use o comando Ctrl+C no terminal!