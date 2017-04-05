import smtplib
import MySQLdb
import datetime

# Send the mail
def sendText(messageBody):

    SUBJECT = ""
    TEXT = messageBody
    SERVER = "localhost"
    FROM = "tim@blah.com"
    TO = ["tresch@gmail.com"]

    # Prepare actual message
    message = """\
    %s
    """ % (TEXT)

    server = smtplib.SMTP(SERVER)
    server.sendmail(FROM, TO, message)
    server.quit()


#SQL data access part
db = MySQLdb.connect(host='localhost', user='pi', passwd='piTin', db='piHub')
cursor = db.cursor()
cursor.execute("select created, data1 from payload where node = 'garage' order by id desc limit 1")
db.commit()

row = cursor.fetchone()
    
print row

now = datetime.datetime.now()
created = row[0]
distance = float(row[1])

print now.hour
print distance

if distance < 1.0:
    print "open"
    if created.hour > 22:
        print "after 23"
        sendText("Garage Door is Open.")
    else:
        print "before 23"
else:
    print "closed"
    sendText("Garage Door is Closed.")

