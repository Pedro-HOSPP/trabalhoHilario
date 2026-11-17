import pickle

def anterior(mat1, mat2, cursos, alunos):
	if cursos[alunos[mat1][1]] < cursos[alunos[mat2][1]]: #comparar nome do curso
		return True
	if cursos[alunos[mat1][1]] > cursos[alunos[mat2][1]]:
		return False

	if alunos[mat1][2] > alunos[mat2][2]: #comparar se uma letra é maior que a outra (I > C)
		return True
	if alunos[mat1][2] < alunos[mat2][2]:
		return False

	if alunos[mat1][3][0] > alunos[mat2][3][0]: #comparar o ano
		return True
	if alunos[mat1][3][0] < alunos[mat2][3][0]:
		return False

	if alunos[mat1][3][1] > alunos[mat2][3][1]: #comparar semestre
		return True
	if alunos[mat1][3][1] < alunos[mat2][3][1]:
		return False

	if alunos[mat1][0] < alunos[mat2][0]: #comparar nome
		return True
	if alunos[mat1][0] > alunos[mat2][0]:
		return False

	return mat1[10:] < mat2[10:] #True se os últimos três dígitos forem menores, False caso contrário
	

def ordenar(cursos, alunos, lista):
	if len(lista) <= 1:
		return lista
	else:
		pivot = lista[0]
		menores = []
		maiores = []
		
		for i in range(1, len(lista)):

            
			if anterior(lista[i] , pivot, cursos, alunos):
				menores.append(lista[i])
			else:
				maiores.append(lista[i])
				
		return ordenar(menores) + [pivot] + ordenar(maiores)

def main():
    with open("entrada.bin", "rb") as arquivo:
        cursos = pickle.load(arquivo)
        alunos = pickle.load(arquivo)
        notas = pickle.load(arquivo)

    lista_matriculas = []
    for i in alunos:
        lista_matriculas.append(i)


		