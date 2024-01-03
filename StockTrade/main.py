import requests
import datetime
from datetime import timedelta

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


#TODO: save as environmental varible before pushing
ALPHAVANTAGE_API_KEY = "UOLN9EF43FIMQQ9T" #stock price stuff 

stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': 'IBM',
    'apikey': ALPHAVANTAGE_API_KEY
}
stock_response = requests.get(STOCK_ENDPOINT,params=stock_params)

if stock_response.status_code == 200:
    stock_data = stock_response.json()
else:
    stock_response.raise_for_status()
    




def get_recent_dates(target_day:str,previous_day:str,data:dict):

    while target_day not in data["Time Series (Daily)"]:
        target_day = datetime.datetime.strptime(target_day,'%Y-%m-%d')
        target_day -= timedelta(days = 1)
        target_day = target_day.strftime(r"%Y-%m-%d")
    

    while previous_day not in data["Time Series (Daily)"]:
        previous_day = datetime.datetime.strptime(previous_day,'%Y-%m-%d')
        previous_day -= timedelta(days = 1)
        previous_day = previous_day.strftime(r"%Y-%m-%d")

    if previous_day == target_day:
        previous_day = datetime.datetime.strptime(previous_day,'%Y-%m-%d')
        previous_day -= timedelta(days = 1)
        previous_day = previous_day.strftime(r"%Y-%m-%d")


    return target_day,previous_day


def find_dates(data:dict):
    today = datetime.datetime.now()
    target_day = today - timedelta(days= 1)
    previous_day = target_day - timedelta(days= 1)

    #formatting dates
    target_day = target_day.strftime(r"%Y-%m-%d")
    previous_day = previous_day.strftime(r"%Y-%m-%d")
   
    if target_day not in data["Time Series (Daily)"] or previous_day not in data["Time Series (Daily)"]:
        target_day,previous_day = get_recent_dates(target_day=target_day, previous_day=previous_day,data=data)
    
    return target_day, previous_day
        
    
def get_price_perctage(data:dict):
    yesterday,dby = find_dates(data) #dby stands for day before yesterday
   
    #1.  - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
    #2. - Get the day before yesterday's closing stock price
    yesterday_closing_price, dby_closing_price = float(data["Time Series (Daily)"][yesterday]["4. close"]), float(data["Time Series (Daily)"][dby]["4. close"]) 
   
    #3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
    price_diff = abs(dby_closing_price-yesterday_closing_price)
    percent_diff = (price_diff/yesterday_closing_price) * 100
    
    #4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
    print(round(percent_diff,3))
    return percent_diff

get_price_perctage(stock_data)


def get_news(diff:float):
    if diff > 5:
        ...





#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

