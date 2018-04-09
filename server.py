from flask import Flask, request, redirect, session, flash, render_template
app = Flask(__name__)
app.secret_key = "unicorns"

####################
#Welcome to the Flask Debug Quiz
#Fix all errors, and fix the commented instructions within the index route
#Good Luck Hackers!


# Answers
# render template not defined
# f in flash message
# bad request error = name was missing an underscore
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


@app.route("/form", methods=['POST', 'GET'])
def theForm():
    
    if len(request.form['First_Name']) < 1 or len(request.form['Last_Name']) < 1:
        flash(f"Please Complete Form")
    else:
        session['info'] = [request.form["First_Name"], request.form['Last_Name'], request.form['FaveSnack']]


    return redirect('/')



app.run(debug=True)