# tests/test_calculator.py
import pytest


# ── Level 1: Basic Logic ───────────────────────────────────────
class TestBasicLogic:

    def test_add_zeros(self, calc):
        assert calc.add(0, 0) == 0

    def test_multiply_by_zero(self, calc):
        assert calc.multiply(0, 5) == 0

    def test_subtract_same_numbers(self, calc):
        assert calc.subtract(5, 5) == 0

    def test_divide_same_numbers(self, calc):
        assert calc.divide(5, 5) == 1.0

    def test_power_of_zero(self, calc):
        assert calc.power(0, 0) == 1   # math rule: 0^0 = 1

    def test_modulus_zero_remainder(self, calc):
        assert calc.modulus(10, 5) == 0


# ── Level 2: Float Logic ───────────────────────────────────────
class TestFloatLogic:

    def test_add_float_and_int(self, calc):
        assert calc.add(1.5, 2) == 3.5

    def test_divide_returns_float(self, calc):
        assert calc.divide(7, 2) == 3.5

    def test_multiply_floats(self, calc):
        assert calc.multiply(1.5, 2.0) == pytest.approx(3.0)

    def test_subtract_floats(self, calc):
        assert calc.subtract(5.5, 2.5) == pytest.approx(3.0)

    def test_divide_float_result(self, calc):
        assert calc.divide(1, 3) == pytest.approx(0.333, rel=1e-2)


# ── Level 2: Negative Number Logic ────────────────────────────
class TestNegativeLogic:

    def test_add_two_negatives(self, calc):
        assert calc.add(-5, -3) == -8

    def test_multiply_two_negatives(self, calc):
        assert calc.multiply(-3, -3) == 9     # negative × negative = positive

    def test_multiply_pos_and_neg(self, calc):
        assert calc.multiply(-2, 3) == -6

    def test_power_negative_base_odd_exp(self, calc):
        assert calc.power(-2, 3) == -8        # odd power keeps negative

    def test_power_negative_base_even_exp(self, calc):
        assert calc.power(-2, 2) == 4         # even power makes positive

    def test_subtract_gives_negative(self, calc):
        assert calc.subtract(3, 10) == -7

    def test_divide_negative_result(self, calc):
        assert calc.divide(-10, 2) == -5.0


# ── Level 2: Edge Cases ────────────────────────────────────────
class TestEdgeCases:

    def test_modulus_a_less_than_b(self, calc):
        assert calc.modulus(3, 5) == 3        # 3 % 5 = 3

    def test_modulus_large_numbers(self, calc):
        assert calc.modulus(1000, 7) == 6

    def test_power_zero_exponent(self, calc):
        assert calc.power(99, 0) == 1         # anything^0 = 1

    def test_power_one_exponent(self, calc):
        assert calc.power(99, 1) == 99

    def test_add_large_numbers(self, calc):
        assert calc.add(999999, 1) == 1000000

    def test_divide_by_one(self, calc):
        assert calc.divide(7, 1) == 7.0


# ── Level 2: Exception Logic ───────────────────────────────────
class TestExceptions:

    def test_divide_by_zero_raises_valueerror(self, calc):
        with pytest.raises(ValueError):
            calc.divide(10, 0)

    def test_divide_by_zero_message(self, calc):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(10, 0)

    def test_modulus_by_zero_raises_valueerror(self, calc):
        with pytest.raises(ValueError):
            calc.modulus(10, 0)

    def test_modulus_by_zero_message(self, calc):
        with pytest.raises(ValueError, match="Cannot mod by zero"):
            calc.modulus(10, 0)

    @pytest.mark.parametrize("a", [1, -1, 0, 999])
    def test_divide_by_zero_always_raises(self, calc, a):
        with pytest.raises(ValueError):
            calc.divide(a, 0)


# ── Level 3: Chained Logic ─────────────────────────────────────
class TestChainedLogic:

    def test_add_then_multiply(self, calc):
        # (2 + 3) * 4 = 20
        result = calc.multiply(calc.add(2, 3), 4)
        assert result == 20

    def test_divide_then_power(self, calc):
        # (8 / 2) ^ 3 = 64
        result = calc.power(calc.divide(8, 2), 3)
        assert result == 64.0

    def test_subtract_then_divide(self, calc):
        # (20 - 10) / 5 = 2
        result = calc.divide(calc.subtract(20, 10), 5)
        assert result == 2.0

    def test_multiply_then_add(self, calc):
        # (3 * 3) + 1 = 10
        result = calc.add(calc.multiply(3, 3), 1)
        assert result == 10

    def test_full_chain(self, calc):
        # ((10 + 5) - 3) * 2 = 24
        step1 = calc.add(10, 5)         # 15
        step2 = calc.subtract(step1, 3) # 12
        result = calc.multiply(step2, 2) # 24
        assert result == 24


# ── Parametrize: All operations together ──────────────────────
class TestParametrize:

    @pytest.mark.parametrize("a, b, expected", [
        (1,   2,    3),
        (0,   0,    0),
        (-1, -1,   -2),
        (100, 200, 300),
        (1.5, 2.5,  4.0),
    ])
    def test_add_many_inputs(self, calc, a, b, expected):
        assert calc.add(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (10,  2,  5.0),
        (9,   3,  3.0),
        (7,   2,  3.5),
        (-6,  2, -3.0),
        (100, 4, 25.0),
    ])
    def test_divide_many_inputs(self, calc, a, b, expected):
        assert calc.divide(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (2, 3,  8),
        (3, 2,  9),
        (5, 0,  1),
        (1, 100, 1),
        (-2, 2,  4),
    ])
    def test_power_many_inputs(self, calc, a, b, expected):
        assert calc.power(a, b) == expected