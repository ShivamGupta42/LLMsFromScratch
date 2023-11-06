with open ("names.txt", "r") as f:
    words = f.readlines()
    for w in words[:1]:
        for ch1, ch2 in zip(w,w[1:]):
            print(ch1,ch2)


