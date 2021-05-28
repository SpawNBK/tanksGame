import os


class PlayerAnimation:

    @staticmethod
    def getSprites(stage):
        if stage == 1:
            return {"driveRight": [os.path.join("sprites", "player", "right_1.png"),
                                   os.path.join("sprites", "player", "right_2.png"),
                                   os.path.join("sprites", "player", "right_3.png"),
                                   os.path.join("sprites", "player", "right_4.png"),
                                   os.path.join("sprites", "player", "right_5.png"),
                                   os.path.join("sprites", "player", "right_6.png")],

                    "driveLeft": [os.path.join("sprites", "player", "left_1.png"),
                                  os.path.join("sprites", "player", "left_2.png"),
                                  os.path.join("sprites", "player", "left_3.png"),
                                  os.path.join("sprites", "player", "left_4.png"),
                                  os.path.join("sprites", "player", "left_5.png"),
                                  os.path.join("sprites", "player", "left_6.png")],

                    "driveUp": [os.path.join("sprites", "player", "up_1.png"),
                                os.path.join("sprites", "player", "up_2.png"),
                                os.path.join("sprites", "player", "up_3.png"),
                                os.path.join("sprites", "player", "up_4.png"),
                                os.path.join("sprites", "player", "up_5.png"),
                                os.path.join("sprites", "player", "up_6.png")],

                    "driveDown": [os.path.join("sprites", "player", "down_1.png"),
                                  os.path.join("sprites", "player", "down_2.png"),
                                  os.path.join("sprites", "player", "down_3.png"),
                                  os.path.join("sprites", "player", "down_4.png"),
                                  os.path.join("sprites", "player", "down_5.png"),
                                  os.path.join("sprites", "player", "down_6.png")] }
