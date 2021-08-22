from flask import Flask, request, url_for,render_template,redirect
import sqlite3
app=Flask(__name__)

@app.route('/<name>')
def index(name="name"):
    con=sqlite3.connect('rakhi.db')
    cur = con.cursor()
    fes2='''INSERT INTO rtdb(reach) VALUES('{}');'''.format(name)
    cur.execute(fes2)
    con.commit()
    return render_template('share.html',name=name)


@app.route('/', methods = ['POST','GET'])
def home():
    if request.method == 'POST':
        yname= request.form['uname']
        print(yname)
        con=sqlite3.connect('rakhi.db')
        cur = con.cursor()
        fes='''INSERT INTO rtdb(name) VALUES('{}');'''.format(yname)
        cur.execute(fes)
        con.commit()
        return redirect(url_for('index',name=yname))
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug = True)
