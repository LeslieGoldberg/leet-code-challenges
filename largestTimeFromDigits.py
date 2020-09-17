import itertools


class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        time_list = []
        re_string = ''
        first = None
        second = None
        first_num = 2
        second_num = 9
        third_num = 5
        fourth_num = 9
        is_time = True

        if is_time is True:
            if len(A) != 4:
                is_time = False

            first = self.test_num(first_num, A)
            if first >= 0:
                time_list.append(first)
            else:
                is_time = False

        if is_time is True:
            if first == 2:
                second = self.test_num(3, A)
            else:
                second = self.test_num(second_num, A)
            if second >= 0:
                time_list.append(second)
            elif second == -1:
                A.append(time_list.pop(0))
                first = self.test_num(1, A)
                if first >= 0:
                    time_list.append(first)
                    second = self.test_num(second_num, A)
                    if second >= 0:
                        time_list.append(second)
                    else:
                        is_time = False
                else:
                    is_time = False

        if is_time is True:
            third = self.test_num(third_num, A)
            if third >= 0:
                time_list.append(third)
            elif third == -1:
                A.append(time_list.pop(1))
                A.append(time_list.pop(0))
                first = self.test_num(1, A)
                if first >= 0:
                    time_list.append(first)
                    second = self.test_num(second_num, A)
                    if second >= 0:
                        time_list.append(second)
                        third = self.test_num(third_num,A)
                        if third >= 0:
                            time_list.append(third)
                        else:
                            is_time = False
                    else:
                        is_time = False
                else:
                    is_time = False

        if is_time is True:
            fourth = self.test_num(fourth_num, A)
            if fourth >= 0:
                time_list.append(fourth)

        if len(time_list) == 4:
            str_list = [str(num) for num in time_list]
            re_string = ''.join(str_list[0:2]) + ':' + ''.join(str_list[2:])

        return re_string

    def test_num(self, number, number_list):
        return_value = -1
        while number >= 0:
            if number in number_list:
                i = number_list.index(number)
                digit = number_list.pop(i)
                return_value = digit
                break
            else:
                number -= 1
        return return_value


class GivenSolution:
    def givenLargestTimeFromDigits(self, A: List[int]) -> str:

        max_time = -1
        # enumerate all possibilities, with the permutation() func
        for h, i, j, k in itertools.permutations(A):
            hour = h * 10 + i
            minute = j * 10 + k
            if hour < 24 and minute < 60:
                max_time = max(max_time, hour * 60 + minute)

        if max_time == -1:
            return ""
        else:
            return "{:02d}:{:02d}".format(max_time // 60, max_time % 60)


test = Solution()
test.largestTimeFromDigits([4, 2, 4, 4])
