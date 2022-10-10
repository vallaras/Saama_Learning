from turtle import update
import psycopg2
import psycopg2.extras

from crud import delete

host= "localhost",
user = "postgres",
password = "vallarasu",
port = "5432",
database = "postgres"
conn = None

try:
    with psycopg2.connect(
                host= "localhost",
                user = "postgres",
                password = "vallarasu",
                port = "5432",
                database = "postgres") as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

            cur.execute('DROP TABLE  IF EXISTS employee')
            create_script = ''' CREATE TABLE IF NOT EXISTS employee (
                                    id    int PRIMARY KEY,
                                    name  varchar(20) NOT NULL,
                                    salary int,
                                    dept_id varchar(30))'''
            cur.execute(create_script)

            insert_script = "INSERT INTO employee (id, name, salary, dept_id) VALUES (%s, %s, %s, %s)"
            insert_value = [(1,'vallarasu',15000,'Devloment'),(2,'john',20000,'tech_lead'),(3,'xyz',10000,'data')]
            for record in insert_value: 
                cur.execute(insert_script,record)
            
            update_script = 'UPDATE employee SET salary = salary + (salary * 0.5)'
            cur.execute(update_script)  

            delete_script = 'DELETE FROM employee WHERE name = %s'
            delete_record = ('xyz',)

            cur.execute(delete_script,delete_record)  

            cur.execute('SELECT * FROM EMPLOYEE')
            for record in cur.fetchall():
                print(record['name'],record['salary'])    
except Exception as error:
    print(error)
finally:
    if conn is not None:    
        conn.close()
                                