print(""""
======MENU======
1 - Cadastrar aluno
2 - Listar alunos
3 - Média da turma
4 - Melhor aluno
5 - Pior aluno
6 - Sair
Escolha:
""")
escola ={}

choose = int(input(""))

if choose == 1:
    sair = 1
    while sair ==2:
        newStudent = input("Nome do Aluno")
        newNota = int(input("Nota do Aluno"))

        escola.update({newStudent:newNota})

    
