from myapp import add

def test_add():
    assert add(2, 4)== 6
    assert add (3, -2) == 1

print (test_add())