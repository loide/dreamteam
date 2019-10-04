#!/usr/bin/env python3

"""
Main module of the server file
"""

import connexion
from config import connex_app as app
from params import cfg


# Read the swagger.yml file to configure the endpoints
app.add_api("swagger.yml")


# create a URL route in our application for "/"
@app.route("/")
def home():
    return "Server up and running."


if __name__ == "__main__":
    app.debug = cfg['debug']
    app.run(host=cfg['host'], port=cfg['port'])
