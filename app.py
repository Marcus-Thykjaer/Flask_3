from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
     return """
    <h1>Home</h1>
    <p>Velkommen min nettside</p>
    <ul>
        <li><a href="/aboutme">About Me</a></li>
        <li><a href="/Fisker">Fisker</a></li>
        <li><a href="/Dyr">Dyr</a></li>
    </ul>
    """

@app.route('/aboutme')
def aboutme():
     return """
    <h1>dette er min veldig fine nettside</h1>
    <p>denne nettsiden er om meg</p>
    <ul>
        <li><a href="/">Hjem</a></li>
    </ul>
    """

@app.route('/Fisker')
def Fisker():
     return """
    <h1>dette er min veldig fine nettside om kule fisker</h1>
    <p>fisker er velldig kule</p>
    <ul>
        <li><a href="/">Hjem</a></li>
    </ul>
    """

@app.route('/Dyr')
def Dyr():
     return """
    <h1>dette er min veldig fine nettside om dyr</h1>
    <p>denne nettsiden er om dyr de er ikke like kule som fisker</p>
    <ul>
        <li><a href="/">Hjem</a></li>
    </ul>
    """

if __name__ == '__main__':
    app.run(debug=True)