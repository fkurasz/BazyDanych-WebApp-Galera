import mysql.connector

db = mysql.connector.connect(
	host="172.17.0.2",
	user="my_user",
	passwd="my_password",
	database="szczepienia"
	)
	
mycursor=db.cursor()
mycursor.execute("SELECT VERSION()")
row=mycursor.fetchone()
#print("Server Version is ",row)

#mycursor.execute("INSERT INTO example ( id, name ) VALUES ( null, 'Pythonowe' );")
#db.commit()

mycursor.execute("SELECT * FROM pacjent")
for x in mycursor:
	print(x)
