import random

def generate_program_data():
    random_number = random.randint(1, 1000)
    program_name = f"Program_{random_number}"
    program_desc = f"Desc_{random_number}"
    return {'name': program_name, 'description': program_desc}

# def generate_program_data():
#     random_number = random.randint(1, 1000)
#     return {'name': f"Program_{random_number}", 'description': f"Desc_{random_number}"}
