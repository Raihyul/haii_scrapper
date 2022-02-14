from haii_contents import *
from bs4 import BeautifulSoup
from urllib import parse, request

DOWNLOAD_IMAGE_DIRECTORY = "../frontend/src/assets/images/"
IMAGE_DIRECTORY = "../../assets/images/"


##### MAIN #####
# Advisory image
def get_advisory_image():
    advisory_soup = BeautifulSoup(main_advisory_kor, "html.parser")
    advisory_images = advisory_soup.find_all("img")
    num = 1
    for image in advisory_images:
        request.urlretrieve("https://" + parse.quote(image["src"][8:]), f"{DOWNLOAD_IMAGE_DIRECTORY}1. Main/3. Collaboration/2. Advisory/advisory-{num}-{image['alt']}.{image['src'].split('.')[-1]}")
        num += 1 


##### NEWS #####
# News image
def get_news_image():
    news_soup = BeautifulSoup(news, "html.parser")
    news_images = news_soup.find_all("img")
    num = 0
    for image in news_images:
        request.urlretrieve("https://" + parse.quote(image["src"][8:]), f"{DOWNLOAD_IMAGE_DIRECTORY}/5. News/news-{len(news_images) - num}.{image['src'].split('.')[-1]}")
        num += 1


##### PARTNERS #####
# Investors Image
def get_investors_image():
    investors_soup = BeautifulSoup(partners_investors_kor, "html.parser")
    investors_images = investors_soup.find_all("img")
    num = 1
    for image in investors_images:
        request.urlretrieve("https://" + parse.quote(image["src"][8:]), f"{DOWNLOAD_IMAGE_DIRECTORY}/6. Partners/investors-{num}-{image['alt']}.{image['src'].split('.')[-1]}")
        num += 1

# Partners Image
def get_partners_image():
    partners_soup = BeautifulSoup(partners_partners_kor, "html.parser")
    partners_images = partners_soup.find_all("img")
    num = 1
    for image in partners_images:
        request.urlretrieve("https://" + parse.quote(image["src"][8:]), f"{DOWNLOAD_IMAGE_DIRECTORY}/6. Partners/partners-{num}-{image['alt']}.{image['src'].split('.')[-1]}")
        num += 1


##### GALLERY #####
# Photo image
def get_photo_image():
    photo_soup = BeautifulSoup(gallery_photo, "html.parser")
    photo_images = photo_soup.find_all("img")
    num = 0
    for image in photo_images:
        request.urlretrieve("https://" + parse.quote(image["src"][8:]), f"{DOWNLOAD_IMAGE_DIRECTORY}/7. Gallery/gallery-{len(photo_images) - num}.{image['src'].split('.')[-1]}")
        num += 1


##### MEMBERS #####
# Members image
def get_members_image():
    members_soup = BeautifulSoup(members_kor, "html.parser")
    members_images = members_soup.find_all("img")
    num = 0
    for image in members_images:
        request.urlretrieve("https://" + parse.quote(image["src"][8:]), f"{DOWNLOAD_IMAGE_DIRECTORY}/8. Members/member-{len(members_images) - num}-{image['alt']}.{image['src'].split('.')[-1]}")
        num += 1