from flask import Flask, render_template, request, session
from api import ask, append_interaction_to_chat_log

app = Flask(__name__)
app.config['SECRET_KEY'] = '89djhff9lhkd93'

@app.route('/')
def index():
    session['chat_log'] = None
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_question():
    question = request.form['question']
    chat_log = session.get('chat_log')
    answer = ask(question, chat_log)
    session['chat_log'] = append_interaction_to_chat_log(question, answer, chat_log)
    return answer

if __name__ == '__main__':
    app.run(debug=True)

