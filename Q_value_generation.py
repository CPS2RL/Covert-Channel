import random
import math
import numpy as np
def main():
    #n_frame = random.randint(2, 6)
    n_frame=6
    #T_H = random.randint(20, 40)
    T_H=30
    #T_L=120
    #T_H = int(T_L/random.randint(1, 5))
    T_L = random.randint(50, 70)
    #T_L=T_H*random.randint(2,5)
    T_lcm = math.lcm(T_H, T_L)
    t_max = n_frame * T_lcm

    c_h = []
    for i in range(n_frame):
        k = random.randint(1, 5)
        c_h.append(k)

    t = 0
    c_inf = []
    while t < t_max + 1:
        c_index = int((t / T_H) % n_frame)
        c_inf.append(c_h[c_index])
        t = t + T_lcm

    unq_ch = list(set(c_h))
    unq_inf = list(set(c_inf))

    #print(unq_inf)
    #print(len(unq_inf) / len(unq_ch))
    return len(unq_inf) / len(unq_ch)



import matplotlib.pyplot as plt



if __name__ == "__main__":
    Q=[]
    for _ in range(100):
        qq=main()
        Q.append(qq)
    #print(Q)

    #x = np.sort(Q)
    #print(sorted(Q))
    print(Q)
    # y-data for the ECDF
    y = np.arange(1, 100 + 1) / 100

    plt.plot(y,sorted(Q),color='black')

    # Add labels and title
    plt.xlabel('Task Percentage (%)')
    plt.ylabel('Relative Channel Capacity, Q')
    plt.title('Q values for randomly generated 100 task')
    # Save the plot as a PDF file
    plt.savefig('ecdf_plot.pdf')

    # Display the plot
    plt.show()
