class WordCounter:
    def __init__(self, sentence):
        self.sentence = sentence.lower()
        self.word_count = {}

    def split_sentence(self):
        return self.sentence.split()

    def count_words(self):
        words = self.split_sentence()
        for word in words:
            if word in self.word_count:
                self.word_count[word] += 1
            else:
                self.word_count[word] = 1

    def display_counts(self):
        for word, count in self.word_count.items():
            print(f"'{word}': {count}")

    def run(self):
        self.count_words()
        self.display_counts()

def main():
    user_input = input("Enter a sentence : ")
    counter = WordCounter(user_input)
    counter.run()

main()
