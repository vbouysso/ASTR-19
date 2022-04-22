# # Import math Library
# import math
import numpy as np
import math

def tabulatesinx():
    valuearray = np.linspace(0, (2*math.pi), num=50)
    print("x                     sin(x)")
    for i in valuearray:
        formati = (format(i,".14f"))
        formatsini = (format(math.sin(i),".14f"))
        
        print(formati, "    ", formatsini)

    
def main():
    
    tabulatesinx();
    
if __name__=="__main__":
    main()