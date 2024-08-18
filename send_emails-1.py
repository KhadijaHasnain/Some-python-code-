import win32com.client as win32
import os

# Read email addresses from a text file
file_path = r'C:\Users\PMLS\Desktop\Email Automated Code\Emails1.txt'  # Change to your file's path
with open(file_path, 'r') as file:
    emails = [line.strip() for line in file if line.strip()]

# Check if Outlook is installed
try:
    outlook = win32.Dispatch('outlook.application')
except Exception as e:
    print("Error: Outlook application could not be accessed.")
    print(e)
    exit()

# Compose the email
subject = "Don't Miss Out: No Contracts, Free Setup, & Lowest Rates in Canada!"
body = """Good day,

Hope you’re doing well.

I’m reaching out to you in regards to your merchant processing services.
Tired of high processing fees? Our limited-time offer is here to give your business a boost without draining your budget!
Here's what you can expect from us:

•	Unbeatable Rates: Lifetime guaranteed fees starting as low as 0.10% for Visa and MasterCard.
•	Advanced Terminals: Get the latest GoDaddy/POYNT Smart Terminal for just $30/month, or choose any other terminal of your choice.
•	Low-Cost Debit: Just $0.04 per debit transaction.
•	No Setup Fees: Try our services without any upfront costs—no strings attached.
•	No Contracts: Cancel any time with zero penalties. You’re in control!
•	Quick Payouts: Next-day funding to keep your cash flow smooth.
•	24/7 Customer Support: Get immediate help without endless call trees.
•	Price Protection: We guarantee your rates will never increase.
•	Low Admin Fee: Just $5/month to cover administrative costs.

Check Out Your Savings 
Simply attach your recent merchant statement, and we'll do a free side-by-side comparison to show how much you could save.
We’re excited to help you take your business to new heights with our reliable and affordable merchant processing services. Got questions? Just hit 'reply' or give us a call.
Sincerely, 
Zack Nelson  
Sales Representative  
Email: zack@rarepayments.com  
Phone: +1 (807) 500 5520  
Rare Payments MSP/ISO 2023
"""

# Send email to each address
for email in emails:
    mail = outlook.CreateItem(0)
    mail.To = email
    mail.Subject = subject
    mail.Body = body
    mail.Send()

print("Emails have been sent successfully!")
