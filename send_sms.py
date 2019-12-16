from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACf9b90a44c9ad4df72b41cf9e26cb2f7d"
# Your Auth Token from twilio.com/console
auth_token  = "aa98d83c90acf4655349eb2da26ecbc5"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+8801764259025", 
    from_="+13342343184",
    body="hello rubayet i am rafa i want to be back..will u accept me ????please??")

print(message.sid)
