import math

def calculate_response_times_upto_time(C, T, total_time):
    n = len(C)
    response_times = {i: [] for i in range(n)}
    
    for current_time in range(1, total_time + 1):
        for i in range(n):
            if current_time % T[i] == 0:
                # Task i arrives at this time
                R_prev = C[i]
                while True:
                    R = C[i] + sum(math.ceil(R_prev / T[j]) * C[j] for j in range(i))
                    if R == R_prev:
                        break
                    R_prev = R
                response_times[i].append((current_time, R))
    
    return response_times

# Example usage
C = [2, 1, 2]  # Computation times
T = [5, 10, 20]  # Periods
total_time = 50  # Total time to calculate the response times for

response_times = calculate_response_times_upto_time(C, T, total_time)
print(response_times)
for i in range(len(C)):
    print(f"Task {i+1} response times:")
    for time, R in response_times[i]:
        print(f"  At time {time}: Response Time = {R}")
