import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock

from cocotb.triggers import RisingEdge, FallingEdge,Timer

@cocotb.test()
async def test_SA(dut):
    """Test for serial adder"""

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    A=1
    B=1
    
    dut.data_a.value=A
    
    dut.data_b.value=B 
    await FallingEdge(dut.clk)
    await FallingEdge(dut.clk)
    await FallingEdge(dut.clk)
    await FallingEdge(dut.clk)
    await FallingEdge(dut.clk)
    
    assert dut.out.value==A+B
    
    dut._log.info('test')