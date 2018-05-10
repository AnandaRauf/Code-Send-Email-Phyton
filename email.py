"""# Send Email
# Code Phyton
# 10 Mei 2018
# Author: Ananda Rauf Maudui
# Name Program: email.py"""
import smtplib

sender = 'You Email@mail.com'
recipient = ['You Friends Email@mail.com']

message = """From: From Person <%s>
To: To Person <%s>
Subject: Testing SMTP E-Mail

Message this send via smtplib and accept by module SMTP Server Python.

""" % (sender, recipient)

try:

    smtpObj = smtplib.SMTP('localhost', 1025)
    smtpObj.sendmail(sender, recipient, message)    

    print "Berhasil Cok ^^"

except Exception, e:

 print str(e)
    print "Error: Yah Gagal Cok"