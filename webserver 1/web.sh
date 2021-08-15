#!/bin/bash
# Requires virtualenv to be activated

# START
echo '[+] Server up, visit http://localhost:8080'
uwsgi --ini npkayak.ini #2> /dev/null
