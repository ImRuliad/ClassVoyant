import os
from dotenv import load_dotenv

load_dotenv()

def base_url():
    base_url = os.getenv('BASE_URL')
    return base_url

"""
def major_url():
    major_url = os.getenv('MAJOR_URL')
    return major_url
"""
if __name__ == "__main__":
    base_url()







