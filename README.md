# Data-extract-
Using python to extract revenue data from Admob and Unity

The Logdata_new file on running does the below
-Generates revenue report for past 4 days from Admob and Unity for the provided credentials
-Stores the report as a csv
-Logins into snowflake as per credentials in config file for snowflake 
-Executes commands on snowcli to upload all the csv data into a table
