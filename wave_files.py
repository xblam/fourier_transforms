import numpy as np
from scipy.io import wavfile
from scipy.fft import fft
import matplotlib.pyplot as plt
import pprint as pprint

class AutoTranscriber:
    def __init__(self, sound_sample, sampling_rate, time_axis):

        self.time_axis = time_axis
        self.sampling_rate = sampling_rate
        self.sound_sample = sound_sample
        fft_result = np.fft.fft(sound_sample)
        fft_magnitude = np.abs(fft_result)
        fft_frequencies = np.fft.fftfreq(len(fft_result), d=1/sampling_rate)

        # positive freqs are the freqs that we can break it down into
        self.positive_freqs = fft_frequencies[:len(fft_frequencies)//2]

        # this is just how much they impact on the overall sound
        self.positive_magnitude = fft_magnitude[:len(fft_result)//2]

        # make the note ranges
        self.note_ranges = self.generate_piano_note_ranges()

    
    # tells me which note this frequency is
    def map_frequency_to_note(freq, note_ranges):
        # midi notes match up with the freq range calculated earlier
        for midi, (low, high) in note_ranges.items():
            if low <= freq < high:
                return midi
        return None # outside of range


    # gives the ranges we will assign notes to
    def generate_piano_note_ranges(self):
        note_ranges = {}
        for midi in range(21, 109):  # MIDI numbers for A0 to C8
            lower_bound = 440.0 * (2 ** ((midi - 69 - 0.5) / 12.0))  # Half step below
            upper_bound = 440.0 * (2 ** ((midi - 69 + 0.5) / 12.0))  # Half step above
            note_ranges[midi] = (lower_bound, upper_bound)
        return note_ranges
    

    def transcribe_to_notes(self, segment_duration=0.1, threshold=0.01):
        """
        Transcribe audio into notes with loudness based on frequency magnitudes.
        Args:
            segment_duration (float): Duration of each segment in seconds.
            threshold (float): Minimum magnitude to consider a frequency.
        Returns:
            List of dicts: [{time: segment_time, notes: [(note_name, magnitude), ...]}, ...]
        """
        notes_by_time = []
        segment_length = int(segment_duration * self.sampling_rate)  # Samples per segment
        total_segments = len(self.sound_sample) // segment_length

        for i in range(total_segments):
            # Extract segment
            start_idx = i * segment_length
            end_idx = start_idx + segment_length
            segment = self.sound_sample[start_idx:end_idx]

            # Perform FFT on the segment
            fft_result = np.fft.fft(segment)
            fft_magnitude = np.abs(fft_result)
            fft_frequencies = np.fft.fftfreq(len(fft_result), d=1/self.sampling_rate)

            # Focus on positive frequencies
            positive_freqs = fft_frequencies[:len(fft_frequencies)//2]
            positive_magnitude = fft_magnitude[:len(fft_result)//2]

            # Aggregate magnitudes by note
            note_magnitudes = {midi: 0 for midi in self.note_ranges.keys()}
            for freq, mag in zip(positive_freqs, positive_magnitude):
                if mag > threshold:
                    midi = self.map_frequency_to_note(freq)
                    if midi is not None:
                        note_magnitudes[midi] += mag

            # Convert to note names and filter out quiet notes
            notes = [
                hwy is this calle dmag and what does this have to do with the rest of the code not working
                (self.midi_to_note_name(midi), mag)
                for midi, mag in note_magnitudes.items() if mag > 0
            ]

            # Store results
            notes_by_time.append({"time": i * segment_duration, "notes": notes})

        return notes_by_time




    def plot_audio(self):
        plt.figure(figsize=(10, 4))
        plt.plot(self.time_axis, s1, color='blue')
        plt.title(f"waves from {start_time} to {end_time} seconds")
        plt.xlabel("time (seconds)")
        plt.ylabel("amplitude")
        plt.grid()
        plt.show()


    def plot_freqs(self):
        # plot the Frequency Spectrum
        plt.figure(figsize=(10, 4))
        plt.plot(self.positive_freqs, self.positive_magnitude, color='red')
        plt.title(f"Frequency Spectrum (5-6 Seconds)")
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Magnitude")
        plt.grid()
        plt.show() 


    
    
@staticmethod
def midi_to_note_name(midi_number):
    """
    Convert a MIDI number to a piano note name.
    """
    NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    octave = (midi_number // 12) - 1
    note = NOTE_NAMES[midi_number % 12]
    return f"{note}{octave}"
       
if __name__ == '__main__':
    file_path = "e_er.wav"  # wave file path
    sampling_rate, data = wavfile.read(file_path)

    # set the start and end times
    start_time = 5
    end_time = 6
    start_sample = int(start_time * sampling_rate)
    end_sample = int(end_time * sampling_rate)
    s1 = data[start_sample:end_sample]
    time_axis = np.linspace(start_time, end_time, len(s1))
    
    bens_notes = AutoTranscriber(s1, sampling_rate, time_axis)

    bens_notes.plot_freqs()
    bens_notes.plot_audio()

    # Transcribe the audio into notes
    notes = bens_notes.transcribe_to_notes(segment_duration=0.1, threshold=0.01)

    # # Display the results
    # for segment in notes:
    #     print(f"Time: {segment['time']:.2f}s")
    #     for note, mag in segment['notes']:
    #         print(f"  Note: {note}, Magnitude: {mag:.2f}")
