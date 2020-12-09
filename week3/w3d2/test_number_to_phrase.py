from number_to_phrase import number_phrase
def test_number_phrase():
    assert number_phrase(1) == 'one'
    assert number_phrase(100) == 'one hundred '
    assert number_phrase(151) == 'one hundred fiftyone'