from fastapi import FastAPI
from faker import Faker
import random
from datetime import datetime, time

app = FastAPI()
fake = Faker()

# Extended disease list
diseases = [
    "Diabetes", "Hypertension", "Asthma", "Cancer", "COVID-19",
    "Tuberculosis", "Flu", "Kidney Disease", "Heart Disease", "Migraine",
    "Stroke", "Pneumonia", "Hepatitis", "Arthritis", "Alzheimer’s",
    "Parkinson’s", "Epilepsy", "Obesity", "Depression", "Anxiety"
]

def generate_patient():
    # Random gender
    gender = random.choice(["Male", "Female"])

    # Gender-specific name
    if gender == "Male":
        name = fake.first_name_male() + " " + fake.last_name()
    else:
        name = fake.first_name_female() + " " + fake.last_name()

    # Patient details
    age = random.randint(1, 90)
    disease = random.choice(diseases)

    # Today's date
    today = datetime.today().date().strftime("%Y-%m-%d")

    # Random time between 9 AM – 5 PM
    random_hour = random.randint(9, 17)
    random_minute = random.randint(0, 59)
    visit_time = time(random_hour, random_minute).strftime("%H:%M")

    # Patient contact details
    patient_email = fake.email()
    patient_phone = fake.phone_number()

    # Caretaker details
    caretaker = {
        "name": fake.name(),
        "email": fake.email(),
        "phone": fake.phone_number()
    }

    # Doctor info
    doctor = fake.name()

    return {
        "name": name,
        "gender": gender,
        "age": age,
        "disease": disease,
        "admission_date": today,
        "admission_time": visit_time,
        "doctor": doctor,
        "address": fake.address(),
        "email": patient_email,
        "phone": patient_phone,
        "caretaker": caretaker
    }

@app.get("/")
def root():
    return generate_patient()
