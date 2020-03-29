import time, csv
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import datetime
import random
from selenium.webdriver.common.keys import Keys
import pandas as pd

driver = webdriver.Chrome()

driver.get("https://forums.edmunds.com/discussion/2864/general/x/entry-level-luxury-performance-sedans/")

comments = pd.DataFrame(columns = ['Date','user_id','comments'])
# user id
# userid_element = driver.find_elements_by_xpath('//*[@id="Comment_1726631"]/div/div[2]/div[1]/span[1]/a[2]')[0]
# userid = userid_element.text

#date
# date_element = driver.find_elements_by_xpath('//*[@id="Comment_1726631"]/div/div[2]/div[2]/span/a/time')[0]
# date = date_element.text

#comment
# comment_element = driver.find_elements_by_xpath('//*[@id="Comment_1726631"]/div/div[3]/div/div[1]')[0]
# comment = comment_element.text

ids = driver.find_elements_by_xpath("//*[contains(@id,'Comment_')]")
comment_ids = []
for i in ids:
    comment_ids.append(i.get_attribute('id'))
    # print(comment_ids)

for x in comment_ids:

    #Extract dates from for each user on a page
    user_date = driver.find_elements_by_xpath('//*[@id="' + x +'"]/div/div[2]/div[2]/span/a/time')[0]
    date = user_date.text

    #Extract user ids from each user on a page
    userid_element = driver.find_elements_by_xpath('//*[@id="' + x +'"]/div/div[2]/div[1]/span[1]/a[2]')[0]
    userid = userid_element.text

    #Extract Message for each user on a page
    user_message = driver.find_elements_by_xpath('//*[@id="' + x +'"]/div/div[3]/div/div[1]')[0]
    comment = user_message.text

    #Adding date, userid and comment for each user in a dataframe    
    comments.loc[len(comments)] = [date,userid,comment]

comments.to_csv('dataframe.csv')