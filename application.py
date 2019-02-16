from flask import Flask
from Boggle import Boggle
app = Flask(__name__)

@app.route('/')
def play():
    """
    To-Dos: 
        Get json pkg from the front-end as the input_file.txt
        Get words dictionary as words_alpha.txt
    """
    
    b = Boggle('words_alpha.txt', 'input_file.txt')
    b.search()
    result = f"{b.return_words}"
    return result

if __name__ == "__main__":
    app.debug = True
    app.run()