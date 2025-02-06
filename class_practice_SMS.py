# Create multiple classes representing different notification channels (Email, SMS, and Push).
# Each channel class should implement the send method.
# Create a function that accepts any object and calls its send method. 
# The object should be able to handle the notification,
#  even if its class is unknown
# demonstrate the above irrespective of type



# try doing it for , "resend" option also.

class Email:
    def send(self):
        print("The email has been sent.")
class SMS:
    def send(self):
        print("The SMS has been sent.")
class Push:
    def send(self):
        print("The messaged is already pushed.")

def fun(notif):
    notif.send()

e=Email()
fun(e)

s=SMS()
fun(s)

p=Push()
fun(p)