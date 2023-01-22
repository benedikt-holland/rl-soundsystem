import wave
import numpy as np
from sklearn.decomposition import FastICA
import scipy.io.wavfile as wf

if __name__ == '__main__':
    input_wave = wave.open("input.wav", "r")
    output_wave = wave.open("output.wav", "r")
    fs = input_wave.getframerate()
    input_raw = input_wave.readframes(-1)
    output_raw = output_wave.readframes(-1)
    input = np.frombuffer(input_raw, 'int16')
    output = np.frombuffer(output_raw, 'int16')
    X = list(zip(input, output[:int(len(output)/2)], output[int(len(output)/2):]))
    ica = FastICA(n_components=3, whiten="arbitrary-variance")
    X_out = ica.fit_transform(X)
    X_1 = np.int16(X_out[:,:1]*32767*100)
    X_2 = np.int16(X_out[:,2]*32767*100)
    wf.write("input_edit.wav", fs, X_1)
    wf.write("output_edit.wav", fs, X_2)
    
    