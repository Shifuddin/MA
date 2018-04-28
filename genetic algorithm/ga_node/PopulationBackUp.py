# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 22:29:37 2018

@author: shifuddin
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 16:32:39 2018

@author: shifuddin
"""
from random import choice, uniform, shuffle, randint
import math

class Population ():
    def __init__ (self, popu_size, task_pre_matrix):
        self.popu_size = popu_size
        
        '''
        Initialize A & B
        '''
        self.A = 1 
        self.B = 1
        if task_pre_matrix[0,0] == 1 or task_pre_matrix [0,1] == 1:
            self.A = 1.5
        
        if task_pre_matrix[0, 1] == 1 or task_pre_matrix [1, 1] == 1:
            self.B = 1.5
        
        
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
    
        for _ in range(init_popu_size):
            chromosome = []
            number_list = list(range(0,len(self.popu)))        
            for _ in range(chromosome_size):
                shuffle(number_list)
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
        for dna in chromosome:
            dna_index = self.popu.index(dna)
            dna_exec_time = self.popu_exec_time[dna_index]
            dna_dt = self.popu_data_tr[dna_index]
            dna_ct = self.A * dna_exec_time + self.B * dna_dt
            if dna_ct <= target_value:
                score += 1
        return score
    
    def calculate_popu_fitness(self, init_population, target_value):
        population_fitness = []
        for chromose in init_population:
            chromosome_fitness = self.calculate_chromose_fitness(chromose, target_value)
            population_fitness.append(chromosome_fitness)
        return population_fitness
    def calculate_fitness_mating_pool(self,target_value, init_population):
        popu_fitness = self.calculate_popu_fitness(init_population, target_value)
        
        mating_pool = []    
    
        for i in range(len(popu_fitness)):
            chr_occurance = self.calculate_pool_occurance(popu_fitness[i], sum(popu_fitness))
        
            for _ in range (1, chr_occurance+1):
                mating_pool.append(i)
            
            
        return mating_pool, popu_fitness
    
    
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