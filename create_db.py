import psycopg2 as pscpg
from psycopg2 import OperationalError

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = pscpg.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

def postgre_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

connect_postgre = create_connection("postgres", "postgres", "jerry1", "127.0.0.1", "5432")
postgre_query(connect_postgre, "create database hr")
connect_postgre = create_connection("hr", "postgres", "jerry1", "127.0.0.1", "5432")
pos*tgre_query(connect_postgre,"create table positions (position_code varchar(3) primary key, position_name varchar(30))")
postgre_query(connect_postgre, "create table employer (emp_id serial primary key, fname varchar(15), lname varchar(25), mname varchar(20), position_code varchar(3), start_date varchar(10))")
postgre_query(connect_postgre, "alter table employer add constraint emp_pos foreign key (position_code) references positions(position_code)")