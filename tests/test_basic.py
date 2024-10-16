import ccpf

NUM_TESTS = 100


def test_cpf():
    for i in range(NUM_TESTS):
        cpf = ccpf.generate()
        assert ccpf.validate(cpf)
        assert not ccpf.has_mask(cpf)
        masked = ccpf.mask(cpf)
        assert ccpf.has_mask(masked)
        assert ccpf.unmask(ccpf.mask(cpf)) == cpf
        cpf = str(int(cpf) + 1)
        assert not ccpf.validate(cpf)
