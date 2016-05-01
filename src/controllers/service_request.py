from flask import request

@app.route('/service_request', methods=['POST'])
def handle_service_request():
    
