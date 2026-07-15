from addition import add , subtract,multiply,divide

def test_add_positive_numbers():
    assert add(2,3)==5

def test_add_negative_numbers():
    assert add(-2,-3)==-5

def test_add_zero():
    assert add(0,5)==5

def test_add_positive_and_negative():
    assert add(5,-3)==2

def test_add_floats():
    assert add(2.5,3.1)==5.6

def test_subtract():
    assert subtract(3,3)==0

def test_negative_numbers():
    assert subtract(-3,-2)==-1

def test_multiply():
    assert multiply(1,1)==1

def test_multiply_zero():
    assert multiply(1,0)==0

def test_divide():
    assert divide(6,3)==2

def test_divide_by_zero():
    try:
        divide(5,0)
    except ZeroDivisionError:
        pass
    else:
        assert False, "Expected ZeroDivisionError"