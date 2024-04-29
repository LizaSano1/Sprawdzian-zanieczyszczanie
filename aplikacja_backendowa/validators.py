from pydantic import ValidationError

def handle_validation_error(e: ValidationError):
    return {"error": str(e)}, 400
