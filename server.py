from flask import Flask, request, redirect, session, flash, render_template
app = Flask(__name__)
app.secret_key = "unicorns"
print(__name__)

####################
#Welcome to the Flask Debug Quiz
#Fix all errors, and fix the commented instructions within the index route
#Good Luck Hackers!
####################

@app.route('/', methods=['GET']) 
def index(): 
    if "info" not in session:
        session['info'] = ""
        print("dojo")
    else:
        session['info'] = session['info']
    return render_template("index.html", info = session['info'])
    ##########################
    #Important!
    #Session['info'] appears as an Array on the front page. 
    #Add the a loop on index.html to display each index of the array on a separate line
    #########################

@app.route('/form', methods = ['POST'])
def form():
    if len(request.form['FirstName']) < 1 or len(request.form['LastName']) < 1:
        flash("Please Complete Form")
        return redirect('/')
    else:
        session['info'] = [request.form["FirstName"], request.form['LastName'], request.form['FaveSnack']]
        return render_template("index.html", info = session['info'])
    


if __name__=="__main__":
    app.run(debug=True)