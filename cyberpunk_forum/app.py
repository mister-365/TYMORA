from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for sessions and flash messages

# User database
users = {
    "admin": "admin123",
    "user123": "admin123"
}

# -------- HOME / LOGIN PAGE --------
@app.route("/")
def home():
    return render_template("index.html")  # your login page


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username").strip()
    password = request.form.get("password").strip()

    if username in users and users[username] == password:
        session["username"] = username
        return redirect(url_for("dashboard"))
    else:
        flash("❌ Invalid username or password. Try again.")
        return redirect(url_for("home"))


# -------- DASHBOARD PAGE --------
@app.route("/dashboard")
def dashboard():
    if "username" in session:
        username = session["username"]
        # Pass username to cyberpunk dashboard
        return render_template("dashboard.html", username=username)
    else:
        flash("⚠ You must log in first.")
        return redirect(url_for("home"))


# -------- LOGOUT --------
@app.route("/logout")
def logout():
    session.pop("username", None)
    flash("You have been logged out.")
    return redirect(url_for("home"))


# -------- RUN APP --------
if __name__ == "__main__":
    app.run(debug=True)
