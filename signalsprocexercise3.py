import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
#define plot parameters

plt.rcParams['figure.dpi'] = 100
plt.rcParams['figure.figsize'] = (9, 7)
#get Fs and sample array
sampFreq, sound = wavfile.read('recordingX (1).wav')
#convert to values from -1 to 1
sound = sound / 2.0**15
#print sound aray shape to find the number of chanels
print(sound,sampFreq)
#sound is single chanel
#sound length
length_in_s = sound.shape[0] / sampFreq
time = np.arange(sound.shape[0]) / sound.shape[0] * length_in_s

# get the fft
#i use 4000 samples as 80 didnt provide a good enough image
fft_spectrum = np.fft.rfft(sound[:4000])
#get abs so i can plot
fft_spectrum_abs = np.abs(fft_spectrum)
# get frequencies in signal
freq = np.fft.rfftfreq(4000, d=1/sampFreq)

#
lfft_spectrum_abs = fft_spectrum_abs / max(fft_spectrum_abs)

plt.subplot(1,2,1)
#plot first 80 samples as dictated
plt.stem(range(80),sound[:80],'-o',)

plt.xlabel("x(n), sample #")
plt.tight_layout()

plt.subplot(1,2,2)
plt.plot(freq, fft_spectrum_abs)
plt.plot(sampFreq/2+freq, np.flip(fft_spectrum_abs))

plt.xlabel("frequency, Hz")
plt.ylabel("Amplitude, units")
plt.tight_layout()
plt.show()


