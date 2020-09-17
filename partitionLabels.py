# A string S of lowercase English letters is given. We want to partition this
# string into as many parts as possible so that each letter appears in
# at most one part, and return a list of integers representing the size of these parts.
# S will have length in range [1, 500].
# S will consist of lowercase English letters ('a' to 'z') only.

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        string_length_list = []
        string_length = 0

        while string_length < len(S):
            substring_length = self.sub_string_creator(S[string_length], S)
            string_length_list.append(substring_length)
            string_length += substring_length

        if sum(string_length_list) == len(S):
            return string_length_list
        else:
            return 'Error'

    def sub_string_creator(self, first_letter, string_of_letters):
        first_letter_of_substring_index = string_of_letters.index(first_letter)
        max_rindex = string_of_letters.rindex(first_letter)
        substring = string_of_letters[first_letter_of_substring_index: max_rindex + 1]
        checked_rindex = self.check_substring(substring, string_of_letters)

        while max_rindex < checked_rindex:
            max_rindex = checked_rindex
            substring = string_of_letters[first_letter_of_substring_index: max_rindex + 1]
            checked_rindex = self.check_substring(substring, string_of_letters)

        substring = string_of_letters[first_letter_of_substring_index: checked_rindex + 1]

        return len(substring)

    def check_substring(self, substring, string_of_letters):
        max_length = string_of_letters.rindex(substring[-1])
        for letter in substring:
            if string_of_letters.rindex(letter) > max_length:
                max_length = string_of_letters.rindex(letter)

        return max_length


class GivenSolution(object):
    def givenPartitionLabels(self, given_string):
        dictionary_of_last_indexes = {letter: index for index, letter in enumerate(given_string)}
        j = anchor = 0
        ans = []
        for index, letter in enumerate(given_string):
            j = max(j, dictionary_of_last_indexes[letter])
            if index == j:
                ans.append(index - anchor + 1)
                anchor = index + 1

        return ans


test = GivenSolution()
test.givenPartitionLabels("ababcbacadefegdehijhklij")