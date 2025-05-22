
class Course:
    def __init__(self, major, name, units, description):
        self.major: str = major
        self.name: str = name
        self.units: int = units
        self.description: str = description
    