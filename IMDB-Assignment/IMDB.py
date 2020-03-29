import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
chromeOptions.add_experimental_option("prefs", {"download.default_directory": "E:\DADV\IMDB-Assignment"})

# options = webdriver.ChromeOptions() 
# options.add_argument("download.default_directory=E:\DADV\IMDB-Assignment")
# driver = webdriver.Chrome(chrome_options=options)

driver = webdriver.Chrome(chrome_options = chromeOptions)

driver.get("https://www.imdb.com/interfaces/")
driver.maximize_window()
driver.find_element_by_partial_link_text("https://datasets.imdbws.com/").click()
time.sleep(4)
driver.find_element_by_partial_link_text("name.basics.tsv.gz").click()
time.sleep(4)
driver.find_element_by_partial_link_text("title.akas.tsv.gz").click()
time.sleep(4)
driver.find_element_by_partial_link_text("title.basics.tsv.gz").click()
time.sleep(4)
driver.find_element_by_partial_link_text("title.crew.tsv.gz").click()
time.sleep(4)
driver.find_element_by_partial_link_text("title.episode.tsv.gz").click()
time.sleep(4)
driver.find_element_by_partial_link_text("title.principals.tsv.gz").click()
time.sleep(4)
driver.find_element_by_partial_link_text("title.ratings.tsv.gz").click()
time.sleep(4)

# driver.close()