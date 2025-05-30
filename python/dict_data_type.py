user = {
    "name": "naga mahesh gatta",
    "age": 32,
    "email": "nagamaheshgatta@gmail.com",
    "is_active": True,
    "address": {
        "street": "Ramalayam veedhi",
        "location": "Hyderabad",
        "pincode": 524226,
        "state": "Telangana"
    }
}

print(user.get('phone'))

user['phone'] = "+91 9052932167"
print(user.get('phone'))

user.update({"address": {"street": "Ramalayam veedhi",
        "location": "Hyderabad",
        "pincode": 524226,
        "state": "Telangana","mandal": "Rangareddy"}})
print(user)


print(user.keys())
print(user.values())

print(user.items())

test_data = {
    "valid_user": {
        "username": "testuser",
        "password": "password123"
    },
    "invalid_user": {
        "username": "wronguser",
        "password": "wrongpass"
    }
}

print(test_data.get('valid_user'))
print(test_data.get('invalid_user'))
