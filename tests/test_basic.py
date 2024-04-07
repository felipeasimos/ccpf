import ccpf


def test_basic_cpf():
    is_valid = ccpf.validate("adf")
    print("validate: ", is_valid)
    cpf = ccpf.generate()
    print("cpf len:", len(cpf))
    print("cpf: ", cpf)
    has_mask = ccpf.has_mask("asdfadf")
    print("has_mask: ", has_mask)
    with_mask = ccpf.mask("adfasd")
    print("with_mask:", with_mask)
    no_mask = ccpf.unmask("adfasdf")
    print("no mask:", no_mask)
    pass
