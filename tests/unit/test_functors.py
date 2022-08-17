from contextlib import suppress

from app.domain.calculation import functors, OperationOptions, MathError


def test_add_functor():
    r = functors[OperationOptions.add](1, 2)
    assert r == 3, f'"Add" functor is not working, got {r}, expected 3'


def test_sub_functor():
    r = functors[OperationOptions.sub](1, 2)
    assert r == -1, f'"Sub" functor is not working, got {r}, expected -1'


def test_mul_functor():
    r = functors[OperationOptions.mul](5, 6)
    assert r == 30, f'"Mul" functor is not working, got {r}, expected 30'


def test_div_functor():
    r = functors[OperationOptions.div](1, 2)
    assert r == 0.5, f'"Div" functor is not working, got {r}, expected 0.5'

    with suppress(MathError):
        r = functors[OperationOptions.div](1, 0)
        assert False, f'"Div" functor is not working properly, expected error, got  {r}'
