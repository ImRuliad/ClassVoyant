
def url_from_file():
    filepath = "../../SPOT/API_ENDPOINT.txt"
    with open(filepath) as file:
        return file.read()


if __name__ == "__main__":
    print(url_from_file())