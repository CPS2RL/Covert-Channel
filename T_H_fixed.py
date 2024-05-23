
##T_H fixed

import numpy as np
import matplotlib.pyplot as plt

# Example array Q_3
Q_3 = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.3333333333333333, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.3333333333333333, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.3333333333333333, 1.0, 1.0, 1.0, 1.0, 0.3333333333333333, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.3333333333333333, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]


Q_6=[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.3333333333333333, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.3333333333333333, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.3333333333333333, 1.0, 1.0, 1.0, 1.0, 0.3333333333333333, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.3333333333333333, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]




fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 6))

# Calculate average and 50th percentile
average_Q3 = np.mean(Q_3)
average_Q4 = np.mean(Q_4)
#percentile_90_Q3 = np.percentile(Q_3, 90)
#percentile_90_Q4 = np.percentile(Q_4, 90)
percentile_90_Q3 = min(Q_3)
percentile_90_Q4 = min(Q_4)


# Plot Q_3 on the first subplot
xticks = [1] + [10 *i for i in range(1,11)]
ax1.bar(np.arange(1, len(Q_3) + 1), Q_3, color='lightgray', edgecolor='none', width=0.5)
ax1.set_xticks(xticks)
ax1.set_xticklabels(xticks)

ax1.set_title('Number of Frames = 3')
ax1.set_xlabel('Taskset ID')
ax1.set_ylabel('Inference Precision')
ax1.axhline(np.mean(Q_3), color='r', linestyle='--', label=f'Average ({np.mean(Q_3):.2f})')
ax1.axhline(percentile_90_Q3, color='g', linestyle='-', label=f'90th Percentile ({percentile_90_Q3:.2f})')
#ax1.legend(loc='upper left',facecolor='lightgray')

# Plot Q_4 on the second subplot
ax2.bar(np.arange(1, len(Q_4) + 1), Q_4, color='lightgray', edgecolor='none', width=0.5)
ax2.set_xticks(xticks)
ax2.set_xticklabels(xticks)

ax2.set_title('Number of Frames = 6')
ax2.set_xlabel('Taskset ID')
ax2.set_ylabel('Inference Precision')
ax2.axhline(np.mean(Q_4), color='r', linestyle='--', label=f'Average ({np.mean(Q_4):.2f})')
ax2.axhline(percentile_90_Q4, color='g', linestyle='-', label=f'90th Percentile({percentile_90_Q3:.2f})')
#ax2.legend(loc='upper left',facecolor='lightgray')

# Show the plot
plt.tight_layout()
plt.savefig('T_H_fixed.pdf')
plt.show()

print(np.mean(Q_3), np.mean(Q_4), min(Q_3), min(Q_4),np.percentile(Q_3, 90),np.percentile(Q_4, 90))


