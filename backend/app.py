from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "bienvenue sur le backend de ParkIno !"

if __name__ == '__main__':
    app.run(debug=True)
