### [shell-py3](https://shell-py3.appspot.com/)!

Interactive server-side Python shell for [Google App Engine](https://cloud.google.com/appengine/) [Python 3.7 Standard](https://cloud.google.com/appengine/docs/standard/python3/). Try it at [shell-py3.appspot.com](https://shell-py3.appspot.com/)!

`logging`, `os`, `sys`, `[requests](https://2.python-requests.org/en/master/)`, and `[google.cloud.ndb](https://googleapis.dev/python/python-ndb/latest/)` are imported automatically.

Interpreter state is stored in the datastore so that variables, function definitions, and other values in the global and local namespaces can be used across commands.

To use the shell in your app, copy `shell.py`, `static/*`, and `templates/*` into your app's source directory. Then, add the URL routes in `shell.py` to your app.

Largely based on the original [App Engine samples shell](https://code.google.com/archive/p/google-app-engine-samples/wikis/GoogleAppEngineSamples.wiki) for Python 2.7, which is Copyright 2007 Google Inc. and licensed under the Apache License, Version 2.0.
