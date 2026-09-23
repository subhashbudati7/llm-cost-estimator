"""Sample per-1M-token prices in USD.

These are placeholder figures for demonstration — always verify against the
provider's current pricing page before relying on them.
"""

PRICES = {
    "gpt-4o": {"input": 2.50, "output": 10.00, "provider": "OpenAI"},
    "gpt-4o-mini": {"input": 0.15, "output": 0.60, "provider": "OpenAI"},
    "claude-sonnet-4": {"input": 3.00, "output": 15.00, "provider": "Anthropic"},
    "claude-haiku-4": {"input": 0.80, "output": 4.00, "provider": "Anthropic"},
    "gemini-2.0-flash": {"input": 0.10, "output": 0.40, "provider": "Google"},
}
