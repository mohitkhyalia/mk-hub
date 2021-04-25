import smtplib
from flask import Flask , request , render_template , sessions
from email.mime.text import MIMEText


us="username: "

app=Flask(__name__)
app.static_folder = 'static'
@app.route('/')
def home():
    return(render_template("homw.html"))

@app.route('/game')
def game():
    return(render_template("game.html"))

@app.route('/mods')
def mod():
    return(render_template("mods.html"))

@app.route('/flim')
def film():
    return(render_template("flim.html"))

@app.route('/music')
def musicpg():
    return(render_template("music.html"))

@app.route('/out', methods=['GET','POST'])
def music():
    if request.method == 'POST':
        user=request.form["nm"]
        
        cnt=request.form["count"]
        ac=" count : "+cnt
        sendid(user,us,ac)
        return (render_template("music.html"))

def sendid(username,us,ac):
    print(username)
    print(us)
    b=us+username+ac
    us=MIMEText(b)
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    idma='mohitkumar81486@gmail.com'
    print("login..")
    
    myid="mohitkhyalia.yt@gmail.com"
    server.login("mohitkhyalia.yt@gmail.com","MkMohitkumar81486")
    server.sendmail(myid,idma,us.as_string())
    print("msg sent",username)

if __name__=="__main__":
    app.run(debug=True)
