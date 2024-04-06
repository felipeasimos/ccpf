#cython: language_level=3
cdef extern from "ccpf/ccpf.h":
    void cpf_validate()

def validate():
    return cpf_validate()
