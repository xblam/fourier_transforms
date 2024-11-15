import numpy as np
from scipy.io import wavfile
from scipy.fft import fft
import matplotlib.pyplot as plt
import pprint as pprint


file_path = "e_er.wav"  # wave file path
sampling_rate, data = wavfile.read(file_path)

# Check if the audio is stereo or mono
if len(data.shape) > 1:
    data = data[:, 0]  # Use only one channel if stereo

# set the start and end times
start_time = 5
end_time = 6
start_sample = int(start_time * sampling_rate)
end_sample = int(end_time * sampling_rate)
s1 = data[start_sample:end_sample]

time_axis = np.linspace(start_time, end_time, len(s1))

# Plot the waveform
# plt.figure(figsize=(10, 4))
# plt.plot(time_axis, s1, color='blue')
# plt.title(f"waves from {start_time} to {end_time} seconds")
# plt.xlabel("time (seconds)")
# plt.ylabel("amplitude")
# plt.grid()
# plt.show()

# perform fft on the data
fft_result = np.fft.fft(s1)
fft_magnitude = np.abs(fft_result)
fft_frequencies = np.fft.fftfreq(len(fft_result), d=1/sampling_rate)

# positive freqs are the freqs that we can break it down into
positive_freqs = fft_frequencies[:len(fft_frequencies)//2]

# this is just how much they impact on the overall sound
positive_magnitude = fft_magnitude[:len(fft_result)//2]

print(positive_freqs.shape)
print(positive_magnitude.shape)

# Plot the Frequency Spectrum
# plt.figure(figsize=(10, 4))
# plt.plot(positive_freqs, positive_magnitude, color='red')
# plt.title(f"Frequency Spectrum (5-6 Seconds)")
# plt.xlabel("Frequency (Hz)")
# plt.ylabel("Magnitude")
# plt.grid()
# plt.show()

#might be able to partition the midi notes into different places, sum up the freqs and magnitudes over those regions to return how much of that note I should play