# THE OBSERVER PATTERN
class Subscriber:
    
    def __init__(self,name):
        self.name = name
    
    def update(self,message):
        self.message = message   
        print(f"{self.name} received news : {self.message}")

class NewsChannel:
    
    def __init__(self):
        self.subscribers = []
        
    def subscribe(self,subscriber_obj):
        self.subscribers.append(subscriber_obj)
        
    def unsubscribe(self,subscriber_obj):
        self.subscribers.remove(subscriber_obj)
    
    def notify(self,news):
        for subscriber in self.subscribers:
            subscriber.update(news)
    
times_of_india = NewsChannel()

vignesh = Subscriber("Vignesh")
vickyy = Subscriber("Vickyy")
unknown = Subscriber("Unknown")

times_of_india.subscribe(vignesh)
times_of_india.subscribe(vickyy)
times_of_india.subscribe(unknown)

times_of_india.notify("Mr.Vignesh Jadhav become President...!!!!")

times_of_india.unsubscribe(unknown)

times_of_india.notify("Soon the World will .......:(")
