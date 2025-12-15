import matplotlib.pyplot as plt

# =========================
# Data
# =========================
data = {
    '64': 555,
    '16': 17,
    'seq': 352,
    '128': 1361,
    '4': 1,
    '8': 68,
    '5120': 12,
    '256': 628,
    '1024': 100,
    '32': 200,
    '512': 196
}

# Sort numeric keys; place non-numeric at the end
keys = []
values = []
for k, v in sorted(
    data.items(),
    key=lambda item: int(item[0]) if item[0].isdigit() else float('inf')
):
    if k.isdigit():
        keys.append(k)
        values.append(v)

# =========================
# Figure style (paper-ready)
# =========================
fontsize=11
plt.rcParams.update({
    "font.size": fontsize,
    "axes.labelsize": 9,
    "xtick.labelsize": fontsize,
    "ytick.labelsize":fontsize,
    "axes.linewidth": 0.8,
})

fig, ax = plt.subplots(figsize=(6.2, 3.4))  # single-column friendly

# =========================
# Plot
# =========================
ax.bar(
    keys,
    values,
    color="0.6",          # grayscale
    edgecolor="black",
    linewidth=0.6
)

# Labels
ax.set_xlabel("K in batch GEMM", fontsize=fontsize)
ax.set_ylabel("Count", fontsize=fontsize)

# Grid (subtle)
ax.yaxis.grid(True, linestyle="--", linewidth=0.5, alpha=0.6)
ax.set_axisbelow(True)

# Remove top/right spines
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Tight layout to avoid clipping
fig.tight_layout()

# =========================
# Save
# =========================
fig.savefig(
    "../figures/shape_dist.pdf",
    bbox_inches="tight"
)
