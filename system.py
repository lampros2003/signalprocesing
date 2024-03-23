from functools import cache
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
#define plot parameters

plt.rcParams['figure.dpi'] = 100
plt.rcParams['figure.figsize'] = (9, 7)
#get Fs and sample array
sampFreq, sound = wavfile.read('recordingX (1).wav')
xn = np.asarray(sound)
@cache
def y(n):
    if n >= 2:
        return xn[n]+((-1.9999)*xn[n-1])+ (xn[n-2]) +(1.8999*y(n-1))+((- 0.9025)* y(n-2))
    if n>= 1:
        return xn[n]-1.9999*xn[n-1]+1.8999*y(n-1)
    else:
        return xn[n]

#get the fft
#i use 3000 samples as 80 didnt provide a good enough image
fft_spectrum1 = np.fft.rfft(sound[:1000])
#get abs so i can plot
fft_spectrum_abs1 = np.abs(fft_spectrum1)
# get frequencies in signal
freq = np.fft.rfftfreq(1000, d=1/sampFreq)
fft_spectrum_abs1 = fft_spectrum_abs1 #/ max(fft_spectrum_abs1)
plt.subplot(1,2,1)

fft_spectrum2 = np.fft.rfft([y(n) for n in range(1000)])
#get abs so i can plot
fft_spectrum_abs2 = np.abs(fft_spectrum2)
# get frequencies in signal
freq = np.fft.rfftfreq(1000, d=1/sampFreq)


plt.subplot(1,2,1)
plt.plot(freq, fft_spectrum_abs1)
plt.plot(max(freq)+freq, np.flip(fft_spectrum_abs1))
plt.xlabel("frequency, Hz x()")
plt.ylabel("Amplitude, units")

freq = np.fft.rfftfreq(1000, d=1/sampFreq)
plt.subplot(1,2,2)
plt.plot(freq, fft_spectrum_abs2)
plt.plot(sampFreq/2+freq, np.flip(fft_spectrum_abs2))
plt.xlabel("frequency, Hz y(n)")
plt.ylabel("Amplitude, units")
plt.tight_layout()
plt.show()

plt.subplot(1,2,1)
plt.stem(range(80),sound[:80],'-o',)
plt.xlabel("x(n), sample #")
plt.tight_layout()
plt.subplot(1,2,2)
yvals = [y(n) for n in range(80)]
plt.stem(range(80),yvals,'-o',)
plt.xlabel("y(n), sample #")
plt.tight_layout()
plt.show()
