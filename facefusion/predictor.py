import threading
import numpy
import opennsfw2
from PIL import Image
from keras import Model

from facefusion.typing import Frame

PREDICTOR = None
THREAD_LOCK = threading.Lock()
MAX_PROBABILITY = 0.75

# No change to this function since it's not directly checking anything.
def get_predictor() -> Model:
    global PREDICTOR

    with THREAD_LOCK:
        if PREDICTOR is None:
            PREDICTOR = opennsfw2.make_open_nsfw_model()
    return PREDICTOR

# No change to this function as well.
def clear_predictor() -> None:
    global PREDICTOR

    PREDICTOR = None

# Modified function to always return False.
def predict_frame(target_frame : Frame) -> bool:
    return False

# Modified function to always return False.
def predict_image(target_path : str) -> bool:
    return False

# Modified function to always return False.
def predict_video(target_path : str) -> bool:
    return False
