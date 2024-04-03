# from numpy import mean

import time
from collections import defaultdict

from logger import logger


class Solution(object):
    @staticmethod
    def solve():
        meteo_dict = defaultdict(list)
        fn = r'measurements.txt'
        with open(fn, 'r', encoding='utf-8') as file:
            for val in file:
                try:
                    meteo_name, _, val_s = val.partition(';')
                    val_f = float(val_s.strip())
                    meteo_dict[meteo_name].append(val_f)
                except:
                    pass

        meteo_dict = {k: meteo_dict[k] for k in sorted(meteo_dict)}
        for meteo_name, meteo_list in meteo_dict.items():
            # TODO: нужно ли округлять значения?
            # print(f'{meteo_name}: {mean(meteo_list)}, {min(meteo_list)}, {max(meteo_list)}')
            # print(f'{meteo_name}: {mean(numpy.array(meteo_list))}, {min(meteo_list)}, {max(meteo_list)}')
            print(f'{meteo_name}: {sum(meteo_list) / len(meteo_list)}, {min(meteo_list)}, {max(meteo_list)}')


def main():
    logger.info("Starting the solution")
    start = time.time()
    Solution.solve()
    logger.info(f"Solution finished, {time.time() - start:} seconds elapsed")


if __name__ == "__main__":
    main()
