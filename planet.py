from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import requests
from PIL import Image
from io import BytesIO
import random
import streamlit as st
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ECX

st.markdown("""
<style>
body {
    color: white !important;
    background-color: black !important;
}
.stApp {
    background-color: black !important;
}
</style>
    """, unsafe_allow_html=True)



class Imagery:
    def __init__(self, planetary_choice):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)

        self.planetary_choice = planetary_choice
        if planetary_choice == "KuiperBelt":
            self.kuiper_belt()
        elif planetary_choice == "Neptune":
            self.neptune()
        elif planetary_choice == "Jupiter":
            self.jupiter()
        elif planetary_choice == "the Sun":
            self.sun()
        elif planetary_choice == "Mars":
            self.mars()

        self.fetch_and_show_image()
        self.driver.quit()

    def kuiper_belt(self):
        self.driver.get("https://science.nasa.gov/gallery/kuiper-belt/")
        element = ECX.presence_of_element_located((By.CLASS_NAME, "hds-media"))
        WebDriverWait(self.driver, 10).until(element)

    def neptune(self):
        self.driver.get("https://science.nasa.gov/gallery/neptune/")
        element = ECX.presence_of_element_located((By.CLASS_NAME, "hds-media"))
        WebDriverWait(self.driver, 10).until(element)

    def jupiter(self):
        self.driver.get("https://science.nasa.gov/gallery/jupiter/")
        element = ECX.presence_of_element_located((By.CLASS_NAME, "hds-media"))
        WebDriverWait(self.driver, 10).until(element)

    def sun(self):
        self.driver.get("https://science.nasa.gov/gallery/the-sun/")
        element = ECX.presence_of_element_located((By.CLASS_NAME, "hds-media"))
        WebDriverWait(self.driver, 10).until(element)

    def mars(self):
        self.driver.get("https://science.nasa.gov/gallery/mars/")
        element = ECX.presence_of_element_located((By.CLASS_NAME, "hds-media"))
        WebDriverWait(self.driver, 10).until(element)


    def fetch_and_show_image(self):
        element = ECX.presence_of_element_located((By.CLASS_NAME, "hds-media")) 
        WebDriverWait(self.driver, 10).until(element)
        gallery = self.driver.find_elements(By.CLASS_NAME, 'hds-media')
        random_item = random.choice(gallery)
        image = random_item.find_element(By.TAG_NAME, 'img')
        image_src = image.get_attribute('src')

        response = requests.get(image_src)
        image_path = BytesIO(response.content)
        st.image(image_path, caption = f"Image of {self.planetary_choice} sourced from NASA's official gallery.", use_column_width=True)


def main():
    st.title("NASA Imagery")
    planetary_choice = st.selectbox("Choose a planetary:", ["KuiperBelt", "Neptune", "Jupiter", "the Sun", "Mars"])
    if st.button("Fetch Image"):
        Imagery(planetary_choice)

if __name__ == "__main__":
    main()