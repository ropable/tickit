from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8069')

assert 'Climbing, shared.' in browser.page_source
