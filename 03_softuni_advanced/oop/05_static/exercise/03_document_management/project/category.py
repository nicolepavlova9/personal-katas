class Category:

    def __init__(self, uid: int, name: str) -> None:
        self.id = uid
        self.name = name

    def edit(self, new_name: str) -> None:
        self.name = new_name

    def __repr__(self) -> str:
        return f"Category {self.id}: {self.name}"
