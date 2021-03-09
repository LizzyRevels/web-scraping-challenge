#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
from bs4 import BeautifulSoup
import requests
import os
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import pymongo
from flask import Flask, render_template


# Step 1 - Scraping
# 
# Hints
# *Use Splinter to navigate the sites when needed and BeautifulSoup to help find and parse out the necessary data.
# *Use Pymongo for CRUD applications for your database. For this homework, you can simply overwrite the existing document each time the /scrape url is visited and new data is obtained.
# *Use Bootstrap to structure your HTML template.

# NASA Mars News

# In[ ]:


# --Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. 

# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)


# In[ ]:


# Define database and collection
db = client.nasa_db
collection = db.news


# In[ ]:


# URL of page to be scraped
url = 'https://mars.nasa.gov/news/8875/testing-proves-its-worth-with-successful-mars-parachute-deployment/'

# Retrieve page with the requests module
response = requests.get(url)


# In[ ]:


# --Read HTML from file

# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')


# In[ ]:



# Retrieve the parent divs for all articles
results = soup.find_all('div', class_='grid_layout')

# loop over results to get article data
for result in results:
    
    # scrape the article header 
    news_title = result('h1', class_='article_title')
    
    # scrape the article paragraph 
    news_p = result.find('p')
    
   
    # print article data
    print('-----------------')
    print(news_title)
    print(news_p)
   
    
#     # Dictionary to be inserted into MongoDB
#     post = {
#         'news_title': news_title,
#         'news_p': news_p,
#     }

#     # Insert dictionary into MongoDB as a document
#     collection.insert_one(post)

# --Assign the text to variables that you can reference later.

# --Example:
# news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"
# news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast." -->


# JPL Mars Space Images - Featured Image

# In[ ]:


# Visit the url for JPL Featured Space Image here https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html.

# Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.

# Make sure to find the image url to the full size .jpg image.

# Make sure to save a complete url string for this image.

# Example:
# featured_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars2.jpg'


# In[ ]:


html_page = requests.get('https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html')
soup = BeautifulSoup(html_page.content, 'html.parser')
header = soup.find('div', class_="floating_text_area")
header 

# image = header.find('image/featured/mars1.jpg')
# link = header.find('a')
# href = link['href']
# print (href) 


# Not working, can't seem to grab the correct information


# Mars Facts

# In[ ]:


# Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
url = 'https://space-facts.com/mars/'
# Use Pandas to convert the data to a HTML table string.
tables = pd.read_html(url)
tables


# Mars Hemispheres

# In[ ]:


# Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
# You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
# Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. 

# -------------Cerberus Hemisphere---------------
# HTML object
html_page = requests.get('https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced')

# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html_page.content, 'html.parser')

# # Retrieve all elements that contain image information
images = soup.find('section', class_='block metadata')

h2 = images.find ('h2')
print(h2)

# scrape the article paragraph 
img_url = images.find('a')
print(img_url)

# -------------Schiaparelli Hemisphere---------------
# HTML object
html_page = requests.get('https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced')

# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html_page.content, 'html.parser')

# # Retrieve all elements that contain image information
images = soup.find('section', class_='block metadata')

h2 = images.find ('h2')
print(h2)

# scrape the article paragraph 
img_url = images.find('a')
print(img_url)

# -------------Syrtis Major Hemisphere---------------
# HTML object
html_page = requests.get('https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced')

# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html_page.content, 'html.parser')

# # Retrieve all elements that contain image information
images = soup.find('section', class_='block metadata')

h2 = images.find ('h2')
print(h2)

# scrape the article paragraph 
img_url = images.find('a')
print(img_url)

# -------------Valles Marineris Hemisphere---------------
# HTML object
html_page = requests.get('https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced')

# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html_page.content, 'html.parser')

# # Retrieve all elements that contain image information
images = soup.find('section', class_='block metadata')

h2 = images.find ('h2')
print(h2)

# scrape the article paragraph 
img_url = images.find('a')
print(img_url)



# Use a Python dictionary to store the data using the keys img_url and title.

# Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

# Example:
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif"},
    {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif"},
]


# Step 2 - MongoDB and Flask Application

# In[ ]:


# Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
# create instance of Flask app

# Start by converting your Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will 
# execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.

# Next, create a route called /scrape that will import your scrape_mars.py script and call your scrape function.

# Store the return value in Mongo as a Python dictionary.

# Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.

# Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate 
# HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.


# Step 3 - Submission
# 
# To submit your work to BootCampSpot, create a new GitHub repository and upload the following:
# 
# -The Jupyter Notebook containing the scraping code used.
# -Screenshots of your final application.
# -Submit the link to your new repository to BootCampSpot.
# -Ensure your repository has regular commits (i.e. 20+ commits) and a thorough README.md file
