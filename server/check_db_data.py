"""
Script to check the actual data in the MongoDB collections.
"""

import sys
import os
from pymongo import MongoClient
from dotenv import load_dotenv
import json
from bson import json_util

# Add the current directory to the path so we can import the src package
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Load environment variables
load_dotenv()

def check_db_data():
    """Check the actual data in the MongoDB collections."""
    try:
        print("Starting database data check...")
        
        # Connect to MongoDB
        mongo_uri = os.getenv('MONGODB_URI', 'mongodb+srv://dsilva:7DaXRzRoueTBa3a5@alumnimanagement.f10hpn9.mongodb.net/?retryWrites=true&w=majority&appName=AlumniManagement')
        db_name = os.getenv('DATABASE_NAME', 'alumni_management')
        
        print(f"Connecting to MongoDB at: {mongo_uri}")
        print(f"Using database: {db_name}")
        
        # Set a timeout for the connection
        client = MongoClient(mongo_uri, serverSelectionTimeoutMS=10000)
        
        # Force a connection to verify it works
        print("Checking connection...")
        client.server_info()
        
        print("Successfully connected to MongoDB")
        
        db = client[db_name]
        
        # Get list of collections
        collections = db.list_collection_names()
        print(f"Available collections: {collections}")
        
        # Check alumni collection
        if 'alumni' in collections:
            print("\nChecking alumni collection...")
            alumni_count = db.alumni.count_documents({})
            print(f"Total alumni count: {alumni_count}")
            
            # Check employment data
            employed_count = db.alumni.count_documents({"employed_after_grad": True})
            print(f"Employed after graduation count: {employed_count}")
            
            # Check employment status
            employment_status_pipeline = [
                {"$group": {"_id": "$employment_status", "count": {"$sum": 1}}},
                {"$sort": {"count": -1}}
            ]
            employment_status_results = list(db.alumni.aggregate(employment_status_pipeline))
            print("Employment status breakdown:")
            for result in employment_status_results:
                print(f"  {result['_id']}: {result['count']}")
            
            # Check graduation data
            graduated_count = db.alumni.count_documents({"graduated": True})
            print(f"Graduated count: {graduated_count}")
            
            # Check salary data
            salary_pipeline = [
                {"$match": {"salary": {"$exists": True, "$ne": None, "$gt": 0}}},
                {"$group": {"_id": None, "avg_salary": {"$avg": "$salary"}, "min_salary": {"$min": "$salary"}, "max_salary": {"$max": "$salary"}}}
            ]
            salary_results = list(db.alumni.aggregate(salary_pipeline))
            if salary_results:
                print(f"Salary statistics: {salary_results[0]}")
            else:
                print("No salary data found")
            
            # Check degree program distribution
            degree_pipeline = [
                {"$group": {"_id": "$degree_program", "count": {"$sum": 1}}},
                {"$sort": {"count": -1}}
            ]
            degree_results = list(db.alumni.aggregate(degree_pipeline))
            print("Degree program distribution:")
            for result in degree_results:
                print(f"  {result['_id']}: {result['count']}")
            
            # Check graduation year distribution
            year_pipeline = [
                {"$group": {"_id": "$graduation_year", "count": {"$sum": 1}}},
                {"$sort": {"_id": 1}}
            ]
            year_results = list(db.alumni.aggregate(year_pipeline))
            print("Graduation year distribution:")
            for result in year_results:
                print(f"  {result['_id']}: {result['count']}")
            
            # Check geographic distribution
            geo_pipeline = [
                {"$group": {"_id": "$location_type", "count": {"$sum": 1}}},
                {"$sort": {"count": -1}}
            ]
            geo_results = list(db.alumni.aggregate(geo_pipeline))
            print("Geographic distribution:")
            for result in geo_results:
                print(f"  {result['_id']}: {result['count']}")
        
        # Check event participation collection
        if 'eventParticipation' in collections:
            print("\nChecking eventParticipation collection...")
            event_count = db.eventParticipation.count_documents({})
            print(f"Total event participation count: {event_count}")
            
            # Check activity type distribution
            activity_pipeline = [
                {"$group": {"_id": "$activity_type", "count": {"$sum": 1}}},
                {"$sort": {"count": -1}}
            ]
            activity_results = list(db.eventParticipation.aggregate(activity_pipeline))
            print("Activity type distribution:")
            for result in activity_results:
                print(f"  {result['_id']}: {result['count']}")
        
        # Check feedback collection
        if 'feedback' in collections:
            print("\nChecking feedback collection...")
            feedback_count = db.feedback.count_documents({})
            print(f"Total feedback count: {feedback_count}")
            
            # Check service type distribution
            service_pipeline = [
                {"$group": {"_id": "$service_type", "count": {"$sum": 1}}},
                {"$sort": {"count": -1}}
            ]
            service_results = list(db.feedback.aggregate(service_pipeline))
            print("Service type distribution:")
            for result in service_results:
                print(f"  {result['_id']}: {result['count']}")
            
            # Check rating distribution for Career Support
            rating_pipeline = [
                {"$match": {"service_type": "Career Support"}},
                {"$group": {"_id": "$rating", "count": {"$sum": 1}}},
                {"$sort": {"_id": 1}}
            ]
            rating_results = list(db.feedback.aggregate(rating_pipeline))
            print("Career Support rating distribution:")
            for result in rating_results:
                print(f"  {result['_id']} Stars: {result['count']}")
        
        # Check programs collection
        if 'programs' in collections:
            print("\nChecking programs collection...")
            program_count = db.programs.count_documents({})
            print(f"Total programs count: {program_count}")
            
            # Check program participation
            program_pipeline = [
                {"$sort": {"participant_count": -1}}
            ]
            program_results = list(db.programs.find({}, {"_id": 0, "program_name": 1, "participant_count": 1}).sort("participant_count", -1))
            print("Program participation:")
            for result in program_results:
                print(f"  {result['program_name']}: {result['participant_count']}")
        
        # Check login logs collection
        if 'loginLogs' in collections:
            print("\nChecking loginLogs collection...")
            log_count = db.loginLogs.count_documents({})
            print(f"Total login logs count: {log_count}")
            
            # Check recent login logs
            recent_logs = list(db.loginLogs.find({}, {"_id": 0, "user": 1, "action": 1, "timestamp": 1}).sort("timestamp", -1).limit(5))
            print("Recent login logs:")
            for log in recent_logs:
                print(f"  {log}")
        
        client.close()
        print("\nMongoDB connection closed")
        
    except Exception as e:
        print(f"Error checking database data: {str(e)}")

if __name__ == "__main__":
    check_db_data()
    print("Script execution completed")
