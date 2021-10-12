from mathTest import *
from numpyTest import numpyAttempt
import pytest
import mathTest
import libraryTesting

# Lan's test
def test_mathAnswer():
    assert mathTest.mathAttempt(3,5) == 0

# Bryant's test
def test_URLRequest(): 
    assert libraryTesting.requestsAttempt('https://www.youtube.com/') == 'it worked!'

#Abdul's Test
def test_abdulAttmeptPass():
    assert abdulAttempt(3,-1) == '-3.0'

#Vincent's Test
def test_numpy():
    assert numpyAttempt(2) == [0,1]