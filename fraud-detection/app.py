from flask import Flask,render_template,request
import model
app=Flask(__name__)

@app.route('/' ,methods=["GET","POST"])
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/about',methods=["GET","POST"])
def about():
    return render_template("about.html")

@app.route('/sub',methods=["GET","POST"])
def sub():
    if request.method=="POST":
        file=request.files['data']
        file_path='dataset/'+file.name
        file.save('dataset/' + file.name)

    o,f,tra,tea=model.predictions(path=file_path)
    return render_template("sub.html", o=o,f=f,tra=tra,tsa=tea)

if __name__=="__main__":
    app.run(debug=True)