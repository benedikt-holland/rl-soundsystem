import wave
import numpy as np
from sklearn.decomposition import FastICA
from sklearn.preprocessing import normalize
import scipy.io.wavfile as wf
import noisereduce as nr
import wavfile

if __name__ == '__main__':
    input, rate_in, bits_in = wavfile.read("input.wav")
    output, rate_out, bits_out = wavfile.read("output.wav")
    result = nr.reduce_noise(np.array(input), sr=rate_in, y_noise=np.array(output), stationary=True, tmp_folder="./tmp")
    wavfile.write("input_edit.wav", result, rate_in, bits_in)
    