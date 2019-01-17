# -*- coding=utf-8 -*-

class Solution(object):
    def get_next_list(self, words, begin, max_width):
        count = 0
        word_list = []
        next_begin = begin
        for i in range(begin, len(words)):
            count += len(words[i])
            if count > max_width:
                break
            count += 1 # add space
            word_list.append(words[i])
            next_begin = i + 1
        
        return word_list, next_begin
            
    def join_words(self, words, max_width):
        span_size = len(words) - 1
        if span_size == 0:
            return words[0] + ' ' * (max_width - len(words[0]))

        pure_word_len = reduce(lambda x, y : x+y, map(lambda x : len(x), words))
        space_count = max_width - pure_word_len

        avg_space_size = int(space_count / span_size)
        left_space_size = space_count % span_size

        span_space_count_list = [avg_space_size] * span_size
        for i in range(0, left_space_size):
            span_space_count_list[i] += 1

        result_str = ''
        for i in range(0, span_size):
            result_str += words[i]
            result_str += ' ' * span_space_count_list[i]
        result_str += words[span_size]

        return result_str

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        next_begin = 0

        while next_begin < len(words):
            word_list, next_begin = self.get_next_list(words, next_begin, maxWidth)
            if next_begin < len(words):
                result.append(self.join_words(word_list, maxWidth))
            else:
                last_str = ' '.join(word_list)
                last_str += ' ' * (maxWidth - len(last_str))
                result.append(last_str)

        return result


if __name__ == "__main__":
    words = ["Science","is","what","we","understand","well","enough","to","explain",
            "to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth = 20
    s = Solution()
    print s.fullJustify(words, maxWidth)