import sys
import random
import datetime
import logging

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)


class Person:
    def __init__(self, age):
        self.gender = random.randint(0, 1)
        self.age = age


class PopulationSimulation:
    def __init__(self):
        self.iteration = 0
        self.starting_population = 1000
        self.disaster_chance = 10
        self.infant_mortality = 5
        self.agriculture = 5
        self.disaster_chance = 10
        self.food = 0
        self.fertility_lower = 18
        self.fertility_higher = 35
        self.able_people = 0
        self.population = []
        self.simulation = np.array([], dtype=int)

    def harvest(self):
        for person in self.population:
            if person.age > 8:
                self.able_people += 1

        self.food += self.able_people * self.agriculture
        if self.food < len(self.population):
            del self.population[0 : int(len(self.population) - self.food)]
            self.food = 0
        else:
            self.food -= len(self.population)

    def reproduce(self):
        for person in self.population:
            if person.gender == 1:
                if person.age > self.fertility_lower:
                    if person.age < self.fertility_higher:
                        if random.randint(0, 5) == 1:
                            if random.randint(0, 100) > self.infant_mortality:
                                self.population.append(Person(0))

    def run_year(self):
        logger.debug('Iteration %s' % self.iteration)
        self.harvest()
        self.reproduce()
        for person in self.population:
            if person.age > 80:
                self.population.remove(person)
            else:
                person.age += 1
        if random.randint(0, 100) < self.disaster_chance:
            del self.population[
                0 : int(random.uniform(0.05, 0.2) * len(self.population))
            ]
        logging.info(len(self.population))
        self.iteration += 1
        return len(self.population)

    def begin_simulation(self):
        # Populate initial population
        logger.info('Beginning...')
        for _ in range(self.starting_population):
            self.population.append(Person(random.randint(18, 50)))

    def run_simulation(self):
        logger.info('Running simulation.')
        self.begin_simulation()
        while 100000 > len(self.population) > 1:
            self.simulation = np.append(self.simulation, [self.run_year()])


if __name__ == '__main__':
    sim = PopulationSimulation()
    sim.run_simulation()
    plt.plot(sim.simulation)
    plt.savefig(
        f'chart-{datetime.datetime.now().strftime("%Y-%m-%d.%H%M%S")}.svg', format='svg'
    )
