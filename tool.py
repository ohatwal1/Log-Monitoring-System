#
# @Author: Omkar Hatwalne
#

import sys
import time
import pandas as pd
from datetime import datetime
from os import path
from dateutil import tz


def main():
    exec_time = time.time()
    command = sys.argv[1]
    if path.exists(command):
        log_data = pd.read_csv(command)
    while True:

        query = (input('> '))
        new_query = query.split(" ")
        op = new_query[0]
        if op == 'EXIT':
            sys.exit()
        elif op == 'QUERY':
            ip = new_query[1]
            cpu_id = int(new_query[2])
            start_date = new_query[3]
            start_time = new_query[4]
            end_date = new_query[5]
            end_time = new_query[6]

            ## start here

            extracted_log_data = [row[1] for row in log_data.iterrows() if
                                  row[1]['ip'] == ip and row[1]['cpu_id'] == cpu_id]
            # print(extracted_log_data)
            local_start_dt = datetime(int(start_date[:4]), int(start_date[5:7]), int(start_date[8:]),
                                      int(start_time[:2]),
                                      int(start_time[3:]), tzinfo=tz.tzlocal())
            local_end_dt = datetime(int(end_date[:4]), int(end_date[5:7]), int(end_date[8:]), int(end_time[:2]),
                                    int(end_time[3:]), tzinfo=tz.tzlocal())

            local_start_dt = int(local_start_dt.timestamp())
            local_end_dt = int(local_end_dt.timestamp())
            if extracted_log_data:
                print(
                    'CPU' + str(extracted_log_data[0]['cpu_id']) + ' usage on ' + extracted_log_data[0]['ip'] + ':')
                output = ''
                for data in extracted_log_data:
                    data_dt = int(data['timestamp'])
                    local_dt = datetime.fromtimestamp(data_dt)
                    # data_utc = local_dt.timestamp()
                    if (int(data_dt) >= local_start_dt) and (data_dt <= local_end_dt):
                        if output:
                            output += ', '
                        output += '(' + str(local_dt.year) + '-' + (
                            '0' + str(local_dt.month) if local_dt.month < 10 else str(local_dt.month)) + '-' + str(
                            local_dt.day) + ' ' + (
                                      '0' + str(local_dt.hour) if local_dt.hour < 10 else str(local_dt.hour)) \
                                  + ':' + ('0' + str(local_dt.minute) if local_dt.minute < 10 else str(
                            local_dt.minute)) + ', ' + str(data['usage']) + '%' + ')'
                print(output)
                print('Execution time : %s' % (time.time()-exec_time))
            else:
                print('Data not found.')
                print('Execution time : %s' % (time.time()-exec_time))
        else:
            print("Operation not supported")
            print('Execution time : %s' % (time.time()-exec_time))

    else:
        print("Invalid Path")
        sys.exit()


if __name__ == '__main__':
    main()
