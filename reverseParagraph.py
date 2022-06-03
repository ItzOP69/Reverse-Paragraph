paragraph = input("Enter your paragraph: ")
words = paragraph.split()
reverseParagraph = []

print("Words: ",words)

for i in range(len(words)):
    reverseParagraph.append(words[len(words) - 1 - i])
    
print("Reverse: ",reverseParagraph)