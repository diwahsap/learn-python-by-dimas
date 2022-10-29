from time import perf_counter
import numpy as np

def load_data(dir): 
    Data = np.genfromtxt(dir, dtype=int,
                        encoding=None, delimiter=",")
    print(Data)

if __name__ == "__main__":
    start_time = perf_counter()

    load_data('/Users/dimas/Documents/KP_UTS/a.txt')

    end_time = perf_counter()
    print(f'It took {end_time- start_time :0.6f} second(s) to complete.')
