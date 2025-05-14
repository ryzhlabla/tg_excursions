from aiogram.types import FSInputFile
# ---------- Точка 0: Приветственный текст ----------
from app.step1_intro.step_start import txt1 as text_step0

# ---------- Точка 1: Вступление ----------
from app.step1_intro.step1 import txt1 as text_step1

audio_step1 = FSInputFile("app/step1_intro/step1.mp3")
photo_step1_1 = FSInputFile("app/step1_intro/Munster,_Germany_1881.jpg")
#photo_step1_2 = FSInputFile("media/step1_intro/photo2.jpg")

# ---------- Точка 2: Музей Пикассо ----------
from app.step8_Picasso.step8 import txt1 as text_step8

#audio_step2 = FSInputFile("media/step2_picasso/audio1.mp3")
#photo_step2_1 = FSInputFile("media/step2_picasso/photo1.jpg")

# --- и так далее для остальных точек ---
