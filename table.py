
from __future__ import annotations

class table:
    def __init__(self, schema: tuple[str]) -> None:
        self.schema: tuple[str] = schema
        self.data: list[tuple[str]] = []
    
    def add(self, entry: tuple[str]) -> None:
        if len(entry) != self.width():
            print(f"ERROR: Could not add entry with id '{entry[0]}' to table because the entry is too short or too long")
            return
        self.data.append(entry)

    def add_at(self, entry: tuple[str], index) -> None:
        if len(entry) != self.width():
            print(f"ERROR: Could not add entry with id '{entry[0]}' to table because the entry is too short or too long")
            return
        self.data.insert(index, entry)
    
    def remove(self, entry: tuple[str]) -> None:
        try:
            self.data.remove(entry)
        except(ValueError):
            print(f"ERROR: Could not remove entry with id '{entry[0]}' from table because it does not exist")

    def remove_at(self, index) -> tuple[str]:
        try:
            temp = self.data[index]
            self.data.pop(index)
            return temp
        except(IndexError):
            print(f"ERROR: Could not remove entry at index {index} from table because index is out of range")

    def get_schema(self) -> tuple[str]:
        return self.schema

    def get_at(self, index) -> None:
        return self.data[index]
    
    def width(self) -> None:
        return len(self.schema)
    
    def depth(self) -> None:
        return len(self.data)

    def __eq__(self, other: table):
        # table: entry
        if len(self.data) != len(other.data):
            return False # not equal if different lengths
        for i in range(len(self.data)):
            if self.data[i] != other.data[i]:
                return False # not equal if at least one item is not the same
        return True
