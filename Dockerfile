   FROM python:3.9

   # Copy the local code to the container
   COPY rest_api_app.py rest_api_app.py
   COPY random_forest_classifier.joblib random_forest_classifier.joblib

   RUN pip install pandas numpy scikit-learn matplotlib flask requests joblib

   # Expose the port the app runs on
   # EXPOSE 5000

   # Command to run the application
   CMD  ["python",  "rest_api_app.py"]