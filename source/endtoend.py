import matplotlib.pyplot as plt

# X-axis: sequence length
x = [64, 128, 256, 512, 1024, 2048, 2560, 3072, 4096]

# Data (latency)
matrixfold_fp16 = [16.45, 19.86, 36.3, 46.57, 130.13, 732, 1143, 1728, 3768]
matrixfold_int8 = [16.95, 20, 37, 47, 132, 840, 1304, 2040, 4436]
fastfold = [128, 139.7, 143.8, 175, 329, 844, 1524, 4866, 12220]
open_omics = [24, 39.53, 88.18, 257.78, 682.7, 2367.43, 3654.44, 5445.42, 10560.44]

plt.figure()

plt.plot(x, matrixfold_fp16, marker='o', label='MatrixFold (FP16)')
plt.plot(x, matrixfold_int8, marker='o', label='MatrixFold (INT8)')
plt.plot(x, fastfold, marker='o', label='FastFold')
plt.plot(x, open_omics, marker='o', label='Open-Omics-AlphaFold')

plt.xlabel('Sequence Length')
plt.ylabel('Latency (s)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig('../figures/hbm_fastfold.pdf')
