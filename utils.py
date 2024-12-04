def validate_name(name):
    return isinstance(name, str) and len(name) > 0

def validate_phone_number(phone, contacts):
    if not phone.isdigit():
        return False
    for contact in contacts:
        if contact['phone'] == phone:
            return False
    return True
