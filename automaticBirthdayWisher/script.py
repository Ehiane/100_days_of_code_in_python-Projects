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
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls(); #basically makes the connection secure.
    connection.login(user = my_email, password = password_)
    connection.sendmail(
        from_addr = my_email, 
        to_addrs = recepient_email, 
        msg="Subject:Hello\n\nThis is the body of my mail."
    );


# hi again
# school stuff started slowing down. 

# today = dt.datetime.now()
# print("Todays date : ",today);

# year = today.year;
# print(f"the year: {year}");

# ----------[SAT 9th sept 2023]----------

