class Controls:
    def __init__(self):

        # Hahmon arvot
        self.speed = 6
        self.gravity = 0.8
        self.jump_height = -18
        self.jump_count = 0
        self.player_x = 0

    def keypress(self, pressed):
        if pressed == "right":
            return 1
        if pressed == "left":
            return -1
        else:
            pass

    def jump_control(self):
        if self.jump_count == 0:
            return self.jump_height
        return 0
