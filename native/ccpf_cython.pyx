cdef extern from "ccpf/ccpf.h":
    int cpf_validate(int a)
    void hello()

def cpf_validate(cpf):
    return cpf_validate(cpf)

def cpf_hello():
    return hello()
