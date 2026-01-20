import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_func() -> mock.MagicMock:
    with mock.patch("app.main.get_exchange_rate_prediction") as func:
        func.return_value = 50
        yield func


def test_func_returns_correct_values1(
    mocked_func: mock.MagicMock
) -> None:
    assert cryptocurrency_action(45) == "Do nothing"


def test_func_returns_correct_values2(
    mocked_func: mock.MagicMock
) -> None:
    assert cryptocurrency_action(44.9) == "Buy more cryptocurrency"


def test_func_returns_correct_values3(
    mocked_func: mock.MagicMock
) -> None:
    assert cryptocurrency_action(55.1) == "Sell all your cryptocurrency"
