"""
Script to remove the balanced alumni data and replace it with a dramatically unbalanced distribution.
This script will:
1. Remove most of the existing alumni records to create an uneven distribution
2. Add new alumni with a dramatically unbalanced distribution
"""

import pymongo
import random
import datetime
import logging
from faker import Faker
from bson import ObjectId

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
    "Philadelphia, PA", "San Antonio, TX", "San Diego, CA", "Dallas, TX", "San Jose, CA"
]

SKILLS = [
    "Python", "Java", "JavaScript", "SQL", "Data Analysis", "Machine Learning", 
    "Web Development", "Cloud Computing", "Project Management", "Communication"
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

def remove_balanced_data(db):
    """Remove most of the existing alumni records to create an uneven distribution."""
    current_year = datetime.datetime.now().year
    years = list(range(current_year - 15, current_year))
    
    # Get current counts by year
    year_counts = {}
    for year in years:
        count = db.alumni.count_documents({"graduation_year": year})
        year_counts[year] = count
        logger.info(f"Current count for {year}: {count} alumni")
    
    # Define target counts for each year (dramatically unbalanced)
    target_counts = {
        current_year - 15: 10,    # 2010: Very few
        current_year - 14: 15,    # 2011: Very few
        current_year - 13: 20,    # 2012: Very few
        current_year - 12: 30,    # 2013: Few
        current_year - 11: 40,    # 2014: Few
        current_year - 10: 200,   # 2015: Major spike (program expansion)
        current_year - 9: 60,     # 2016: Drop after spike
        current_year - 8: 50,     # 2017: Continued drop
        current_year - 7: 40,     # 2018: Low point
        current_year - 6: 70,     # 2019: Recovery
        current_year - 5: 150,    # 2020: Growth
        current_year - 4: 100,    # 2021: Slight drop (pandemic effect)
        current_year - 3: 80,     # 2022: Continued drop
        current_year - 2: 180,    # 2023: Major recovery
        current_year - 1: 300,    # 2024: Massive spike (current year)
    }
    
    # For each year, remove or add records to match target counts
    for year in years:
        current_count = year_counts.get(year, 0)
        target_count = target_counts.get(year, 50)  # Default to 50 if not specified
        
        if current_count > target_count:
            # Remove excess records
            records_to_remove = current_count - target_count
            logger.info(f"Removing {records_to_remove} records from year {year}")
            
            # Find records to remove
            records = list(db.alumni.find({"graduation_year": year}, {"_id": 1}).limit(records_to_remove))
            record_ids = [record["_id"] for record in records]
            
            # Remove records
            if record_ids:
                result = db.alumni.delete_many({"_id": {"$in": record_ids}})
                logger.info(f"Removed {result.deleted_count} records from year {year}")
        
        elif current_count < target_count:
            # Need to add records - will be done in the next step
            logger.info(f"Need to add {target_count - current_count} records for year {year}")
    
    # Get updated counts
    updated_counts = {}
    for year in years:
        count = db.alumni.count_documents({"graduation_year": year})
        updated_counts[year] = count
    
    return updated_counts, target_counts

def generate_alumni_for_year(year, count):
    """Generate alumni data for a specific graduation year."""
    alumni_data = []
    current_year = datetime.datetime.now().year
    
    for _ in range(count):
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

def add_missing_alumni(db, current_counts, target_counts):
    """Add alumni records to reach target counts for each year."""
    alumni_to_add = []
    
    for year, target in target_counts.items():
        current = current_counts.get(year, 0)
        if current < target:
            # Need to add records
            count_to_add = target - current
            logger.info(f"Adding {count_to_add} records for year {year}")
            
            # Generate alumni for this year
            year_alumni = generate_alumni_for_year(year, count_to_add)
            alumni_to_add.extend(year_alumni)
    
    # Insert all new alumni
    if alumni_to_add:
        result = db.alumni.insert_many(alumni_to_add)
        logger.info(f"Added {len(result.inserted_ids)} alumni records")
    
    return len(alumni_to_add)

def main():
    """Main function to remove balanced data and add unbalanced data."""
    try:
        # Connect to MongoDB
        client, db = connect_to_mongodb()
        
        # Check existing alumni count
        total_alumni_before = db.alumni.count_documents({})
        logger.info(f"Total alumni count before: {total_alumni_before}")
        
        # Remove balanced data
        current_counts, target_counts = remove_balanced_data(db)
        
        # Add missing alumni to reach target counts
        added_count = add_missing_alumni(db, current_counts, target_counts)
        
        # Check final alumni count
        total_alumni_after = db.alumni.count_documents({})
        logger.info(f"Total alumni count after: {total_alumni_after}")
        logger.info(f"Net change: {total_alumni_after - total_alumni_before}")
        
        # Get final counts by year
        current_year = datetime.datetime.now().year
        years = list(range(current_year - 15, current_year))
        logger.info(f"Final alumni distribution by graduation year:")
        for year in sorted(years):
            count = db.alumni.count_documents({"graduation_year": year})
            logger.info(f"  {year}: {count} alumni")
        
        # Close MongoDB connection
        client.close()
        logger.info("MongoDB connection closed")
        logger.info("Data redistribution completed successfully")
        
    except Exception as e:
        logger.error(f"Error in main function: {str(e)}")

if __name__ == "__main__":
    main()
