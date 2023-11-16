from typing import NamedTuple  # could be a  data class?


class Book(NamedTuple):
    id: int
    name: str
    author: str
