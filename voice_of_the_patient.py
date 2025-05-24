#STEP 1: SETUP AUDIO RECORDER (FFMPEG & PORTAUDIO)
import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


#STEP 2: SETUP SPEECH-TO-TECT STT MODEL FOR TRANSCRIPTION
