# Covert-Channel
This study investigates the presence of illicit
information flows in fixed-priority multiframe real-time systems.
We identify an algorithmic covert channel (called FrameLeaker)
that enables a low-priority task to deduce the execution patterns
(frames) of a high-priority task
We propose a metric to
measure the successful inference of receiving frames ( Q value). We generate Q value for Four Cases by running **Q_value_generation.py**:
1. TL and TH are randomly generated
2. TL and TH are harmonic
3. Fixed TL and varied TH 
4. Fixed TH and varied TL
![image](https://github.com/CPS2RL/FrameLeaker/assets/71979845/6a1ed0e7-d2fa-4fc0-be11-4b661f82086e)
