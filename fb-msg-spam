import fbchat
from getpass import getpass
username = str(input("Username: "))
client = fbchat.Client(username, getpass())
name=str(input("Name : "))
friends = client.getUsers(name)
friend = friends[0]
msg = str(input("Message: "))
for u in range(100):
    sent = client.send(friend.uid, msg)
    if sent:
        print("Message sent successfully!")
