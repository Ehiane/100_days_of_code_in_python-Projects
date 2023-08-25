
##SMTP - [Simple Mail Transport Protocol]:
# this contains all the rules that determine how an email 
# is received, passed and sent around the internet.
#@ simple analogy, SMTP is like a postman for a post office(your email provider)



## HOW EMAIL'S WORK:
# for instance, lets say im sending an email from my gmail account to someones
# yahoo account. my mail goes from my laptop to the Gmail mail server 
# then from there transports  to the yahoo mail server and holds it until the 
# receipient comes online. Once the receipient is online, then the mail is 
# downloaded to the user's system.


##  SYNTAX
# #* makes it impossible for the mail to be understood if intercepted by a third party.
# connection.starttls(); #basically makes the connection secure.
# connection.login(user = my_email, password = password_)
# connection.sendmail(
#     from_addr = my_email, 
#     to_addrs = recepient_email, 
#     msg="Subject:Hello\n\nThis is the body of my mail."
#     );
# connection.close();