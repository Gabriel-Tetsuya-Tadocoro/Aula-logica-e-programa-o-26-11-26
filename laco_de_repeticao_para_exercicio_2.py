nota=0
soma=0
aluno=""
media=0

aluno = str(input("Digite o nome do aluno:"))
print ("Calculo de notas")
for x in range (0,3):
    nota = int(input(f"Digite a {x+1} º nota:"))
    soma =soma+nota
media=soma/3
print (aluno, "sua media é", media)
if media>=6:
    print("Status :Aluno Aprovado")
else:
    print("Status: Aluno reprovado")