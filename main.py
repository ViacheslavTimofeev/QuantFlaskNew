from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['post', 'get'])
def index():
    if request.method == 'POST':
        name = request.form.get('str')
        fio = request.form.get('comment')
        print(name)
        print(fio)
    return render_template("Index.html")


name = """Иванов Иван Иванович
         Пётр Петров
      """
print(name)
name2 = name.split('\n')
for fio in name2:
    print(fio.rstrip())
if __name__ == '__main__':
    app.run(debug=True)
