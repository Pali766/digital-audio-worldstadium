import numpy as np
import matplotlib.pyplot as plt

class StadiumAudioSimulation:
    def __init__(self, num_speakers=10, stadium_radius=100):
        self.num_speakers = num_speakers
        self.stadium_radius = stadium_radius
        self.speakers = self._initialize_speakers()

    def _initialize_speakers(self):
        angles = np.linspace(0, 2 * np.pi, self.num_speakers, endpoint=False)
        speakers = [(np.cos(angle) * self.stadium_radius, np.sin(angle) * self.stadium_radius) for angle in angles]
        return speakers

    def simulate_audio(self, audio_signal):
        # Simulate the audio from the speakers
        print("Simulating audio in stadium...")
        total_sound = np.zeros(len(audio_signal))
        for speaker in self.speakers:
            # Each speaker can play the audio signal with some delay based on the distance
            distance = np.hypot(speaker[0], speaker[1])
            delay = int(distance / 343 * 44100)  # Speed of sound ~ 343 m/s
            delayed_signal = np.roll(audio_signal, delay)
            total_sound += delayed_signal / self.num_speakers
        return total_sound

if __name__ == '__main__':
    # Generate a simple audio signal (a sine wave)
    fs = 44100  # Sampling frequency
    t = np.linspace(0, 1, fs)
    frequency = 440  # A4 note
    audio_signal = np.sin(2 * np.pi * frequency * t)

    # Simulate the stadium audio
    stadium_simulator = StadiumAudioSimulation(num_speakers=10)
    stadium_audio = stadium_simulator.simulate_audio(audio_signal)

    # Plotting the outputs
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.title('Original Audio Signal')
    plt.plot(t, audio_signal)
    plt.subplot(2, 1, 2)
    plt.title('Stadium Audio Signal')
    plt.plot(t, stadium_audio)
    plt.xlabel('Time (s)')
    plt.tight_layout()
    plt.show()
