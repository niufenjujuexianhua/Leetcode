class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        dt = {v : i for i, v in enumerate(order)}

        for a, b in zip(words, words[1:]):
            if a.startswith(b) and len(a) > len(b):
                return False

            for ca, cb in zip(a, b):
                if ca != cb:
                    if dt[ca] > dt[cb]:
                        return False
                    break
        return True