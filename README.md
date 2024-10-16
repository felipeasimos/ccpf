## ccpf

A CPF (brazilian register numbers for persons) library that can:
* Validate CPFs
* Generate random CPFs
* Apply and remove masks from CPFs
* Check if CPFs are masked

### Install

Just do `pip3 install ccpf` and you are good to go.

### How to use

After `import`ing `ccpf` you can:

* `generate()` - generate a random valid unmasked CPF

```
import ccpf
cpf = ccpf.generate()
assert ccpf.validate(cpf)
```

* `validate(cpf)` - validate if a string is a valid CPF. Works for masked and unmasked CPFs.

```
import ccpf
cpf = ccpf.generate()
assert ccpf.validate(cpf)
```

* `has_mask(cpf)` - return wheter or not the given CPF is masked.

```
import ccpf
cpf = ccpf.generate()
assert not ccpf.has_mask(cpf)
```

* `mask(cpf)` - return the masked version of the given CPF. If the CPF is already masked, just return it.

```
import ccpf
cpf = ccpf.generate()
assert not ccpf.has_mask(cpf)
masked = ccpf.mask(cpf)
assert ccpf.has_mask(masked)
masked2 = ccpf.mask(masked)
assert ccpf.has_mask(masked2)
```

* `unmask(cpf)` - return unmasked version of the given CPF. If the CPF is already unmasked, just return it.

```
import ccpf
cpf = ccpf.generate()
assert not ccpf.has_mask(cpf)
unmasked = ccpf.unmask(cpf)
assert not ccpf.has_mask(unmasked)
masked = ccpf.mask(unmasked)
assert ccpf.has_mask(masked)
unmasked2 = ccpf.unmask(masked)
assert not ccpf.has_mask(unmasked2)
```

### Run tests

Just execute `tox` by calling it: 

```
tox
```
