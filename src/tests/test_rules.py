from sastrawi.rules import is_PAS, is_invalid_APS


def test_is_PAS() -> None:
    assert is_PAS("bermasalah") == True
    assert is_PAS("bersekolah") == True
    assert is_PAS("bertahan") == True
    assert is_PAS("mencapai") == True
    assert is_PAS("petani") == True
    assert is_PAS("terabai") == True

    assert is_PAS("menggunakan") == False


def test_invalid_APS() -> None:
    # test for invalid affix pair
    assert is_invalid_APS("berjatuhi") == True
    assert is_invalid_APS("dipukulan") == True
    assert is_invalid_APS("ketiduri") == True
    assert is_invalid_APS("ketidurkan") == True
    assert is_invalid_APS("menduaan") == True
    assert is_invalid_APS("terduaan") == True
    assert is_invalid_APS("perkataan") == True

    assert is_invalid_APS("memberikan") == False
    assert is_invalid_APS("ketahui") == False
