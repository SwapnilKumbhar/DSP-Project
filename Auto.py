import librosa
import Notes
import numpy as np

class Autotune:
    def __init__(self, y, sr, scale):
        self.INPUT_WAVE = y
        self.INPUT_SR = sr
        self.SCALE = scale
        self._note = Notes.Notes(scale)
        
        self.NOTES = self._note.getScale()
        self.OUTPUT_WAVE = np.empty(shape=self.INPUT_WAVE.shape)

    def correct(self):
        step = int(self.INPUT_SR/20)
        print('Detected fq\tCorrected fq\tCorrection factor')
        print('--------------------------------------------')
        for x in range(0,len(self.INPUT_WAVE),step):
            # find STFT
            # Match to closest frequency
            # transpose
            # Append to self.OUTPUT_WAVE
            # Return output wave
            
            y = self.INPUT_WAVE[x:x+step]
            f = self._findStft(y)
            
            diff_array = [ np.abs(note - f) for note in self.NOTES ]
            note = np.argmin(diff_array)
            print(f,end='\t')
            print(self.NOTES[note],end='\t')

            self.OUTPUT_WAVE[x:x+step] = self._transpose(y, f, self.NOTES[note])
            #self.OUTPUT_WAVE = np.concatenate(self.OUTPUT_WAVE,self._transpose(y, f, self.NOTES[note]))

        print('-------------------------------------------')
        return librosa.util.normalize(self.OUTPUT_WAVE)
    
    def _findStft(self,y):
        # Find stft, use argmax, find mean if req
        # Return max amp frequency in the interval

        yD = librosa.stft(y,n_fft=self.INPUT_SR)
        arr = np.argmax(yD,axis=0)
        fq = np.mean(arr)

        return self._note.normalize(fq)
    
    def _transpose(self, y, fold, fnew):
        # Calculate the steps to be transposed based on the old and new frequencies.
        steps = self._note.getStep(fold,fnew)
        print(steps)
        yT = librosa.effects.pitch_shift(y,self.INPUT_SR,steps)
        return yT

