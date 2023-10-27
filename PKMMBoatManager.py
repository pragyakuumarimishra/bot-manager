from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a list of allowed and blocked IP addresses
allowed_ips = ["127.0.0.1"]
blocked_ips = []

# Middleware to check if the request is coming from an allowed IP
@app.before_request
def before_request():
    client_ip = request.remote_addr
    if client_ip in blocked_ips:
        return jsonify({"error": "Access forbidden for your IP address."}), 403

# Route for handling normal requests
@app.route('/')
def index():
    return "Welcome to the bot-managed application!"

# Route for adding an IP address to the allowed list
@app.route('/allow_ip/<ip>', methods=['POST'])
def allow_ip(ip):
    allowed_ips.append(ip)
    return jsonify({"message": f"IP address {ip} added to the allowed list."})

# Route for blocking an IP address
@app.route('/block_ip/<ip>', methods=['POST'])
def block_ip(ip):
    blocked_ips.append(ip)
    return jsonify({"message": f"IP address {ip} added to the blocked list."})

if __name__ == '__main__':
    app.run(debug=True)
