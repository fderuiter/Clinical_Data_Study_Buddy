from cdisc_library_client.utils import normalize_headers


def test_normalize_headers_bytes():
    headers = {"Authorization": b"token"}
    assert normalize_headers(headers) == {"Authorization": "token"}


def test_normalize_headers_mixed_types():
    headers = {"Foo": bytearray(b"bar"), "Num": 123}
    assert normalize_headers(headers) == {"Foo": "bar", "Num": "123"}

