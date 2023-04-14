class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        window_len = len(words) * word_len
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        
        res = []
        for i in range(len(s) - window_len + 1):
            cur_count = {}
            j = 0
            while j < window_len:
                cur_word = s[i+j:i+j+word_len]
                if cur_word not in word_count:
                    break
                cur_count[cur_word] = cur_count.get(cur_word, 0) + 1
                if cur_count[cur_word] > word_count[cur_word]:
                    break
                j += word_len
            if j == window_len:
                res.append(i)
        
        return res