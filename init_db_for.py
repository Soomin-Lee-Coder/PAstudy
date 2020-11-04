import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

for i in range(1, 100):
    data = requests.get('https://www.coursera.org/search?query=people%20analytics&page=' + str(i) + '&index=prod_all_products_term_optimization', headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    programs = soup.select('#rendered-content > div > div > div.rc-SearchPage > div.ais-InstantSearch__root > div > div.rc-SearchTabs > div.ais-MultiIndex__root > div.tab-contents > div > div > div > ul > li')

    for program in programs:
        h_tag = program.select_one('div > a > div > div > div.card-content.horizontal-box > div.card-info.vertical-box > h2')
        if h_tag is not None:
            source = program.select_one('div > a > div > div > div.card-content.horizontal-box > div.card-info.vertical-box > div.partner-logo-wrapper.horizontal-box > span').text
            title = h_tag.text
            program_type = program.select_one('div > a > div > div > div.card-content.horizontal-box > div.card-info.vertical-box > div:nth-child(3) > div').text
            star = program.select_one('div > a > div > div > div.rc-ProductInfo > div.rating-enroll-wrapper > div:nth-child(1) > div > span.ratings-text').text
            student = program.select_one(' div > a > div > div > div.rc-ProductInfo > div.rating-enroll-wrapper > div.enrollment.info-item > span > span').text
            program_info = {
                'source': source,
                'title': title,
                'program_type': program_type,
                'star': star,
                'student':student
            }
            print(program_info)
            db.programs.insert_one(program_info)

    programs = soup.select('#course > li:nth-child(1) > div > dl > dt')
    for program in programs:
        h_tag = program.select_one('div > a > div > div > div.card-content.horizontal-box > div.card-info.vertical-box > h2')
        if h_tag is not None:
            source = program.select_one('div > a > div > div > div.card-content.horizontal-box > div.card-info.vertical-box > div.partner-logo-wrapper.horizontal-box > span').text
            title = h_tag.text
            program_type = program.select_one('div > a > div > div > div.card-content.horizontal-box > div.card-info.vertical-box > div:nth-child(3) > div').text
            star = program.select_one('div > a > div > div > div.rc-ProductInfo > div.rating-enroll-wrapper > div:nth-child(1) > div > span.ratings-text').text
            student = program.select_one(' div > a > div > div > div.rc-ProductInfo > div.rating-enroll-wrapper > div.enrollment.info-item > span > span').text
            program_info = {
                'source': source,
                'title': title,
                'program_type': program_type,
                'star': star,
                'student':student
            }
            print(program_info)
            db.programs.insert_one(program_info)