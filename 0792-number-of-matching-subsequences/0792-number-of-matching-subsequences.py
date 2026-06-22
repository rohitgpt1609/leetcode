from collections import defaultdict

class Solution:
    def numMatchingSubseq(self, s, words):
        buckets = defaultdict(list)

        for word in words:
            buckets[word[0]].append((word, 0))

        count = 0

        for char in s:
            current = buckets[char]
            buckets[char] = []

            for word, index in current:
                index += 1

                if index == len(word):
                    count += 1
                else:
                    buckets[word[index]].append((word, index))

        return count