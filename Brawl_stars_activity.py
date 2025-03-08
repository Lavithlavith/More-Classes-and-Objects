class BrawlStars:
    def __init__(self,charecterName):
        self.charecterName= charecterName
    
    def startGame(self):
        for i in range(1,10):
            print(self.charecterName ,"is still playing")
    
    def __del__(self):
        print(self.charecterName, "is destroyed")

chester = BrawlStars("chester")
chester.startGame()

for i in range(1,10):
    print("this is loop")
