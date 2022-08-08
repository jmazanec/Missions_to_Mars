#!/usr/bin/env python
# coding: utf-8

# In[53]:


import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
import requests
import os
import time
from webdriver_manager.chrome import ChromeDriverManager


# NASA News - Mars

# In[54]:


#Creation of executable path to create connection

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
#create url
url = 'https://redplanetscience.com/'
browser.visit(url)
#make holder for html
html = browser.html
#brew soup with parser function
soup = BeautifulSoup(html, 'html.parser')


# In[56]:


print(soup.prettify())


# In[57]:


results = soup.find('div', class_='content_title')
titlesnews = results.text
print(titlesnews)


# In[58]:


results = soup.find('div', class_="article_teaser_body")
newsparagraph = results.text
print(newsparagraph)


# In[59]:


browser.quit()


# JPL Mars Space Images—Featured Image

# In[60]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
#create url
url = 'https://spaceimages-mars.com/'
browser.visit(url)
#make holder for html
html = browser.html
#brew soup with parser function
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())


# In[61]:


#Pull image featured in header
results = soup.find('img', class_="headerimage")
featured_image_url = f"{url}{results['src']}"
print(featured_image_url)


# In[62]:


browser.quit()


# Mars Facts

# In[63]:


url = "https://galaxyfacts-mars.com/"


# In[64]:


df = pd.read_html(url)
#tables


# In[65]:


#Select table and rename columns
mars_table_df = df[1] 
mars_table_df.columns = ["Description", "Info"]
mars_table_df


# In[66]:


#Set Description column as the index
mars_table_df.set_index('Description', inplace=True)
mars_table_df


# In[67]:


#convert data into the html table string
mars_html_table = mars_table_df.to_html()
mars_html_table = mars_html_table.replace("\n", "")
mars_html_table


# In[68]:


browser.quit()


# Mars Hemispheres

# In[86]:


#create executable path
executable_path = {'executable_path': ChromeDriverManager().install()}

browser = Browser('chrome', **executable_path, headless=False)
#create url
url_hemi = 'https://marshemispheres.com/'
#visit site
browser.visit(url_hemi)
#brew soup with parser function
soup_hemi = BeautifulSoup(browser.html, 'html.parser')

print(soup_hemi.prettify())


# In[92]:


#create empty set
herberto = []
#go to the html and find all tags that are h3
title = soup_hemi.find_all('h3')
#print findings
title


# In[93]:


#remove last title which is not a hemisphere
title = title[:-1]


# In[94]:


#present list of titles
for t in title:
    herberto.append(t.text)
    
herberto


# In[95]:


#create empty set for imgs
imgs = []
count = 0
for herb in herberto:
    browser.find_by_css("img.thumb")[count].click()
    imgs.append(browser.find_by_css('img.wide-image')['src'])
    browser.back()
    count = count + 1

imgs


# In[96]:


hemi_img_url = []
counts = 0
for i in imgs:
    hemi_img_url.append({"title":herberto[counts],"img_url":imgs[counts]})
    counts = counts + 1

hemi_img_url


# In[97]:


browser.quit()


# In[ ]:




