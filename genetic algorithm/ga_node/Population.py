# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 16:32:39 2018

@author: shifuddin
"""
from random import choice, uniform, shuffle, randint
import math

class Population ():
    def __init__ (self, popu_size):
        self.popu_size = popu_size
        
    def init_population(self):
        
        self.popu = []
        self.popu_exec_time = []
        self.popu_data_tr = []
        
        for i in range(1, (self.popu_size+1)):
            self.popu.append('N'+str(i))
            self.popu_exec_time.append(uniform(0,10))
            self.popu_data_tr.append(uniform(0,10))
        
        return self.popu, self.popu_exec_time, self.popu_data_tr
    
    def create_init_population(self, init_popu_size, chromosome_size):
        initial_population = []
        number_list = list(range(0,len(self.popu))) 
        for _ in range(init_popu_size):
            chromosome = []
            shuffle(number_list)
            for _ in range(chromosome_size):
                dna = number_list.pop(len(number_list)-1)
                chromosome.append(self.popu[dna])
        
            initial_population.append(chromosome)

        return initial_population
    
    def calculate_pool_occurance(self,chromose_fitness, total_popu_fitness):
        occurance = 0
        if total_popu_fitness > 0:
            ratio = chromose_fitness / total_popu_fitness
            occurance = math.ceil((ratio*100))
        return occurance
    def calculate_chromose_fitness(self,chromosome, target_value):
        score = 0
        dna_level_fitness = []
        for dna in chromosome:
            dna_index = self.popu.index(dna)
            dna_exec_time = self.popu_exec_time[dna_index]
            dna_dt = self.popu_data_tr[dna_index]
            dna_ct = dna_exec_time + dna_dt
            if dna_ct <= target_value:
                score += 1
                dna_level_fitness.append(1)
            else:
                dna_level_fitness.append(0)
        return score, dna_level_fitness
    
    def calculate_popu_fitness(self, init_population, target_value):
        population_fitness = []
        dna_level_fitness_list = []
        for chromose in init_population:
            chromosome_fitness, dna_level_fitness = self.calculate_chromose_fitness(chromose, target_value)
            population_fitness.append(chromosome_fitness)
            dna_level_fitness_list.append(dna_level_fitness)
        return population_fitness, dna_level_fitness_list
    def calculate_fitness_mating_pool(self,target_value, init_population):
        popu_fitness, popu_fitness_dna = self.calculate_popu_fitness(init_population, target_value)
        
        mating_pool = []    
    
        for i in range(len(popu_fitness)):
            chr_occurance = self.calculate_pool_occurance(popu_fitness[i], sum(popu_fitness))
        
            for _ in range (1, chr_occurance+1):
                mating_pool.append(i)
            
            
        return mating_pool, popu_fitness, popu_fitness_dna
    
    
    def perform_crossover(self,chromosome_1, chromose_2):
        mid_point = randint(1, len(chromosome_1))
        child = chromosome_1[0:mid_point] + chromose_2[mid_point:] 
    
        return child


    def change_dna(self, child):
        while True:
            random_dna = choice(self.popu)
            if random_dna not in child:
                break
        return random_dna
    
    
    def perform_mutation (self,child, mutation_factor):
    
        for i in range(len(child)):
            RU = uniform(0,1)
            
            if (RU < mutation_factor):
                new_dna = self.change_dna(child)
                child [i] = new_dna
                
        return child