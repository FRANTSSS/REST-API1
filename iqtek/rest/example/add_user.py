
__all__ = [
    "add_user_response",
    "add_user_example"
]


add_user_response = {
    201: {
        "description": "Created",
        "content": {
            "application/json": {
                "examples": {
                    "add": {
                        "summary": "Add User",
                        "value": {
                            "user": {
                                "uuid": "a5934a0e-66b3-4222-a83d-61fd9fb14ebc",
                                "full_name": "Frantsev Artyom Ilyich"
                            }
                        }
                    },
                }
            }
        }
    },
}

add_user_example = {
    "add": {
        "summary": "Add User",
        "value": {
            "user": {
                "full_name": "Frantsev Artyom Ilyich"
            }
        }
    }
}