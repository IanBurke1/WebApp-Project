import sqlite3

db = sqlite3.connect('bmi.db')
cur = db.cursor()

db.execute('CREATE TABLE user_input (height DOUBLE, weight DOUBLE)')
db.commit()
db.close()