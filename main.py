#!/usr/bin/env python3

import IO,Auto
import Plotter
import sys

def viewHelp():
    print('\nAUTOMATED PITCH CORRECTION')
    print('\tThis is an implementation of the Autotune Vocoder that is used in the Music Industry')
    print('\tThis program takes input a Wave file and pitch corrects it to the input Scale.')
    print('\nPROCEDURE')
    print('\tIt works as follows:')
    print('\t1. Take a small chunk of the data. Typically 0.1 seconds worth of data.')
    print('\t2. Transform it to frequency domain using Short term Fourier Tranform, keeping bin ')
    print('\tequal to sample rate, as this will segregate each frequency into bins of ')
    print('\t1 Hz.')
    print('\t3. Find the maximum amplitude among the frequency bins, this is our dominant frequency in the chunk.')
    print('\t4. Correspond the frequency with the closest frequency in the scale.')
    print('\t5. Transpose the current frequency to the matched frequency. Append this to output wave.')
    print('\t6. Move on to next chunk, repeat this procedure for the entire sequence.')
    print('\nUSAGE')
    print('\t./main <path to input file> <Scale> <path to output file [default is output.wav]>')

def start(ip,op,scale):
    io = IO.IO(ip)
    y, sr = io.load()
    
    auto = Auto.Autotune(y,sr,scale)
    print('Starting Pitch Correction.')
    yT = auto.correct()
    print('Pitch Correction Completed.')

    input('Enter any key to view output Plots.')
    print('Calculating Plots...')
    plt = Plotter.Plotter(y,sr,yT,sr)
    plt.plot()

    print('Dumping output to %s...'%op,end='')
    io.dump(op,yT,sr)
    print('Done.')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        viewHelp()
        sys.exit(0)
    else:
        op = 'output.wav'
        if sys.argv[1] == '-h' or sys.argv[1] == '--help':
            viewHelp()
            sys.exit(0)
        else:
            ip = sys.argv[1]
            scale = int(sys.argv[2])
            if sys.argv[3] is not None:
                op = sys.argv[3]
            start(ip,op,scale)
            print('Exiting...')

