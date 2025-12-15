import matplotlib.pyplot as plt
import numpy as np

# X-axis: sequence length
x = [64, 128, 256, 512, 1024, 2048, 2560, 3072, 4096]

# Latency data
matrixfold_fp16 = [16.45, 19.86, 36.3, 46.57, 130.13, 732, 1143, 1728, 3768]
matrixfold_int8 = [16.95, 20, 37, 47, 132, 840, 1304, 2040, 4436]
open_omics = [24, 39.53, 88.18, 257.78, 682.7, 2367.43, 3654.44, 5445.42, 10560.44]
fastfold = [128, 139.7, 143.8, 175, 329, 844, 1524, 4866, 12220]

# Speedup over Open-Omics AlphaFold
speedup_fp16 = [o / m for o, m in zip(open_omics, matrixfold_fp16)]
speedup_int8 = [o / m for o, m in zip(open_omics, matrixfold_int8)]
speedup_fastfold = [o / m for o, m in zip(open_omics, fastfold)]
print(max(speedup_fp16), min(speedup_fp16))

fig, ax1 = plt.subplots()

# --------------------
# Left Y-axis: Latency
# --------------------
ax1.plot(x, matrixfold_fp16, marker='o', label='MatrixFold (FP16) Latency')
ax1.plot(x, matrixfold_int8, marker='o', label='MatrixFold (INT8) Latency')
ax1.plot(x, fastfold, marker='o', label='FastFold Latency')
ax1.plot(x, open_omics, marker='o', 
         label='Open-Omics AlphaFold Latency')

ax1.set_xlabel('Sequence Length')
ax1.set_ylabel('Latency (s)')
# lat_max = max(fastfold)

ax1.set_ylim(-1000, 13000)
ax1.set_yticks([0, 2000, 4000, 6000, 8000, 10000, 12000])
# ax1.set_ylim(0, lat_max)
# num_ticks = 6
# lat_ticks = np.linspace(0, lat_max, num_ticks)
# ax1.set_yticks(lat_ticks)

ax1.grid(True)

# --------------------
# Right Y-axis: Speedup
# --------------------
ax2 = ax1.twinx()
ax2.plot(x, speedup_fp16, marker='x', linestyle=':',
         label='MatrixFold (FP16) Speedup')
ax2.plot(x, speedup_int8, marker='x', linestyle=':',
         label='MatrixFold (INT8) Speedup')
ax2.plot(x, speedup_fastfold, marker='x', linestyle=':',
         label='FastFold Speedup')

ax2.set_ylabel('Speedup over Open-Omics AlphaFold')
ax2.axhline(1.0, linestyle='--', color='#d62728')

spd_max = max(max(speedup_fp16), max(speedup_int8), max(speedup_fastfold))
ax2.set_ylim(0, spd_max)

# Match tick count and alignment
# spd_ticks = np.linspace(0, spd_max, num_ticks)
# ax2.set_yticks(spd_ticks)
ax2.set_ylim(-0.5, 7)
ax2.set_yticks([0, 1, 2, 3, 4, 5, 6])


# --------------------
# Legend (merged)
# --------------------
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right', framealpha=0.5)

plt.tight_layout()
plt.savefig('../figures/overall_performance.pdf')
