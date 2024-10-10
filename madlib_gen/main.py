with open("story.txt", "r") as f:
    story = f.read()

print(story,"\n\n")
words = set()
start_target_letter = "<"
end_target_letter =">"
start_word = -1


for i, char in enumerate(story):
    if char == start_target_letter:
        start_word = i
    if char == end_target_letter and start_word != -1:
        words.add(story[start_word: i + 1])
        start_word = -1
print(words)

for word in words:
    answer = input('type a word to replace ' + word + " and hit ENTER: ", )
    story = story.replace(word, answer)
print("\n\n",story)