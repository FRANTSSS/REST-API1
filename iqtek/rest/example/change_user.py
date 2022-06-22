
__all__ = [
    "change_user_response",
    "change_user_example"
]


change_user_response = {
    204: {
        "description": "Changed",
        "content": {
            "application/json": {
                "examples": {
                    "put": {
                        "summary": "Change User"
                    },
                }
            }
        }
    },
}

change_user_example = {
    "change": {
        "summary": "Change User",
        "value": {
            "user": {
                "uuid": "a5934a0e-66b3-4222-a83d-61fd9fb14ebc",
                "full_name": "Frantsev Artyom Ilyich"
            }
        }
    }
}
