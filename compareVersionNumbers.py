class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1_list = version1.split('.')
        version2_list = version2.split('.')
        if len(version1_list) == len(version2_list):
            pass
        elif len(version1_list) > len(version2_list):
            while len(version1_list) > len(version2_list):
                version2_list.append('0')
        elif len(version1_list) < len(version2_list):
            while len(version1_list) < len(version2_list):
                version1_list.append('0')

        return_value = self.compare_lists(version1_list, version2_list)
        return return_value

    def compare_lists(self, list1, list2):
        i = 0
        while i < len(list1):
            if list1[i] != list2[i]:
                if int(list1[i]) > int(list2[i]):
                    return 1
                elif int(list1[i]) < int(list2[i]):
                    return -1
            i += 1
        return 0

s = Solution()
s.compareVersion("1.0", "1.0.0")
