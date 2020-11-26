# import dependencies
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
import pandas as pd
from selenium import webdriver
import time

## NASA Mars News

# open browser window
def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

def scrape_all():
    articles_images ={}
    articles_images['article'] = scrape_article()
    articles_images['feature_image'] = scrape_feature_image()
    articles_images['cerberus'] = scrape_cerberus()
    articles_images['schiaparelli'] = scrape_schiaparelli()
    articles_images['syrtis_major'] = scrape_syrtis_major()
    articles_images['valles_marineris'] = scrape_valles_marineris()
    return articles_images

def scrape_article():
    browser = init_browser()
    # define website and open in browser window
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup 
    html = browser.html
    soup = bs(html, 'html.parser')

    # Retrieve the parent divs for first page
    articles1 = soup.find_all(class_='list_text')

    # loop over results to get article data
    for article in articles1:
        # scrape the article title
        news_title = article.find(class_='content_title').text
        # scrape the article paragraph
        news_p = article.find(class_='article_teaser_body').text
        # add articles into dictionary
        articles = {
            'Title': news_title,
            'Paragraph': news_p
        }
        
    # Close the browser after scraping
    browser.quit()
    return articles

def scrape_feature_image():
    browser = init_browser()
    # define website and open in browser window
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    # These are big pages to load so I'm giving some more time to make sure the whole page is loaded before continuing
    time.sleep(5)

    # get to the page with the image url
    browser.links.find_by_partial_text('FULL IMAGE').first.click()
    time.sleep(5)
    browser.links.find_by_partial_text('more info').first.click()
    time.sleep(5)

    # Scrape page into Soup 
    html = browser.html
    soup = bs(html, 'html.parser')

    # Identify and return the images
    results = soup.select_one('figure.lede a img').get('src')

    # Close the browser after scraping
    browser.quit()

    # store the image url
    images = {
        'feature_image_url': f'https://www.jpl.nasa.gov{results}'
    } 

    return images

def scrape_cerberus():
    browser = init_browser()
    # define website and open in browser window
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # time to load the page
    time.sleep(5)

    # get to the page with the image url
    browser.links.find_by_partial_text('Cerberus Hemisphere').first.click()

    # scrape page into Soup
    html = browser.html
    soup = bs(html, 'html.parser')
    
    # Identify and return the images
    results = soup.select_one('img.wide-image').get('src')

    # Close the browser after scraping
    browser.quit()

    # store the image url
    images = {
        'cerberus_image_url': f'https://astrogeology.usgs.gov{results}'
    } 

    return images

def scrape_schiaparelli():
    browser = init_browser()
    # define website and open in browser window
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # time to load the page
    time.sleep(5)

    # get to the page with the image url
    browser.links.find_by_partial_text('Schiaparelli Hemisphere').first.click()

    # scrape page into Soup
    html = browser.html
    soup = bs(html, 'html.parser')
    
    # Identify and return the images
    results = soup.select_one('img.wide-image').get('src')

    # Close the browser after scraping
    browser.quit()

    # store the image url
    images = {
        'schiaparelli_image_url': f'https://astrogeology.usgs.gov{results}'
    } 

    return images

def scrape_syrtis_major():
    browser = init_browser()
    # define website and open in browser window
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # time to load the page
    time.sleep(5)

    # get to the page with the image url
    browser.links.find_by_partial_text('Syrtis Major Hemisphere').first.click()

    # scrape page into Soup
    html = browser.html
    soup = bs(html, 'html.parser')
    
    # Identify and return the images
    results = soup.select_one('img.wide-image').get('src')

    # Close the browser after scraping
    browser.quit()

    # store the image url
    images = {
        'syrtis_major_image_url': f'https://astrogeology.usgs.gov{results}'
    } 

    return images

def scrape_valles_marineris():
    browser = init_browser()
    # define website and open in browser window
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # time to load the page
    time.sleep(5)

    # get to the page with the image url
    browser.links.find_by_partial_text('Valles Marineris Hemisphere').first.click()

    # scrape page into Soup
    html = browser.html
    soup = bs(html, 'html.parser')
    
    # Identify and return the images
    results = soup.select_one('img.wide-image').get('src')

    # Close the browser after scraping
    browser.quit()

    # store the image url
    images = {
        'valles_marineris_image_url': f'https://astrogeology.usgs.gov{results}'
    } 

    return images

