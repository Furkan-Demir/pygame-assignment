class Camera():
    def __init__(self,player):
        self.x = player.x - 384
        self.y = player.y - 284
    def update(self,player):
        self.x = player.x - 384
        self.y = player.y - 284