# llm-cost-estimator

A tiny Python library + CLI that estimates LLM API spend from token counts. Built as a pipeline test for an automated GitHub portfolio workflow.

## Why

Every AI project needs a budget line. Before wiring an LLM into anything, you want a 5-second answer to "what will 10M tokens cost me on model X?" — this gives it.

## Install

```bash
pip install -e ".[dev]"
```

## Usage

```python
from cost_estimator import estimate_cost

estimate_cost("gpt-4o-mini", input_tokens=1_000_000, output_tokens=500_000)
# {'model': 'gpt-4o-mini', 'provider': 'OpenAI', ..., 'total_cost_usd': 0.45}
```

```bash
llm-cost --model gpt-4o-mini --input-tokens 1000000 --output-tokens 500000
llm-cost --list-models
```

## Tests

```bash
PYTHONPATH=src pytest -q
```

CI runs the suite on every push via GitHub Actions.

## Limitations

- Prices in `src/cost_estimator/prices.py` are sample figures — verify against the provider's current pricing before relying on them.
- No token counting yet: you supply the token counts (pair with a tokenizer for a full pipeline).
