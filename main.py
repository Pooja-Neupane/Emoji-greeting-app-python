from flask import Flask, request, render_template_string

app = Flask(__name__)

# Template for the form
form_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Flask Greeting App</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light text-center p-5">
    <div class="container">
        <h1 class="mb-4">👋 Submit Your Name</h1>
        <form method="POST" action="/form" class="w-50 mx-auto border p-4 rounded shadow bg-white">
            <div class="mb-3">
                <label for="name" class="form-label">Enter Your Name:</label>
                <input type="text" id="name" name="name" class="form-control" placeholder="Your Name" required>
            </div>
            <input type="submit" value="Greet Me" class="btn btn-primary w-100">
        </form>
        <a href="/" class="btn btn-link mt-3">Back to Home</a>
    </div>
</body>
</html>
'''

# Template for the greeting
greet_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Greeting</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-success-subtle text-center p-5">
    <div class="container">
        <h1 class="text-success">Hello, {{ name }}! 🎉</h1>
        <p class="lead">Welcome to the Flask Greeting App!</p>
        <a href="/form" class="btn btn-outline-primary mt-3">Try Again</a>
    </div>
</body>
</html>
'''

@app.route("/")
def home():
    return "<h1 style='text-align:center;'>Welcome to the Flask Greeting App</h1><div style='text-align:center;'><a href='/form'>Go to Form</a></div>"

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form['name']
        return render_template_string(greet_template, name=name)
    return render_template_string(form_template)

if __name__ == "__main__":
    app.run(debug=True)
