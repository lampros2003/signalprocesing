import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
#define plot parameters

plt.rcParams['figure.dpi'] = 100
plt.rcParams['figure.figsize'] = (9, 7)
#get Fs and sample array
sampFreq, sound = wavfile.read('recordingX (1).wav')
#multiply sampling frequency by two
for i in range(int(sound.size/2)):
    sound[i] = sound[2*i]
sound = sound[:int(sound.size/2)]
sampFreq = sampFreq/2
#convert to values from -1 to 1
sound = sound / 2.0**15
#print sound aray shape to find the number of chanels

#sound is single chanel
#sound length
length_in_s = sound.shape[0] / sampFreq
time = np.arange(sound.shape[0]) / sound.shape[0] * length_in_s

# get the fft
#i use 3000 samples as 80 didnt provide a good enough image
fft_spectrum = np.fft.rfft(sound[:4000])
#get abs so i can plot
fft_spectrum_abs = np.abs(fft_spectrum)
# get frequencies in signal
freq = np.fft.rfftfreq(4000, d=1/sampFreq)

#
fft_spectrum_abs = fft_spectrum_abs / max(fft_spectrum_abs)

plt.subplot(1,2,1)
#plot first 40 samples as dictated
plt.stem(range(40),sound[:40],'-o',)

plt.xlabel("x(2n), sample #")
plt.tight_layout()

plt.subplot(1,2,2)
plt.plot(freq, fft_spectrum_abs)
plt.plot(sampFreq/2+freq, np.flip(fft_spectrum_abs))

plt.xlabel("frequency, Hz")
plt.ylabel("Amplitude, units")
plt.tight_layout()
plt.show()


