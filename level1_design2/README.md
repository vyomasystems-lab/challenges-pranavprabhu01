# Sequence Detector Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives input to the Design Under Test (sequence detector module here) which takes in 1-bit input

The values are assigned to the input port using 
```
 dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut.inp_bit.value=0
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut.inp_bit.value=0
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
```

The assert statement is used for comparing the design's outut to the expected value.

The following error is seen:
```
assert dut.seq_seen.value==1
```
## Test Scenario **(Important)**
- Test Input:101011
- Expected Output: out=1
- Observed Output in the DUT dut.sum=0

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
 SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = IDLE;    ==>Bug
```
For the design, the next state should be SEQ_10

## Design Fix
Updating the design and re-running the test makes the test pass.



The updated design is checked in as adder_fix.v

## Verification Strategy

## Is the verification complete ?
