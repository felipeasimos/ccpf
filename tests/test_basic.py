import pytest
import ccpf


def test_basic_cpf():
    is_valid = ccpf.validate()
    assert is_valid
