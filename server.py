from flask import Flask, request, redirect, session, flash, render_template
app = Flask(__name__)
app.secret_key = "unicorns"

####################
#Welcome to the Flask Debug Quiz
#Fix all errors, and fix the commented instructions within the index route
#Good Luck Hackers!
####################

@app.route('/') 
def index(): 
    


    if "info" not in session:
        session['info'] = ""
    
    ##########################
    #Important!
    #Session['info'] appears as an Array on the front page. 
    #Add the a loop on index.html to display each index of the array on a separate line
    #########################
    
    return render_template("index.html", info = session['info'])


@app.route("/form", methods=['POST'])
def form():

    x = request.form['First_Name']
    y = request.form['Last_Name']
    z = request.form['FaveSnack']
    print(x,y,z)
    
    if len(x) < 1 or len(y) < 1 or len(z) < 1:
        flash("Please Complete Form")
    else:
        session['info'] = [x, y, z]


    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)