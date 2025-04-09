from dataclasses import dataclass, field


@dataclass
class Quote:
    text: str
    autor: str
    tags: list[str] = field(default_factory=list)
