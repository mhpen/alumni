"""
Script to add alumni data with a dramatically unbalanced graduation year distribution.
This script will create a very uneven distribution of graduation years to make
the "Alumni by Graduation Year" chart more visually interesting.
"""

import pymongo
import random
import datetime
from bson import ObjectId
import logging
from faker import Faker

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize Faker for generating realistic data
fake = Faker()

# MongoDB connection string
MONGO_URI = "mongodb+srv://dsilva:7DaXRzRoueTBa3a5@alumnimanagement.f10hpn9.mongodb.net/?retryWrites=true&w=majority&appName=AlumniManagement"
DB_NAME = "alumni_management"

# Constants for data generation
DEGREE_PROGRAMS = [
    "Bachelor of Science in Computer Science",
    "Bachelor of Science in Information Technology",
    "Bachelor of Science in Business Administration",
    "Bachelor of Arts in Communication",
    "Bachelor of Science in Nursing",
    "Bachelor of Science in Civil Engineering",
    "Bachelor of Science in Mechanical Engineering",
    "Bachelor of Science in Electrical Engineering",
    "Bachelor of Arts in Psychology",
    "Bachelor of Science in Accounting"
]

MAJORS = [
    "Computer Science", "Information Technology", "Business Administration", 
    "Communication", "Nursing", "Civil Engineering", "Mechanical Engineering", 
    "Electrical Engineering", "Psychology", "Accounting", "Marketing", "Finance"
]

LOCATIONS = [
    "New York, NY", "Los Angeles, CA", "Chicago, IL", "Houston, TX", "Phoenix, AZ",
    "Philadelphia, PA", "San Antonio, TX", "San Diego, CA", "Dallas, TX", "San Jose, CA",
    "Austin, TX", "Jacksonville, FL", "Fort Worth, TX", "Columbus, OH", "Charlotte, NC"
]

SKILLS = [
    "Python", "Java", "JavaScript", "SQL", "Data Analysis", "Machine Learning", 
    "Web Development", "Cloud Computing", "Project Management", "Communication",
    "Leadership", "Problem Solving", "Critical Thinking", "Teamwork", "Time Management"
]

EMPLOYMENT_STATUSES = [
    "Employed Full-Time", "Employed Part-Time", "Self-Employed", "Freelance", 
    "Unemployed", "Pursuing Higher Education", "Internship", "Contract Work"
]

INDUSTRIES = [
    "Technology", "Healthcare", "Finance", "Education", "Manufacturing", "Retail",
    "Government", "Non-Profit", "Entertainment", "Media", "Consulting"
]

COMPANY_TYPES = [
    "Startup", "Small Business", "Medium Enterprise", "Large Corporation", 
    "Multinational", "Government Agency", "Non-Profit Organization"
]

SALARY_RANGES = [
    "$30,000 - $50,000", "$50,000 - $70,000", "$70,000 - $90,000", 
    "$90,000 - $110,000", "$110,000 - $130,000", "$130,000+"
]

def connect_to_mongodb():
    """Connect to MongoDB and return the database object."""
    try:
        client = pymongo.MongoClient(MONGO_URI)
        db = client[DB_NAME]
        logger.info(f"Connected to MongoDB: {DB_NAME}")
        return client, db
    except Exception as e:
        logger.error(f"Error connecting to MongoDB: {str(e)}")
        raise

def generate_alumni_with_dramatic_distribution(count=500):
    """Generate alumni data with a dramatically unbalanced distribution of graduation years."""
    alumni_data = []
    current_year = datetime.datetime.now().year
    
    # Create a range of graduation years (last 15 years)
    graduation_years = list(range(current_year - 15, current_year))
    
    # Create a dramatically unbalanced distribution
    # Define specific years with very high or very low counts
    
    # Define the distribution pattern (manually set for dramatic effect)
    distribution = {
        current_year - 15: 5,    # 2010: Very few
        current_year - 14: 8,    # 2011: Very few
        current_year - 13: 10,   # 2012: Very few
        current_year - 12: 15,   # 2013: Few
        current_year - 11: 20,   # 2014: Few
        current_year - 10: 80,   # 2015: Major spike (program expansion)
        current_year - 9: 30,    # 2016: Drop after spike
        current_year - 8: 25,    # 2017: Continued drop
        current_year - 7: 20,    # 2018: Low point
        current_year - 6: 35,    # 2019: Recovery
        current_year - 5: 60,    # 2020: Growth
        current_year - 4: 45,    # 2021: Slight drop (pandemic effect)
        current_year - 3: 30,    # 2022: Continued drop
        current_year - 2: 70,    # 2023: Major recovery
        current_year - 1: 120,   # 2024: Massive spike (current year)
    }
    
    # Adjust to match the requested count
    total = sum(distribution.values())
    scale_factor = count / total
    
    alumni_per_year = {year: max(1, int(count * distribution[year] / total)) for year in distribution}
    
    # Ensure the total matches the requested count
    total_allocated = sum(alumni_per_year.values())
    if total_allocated != count:
        diff = count - total_allocated
        # Distribute the difference to the years with the highest counts
        for year in sorted(alumni_per_year.keys(), key=lambda y: alumni_per_year[y], reverse=True):
            if diff > 0:
                alumni_per_year[year] += 1
                diff -= 1
            elif diff < 0:
                if alumni_per_year[year] > 1:  # Ensure at least 1 alumni per year
                    alumni_per_year[year] -= 1
                    diff += 1
            if diff == 0:
                break
    
    logger.info(f"Alumni distribution by graduation year (dramatically unbalanced):")
    for year, count in sorted(alumni_per_year.items()):
        logger.info(f"  {year}: {count} alumni")
    
    # Generate alumni data for each year
    for year, year_count in alumni_per_year.items():
        for _ in range(year_count):
            # Generate employment data
            employed_after_grad = random.choices(["Yes", "No"], weights=[0.85, 0.15])[0]
            
            if employed_after_grad == "Yes":
                time_to_employment = random.randint(1, 24)  # 1-24 months
            else:
                time_to_employment = None
                
            # Generate random skills (3-8 skills per alumni)
            num_skills = random.randint(3, 8)
            skills_list = random.sample(SKILLS, min(num_skills, len(SKILLS)))
            skills = ", ".join(skills_list)
            
            # Generate degree and major
            degree = random.choice(DEGREE_PROGRAMS)
            major = degree.split("in ")[-1] if "in " in degree else random.choice(MAJORS)
            
            # Generate employment data
            current_employment_status = random.choice(EMPLOYMENT_STATUSES)
            
            if current_employment_status in ["Employed Full-Time", "Employed Part-Time", "Self-Employed", "Freelance", "Contract Work"]:
                industry = random.choice(INDUSTRIES)
                company_type = random.choice(COMPANY_TYPES)
                salary_range = random.choice(SALARY_RANGES)
                job_title = fake.job()
                skills_used = ", ".join(random.sample(skills_list, min(len(skills_list), random.randint(2, 5))))
            else:
                industry = None
                company_type = None
                salary_range = None
                job_title = None
                skills_used = None
            
            alumni = {
                "name": fake.name(),
                "age": random.randint(22, 45),
                "gender": random.choice(["Male", "Female", "Non-binary", "Prefer not to say"]),
                "graduation_year": year,
                "degree": degree,
                "major": major,
                "gpa": round(random.uniform(2.5, 4.0), 2),
                "internship_experience": random.choice(["Yes", "No"]),
                "skills": skills,
                "location": random.choice(LOCATIONS),
                "employed_after_grad": employed_after_grad,
                "time_to_employment": time_to_employment,
                "current_employment_status": current_employment_status,
                "industry": industry,
                "company_type": company_type,
                "salary_range": salary_range,
                "job_title": job_title,
                "skills_used": skills_used,
                "email": fake.email(),
                "phone": fake.phone_number(),
                "linkedin_profile": f"linkedin.com/in/{fake.user_name()}",
                "communication_preference": random.choice(["Email", "Phone", "Both"]),
                "created_at": datetime.datetime.now(),
                "updated_at": datetime.datetime.now()
            }
            
            alumni_data.append(alumni)
    
    return alumni_data

def main():
    """Main function to add data to MongoDB collections."""
    try:
        # Connect to MongoDB
        client, db = connect_to_mongodb()
        
        # Check existing alumni count
        alumni_count = db.alumni.count_documents({})
        logger.info(f"Current alumni count: {alumni_count}")
        
        # Generate and insert alumni data with dramatically unbalanced distribution
        alumni_data = generate_alumni_with_dramatic_distribution(count=500)
        if alumni_data:
            result = db.alumni.insert_many(alumni_data)
            logger.info(f"Added {len(result.inserted_ids)} alumni records with dramatically unbalanced distribution")
        
        # Close MongoDB connection
        client.close()
        logger.info("MongoDB connection closed")
        logger.info("Data generation completed successfully")
        
    except Exception as e:
        logger.error(f"Error in main function: {str(e)}")

if __name__ == "__main__":
    main()
