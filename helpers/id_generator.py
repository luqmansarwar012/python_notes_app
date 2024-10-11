import uuid


def id_generator() -> int:
    return int(uuid.uuid4().int & 0xFFFF)
