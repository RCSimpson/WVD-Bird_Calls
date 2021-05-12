import numpy as np
import sounddevice as sd
import time
from scipy.io.wavfile import read, write

zf_sample_rate, zf_data = read("zebra_finch.wav")
sf_sample_rate, sf_data = read("star_finch.wav")
syn_sample_rate, syn_data = read("synthbird.wav")
ng_sample_rate, ng_data = read("nightingale_syllable.wav")

sd.play(zf_data, zf_sample_rate)
time.sleep(3)

sd.play(sf_data, sf_sample_rate)
time.sleep(3)

sd.play(syn_data, syn_sample_rate)
time.sleep(3)

sd.play(ng_data, ng_sample_rate)
time.sleep(3)