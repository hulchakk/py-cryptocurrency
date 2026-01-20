import pytest
from unittest import mock
from typing import Any, Callable

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_func() -> Any:
    with mock.patch("app.main.get_exchange_rate_prediction") as func:
        yield func


@pytest.mark.parametrize(
    "rate,prediction,expected",
    [
        (1, 6, "Buy more cryptocurrency"),
        (6, 1, "Sell all your cryptocurrency"),
        (6, 6 , "Do nothing")
    ]
)
def test_func_returns_correct_values(
    rate: int,
    prediction: int,
    expected: str,
    mocked_func: Callable
) -> None:
    mocked_func.return_value = prediction
    assert cryptocurrency_action(rate) == expected
