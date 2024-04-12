from lib.diary_entry import *
import pytest
"""
given both empty title and contents 
raises an error 
"""
def test_raises_error_with_empty_title_or_contents():
    with pytest.raises(Exception) as e:
        DiaryEntry("", "")
    e_message = str(e.value)
    assert e_message == "Diary entries must have a title and contents"


"""
given a title and some contents
returns a formatted string 
"""
def test_format_string():
    diary_entry = DiaryEntry("Title1", "Some contents1")
    actual = diary_entry.format()
    assert actual == "Title1: Some contents1"

"""
given a title and some contents
returns a the total number of words in the contents as an int
"""

def test_count_words():
    diary_entry = DiaryEntry("Title1", "Some contents1")
    actual = diary_entry.count_words()
    assert actual == 2

"""
given a wpm
returns the time in minutes to read a given contents
"""
def test_reading_time():
    diary_entry = DiaryEntry("Title1", "Some contents1")
    actual = diary_entry.reading_time(2)
    assert actual == 1
"""
given a wpm of 0
returns an error
"""
def test_reading_time():
    diary_entry = DiaryEntry("Title1", "Some contents1")
    with pytest.raises(Exception) as e:
        diary_entry.reading_time(0)
    e_message = str(e.value)
    assert e_message == "wpm cannot be 0"
"""
given a wpm and a time in minutes 
returns the words that can be read in that time 
"""
def test_reading_chunk():
    diary_entry = DiaryEntry("Title1", "one two three four five six seven eight")
    actual = diary_entry.reading_chunk(7,1)
    assert actual == "one two three four five six seven"

"""
given a wpm and a time in minutes multiple times
returns the words that can be read in that time, not including those already read
"""
def test_reading_chunk_three_times():
    diary_entry = DiaryEntry("Title1", "one two three four five six seven eight nine ten")
    actual1 = diary_entry.reading_chunk(2,1)
    assert actual1 == "one two"
    actual2 = diary_entry.reading_chunk(3,1)
    assert actual2 == "three four five"
    actual3 = diary_entry.reading_chunk(3,1)
    assert actual3 == "six seven eight"
"""
given a wpm and a time in minutes 
that allows user to read more words than are left to read
user goes back to start of the contents
"""
def test_reading_chunk_goes_back_to_start():
    diary_entry = DiaryEntry("Title1", "one two three four five six seven eight nine ten")
    actual4 = diary_entry.reading_chunk(2,1)
    assert actual4 == "one two"
    actual5 = diary_entry.reading_chunk(15,1)
    assert actual5 == "three four five six seven eight nine ten"
    actual6 = diary_entry.reading_chunk(4,1)
    assert actual6 == "one two three four"
