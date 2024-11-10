class UserData:
    LOGIN = "Грозный"
    PASSWORD = "1530"
    FIRST_NAME = "Иван"
    COURIER_NO_LOGIN = {"login": "", "password": "1530", "first_name": "Иван"}
    COURIER_NO_PASSWORD = {"login": "Грозный", "password": "", "first_name": "Иван"}
    COURIER_VALID_DATA = {"login": "Грозный", "password": "1530", "first_name": "Иван"}

class OrderData:
     order_data_black = {
        "firstName": "Василий",
        "lastName": "III",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "1533-01-01",
        "comment": "Можно кататься",
        "color": [
            "BLACK"
        ]
    }

     order_data_grey = {
         "firstName": "Иван",
         "lastName": "III",
         "address": "Konoha, 142 apt.",
         "metroStation": 8,
         "phone": "+7 800 355 35 35",
         "rentTime": 10,
         "deliveryDate": "1505-06-06",
         "comment": "Тоже покатаюсь",
         "color": [
             "GREY"
         ]
     }

     order_data_two_colors = {
         "firstName": "Иван",
         "lastName": "Грозный",
         "address": "Konoha, 142 apt.",
         "metroStation": 8,
         "phone": "+7 800 355 35 35",
         "rentTime": 10,
         "deliveryDate": "1530-06-06",
         "comment": "Тоже покатаюсь",
         "color": [
             "GREY", "BLACK"
         ]
     }

     order_data_no_colors = {
         "firstName": "Борис",
         "lastName": "Годунов",
         "address": "Konoha, 142 apt.",
         "metroStation": 8,
         "phone": "+7 800 355 35 35",
         "rentTime": 10,
         "deliveryDate": "1605-06-06",
         "comment": "Тоже покатаюсь",
         "color": [
             " "
         ]
     }
