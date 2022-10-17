class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # if len(sentence)<26:
        #     return False
        # alpha = [-1]*26
        # for s in sentence:
        #     alpha[ord(s)-97] = 0
        # if -1 in alpha:
        #     return False
        # return True
        return len(set(sentence)) == 26
        