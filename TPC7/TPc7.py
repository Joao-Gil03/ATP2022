import csv
import matplotlib.pyplot as plt


def leralunos(filename):
    file= open(filename,encoding='UTF8')
    file.readline()
    csv_file=csv.reader(file,delimiter=',')
    lista=[]
    for alunos in csv_file:
        lista.append(tuple(alunos))
    return lista

alunos= leralunos('alunos.csv')


def dist_alunos (alunos):
    dici={}
    for   _,_,curso,*_ in alunos:
        if curso in dici:
            dici[curso] += 1
        else:
            dici[curso] = 1

    return dici
aluno0= dist_alunos(alunos)

def medalunos (alunos):
    lista = []
    for id,nome,curso,tpc1,tpc2,tpc3,tpc4 in alunos:
        x= int(tpc1)+int(tpc2)+int(tpc3)+int(tpc4)
        media=x/4
        lista.append((id,nome,curso,tpc1,tpc2,tpc3,tpc4,media))
    return lista

aluno1= medalunos(alunos)


def escalao_alunos(aluno1):
    lista=[]
    for id,nome,curso,tpc1,tpc2,tpc3,tpc4,media in aluno1:
        if media>0 and media<=4:
            lista.append((id,nome,curso,tpc1,tpc2,tpc3,tpc4,media,'E'))
        if media>4 and media<=8:
            lista.append((id,nome,curso,tpc1,tpc2,tpc3,tpc4,media,'D'))
        if media>8 and media<=12: 
            lista.append((id,nome,curso,tpc1,tpc2,tpc3,tpc4,media,'C'))
        if media>12 and media<=16:
            lista.append((id,nome,curso,tpc1,tpc2,tpc3,tpc4,media,'B'))
        if media>16 and media<=20:
            lista.append((id,nome,curso,tpc1,tpc2,tpc3,tpc4,media,'A'))
    
    return lista

aluno2=escalao_alunos(aluno1)

def distribuiçao_escala(aluno2):
    dici={}
    for _,_,_,_,_,_,_,_,escalao in aluno2:
        if escalao in dici:
            dici[escalao]+=1
        else:
            dici[escalao] =1
    return dici
aluno3=distribuiçao_escala(aluno2)

def dist_grafico(aluno3):
    
    y=aluno3.values()
    x=aluno3.keys()
    plt.plot(x,y)
    plt.xlabel('Escalão')
    plt.ylabel('Número de alunos')
    plt.show()

def dist_tabela(aluno0):
    n=0
    p = list(aluno0.keys())
    d = list(aluno0.values())
    print(f'|{"Curso:":20}|{"Número de alunos":20}|')
    while n<len(aluno0):
        print(f'|{str(p[n]):20}|{str(d[n]):20}|')
        n=n+1

#Menu
def menu ():
    print("""
    --------------------------------------------------------------------------------------------------------------
    (1) Calcula a distribuição dos alunos por curso
    (2) Calcula a média das notas de cada aluno e acrescenta essa nova coluna no dataset em memória
    (3) Calcula os escalões
    (4) Calcula a distribuição dos alunos por escalão
    (5) Gráfico de linha a distribuição dos alunos por escalão
    (0) Sair
    --------------------------------------------------------------------------------------------------------------
    """)

    variavel = True
    leralunos('alunos.csv')
    while variavel == True:
        opcao = int(input("O que desejas?"))
        if opcao == 1:
            print(dist_alunos (alunos))
        if opcao == 2:
            print(medalunos (alunos))
        if opcao == 3:
            print(escalao_alunos(aluno1))
        if opcao == 4:
            dist_grafico(aluno3)
        if opcao == 5:
            dist_tabela(aluno0)
       
        if opcao == 0:
            variavel = False
            print("Até à próxima!")

menu()
