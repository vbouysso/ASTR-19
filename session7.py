import numpy as np
import matplotlib.pyplot as plt
import math



def returnexp(x):
    return (x*x)

def main():
    x = np.linspace(0, 1, 100)
    y1 = returnexp(x)
    plt.plot(x,y1)
    plt.xlabel("Time [milliseconds]")
    plt.ylabel("Awesomeness")
    plt.savefig("awesomegraph.pdf", format="pdf")

if __name__ == '__main__':
    main()