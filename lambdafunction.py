import json
import smtplib
from email.message import EmailMessage
print('Loading function')
from password import *

def lambda_handler(event, context):
    json_str = json.dumps(event)
    #load the json to a string
    resp = json.loads(json_str)
    msg=EmailMessage()
    msg['Subject']='Succesfully Registered for Linux Training!'
    msg['From']='<your email id>'
    msg['to']= str(resp['email'])
    msg.set_content('Hi {}, You have been succesfully registered for Linx Training by JinnyCodes\n Join Training with this link- https://www.youtube.com/channel/UCTEY5KsyagWvsD6OdIA6xJA \n\n Thanks And Regards \n\n Jinnycodes'.format(resp['name']))
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login('<your email id>',password())
        smtp.send_message(msg)
    return("Thanks for coming to our website")


#Make sure to enable "Less secure app" functionality in your email address
#in api gateway while enabling COROS - in Access-control-allow-header put -> 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'
