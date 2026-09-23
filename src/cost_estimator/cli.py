"""Command-line interface for llm-cost-estimator."""

import argparse
import json

from .estimator import estimate_cost, list_models


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Estimate LLM API cost from token counts."
    )
    parser.add_argument("--model", help="Model name, e.g. gpt-4o-mini")
    parser.add_argument("--input-tokens", type=int, default=0)
    parser.add_argument("--output-tokens", type=int, default=0)
    parser.add_argument(
        "--list-models", action="store_true", help="List known models and exit"
    )
    args = parser.parse_args(argv)

    if args.list_models:
        print("\n".join(list_models()))
        return 0
    if not args.model:
        parser.error("--model is required (unless --list-models)")

    result = estimate_cost(args.model, args.input_tokens, args.output_tokens)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
