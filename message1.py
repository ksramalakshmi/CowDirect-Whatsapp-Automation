from pywhatkit import sendwhatmsg_instantly as sendwhatmsg
import pandas as pd
from datetime import date, datetime

data = pd.read_csv("sample.csv")

if len(data.columns) != 10:
    print("Please check the file. It should have 10 columns.")
    exit()

today = date.today()
today = today.strftime("%d/%m/%Y")

for index, row in data.iterrows():
    if row['Status'] != 'Inactive':
        milk_supplied = str(row['Milk supply'])
        payment_received = str(row['This month payment received'])
        previous_month = row['Previous month pending bill']
        cost_of_milk = str(row['Milk sale value'])
        remaining_balance = row['Remaining to pay']

        message= """"""
        if remaining_balance < 0 and previous_month < 0:
            message="""
Dear Customer,

Milk account from 01/04/2023 to """ + today + """.

Milk supplied:""" + milk_supplied + """ Ltrs
Supplied milk cost: Rs.""" + cost_of_milk + """
Paid this month: Rs.""" + payment_received + """
Last month advance: Rs.""" + str(previous_month).strip('-') + """
Balance excess: Rs.""" + str(remaining_balance).strip('-') + """

Enjoy Natural Cow Milk Daily,
Team CowDirect
                    """
        elif remaining_balance < 0 and previous_month > 0:
            message="""
Dear Customer,

Milk account from 01/04/2023 to """ + today + """.

Milk supplied:""" + milk_supplied + """ Ltrs
Supplied milk cost: Rs.""" + cost_of_milk + """
Paid this month: Rs.""" + payment_received + """
Last month due: Rs.""" + str(previous_month) + """
Balance excess: Rs.""" + str(remaining_balance).strip('-') + """

Enjoy Natural Cow Milk Daily,
Team CowDirect
                    """
            
        elif remaining_balance > 0 and previous_month > 0:
            message="""
Dear Customer,

Milk account from 01/04/2023 to """ + today + """.

Milk supplied: """ + milk_supplied + """ Ltrs
Supplied milk cost : Rs.""" + cost_of_milk + """
Paid this month: Rs.""" + payment_received + """
Last month due: Rs.""" + str(previous_month) + """
*Balance due: Rs.""" + str(remaining_balance) + """*

*Kindly pay Rs.""" + str(remaining_balance) + """*,

Enjoy Natural Cow Milk Daily,
Team CowDirect
                    """

        elif remaining_balance > 0 and previous_month < 0:
            message="""
Dear Customer,

Milk account from 01/04/2023 to """ + today + """.

Milk supplied: """ + milk_supplied + """ Ltrs
Supplied milk cost : Rs.""" + cost_of_milk + """
Paid this month: Rs.""" + payment_received + """
Last month advance: Rs.""" + str(previous_month).strip('-') + """
*Balance due: Rs.""" + str(remaining_balance) + """*

*Kindly pay Rs.""" + str(remaining_balance) + """*,

Enjoy Natural Cow Milk Daily,
Team CowDirect
                    """

        phone_no = "+91" + str(row['Phone number'])

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_time = current_time.split(":")
        current_time = [int(i) for i in current_time]

        sendwhatmsg(phone_no, message, tab_close=True, wait_time=20)

        print(message)
        print("---------------------------------------------------")
print("All messages sent successfully!")
