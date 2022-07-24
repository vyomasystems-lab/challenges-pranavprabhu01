# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    A=2
    dut.sel.value=30
    dut.inp30.value=A
    await Timer(2, units='ns')
    dut._log.info(f'DUT={int(dut.out.value):02}')
    assert dut.out.value==A
     



    
