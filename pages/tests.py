from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8069')

assert 'Hello, Django!' in browser.page_source
