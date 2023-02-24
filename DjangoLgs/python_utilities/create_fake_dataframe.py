import csv
import pandas as pd
from faker import Faker
import datetime
import random
from faker.providers import DynamicProvider

skill_provider = DynamicProvider(
     provider_name="skills",
     elements=["Python", "Pandas", "Linux", "SQL", "Data Mining"],
)


def fake_data_generation(records):
    fake = Faker('en_US')
    
    employee = []
    
    fake.add_provider(skill_provider)

    for i in range(records):
        first_name = fake.first_name()
        last_name = fake.last_name()



        employee.append({
                "First Name": first_name,
                "Last Name": last_name,
                "Birth Date" : fake.date(pattern="%Y-%m-%d", end_datetime=datetime.date(1995, 1,1)),
                "Email": str.lower(f"{first_name}.{last_name}@fake_domain-2.com"),
                "Hobby": fake.word(),
                "Experience" : random.randint(0,15),
                "Start Year": fake.year(),
                "Salary": random.randrange(75000,150000, 5000),
                "City" : fake.city(),
                "Nationality" : fake.country(),
                "Skill": fake.skills()
                })
        
    return employee


df = pd.DataFrame(fake_data_generation(50))
df.head()
print(df)

with open('fake.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['First Name', 'Hobby', 'Nationality', 'Bith Date'])
    for n in range(1, 100):
        writer.writerow(fake_data_generation())