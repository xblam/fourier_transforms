import numpy as np
from scipy.io import wavfile
from scipy.fft import fft
import matplotlib.pyplot as plt

# Load WAV file
sample_rate, data = wavfile.read('your_file.wav')

# If stereo, select one channel
if data.ndim > 1:
    data = data[:, 0]

# Perform FFT on a segment of data (you could also use a sliding window for STFT)
n = len(data)
audio_fft = fft(data)
frequencies = np.fft.fftfreq(n, 1 / sample_rate)

# Plot the frequency spectrum
plt.plot(frequencies[:n // 2], np.abs(audio_fft)[:n // 2])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Frequency Spectrum')
plt.show()