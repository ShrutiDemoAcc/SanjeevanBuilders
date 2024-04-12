import json

import requests
import streamlit as st


# https://lottiefiles.com/animations/design-studio-kxgH964Ol6?from=search
"""
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
        """

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
#    return r.json()

st.title("Include lottie files in streamlit")
lottie_hello = load_lottieurl("https://lottie.host/a46f4eeb-7c99-4103-a113-d167cdc35621/tnjDpM1Eb7.lottie")
#lottie_h = load_lottieurl("https://lottie.host/adc52558-7b65-4306-a305-8fa44315d13b/A2Kc5CI8ci.json")

def st_lottie(lottie_coding, speed, reverse, loop, quality, rendered, height, width, key):
    pass


st_lottie(
        "lottie_coding",
        speed = 1,
        reverse=False,
        loop=True,
        quality="low",
        rendered="svg",
        height=None,
        width=None,
        key=None,

    )