import pytest
import roots_quadratic_equ as roots


def test_root_quadratic_equ():
    # input
    data = [1, 4, 4]
    correct = [-2]
    # action
    result = roots.roots_quadratic_equ(*data)
    # then
    assert result == correct


def test_root_quadratic_equ_wrong():
    # input
    data = [1, "4", 4]
    # action
    with pytest.raises(TypeError):
        result = roots.roots_quadratic_equ(*data)


def test_none_root_quadratic_equ():
    # input
    data = [4, 1, 1]
    correct = []
    # action
    result = roots.roots_quadratic_equ(*data)
    # then
    assert result == correct


def test_roots_quadratic_equ():
    # input
    data = [1, 20, 49]
    correct = [-2.86, -17.14]
    # action
    result = roots.roots_quadratic_equ(*data)
    # then
    assert result == correct

