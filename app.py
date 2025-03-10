rom flask import Flask, request, redirect

app = Flask(__name__)

# Common redirect parameters to test
REDIRECT_PARAMS = ["url", "redirect", "next", "return", "goto"]

@app.route('/')
def home():
    return """
    <h2>Vulnerable Open Redirect Test App</h2>
    <p>Try visiting:</p>
    <ul>
        <li><a href="/redirect?url=http://evil.com">/redirect?url=http://evil.com</a></li>
        <li><a href="/redirect?redirect=http://evil.com">/redirect?redirect=http://evil.com</a></li>
        <li><a href="/redirect?next=http://evil.com">/redirect?next=http://evil.com</a></li>
        <li><a href="/redirect?return=http://evil.com">/redirect?return=http://evil.com</a></li>
        <li><a href="/redirect?goto=http://evil.com">/redirect?goto=http://evil.com</a></li>
    </ul>
    """

@app.route('/redirect')
def vulnerable_redirect():
    for param in REDIRECT_PARAMS:
        if param in request.args:
            target = request.args.get(param)
            if target:
                return redirect(target)
    return "No valid redirect parameter provided", 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
