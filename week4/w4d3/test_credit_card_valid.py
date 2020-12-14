from credit_card_valid import card_validation
def test_credit_card():
    assert card_validation('4556737586899855') == True
    assert card_validation('4455323') == False