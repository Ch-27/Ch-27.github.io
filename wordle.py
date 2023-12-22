!pip install django

##chatGPT
import random
from django.http import HttpResponse
from django.shortcuts import render

# Use the specific path
file_path = "/content/drive/MyDrive/Wordle/word.txt"

def home(request):
    return render(request, 'home.html')

def game(request):
    with open(file_path, 'r') as f:
        words = [word.strip() for word in f.readlines()]

    word = random.choice(words)
    guesses = 6
    letters = []

    if request.method == 'POST':
        guess = request.POST.get('guess', '').lower()
        if guess.isalpha() and len(guess) == 1:
            if guess not in letters:
                if guess in word:
                    letters.append(guess)
                else:
                    guesses -= 1

            if set(letters) == set(word):
                return render(request, 'win.html')
            elif guesses == 0:
                return render(request, 'lose.html')

    return render(request, 'game.html', {'guesses': guesses, 'letters': letters, 'word': word})
