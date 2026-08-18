import edge_tts
import pygame


VOICE = "en-US-AriaNeural"
OUTPUT_FILE = "response.mp3"


async def text_to_speech(text):

    communicate = edge_tts.Communicate(text, VOICE)

    await communicate.save(OUTPUT_FILE)

    if not pygame.mixer.get_init():
        pygame.mixer.init()

    pygame.mixer.music.load(OUTPUT_FILE)
    pygame.mixer.music.play()


def stop_speaking():

    if pygame.mixer.get_init():

        pygame.mixer.music.stop()
        pygame.mixer.quit()