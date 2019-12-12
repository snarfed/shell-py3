import os
DEBUG = os.environ.get('GAE_ENV') in (None, 'localdev')  # 'standard' in production
LOCAL = os.environ.get('GAE_ENV') == 'localdev'

if DEBUG:
  os.environ.setdefault('CLOUDSDK_CORE_PROJECT', 'shell-py3')
  os.environ.setdefault('DATASTORE_DATASET', 'shell-py3')
  os.environ.setdefault('GOOGLE_CLOUD_PROJECT', 'shell-py3')

import logging
logging.getLogger().setLevel(logging.DEBUG)
logging.getLogger('google.cloud').setLevel(logging.INFO)

if DEBUG:
  os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'fake_user_account.json'

from google.cloud import ndb
ndb_client = ndb.Client()

from google.cloud import error_reporting
error_reporting_client = error_reporting.Client()

from google.cloud import tasks_v2
tasks_client = tasks_v2.CloudTasksClient()

if DEBUG:
  # HACK! work around that these don't natively support dev_appserver.py.
  # https://github.com/googleapis/python-ndb/issues/238
  ndb_client.host = 'localhost:8089'
  ndb_client.secure = False

  error_reporting_client.host = 'localhost:9999'
  error_reporting_client.secure = False

  tasks_client.host = 'localhost:9999'
  tasks_client.secure = False
