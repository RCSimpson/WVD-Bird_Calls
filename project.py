import scipy
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import read
sample_rate, data = read("Audio/StarFinch.wav")
a=0.008
shift = int(0.2*data.shape[0])
length = a*data.shape[0]/sample_rate
N = int(a*data.shape[0])
time = np.linspace(0., length, N)
print(time.shape)
print(data[:N,:].shape)

data1 = data[shift:N+shift, 0]
data2 = data[shift:N+shift, 1]
# data1 = butter_lowpass_filter(data[shift:N+shift, 0], 1, sample_rate, 2)
# data2 = butter_lowpass_filter(data[shift:N+shift, 1], 1, sample_rate, 2)
import sounddevice as sd
sd.play(data1, sample_rate)

plt.plot(time, data1, label="Left channel")
plt.plot(time, data2, label="Right channel")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()

# from scipy.signal import hilbert
# dual = hilbert(data1, N=N)
#
# from scipy import signal
# from scipy.fft import fftshift
# shift = 100000
# f, t, Sxx = signal.spectrogram(dual, fs=sample_rate, return_onesided=False)
# print(Sxx.shape)
# print(t.shape)
# print(f.shape)
# plt.pcolormesh(t, f, Sxx, shading='gouraud')
# plt.ylabel('Frequency [Hz]')
# plt.xlabel('Time [sec]')
# plt.show()