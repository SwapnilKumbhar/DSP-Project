import math

class Notes:
    TONE = 220
    NOTES = []
    MAJOR = [0,2,4,5,7,9,11]

    def __init__(self):
        for x in range(0,12):
            self.NOTES.append(self.TONE * 2**(x/12))

    def getScale(self,Trans):
        SCALE = []
        for num in self.MAJOR:
            SCALE.append(self.NOTES[(Trans+num)%12])
        return SCALE

    def normalize(self,note):
        if note < self.TONE:
            return self.normalize(note*2)
        elif note > 2*self.TONE:
            return self.normalize(note/2)
        else:
            return note

    def getStep(self,fnew,fold):
        return 12*math.log(fnew/fold,2)
