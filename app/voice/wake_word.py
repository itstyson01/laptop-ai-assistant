import openwakeword
from openwakeword.model import Model
import pyaudio
import numpy as np


SAMPLE_RATE = 16000
CHUNK = 1280
WAKE_WORD_THRESHOLD = 0.3


openwakeword.utils.download_models()

model = Model()


def wait_for_wake_word():

    audio = pyaudio.PyAudio()

    stream = audio.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=SAMPLE_RATE,
        input=True,
        frames_per_buffer=CHUNK
    )

    print("Listening for wake word...")

    try:

        while True:

            audio_data = stream.read(
                CHUNK,
                exception_on_overflow=False
            )

            audio_array = np.frombuffer(
                audio_data,
                dtype=np.int16
            )

            prediction = model.predict(audio_array)

            for wake_word, score in prediction.items():

                if score > WAKE_WORD_THRESHOLD:

                    print(f"Wake word detected: {wake_word}")

                    return True

    finally:

        stream.stop_stream()
        stream.close()
        audio.terminate()


def listen_for_wake_word(stop_event, detected_event):

    audio = pyaudio.PyAudio()

    stream = audio.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=SAMPLE_RATE,
        input=True,
        frames_per_buffer=CHUNK
    )

    try:

        while not stop_event.is_set():

            audio_data = stream.read(
                CHUNK,
                exception_on_overflow=False
            )

            audio_array = np.frombuffer(
                audio_data,
                dtype=np.int16
            )

            prediction = model.predict(audio_array)

            for wake_word, score in prediction.items():

                if score > WAKE_WORD_THRESHOLD:

                    print(f"Wake word detected during TTS: {wake_word}")

                    detected_event.set()
                    stop_event.set()

                    return

    finally:

        stream.stop_stream()
        stream.close()
        audio.terminate()