from three_word_markov import Markov
import re
import sys
from ast import literal_eval
import io

# prep the text for training
def prep_text(text):
    # remove urls
    # https://stackoverflow.com/questions/11331982/how-to-remove-any-url-within-a-string-in-python
    text = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', text)
    return text.replace('=', '')

# read a file for its text
def read_file(filename):
    with io.open(filename, "r", encoding='utf8') as file:
        contents = file.readlines()
        contents = [l.replace('\n', '\n ') for l in contents]

    a = ""
    for line in contents:
        a += repr(line)
    a = a.replace('"', '').replace("'", "")
    return a

def prep_output(output):
    out = output.strip().replace(" .", ".").split()
    out[0] = out[0].capitalize()
    for index in range(len(out)):
        if (index != 0):
            if out[index-1][-1] in [".","!","?"]:
                caps = out[index].capitalize()
                out[index] = caps
    s = ''
    for w in out:
        s += w + ' '
    out = s.strip()
    if out[-1] not in [".", ",",":","!","?"]:
        out += "."
    return out.replace(' i ', ' I ')

text = prep_text(read_file('kendricklamar.txt'))

m = Markov(text, 3)
length = (25 if len(sys.argv)<2 else int(sys.argv[1]))

print("---\n{}\n---".format(prep_output(m.build_text(length))))
