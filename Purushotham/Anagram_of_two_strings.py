s1, s2 = input("String 1: "), input("String 2: ")
print(f"Anagrams!" if sorted(s1.lower().replace(" ", "")) == sorted(s2.lower().replace(" ", "")) else "Not anagrams!")