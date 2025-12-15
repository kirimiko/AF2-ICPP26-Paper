import matplotlib.pyplot as plt
import numpy as np

fontsize=22
# ===========================
# 1. 数据准备
# ===========================
# Experiment 1: Varying K (Fixed M=32, N=32)
k_values = [32, 64, 128, 256, 512, 1024, 2048]
k_fp16   = [117, 212, 344, 492, 630, 724, 718]
k_int8   = [123, 225, 443, 782, 1088, 1373, 1685]

# Experiment 2: Varying N (Fixed M=32, K=32)
n_values = [32, 64, 128, 256, 512, 1024, 2048]
n_fp16   = [117, 123, 123, 122, 124, 117, 116]
n_int8   = [123, 118, 122, 123, 121, 124, 121]

# ===========================
# 2. 全局绘图风格设置 (Paper Style)
# ===========================
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman'],
    'font.size': 14,
    'axes.linewidth': 1.5,
    'xtick.major.width': 1.2,
    'ytick.major.width': 1.2,
    'legend.fontsize': 12,
    'lines.linewidth': 2,
    'lines.markersize': 8
})

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# ===========================
# 3. 子图 (a): Impact of K
# ===========================
ax1.plot(k_values, k_fp16, marker='o', label='FP16', color='#1f77b4', linestyle='-') # Blue
ax1.plot(k_values, k_int8, marker='s', label='INT8', color='#d62728', linestyle='--') # Red

ax1.set_xscale('log', base=2)
ax1.set_xlabel('K Dimension (Reduction)', fontweight='bold', fontsize=fontsize)
ax1.set_ylabel('Throughput (GFLOPS)', fontweight='bold', fontsize=fontsize)
ax1.set_title('(a) Sensitivity to K (M=N=32)', fontsize=fontsize, pad=10)
ax1.grid(True, which="both", ls="-", alpha=0.2)
ax1.legend(loc='upper left', frameon=False,fontsize=fontsize)

# 设置xticks以显示具体的数字而不是指数
ax1.set_xticks(k_values)
ax1.set_xticklabels(k_values, rotation=45, fontsize=fontsize)

# ===========================
# 4. 子图 (b): Impact of N
# ===========================
ax2.plot(n_values, n_fp16, marker='o', label='FP16', color='#1f77b4', linestyle='-')
ax2.plot(n_values, n_int8, marker='s', label='INT8', color='#d62728', linestyle='--')

ax2.set_xscale('log', base=2)
ax2.set_xlabel('N Dimension (Independent)', fontweight='bold', fontsize=fontsize)
# Y轴标签可以省略，或者保持一致
# ax2.set_ylabel('Throughput (GFLOPS)', fontweight='bold') 
ax2.set_title('(b) Sensitivity to N (M=K=32)', fontsize=fontsize, pad=10)
ax2.grid(True, which="both", ls="-", alpha=0.2)

# 为了对比鲜明，我们让两张图的Y轴范围保持一致，或者让右图也能看清
# 这里建议：为了显示右图的“平坦”，Y轴可以设定为从0开始，但如果为了对比左图的巨大差异，可以共享Y轴
# 策略：共享Y轴可以让读者直观看到 K=32 时的性能是多么低
ax2.set_ylim(ax1.get_ylim()) 
# 如果觉得右图线条挤在一起看不清，可以注释掉上面这一行，使用独立的scale

ax2.set_xticks(n_values)
ax2.set_xticklabels(n_values, rotation=45,fontsize=fontsize)

# ===========================
# 5. 保存与展示
# ===========================
plt.tight_layout()
plt.savefig('../figures/gemm_sensitivity.pdf', format='pdf', bbox_inches='tight')
print("Figure saved as gemm_sensitivity.pdf")
plt.show()