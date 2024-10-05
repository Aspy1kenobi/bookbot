from collections import Counter

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    # Get word and character counts
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    
    # Generate and print report
    report = generate_report(num_words, char_count)
    print(report)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_char_count(text):
    # Convert text to lowercase and filter out non-alphabetic characters
    text = text.lower()
    filtered_text = ''.join(char for char in text if char.isalpha())
    return Counter(filtered_text)


def generate_report(num_words, char_count):
    # Create a report with word count and character frequency
    report = []
    report.append("----- Book Analysis Report -----")
    report.append(f"Total number of words: {num_words}")
    report.append("\nCharacter frequencies:")
    
    for char, count in sorted(char_count.items()):
        report.append(f"{char}: {count}")
    
    report.append("\n----- End of Report -----")
    return "\n".join(report)


main()