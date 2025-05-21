"""
MongoDB Utilities for Alumni Management System

This module provides utilities for interacting with MongoDB for the Alumni Management System.

Author: Augment Agent
Date: 2025-05-21
"""

import os
import logging
import json
import numpy as np
import pandas as pd
from pymongo import MongoClient
from bson.binary import Binary
import pickle
import datetime

# Set up logging
logger = logging.getLogger(__name__)

# MongoDB connection string
MONGODB_URI = "mongodb+srv://dsilva:7DaXRzRoueTBa3a5@alumnimanagement.f10hpn9.mongodb.net/?retryWrites=true&w=majority&appName=AlumniManagement"

class MongoDBHandler:
    """Handler for MongoDB operations."""

    def __init__(self, connection_string=MONGODB_URI, db_name="alumni_management"):
        """
        Initialize the MongoDB handler.

        Args:
            connection_string: MongoDB connection string
            db_name: Name of the database
        """
        self.connection_string = connection_string
        self.db_name = db_name
        self.client = None
        self.db = None

        logger.info(f"MongoDB handler initialized for database: {db_name}")

    def connect(self):
        """
        Connect to MongoDB.

        Returns:
            MongoDB database object
        """
        try:
            self.client = MongoClient(self.connection_string)
            self.db = self.client[self.db_name]
            # Test the connection
            self.client.admin.command('ping')
            logger.info(f"Connected to MongoDB database: {self.db_name}")
            return self.db
        except Exception as e:
            logger.error(f"Error connecting to MongoDB: {str(e)}")
            raise

    def close(self):
        """Close the MongoDB connection."""
        if self.client:
            self.client.close()
            logger.info("MongoDB connection closed")

    def save_model_metadata(self, model_name, model_type, accuracy, precision, recall, f1, parameters, timestamp=None):
        """
        Save model metadata to MongoDB.

        Args:
            model_name: Name of the model
            model_type: Type of the model (e.g., random_forest, xgboost)
            accuracy: Model accuracy
            precision: Model precision
            recall: Model recall
            f1: Model F1 score
            parameters: Model parameters
            timestamp: Timestamp of the model training

        Returns:
            ID of the inserted document
        """
        if not self.db:
            self.connect()

        collection = self.db["model_metadata"]

        if timestamp is None:
            timestamp = datetime.datetime.now()

        metadata = {
            "model_name": model_name,
            "model_type": model_type,
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1": f1,
            "parameters": parameters,
            "timestamp": timestamp
        }

        try:
            result = collection.insert_one(metadata)
            logger.info(f"Model metadata saved to MongoDB with ID: {result.inserted_id}")
            return result.inserted_id
        except Exception as e:
            logger.error(f"Error saving model metadata to MongoDB: {str(e)}")
            raise

    def save_model_binary(self, model_id, model_object, preprocessor=None, label_encoder=None):
        """
        Save model binary data to MongoDB.

        Args:
            model_id: ID of the model metadata document
            model_object: Trained model object
            preprocessor: Preprocessor object
            label_encoder: Label encoder object

        Returns:
            ID of the inserted document
        """
        if not self.db:
            self.connect()

        collection = self.db["model_binaries"]

        # Serialize model objects
        model_binary = Binary(pickle.dumps(model_object, protocol=4))

        binary_data = {
            "model_id": model_id,
            "model_binary": model_binary,
            "timestamp": datetime.datetime.now()
        }

        if preprocessor is not None:
            binary_data["preprocessor"] = Binary(pickle.dumps(preprocessor, protocol=4))

        if label_encoder is not None:
            binary_data["label_encoder"] = Binary(pickle.dumps(label_encoder, protocol=4))

        try:
            result = collection.insert_one(binary_data)
            logger.info(f"Model binary data saved to MongoDB with ID: {result.inserted_id}")
            return result.inserted_id
        except Exception as e:
            logger.error(f"Error saving model binary data to MongoDB: {str(e)}")
            raise

    def save_feature_importance(self, model_id, feature_importance_df):
        """
        Save feature importance data to MongoDB.

        Args:
            model_id: ID of the model metadata document
            feature_importance_df: DataFrame with feature importance data

        Returns:
            ID of the inserted document
        """
        if not self.db:
            self.connect()

        collection = self.db["feature_importance"]

        # Convert DataFrame to list of dictionaries
        feature_importance_data = feature_importance_df.to_dict(orient="records")

        document = {
            "model_id": model_id,
            "feature_importance": feature_importance_data,
            "timestamp": datetime.datetime.now()
        }

        try:
            result = collection.insert_one(document)
            logger.info(f"Feature importance data saved to MongoDB with ID: {result.inserted_id}")
            return result.inserted_id
        except Exception as e:
            logger.error(f"Error saving feature importance data to MongoDB: {str(e)}")
            raise

    def save_confusion_matrix(self, model_id, confusion_matrix, class_names):
        """
        Save confusion matrix data to MongoDB.

        Args:
            model_id: ID of the model metadata document
            confusion_matrix: Confusion matrix as a numpy array
            class_names: Names of the classes

        Returns:
            ID of the inserted document
        """
        if not self.db:
            self.connect()

        collection = self.db["confusion_matrices"]

        # Convert numpy array to list
        cm_data = confusion_matrix.tolist()

        document = {
            "model_id": model_id,
            "confusion_matrix": cm_data,
            "class_names": class_names,
            "timestamp": datetime.datetime.now()
        }

        try:
            result = collection.insert_one(document)
            logger.info(f"Confusion matrix data saved to MongoDB with ID: {result.inserted_id}")
            return result.inserted_id
        except Exception as e:
            logger.error(f"Error saving confusion matrix data to MongoDB: {str(e)}")
            raise

    def save_classification_report(self, model_id, classification_report):
        """
        Save classification report data to MongoDB.

        Args:
            model_id: ID of the model metadata document
            classification_report: Classification report as a dictionary

        Returns:
            ID of the inserted document
        """
        if not self.db:
            self.connect()

        collection = self.db["classification_reports"]

        document = {
            "model_id": model_id,
            "classification_report": classification_report,
            "timestamp": datetime.datetime.now()
        }

        try:
            result = collection.insert_one(document)
            logger.info(f"Classification report data saved to MongoDB with ID: {result.inserted_id}")
            return result.inserted_id
        except Exception as e:
            logger.error(f"Error saving classification report data to MongoDB: {str(e)}")
            raise

    def save_predictions(self, model_id, predictions_df):
        """
        Save prediction results to MongoDB.

        Args:
            model_id: ID of the model metadata document
            predictions_df: DataFrame with prediction results

        Returns:
            ID of the inserted document
        """
        if not self.db:
            self.connect()

        collection = self.db["predictions"]

        # Convert DataFrame to list of dictionaries
        predictions_data = predictions_df.to_dict(orient="records")

        document = {
            "model_id": model_id,
            "predictions": predictions_data,
            "timestamp": datetime.datetime.now()
        }

        try:
            result = collection.insert_one(document)
            logger.info(f"Prediction results saved to MongoDB with ID: {result.inserted_id}")
            return result.inserted_id
        except Exception as e:
            logger.error(f"Error saving prediction results to MongoDB: {str(e)}")
            raise
