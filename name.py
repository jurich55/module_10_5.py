import multiprocessing
import datetime


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while file.readline():
            all_data.append(file.readline())


filenames = [f'./file {number}.txt' for number in range(1, 5)]
if __name__ == '__main__':

    start = datetime.datetime.now()
    for file in filenames:
        read_info(file)
    end = datetime.datetime.now()
    print(f'{end - start} - линейный')
    # 0:00:02.919603

    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(f'{end - start} - многопроцессный')
    # 0:00:01.145156
