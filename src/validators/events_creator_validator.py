from cerberus import Validator

def events_creator_validator(req: any):
    body_validator = Validator({
        "data": {
            "type": "dict",
            "schema": {
                "name": {
                    "type": "string",
                    "required": True,
                    "empty": False,
                },
            }
        }
    })

    res = body_validator.validate(req.json)

    if res is False:
        print(body_validator.errors)
        return body_validator.errors