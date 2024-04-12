# this class needs to be refactored/readability improved 

class DiaryEntry:
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("Diary entries must have a title and contents")
        self.title = title
        self.contents = contents
        self.chunk_words_no = 0
        pass

    def format(self):
        output = f"{self.title}: {self.contents}"
        return output

    def count_words(self):
        no_words = len(self.contents.split())
        return no_words

    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception("wpm cannot be 0")
        no_words = len(self.contents.split())
        return no_words/wpm

    def reading_chunk(self, wpm, minutes):
        words_in_contents = self.contents.split()
        print(f"words_in_contents: {words_in_contents}")
        no_words_read=wpm*minutes
        print(f"chunk_words_no:{self.chunk_words_no}")
        print(f"no_words_read:{no_words_read}")
        # this line is the issue 
        words_read = words_in_contents[self.chunk_words_no:self.chunk_words_no+no_words_read]
        print(f"words_read:{words_read}")
        self.chunk_words_no += no_words_read
        if self.chunk_words_no >= len(self.contents.split()):
            self.chunk_words_no =0
        print(f"chunk_words_no:{self.chunk_words_no}")
        return " ".join(words_read)
