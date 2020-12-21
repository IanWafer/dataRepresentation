import mysql.connector
import dbconfig as cfg

db = mysql.connector.connect(
    host=cfg.mysql['host'],
    user=cfg.mysql['username'],
    password=cfg.mysql['password'],
    database=cfg.mysql['database']
)

cursor = db.cursor()
sql="CREATE TABLE santaPresents (id INT PRIMARY KEY, name VARCHAR(250), from_age INT, price INT)"

cursor.execute(sql)