#!/usr/bin/env python3
from pytm import TM, Boundary, Actor, Server, Datastore, DatastoreType, Classification, Lambda, Data, Dataflow

# Step-01
# setting up the threat model
tm = TM("My Test Threat Model")         # Set your threat model name
tm.description = """
A Short Description of My Threat Model
---------------------------------------
This is a sample threat model of a very simple system - a web-based comment system. 
The user enters comments and these are added to a database and displayed back to the user. 
The thought is that it is, though simple, a complete enough example to express meaningful threats.
"""
tm.isOrdered = True                     # This will help the TM to pictuarize each of the Boundary/Block in sequence as listed in the code
tm.mergeResponses = True                # Will generate a top-down data flow diagram, else different
tm.assumptions =[
    "Here we can document a list of assumptions about the system",
    "Assumption-1: Webserver will be all secure",
    "Assumption-2: PII data will be encrypted at Rest and in-transit"
]

# Step-02
# Define the boundaries/ dotted rectangle block - Red

# Boundary-1: Define a simple internet block/
# Rectangular dotted block in red color,
# when attached to a <Actor>, will represent that Actor is internet-enabled
internet = Boundary("Internet")

# Boundary-2: Define the Database Server Block/Boundary
server_db = Boundary("Server/DB")
server_db.levels = [200]

# Boundary-3: Define the Oracle Cloud Infrastructure VCN Block/Boundary
# This Cloud VCN is required, because our OCI serverless function will periodically runs
# to clean the Database
oci_vcn = Boundary("OCI VCN")

# Step-3: Define and design the
# A. 1x Actors >> user
# B. 1x Web-Server in Ubuntu
# C. 2x-Datastore/Databases: {SQL Database, Real Identity Database} in Centos Server
# D. 1X OCI Serverless Function in OCI VCN

# 3.A Define the Actor >> User and place it under the <internet boundary>
user = Actor("User")
user.inBoundary = internet
user.levels = [2]

# 3.B 1x Web-Server in ubuntu
# Check list
"""
- [x] Web server hardening:  https://resources.infosecinstitute.com/topic/web-server-security-web-server-hardening/ or follow CIS Security Benachmarking 
    - Disable the signatue, 
    - Configure Log server access, 
    - Disable the HTTP trace and Track requests to avoid XSS attack/ TraceEnable Off and Reload Apache
    - Create non-root users
    - Restrict IP access <if your web server is used for only limited purposes >
    - Disable SSLv2 and SSLv3 # many web servers still run SSL 2.0/3.0 and TLS 1.0/1.1 protocols by default, putting any data transferred over these encryption methods at risk. 
    - Disable directory listing
    - Eliminate unused modules
    - Install Mod_evasive and Mod_security
    - Constantly check for patches
- [x] Web form Input Sanitization
    - Input sanitization is a cybersecurity measure of checking, cleaning, and filtering data inputs from users, APIs, 
    - and web services of any unwanted characters and strings to prevent the injection of harmful codes into the system.
- [x] Apache web server character encoding: Make sure in my.cnf and php.ini that all the connections are encoded with utf8
- [x] Apache Web Server Authentication and Authorization modules/Sources- https://httpd.apache.org/docs/2.4/howto/auth.html # AllowOverride AuthConfig

"""
web = Server("Web Server")
web.os = "Ubuntu"
web.controls.isHardened = True
web.controls.sanitizesInput = False
web.controls.encodesOutput = True
web.controls.authorizesSource = False
web.controls.implementsServerSideValidation = True
web.controls.authenticationScheme = "Yes"
web.controls.implementsCSRFToken = True
web.sourceFiles = ["../../../pytm/pytm/json.py",
                   "../../../pytm/docs/advanced_template.md"]


# 3.C - 2x Databases/DataStores under Boundary/Block: Server/DB
# C1- SQL Database
'''
# Checklist
- [x] SQL Server Hardening / Best Practices: https://www.netwrix.com/sql_server_security_best_practices.html
    -  Harden the Centos Server where MySQL Server Operates
    - Install Only the Required SQL Database Components
    - Limit the Permissions of Service Accounts According to the Principle of Least Privilege
    - Turn Off the SQL Server Browser Service
    - Use Groups and Roles to Simplify Management of Effective Permissions
    - Follow the Principle of Least Privilege when Assigning SQL Server Roles
    - Use Strong Passwords for Database Administrators
    - Install SQL Server Updates Promptly
    - Use Appropriate Authentication Options 
    - Control Password Options for Logins
    - Be Diligent about Disabling and Deleting Logins
    - Use a Strong Database Backup Strategy
    - Monitor Activity on Your SQL Server 
    - Audit Access and Changes to SQL Server and Your Databases
    - Protect against SQL Injection Attacks
    - Use Encryption Wisely
- [x] InScope Database management services provide a complete suite of database administration and management services . W
'''
db = Datastore("MySQL Database")
db.type = DatastoreType.SQL
db.inBoundary = server_db
db.OS = "Centos"
db.sourceFiles = ["../../../pytm/pytm/pytm.py"]
db.controls.isHardened = False
db.inScope = True
db.maxClassification = Classification.RESTRICTED
db.levels = [2]

# C2- Real Identity Database/DataStore
secretDb = Datastore("Real Identity Database")
secretDb.type = DatastoreType.SQL
secretDb.inBoundary = server_db
secretDb.OS = "Centos"
secretDb.sourceFiles = ["../../../pytm/pytm/pytm.py"]
secretDb.controls.isHardened = True
secretDb.inScope = True
secretDb.storesPII = True
secretDb.maxClassification = Classification.TOP_SECRET

# 3.D Define the Serverless function in OCI
my_lambda = Lambda("OCI-Function")
my_lambda.inBoundary = oci_vcn
my_lambda.controls.hasAccessControl = True
my_lambda.controls.isEncrypted = True
my_lambda.levels = [1,2]

# Step-4: Define the Dataflows between different boundaries, modules and actors
# Step-4.1: Dataflow from SQL Database to Real Identity Database
token_user_identity = Data(
    "Token verifying user identity", classification=Classification.SECRET
)

db_to_secretDb = Dataflow(db, secretDb, "Database verify real user identity")
db_to_secretDb.protocol = "RDA-TCP"  # Remote Database Access
db_to_secretDb.dstPort = 40234
db_to_secretDb.data = token_user_identity
db_to_secretDb.note = "Verifying that the user is who they say they are."
db_to_secretDb.maxClassification = Classification.SECRET

# Step-4.2: Dataflow from user to webserver
comments_in_text = Data(
    "Comments in HTML or Markdown", classification=Classification.PUBLIC
)

user_to_web = Dataflow(user,web, "User enters comments (*)")
user_to_web.protocol = "HTTP"
user_to_web.dstPort = 80
user_to_web.data = comments_in_text
user_to_web.note = "This is a simple web app\n that stores and retrieves user comments."

# Step-4.3: Webserver to MySQL Database Server to store the comments into database
query_insert = Data("Store the comments into MySQL Database", classification=Classification.PUBLIC)
web_to_db = Dataflow(web, db, "Webserver Store the comments into MySQL Database")
web_to_db.protocol = "MySQL"
web_to_db.dstPort = 3306
web_to_db.data = query_insert
web_to_db.note = "Web Server inserts user comments\ninto it's SQL query and stores them in the DB"

# Step-4.4: MySQL Database to WebServer
# Webserver retrieves comments from MySQL DB and then display those to user to count the comments he has made
comment_retrieved = Data(
    "Web server retrieves comments from DB", classification=Classification.PUBLIC
)
db_to_web = Dataflow(db,web, "Webserver Retrieve comments from DB")
db_to_web.protocol = "MySQL"
db_to_web.dstPort = 80
db_to_web.data = comment_retrieved
db_to_web.responseTo = web_to_db

# Step-4.4 Webserver to User
# Show the retrieved comments to user
comment_to_show = Data(
    "Web server shows comments to the end user", classification=Classification.PUBLIC
)
web_to_user = Dataflow(web,user, "Webserver Shows comments (*) to users")
web_to_user.protocol = "HTTP"
web_to_user.data = comment_to_show
web_to_user.responseTo = user_to_web

# Step-4.5 Serverless function clears MySQL Database
clear_op = Data(
    "Serverless function clears DB", classification=Classification.PUBLIC
)
my_lambda_to_db = Dataflow(my_lambda,db, "Serverless function periodically cleans DB")
my_lambda_to_db.protocol = "MySQL"
my_lambda_to_db.dstPort = 3306
my_lambda_to_db.data = clear_op

userIdToken = Data(
    name="User ID token",
    description="Some unique token that represents the user real data in the secret database",
    classification=Classification.TOP_SECRET,
    traverses=[user_to_web,db_to_secretDb],
    processedBy=[db,secretDb]
)


if __name__ == "__main__":
    tm.process()











