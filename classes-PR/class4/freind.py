class friend:
     def __init__(self,name):
         self.name=name
         self.message='party'
     def invite(self,message):
         self.message=message
     def showInvite(self):
         return self.message
class party:
    def __init__(self,place):
        self.place=place
        self.friends =[]
    def addFriend(self,friend):
        self.friends.append(friend)
    def deleteFriend(self,friend):
        self.friends.remove(friend)
    def sendInvites(self,date):
        for friend in self.friends:
            friend.invite(f'{self.place}:{date}')
if __name__=='__main__':
    party=party("Summer party")
    james=friend("james")

    party.addFriend(james)
    party.sendInvites("Friday ")
    
    print(friend.showInvite(james))

