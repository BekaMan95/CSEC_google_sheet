class Solution:
    def sortSentence(self, s: str) -> str:
        arranged = sorted(s.split(" "), key=lambda k: k[-1])
        sentence = str()
        for i in arranged:
            sentence += i[:-1]+' '
        return sentence.strip()
