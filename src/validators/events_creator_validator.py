from cerberus import Validator

def events_creator_validator(req: any):
    body_validator = Validator({
        "data": {
            "type": "dict",
            "schema": {
                "nome": {
                    "type": "string",
                    "required": True,
                    "empty": False,
                },
            }
        }
    })

    res = body_validator.validate(req.json)

    if res is False:
        raise Exception(body_validator.errors)