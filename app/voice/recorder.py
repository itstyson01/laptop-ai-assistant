import sounddevice as sd
import soundfile as sf


SAMPLE_RATE = 44100
RECORD_SECONDS = 5
OUTPUT_FILE = "recording.wav"


def record_audio():
    print("🎤 Listening...")

    audio = sd.rec(
        int(RECORD_SECONDS * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32",
    )

    sd.wait()

    print("✅ Recording complete")

    sf.write(
        OUTPUT_FILE,
        audio,
        SAMPLE_RATE,
    )

    print(f"💾 Audio saved to: {OUTPUT_FILE}")

    return audio

