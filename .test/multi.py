import threading
from time import perf_counter
import numpy as np

def load_data(dir): 
    Data = np.genfromtxt(dir, dtype=int,
                        encoding=None, delimiter=",")
    print(Data)

if __name__ == "__main__":
    start_time = perf_counter()

    # Create lock (optional)
    thread_lock = threading.Lock()

    # Create thread
    t1 = threading.Thread(target=load_data('/Users/dimas/Documents/KP_UTS/a.txt'))
    t2 = threading.Thread(target=load_data('/Users/dimas/Documents/KP_UTS/a.txt'))

    # Start task execution
    t1.start()
    t2.start()

    # Wait for process to complete execution
    t1.join()
    t2.join()

    end_time = perf_counter()
    print(f'It took {end_time- start_time :0.6f} second(s) to complete.')