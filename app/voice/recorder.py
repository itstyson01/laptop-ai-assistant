import pyaudio
import wave
import numpy as np


SAMPLE_RATE = 16000
CHANNELS = 1
FORMAT = pyaudio.paInt16

OUTPUT_FILE = "recording.wav"

CHUNK = 1024

SILENCE_DURATION = 2.0
SILENCE_THRESHOLD = 500


def record_audio():

    print("🎤 Listening...")

    audio = pyaudio.PyAudio()

    sample_width = audio.get_sample_size(FORMAT)

    stream = audio.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=SAMPLE_RATE,
        input=True,
        frames_per_buffer=CHUNK,
    )

    frames = []

    started_speaking = False
    silence_chunks = 0

    required_silence_chunks = int(
        SILENCE_DURATION * SAMPLE_RATE / CHUNK
    )

    try:

        while True:

            data = stream.read(
                CHUNK,
                exception_on_overflow=False
            )

            frames.append(data)

            audio_array = np.frombuffer(
                data,
                dtype=np.int16
            )

            volume = np.sqrt(
                np.mean(audio_array.astype(np.float32) ** 2)
            )

            if not started_speaking:

                if volume > SILENCE_THRESHOLD:

                    started_speaking = True

                    silence_chunks = 0

                    print("🗣️ Speech detected...")

                continue

            if volume < SILENCE_THRESHOLD:

                silence_chunks += 1

            else:

                silence_chunks = 0

            if silence_chunks >= required_silence_chunks:

                break

    finally:

        stream.stop_stream()
        stream.close()
        audio.terminate()

    audio_bytes = b"".join(frames)

    with wave.open(OUTPUT_FILE, "wb") as wf:

        wf.setnchannels(CHANNELS)
        wf.setsampwidth(sample_width)
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(audio_bytes)

    print("✅ Recording complete")
    print(f"💾 Audio saved to: {OUTPUT_FILE}")

    return np.frombuffer(
        audio_bytes,
        dtype=np.int16
    ).reshape(-1, 1)