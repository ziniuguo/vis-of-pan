from random import randint, choice
import time
import matplotlib.pyplot as plt
import streamlit as st
import matplotlib
import random

st.beta_set_page_config(page_title="SIR SIMULATION", page_icon=None, layout='wide', initial_sidebar_state='expanded')

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

set_background_image = """
            <style>
            body {
            background-image: url("https://raw.githubusercontent.com/ziniuguo/UROPProject/master/bg.jpg");
            background-repeat: repeat;
            background-size: cover;
            }
            </style>
            """
st.markdown(set_background_image, unsafe_allow_html=True)

st.title("Visualisation of Epidemic")
st.subheader("Professor: Tan Da Yang \n Student: Guo Ziniu, Liang Junyi, Liu Nanhan")
st.header("Introduction")
st.write("The COVID‑19 pandemic, also known as the coronavirus pandemic, is an ongoing global pandemic of coronavirus "
         "disease 2019 (COVID‑19), caused by severe acute respiratory syndrome coronavirus 2 (SARS‑CoV‑2).")
st.write("The pandemic has caused global social and economic disruption, including the largest global recession since "
         "the Great Depression. Up to 100 million people have fallen into extreme poverty and global famines are "
         "affecting 265 million people. It has led to the postponement or cancellation of sporting, religious, "
         "political, and cultural events, widespread supply shortages exacerbated by panic buying, and decreased "
         "emissions of pollutants and greenhouse gases. Schools, universities, and colleges have been closed either "
         "on a nationwide or local basis in 161 countries, affecting approximately 98.6 percent of the world's "
         "student population.")
st.write("The SIR model is one of the simplest compartmental models, and many models are derivatives of this basic "
         "form. The model consists of three compartments:")
st.info("S: The number of susceptible individuals. When a susceptible and an infectious individual come into "
        "infectious contact, the susceptible individual contracts the disease and transitions to the infectious "
        "compartment.")
st.info("I: The number of infectious individuals. These are individuals who have been infected and are capable of "
        "infecting susceptible individuals.")
st.info("R: The number of removed (and immune) or deceased individuals. These are individuals who have been infected "
        "and have either recovered from the disease and entered the removed compartment, or died. It is assumed that "
        "the number of deaths is negligible with respect to the total population. This compartment may also be "
        "called recovered or resistant.")
st.write("Here, we use animation to simulate the spread of infectious diseases in the population, and draw a picture "
         "based on the data simulated by the animation.")
st.header("Dynamic Animation")

SSlider = st.sidebar.slider('susceptible', 0, 500, 250, step=1)
ISlider = st.sidebar.slider('infected', 0, 20, 10, step=1)
betaSlider = st.sidebar.slider('beta (infection rate)', 0.0, 1.0, 0.2, step=0.1)
gamaSlider = st.sidebar.slider('gamma (recover and death rate)', 0.0, 1.0, 0.2, step=0.1)
infected_distanceSlider = st.sidebar.slider('infected_distance', 0.0, 100.0, 50.0, step=1.0)

plhd = st.empty()

if st.sidebar.button("OK"):
    S = SSlider
    I = ISlider
    beta = betaSlider
    gama = gamaSlider
    infected_distance = infected_distanceSlider
    plhd.warning('Running...')
else:
    plhd.info('Please click the button "OK" to start the simulation.')
    S = 0
    I = 0
    beta = 0.0
    gama = 0.0
    infected_distance = 0.0
    days = 0


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
        self.id = infected_distance
        """
        Random walk parameters
        """

    def random_walk(self, a_list):
        """
        show how the people move
        """
        for i in range(len(a_list)):
            x_direction = choice([-1, 1, -2, 2, 0])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([-1, 1, -2, 2, 0])
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
                if self.get_distance(self.s_list[s][0], self.s_list[s][1], self.i_list[i][0],
                                     self.i_list[i][1]) <= self.id and random.random() < beta:
                    empty_list.append(self.s_list[s])
                    break
        for el in range(len(empty_list)):
            self.s_list.remove(empty_list[el])
            self.i_list.append(empty_list[el])

        for i in range(len(self.i_list)):
            if random.random() < gama:
                empty_list2.append(self.i_list[i])
        for i in empty_list2:
            self.r_list.append(i)
            self.i_list.remove(i)


A = Simulation_sir(S, I, beta, gama, infected_distance)


def gameLoop():
    # Process
    A.random_walk(A.s_list)
    A.random_walk(A.i_list)
    A.random_walk(A.r_list)
    A.check_neighbours()


def main2(d1, d2, d3):
    A.set_initial_position()
    li = [len(A.i_list)]
    ls = [len(A.s_list)]
    lr = [len(A.r_list)]
    days = [1]
    day = 1
    plhd2 = st.empty()
    while A.i_list:
        gameLoop()

        # Line chart
        f2 = plt.subplot2grid((4, 4), (0, 3))
        day += 1
        days.append(day)
        li.append(len(A.i_list))
        ls.append(len(A.s_list))
        lr.append(len(A.r_list))
        f2.plot(days, li, 'r-', lw=0.5)
        f2.plot(days, ls, 'b-', lw=0.5)
        f2.plot(days, lr, 'green', lw=0.5)
        plt.xlabel('Days', size=5)
        plt.ylabel('Number', size=5)
        matplotlib.rc('xtick', labelsize=3)
        matplotlib.rc('ytick', labelsize=3)
        ax = plt.gca()
        ax.spines["top"].set_linewidth(0.5)
        ax.spines["bottom"].set_linewidth(0.5)
        ax.spines["right"].set_linewidth(0.5)
        ax.spines["left"].set_linewidth(0.5)

        # Scatter
        f1 = plt.subplot2grid((4, 10), (0, 0), colspan=7, rowspan=3)
        f1.scatter([i[0] for i in d1], [i[1] for i in d1], c='r', marker='s', s=10, label='infected')
        f1.scatter([i[0] for i in d2], [i[1] for i in d2], c='g', marker='>', s=10, label='removed')
        f1.scatter([i[0] for i in d3], [i[1] for i in d3], c='b', marker='+', s=10, label='susceptible')
        f1.legend(bbox_to_anchor=(1.3, 0.5), loc='upper right', borderaxespad=0, prop={"size": 6}, framealpha=0.0)
        f1.axis('off')
        plt.xlim(0, 405)
        plt.ylim(0, 405)
        plhd2.pyplot()
        time.sleep(0.1)
        if A.gama == 0:
            if len(A.s_list) == 0 and A.beta != 0:
                plhd.error('All the people are infected and can never be recovered! Because γ equals 0.')
                break
            elif A.beta == 0:
                plhd.error('The number of susceptible and infected people will not change! Because both β and γ are 0.')
                break
    if len(A.i_list) == 0 and len(A.s_list) != 0:
        plhd.success('The infected people are all recovered or dead.')
    elif len(A.i_list) == 0 and len(A.s_list) == 0 and len(A.r_list) != 0:
        plhd.success('The infected people are all recovered or dead.')


main2(A.i_list, A.r_list, A.s_list)
