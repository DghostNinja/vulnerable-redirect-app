from flask import Flask, request, redirect, jsonify

app = Flask(__name__)

# List of vulnerable redirect parameters
VULNERABLE_PARAMS = ["url", "redirect", "next", "return", "goto"]

@app.route('/')
def home():
    return "<h2>Vulnerable Open Redirect Test App</h2><p>Use /redirect?url=http://evil.com to test.</p>"

@app.route('/redirect')
def open_redirect():
    for param in VULNERABLE_PARAMS:
        if param in request.args:
            target = request.args.get(param)
            app.logger.warning(f"Redirecting to: {target}")
            return redirect(target, code=302)
    return jsonify({"error": "No redirect parameter provided"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
  
