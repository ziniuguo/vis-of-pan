from random import randint, choice
import matplotlib.pyplot as plt

S = int(input("Susceptible people"))
I = int(input("Infected people"))
beta = float(input("infection rate"))
gama = float(input("recover rate"))
infected_distance = float(input("infected_distance"))


class Simulation_sir:

    def __init__(self, S, I, beta, gama, infected_distance):
        """
        SIR model parameters:
        S:= the num of susceptible group
        I:= the num of infected group
        beta:= the infectious rate # must be decimals and the significant figures equals 1
        gama:= the recovered and removed rate # the same as beta
        infected_distance:= how far can be infected
        """
        self.s = S
        self.i = I
        self.r = 0
        self.beta = beta
        self.gama = gama
        self.s_list = []
        self.i_list = []
        self.r_list = []
        self.status = 's'
        self.id = infected_distance
        """
        Random walk parameters
        """

    def random_walk(self, a_list):
        """
        show how the people move
        """
        for i in range(len(a_list)):
            x_direction = choice([-1, 1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            a_list[i][0] += x_step
            a_list[i][1] += y_step

            if a_list[i][0] <= 0 or a_list[i][0] >= 400:
                a_list[i][0] -= x_step
            if a_list[i][1] <= 0 or a_list[i][1] >= 400:
                a_list[i][1] -= y_step

    def set_initial_position(self):
        """
        create the beginning situation
        """
        for s in range(self.s):
            s_x = randint(0, 400)
            s_y = randint(0, 400)
            self.s_list.append([s_x, s_y])
        for i in range(self.i):
            i_x = randint(0, 400)
            i_y = randint(0, 400)
            self.i_list.append([i_x, i_y])

    def get_distance(self, x, y, a, b):
        """
        calculate the distance between the infected and susceptible
        parameters:
        x, y := one's position
        a, b := one's position
        d is the answer
        """
        d_square = (x - a) ** 2 + (y - b) ** 2
        d = d_square ** (1 / 2)
        return d

    def check_neighbours(self):
        """
        the main logical part to show how people get infected and be recovered/removed
        parameters:
        empty_list:= to preserve the current location of the new infected people temporarily
        """
        empty_list = []
        empty_list2 = []
        for s in range(len(self.s_list)):
            for i in range(len(self.i_list)):
                b = randint(0, int(10 * (1 - self.beta)))
                if self.get_distance(self.s_list[s][0], self.s_list[s][1], self.i_list[i][0],
                                     self.i_list[i][1]) <= self.id and b == 1:
                    empty_list.append(self.s_list[s])
                    break
        for el in range(len(empty_list)):
            self.s_list.remove(empty_list[el])
            self.i_list.append(empty_list[el])

        for i in range(len(self.i_list)):
            g = randint(0, int(10 * (1 - self.gama)))
            if g == 1:
                empty_list2.append(self.i_list[i])
        for i in empty_list2:
            self.r_list.append(i)
            self.i_list.remove(i)


A = Simulation_sir(S, I, gama, beta, infected_distance)
A.set_initial_position()

fig, ax = plt.subplots(figsize=(10, 7))
plt.axis('off')
ax.set_xlim([-20, 420])
ax.set_ylim([-20, 420])
ax.set_autoscale_on(False)
ax.set_xticks(range(0, 1, 10))
ax.set_yticks(range(0, 1, 10))

x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
point1, = ax.plot(x1, y1, 'o', ms=8, color='green')
point2, = ax.plot(x2, y2, 's', ms=8, color='red')
point3, = ax.plot(x3, y3, 'x', ms=8, color='grey')


def display(ax):
    global point1, point2, point3
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    x3 = []
    y3 = []
    for i in range(len(A.s_list)):
        x1.append(A.s_list[i][0])
        y1.append(A.s_list[i][1])
    for i in range(len(A.i_list)):
        x2.append(A.i_list[i][0])
        y2.append(A.i_list[i][1])
    for i in range(len(A.r_list)):
        x3.append(A.r_list[i][0])
        y3.append(A.r_list[i][1])
    # 画图
    point1.set_xdata(x1)
    point1.set_ydata(y1)
    ax.draw_artist(point1)
    point2.set_xdata(x2)
    point2.set_ydata(y2)
    ax.draw_artist(point2)
    point3.set_xdata(x3)
    point3.set_ydata(y3)
    ax.draw_artist(point3)
    ax.figure.canvas.draw()


def gameLoop(ax):
    # 运动的过程
    A.random_walk(A.s_list)
    A.random_walk(A.i_list)
    A.random_walk(A.r_list)
    # 判断是否感染
    A.check_neighbours()
    display(ax)


def main2():
    plt.ion()
    A.set_initial_position()
    li = [len(A.i_list)]
    ls = [len(A.s_list)]
    lr = [len(A.r_list)]
    days = [1]
    day = 1
    while A.i_list:
        plt.clf()
        day += 1
        days.append(day)
        li.append(len(A.i_list))
        ls.append(len(A.s_list))
        lr.append(len(A.r_list))
        plt.plot(days, li, 'r-')
        plt.plot(days, ls, 'b-')
        plt.plot(days, lr, 'black')
        plt.pause(0.1)
    plt.ioff()
    plt.show()


if __name__ == '__main__':
    timer = fig.canvas.new_timer(interval=100)
    timer.add_callback(gameLoop, ax)
    timer.start()
    # main2()
    plt.show()
