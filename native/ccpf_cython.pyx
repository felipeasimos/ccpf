#cython: language_level=3
from libc.stdlib cimport free, malloc, realloc
cdef extern from "ccpf/ccpf.h":
    int cpf_validate(char* cpf)
    void cpf_generate(char* cpf)
    int cpf_has_mask(char* cpf);
    void cpf_mask(char* cpf)
    void cpf_unmask(char* cpf)

def validate(cpf: str) -> bool:
    cpf_bytes = cpf.encode()
    cdef char* cpf_string = cpf_bytes
    return bool(cpf_validate(cpf_string))

def generate() -> str:
    # don't allocate for null byte
    cdef char* cpf_string = <char*> malloc(11 * sizeof(char));
    cpf_generate(cpf_string)
    try:
        py_bytes = cpf_string[:11]
    finally:
        free(cpf_string)
    return py_bytes.decode('ascii')

def has_mask(cpf: str) -> bool:
    cpf_bytes = cpf.encode()
    cdef char* cpf_string = cpf_bytes
    return bool(cpf_has_mask(cpf_string))

def mask(cpf: str) -> str:
    cpf_bytes = cpf.encode() + b'\x00\x00\x00'
    cdef char* cpf_string = cpf_bytes
    cpf_mask(cpf_string)
    py_bytes = cpf_string[:14]
    return py_bytes.decode('ascii')

def unmask(cpf: str) -> str:
    cpf_bytes = cpf.encode()
    cdef char* cpf_string = cpf_bytes
    cpf_unmask(cpf_string)
    py_bytes = cpf_string[:11]
    return py_bytes.decode('ascii')
