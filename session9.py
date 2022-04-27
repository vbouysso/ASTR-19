import numpy as np
import matplotlib.pyplot as plt
import math


def main():
    x = np.random.sample(100)
    print("x :", x)
    plt.hist(x,bins=100,alpha=0.5,edgecolor="black")

    plt.ylabel("size of bin")
    plt.xlabel("x value")
    plt.show()
    plt.savefig("1000nums100bins.pdf", format="pdf")

if __name__ == '__main__':
    main()