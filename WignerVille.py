import numpy as np
from tftb.generators import fmlin, amgauss, sigmerge, noisecg
from tftb.processing import WignerVilleDistribution
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.io.wavfile import read, write
import sounddevice as sd

def synthetic_bird(n=800, J=2, A=[0.5,1], F=[0.13,0.13], a=[0.002,0.001], T=[400,600]):
    n = np.linspace(0,800,800)
    tot=np.zeros(800)
    phi=0
    for j in range(J):
        phase= 2*np.pi*F[j]*n + phi
        gauss = np.exp(-a[j]*((n-T[j])**2)/2 )
        tot += A[j]*np.cos(phase)*gauss
    return tot + np.random.normal(0,0.03,800)

# bird_call = synthetic_bird()
# # print(bird_call)
# fig =plt.figure(figsize=(8,4))
# plt.plot(bird_call)
# plt.title('Synthetic Bird Syllable', fontsize=15)
# plt.xlabel('Time', fontsize=15)
# plt.ylabel('Amplitude', fontsize=15)
# plt.xticks(fontsize=12)
# plt.yticks(fontsize=12)
# plt.xlim([0,800])
# plt.tight_layout()
# plt.savefig('synthbird')
# plt.show()

def zebra_finches():
    sample_rate, data = read("Audio/ZebraFinchSongs.wav")
    a= 0.0003
    shift= int(0.049*data.shape[0])
    length = a*data.shape[0]/sample_rate
    N = int(a*data.shape[0])
    time = np.linspace(0., length, N)
    return time, sample_rate, data[shift:N+ shift,:], N

def star_finches():
    sample_rate, data = read("Audio/StarFinch.wav")
    a= 0.008
    shift= int(0.2*data.shape[0])
    length = a*data.shape[0]/sample_rate
    N = int(a*data.shape[0])
    time = np.linspace(0., length, N)
    return time, sample_rate, data[shift:N+ shift,:], N

def nightingale():
    sample_rate, data = read("Audio/nightingale.wav")
    a = 0.0028
    shift = int(0.034*data.shape[0])
    length = a * data.shape[0] / sample_rate
    N = int(a * data.shape[0])
    time = np.linspace(0., length, N)
    return time, sample_rate, data[shift:N + shift, :], N

# Play Sampled Bird Noise
# time, sample_rate, data, N = zebra_finches()
# data1=np.int16(data/np.max(np.abs(data)) * 32767)
# sd.play(data, sample_rate)
# write("Sampled_Bird_Syllables/zebra_finch.wav", sample_rate, data=data1)
#
# time, sample_rate, data, N = star_finches()
# sd.play(data, sample_rate)
# data1=np.int16(data/np.max(np.abs(data)) * 32767)
# write("Sampled_Bird_Syllables/star_finch.wav", sample_rate, data1)

time, sample_rate, data, N = nightingale()
sd.play(data, sample_rate)
data1=np.int16(data/np.max(np.abs(data)) * 32767)
write("Sampled_Bird_Syllables/nightingale_syllable.wav", sample_rate, data1)

#Plot Dual Channel sound data
fig=plt.figure(figsize=(8,4))
#plt.plot(time, data[:,0], label="Left channel", linewidth=0.2, alpha=0.5)
plt.plot(time,data[:,1], label="Right channel", linewidth=0.2)
plt.legend()
plt.title('Dual Channel Nightingale Syllable', fontsize=15)
plt.xlabel("Time [s]", fontsize=15)
plt.ylabel("Amplitude", fontsize=15)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.show()
#plt.savefig('strfnch.png')

# from scipy.signal import hilbert
# #generate the analytic signal from the bird syllabel
# dual = hilbert(data[:, 0], N=18000) #Use N=18000 for large time-series. Defeault otherwise
#
# wvd = WignerVilleDistribution(dual)
# wvd.run()
# wvd.plot(kind='contour', show_tf=True)
