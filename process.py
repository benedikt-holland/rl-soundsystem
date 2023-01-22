import wave
import numpy as np
from sklearn.decomposition import FastICA
from sklearn.preprocessing import normalize
import scipy.io.wavfile as wf

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
    wf.write("output_edit.wav", fs_out, output)
    output = output[:, 0]
    output = output / np.linalg.norm(output)
    input = input / np.linalg.norm(input)
    result = input - output
    wf.write("input_edit.wav", fs_in, 32767*100*result.astype("int16"))
    
    