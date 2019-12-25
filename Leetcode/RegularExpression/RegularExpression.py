class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        a = (len(s) == 0)
        b = (len(p) == 0)
        if a and b:
            return True
        elif (not a) and (not b):
            return self.isMatchHelper(s, p, 0, 0)
        if (not a) and b:
            return False
        if a and (not b):
            return self.onlyStars(p)

    def isMatchHelper(self, s, p, i, j):
        """
        :param i: Location in p
        :param j: Location in s
        :return:
        """
        while i < len(p) - 1:
            if p[i] == '.':
                if p[i + 1] == '*':
                    if (i + 1) == (len(p) - 1):
                        return True
                    else:
                        while not self.isMatchHelper(s, p, i+2, j):
                            j += 1
                            if j == len(s):
                                if (i + 2) <= (len(p) - 1):
                                    return self.onlyStars(p[i + 2:])
                                else:
                                    return True
                    i += 1
                else:
                    j += 1
            else:   # Letter
                if p[i + 1] == '*':
                    if (i + 1) == (len(p) - 1):
                        while j < len(s) and s[j] == p[i]:
                            j += 1
                        i += 1
                    else:
                        while p[i] == s[j] and not self.isMatchHelper(s, p, i+2, j):
                            j += 1
                            if j == len(s):
                                if (i+2) <= (len(p) - 1):
                                    return self.onlyStars(p[i + 2:])
                                else:
                                    return True
                        i += 1
                else:
                    if s[j] == p[i]:
                        j += 1
                    else:
                        return False

            if j == len(s): # Whole string matched but pattern might still have more stuff
                if (i + 1) <= (len(p) - 1):
                    return self.onlyStars(p[i + 1:])
                else:
                    return True
            i += 1

        if not p[-1] == '*':
            if j == len(s) - 1 and (p[-1] == '.' or p[-1] == s[-1]):
                return True
        return False

    def onlyStars(self, p):
        if len(p) == 1:
            return False
        if not p[-1] == '*':
            return False
        for i in range(len(p) - 1):
            if i % 2 == 1:
                if not p[i] == '*':
                    return False
        return True

print(Solution().isMatch('abcaaaaaaabaabcabac', '.*b*'))