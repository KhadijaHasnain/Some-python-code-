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
To format the body of the email with bold text, you can use HTML formatting within the body of the email. Here's how you can modify the `body` variable to include bold text:

html = f"""\
    <html>
      <body>
        <p style="color:red;">Your main text goes here.</p>
        <p style="color:green;"><strong>Contact Us:</strong><br>Email: {email}<br>Phone: +1234567890</p>
      </body>
    </html>
    """

This HTML structure uses `<strong>` tags to make the text bold. When you send this email, it will appear with the specified formatting. Just replace the `body` variable in your code with this updated version.

# Send email to each address
for email in emails:
    mail = outlook.CreateItem(0)
    mail.To = email
    mail.Subject = subject
    mail.Body = body
    mail.Send()

print("Emails have been sent successfully!")
