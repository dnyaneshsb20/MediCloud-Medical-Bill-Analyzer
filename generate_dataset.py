import pandas as pd
import random
from faker import Faker

fake = Faker()

# Fixed choices
doctors = ["Dr. Sharma", "Dr. Mehta", "Dr. Khan", "Dr. Reddy", "Dr. Patel"]
symptoms_list = ["Fever", "Cough", "Headache", "Stomach Pain", "Chest Pain", "Back Pain", "Cold", "Fatigue"]
medicines_list = ["Paracetamol", "Ibuprofen", "Amoxicillin", "Cough Syrup", "Vitamin D", "Antacid"]

# Generate dataset
records = []
for i in range(100):  # 100 patients
    patient_id = i + 1
    name = fake.name()
    age = random.randint(10, 80)
    gender = random.choice(["Male", "Female"])
    doctor = random.choice(doctors)
    symptom = random.choice(symptoms_list)
    medicines = ", ".join(random.sample(medicines_list, random.randint(1, 3)))
    consultation_fee = random.choice([200, 300, 400, 500])
    medicine_cost = random.randint(100, 500)
    total_bill = consultation_fee + medicine_cost
    email = fake.email()

    records.append([
        patient_id, name, age, gender, doctor, symptom,
        medicines, consultation_fee, medicine_cost, total_bill, email
    ])

# Create DataFrame
df = pd.DataFrame(records, columns=[
    "PatientID", "Name", "Age", "Gender", "Doctor",
    "Symptom", "Medicines", "ConsultationFee",
    "MedicineCost", "TotalBill", "Email"
])

# Save dataset
df.to_csv("medical_billing_dataset.csv", index=False)
print("✅ Dataset generated and saved as medical_billing_dataset.csv")
print(df.head())
