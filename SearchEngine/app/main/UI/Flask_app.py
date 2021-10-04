from flask import Flask,redirect,url_for,render_template
from flask import *
from app.main.Controller.file_location import multiThreading

app=Flask(__name__)
# root of api
@app.route('/')
def app_interface():
    return render_template('SE_interface.html')
# submit root
@app.route('/submit',methods=['POST',"GET"])
def submit():
    marks:0
    if request.method=='POST':
        fname=request.form['search']
        result = multiThreading(fname,['E:\\','F:\\'])
    return render_template('SE_interface.html',output=result)
# main
if __name__=='__main__':
    app.run(debug=True)