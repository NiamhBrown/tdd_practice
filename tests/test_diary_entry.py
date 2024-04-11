from lib.diary_entry import *
import pytest

def test_25_word_text():
    actual = reading_time("hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello") 
    result = "0.125 minutes"
    assert result == actual

def test_50_word_text():
    actual = reading_time("hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello hello") 
    result = "0.25 minutes"
    assert result == actual

def test_empty_string_returns_prompt():
    actual = reading_time("")
    result = 'You did not enter a text.'
    assert actual == result 

def test_input_not_string():
    actual = reading_time(5)
    result = 'Input is not a string'
    assert actual == result 