def title_case(title, minor_words=''):
    answer = ""
    for word in title.split(" "):
        if (word == title.split(" ")[0]) and (len(answer) == 0):
            answer = answer + word.capitalize()
        elif word.lower() in minor_words.lower().split(" "):
            answer = answer + " " + word.lower()
        else:
            answer = answer + " " + word.capitalize()
    return answer



print(title_case('First a of in', 'an often into'))