
import demoji

demoji.download_codes()


def replace_emojis(text):
    emoji_dict = demoji.findall(text)
    for emoji, description in emoji_dict.items():
        text = text.replace(emoji, f":{description}:")
    return text

text_with_emojis = "I love Python! 😊🐍❤️"

text_without_emojis = replace_emojis(text_with_emojis)

print(text_without_emojis)
