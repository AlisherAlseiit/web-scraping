py -3 -m venv venv  <--- creates virtual environment for the project

don't forget to select correct python select interpreter 

venv\Scripts\activate.bat <------ to use virtual environment in terminal

pip install beautifulsoup4

pip install lxml




scraping html file
--------------------------------------------------------------------------------
soup.find_all('h5') < --- finds all h5 tags


with open('home.html', 'r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(f'{course_name} costs {course_price}')

--------------------------------------------------------------------------------------

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
job_cards = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job in job_cards:
    job_published_date = job.find('span', class_='sim-posted')
    published_text = job_published_date.find('span').text

    if 'few' in published_text:
        job_company = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
        job_skills = job.find('span', class_='srp-skills').text.replace(' ', '')

        print(f'''
        Company Name: {job_company},
        Required Skills: {job_skills},
        ''')

--------------------------------------------------------------------------------------------



