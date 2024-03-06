import re

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        common_str = ""
        index = 0
        len1 = len(str1)
        len2 = len(str2)
        divisors_str1 = {}
        divisors_str2 = {}
        largest_common_divisor = 1
        divisor = 2
        while len1 != 1:
            while len1 % divisor == 0:
                try:
                    divisors_str1[divisor] += 1
                except KeyError:
                    divisors_str1[divisor] = 1
                len1 /= divisor
            divisor += 1
        divisor = 2
        # While looking for divisors, the largest common divisor will also bedetermined to save some time
        while len2 != 1:
            while len2 % divisor == 0:
                try:
                    divisors_str2[divisor] += 1
                except KeyError:
                    divisors_str2[divisor] = 1
                len2 /= divisor
            if divisor in divisors_str2 and divisor in divisors_str1:
                largest_common_divisor *= divisor ** min(divisors_str1[divisor], divisors_str2[divisor])
            divisor += 1

        print("Largest common divisor for {} and {} is {}".format(str1, str2, largest_common_divisor))    

        while str1[index] == str2[index]: 
            print("At index {}...".format(index))
            print("there is {}.".format(str1[index]))
            common_str += str1[index]
            print("Common string is now: {}.".format(common_str))
            index += 1
            if index == largest_common_divisor: break

        # print("Splitting {} by the pattern {}.".format(str1, common_str))
        # verify1 = re.split("(?={})".format(common_str), str1)
        # verify2 = re.split("(?={})".format(common_str), str2)
        # print(verify1)
        # print(verify2)
        try:
            for index in range(0, len(str1), len(common_str)):
                print("Index is {}.".format(index))
                portion = str1[index:index + len(common_str)]
                if portion == "": break
                print("Comparing {} against {}.".format(common_str, portion))
                if common_str != portion: return ""

            for index in range(0, len(str2), len(common_str)):
                portion = str2[index:index + len(common_str)]
                if portion == "": break
                print("Comparing {} against {}.".format(common_str, portion))
                if common_str != portion: return ""
        except ValueError: return ""
        # if verify1 == str1 and verify1  or verify2 == str2 and verify2 != common_str: return ""
        
        return common_str