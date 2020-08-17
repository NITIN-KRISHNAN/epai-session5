import session5

def test_squared_power_list():
    res = session5.squared_power_list(2, start=0,end=5,repetitions=5)
    r = [1.0, 2.0, 4.0, 8.0, 16.0,32.0]
    print(r, res, res == [1.0, 2.0, 4.0, 8.0, 16.0,32.0])
    assert res == [1.0, 2.0, 4.0, 8.0, 16.0,32.0], "fail test_squared_power_list"