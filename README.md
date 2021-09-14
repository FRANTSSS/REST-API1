# REST-API version 1.1

methods:

get: /getUser{"fio": str}
post: /addUser{"fio": str}
put: /changeUser{"id": int, "fio": str}
delete: /deleteUser{"id": int}
