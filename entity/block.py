from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Block:
    name: str
    renewable: Dict[str, bool]
    stackable: bool
    stackable_amount: int
    tools: List[str]
    blast_resistance: Dict[str, float]
    hardness: float
    luminant: bool
    transparent: bool
    flammable: Dict[str, bool]
    lava_ignitable: Dict[str, bool]
