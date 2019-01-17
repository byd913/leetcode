# -*- coding=utf-8 -*-

import unittest
from full_justify import Solution

class TestFullJustify(unittest.TestCase):
    def test_case1(self):
        solution = Solution()
        words = ["This", "is", "an", "example", "of", "text", "justification."]
        maxWidth = 16
        expect_result = [
            "This    is    an",
            "example  of text",
            "justification.  "
        ]

        result = solution.fullJustify(words, maxWidth)
        self.assertListEqual(result, expect_result)
            
    def test_case2(self):
        solution = Solution()
        words = ["Science","is","what","we","understand","well","enough","to","explain",
                "to","a","computer.","Art","is","everything","else","we","do"]
        maxWidth = 20
        expect_result = [
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  "
        ]

        result = solution.fullJustify(words, maxWidth)
        self.assertListEqual(result, expect_result)

    def test_case3(self):
        solution = Solution()
        words = ["What","must","be","acknowledgment","shall","be"]
        maxWidth = 16
        expect_result = [
            "What   must   be",
            "acknowledgment  ",
            "shall be        "
        ]

        result = solution.fullJustify(words, maxWidth)
        self.assertListEqual(result, expect_result)
    

if __name__ == "__main__":
    unittest.main()