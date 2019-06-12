import os
import getpass
from subprocess import check_output

os.system("python Allaccounts_Admoblogin.py")
os.system("python generate_report_admob_3d.py")          #Adjust date,add dimensions,metricss in this report as needed
os.system("C:\snowsql -f logdata_new_admob.sql")

os.system("python generatereport_unity_4d.py")
os.system("C:\snowsql -f logdata_new_unity.sql")

