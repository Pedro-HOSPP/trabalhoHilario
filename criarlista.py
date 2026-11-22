import pickle

def anterior(mat1, mat2, cursos, alunos):
	if cursos[alunos[mat1][1]] < cursos[alunos[mat2][1]]: #comparar nome do curso
		return True
	if cursos[alunos[mat1][1]] > cursos[alunos[mat2][1]]:
		return False

	if alunos[mat1][2] > alunos[mat2][2]: #comparar se uma letra Ã© maior que a outra (I > C)
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

	return mat1 < mat2 

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
				
		return ordenar(cursos, alunos, menores) + [pivot] + ordenar(cursos, alunos, maiores)

def gerar_relatorio(lista_matriculas, cursos, alunos, notas):
    with open("saida.txt", "w") as arquivo:
        curso_anterior = ''
        tipo_anterior = ''

        for mat in lista_matriculas:
            nome, curso, tipo, (ano, semestre), respondeu = alunos[mat]

            if curso != curso_anterior:
                if curso_anterior != '':
                    arquivo.write("\n")

                arquivo.write(f"Curso: {cursos[curso]}\n")
                curso_anterior = curso
                tipo_anterior = ''

            if tipo != tipo_anterior:
                if tipo == "I":
                    arquivo.write("Ingressantes:\n")
                else:
                    arquivo.write("Concluintes:\n")

                tipo_anterior = tipo

            if respondeu:
                situacao = "Ok"
            else:
                situacao = "Pendente"

            escrever = f"* {nome} - {mat} - {ano}/{semestre} - {situacao}"

            if tipo == "C":
                if mat in notas:
                    nota = notas[mat]
                else:
                    nota = 0.0

                escrever = escrever + f" - {nota:.2f}"

            arquivo.write(escrever + "\n")

def main():
    with open("entrada100.bin", "rb") as arquivo:
        cursos = pickle.load(arquivo)
        alunos = pickle.load(arquivo)
        notas = pickle.load(arquivo)

    lista_matriculas = []
    for i in alunos:
        lista_matriculas.append(i)
    
    lista_ordenada = ordenar(cursos, alunos, lista_matriculas)
    gerar_relatorio(lista_ordenada, cursos, alunos, notas)
if __name__ == '__main__':
    main()