
from table import table

class isa:
    def __init__(self, signals: tuple[str]) -> None:
        self.table = table(signals)

    def add_instr(self, instr: tuple[str]) -> None:
        self.table.add(instr)
    
    def get_instr_at(self, index) -> tuple[str]:
        return self.table.get_at(index)
    
    def swap_instr(self, index_a, index_b) -> None:
        self.table.add_at(self.table.remove_at(index_a), index_b)
    
    def get_signals(self) -> None:
        return self.table.get_schema()
