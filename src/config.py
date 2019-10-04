import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import  params

basedir = os.path.abspath(os.path.dirname(__file__))

LOCAL_DATABASE = True

# Create the connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get the underlying Flask app instance
app = connex_app.app

if LOCAL_DATABASE:
    # Build the local Sqlite ULR for SqlAlchemy
    db_url = "sqlite:////" + os.path.join(basedir, "people.db")
else:
    # Build the RDS Postgres Database
    aws_rds_user = params.db['rds_user']
    aws_rds_passwd = params.db['rds_passwd']
    aws_rds_endpoint = params.db['rds_endpoint']
    aws_rds_port = params.db['rds_port']
    aws_rds_dbname = params.db['rds_dbname']
    db_url = "postgres://" \
            + aws_rds_user + ":" \
            + aws_rds_passwd + "@" \
            + aws_rds_endpoint + ":" \
            + aws_rds_port + "/" \
            + aws_rds_dbname
    print(db_url)

# Configure the SqlAlchemy part of the app instance
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create the SqlAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)
