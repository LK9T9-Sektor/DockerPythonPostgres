## Setup, run
- Requred installed applications:</br>
Docker(https://www.docker.com/)</br>
Python(https://www.python.org/)

- Requred installed Python libraries:<br/>
docker<br/>
psycopg2<br/>
sqlalchemy<br/>
sqlalchemy_utils

- Run:</br>
Start the docker app if it is not running on the OS<br/>
Run the script:<br/>
src<br/>
└── start.py

## Manual run db in docker

Use CMD:<br/>
... cd to the project folder ...<br/>
cd src\database

docker build -t db-postgre .<br/>
docker images<br/>
docker run -d -p 5432:5432 db-postgre

## CRUD scripts
app<br/>
└── ...<br/>
create.py - insert records into a table<br/>
delete.py - removing records from a table<br/>
init_db.py - connect to postgresql, creating database if it doesn't exist, creating tables, and inserting data<br/>
read.py - reading records from a table<br/>
update.py - updating the selected record in the table
