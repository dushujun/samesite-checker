import pytest


@pytest.mark.parametrize('useragent, expected', (
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.3538.77 Safari/537.36', False),
    ('curl/7.54.0', True),
    ('', True),
    ('Mozilla/5.0 (Linux; U; Android 7.0; en-US; SM-G935F Build/NRD90M) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/13.3.8.976 U3/0.8.0 Mobile Safari/534.30', True),
    ('Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; Micromax A106 Build/KOT49H) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.6.0.378 U3/0.8.0 Mobile Safari/533.1', False),
))
def test_samesite(useragent, expected):
    from samesite import should_send_sameiite_none

    assert should_send_sameiite_none(useragent) == expected
