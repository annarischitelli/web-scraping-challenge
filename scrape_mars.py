#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup


# ## Scrape for Mars News

executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

url = "https://mars.nasa.gov/news/"
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')
item = soup.find('li', class_='slide')


#Pulling headlines using 2/Activites/02
title = item.find('div', class_="content_title").find('a').text
paragraph = item.find('div', class_='rollover_description_inner').text
print(title,paragraph)

#Quit browser
browser.quit()


# ## Scrape for Mars Image 

executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars/"
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')

#Pulling image using 2/Activites/09
image_url = soup.find('article', class_='carousel_item').find('a', class_="button fancybox")['data-fancybox-href']
featured_image_url = url + image_url

#Return image URL
print(featured_image_url)

#Quit browser
browser.quit()


# ## Scrape for Mars Facts

url = "https://space-facts.com/mars/"

tables = pd.read_html(url)
tables

type(tables)

df = tables[0]
df.head()

#Dataframe to HTML
html_table = df.to_html()
html_table

df.to_html('table.html')

get_ipython().system('open table.html')


# ## Scrape Mars Hemispheres

#Find title and image URL to VALLES MARINERIS Hemisphere 
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

marineris_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
browser.visit(marineris_url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')

#Pull specific info for hemi
marineris_title  = soup.find('h2', class_='title').text
marineris_image_url = soup.find('div', class_='downloads').find('a')["href"]

#Title + Image together
print(marineris_title, marineris_image_url)

#Quit browser
browser.quit()


#Find title and image URL to Mars CEREBUS Hemisphere 
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

cerebus_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
browser.visit(cerebus_url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')

#Pull specific info for hemi
cerberus_title = soup.find('h2', class_='title').text
cerberus_image_url = soup.find('div', class_='downloads').find('a')["href"]

#Title + Image together
print(cerberus_title,cerberus_image_url)

#Quit browser
browser.quit()


#Find title and image URL to Mars SHIAPARELLI Hemisphere 
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

shiaparelli_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
browser.visit(shiaparelli_url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')

#Pull specific info for hemi
shiaparelli_title  = soup.find('h2', class_='title').text
shiaparelli_image_url = soup.find('div', class_='downloads').find('a')["href"]

#Title + Image together
print(shiaparelli_title, shiaparelli_image_url)

#Quit browser
browser.quit()


#Find title and image URL to Mars SYRTIS MAJOR Hemisphere 
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

syrtis_url = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
browser.visit(syrtis_url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')

#Pull specific info for hemi
syrtis_title  = soup.find('h2', class_='title').text
syrtis_image_url = soup.find('div', class_='downloads').find('a')["href"]

#Title + Image together
print(syrtis_title, syrtis_image_url)

#Quit browser
browser.quit()


#Example code
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": marineris_image_url},
    {"title": "Cerberus Hemisphere", "img_url": cerberus_image_url},
    {"title": "Schiaparelli Hemisphere", "img_url": shiaparelli_image_url},
    {"title": "Syrtis Major Hemisphere", "img_url": syrtis_image_url},
]
print(hemisphere_image_urls)

#Quit browser
browser.quit()

