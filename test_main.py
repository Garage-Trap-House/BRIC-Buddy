import pytest
import libraryTesting

# Bryant's test
def test_URLRequest(): 
    assert libraryTesting.requestsAttempt('https://www.youtube.com/') == 'it worked!'

