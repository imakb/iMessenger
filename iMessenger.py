from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Mock message database
conversations = {
    "Alice Thompson": [
        {"content": "Hey, how are you?", "sender": "Alice Thompson"},
        {"content": "I'm good, thanks! How about you?", "sender": "You"},
        {"content": "Doing well, thanks for asking!", "sender": "Alice Thompson"},
    ],
    "Bob Montgomery": [
        {"content": "Are you coming to the party?", "sender": "Bob Montgomery"},
        {"content": "Yes, I'll be there!", "sender": "You"},
    ],
    "Charlie Fitzgerald": [
        {"content": "Did you see the new MacBook M3?", "sender": "Charlie Fitzgerald"},
        {"content": "Yes, it looks amazing!", "sender": "You"},
        {"content": "I'm thinking of getting one.", "sender": "Charlie Fitzgerald"},
        {"content": "Me too!", "sender": "You"},
    ],
    "David Armstrong": [
        {"content": "That photo you posted was awesome!", "sender": "David Armstrong"},
        {"content": "Thank you!", "sender": "You"},
    ],
    "Eve Harrison": [
        {"content": "Are we still on for dinner tonight?", "sender": "Eve Harrison"},
        {"content": "Yes, see you at 7!", "sender": "You"},
    ],
    "Frank Patterson": [
        {"content": "How's the project going?", "sender": "Frank Patterson"},
        {"content": "It's on track. Should be done by next week.", "sender": "You"},
    ],
    "Grace Wallace": [
        {"content": "Can you help me with my homework?", "sender": "Grace Wallace"},
        {"content": "Of course! What do you need help with?", "sender": "You"},
    ],
}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/chat')
def chat():
    return render_template('index.html', conversations=conversations)

@app.route('/login', methods=['POST'])
def handle_login():
    return redirect(url_for('chat'))

@app.route('/logout')
def logout():
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
