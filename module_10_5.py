import multiprocessing as mp
import time
from contextlib import contextmanager

@contextmanager
def timer(label):
    start = time.time()
    try:
        yield
    finally:
        duration = time.time() - start
        print(f'Время выполнения ({label}): {duration:.2f} сек')

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as f:
        line = f.readline()
        while line:
            all_data.append(line)
            line = f.readline()

if __name__ == "__main__":
    filenames = [f'./file {i}.txt' for i in range(1, 5)]

    with timer('линейное выполнение'):
        for filename in filenames:
            read_info(filename)

    with timer('многопроцессное выполнение'):
        with mp.Pool(processes=mp.cpu_count()) as pool:
            pool.map(read_info, filenames)