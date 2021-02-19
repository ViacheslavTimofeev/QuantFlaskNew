from flask import Flask, render_template, request

app = Flask(__name__)




@app.route('/', methods=['post', 'get'])
def index():
    if request.method == 'POST':
        name = request.form.get('str')
        fio = request.form.get('comment')
        print(name)
        print(fio)
        name2 = name.split()
        print(name2)
        for fname in name2:
            print(fname.rstrip())
    return render_template("Index.html")



if __name__ == '__main__':
    app.run(debug=True)
