import win32com.client as win32
import os

# Read email addresses from a text file
file_path = r'A:\Python automate email sending system\emails.txt'  # Change to your file's path
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
subject = "Exciting Marketing Offer!"

# HTML body with bold text
for email in emails:
    html = f"""\
        <html>
          <body>
            <p style="color:red;">Your main text goes here.</p>
            <p style="color:green;"><strong>Contact Us:</strong><br>Email: {email}<br>Phone: +1234567890</p>
          </body>
        </html>
        """

    # Send email to each address
    mail = outlook.CreateItem(0)
    mail.To = email
    mail.Subject = subject
    mail.HTMLBody = html
    mail.Send()

print("Emails have been sent successfully!")
