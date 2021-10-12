from pytest import *
from unittest.mock import patch
from main import abdul, funcToTest
from mathTest import abdulAttempt

def test_abdulAttmeptPass():
    assert abdulAttempt(3,-1) == '-3.0'
