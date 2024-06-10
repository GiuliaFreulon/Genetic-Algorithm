import random

# A taxa de crossover determina se vai ocorrer crossover ou se os filhos vão ser clones dos pais
# O crossover realizado é o de um-ponto, no qual um ponto aleatório do cromossomo é escolhido para dividi-lo
# Depois da divisão, junta-se a primeira parte do cromossomo1 com a segunda parte do cromossomo2 e vice-versa para formar os filhos
def crossover(parents, size, crossover_rate):
	parent1 = parents[0]
	parent2 = parents[1]
	
	if random.random() < crossover_rate:
		crossover_point = random.randint(0, size-1)
		child1 = parent1[0:crossover_point] + parent2[crossover_point:]
		child2 = parent2[0:crossover_point] + parent1[crossover_point:]
	else:
		child1 = parent1
		child2 = parent2
		
	return child1, child2