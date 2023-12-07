ruSTRDictionary:list[str] = input("Enter string on Russian: ").lower().split()
ruenDictionary = {"я":"i", "люблю":"love", "людей":"people", "очень":"so", "сильно":"much", "навеки":"forever"}
enSTRDictionary = ""
for w in ruSTRDictionary:
    try:
        enSTRDictionary += ruenDictionary[w] + " "
    except:
        enSTRDictionary += w + " "

print(enSTRDictionary.capitalize())