import openwakeword
from openwakeword.model import Model
import pyaudio
import numpy as np


def wait_for_wake_word():

    openwakeword.utils.download_models()

    model = Model()

    audio = pyaudio.PyAudio()

    stream = audio.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=16000,
        input=True,
        frames_per_buffer=1280
    )

    print("Listening for wake word...")

    while True:

        audio_data = stream.read(
            1280,
            exception_on_overflow=False
        )

        audio_array = np.frombuffer(
            audio_data,
            dtype=np.int16
        )

        prediction = model.predict(audio_array)

        for wake_word, score in prediction.items():

            if score > 0.5:
                print(f"Wake word detected: {wake_word}")

                stream.stop_stream()
                stream.close()
                audio.terminate()

                return True