import os
from selenium import webdriver

browser=webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

elements=browser.find_elements_by_class_name("form-control")
for element in elements:
    element.send_keys("popka")
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла

file_input=browser.find_element_by_css_selector("[type='file']")
file_input.send_keys(file_path)

button = browser.find_element_by_tag_name("button")
button.click()