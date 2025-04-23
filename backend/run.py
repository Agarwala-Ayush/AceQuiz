from app import create_app

app = create_app()

@app.route("/")
def index():
    return "AceQuiz Backend is live!"


if __name__=="__main__":
    app.run()
