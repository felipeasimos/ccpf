import ccpf

NUM_TESTS = 100

def test_cpf():
    for i in range(NUM_TESTS):
        cpf = ccpf.generate()
        assert ccpf.validate(cpf)
        assert ccpf.has_mask(cpf) == False
        assert ccpf.has_mask(ccpf.mask(cpf)) == True
        assert ccpf.unmask(ccpf.mask(cpf)) == cpf
