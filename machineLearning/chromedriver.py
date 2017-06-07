import os, urllib, time, sys, requests
from selenium import webdriver

chromedriverpath = "/home/diginess/code/deeplearning/chromedriver"
browser = webdriver.Chrome(chromedriverpath)

#searchterm = "cat"
searchterm = sys.argv[1]

#Current search URL is unwieldy, check out this link for some ideas in order to break up the search options:
#https://stackoverflow.com/questions/18387598/selenium-webdriver-click-google-search
url = "https://www.google.com/search?q=" + searchterm + "&safe=on&espv=2&biw=1599&bih=726&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiI56_7isXSAhXC4iYKHcbZCLEQAUIBigB#q=" + searchterm + "&safe=off&tbm=isch&tbs=sur:fc&*"

browser.get(url)

#TO DO here:  Figure out how to time it or keep testing it so that the show more button is actually clicked.  
#Maybe a time.wait(1) would work...
for _ in range(30):
    browser.execute_script("window.scrollBy(0,10000)")
    time.sleep(.1)
    showmore = browser.find_elements_by_id('ksb_kvc')
    for button in showmore:
    	button.click()

images = browser.find_elements_by_class_name('rg_l')

if not os.path.exists("./images/" + searchterm):
    os.makedirs("./images/" + searchterm)

count = 1
for image in images:
    href = image.get_attribute('href')
    if '?imgurl=' in href:  # Do this because often times the last result will not be an actual image
        image_url_raw = href.split('?imgurl=')[1].split('&imgrefurl=')[0]
        image_url = urllib.unquote(urllib.unquote(image_url_raw))
        #image_url = requests.get(image_url_raw)
        #print image_url
        savePath = "./images/" + searchterm + "/" + "image" + str(count) + ".jpg"
        urllib.urlretrieve(image_url, savePath)
        count += 1
print count - 1

#Note:  In order to call this program from
#imageCoverter.py or the neural net code,
#use:
#os.system("chromedriver.py <arguments here>")
#The above will wait for the process to finish before
#continuing.  If you want to do threads, you can use
#the multiprocessing module: https://docs.python.org/3/library/subprocess.html#module-subprocess
#Can also import the other script:
#import script1
#script.myFunction(i)