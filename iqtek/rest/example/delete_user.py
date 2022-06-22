
__all__ = [
    "delete_user_response"
]


delete_user_response = {
    204: {
        "description": "Deleted",
        "content": {
            "application/json": {
                "examples": {
                    "get": {
                        "summary": "Delete User"
                    },
                }
            }
        }
    },
}
