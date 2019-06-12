import os
#import getpass
#from subprocess import check_output


os.system("python generatereport_unity_Old.py")          #Adjust date,add dimensions,metricss in this report as needed
os.system("C:\snowsql -f logdata_old_unity.sql")


