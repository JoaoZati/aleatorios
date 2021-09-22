import pytest


@pytest.fixture(scope="function")
def x(request):
    return request.param * 3


@pytest.fixture(scope="function")
def y(request):
    return request.param * 2


@pytest.mark.parametrize("x, y", [("a", "b")], indirect=["x"])
def test_indirect(x, y):
    assert x == "aaa"
    assert y == "b"


@pytest.mark.parametrize("x, y", [("a", "b")], indirect=["x", "y"])
def test_indirect_2(x, y):
    assert x == "aaa"
    assert y == "bb"


@pytest.mark.parametrize(
    "x, y",
    [
        ('a', 'b'),
        ('c', 'd')
    ],
)
def test_indirect(x, y):
    assert x == "a" or x == "c"
    assert (y == "b" or y == "d")
