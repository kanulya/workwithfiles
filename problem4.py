
p = '''Python is a widely used high-level programming language for general-purpose

programming, created by Guido van Rossum and first released in 1991. An interpreted

language, Python has a design philosophy that emphasizes code readability (notably

using whitespace indentation to delimit code blocks rather than curly brackets or

keywords), and a syntax that allows programmers to express concepts in fewer lines of

code than might be used in languages such as C++ or Java.
'''
def serch_t(file):
    t_words = []
    with open(file, 'r') as f:
        for word in list(f.read().split()):
            if 't' in word or 'T' in word:
                t_words.append(word)
            else:
                print('Не содержит t или T')
    return t_words
print(serch_t('python.txt'))
