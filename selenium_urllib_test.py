from selenium import webdriver
import time
"""options = webdriver.ChromeOptions()
options.add_argument('--headless')"""
driver = webdriver.Chrome()
print("Title:")
i = str(input())
driver.get('https://www.library.pref.gunma.jp/?action=pages_view_main&active_action=v3search_view_main_init&search_mode=detail&block_id=2870')
print(driver.title)
search_box = driver.find_element_by_name("title")
search_box.send_keys(i)
search_box.submit()
print(driver.title)
for i, g in enumerate(driver.find_elements_by_class_name("odd")):
    print("------ " + str(i+1) + " ------")
    r = g.find_element_by_class_name("sc_book_title_area")
    print(odd.find_element_by_tag_name("h3").text)  # タイトル
      # URL
    """s = g.find_element_by_class_name("s")
    print("\t" + s.find_element_by_class_name("st").text)  # サマリー"""
