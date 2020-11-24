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

def scrape_info():
    browser = init_browser()
    # define website and open in browser window
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup 
    html = browser.html
    soup = bs(html, 'html.parser')

    # Retrieve the parent divs for first page
    articles = soup.find_all(class_='list_text')

    # loop over results to get article data
    for article in articles:
        # scrape the article title
        news_title = article.find(class_='content_title').text
        # scrape the article paragraph
        news_p = article.find(class_='article_teaser_body').text
        # add articles into dictionary
        collection = {
            'Title': news_title,
            'Paragraph': news_p
        }
        
    # Close the browser after scraping
    browser.quit()
    return collection

def scrape_info2():
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