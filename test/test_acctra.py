import acctra


def test_format_date():
    assert acctra.format_date("2018-11-08T08:21:45.902633") == "08-11-2018"
    assert acctra.format_date("2019-06-30T15:11:53.136004") == "30-06-2019"
    assert acctra.format_date("2018-02-13T04:43:11.374324") == "13-02-2018"


def test_hide_sensitive_number():
    assert acctra.hide_sensitive_number("Visa Platinum 1813166339376336") == "Visa Platinum 1813 16XX XXXX 6336"
    assert acctra.hide_sensitive_number("Счет 97848259954268659635") == "Счет XX9635"
    assert acctra.hide_sensitive_number("Maestro 9171987821259925") == "Maestro 9171 98XX XXXX 9925"
