def anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)

if __name__ == "__main__":
    str1 = input("")
    str2 = input("")
    if anagrams(str1, str2):
        print("YES")
    else:
        print("NO")