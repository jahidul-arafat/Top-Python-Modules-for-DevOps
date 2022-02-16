#!/usr/bin/env python3
from pytm import (
    TM,
    Boundary,
    Actor,
    Server,
    Datastore,
    DatastoreType,
    Classification,
    Data,
    Dataflow,
    ociFunction
)

# Step-0: Setting up the Threat Model
tm = TM("My Test Threat Model")         # Set your threat model name
tm.description = """
A Short Description of My Threat Model
---------------------------------------
This is a sample threat model of a very simple system - a web-based comment system.
The user enters comments and these are added to a database and displayed back to the user. 
The thought is that it is, though simple, a complete enough example to express meaningful threats.
"""
tm.isOrdered = True                     # This number the data flows; IF False, Dataflows will not be numbered
tm.mergeResponses = True                # Will generate a top-down data flow diagram, else different
tm.assumptions =[
    "Assumption-1: Webserver will be all secure",
    "Assumption-2: PII data will be encrypted at Rest and in-transit"
]

# Step-1: Define and design the System Components
# 1A. Design the CORE Components
'''
- 1x Web-Server in Ubuntu
- 2x-Datastore/Databases: {SQL Database, Real Identity Database} in Centos Server
- 1X OCI Serverless Function in OCI VCN
'''

# A1. 1x Web-Server in OCI/OCI Linux 8
web = Server("Web Server")
web.os = "Oracle Linux 8"
web.onOCI = True
web.controls.isHardened = True
web.controls.sanitizesInput = False
web.controls.encodesOutput = True
web.controls.authorizesSource = False
web.controls.implementsServerSideValidation = True
web.controls.authenticationScheme = "Yes"
web.controls.implementsCSRFToken = True

# A2. - 2x Databases/DataStores under Boundary/Block: Server/DB
# Database-1: SQL Database
db = Datastore("DB-1: OCI Autonomous Database (ADB)")
db.type = DatastoreType.SQL
db.onOCI = True
db.controls.isHardened = False
db.inScope = True
db.maxClassification = Classification.RESTRICTED

# Database-2: Real Identity Database/DataStore
secretDb = Datastore("DB-2: OCI-ADB/Real Identity Database")
secretDb.type = DatastoreType.SQL
secretDb.controls.isHardened = True
secretDb.inScope = True
secretDb.storesPII = True
secretDb.maxClassification = Classification.TOP_SECRET

# A3. Define the Serverless function in OCI
my_lambda = ociFunction("OCI-Function")
my_lambda.controls.hasAccessControl = True
my_lambda.controls.isEncrypted = True

# 1B. Design the EXTERNAL Components
# 1x Actors >> user

# B1. Define the Actor named <User>
user = Actor("User")

# Step-2: Define the Dataflows between Components
# 2.1: SQL Database >> Real Identity Database
db_to_secretDb = Dataflow(db, secretDb, "Database verify real user identity")
db_to_secretDb.protocol = "RDA-TCP"  # Remote Database Access
db_to_secretDb.dstPort = 40234
db_to_secretDb.data = Data("Token verifying user identity", classification=Classification.SECRET)
db_to_secretDb.note = "Verifying that the user is who they say they are."
db_to_secretDb.maxClassification = Classification.SECRET

# 2.2: User >> Webserver
user_to_web = Dataflow(user,web, "User enters comments (*)")
user_to_web.protocol = "HTTP"
user_to_web.dstPort = 80
user_to_web.data = Data("Comments in HTML or Markdown", classification=Classification.PUBLIC)  #comment's in text
user_to_web.note = "This is a simple web app\n that stores and retrieves user comments."

# 2.3 Webserver >> MySQL Database Server
# Purpose: to store the comments into database
web_to_db = Dataflow(web, db, "Webserver Store the comments into OCI-ADB Database")
web_to_db.protocol = "SQL"
web_to_db.dstPort = 1522
web_to_db.data = Data("Store the comments into OCI-ADB Database", classification=Classification.PUBLIC)
web_to_db.note = "Web Server inserts user comments\ninto it's SQL query and stores them in the DB"

# 2.4: MySQL Database >> WebServer
# Purpose: Webserver retrieves comments from MySQL DB and then display those to user to count the comments he has made
db_to_web = Dataflow(db,web, "Webserver Retrieve comments from OCI-ADB")
db_to_web.protocol = "SQL"
db_to_web.dstPort = 80
db_to_web.data = Data("Web server retrieves comments from DB", classification=Classification.PUBLIC)
db_to_web.responseTo = web_to_db

# 2.5 Webserver >> User
# Purpose: Show the retrieved comments to user
web_to_user = Dataflow(web,user, "Webserver Shows comments (*) to users")
web_to_user.protocol = "HTTP"
web_to_user.data = Data("Web server shows comments to the end user", classification=Classification.PUBLIC) #comments_to_show
web_to_user.responseTo = user_to_web

# 2.6 My lambda >>  MySQL Database
# Purpose: To periodically clears MySQL Database
my_lambda_to_db = Dataflow(my_lambda,db, "Serverless function periodically cleans DB")
my_lambda_to_db.protocol = "MySQL"
my_lambda_to_db.dstPort = 3306
my_lambda_to_db.data = Data("Serverless function clears DB", classification=Classification.PUBLIC) #clear_op

# Step-3: Define the data that is shared among different actors, processes, databases, servers and functions
# 3.1 Data: userIdToken
# top_secret data which is processed by MySQL Database and Real Identity Database and
# traversed through [ User >> Webserver>>MySQL DB >> SecretDB ]
userIdToken = Data(
    name="User ID token",
    description="Some unique token that represents the user real data in the secret database",
    classification=Classification.TOP_SECRET,
    traverses=[user_to_web,db_to_secretDb],
    processedBy=[db,secretDb]
)

# Step-4: Define the boundaries

oci = Boundary("Oracle Cloud Infrastructure")
oci_vcn = Boundary("VCN 10.0.0.0/16")
oci_vcn.inBoundary = oci
db.inBoundary = oci_vcn
secretDb.inBoundary = oci_vcn
my_lambda.inBoundary = oci_vcn

oci_vcn_subnet = Boundary("Subnet 10.0.1.0/24")
oci_vcn_subnet.inBoundary = oci_vcn
web.inBoundary = oci_vcn_subnet


if __name__ == "__main__":
    tm.process()











