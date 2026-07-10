# 211. Design Add and Search Words Data Structure


class WordDictionary:

    def __init__(self):
        self.graph = {}

    def addWord(self, word: str) -> None:
        curr = self.graph
        for i in range(len(word)):
            if word[i] not in curr:
                curr[word[i]] = [{}, False]
            if i == len(word) - 1:
                curr[word[i]][1] = True
            curr = curr[word[i]][0]

    def search(self, word: str) -> bool:
        def helper(currNode, lettersLeft):
            if not lettersLeft:
                return currNode[1]
            if lettersLeft[0] != ".":
                if lettersLeft[0] in currNode[0]:
                    return helper(currNode[0][lettersLeft[0]], lettersLeft[1:])
                else:
                    return False
            else:
                return any(helper(currNode[0][c], lettersLeft[1:]) for c in currNode[0])

        return helper([self.graph, False], word)


# addWord
# Time Complexity: O(L), where L is the length of word
# Space Complexity: O(L), where L is the length of word (worst case, new node per letter)

# search
# Time Complexity: O(26^L) worst case, where L is the length of word (branches on every dot)
# Space Complexity: O(L), where L is the length of word (max recursion depth)
