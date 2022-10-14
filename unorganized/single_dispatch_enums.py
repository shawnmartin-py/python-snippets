from enum import Enum, unique
from functools import singledispatchmethod


class Color(str, Enum):
  RED = "red"
  GREEN = "green"
  BLUE = "blue"
  NAVY = "navy"
  YELLOW = "yellow"


  def __eq__(self, other):
    if isinstance(other, str):
      return self.name.lower() == other.lower()
    return self is other

  


print(Color.RED == 'red')



