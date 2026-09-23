"""Core cost estimation logic."""

from .prices import PRICES


def list_models():
    """Return the known model names, sorted."""
    return sorted(PRICES)


def estimate_cost(model, input_tokens, output_tokens):
    """Estimate the USD cost for a model given input/output token counts.

    Returns a dict with the per-side and total cost breakdown.
    """
    if model not in PRICES:
        raise ValueError(
            f"unknown model: {model!r}. Known models: {', '.join(list_models())}"
        )
    if input_tokens < 0 or output_tokens < 0:
        raise ValueError("token counts must be non-negative")
    price = PRICES[model]
    input_cost = input_tokens / 1_000_000 * price["input"]
    output_cost = output_tokens / 1_000_000 * price["output"]
    return {
        "model": model,
        "provider": price["provider"],
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "input_cost_usd": round(input_cost, 6),
        "output_cost_usd": round(output_cost, 6),
        "total_cost_usd": round(input_cost + output_cost, 6),
    }
