"""
Script to add more data with a natural, unbalanced distribution to the MongoDB collections.
This script will add alumni data with a realistic distribution of graduation years
to make the dashboard visualizations look more natural and realistic.
"""

import pymongo
import random
import datetime
from bson import ObjectId
import logging
from faker import Faker
import numpy as np

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

def generate_alumni_with_natural_distribution(count=400):
    """Generate alumni data with a natural, unbalanced distribution of graduation years."""
    alumni_data = []
    current_year = datetime.datetime.now().year
    
    # Create a range of graduation years (last 15 years)
    graduation_years = list(range(current_year - 15, current_year))
    
    # Create a natural distribution with more recent years having more alumni
    # and some years having spikes or dips
    
    # Base weights - exponential growth towards recent years
    base_weights = [1.2 ** i for i in range(len(graduation_years))]
    
    # Add some random variation to create spikes and dips
    random_factors = []
    for i in range(len(graduation_years)):
        # Add random spikes for certain years (e.g., program expansions)
        if i % 4 == 0:  # Every 4 years, add a spike
            factor = random.uniform(1.2, 1.5)
        # Add random dips for certain years (e.g., economic downturns)
        elif i % 5 == 0:  # Every 5 years, add a dip
            factor = random.uniform(0.6, 0.8)
        else:
            factor = random.uniform(0.9, 1.1)  # Small random variation
        random_factors.append(factor)
    
    # Combine base weights with random factors
    weights = [base_weights[i] * random_factors[i] for i in range(len(graduation_years))]
    
    # Normalize weights to sum to 1
    total_weight = sum(weights)
    normalized_weights = [w / total_weight for w in weights]
    
    # Calculate alumni per year based on weights
    alumni_per_year = {}
    remaining_count = count
    
    for i, year in enumerate(graduation_years):
        if i < len(graduation_years) - 1:
            # Allocate based on weight, but ensure at least 1 alumni per year
            allocation = max(1, int(count * normalized_weights[i]))
            if allocation > remaining_count:
                allocation = remaining_count
            alumni_per_year[year] = allocation
            remaining_count -= allocation
        else:
            # Last year gets any remaining alumni
            alumni_per_year[year] = remaining_count
    
    logger.info(f"Alumni distribution by graduation year (natural, unbalanced):")
    for year, count in sorted(alumni_per_year.items()):
        logger.info(f"  {year}: {count} alumni")
    
    # Generate alumni data for each year
    for year, year_count in alumni_per_year.items():
        for _ in range(year_count):
            # Generate employment data
            # More recent graduates have lower employment rates
            if year >= current_year - 3:
                employed_after_grad = random.choices(["Yes", "No"], weights=[0.75, 0.25])[0]
            else:
                employed_after_grad = random.choices(["Yes", "No"], weights=[0.9, 0.1])[0]
            
            if employed_after_grad == "Yes":
                # More recent graduates have longer time to employment
                if year >= current_year - 3:
                    time_to_employment = random.randint(3, 24)  # 3-24 months
                else:
                    time_to_employment = random.randint(1, 12)  # 1-12 months
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
            # More recent graduates have different employment status distribution
            if year >= current_year - 3:
                weights = [0.6, 0.1, 0.05, 0.05, 0.1, 0.05, 0.03, 0.02]  # More unemployment, internships
            else:
                weights = [0.8, 0.05, 0.05, 0.05, 0.02, 0.01, 0.01, 0.01]  # More full-time employment
                
            current_employment_status = random.choices(EMPLOYMENT_STATUSES, weights=weights)[0]
            
            if current_employment_status in ["Employed Full-Time", "Employed Part-Time", "Self-Employed", "Freelance", "Contract Work"]:
                industry = random.choice(INDUSTRIES)
                company_type = random.choice(COMPANY_TYPES)
                
                # Salary ranges vary by graduation year (more experienced alumni earn more)
                years_since_graduation = current_year - year
                if years_since_graduation <= 2:
                    salary_weights = [0.5, 0.3, 0.15, 0.05, 0.0, 0.0]
                elif years_since_graduation <= 5:
                    salary_weights = [0.2, 0.4, 0.25, 0.1, 0.05, 0.0]
                elif years_since_graduation <= 10:
                    salary_weights = [0.05, 0.15, 0.3, 0.3, 0.15, 0.05]
                else:
                    salary_weights = [0.0, 0.05, 0.15, 0.3, 0.3, 0.2]
                    
                salary_range = random.choices(SALARY_RANGES, weights=salary_weights)[0]
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
        
        # Generate and insert alumni data with natural, unbalanced distribution
        alumni_data = generate_alumni_with_natural_distribution(count=400)
        if alumni_data:
            result = db.alumni.insert_many(alumni_data)
            logger.info(f"Added {len(result.inserted_ids)} alumni records with natural, unbalanced distribution")
        
        # Close MongoDB connection
        client.close()
        logger.info("MongoDB connection closed")
        logger.info("Data generation completed successfully")
        
    except Exception as e:
        logger.error(f"Error in main function: {str(e)}")

if __name__ == "__main__":
    main()
