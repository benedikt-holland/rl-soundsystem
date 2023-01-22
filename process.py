import wave
import numpy as np
from sklearn.decomposition import FastICA
from sklearn.preprocessing import normalize
import scipy.io.wavfile as wf
import noisereduce as nr
import wavfile
import matplotlib.pyplot as plt


def normalize_subtract(data, noise):
    data_norm = np.linalg.norm(data)
    noise_norm = np.linalg.norm(noise)
    data /= data_norm
    noise /= noise_norm
    return data - noise


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
    output = output[:, 0]
    n_max = 300000
    result = nr.reduce_noise(input[:n_max], sr=fs_in ,y_noise=output[:n_max], n_jobs=-1)
    wf.write("input_edit.wav", fs_in, result.astype("int16"))
    
    