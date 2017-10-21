import librosa
import Notes
import numpy as np

class Autotune:
    def __init__(self, y, sr, scale):
        self.INPUT_WAVE = y
        self.INPUT_SR = sr
        self.SCALE = scale
        self._note = Notes.Notes()
        
        self.NOTES = self._note.getScale(scale)

    def correct(self):
        step = int(sr/2)
        for x in range(0,len(y),step):
            # find STFT
            # Match to closest frequency
            # transpose
            # Append to self.OUTPUT_WAVE
            # Return output wave

        return
    
    def _findStft(self):
        # Find stft, use argmax, find mean if req
        # Return max amp frequency in the interval
        return
    
    def _transpose(self, fold, fnew):
        # Calculate the steps to be transposed based on the old and new frequencies.
        return
