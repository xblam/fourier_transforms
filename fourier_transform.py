import numpy as np
import matplotlib.pyplot as plt

# Define the function points
x = np.linspace(-1, 1, 1024)
y = x**2

# Perform the Fourier Transform
fft_y = np.fft.fft(y)
freq = np.fft.fftfreq(len(x), d=(x[1] - x[0]))

# Initialize an empty list to store each sinusoidal component
sin_components = []

# Reconstruct the function using each individual frequency component
for i in range(len(fft_y)):
    # Extract the current frequency component
    amplitude = np.abs(fft_y[i]) / len(x)
    phase = np.angle(fft_y[i])
    frequency = freq[i]
    
    # Generate the sinusoidal component for this frequency
    sin_component = amplitude * np.cos(2 * np.pi * frequency * x + phase)
    sin_components.append(sin_component)

# Plot the individual sinusoidal components
plt.figure(1)
for i, sin_wave in enumerate(sin_components[:10]):  # Display first 10 components
    plt.plot(x, sin_wave, label=f"Component {i}")
plt.xlabel("x")
plt.ylabel("Amplitude")
plt.legend()
plt.title("First 10 Sinusoidal Components of x^2")
plt.show()

plt.figure(2)
plt.plot(x, y)
plt.show()