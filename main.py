import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Настройка прокси
proxy = "http://45.92.177.60:8080"
options = Options()
options.add_argument(f'--proxy-server={proxy}')

# Укажите путь к вашему chromedriver
chrome_driver_path = r'C:\WebDriver\bin\chromedriver.exe'  # Замените на фактический путь
service = Service(chrome_driver_path)

# Инициализация браузера
driver = webdriver.Chrome(service=service, options=options)

def download_video_review(url):
    driver.get(url)
    time.sleep(5)  # Ожидание загрузки страницы

    # Парсим HTML
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    video_tags = soup.find_all('video')

    for i, video in enumerate(video_tags):
        video_url = video.get('src')
        if video_url and "blob:" not in video_url:
            video_data = requests.get(video_url).content
            with open(f'video_review_{i}.mp4', 'wb') as video_file:
                video_file.write(video_data)
            print(f'Скачано видео {i+1}: video_review_{i}.mp4')
        else:
            print("Не удалось получить прямую ссылку на видео.")

def main():
    url = 'https://www.wildberries.ru/catalog/192186031/feedbacks?imtId=183532775&size=31'
    download_video_review(url)
    driver.quit()  # Закрытие браузера после завершения

if __name__ == "__main__":
    main()
