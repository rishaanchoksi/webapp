from flask import Flask, render_template, request, session, redirect, url_for


app = Flask(__name__)

app.config["SECRET_KEY"] = "string"

@app.errorhandler(404)
def not_found(e):
    return render_template("notfound.html")

@app.route("/")
@app.route("/home")
def hello_world():
    return "<p>Welcome to Rishaans web app</p>"

@app.route('/test', methods=['GET', 'POST'])
def test():
    return redirect("/home")

@app.route('/test2', methods=['GET', 'POST'])
def test2():
    return redirect(url_for("registration"))

@app.route("/aboutme")
def aboutme():
    name = "Rishaan"
    session["name"] = name
    session.clear()
    #session = {"name": "Rishaan"}
    return render_template("aboutme.html")

@app.route("/alto")
def alto():
    return render_template("alto.html")

@app.route("/upper")
def upper():
    return render_template("upper.html")

@app.route("/validate_upper")
def validate_upper():
    word = request.args["string"]
    upper=""


    for character in word:
        if character.islower() == True:
            ord_character = ord(character) - 32
            chr_character = chr(ord_character)
            upper = upper+chr_character

        else: 
            upper = upper + character
            
    return render_template("upper.html", result=upper)



@app.route("/lower")
def lower():
    return render_template("lower.html")

@app.route("/validate_lower")
def validate_lower():
    word = request.args["string"]
    lower=""

    for character in word:
        if character.isupper() == True:
            ord_character = ord(character) + 32
            chr_character = chr(ord_character)
            lower = lower+chr_character

        else:
            lower=lower+character

    return render_template("lower.html", result=lower)

@app.route("/evenorodd")
def evenorodd():
    return render_template("evenorodd.html")

@app.route("/validate_num")
def validate_num():
    num = int(request.args["number"])

    if num%2==0:
        result="even"
    else:
        result="odd"
    


    return render_template("evenorodd.html", result=result)

@app.route("/eligibility")
def eligibletovote():
    return render_template("eligibletovote.html")

@app.route("/validate_eligibility")
def validate_eligibility():
    age = int(request.args["age"])

    if age > 18 or age == 18:
        result="Eligible to vote"

    else: 
        result="Only 18+ are eligible to vote"

    return render_template("eligibletovote.html", result=result)





@app.route("/vorc", methods=["POST", "GET"])
def vowelorconsonant():
    result=''
    if request.method=="POST":
        letter = (request.form["letter"])

        vowels=("a", "e", "i", "o", "u")

        if letter.lower() in vowels:
            result="letter is a vowel"

        else: 
            result="letter is a consonant"
    return render_template("vorc.html", result=result)

@app.route('/reverse', methods=["POST", "GET"])
def reversestring():
    reverse_string=""

    if request.method=="POST":
        string=request.form.get("string")

        for i  in string:
            reverse_string=i + reverse_string

    return render_template("reverse.html", result=reverse_string)


@app.route('/sign', methods=["POST", "GET"])
def sign():
    sign=""
    if request.method=="POST":

        month = request.form.get("months")
        day = int(request.form.get("date"))

        if month == "Jan":
            if day >= 1 and day <= 19:
                sign="capricorn"
            else:
                sign="aquarius"
            
        elif month == "Feb":
            if day >= 1 and day <= 19:
                sign="aquarius"
            else:
                sign="pisces"

        elif month == "Mar":
            if day >= 1 and day <= 20:
                sign="pisces"
            else:
                sign="aries"

        elif month == "Apr":
            if day >= 1 and day <= 20:
                sign="aries"
            else:
                sign="taurus"

        elif month == "May":
            if day >= 1 and day <= 20:
                sign="taurus"
            else:
                sign="gemini"

        elif month == "Jun":
            if day >= 1 and day <= 20:
                sign="gemini"
            else:
                sign="cancer"

        elif month == "Jul":
            if day >= 1 and day <= 22:
                sign="cancer"
            else:
                sign="leo"

        elif month == "Aug":
            if day >= 1 and day <= 22:
                sign="leo"
            else:
                sign="virgo"

        elif month == "Sep":
            if day >= 1 and day <= 22:
                sign="virgo"
            else:
                sign="libra"

        elif month == "Oct":
            if day >= 1 and day <= 22:
                sign="libra"
            else:
                sign="scropio"

        elif month == "Nov":
            if day >= 1 and day <= 22:
                sign="scorpio"
            else:
                sign="sagittarius"

        elif month == "Dec":
            if day >= 1 and day <= 21:
                sign="sagittarius"
            else:
                sign="capricorn"

    return render_template("sign.html", sign=sign)

@app.route('/shipping', methods=["POST", "GET"])
def shipping():
    price=0
    if request.method=="POST":

        weight = float(request.form.get("weight"))

        if weight == 20:
            price = 10*weight
            
        elif weight >= 10 and weight < 20:
            price = 12*weight

        elif weight >= 1 and weight < 10:
            price = 14*weight

        elif weight < 1:
            price = 0 

        else:
            price = "We do not deliver packages over 20kg"

    return render_template ("shipping.html", price="The total cost is $" + str(price))


usernames={"user1@gmail.com" : "user123"}
@app.route('/registration', methods=["POST", "GET"])
def registration():
    if request.method=="GET":
        return render_template("registration.html")
    if request.method=="POST":
        name=request.form.get("name")
        email=request.form.get("email")
        password=request.form.get("password")
        confirmpassword=request.form.get("confirmpassword")
        phonenumber=request.form.get("phonenumber")
        gender=request.form.get("gender")
        zipcode=request.form.get("zipcode")
        if  email in usernames:
            message=("email is already taken")
            return render_template("login.html", message=message)
        else:
            if password==confirmpassword:
                message="registration succesful"
                return render_template("login.html", message=message)

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("password")
        password_db=usernames.get(email)
        if password_db==None:
            message="invalid credentials"
            return render_template("login.html", message=message)
        elif password==password_db:
            return render_template("homepage1.html")
        elif password !=password_db:
            message="invalid credentials"
            return render_template("login.html", message=message)
    
@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    if request.method=="GET":
        return render_template("calculator.html")
    if request.method=="POST":
        num1=int(request.form.get("num1"))
        num2=int(request.form.get("num2"))
        operator=request.form.get("operator")
        result=0
        if operator=="add":
            result=num1 + num2
        if operator=="subtract":
            result=num1 - num2
        if operator=="divide":
            result=num1/num2
        if operator=="multiply":
            result=num1*num2
        print(result)
        return render_template("calculator.html", result=result)

@app.route('/bmi', methods=['GET', 'POST'])
def bmi():
    bodytype=""
    bmi=0
    if request.method=="GET":
        return render_template("bmi.html")
    if request.method=="POST":
        weight=float(request.form.get("weight"))
        session["weight"] = weight  
        height=float(request.form.get("height"))
        bmi= weight/(height*height)
        if bmi < 18.5:
            bodytype="underweight"
        if bmi >= 18.5 and bmi < 25:
            bodytype="healthy"
        else:
            bodytype="overweight"
        bmi="%.1f"%bmi
        
    
    return render_template("bmi.html", bmi="Your bmi is " + str(bmi) + "and your body type is " + bodytype)

@app.route('/planetweight', methods=['GET', 'POST'])
def planetweight():
    if request.method=="GET":
        return render_template("planetweight.html")
    if request.method=="POST":
        weight = session.get("weight")
        planetweight=0
        planet = request.form.get("planet")
        if planet == "mercury":
            planetweight = weight*0.38
        elif planet == "venus":
            planetweight= weight*0.91
        elif planet == "mars":
            planetweight=weight*0.38
        elif planet == "jupiter":
            planetweight=weight*2.34
        elif planet == "saturn":
            planetweight=weight*1.06
        elif planet == "uranus":
            planetweight = weight*0.92
        elif planet == "neptune":
            planetweight= weight*1.19

        return render_template("planetweight.html", planetweight="Your weight on " + planet + "is " + str(planetweight))


@app.route('/q1', methods=['GET', 'POST'])
def q1():
    if request.method=="GET":
        return render_template("quiz_app/q1.html")
    attempted_questions = session.get("attempted_questions", [])
    print(attempted_questions)
    if "q1" in attempted_questions:
        return render_template("error.html", message="question is already attempted")
    attempted_questions.append("q1")
    session["attempted_questions"] = attempted_questions
    score = session.get("score", 0)
    print(score)
    if request.method=="POST":
        answer=request.form.get("answer")
        if answer=="HTML":
            result="correct"
            score = score + 1
        else:
            result="wrong"
        session["score"] = score
    return render_template("quiz_app/q1.html", result="Your answer is " + result)

@app.route('/q2', methods=['GET', 'POST'])
def q2():
    if request.method=="GET":
        return render_template("quiz_app/q2.html")
    attempted_questions = session.get("attempted_questions", [])
    print(attempted_questions)
    if "q2" in attempted_questions:
        return render_template("error.html", message="question is already attempted")
    attempted_questions.append("q2")
    session["attempted_questions"] = attempted_questions
    score = session.get("score", 0)
    print(score)
    
    

    if request.method=="POST":
        answer=request.form.get("answer")
        if answer=="Python":
            result="correct"
            score = score + 1       
        else:
            result="wrong"
        session["score"] = score
    return render_template("quiz_app/q2.html", result="Your answer is " + result)
    

if __name__ == "__main__":
    app.run(debug=True)

# 1 input from viewpage
# 2 data sent to server for processing
# 3 generate output
# 4 show the output on viewpage 
