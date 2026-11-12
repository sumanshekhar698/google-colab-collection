
class NotifierBase:
    def send(self, msg):
        raise NotImplementedError("This method should be implemented by sub class")


class SlackNotifier(NotifierBase):
    def send(self, msg):
        return f" Slack msg: {msg}"


class EmailNotifier(NotifierBase):
    def send(self, msg):
        return f" Email msg: {msg}"


# COMPOSITION :: has a

class Email:
    def deliver(self, msg):
        return f" Email msg: {msg}"


class Slack:
    def deliver(self, msg):
        return f" Slack msg: {msg}"

class SMS:
    def deliver(self, msg):
        return f" SMS msg: {msg}"

class WhatsApp:
    def deliver(self, msg):
        return f" WhatsApp msg: {msg}"


class Notifier:

    def __init__(self, *channels):
        self.channels= list(channels)

    def send(self, msg):
        return [channel.deliver(msg)  for channel in self.channels]


notifer = Notifier(Slack(), SMS(), Email())

list_of_msgs = notifer.send("Deployment Done!!!")

for msg in list_of_msgs:
    print(msg)


print()
notifer.channels = [Slack(), WhatsApp()]
list_of_msgs = notifer.send("Deployment Done!!!")

for msg in list_of_msgs:
    print(msg)