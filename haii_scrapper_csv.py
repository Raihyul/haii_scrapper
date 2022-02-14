from haii_contents import *
from bs4 import BeautifulSoup
from urllib import parse, request
import csv

DOWNLOAD_IMAGE_DIRECTORY = "../frontend/src/assets/images/"
IMAGE_DIRECTORY = "../../assets/images/"

##### COMMON #####
# array data -> csv file
def to_csv(csv_name, data):
    with open(f"../frontend/public/{csv_name}.csv", "w", newline="", encoding="utf8") as f:
        wt = csv.writer(f)
        for each in data:
            wt.writerow(each)


##### MAIN #####
# Advisory info
def get_advisory_info(advisory):
    advisory_soup = BeautifulSoup(advisory, "html.parser")
    all_info = advisory_soup.find_all("div", {"class": "single-team"})
    advisory_info = []
    for info in all_info:
        try:
            name = info.find("h2").text
        except:
            name = info.find("h6").text
        affiliation = info.find("p").text
        image_type = info.find("img")["src"].split(".")[-1]
        advisory_info.append({"name": name, "affiliation": affiliation, "image_type": image_type})
    return advisory_info

def combine_advisory_info():
    advisory_info_kor = get_advisory_info(main_advisory_kor)
    advisory_info_eng = get_advisory_info(main_advisory_eng)
    total_advisory_info = [["name_kor", "name_eng", "affiliation_kor", "affiliation_eng", "image_directory"]]
    for i in range(len(advisory_info_kor)):
        name_kor = advisory_info_kor[i]["name"]
        name_eng = advisory_info_eng[i]["name"]
        affiliation_kor = advisory_info_kor[i]["affiliation"]
        affiliation_eng = advisory_info_eng[i]["affiliation"]
        image_directory = f"{IMAGE_DIRECTORY}1. Main/3. Collaboration/2. Advisory/advisory-{i+1}-{name_kor}.{advisory_info_kor[i]['image_type']}"
        total_advisory_info.append([name_kor, name_eng, affiliation_kor, affiliation_eng, image_directory])
    to_csv("main_advisory", total_advisory_info)


##### SCIENCE #####
# Publications info
def get_publications_info():
    publications_soup = BeautifulSoup(science_publications, "html.parser")
    all_info = publications_soup.find_all("div", {"class": "single-comments"})
    publications_info = [["people", "year", "first_content", "second_content"]]
    for info in all_info:
        people= info.find("h4").text
        year = info.find("span").text
        contents = info.find_all("p")
        if len(contents) == 1:
            first_content = contents[0].text
            second_content = ""
        else:
            first_content = contents[0].text
            second_content = contents[1].text
        publications_info.append([people, year, first_content, second_content])
    to_csv("publications", publications_info)


##### NEWS #####
# News info
def get_news_info():
    news_soup = BeautifulSoup(news, "html.parser")
    all_info = news_soup.find_all("div", {"class": "single-news"})
    news_info = [["thumbnail_url", "date", "url", "title", "content"]]
    num = 0
    for info in all_info:
        image_type = info.find("img")["src"].split(".")[-1]
        thumbnail_url = f"{IMAGE_DIRECTORY}5. News/news-{len(all_info) - num}.{image_type}"
        date = info.find("div", {"class": "date"}).text
        url = info.find("a")["href"]
        title = info.find("a").text
        content = info.find("p").text
        news_info.append([thumbnail_url,date, url, title, content])
        num += 1
    to_csv("news", news_info)


##### PARTNERS #####
# Investors info
def get_investors_info(investors):
    investors_soup = BeautifulSoup(investors, "html.parser")
    all_info = investors_soup.find_all("div", {"class": "single-news"})
    investors_info = []
    for info in all_info:
        try:
            name = info.find("h2").text
        except:
            name = info.find("h6").text
        image_type = info.find("img")["src"].split(".")[-1]
        investors_info.append({"name": name, "image_type": image_type})
    return investors_info

def combine_investors_info():
    investors_info_kor = get_investors_info(partners_investors_kor)
    investors_info_eng = get_investors_info(partners_investors_eng)
    total_investors_info = [["name_kor", "name_eng", "image_directory"]]
    for i in range(len(investors_info_kor)):
        name_kor = investors_info_kor[i]["name"]
        name_eng = investors_info_eng[i]["name"]
        image_directory = f"{IMAGE_DIRECTORY}6. Partners/investors-{i+1}-{name_kor}.{investors_info_kor[i]['image_type']}"
        total_investors_info.append([name_kor, name_eng, image_directory])
    to_csv("partners_investors", total_investors_info)

# Partners info
def get_partners_info(partners):
    partners_soup = BeautifulSoup(partners, "html.parser")
    all_info = partners_soup.find_all("div", {"class": "single-news"})
    partners_info = []
    for info in all_info:
        try:
            name = info.find("h2").text
        except:
            name = info.find("h6").text
        image_type = info.find("img")["src"].split(".")[-1]
        partners_info.append({"name": name, "image_type": image_type})
    return partners_info

def combine_partners_info():
    partners_info_kor = get_partners_info(partners_partners_kor)
    partners_info_eng = get_partners_info(partners_partners_eng)
    total_partners_info = [["name_kor", "name_eng", "image_directory"]]
    for i in range(len(partners_info_kor)):
        name_kor = partners_info_kor[i]["name"]
        name_eng = partners_info_eng[i]["name"]
        image_directory = f"{IMAGE_DIRECTORY}6. Partners/partners-{i+1}-{name_kor}.{partners_info_kor[i]['image_type']}"
        total_partners_info.append([name_kor, name_eng, image_directory])
    to_csv("partners_partners", total_partners_info)


##### GALLERY #####
# Video info
def get_video_info():
    video_soup = BeautifulSoup(gallery_video, "html.parser")
    all_info = video_soup.find_all("iframe")
    video_urls = [["video_url"]]
    for info in all_info:
        url = info["src"]
        video_urls.append([url])
    to_csv("gallery_video", video_urls)

# Photo info
def get_photo_info():
    photo_soup = BeautifulSoup(gallery_photo, "html.parser")
    all_info = photo_soup.find_all("div", {"class": "single-news"})
    # print(all_info)
    photo_info = [["image_directory", "title"]]
    num = 0
    for info in all_info:
        image_type = info.find("img")["src"].split(".")[-1]
        image_directory = f"{IMAGE_DIRECTORY}7. Gallery/gallery-{len(all_info) - num}.{image_type}"
        title = info.find("h2").text
        photo_info.append([image_directory, title])
        num += 1
    to_csv("gallery_photo", photo_info)


##### MEMBERS #####
# Members info
def get_members_info(members):
    members_soup = BeautifulSoup(members, "html.parser")
    all_info = members_soup.find_all("div", {"class": "single-news"})
    members_info = []
    for info in all_info:
        try:
            name = info.find("h2").text
        except:
            name = info.find("h6").text
        department = info.find("span").text
        introduction = info.find("pre").text
        image_type = info.find("img")["src"].split(".")[-1]
        members_info.append({"name": name, "department": department, "introduction": introduction, "image_type": image_type})
    return members_info

def combine_members_info():
    members_info_kor = get_members_info(members_kor)
    members_info_eng = get_members_info(members_eng)
    total_members_info = [["name_kor", "name_eng", "department_kor", "department_eng", "introduction_kor", "introduction_eng", "image_directory"]]
    for i in range(len(members_info_kor)):
        name_kor = members_info_kor[i]["name"]
        name_eng = members_info_eng[i]["name"]
        department_kor = members_info_kor[i]["department"]
        department_eng = members_info_eng[i]["department"]
        introduction_kor = members_info_kor[i]["introduction"]
        introduction_eng = members_info_eng[i]["introduction"]
        image_directory = f"{IMAGE_DIRECTORY}8. Members/members-{i+1}-{name_kor}.{members_info_kor[i]['image_type']}"
        total_members_info.append([name_kor, name_eng, department_kor, department_eng, introduction_kor, introduction_eng, image_directory])
    to_csv("members", total_members_info)
