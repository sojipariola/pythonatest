from myapp import add

def test_add():
    assert add(2, 4)== 6
    assert add (3, -2) == 1
    assert add(200, 4)== 204
    assert add (300, -2) == 298

print (test_add())