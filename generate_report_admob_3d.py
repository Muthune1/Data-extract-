#!/usr/bin/python
#
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Retrieves a saved report or generates a new one.

To get ad clients, run get_all_ad_clients.py.

Tags: reports.generate
"""

__author__ = 'jalc@google.com (Jose Alcerreca)'

import argparse
import sys
import csv

from adsense_util import get_account_id
from adsense_util_data_collator import DataCollator
from apiclient import sample_tools
from oauth2client import client


# Declare command-line flags.
argparser = argparse.ArgumentParser(add_help=False)
argparser.add_argument(
    '--report_id',
    help='The ID of the saved report to generate')


def main(argv):
  # Authenticate and construct service.
  service, flags = sample_tools.init(
      argv, 'adsense', 'v1.4', __doc__, __file__, parents=[argparser],
      scope='https://www.googleapis.com/auth/adsense.readonly')

  # Process flags and read their values.
  saved_report_id = flags.report_id

  try:
    # Let the user pick account if more than one.
    account_id = get_account_id(service)

    # Retrieve report.
    if saved_report_id:
      result = service.accounts().reports().saved().generate(
          accountId=account_id, savedReportId=saved_report_id).execute()
    else:
      result = service.accounts().reports().generate(
          accountId=account_id, startDate='today-3d', endDate='today-1d',
          metric=['INDIVIDUAL_AD_IMPRESSIONS','INDIVIDUAL_AD_IMPRESSIONS_RPM',
                  'EARNINGS'],
          dimension=['DATE','APP_NAME','AD_UNIT_NAME','COUNTRY_CODE','APP_PLATFORM'],
          sort=['+DATE']).execute()

    result = DataCollator([result]).collate_data()
   
    # Display headers.
    for header in result['headers']:
      print ('%25s' % header['name'],)
    #print(result)
    with open('out_3d.csv','w') as f:   
    # Display results.
     for row in result['rows']:
      i=0
      for column in row:
        print ('%s' % column)
        f.write('%s' % column)
        i+=1
        if i<8:
           print (',')
           f.write(',')
        else:
           f.write('\n')   
     
     f.close() 
      
    # Display date range.
  #  print ('Report from %s to %s.' % (result['startDate'], result['endDate']))
    #print

  except client.AccessTokenRefreshError:
    print ('The credentials have been revoked or expired, please re-run the '
           'application to re-authorize')

if __name__ == '__main__':
  main(sys.argv)
