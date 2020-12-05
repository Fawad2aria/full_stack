from binary_search import search
def test_binary_search():
    assert search([1,2,3,4], 3) == 2
    assert search([1,2,3,4], 5) == -1
    assert search([1,2,3,4], 1) == 0
    assert search([1,2,3,4], 4) == 3
    assert search([1,2,3,4,5], 1) == 0
    assert search([1,2,3,4,5], 5) == 4
    assert search([1,2,3,4,5], 3) == 2
    assert search([1,2,3,4,5], 3) == 2
