import numpy as np
import matplotlib.pyplot as plt
import math



def returnsin(x):
    return math.sin(x)
def returncos(x):
    return math.cos(x)

def main():
    x = np.linspace(0, 1, 100)
    f2 = np.vectorize(returnsin)
    f3 = np.vectorize(returncos)
    # y1 = returnsin(x)
    # z1 = returncos(x)
    f, axarr = plt.subplots(1,2)
    axarr[0].plot(f2(x),x)
    axarr[1].plot(f3(x),x)
    axarr[0].set_title('sin(x)')
    axarr[1].set_title('cos(x)')
    plt.savefig("sinandcos.pdf", format="pdf")

if __name__ == '__main__':
    main()