import numpy as np
from scipy.io import wavfile
from scipy.fft import fft
import matplotlib.pyplot as plt
import pprint as pprint

if __name__ == '__main__':
    sample_rate, data = wavfile.read("e_er.wav") # read in the data
    # Frame length in samples (0.1 seconds)
    frame_length = int(0.1 * sample_rate)
    print(f'sample rate {sample_rate}')
    print(f'frame_length {frame_length}')

    # # Create segments
    # segments = [data[i:i + frame_length] for i in range(0, len(data), frame_length)]

    # # Remove any incomplete segment at the end
    # segments = [seg for seg in segments if len(seg) == frame_length]


def fourier_transform(data):
    return False
