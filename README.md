# UTG-SC: Paper Result Summaries

Companion materials for **Authorizing a Completed Model Update: Update-Transition Grounded Selective Commit for Low-Label PolSAR Classification**.

This repository provides tabulated experimental results associated with the paper and a small utility for viewing them. It is a results-materials release, not a complete implementation or training package.

## Contents

| File | Contents |
| --- | --- |
| `results/main_table_12cells.csv` | Per-setting evaluation results |
| `results/main_table_summary.csv` | Aggregate method comparisons |
| `results/harm_summary_per_dataset.csv` | Per-dataset class-harm summaries |
| `results/cost_table.csv` | Reported computational measurements |

The tables are preserved from the submission materials. Please consult the paper for metric definitions, experimental settings, and limitations. Values and units follow the column headings and the paper; percentage-point differences are identified by `pp` where applicable.

## View the tables

With Python 3 (standard library only):

```sh
python tools/preview_results.py
python tools/preview_results.py results/main_table_12cells.csv
```

The utility prints the existing CSV values as a Markdown table; it does not run experiments or recompute model predictions.

## Implementation availability

Model implementations, training and inference pipelines, core method code, model weights, and raw datasets are not included in this public release. This repository alone does not reproduce model training or inference.

The repository URL is retained as the companion-materials link for the paper.

## License

See [LICENSE](LICENSE) for the license applicable to the materials included here.
