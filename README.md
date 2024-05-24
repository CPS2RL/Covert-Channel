# FrameLeaker Implementation
This study investigates the presence of illicit
information flows in fixed-priority multiframe real-time systems.
We identify an algorithmic covert channel (called FrameLeaker)
that enables a low-priority task to deduce the execution patterns
(frames) of a high-priority task.

**Python version:** python 3.10

We propose a metric to
measure the successful inference of receiving frames ( Q value). We generate Q value for Four Cases by running `python3 Q_value_generation.py`:
1. TL and TH are randomly generated
2. TL and TH are harmonic
3. Fixed TL and varied TH 
4. Fixed TH and varied TL

   
To generate the plot fo reach cases, run `python3 harmonic.py/non_harmonic.py/T_H_fixed.py/T_L_fixed.py`. 

Paper Link: https://monowarhasan.info/papers/FrameLeaker_ISORC_2024.pdf
