from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    trabajos = [
        {
            'nombre': 'Desarrollo de aplicaciones web',
            'categoria': 'Desarrollo web',
            'imagen': 'img/trabajos/1.jpg'
        },
        {
            'nombre': 'Desarrollo de aplicaciones web',
            'categoria': 'Desarrollo web',
            'imagen': 'img/trabajos/2.jpg'
        },
        {
            'nombre': 'Desarrollo de aplicaciones web',
            'categoria': 'Desarrollo web',
            'imagen': 'img/trabajos/3.jpg'
        },
        {
            'nombre': 'Desarrollo de aplicaciones web',
            'categoria': 'Desarrollo web',
            'imagen': 'img/trabajos/4.jpg'
        },
        {
            'nombre': 'Desarrollo de aplicaciones web',
            'categoria': 'Desarrollo web',
            'imagen': 'img/trabajos/5.jpg'
        },
        {
            'nombre': 'Desarrollo de aplicaciones web',
            'categoria': 'Desarrollo web',
            'imagen': 'img/trabajos/6.jpg'
        },
        {
            'nombre': 'Desarrollo de aplicaciones web',
            'categoria': 'Desarrollo web',
            'imagen': 'img/trabajos/7.jpg'
        },
        {
            'nombre': 'Desarrollo de aplicaciones web',
            'categoria': 'Desarrollo web',
            'imagen': 'img/trabajos/8.jpg'
        },
    ]
    return render_template('index.html', trabajos=trabajos)

if __name__ == '__main__':
    app.run(debug=True)