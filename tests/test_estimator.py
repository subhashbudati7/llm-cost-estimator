import pytest

from cost_estimator import estimate_cost, list_models


def test_known_model_math():
    r = estimate_cost("gpt-4o-mini", 1_000_000, 1_000_000)
    assert r["input_cost_usd"] == pytest.approx(0.15)
    assert r["output_cost_usd"] == pytest.approx(0.60)
    assert r["total_cost_usd"] == pytest.approx(0.75)
    assert r["provider"] == "OpenAI"


def test_zero_tokens():
    r = estimate_cost("gpt-4o-mini", 0, 0)
    assert r["total_cost_usd"] == 0


def test_unknown_model():
    with pytest.raises(ValueError):
        estimate_cost("nope-9000", 10, 10)


def test_negative_tokens():
    with pytest.raises(ValueError):
        estimate_cost("gpt-4o-mini", -1, 10)


def test_list_models_sorted():
    models = list_models()
    assert models == sorted(models)
    assert "gpt-4o" in models
