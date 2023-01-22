import wave
import numpy as np
from sklearn.decomposition import FastICA
from sklearn.preprocessing import normalize
import scipy.io.wavfile as wf
import noisereduce as nr
import wavfile
import matplotlib.pyplot as plt

if __name__ == '__main__':
    input_wave = wave.open("input.wav", "r")
    output_wave = wave.open("output.wav", "r")
    fs_in = input_wave.getframerate()
    fs_out = output_wave.getframerate()
    input_raw = input_wave.readframes(-1)
    output_raw = output_wave.readframes(-1)
    input = np.frombuffer(input_raw, 'int16')
    output = np.frombuffer(output_raw, 'int16')
    output = np.reshape(output, (-1, 2))
    #wf.write("output_edit.wav", fs_out, output)
    output = output[:, 0]
    output_norm = np.linalg.norm(output)
    input_norm = np.linalg.norm(input)
    output = output / output_norm
    input = input / input_norm
    result = input - output
    plt.plot(input)
    plt.plot(result, alpha=0.5)
    plt.show()
    wf.write("input_edit.wav", fs_in, result.astype("int16"))
    
    