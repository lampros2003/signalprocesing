
import math
import numpy as np
import matplotlib.pyplot as plt
import wave

file_path = "recordingX (1).wav"

with wave.open(file_path, "rb") as wav_file:
     sample_width=wav_file.getsampwidth()
     audio_data = wav_file.readframes(-1) #get as a byte string
     sample_rate=wav_file.getframerate()

#converting byte string to a numpy array of integers

if sample_width == 1:
     audio_array = np.frombuffer(audio_data, dtype=np.uint8)
elif sample_width == 2:
     audio_array = np.frombuffer(audio_data, dtype=np.int16)

duration=len(audio_array)/sample_rate

time_index=np.arange(len(audio_array))

#time domain representation
time=np.linspace(0, duration, len(audio_array))
#samples
spec_samples=audio_array[0:80]


# coefficients
b0 = 1.0
b1 = -1.9999
b2 = 1.0
a1 = 1.8999
a2 = -0.9025

# sampling Frequency
F = sample_rate 

output_signal = np.zeros(len(audio_array))

for i in range(len(audio_array)):
    if i >= 2:
        output_signal[i] = b0 * audio_array[i] + b1 * audio_array[i - 1] + b2 * audio_array[i - 2] + a1 * output_signal[i - 1] + a2 * output_signal[i - 2]
    elif i >= 1:
        output_signal[i] = b0 * audio_array[i] + b1 * audio_array[i - 1] + a1 * output_signal[i - 1]
    else:
        output_signal[i] = b0 * audio_array[i]

final_output_signal=output_signal[0:sample_rate]

#computing the spectrum using FFT algorithm
spectrum = np.fft.fft(final_output_signal)

#frequencies that correspond to spectrum bins
frequencies = np.fft.fftfreq(len(spectrum), d=1/sample_rate)

plt.figure()
plt.plot(frequencies, np.abs(spectrum),label='X')

plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")

plt.title("Audio Signal")
plt.grid(True)
plt.show()