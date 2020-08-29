from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    for i in range(0,1000):
        if i % 2 == 0 :continue
        print(i)
    return i
if __name__=="__main__":
    app.run()