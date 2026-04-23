import argparse
import re
from pathlib import Path

import matplotlib.pyplot as plt

fontsize=12
LOG_PATTERN = re.compile(r"^(SVE|SME|SCALER)\s+.*?N=(\d+).*?pack%=(\d+\.\d+)")
label_map = {
	'SCALER': 'SCALAR',
	'SVE': 'VECTOR',
	'SME': 'ZA',
}


def parse_log(log_path: Path) -> dict[str, dict[int, float]]:
	data: dict[str, dict[int, float]] = {"SVE": {}, "SME": {}, "SCALER": {}}
	for line in log_path.read_text().splitlines():
		match = LOG_PATTERN.search(line)
		if not match:
			continue
		kind, n_str, pack_str = match.groups()
		data[kind][int(n_str)] = float(pack_str)
	return data


def plot_pack_percent(data: dict[str, dict[int, float]], output: Path) -> None:
	fig, ax = plt.subplots(figsize=(7, 5))

	styles = {
		"SCALER": {"color": "#8c564b", "marker": "o"},
		"SVE": {"color": "#1f77b4", "marker": "s"},
		"SME": {"color": "#2ca02c", "marker": "^"},
	}

	expected_ns = [64, 128, 256, 512, 1024]
	positions = {n: i for i, n in enumerate(expected_ns)}  # keep x axis evenly spaced

	for label in ["SCALER", "SVE", "SME"]:
		ns = [n for n in expected_ns if n in data[label]]
		if not ns:
			continue
		xs = [positions[n] for n in ns]
		packs = [data[label][n] for n in ns]
		ax.plot(xs, packs, label=label_map[label].lower(), **styles[label])

	ax.set_xticks(list(positions.values()), labels=[str(n) for n in expected_ns], fontsize=fontsize)
	ax.set_xlabel("GEMM shape N", fontsize=fontsize)
	ax.set_ylabel("packing performance proportion (%)", fontsize=fontsize)
	# ax.set_title("The impact of different packing strategies")
	ax.grid(True, linestyle="--", linewidth=0.6, alpha=0.6)
	ax.legend(fontsize=fontsize)
	fig.tight_layout()
	fig.savefig(output)


def main() -> None:
	parser = argparse.ArgumentParser(description="Plot pack percent curves from log file.")
	parser.add_argument(
		"--log",
		dest="log_path",
		type=Path,
		default=Path(__file__).with_name("pack_percent_data.log"),
		help="Path to the log file to parse.",
	)
	parser.add_argument(
		"--output",
		dest="output",
		type=Path,
		default="../figures/pack_performance.pdf",
		help="Path to save the output figure.",
	)
	args = parser.parse_args()

	if not args.log_path.exists():
		raise FileNotFoundError(f"Log file not found: {args.log_path}")

	data = parse_log(args.log_path)
	if not any(data.values()):
		raise ValueError("No pack percent data parsed from log file.")

	plot_pack_percent(data, args.output)
	print(f"Saved plot to {args.output}")


if __name__ == "__main__":
	main()
