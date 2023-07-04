import itertools

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from transformations import Physics
phys = Physics()
import random
class Charts:


    def get_population(self,n,*arguments):


        self.P = arguments[0]
        self.F = arguments[1]
        self.energy = arguments[2]
        self.p_food = arguments[3]
        self.p_energy = arguments[4]
        self.t = arguments[5]
        self.n = n
        self.T_random = random.uniform(0, n/1000 ) // 1
        def data_gen():

            for cnt in range(n):
                t = cnt// 1
                self.food = phys.get_function('food', p = self.p_food*self.P, P=self.P, F = self.F)
                self.energy = phys.get_function('energy', P=self.P, p=self.p_energy * self.P, energy=self.energy)
                print('T_random =',self.T_random)
                print('t =', t)
                self.P = phys.get_function('population', food=self.F, energy=self.energy, P=self.P)
                if t == self.T_random:
                    pri = random.uniform(-1 * 0.4 * self.P, 0.5 * self.P)
                    self.P += pri
                    self.T_random = random.uniform(self.T_random + 1, self.T_random + 50) // 1
                print('F =', self.food)
                print('E =', self.energy)
                print('P =', self.P)

                yield t, self.P

        def init():

            ax.set_ylim(0, 100)
            ax.set_xlim(0, 1)
            del xdata[:]
            del ydata[:]
            line.set_data(xdata, ydata)
            return line,

        fig, ax = plt.subplots()
        line, = ax.plot([], [], lw=2)
        ax.grid()
        xdata, ydata = [], []

        def run(data):
            # update the data
            t, y = data
            xdata.append(t)
            ydata.append(y)
            xmin, xmax = ax.get_xlim()
            ymin, ymax = ax.get_ylim()
            if t >= xmax:
                ax.set_xlim(xmin, 2 * xmax)
                ax.figure.canvas.draw()
            line.set_data(xdata, ydata)
            if y >= ymax:
                ax.set_ylim(ymin, 2 * ymax)
                ax.figure.canvas.draw()
            line.set_data(xdata, ydata)

            return line,

        ani = animation.FuncAnimation(fig, run, data_gen, interval=100, init_func=init, save_count=100, blit=True, repeat=False)

        plt.show()

    def get_food(self, n,  *arguments):
        self.P = arguments[0]
        self.F = arguments[1]
        self.energy = arguments[2]
        self.p_food = arguments[3]
        self.p_energy = arguments[4]
        self.t = arguments[5]
        self.T_random = random.uniform(1, n / 1000) // 1
        def data_gen():
            for cnt in range(n):
                print('F =', self.F)
                t = cnt //1

                self.F = phys.get_function('food', p = self.p_food  * self.P, P=self.P, F=self.F)
                if t == self.T_random:
                    pri = random.uniform(-1 * 0.4 * self.F, 0.3 * self.F)
                    self.F += pri
                    self.T_random = random.uniform(self.T_random + 1, self.T_random + 50) // 1
                self.energy = phys.get_function('energy',energy = self.energy, P=self.P, p = self.p_energy * self.P)
                self.P = phys.get_function('population', food=self.F, energy=self.energy, P=self.P)

                yield t, self.F //10

        def init():

            ax.set_ylim(0, 10)
            ax.set_xlim(0, 1)
            del xdata[:]
            del ydata[:]
            line.set_data(xdata, ydata)
            return line,

        fig, ax = plt.subplots()
        line, = ax.plot([], [], lw=2)
        ax.grid()
        xdata, ydata = [], []

        def run(data):
            # update the data
            t, y = data
            xdata.append(t)
            ydata.append(y)
            xmin, xmax = ax.get_xlim()
            ymin, ymax = ax.get_ylim()
            if t >= xmax:
                ax.set_xlim(xmin, 2 * xmax)
                ax.figure.canvas.draw()
            line.set_data(xdata, ydata)
            if y >= ymax:
                ax.set_ylim(ymin, 2 * ymax)
                ax.figure.canvas.draw()
            line.set_data(xdata, ydata)

            return line,

        ani = animation.FuncAnimation(fig, run, data_gen, interval=100, init_func=init, save_count=100)
        plt.show()

    def get_energy(self,  *arguments):
        self.P = arguments[0]
        self.F = arguments[1]
        self.energy = arguments[2]
        self.p_food = arguments[3]
        self.p_energy = arguments[4]
        self.t = arguments[5]
        def data_gen():
            for cnt in itertools.count(0, 40):
                t = cnt / self.t
                self.F = phys.get_function('food', P=self.P, p=self.p_food * self.P, F=self.F)
                pri = random.uniform(0.4 * self.P, 0.4 * self.P)
                self.energy = phys.get_function('energy', p =self.p_energy * self.P, P=self.P, energy=self.energy)
                self.P = phys.get_function('population', F=self.F, energy=self.energy, P=self.P)
                # self.res = phys.get_function('resources', res=self.res, p=self.P // 50, E=self.energy)
                print('E =', self.energy)
                print('P =', self.P)
                yield t, self.energy

        def init():

            ax.set_ylim(0, 10)
            ax.set_xlim(0, 1)
            del xdata[:]
            del ydata[:]
            line.set_data(xdata, ydata)
            return line,

        fig, ax = plt.subplots()
        line, = ax.plot([], [], lw=2)
        ax.grid()
        xdata, ydata = [], []

        def run(data):
            # update the data
            t, y = data
            xdata.append(t)
            ydata.append(y)
            xmin, xmax = ax.get_xlim()
            ymin, ymax = ax.get_ylim()
            if t >= xmax:
                ax.set_xlim(xmin, 2 * xmax)
                ax.figure.canvas.draw()
            line.set_data(xdata, ydata)
            if y >= ymax:
                ax.set_ylim(ymin, 2 * ymax)
                ax.figure.canvas.draw()
            line.set_data(xdata, ydata)

            return line,

        ani = animation.FuncAnimation(fig, run, data_gen, interval=100, init_func=init, save_count=100)
        plt.show()

    def get_resources(self, *arguments):
        self.P = arguments[0]
        self.F = arguments[1]
        self.energy = arguments[2]
        self.res = arguments[3]
        self.p_food = arguments[4]
        self.p_energy = arguments[5]
        self.p_res = arguments[6]
        self.t = arguments[7]
        def data_gen():

            for cnt in itertools.count():
                t = cnt/self.t
                self.P = phys.get_function('population', F=self.F, energy=self.energy, P=self.P)

                # pri = random.uniform(0.4 * self.P, 0.4 * self.P)
                self.food = phys.get_function('food', P=self.P, p=self.p_food *self.P, F=self.F)
                self.energy = phys.get_function('energy',p=self.p_energy * self.P, P=self.P, energy=self.energy)
                self.res = phys.get_function('resources', res = self.res, p=self.p_res *self.P,P=self.P, E = self.energy )
                print('F =', self.food)
                print('E =', self.energy)
                print('P =',50*self.P)
                print('res =', self.res)
                yield t, self.res

        def init():

            ax.set_ylim(0, 100)
            ax.set_xlim(0, 1)
            del xdata[:]
            del ydata[:]
            line.set_data(xdata, ydata)
            return line,

        fig, ax = plt.subplots()
        line, = ax.plot([], [], lw=2)
        ax.grid()
        xdata, ydata = [], []

        def run(data):
            # update the data
            t, y = data
            xdata.append(t)
            ydata.append(y)
            xmin, xmax = ax.get_xlim()
            ymin, ymax = ax.get_ylim()
            if t >= xmax:
                ax.set_xlim(xmin, 2 * xmax)
                ax.figure.canvas.draw()
            line.set_data(xdata, ydata)
            if y >= ymax:
                ax.set_ylim(ymin, 2 * ymax)
                ax.figure.canvas.draw()
            line.set_data(xdata, ydata)

            return line,

        ani = animation.FuncAnimation(fig, run, data_gen, interval=100, init_func=init, save_count=100)
        plt.show()


class All_Charts:
    def get_all_charts(self, *ar):

        self.Charts = Charts()
        self.initial_population = ar[0]
        self.initial_food = ar[1]
        self.initial_energy = ar[2]
        self.initial_resources = ar[3]
        self.p_food = ar[4]
        self.p_energy = ar[5]
        self.p_res = ar[6]
        self.t = ar[7]


        plt.subplot(2,2,1)
        Charts.get_population(self.initial_population, self.initial_food, self.initial_energy, self.p_food, self.p_energy, self.t)
        plt.title("population")

        plt.subplot(2, 2, 2)
        Charts.get_food(100, 100, 100, 100, 0.2, 0.2, 0.2, 10)
        plt.title("food")
        #
        plt.subplot(2, 2, 3)
        Charts.get_energy(self.initial_population, self.initial_food, self.initial_energy, self.initial_resources, self.p_food, self.p_energy,self.p_res, self.t)
        plt.title("energy")

        plt.subplot(2, 2, 4)
        Charts.get_resources(self.initial_population, self.initial_food, self.initial_energy, self.initial_resources, self.p_food, self.p_energy,self.p_res, self.t)
        plt.title("resources")
        plt.show()
# ch = All_Charts()
# ch.get_all_charts(100, 100, 100, 100, 0.2, 0.2, 0.2, 10)

Charts = Charts()

Charts.get_food(1000, 100, 1, 1, 0.4, 0.4, 10)



