with open("file.txt", 'r') as file:
    content = file.read()
    word = content.split()
    print(f"Word count = {len(word)}")
    