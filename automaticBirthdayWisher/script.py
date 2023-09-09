import smtplib;
import datetime as dt;

# smtplib.SMTP("smtp.gmail,com",port=587);

## MESSAGES WITH NO SUBJECT ARE PRIMED AS TARGET FOR SPAM MAILS. 

my_email = "ehianesocials@gmail.com"; #!this email should have the app password activated.
password_ = "ouyzzwqnznprrghu"  #password gotten from your email provider, (for gmail-> setup app password).
recepient_email = "ehiane.business@gmail.com";


# connection = smtplib.SMTP("smtp.gmail.com");

# # TLS- Transport Layer Security.
# A better way:
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls(); #basically makes the connection secure.
#     connection.login(user = my_email, password = password_)
#     connection.sendmail(
#         from_addr = my_email, 
#         to_addrs = recepient_email, 
#         msg="Subject:Hello\n\nThis is the body of my mail."
#     );


# hi again
# school stuff started slowing down. 

today = dt.datetime.now() #type : datetime
print("Todays date : ",today);

year = today.year; #type: int
print(f"the year: {year}");

# ----------[SAT 9th sept 2023]----------
# in the datetime string, you can tap into, day, month, year, hour,... ,microsecond

day_of_the_week = today.weekday()
print( "today is the ",day_of_the_week + 1, "day of the week"); #there's an offset of 1 because 0's the first number in computers.

# when creating a datetime object, the only thing you are required to give is the day, year & month
date_of_birth = dt.datetime(year=2003, month=7, day= 30);
print(f"your date of birth is {date_of_birth}")

