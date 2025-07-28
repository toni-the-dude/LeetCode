class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        key = key.replace(" ", "")
        key = dict.fromkeys(key)
        i = 97

        for k in key.keys():
            key[k] = chr(i)
            i += 1

        decoded = ""

        for c in message:
            if c == " ": decoded += " "
            else: decoded += key[c]

        return decoded