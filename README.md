## Run db in docker

Use CMD:<br/>
... cd to the project folder ...<br/>
cd database

docker build -t db-postgre .<br/>
docker images<br/>
docker run -d -p 5432:5432 db-postgre

## Create db, tables, insert data
- Run app.py from app folder<br/>
app.py - connect to postgresql, creating database if not exists, creating tables and inserting data

## CRUD scripts
create.py<br/>
delete.py<br/>
read.py<br/>
update.py