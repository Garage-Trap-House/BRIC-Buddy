from mathTest import *
import pytest
import mathTest
import libraryTesting

# Lan's test
def test_mathAnswer():
    assert mathTest.mathAttempt(3,5) == 0
import libraryTesting

# Bryant's test
def test_URLRequest(): 
    assert libraryTesting.requestsAttempt('https://www.youtube.com/') == 'it worked!'

def test_abdulAttmeptPass():
    assert abdulAttempt(3,-1) == '-3.0'
