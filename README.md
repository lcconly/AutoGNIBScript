# Program Language 
Python
# Package for Run
Install following package first (for Mac):
```
$ brew install chromedriver
$ pip install splinter
$ pip install twilio
```
# Your Information (a.txt)
```
GNIBNo=GNIB number
GNIBExDT=Expire date of GNIB: DD/MM/YYYY 
GivenName=Your Given Name 
SurName=Your SurName
DOB=Your Date of birth: DD/MM/YYYY
Email=Your Email
PPNo=Your Passport
```
# Get your twilio ID and Token
Twilio is used to inform you if new apponiment shows. You can visit [Twilio](https://www.twilio.com) to get news ID and Token and set you phone number. And then fill:
```
13  account_sid = "XXXXXXXXXXX"
14  auth_token = "XXXXXXXXXXX"
```
And also change:
```
85        message = client.messages.create(to="Receive Number",from_="Sent Number in Twilio",body="Hurry UP!!! Look at the computer!!!!")
```

#Run
```
$ Python gnib.py
```
