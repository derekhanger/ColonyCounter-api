from datetime import datetime

class AgarPlate:
    def __init__(self, img):
        self.img = img
        self.date = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
        self.count = -1