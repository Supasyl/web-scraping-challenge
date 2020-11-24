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

## JPL Mars Space Images - Feature Image

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
    image_url = f'https://www.jpl.nasa.gov{results}'

    # Url to be inserted as a MongoDB document
    url = {
        'feature_image_url': image_url
    }
    
## Mars Facts

# In[73]:


url = 'https://space-facts.com/mars/'

# Use Panda's `read_html` to parse the url
tables = pd.read_html(url)
tables


# In[74]:


# extract the table containing facts about Mars
mars_fact_df = tables[0]
mars_fact_df


# In[75]:


# rename the columns
mars_fact_df = mars_fact_df.rename(columns={0: 'facts', 1: 'Mars_planet'})
mars_fact_df


# In[76]:


# export table to HTML format
Mars_table = mars_fact_df.to_html()
Mars_table


# # Mars Hemispheres

# ## Cerberus

# In[142]:


# open browser window
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[143]:


# define website and open in browser window
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[144]:



# get to the page with the image url
# another option:
# browser.find_by_css('h3')[0].click()
browser.links.find_by_partial_text('Cerberus Hemisphere').first.click()

html = browser.html
soup = bs(html, 'html.parser')
# Identify and return the images
results = soup.select_one('img.wide-image').get('src')
print(results)

# Close the browser after scraping
browser.quit()

# store the image url
image_url = f'https://astrogeology.usgs.gov{results}'

# Url to be inserted as a MongoDB document
post = {
    'cerberus_image_url': image_url
}
images.insert_one(post)


# ## Schiaparelli

# In[145]:


# open browser window
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[146]:


# define website and open in browser window
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[147]:


# get to the page with the image url
browser.links.find_by_partial_text('Schiaparelli Hemisphere').first.click()

html = browser.html
soup = bs(html, 'html.parser')
# Identify and return the images
results = soup.select_one('img.wide-image').get('src')
print(results)

# Close the browser after scraping
browser.quit()

# store the image url
image_url = f'https://astrogeology.usgs.gov{results}'

# Url to be inserted as a MongoDB document
post = {
    'schiaperelli_image_url': image_url
}
images.insert_one(post)


# ## Syrtis Major

# In[148]:


# open browser window
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[149]:


# define website and open in browser window
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[150]:


# get to the page with the image url
browser.links.find_by_partial_text('Syrtis Major Hemisphere').first.click()

html = browser.html
soup = bs(html, 'html.parser')
# Identify and return the images
results = soup.select_one('img.wide-image').get('src')
print(results)

# Close the browser after scraping
browser.quit()

# store the image url
image_url = f'https://astrogeology.usgs.gov{results}'

# Url to be inserted as a MongoDB document
post = {
    'syrtis_major_image_url': image_url
}
images.insert_one(post)


# ## Valles Marineris

# In[151]:


# open browser window
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[152]:


# define website and open in browser window
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[153]:


# get to the page with the image url
browser.links.find_by_partial_text('Valles Marineris Hemisphere').first.click()

html = browser.html
soup = bs(html, 'html.parser')
# Identify and return the images
results = soup.select_one('img.wide-image').get('src')
print(results)

# Close the browser after scraping
browser.quit()

# store the image url
image_url = f'https://astrogeology.usgs.gov{results}'

# Url to be inserted as a MongoDB document
post = {
    'valles_marineris_major_image_url': image_url
}
images.insert_one(post)


# In[ ]:




