massage = input(">")
words = massage.split(' ')
emojis = {
    ":)": "😀",
    ":(": "😫",
    ":1": "😌",
    ":2": "🤣"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
