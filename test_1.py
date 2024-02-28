import pytest


@pytest.mark.parametrize("a, b, expected_result",
                         [
                             (1, 2, 3),
                             (3, 4, 7),
                             (5, 6, 11)
                         ])
def test_add(a, b, expected_result):
    assert a + b == expected_result


@pytest.mark.parametrize("a, b, expected_result",
                         [
                             (1, 2, -1),
                             (3, 4, -1),
                             (5, 6, -1)
                         ])
def test_min(a, b, expected_result):
    assert a - b == expected_result


@pytest.mark.parametrize("a, b, expected_result",
                         [
                             (1, 2, 0.5),
                             (3, 4, 0.75),
                             (6, 6, 1)
                         ])
def test_div(a, b, expected_result):
    assert a / b == expected_result


@pytest.mark.parametrize("a, b, expected_result",
                         [
                             (1, 2, 2),
                             (3, 4, 12),
                             (6, 6, 1)
                         ])
def test_div(a, b, expected_result):
    assert a * b == expected_result
