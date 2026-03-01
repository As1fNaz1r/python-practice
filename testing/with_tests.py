from without_test import add
def test_add():
    assert add(2,3) == 5
    assert add(2.5,3.5) ==6.0
    assert add(-1,1) == 0
    # assert tt.add("2","3") == 5
    print("all test passed")

test_add()