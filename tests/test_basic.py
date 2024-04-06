import pytest
import ccpf


def test_basic_cpf():
    is_valid = ccpf.hello()
    assert is_valid
