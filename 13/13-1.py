from flask import Flask

app = Flask(__name__)

@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    luku = int(luku)
    if luku > 1:
        for i in range(2, luku):
            if (luku % i) == 0:
                vastaus = {"luku" : luku, "isPrime" : False}
                break
        else:    
            vastaus = {"luku" : luku, "isPrime" : True}
    else:
        vastaus = {"luku" : luku, "isPrime" : False}
    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)