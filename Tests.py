from YouTubePages import SearchStep
import time

def test_youtube_search(browser):
    page = SearchStep(browser)
    page.go_to()
    assert page.driver.title == "YouTube"
    page.enter_word("rickroll")
    page.click_on_the_search_button()
    assert ("No results found" not in page.driver.page_source)
    page.check_results()
    assert page.driver.current_url == "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    elements = page.find_name()
    assert elements == "Rick Astley - Never Gonna Give You Up (Video)"