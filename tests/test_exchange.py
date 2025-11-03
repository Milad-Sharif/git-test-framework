
def test_get_exchange_rate(mocker):
    fake_response = mocker.Mock()
    fake_response.json.return_value = {"rates": {"USD": 1.25}}
    mocker.patch("calculator.calculator.requests.get", return_value = fake_response)

    from calculator.calculator import get_exchange_rate
    result = get_exchange_rate("EUR","USD")

    assert result == 1.25

 