##This is the correct version of code
import math

def calculate_multiframe_response_times_upto_time(C, T, total_time):
    n = len(C)
    response_times = {i: [] for i in range(n)}

    for current_time in range(0, total_time + 1):
        for i in range(n):
            if current_time % T[i] == 0:
                # Task i arrives at this time
                frame_index = (current_time // T[i]) % len(C[i])
                current_C = C[i][frame_index]
                R_prev = current_C
                while True:
                    R = current_C + sum(
                        math.ceil(R_prev / T[j]) * C[j][(current_time // T[j]) % len(C[j])]
                        for j in range(i)
                    )
                    if R == R_prev:
                        break
                    R_prev = R
                response_times[i].append((current_time, R))

    return response_times

# Example usage
C = [
    [2],  # Computation times for task 1
    [1, 2, 3],     # Computation times for task 2
    [2]   # Computation times for task 3
]
T = [5, 10, 20]  # Periods
total_time = 40  # Total time to calculate the response times for

response_times = calculate_multiframe_response_times_upto_time(C, T, total_time)
print(response_times)
for i in range(len(C)):
    print(f"Task {i+1} response times:")
    for time, R in response_times[i]:
        print(f"  At time {time}: Response Time = {R}")
