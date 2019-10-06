cfg = {
    "local_database": True,
    "host": "0.0.0.0",
    "port": 443,
    "debug": True,
    "ssl_context": "adhoc"
}

db = {
    "rds_user" : "AWS_RDS_USER",
    "rds_passwd" : "AWS_RDS_PASSWD",
    "rds_endpoint" : "AWS_RDS_ENDPOING",
    "rds_port" : "5432",
    "rds_dbname" : "AWS_RDS_DBNAME"
}

# Data to initialize database with
people_data = [
    {"fname": "Doug", "lname": "Farrell"},
    {"fname": "Kent", "lname": "Brockman"},
    {"fname": "Bunny", "lname": "Easter"},
]
