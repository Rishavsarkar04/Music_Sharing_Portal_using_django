import threading
from app.models import MyUser
class CustomThread(threading.Thread):
    elist=[]
    def __init__(self,obj,list=[]):
        threading.Thread.__init__(self)
        self.object=obj
        self.elist=list 
    def run(self):
        try:
            for em in self.elist:
                user = MyUser.objects.get(email=em)
                self.object.emails.add(user)
        except Exception as e:
            print(e)
