import requests
import smtplib


# api key

api_file = open('API key for Google maps.txt', 'r')
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
    sender = 'pvcpython11@gmail.com'
    reciepient = 'pvcpython11@gmail.com'
    subject = "Email from Python code for Google Maps API"
    message = "Hi, the code works!"
    
    email = 'Subject: {}\n\n{}'.format(subject,message)

    password = 'tishapro11'

    send_email = smtplib.SMTP("smtp.gmail.com",587)

    send_email.starttls()

    send_email.login(sender,password)

    send_email.sendmail(sender,reciepient,email)

    send_email.quit()

    print ("Sent email")

# check if travel time is more than 1 hour
# if (seconds > 3600):
#     # email constraints
#     sender = "pvcpython11@gmail.com"    
#     recipient = "pvcpython11@gmail.com"          
#     subject = "Sick Day"   
#     message = "Hi Team,\n\nSorry, but I can't make it into work today."
    
#     # format email
#     email = "Subject: {}\n\n{}".format(subject, message)
    
#     # get sender password
#     # password_file = open("password.txt", "r")
#     password = 'tishapro11'
#     # password_file.close()
    
#     # creates SMTP session 
#     s = smtplib.SMTP("smtp.gmail.com", 587) 
      
#     # start TLS for security 
#     s.starttls() 
      
#     # authentication 
#     print (sender, password)
#     s.login(sender, password) 
      
#     # sending the mail 
#     s.sendmail(sender, recipient, email)
      
#     # terminating the session 
#     s.quit() 

#     # success message
#     print("\nSuccessfully sent a sick-day email to", recipient, "since the travel time was too long")