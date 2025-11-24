from utils.convertion import toDigits, fromDigits
import pytest

class TestConvertion:
    def test(self):
        for i in range(1, 100000):
            value = i
            digits = toDigits(value, 255)
            print(f"value: {value}, digits: {digits}")
            assert fromDigits(digits, 255) == value

    def test_zero_base_toDigits(self):
        with pytest.raises(ValueError):
            toDigits(0, 2)
    
    def test_negative_base_toDigits(self):
        with pytest.raises(ValueError):
            toDigits(-5, 2)
            
    def test_invalid_base_fromDigits(self):
        with pytest.raises(ValueError):
            fromDigits([1,0,1], 1)
    
    def test_invalid_base_fromDigits_negative(self):
        with pytest.raises(ValueError):
            fromDigits([1,0,1], 0)

    def test_example(self):
        value = 42
        assert toDigits(value, 2) == [1, 0, 1, 0, 1, 0]
        
    def test_one(self):
        value = 42
        assert toDigits(value,3) == [1, 1, 2, 0]
 
    def test_two(self):
        value = [1, 0, 1, 0, 1, 0]
        assert fromDigits(value, 2) == 42

    def test_three(self):
        value = [1, 1, 2, 0]
        assert fromDigits(value, 3) == 42