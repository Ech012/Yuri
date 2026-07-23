import sounddevice as sd
from scipy.signal import resample
import numpy as np

TIME = 5
FREQ = 44100
WHISPER_FREQ = 16000


def record_voice():
    input("PLease Type anyting to strart the recording: ")
    record = sd.rec(int(TIME * FREQ), samplerate=FREQ, channels=1, dtype="float32")
    sd.wait()
    num_samples = int(len(record) * WHISPER_FREQ / FREQ)
    audio_resampled = resample(record.flatten(), num_samples)
    return audio_resampled.astype(np.float32)


