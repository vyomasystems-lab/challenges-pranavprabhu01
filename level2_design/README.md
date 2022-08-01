# Bitmanip Coprocessor Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (adder module here) which takes in four 32-bit inputs mav_putvalue_instr,mav_putvalue_src1,mav_putvalue_src2,mav_putvalue_src3 and gives 33-bit output mav_putvalue

The values are assigned to the input port using 
```
mav_putvalue_src1 = 0x6
mav_putvalue_src2 = 0x0
mav_putvalue_src3 = 0x1
mav_putvalue_instr = 0x101010B3
```

The assert statement is used for comparing the design's outut to the expected value.

The following error is seen:

```
assert dut_output == expected_mav_putvalue, error_message
```
## Test Scenario **(Important)**
- Test Inputs: mav_putvalue_src1 = 0x6 mav_putvalue_src2 = 0x0 mav_putvalue_src3 = 0x1
- Expected Output: out=0x00
- Observed Output in the DUT dut.out=0x02
![](https://github.com/vyomasystems-lab/challenges-pranavprabhu01/blob/master/level2_design/Screenshot%20(36).png)

Output mismatches for the above inputs proving that there is a design bug

## Verification Strategy
By providing random inputs to the design we can find the bugs.

## Is the verification complete ?
