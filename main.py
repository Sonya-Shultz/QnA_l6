from selenium import webdriver
import time


def open_chrome():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/")
    assert driver.title == "YouTube"

    elem = driver.find_element_by_xpath("//input[@id=\"search\"]")
    elem.send_keys("rikroll")
    driver.find_element_by_xpath("//button[@id=\"search-icon-legacy\"]").click()
    assert ("No results found" not in driver.page_source) and ("Результатов не найдено" not in driver.page_source)

    # час на завантажити сторінку
    time.sleep(5)
    driver.find_element_by_xpath("//div[@id=\"contents\"]/ytd-item-section-renderer/div/ytd-video-renderer[1]" +
                                 "/div/ytd-thumbnail/a/yt-img-shadow/img").click()
    # час на пропустити рекламу
    time.sleep(30)
    assert driver.current_url == "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

    header = driver.find_element_by_css_selector("h1.title > yt-formatted-string").text
    assert "Rick Astley - Never Gonna Give You Up" in header
    driver.close()


if __name__ == '__main__':
    open_chrome()
