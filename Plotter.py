import librosa
import librosa.display as disp
import matplotlib.pyplot as plt

class Plotter:
    N_ROWS = 3
    N_COLUMNS = 3

    def __init__(self,y,sr,oy,osr):
        self.INPUT_WAVE = y
        self.INPUT_SR = sr
        self.OUTPUT_WAVE = oy
        self.OUTPUT_SR = osr

    def plot(self):
        '''Plot waveplot, power spectrogram, chromagram.
        Left column will show the INPUT wave.
        Right column will show the OUTPUT wave.
        '''
        
        plt.subplot(321)
        plt.title('Input Waveform')
        self.plotWave(self.INPUT_WAVE,self.INPUT_SR)

        plt.subplot(322)
        plt.title('Output Waveform')
        self.plotWave(self.OUTPUT_WAVE,self.OUTPUT_SR)

        plt.subplot(323)
        plt.title('Input Power Spectrogram')
        self.plotSpec(self.INPUT_WAVE,self.INPUT_SR) 
        
        plt.subplot(324)
        plt.title('Output Power Spectrogram')
        self.plotSpec(self.OUTPUT_WAVE,self.OUTPUT_SR) 

        plt.subplot(325)
        plt.title('Input Chromatograph')
        self.plotChroma(self.INPUT_WAVE,self.INPUT_SR) 

        plt.subplot(326)
        plt.title('Output Chromatograph')
        self.plotChroma(self.OUTPUT_WAVE,self.OUTPUT_SR) 

        plt.show()

        return

    def plotWave(self,y,sr):
        print('Plotting waveplot...',end='')
        disp.waveplot(y,sr)
        print('Done')
        return

    def plotSpec(self,y,sr):
        print('Plotting Power Spectrogram...',end="")
        yD = librosa.stft(y,n_fft=sr)
        disp.specshow(librosa.amplitude_to_db(yD),y_axis='log',x_axis='time')
        print('Done')
        return

    def plotChroma(self,y,sr):
        print('Plotting Chromatograph...',end='')
        cD = librosa.feature.chroma_stft(y,n_fft=sr)
        disp.specshow(cD,y_axis='chroma',x_axis='time')
        print('Done')
        return
