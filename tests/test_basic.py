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


def test_example_generate():
    for i in range(NUM_TESTS):
        cpf = ccpf.generate()
        assert ccpf.validate(cpf)


def test_example_validate():
    for i in range(NUM_TESTS):
        cpf = ccpf.generate()
        assert ccpf.validate(cpf)


def test_example_has_mask():
    for i in range(NUM_TESTS):
        cpf = ccpf.generate()
        assert not ccpf.has_mask(cpf)


def test_example_mask():
    for i in range(NUM_TESTS):
        cpf = ccpf.generate()
        assert not ccpf.has_mask(cpf)
        masked = ccpf.mask(cpf)
        assert ccpf.has_mask(masked)
        masked2 = ccpf.mask(masked)
        assert ccpf.has_mask(masked2)


def test_example_unmask():
    for i in range(NUM_TESTS):
        cpf = ccpf.generate()
        assert not ccpf.has_mask(cpf)
        unmasked = ccpf.unmask(cpf)
        assert not ccpf.has_mask(unmasked)
        masked = ccpf.mask(unmasked)
        assert ccpf.has_mask(masked)
        unmasked2 = ccpf.unmask(masked)
        assert not ccpf.has_mask(unmasked2)
