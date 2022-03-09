morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
alphalbet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def alpha_convert_morse(words):
    list_words = list(words.strip())
    answer = ""
    for word in list_words:
        for i in range(0,26):
            if word == alphalbet[i]:
                answer += morse[i]
    print(f"{answer}")


while True:
    words = input("Inputs the word you want to convert: ").lower()
    alpha_convert_morse(words)
    