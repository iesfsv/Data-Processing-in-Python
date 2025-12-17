
def test_sum():
    assert sum([2,2]) == 4, "Should be 2"

def test_len_vs__len__():
    a_tuple = (1,2,3,5)
    assert len(a_tuple) == a_tuple.__len__(), "Function len returned different result than method __len__"
