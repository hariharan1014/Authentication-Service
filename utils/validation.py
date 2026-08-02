def validate_registration_data(data):
    required_fields = [
        "username",
        "email",
        "password"
    ]
    for key in required_fields:
        value=data.get(key)
        if value is None or value.strip() == "" :
            return ({
                "success" : False,
                "message" : f"{key} is required."
            })
    return ({
        "success" : True,
        "message" : "Validation is successful."
    })