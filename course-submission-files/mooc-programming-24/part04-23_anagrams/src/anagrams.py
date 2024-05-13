# Write your solution here
def anagrams(string1, string2):
    return sorted(string1.lower()) == sorted(string2.lower())