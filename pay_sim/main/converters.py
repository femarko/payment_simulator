import uuid


class UUIDConverter:

    regex = (
        r"[0-9a-fA-F]{32}"
        r"|"
        r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-"
        r"[0-9a-fA-F]{4}-[0-9a-fA-F]{12}"
    )

    def to_python(self, value) -> uuid.UUID:
        return uuid.UUID(value)

    def to_url(self, value) -> str:
        return uuid.UUID(str(value)).hex
