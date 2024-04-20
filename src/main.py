from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from login import login , loadCookies, saveCookies

words={}
tweetsids = []

def track_word_counts(word):
   if word in words.keys():
       words[word] += 1
   else:
       words[word] = 1

def twitter_scrapper (url,driver):
    # Set up the driver
    # Open the website
    driver = loadCookies(driver)
    driver.get(url)
    time.sleep(5)
    div_element = driver.find_element(By.XPATH, '//div[@data-testid="tweetText"]')
    content = div_element.text.replace('\n','').split(' ')
    div_element.click()
    tweeturl= driver.current_url
    time.sleep(1)
    tid = tweeturl.split('/')[-1]
    print(tid)
    if not tid in tweetsids:
        for word in content:
            if word.startswith('$') and not word[1].isdigit() :
                track_word_counts(word)
        tweetsids.append(tid) 
    return words,tweetsids        
accounts=[
        "https://twitter.com/Mr_Derivatives",
        "https://twitter.com/warrior_0719",
        "https://twitter.com/ChartingProdigy",
        "https://twitter.com/allstarcharts",
        "https://twitter.com/yuriymatso",
        "https://twitter.com/TriggerTrades",
        "https://twitter.com/AdamMancini4",
        "https://twitter.com/CordovaTrades",
        "https://twitter.com/Barchart",
        "https://twitter.com/RoyLMattox"
    ]
      
if __name__ == '__main__':
    word = input ("Enter the word you want to track: ")
    session_interval = input ("Enter the session interval in minuites: ")
    driver = webdriver.Firefox() 
    # while True: 
    try:
        for account in accounts:
            words,tweetsids= twitter_scrapper(account,driver)
        if word in words.keys():
            print(f"{word} appeared {words[word]} times in the last{session_interval}.")
        else:
            print(f"{word} did not appear in the last {session_interval}.")
    except Exception as e:
        print(e)
    # time.sleep(int(session_interval)*60)   