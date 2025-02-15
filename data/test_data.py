class CourierCredentials:
    no_login_courier = {"password": "qwerty2", "firstName": "bessameMucho"}
    no_password_courier = {"login": "qwerty2", "firstName": "bessameMucho"}
    empty_login_courier = {"login": "qwerty1", "password": "", "firstName": "bessameMucho"}
    empty_password_courier = {"login": "", "password": "qwerty1", "firstName": "bessameMucho"}

    test_courier = {"login": "qwerty1ytrewq", "password": "opa_password_style", "firstName": "bessameMucho"}
    test_courier_wrong_password = {"login": "qwerty1ytrewq", "password": "WRONG"}
    test_courier_wrong_login = {"login": "WRONG", "password": "opa_password_style"}
    test_courier_no_password = {"login": "qwerty1ytrewq", "password": ""}
    test_courier_no_login = {"password": "opa_password_style"}


class ScooterOrderData:
    scooter_order = {
        "firstName": "Vanya",
        "lastName": "Helsing",
        "address": "Castle, 2 bashnya, left window",
        "metroStation": 5,
        "phone": "+7 880 055 55 55",
        "rentTime": 5,
        "deliveryDate": "2025-06-06",
        "comment": "I'll outrun Dracula",
        "color": [
            "BLACK"
        ]
    }


class ErrorMessage:
    no_login_or_pass_message = "Недостаточно данных для входа"
    wrong_login_pass_message = "Учетная запись не найдена"
