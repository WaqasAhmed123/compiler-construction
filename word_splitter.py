from docx import Document
import string

def custom_word_splitter(text):
    words = []
    current_word = ""

    for char in text:
        # If the character is a letter or a digit, add it to the current word
        if char.isalnum() or char in string.punctuation:
            current_word += char
        else:
            # If the current word is not empty, add it to the list of words
            if current_word:
                words.append(current_word)
                current_word = ""

    # Add the last word if the text ends with a letter or digit
    # if current_word:
    #     words.append(current_word)

    return words

# Read Word document content using open
document_path = "word_splitter_doc.docx"
with open(document_path, 'rb') as file:
    doc = Document(file)
    text_from_document = ""
    for paragraph in doc.paragraphs:
        text_from_document += paragraph.text + "\n"


class Token:
    



# Use the custom word splitter
result = custom_word_splitter(text_from_document)
print(result)
