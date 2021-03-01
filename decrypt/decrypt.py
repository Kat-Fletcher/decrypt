in_string = input("give me a phrase ")
in_string = in_string.lower()
print("")
out_string = ""
for i in range(0,26):
    for j in range(len(in_string)):
        if ord(in_string[j]) != 32:
            if (ord(in_string[j]) + i) > 122:
                out_string += chr(ord(in_string[j]) + i - 26)
            else:
                out_string += chr(ord(in_string[j]) + i)
        else:
            out_string += " "
    print(out_string)
    out_string = ""
