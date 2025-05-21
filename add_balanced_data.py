"""
Script to add more data with balanced graduation years to the MongoDB collections.
This script will add alumni data with a balanced distribution of graduation years
to make the dashboard visualizations look better.
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
    "Leadership", "Problem Solving", "Critical Thinking", "Teamwork", "Time Management",
    "Marketing", "Sales", "Finance", "Accounting", "Human Resources", "Customer Service",
    "Public Speaking", "Writing", "Research", "Design", "UX/UI", "Mobile Development",
    "DevOps", "Cybersecurity", "Networking", "Database Management", "Big Data"
]

EMPLOYMENT_STATUSES = [
    "Employed Full-Time", "Employed Part-Time", "Self-Employed", "Freelance", 
    "Unemployed", "Pursuing Higher Education", "Internship", "Contract Work"
]

INDUSTRIES = [
    "Technology", "Healthcare", "Finance", "Education", "Manufacturing", "Retail",
    "Government", "Non-Profit", "Entertainment", "Media", "Consulting", "Energy",
    "Transportation", "Construction", "Real Estate", "Hospitality", "Agriculture"
]

COMPANY_TYPES = [
    "Startup", "Small Business", "Medium Enterprise", "Large Corporation", 
    "Multinational", "Government Agency", "Non-Profit Organization", "Educational Institution"
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

def generate_alumni_with_balanced_years(count=300):
    """Generate alumni data with balanced graduation years."""
    alumni_data = []
    current_year = datetime.datetime.now().year
    
    # Create a balanced distribution of graduation years (last 10 years)
    graduation_years = list(range(current_year - 10, current_year))
    
    # Allocate alumni per year (more recent years have slightly more alumni)
    alumni_per_year = {}
    total_allocated = 0
    
    # Allocate alumni with a slight bias towards more recent years
    for year in graduation_years:
        # Calculate weight based on recency (more recent = higher weight)
        recency_weight = (year - (current_year - 10)) / 10  # 0.0 to 0.9
        # Base allocation plus recency bonus
        allocation = int(count / len(graduation_years) * (1 + recency_weight * 0.5))
        alumni_per_year[year] = allocation
        total_allocated += allocation
    
    # Adjust to match the requested count
    if total_allocated != count:
        diff = count - total_allocated
        # Distribute the difference across years
        for year in sorted(graduation_years, reverse=True):
            if diff > 0:
                alumni_per_year[year] += 1
                diff -= 1
            elif diff < 0:
                if alumni_per_year[year] > 1:  # Ensure at least 1 alumni per year
                    alumni_per_year[year] -= 1
                    diff += 1
            if diff == 0:
                break
    
    logger.info(f"Alumni distribution by graduation year:")
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
            skills_list = random.sample(SKILLS, num_skills)
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
        
        # Generate and insert alumni data with balanced graduation years
        alumni_data = generate_alumni_with_balanced_years(count=300)
        if alumni_data:
            result = db.alumni.insert_many(alumni_data)
            logger.info(f"Added {len(result.inserted_ids)} alumni records with balanced graduation years")
        
        # Close MongoDB connection
        client.close()
        logger.info("MongoDB connection closed")
        logger.info("Data generation completed successfully")
        
    except Exception as e:
        logger.error(f"Error in main function: {str(e)}")

if __name__ == "__main__":
    main()
