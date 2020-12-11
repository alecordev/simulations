import datetime

import numpy as np
import matplotlib.pyplot as plt


class Simulation:
    def __init__(self, iterations=20):
        self.iterations = iterations
        self.money = 1000
        self.interest = 0.06
        self.series = np.array([], dtype='float64')

    def run_iteration(self):
        self.money = (1 + self.interest) * self.money
        self.series = np.append(self.series, [self.money])

    def run_simulation(self):
        for _ in range(self.iterations):
            self.run_iteration()
            print(self.money)
        return self.money


def plot(series):
    plt.plot(range(len(series)), series)
    plt.savefig(
        f'chart-{datetime.datetime.now().strftime("%Y-%m-%d.%H%M%S")}.svg', format='svg'
    )


if __name__ == '__main__':
    sim = Simulation()
    sim.run_simulation()
    plot(sim.series)
