class DVD:

    def __init__(
        self,
        name: str,
        id: int,
        creation_year: int,
        creation_month: str,
        age_restriction: int,
    ) -> None:
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int) -> "DVD":
        day, month, year = map(int, date.split("."))
        months = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]
        creation_month = months[month - 1]
        return cls(name, id, year, creation_month, age_restriction)

    def __repr__(self):
        dvd_status = "rented" if self.is_rented else "not rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {dvd_status}"
