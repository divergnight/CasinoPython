from flask import Flask, render_template,request,url_for,session,redirect
from poker_draw import draw
from VideoPokerEnv import VideoPokerEnv
from poker_earn import poker_score,earnings

app = Flask(__name__)
app.secret_key = 'ma_key'

vpoker_env = VideoPokerEnv()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def get_wallet():
    if 'age' in request.form:
        age = int(request.form['age'])
        if age < 18:
            session['age_error'] = age
            return render_template('index.html')
        else:
            session['wallet'] = int(request.form['wallet'])
            return redirect(url_for('board'))
    return render_template('index.html')



@app.route('/board')
def board():
    return render_template('board.html')

@app.route('/board', methods=['POST'])
def game():
    if 'bet' in request.form:
        bet = int(request.form['bet'])

        if bet > session['wallet']:
            session['bet_error'] = bet
            return render_template('board.html')
        else:
            session['bet'] = bet
            session['deck'],session['card'] = draw(vpoker_env.deck())
            return render_template('board.html')

    if 'change_card' in request.form:
        cards = session['card']
        choice = [x for x in cards if 'c'+str(cards.index(x)+1) not in request.form]

        no,new_cards = draw(session['deck'],choice)

        score = poker_score(new_cards)
        earn, multiplier, score_name = earnings(score, session['bet'], vpoker_env)
        session['card'] = new_cards
        session['wallet'] += earn
        session['score_name'] = score_name

        return render_template('board.html')

    if 'replay' in request.form:
        session.pop('bet',None)
        session.pop('card',None)
        return render_template('board.html')


    if 'quit' in request.form:
        session.pop('bet',None)
        session.pop('card',None)
        return redirect(url_for('quit'))

    return render_template('board.html')

@app.route('/quit')
def quit():
    return render_template('quit.html')    

@app.route('/quit', methods=['POST'])
def cashout():
    if 'cashout' in request.form:
        session.clear()
        return redirect(url_for('index'))

    return render_template('quit.html') 

if __name__== '__main__':
    app.run(debug=True)