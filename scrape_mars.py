import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path":'/usr/local/bin/chromedriver'}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    mars_dict = {
        'title': " ",
        'paragraph': " ",
        'featured_image_url': " ",
        'html_table': " ",
        'marineris_title': " " , 
        'marineris_image_url': " ",
        'cerberus_title': " " , 
        'cerberus_image_url': " ",
        'shiaparelli_title': " " , 
        'shiaparelli_image_url': " ",
        'syrtis_title': " " , 
        'syrtis_image_url': " " 
    }
    titleparagraph = mars_titleparagraph()
    mars_dict['title'] = titleparagraph[0]
    mars_dict['paragraph'] = titleparagraph[1]
    mars_dict['featured_image_url'] = featured_image()
    marineris_titlemarineris_image_url = marineristitleimage()
    mars_dict['marineris_title'] = marineris_titlemarineris_image_url[0]
    mars_dict['marineris_image_url'] = marineris_titlemarineris_image_url[1]
    cerberus_titlecerberus_image_url = cerberustitleimage()
    mars_dict['cerberus_title'] = cerberus_titlecerberus_image_url[0]
    mars_dict['cerberus_image_url'] = cerberus_titlecerberus_image_url[1]
    shiaparelli_titleshiaparelli_image_url = shiaparellititleimage()
    mars_dict['shiaparelli_title'] = shiaparelli_titleshiaparelli_image_url[0]
    mars_dict['shiaparelli_image_url'] = shiaparelli_titleshiaparelli_image_url[1]
    syrtis_titlesyrtis_image_url = syrtistitleimage()
    mars_dict['syrtis_title'] = syrtis_titlesyrtis_image_url[0]
    mars_dict['syrtis_image_url'] = syrtis_titlesyrtis_image_url[1]
    return mars_dict

def mars_titleparagraph():
    browser = init_browser()
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    item = soup.find('li', class_='slide')
    title = item.find('div', class_="content_title").find('a').text
    paragraph = item.find('div', class_='rollover_description_inner').text
    browser.quit()
    return title, paragraph

def featured_image():
    browser = init_browser()
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image_url = soup.find('article', class_='carousel_item').find('a', class_="button fancybox")['data-fancybox-href']
    featured_image_url = 'https://www.jpl.nasa.gov' + image_url
    browser.quit()
    return featured_image_url

def marineristitleimage():
    browser = init_browser()
    marineris_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
    browser.visit(marineris_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    marineris_title  = soup.find('h2', class_='title').text
    marineris_image_url = soup.find('div', class_='downloads').find('a')["href"]
    browser.quit()
    return marineris_title, marineris_image_url

def cerberustitleimage():
    browser = init_browser()
    cerberus_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    browser.visit(cerberus_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    cerberus_title = soup.find('h2', class_='title').text
    cerberus_image_url = soup.find('div', class_='downloads').find('a')["href"]
    browser.quit()
    return cerberus_title, cerberus_image_url

def shiaparellititleimage():
    browser = init_browser()
    shiaparelli_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
    browser.visit(shiaparelli_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    shiaparelli_title  = soup.find('h2', class_='title').text
    shiaparelli_image_url = soup.find('div', class_='downloads').find('a')["href"]
    browser.quit()
    return shiaparelli_title, shiaparelli_image_url

def syrtistitleimage():
    browser = init_browser()
    syrtis_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
    browser.visit(syrtis_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    syrtis_title  = soup.find('h2', class_='title').text
    syrtis_image_url = soup.find('div', class_='downloads').find('a')["href"]
    browser.quit()
    return syrtis_title, syrtis_image_url