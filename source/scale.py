import matplotlib.pyplot as plt
import numpy as np
fontsize=17

# 数据
numa = [1, 2, 4, 8]
seq_lengths = [512, 1024, 1576]

fp16 = {
    512: [162, 96, 46.57, 200],
    1024: [465, 306, 183, 130.13],
    1576: [1190, 747, 421, 290]
}

int8 = {
    512: [171, 103, 47, 210],
    1024: [470, 315, 187, 132],
    1576: [1424, 854, 432, 294]
}

fastfold = {512: 175, 1024: 329, 1576: 500}
open_omics = {512: 257.78, 1024: 682.7, 1576: 1559.32}

# 创建子图，每个子图纵轴独立
fig, axes = plt.subplots(1, 3, figsize=(18,4), sharey=False)

for i, seq in enumerate(seq_lengths):
    ax = axes[i]
    
    # 绘制 FP16 和 INT8
    ax.plot(numa, fp16[seq], marker='o', label='MatrixFold', color='#d62728')
    # ax.plot(numa, int8[seq], marker='s', label='INT8')
    
    # 绘制 fastfold 和 open-omics-alphafold 虚横线
    ax.axhline(fastfold[seq], linestyle='--', label='FastFold' if i==2 else "")
    ax.axhline(open_omics[seq], color='green', linestyle='--', label='Open-Omics-Alphafold' if i==2 else "")
    
    ax.set_title(f'Sequence length {seq}', fontsize=fontsize)
    ax.set_xlabel('NUMA nodes', fontsize=fontsize)
    ax.set_xticks(numa)
    ax.set_xticklabels(numa, fontsize=fontsize)
    ax.set_yticklabels([int(x) for x in ax.get_yticks()], fontsize=fontsize)
    ax.grid(True, linestyle=':', alpha=0.5)

axes[2].set_ylabel('Time (s)', fontsize=fontsize)
axes[2].legend(loc='upper right',fontsize=fontsize)
# plt.suptitle('Performance across NUMA nodes and sequence lengths')
plt.tight_layout()
plt.savefig('../figures/scale.pdf')
