"""
起動するときはF5ではなく
streamlit run my_streamit.py
"""

import streamlit as st
import cv2

def mosaic(img):
    h, w = img.shape[:2]
    img = cv2.resize(img, (w//10, h//10))
    img = cv2.resize(img, (w, h), interpolation = cv2.INTER_NEAREST)
    return img


def main():

    cap = cv2.VideoCapture(0)

    column1, column2 = st.columns(2)
    with column1:
        st.markdown("### origin")
        image1 = st.empty()

    with column2:
        st.markdown("### mosaic")
        image2 = st.empty()

    while True:
        ret, frame = cap.read()
        if ret:
            frame = frame[:, :, ::-1]   # BGR -> RGB
            image1.image(frame)
            image2.image(mosaic(frame))


if __name__ == "__main__":
    main()