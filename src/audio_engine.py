import numpy as np
import scipy.signal
import matplotlib.pyplot as plt

class AudioSignalProcessor:
    def __init__(self, fs):
        self.fs = fs  # Sampling frequency

    def generate_sine_wave(self, frequency, duration):
        t = np.linspace(0, duration, int(self.fs * duration), endpoint=False)
        return t, np.sin(2 * np.pi * frequency * t)

    def apply_low_pass_filter(self, signal, cutoff_frequency):
        nyquist = 0.5 * self.fs
        normal_cutoff = cutoff_frequency / nyquist
        b, a = scipy.signal.butter(1, normal_cutoff, btype='low', analog=False)
        return scipy.signal.filtfilt(b, a, signal)

    def apply_high_pass_filter(self, signal, cutoff_frequency):
        nyquist = 0.5 * self.fs
        normal_cutoff = cutoff_frequency / nyquist
        b, a = scipy.signal.butter(1, normal_cutoff, btype='high', analog=False)
        return scipy.signal.filtfilt(b, a, signal)

    def apply_band_pass_filter(self, signal, low_cutoff, high_cutoff):
        nyquist = 0.5 * self.fs
        normal_cutoff = [low_cutoff / nyquist, high_cutoff / nyquist]
        b, a = scipy.signal.butter(1, normal_cutoff, btype='band', analog=False)
        return scipy.signal.filtfilt(b, a, signal)

    def plot_signal(self, t, signal, title='Signal'): 
        plt.figure(figsize=(10, 4))
        plt.plot(t, signal)
        plt.title(title)
        plt.xlabel('Time [s]')
        plt.ylabel('Amplitude')
        plt.grid()
        plt.show()  

# Example usage:
if __name__ == '__main__':
    fs = 44100  # Sampling frequency
    duration = 1.0  # seconds
    frequency = 440  # A4 note
    processor = AudioSignalProcessor(fs)
    t, signal = processor.generate_sine_wave(frequency, duration)
    filtered_signal = processor.apply_low_pass_filter(signal, 1000)  # Cut off at 1000 Hz
    processor.plot_signal(t, signal, 'Original Signal')
    processor.plot_signal(t, filtered_signal, 'Filtered Signal')
