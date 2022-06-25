from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Block:
    name: str = None
    renewable: Dict[str, bool] = field(default_factory=dict)
    stackable: bool = False
    stackable_amount: int = 0
    tools: List[str] = field(default_factory=list)
    blast_resistance: Dict[str, float] = field(default_factory=dict)
    hardness: float = 0.0
    luminant: bool = False
    transparent: bool = False
    flammable: Dict[str, bool] = field(default_factory=dict)
    lava_ignitable: Dict[str, bool] = field(default_factory=dict)
