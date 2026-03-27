import requests
from bs4 import BeautifulSoup
import pandas as pd
# Fetch Page
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
print(page.status_code)

#Parse Data
soup = BeautifulSoup(page.content,'html.parser')
results = soup.find(id="ResultsContainer")
#Get the html tags and Extract actual text
job_elements=soup.find_all("div", class_="card-content")

job_titles_list=[]
#Extract specific piece of info and store it in a list
for job in job_elements:
    job_title= job.find("h2",class_='title is-5').text.strip() if job.find("h2",class_='title is-5') else "N/A"
    company_name=job.find("h3",class_='subtitle is-6 company').text.strip() if job.find("h3",class_='subtitle is-6 company') else "N/A"
    job_titles_list.append({"Job Title":job_title,
                            "Company Name":company_name})

#Convert list into DataFrame and save as CSV
df= pd.DataFrame(job_titles_list)
df.to_csv('job_titles.csv', index=False)

    
