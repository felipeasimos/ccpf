import native as _native


def validate(cpf: str) -> bool:
    return _native.validate(cpf)


def generate() -> str:
    return _native.generate()


def has_mask(cpf: str) -> bool:
    return _native.has_mask(cpf)


def mask(cpf: str) -> str:
    return _native.mask(cpf)


def unmask(cpf: str) -> str:
    return _native.unmask(cpf)
