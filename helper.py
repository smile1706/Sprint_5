from faker import Faker

fake = Faker()

def generate_registration_data():
    username = fake.name()
    email = fake.email()
    correct_password = fake.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return username, email, correct_password  # Возвращаем кортеж (email, correct_password)

def generate_incorrect_registration_data():
    username = fake.name()
    email = fake.email()
    incorrect_password = fake.password(length=5, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return username, email, incorrect_password  # Возвращаем кортеж (email, correct_password)