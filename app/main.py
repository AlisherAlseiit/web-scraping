import time

from bs4 import BeautifulSoup
import requests


my_skills = 'python'


def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    job_cards = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(job_cards):
        job_published_date = job.find('span', class_='sim-posted')
        published_text = job_published_date.find('span').text

        if 'few' in published_text:
            job_company = job.find('h3', class_='joblist-comp-name').text.strip()
            job_skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']

            if my_skills in job_skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    
                    f.write(f'Company Name: {job_company.strip()} \n')
                    f.write(f'Required_skills: {job_skills.strip()} \n')
                    f.write(f'link: {more_info}')
                
                print(f'File saved: {index}')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} seconds.")
        time.sleep(time_wait * 60)

