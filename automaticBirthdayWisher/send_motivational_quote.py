
##ESSENTIALS:
import datetime as dt, random as r, smtplib as emailsender
QUOTES_FILE = "quotes.txt"
FIRST_QUOTE = 0
DOMAIN_ = "smtp.gmail.com"
MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY,SATURDAY,SUNDAY =  1,2,3,4,5,6,7

##Objective:
"""
*find current day of the week
* get quotes from quotes file, store them in a list
* randomly pick a quote from the list
* send the email using smtplib
"""

# $----------------------------------------[QUOTE GENERATION SECTION]--------------------------------------------------------------

# found day of the week
today = dt.datetime.now() #getting today's date
day_of_the_week = today.weekday() + 1; #adjusting offset of 1;

# works fine.
def get_quotes(filename=QUOTES_FILE):
    """
    -> List;
    gets quotes from quotes.txt, stores in a list & returns the list.
    """
    # creating list;
    all_quotes = [];
    with open(filename, "r") as file:
        lines = file.readlines();
        for line in lines:
            all_quotes.append(line);
    return all_quotes;

# works fine.
def pick_a_quote():
    """
    ->String;
    randomly picks a quote from the get_quotes() funct and returns it.
    """
    all_quotes = get_quotes();
    x = r.randrange(FIRST_QUOTE,len(all_quotes)+1);
    chosen_quote = all_quotes[x];
    return chosen_quote;


# $----------------------------------------[EMAIL SENDING SECTION]--------------------------------------------------------------
senders_email = "ehianesocials@gmail.com";
password_ = "ouyzzwqnznprrghu";
recepient_email = "ehiane.business@gmail.com";

def send_email(sender, receipent, the_password, email_subject,email_body):
    """
    -> None;
    sends the motivational quote to the recepient provided the prior setup is good. 
    !DOESN'T ACCEPT EMOJI'S IN THE TEXT BODY
    """
    if day_of_the_week == SATURDAY:
        try:
            with emailsender.SMTP(DOMAIN_) as connection:
                connection.starttls(); #securing connection
                connection.login(user=sender, password=the_password)
                connection.sendmail(
                    from_addr= sender,
                    to_addrs= receipent,
                    msg=f"Subject: {email_subject}\n\n{email_body}"
                );
            print("email sent successfully")
        except emailsender.SMTPConnectError:
            raise emailsender.SMTPConnectError("There is a connection error, verify function args and try again");

def draft_and_send_email():
    send_email(sender=senders_email, receipent=recepient_email, the_password=password_, email_subject="Motivational quote of the day", email_body= pick_a_quote())

draft_and_send_email();