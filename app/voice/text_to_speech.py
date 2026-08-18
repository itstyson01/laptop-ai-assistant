import edge_tts
import pygame


VOICE = "en-US-AriaNeural"


async def text_to_speech(text):
    communicate = edge_tts.Communicate(text, VOICE)

    await communicate.save("response.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("response.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pass

    pygame.mixer.quit()