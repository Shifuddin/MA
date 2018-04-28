# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 16:20:40 2018

@author: shifuddin
"""
from Population import Population
from random import choice


def get_matches(current_population, target_value, mutation_factor, highest_gen):
    
    current_generation = 1
    
    dict1 = {}
    while current_generation < highest_gen:
    
        mating_pool, population_fitness, fit_dna = population.calculate_fitness_mating_pool(target_value, current_population)

        if len(mating_pool) == 0:
            print ("Can not create first generation. No match.")
            break    
        print (current_generation)
        print (current_population)
        print (population_fitness)
        for l in range(0, len(fit_dna)):
            for m in range(0, len(fit_dna[l])):
                if fit_dna[l][m] == 1:
                    
                    if current_population[l][m] not in dict1:
                        index_in_popu = popu.index(current_population[l][m])
                        dict1[current_population[l][m]] = [popu_exec_time[index_in_popu], pop_data_tr[index_in_popu]]
        new_population = []
        for _ in range(len(current_population)):
            best_chr_1 = current_population[ choice(mating_pool)]
            best_chr_2 = current_population[ choice(mating_pool)]
            
            old_child = population.perform_crossover(best_chr_1, best_chr_2) 
            mutated_child = population.perform_mutation(old_child, mutation_factor)
            new_population.append(mutated_child)
            
        current_population = new_population
        current_generation +=1
        mutation_factor -= 0.00005
    return dict1
    
pop_size = 20
population = Population(pop_size)
popu, popu_exec_time, pop_data_tr = population.init_population()

chromosome_per_gen = 4
dna_per_chromose = 3
number_generation = 15
mutation_fact = 0.003
expected_exec_task = 5
init_popu = population.create_init_population(chromosome_per_gen, dna_per_chromose)
node_dict = get_matches(init_popu, expected_exec_task, mutation_fact, number_generation)
for key in node_dict.items():
    print (key)
