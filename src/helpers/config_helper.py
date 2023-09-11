import os

def get_base_url():
    env = os.environ.get('ENV', 'staging')
    if env.lower() == 'staging':
        return 'https://s8.asyx.com'
    elif env.lower() == 'prod':
        return 'https://id2.asyx.com'
    else:
        raise Exception(f"Unknown environment {env}")
