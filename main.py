import Entities.population
from Functions import fitness

def main():

    # Variáveis:
    price = [22, 3, 8, 5, 5, 5, 32, 13, 8, 4, 6, 4, 2, 7, 2, 4, 7, 6, 8, 6]
    necessity = [10, 5, 6, 10, 8, 7, 9, 9, 5, 5, 6, 7, 7, 2, 9, 6, 1, 4, 3, 2]
    max_budget = 75

    genes = [0, 1] # O gene 0 = ausência; O gene 1 = presença
    chromosome_size = len(price)

    population_size = 100
    max_generation = 100
    mutation_rate = 0.01
    crossover_rate = 0.8

    print("\n---- ALGORITMO GENÉTICO ----\n")
    print("----------------------------")
    print(f"Orçamento Máximo: {max_budget}")
    print(f"Geração Máxima: {max_generation}")
    print(f"Taxa de Mutação: {mutation_rate}")
    print(f"Taxa de Crossover: {crossover_rate}")
    print("----------------------------")
    print("  ID  | Preço | Necessidade")
    print("----------------------------")
    for i, (p, n) in enumerate(zip(price, necessity), start=1):
        print(f"  {i:2}  |  {p:4}  |  {n:6}")
    print("----------------------------")

    # População Inicial
    initial_population = Entities.population.generate_population(population_size, chromosome_size, genes)
    average_fitness = fitness.avg_fitness(initial_population, price, necessity, max_budget)
    print(f"Geração: {1} | Fitness Médio: {average_fitness}")
    
    # Primeira Geração
    new_population = Entities.population.new_generation(initial_population, price, necessity, max_budget, chromosome_size, crossover_rate, mutation_rate)
    average_fitness = fitness.avg_fitness(new_population, price, necessity, max_budget)
    print(f"Geração: {2} | Fitness Médio: {average_fitness}")

    generation = 2
    best = 0
    while(generation != max_generation):
        generation += 1

        new_population = Entities.population.new_generation(new_population, price, necessity, max_budget, chromosome_size, crossover_rate, mutation_rate)
        average_fitness = fitness.avg_fitness(new_population, price, necessity, max_budget)
        print(f"Geração: {generation} | Fitness Médio: {average_fitness}")

        best_fit = fitness.best_fitness(new_population, price, necessity, max_budget)
        best = best_fit[0]

    picked_items = []
    total_price = 0
    total_necessity = 0
    best_chromosome = best_fit[1]

    for i in range(len(best_chromosome)):
        if(best_chromosome[i] == 1):
            picked_items.append(i+1)
            total_price += price[i]
            total_necessity += necessity[i]
    
    print(f"\n| Itens Escolhidos: {picked_items}")
    print(f"| Melhor Necessidade: {total_necessity}")
    print(f"| Preço: {total_price}\n")


if __name__ == "__main__":
    main()