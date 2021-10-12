from mathTest import mathAttempt
import pytest
import mathTest

# Lan's test
def test_mathAnswer():
    assert mathTest.mathAttempt(3,5) == 0

