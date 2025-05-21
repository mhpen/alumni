@echo off
echo Training all models and saving results to MongoDB...

REM Activate virtual environment if it exists
if exist "server\venv\Scripts\activate.bat" (
    call server\venv\Scripts\activate.bat
) else (
    echo Virtual environment not found. Make sure you have set up the environment.
    exit /b 1
)

REM Run the training script
python server\src\scripts\train_all_models_mongodb.py --career-train alumni-dataset\bsu_career_train.csv --career-test alumni-dataset\bsu_career_test.csv --employment-train alumni-dataset\bsu_career_train.csv --employment-test alumni-dataset\bsu_career_test.csv

REM Check if the script ran successfully
if %ERRORLEVEL% NEQ 0 (
    echo Training failed with error code %ERRORLEVEL%
    exit /b %ERRORLEVEL%
)

echo All models trained successfully and saved to MongoDB!
