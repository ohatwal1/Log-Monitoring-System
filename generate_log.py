import time
import sys
from random import randint
import pandas as pd


def main():
    start_time = int(time.time())
    end_time = start_time + 60*60*24
    try:
        filename = sys.argv[1]
    except:
        sys.exit('Path does not exists')


    log_data = pd.DataFrame(columns=['timestamp', 'ip', 'cpu_id', 'usage'])
    for curr_time in range(start_time, end_time, 60):
        log_data = log_data.append(pd.DataFrame({'timestamp':str(curr_time), 'ip':'192.168.1.' + str(randint(0, 255)),
                                            'cpu_id': [randint(0, 1)], 'usage': [randint(0, 100)]}), ignore_index=True)
    log_data.to_csv(filename, index=False)
    return


if __name__ == "__main__":
    main()
