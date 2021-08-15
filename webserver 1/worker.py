#!/usr/bin/env python
import os
from npkayak import create_app

app = create_app(os.getenv('FLASK_CONFIG') or {})
app.app_context().push()

print('\x1b[32m[\x1b[1m\x1b[92m{}\x1b[0m\x1b[32m]\x1b[0m'.format('Visit http://localhost:8080'))
