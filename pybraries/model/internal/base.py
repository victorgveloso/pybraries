import json

from jsonpickle import decode, encode


class Base:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__dict__.update(**kwargs)

    @classmethod
    def from_json(cls, text: str):
        try:
            return decode(text)
        except (ValueError, NotImplementedError, TypeError):
            return json.loads(text, object_hook=cls.from_dict)

    def to_json(self):
        return encode(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)
