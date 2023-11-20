import random

class VocabularyTrainer:
    def __init__(self):
        self.vocabulary = {}
        self.wordstolearn = []

    def add_word(self, word, translation):
        self.vocabulary[word] = translation
        self.wordstolearn.append(word)

    def start_quiz(self):
        random.shuffle(self.wordstolearn)
        correct = 0
        total = min(15, len(self.wordstolearn))

        for i in range(total):
            current_word = self.wordstolearn[i]
            
            
            while True:
                trans = input(f"Translate '{current_word}' to English: ").strip().lower()
                if trans:
                    break
                else:
                    print("Please enter a valid translation.")

            if trans == self.vocabulary[current_word]:
                print("Correct!\n")
                correct += 1
            else:
                print(f"Wrong! The correct translation is '{self.vocabulary[current_word]}'\n")

        print(f"Quiz complete. Your score: {correct}/{total}")

if __name__ == "__main__":
    trainer = VocabularyTrainer()

   #to add new word write under this cod:trainer.add_word("translate", "word")
    trainer.add_word("привіт", "hello")
    trainer.add_word("сонце", "sun")
    trainer.add_word(" здобувати", "acquire")
    trainer.add_word("демонструвати", "demonstrate")
    trainer.add_word("виправдовувати", "justify")
    trainer.add_word("оптимізувати", "optimize")
    trainer.add_word("пляшка", "bottle")
    trainer.add_word("стакан", "glass")
    trainer.add_word("тарілка", "plate")
    trainer.add_word("телефон", "phone")
    trainer.add_word("праска", "iron")
    trainer.add_word("перекладати", "translate")
    trainer.add_word("вазон", "flowerpot")
    trainer.add_word("ключ", "key")
    trainer.add_word("ноутбук", "laptop")
    trainer.add_word("штани", "pants")

    

    
    trainer.start_quiz()
