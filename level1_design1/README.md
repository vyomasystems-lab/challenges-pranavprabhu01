# Mux Design Verification

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (mux module here) which takes in 2-bit inputs starting from inp0-inp30 and gives 2-bit out

The values are assigned to the input port using 
```
A=2
dut.sel.value=30
dut.inp30.value=A
```

The assert statement is used for comparing the mux's outut to the expected value.

The following error is seen:
```
assert dut.out.value == A
```
## Test Scenario 
- Test Inputs: inp30=2
- Expected Output: out=2
- Observed Output in the DUT dut.out=0
 ![](https://raw.githubusercontent.com/vyomasystems-lab/challenges-pranavprabhu01/master/level1_design1/Screenshot%20(31).png?token=GHSAT0AAAAAABXE3B2XWNVLBV2NZNR7H5J4YXGDS5Q)
Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
 5'b11101: out = inp29;
 default: out = 0;
```
For the mux design, inp30 needs to be added

## Design Fix
Updating the design and re-running the test makes the test pass.
![](https://raw.githubusercontent.com/vyomasystems-lab/challenges-pranavprabhu01/master/level1_design1/Screenshot%20(37).png?token=GHSAT0AAAAAABXE3B2WKTNYPVWCJZ6CN5HWYXGDW2A)
## Verification Strategy
Observing the Verilog code and trying various possible inputs. The verification is complete.

