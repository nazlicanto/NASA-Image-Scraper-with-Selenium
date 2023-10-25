# NASA-Image-Scraper
### `NASA-Image-Scraper` is a Streamlit web application that provides users with random images of celestial bodies sourced from NASA's official gallery. The application employs the `Selenium` framework for web scraping and displays the fetched image using `Streamlit`. Deployed on AWS.

![sample imaj](https://github.com/nazlicanto/NASA-Image-Scraper/blob/main/imaj/merge.jpg)


## Features

### Selenium Webdriver: 
The application uses Selenium with Chrome Webdriver to navigate to NASA's gallery pages and scrape image data. The Chrome Webdriver operates in headless mode, so the browser is invisible during the scraping process due to servicing on Streamlit. 

### Streamlit: 
Streamlit provides an interactive web interface, allowing users to select a celestial body and view its image with ease.

### Explicit Waits (WebDriverWait): 
To ensure that page elements load fully before the scraper attempts to access them, explicit waits are implemented. The sleep times method is also applicable.


### PIL (Python Imaging Library): 
Once an image is scraped, it's processed using the PIL library to be displayed on the Streamlit application.