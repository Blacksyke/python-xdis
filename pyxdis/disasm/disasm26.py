#  Copyright (c) 2015-2016 by Rocky Bernstein
"""
Python 2.6 bytecode disassembler

This sets up opcodes Python's 2.6 and calls a generalized
disassemble routine for Python 2.
"""

from pyxdis.disasm.disasm2 import Disassemble2

class Disassemble26(Disassemble2):

    def __init__(self):
        super(Disassemble2, self).__init__(2.6)

    pass

if __name__ == "__main__":
    from pyxdis import PYTHON_VERSION
    if PYTHON_VERSION == 2.6:
        from pyxdis.disasm.disasm2 import _test
        _test(PYTHON_VERSION)
    else:
        print("Need to be Python 2.6 to demo; I am %s." %
              PYTHON_VERSION)
