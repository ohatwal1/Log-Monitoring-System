# Log_Monitoring_System

A log monitoring system, which monitors 1000 servers. Each server has 2 CPUs. Each server generates a log for CPU usage every minute. 
Example: 
    timestamp  IP           cpu_id usage 
    1414689783 192.168.1.10     0   87 
    1414689783 192.168.1.10     1   90 
    1414689783 192.168.1.11     1   93 

(1) generate.py: Generate the logs for one day, say 2014-10-31, just use random numbers between 0% to 100% as CPU usage. 
    The generator writes data to files in a directory. The timestamp is Unix time. 

(2) tool.py: Uses a command line tool which takes a directory of data files as a parameter and lets you query CPU usage for a specific CPU in a given time period. 
   
It is an interactive command line tool which read a user’s commands from stdin. The tool support two commands. 

One command will print results to stdout. Its syntax is QUERY IP cpu_id time_start time_end. Time_start and time_end should be specified in the format YYYY-MM-DD HH:MM where YYYY is a four-digit year, MM is a two digit month (i.e., 01 to 12), DD is the day of the month (i.e., 01 to 31), HH is the hour of the day, and MM is the minute of an hour. 

The second command to support is EXIT. It will exit the tool.

Ex- To run the generator: 
python generate.py DATA_PATH 
To run the interactive query tool:
python tool.py DATA_PATH

Sample-

>QUERY 192.168.1.10 1 2014-10-31 00:00 2014-10-31 00:05 
CPU1 usage on 192.168.1.10: (2014-10-31 00:00, 90%), (2014-10-31 00:01, 89%), (2014-10-31 00:02, 87%), 
(2014-10-31 00:03, 94%) (2014-10-31 00:04, 88%) 

>QUERY 192.168.1.12 0 2014-10-31 00:00 2014-10-31 00:05 
CPU0 usage on 192.168.1.12: (2014-10-31 00:00, 90%), (2014-10-31 00:01, 89%), (2014-10-31 00:02, 87%), (2014-10-31 00:03, 94%), (2014-10-31 00:04, 88%) 

>EXIT

Requirements : 
• Python 3.6 – pandas

How to run : 

$ python generate_log.py <Filename.csv> 

$ python tool.py <Filename.csv>
