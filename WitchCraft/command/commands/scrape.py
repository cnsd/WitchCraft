import config.config as config
from config.config import *


'''
scrape(url, rtype = ScrapeType.forum, rtarget = ScrapeTarget.titles, headers = {}, verify = False)

A function to scrape data off pages.

Input: url to scrape,
     type (forum[1] or thread[2]),
     target(titles[1], common opener[2], comments[3], common replier[4]),
     headers as dictionary to pass with the url,
     optional SSL Verification flag (Default: False to get rid of SSL errors)

     Defaults:
        + Request type = 1 (Forum)
        + ScrapeTarget = 1 (Titles)
        + Headers = none ({})
        + SSL Verification = False

Output: Depends on the type and the target,
    - Forum:
      + (Forum + Titles) RETURNS a list occupied by titles of the threads on the first page.
      + (Forum + common opener) RETURNS the name and profile url of the person who owns the highest amount of threads on the first page the forum.

    - Thread:
      + (Thread + comments) RETURNS a list occupied by all of the comments in a thread or only the first page.
      + (Thread + common replier) RETURNS the name and profile url of the person who owns the highest amount of comments on the first page of a thread.
'''
def scrape(args):
  #url, rtype = ScrapeType.forum, rtarget = ScrapeTarget.titles, headers = {}, verify = False
  if (rtype == ScrapeType.forum):
    if (rtarget == ScrapeTarget.titles):
      print 'Scraping titles on %s.' % url

    elif (rtarget == ScrapeTarget.common_opener):
      print 'Scraping common openers on %s.' % url


  elif (rtype == ScrapeType.thread):
    print 'y'

  else:
    print 'Error in the type'