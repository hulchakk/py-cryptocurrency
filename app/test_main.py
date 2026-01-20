from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_func_returns_correct_values1(
    mocked_func: mock.MagicMock
) -> None:
    mocked_func.return_value = 100
    assert cryptocurrency_action(95) == "Buy more cryptocurrency"
    assert cryptocurrency_action(106) == "Sell all your cryptocurrency"
    assert cryptocurrency_action(100) == "Do nothing"
