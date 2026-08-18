import asyncio
import threading

import pygame

from ai.gemini import ask_gemini
from voice.speech_to_text import speech_to_text
from voice.text_to_speech import text_to_speech, stop_speaking
from voice.recorder import record_audio
from voice.wake_word import (
    wait_for_wake_word,
    listen_for_wake_word
)


def listen_for_interrupt():

    stop_event = threading.Event()
    detected_event = threading.Event()

    listener_thread = threading.Thread(
        target=listen_for_wake_word,
        args=(stop_event, detected_event),
        daemon=True
    )

    listener_thread.start()

    while pygame.mixer.music.get_busy():

        if detected_event.is_set():

            stop_speaking()

            break

    stop_event.set()

    listener_thread.join()


while True:

    # --------------------------------
    # Wait for wake word
    # --------------------------------

    wait_for_wake_word()

    print("Assistant activated!")

    # --------------------------------
    # Record command
    # --------------------------------

    audio = record_audio()

    print("Audio shape:", audio.shape)

    # --------------------------------
    # Speech → Text
    # --------------------------------

    speech_text = speech_to_text()

    print("You:", speech_text)

    # --------------------------------
    # Cancel command
    # --------------------------------

    if speech_text.lower().strip() in ["cancel", "stop"]:

        print("🛑 Command cancelled")

        continue

    # --------------------------------
    # Gemini
    # --------------------------------

    response = ask_gemini(
        prompt=speech_text
    )

    print("Gemini:", response)

    # --------------------------------
    # Text → Speech
    # --------------------------------

    asyncio.run(
        text_to_speech(response)
    )

    # --------------------------------
    # Listen for "Hey Jarvis"
    # while TTS is speaking
    # --------------------------------

    listen_for_interrupt()