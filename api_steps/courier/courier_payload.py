from faker import Faker

fake = Faker()
class CourierPayloads:
    registration_data = {
            "login": fake.pystr(max_chars=11).strip(),
            "password": fake.pystr(max_chars=11).strip(),
            "firstName": fake.pystr(max_chars=11).strip()
        }
    registration_data_without_password = {
            "login": fake.pystr(max_chars=11).strip(),
            "firstName": fake.pystr(max_chars=11).strip()
        }
    registration_data_without_firstName = {
        "login": fake.pystr(max_chars=11).strip(),
        "password": fake.pystr(max_chars=11).strip()
    }
    login = {
    "login": "alenka12",
    "password": "1234"
    }
    login_without_password = {
        "login": "alenka12"
    }
    login_with_not_existed_user = {
    "login": "alenka12372183791283",
    "password": "1234"
    }
    login_incorrect_password = {
    "login": "alenka12",
    "password": "12344"
    }
    create_order = {...}