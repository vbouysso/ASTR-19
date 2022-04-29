import numpy as np
import matplotlib.pyplot as plt


def main():
    print("hello")
    x = np.random.randint(50, size=1000)
    plt.hist(x,bins=100,alpha=0.5,edgecolor="black")
    plt.ylabel("number of random #s in 10 group")
    plt.xlabel("random #s range from 0-50, groups/bins of size 10")
    plt.title("1000 random #s")
    plt.show()


if __name__ == "__main__":
    main()