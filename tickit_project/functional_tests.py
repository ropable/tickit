from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8069/admin')

assert 'Django site admin' in browser.title
