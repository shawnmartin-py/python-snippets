class MyType(type):
  def __new__(mcls, name, bases, cls_dict):
    new_class = super().__new__(mcls, name, bases, cls_dict)
    return new_class

class Person(metaclass=MyType): ...

class SlottedStruct(type):
  def __new__(mcls, name, bases, class_dict):
    cls_object = super().__new__(mcls, name, bases, class_dict)

    setattr(cls_object, '__slots__', [f'_{field}' for field in cls_object._fields])

    for field in cls_object._fields:
      slot = f'_{field}'
      setattr(cls_object, field, property(fget=lambda self, attrib=slot: getattr(self, attrib)))

    def eq(self, other):
      if isinstance(other, cls_object):
        self_fields = [getattr(self, field) for field in cls_object._fields]
        other_fields = [getattr(other, field) for field in other._fields]
        return self_fields == other_fields
      return False
    setattr(cls_object, '__eq__', eq)

    def hash_(self):
      field_values = (getattr(self, field) for field in cls_object._fields)
      return hash(tuple(field_values))
    setattr(cls_object, '__hash__', hash_)

    def string_(self):
      field_values = (getattr(self, field) for field in cls_object._fields)
      field_values_joined = ', '.join(map(str, field_values))
      return f'{cls_object.__name__}({field_values_joined})'
    setattr(cls_object, '__str__', string_)

