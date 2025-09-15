# tests/test_quick_check.py
def test_math():
    assert 2 + 2 == 4, "Basic math seems to have failed!"

def test_hello_world():
    message = "Hello, Automation Engineer!"
    assert "Engineer" in message