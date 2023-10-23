
class Player:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
    