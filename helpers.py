from faker import Faker

fake = Faker(locale="ru_RU")

def random_courier_login():
    # login = fake.text(max_nb_chars=10) + str(fake.random_int(0, 999))
    login = fake.text()
    return login

def random_courier_password():
    password = fake.password(length=10, upper_case=True, lower_case=True)
    return password

def random_courier_firstname():
    first_name = fake.first_name()
    return first_name