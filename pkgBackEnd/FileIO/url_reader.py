
#error check these functions later....

def load_base_url():
    try:
        API_filepath = "../../SPOT/API_ENDPOINT.txt"
        with open(API_filepath) as file:
            API_url = file.read()
            return API_url
    except FileNotFoundError as e:
        print(f"API file not found, make sure API_ENDPOINT.txt exists under /SPOT/ {e}")


if __name__ == "__main__":
    print(load_base_url())