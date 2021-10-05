import requests
import smtplib

# API Key in a file

api_file = open('..', 'r')
api_key = api_file.read()
api_file.close()

home = input("Enter home address: ")
work = input("\nEnter work address: ")

url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"

get_request = requests.get(url + "origins=" + home + "&destinations=" + work + "&key=" + api_key) 

time = get_request.json()['rows'][0]['elements'][0]['duration']['text']
seconds = get_request.json()['rows'][0]['elements'][0]['duration']['value']

print ("Time to reach from home to work is: ", time )

if (seconds > 3600):
    sender = '..'
    reciepient = '..'
    subject = "Email from Python code for Google Maps API"
    message = "Hello! The commute time is more than an hour."  
    password = '..'

    # Format email
    email = 'Subject: {}\n\n{}'.format(subject,message)
    
    # Create a SMTP session 
    send_email = smtplib.SMTP("smtp.gmail.com",587)

    # Start TLS for security 
    send_email.starttls()

    # Authentication 
    send_email.login(sender,password)

    # Sending the mail 
    send_email.sendmail(sender,reciepient,email)

    # Terminating the session
    send_email.quit()

    # Success message
    print ("Sent email since commute takes more than an hour!")