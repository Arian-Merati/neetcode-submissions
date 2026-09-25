class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            letters_list = [0] * 26
            for letter in word:
                position = ord(letter) - ord("a")
                letters_list[position] += 1
            groups[tuple(letters_list)].append(word)
        return list(groups.values())

        