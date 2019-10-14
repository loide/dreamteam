#!/usr/bin/env python3

import os
from config import db
from models import Person
import params

# Delete database file if it exists currently
if params.cfg['local_database'] and os.path.exists("people.db"):
    print("Remove existent database people.db")
    os.remove("people.db")

# Create the database
try:
    print("Create the new database.")
    db.create_all()

    # iterate over the PEOPLE structure and populate the database
    if params.people_data:
        print("Populate the new database.")
        for person in params.people_data:
            p = Person(lname=person.get("lname"), fname=person.get("fname"))
            db.session.add(p)

    db.session.commit()
except Exception as e:
    print(e)
