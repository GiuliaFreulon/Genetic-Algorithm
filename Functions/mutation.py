import random

# Faz a mutação nos genes do cromossomo de acordo com a taxa de mutação
def mutation(chromosome, mutation_rate):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            if chromosome[i] == 0:
                chromosome[i] = 1
            else:
                chromosome[i] = 0
    
    return chromosome
        
