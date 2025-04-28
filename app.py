from flask import Flask, render_template, request, redirect, session, url_for, make_response
from flask import send_from_directory
app = Flask(__name__)
app.secret_key = 'super-secret-key'  # Change this in production

# Actual decoded flags
LEVEL_FLAGS = {
    1: 'flag{Base64_hidden}',
    2: 'flag{Caesar_cither}',
    3: 'flag{ROT13_is_forel}',
    4: 'flag{hidden_in_html}',
    5: 'flag{hidden_in_css}',
    6: 'flag{invisible_text}',
    7: 'flag{found_in_header}',
    8: 'flag{hidden_in_robots}',
    9: 'flag{url_encoded}',
    10: 'flag{css_hidden_flag}'
}


@app.route('/robots.txt')
def robots_txt():
    return send_from_directory(app.static_folder, 'robots.txt')

@app.route('/')
def index():
    session.clear()
    return render_template('index.html')

@app.route('/', methods=['POST'])
def level1():
    flag = request.form.get('flag')
    if flag == LEVEL_FLAGS[1]:
        session['level'] = 2
        return redirect(url_for('level2'))
    return render_template('index.html', message='Incorrect. Try again.')

@app.route('/level2')
def level2():
    if session.get('level') != 2:
        return redirect(url_for('index'))
    return render_template('level2.html')

@app.route('/level2', methods=['POST'])
def level2_post():
    flag = request.form.get('flag')
    if flag == LEVEL_FLAGS[2]:
        session['level'] = 3
        return redirect(url_for('level3'))
    return render_template('level2.html', message='Nope! Try again.')

@app.route('/level3')
def level3():
    if session.get('level') != 3:
        return redirect(url_for('index'))
    return render_template('level3.html')

@app.route('/level3', methods=['POST'])
def level3_post():
    flag = request.form.get('flag')
    if flag == LEVEL_FLAGS[3]:
        session['level'] = 4
        return redirect(url_for('level4'))
    return render_template('level3.html', message='Wrong flag.')

@app.route('/level4')
def level4():
    if session.get('level') != 4:
        return redirect(url_for('index'))
    return render_template('level4.html')

@app.route('/level4', methods=['POST'])
def level4_post():
    flag = request.form.get('flag')
    if flag == LEVEL_FLAGS[4]:
        session['level'] = 5
        return redirect(url_for('level5'))
    return render_template('level4.html', message='Wrong flag.')

@app.route('/level5')
def level5():
    if session.get('level') != 5:
        return redirect(url_for('index'))
    return render_template('level5.html')

@app.route('/level5', methods=['POST'])
def level5_post():
    flag = request.form.get('flag')
    if flag == LEVEL_FLAGS[5]:
        session['level'] = 6
        return redirect(url_for('level6'))
    return render_template('level5.html', message='Wrong flag.')

@app.route('/level6')
def level6():
    if session.get('level') != 6:
        return redirect(url_for('index'))
    return render_template('level6.html')

@app.route('/level6', methods=['POST'])
def level6_post():
    flag = request.form.get('flag')
    if flag == LEVEL_FLAGS[6]:
        session['level'] = 7
        return redirect(url_for('level7'))
    return render_template('level6.html', message='Wrong flag.')

@app.route('/level7')
def level7():
    if session.get('level') != 7:
        return redirect(url_for('index'))
    resp = make_response(render_template('level7.html'))
    resp.headers['X-Flag'] = LEVEL_FLAGS[7]  # Set flag in HTTP header
    return resp

@app.route('/level7', methods=['POST'])
def level7_post():
    flag = request.form.get('flag')
    if flag == LEVEL_FLAGS[7]:
        session['level'] = 8
        return redirect(url_for('level8'))
    return render_template('level7.html', message='Wrong flag.')

@app.route('/level8')
def level8():
    if session.get('level') != 8:
        return redirect(url_for('index'))
    return render_template('level8.html')

@app.route('/level8', methods=['POST'])
def level8_post():
    flag = request.form.get('flag')
    if flag == LEVEL_FLAGS[8]:
        session['level'] = 9
        return redirect(url_for('level9'))
    return render_template('level8.html', message='Wrong flag.')

@app.route('/robots.txt.txt')
def robots():
    return "User-agent: *\nDisallow: /supersecretpath\n", 200, {'Content-Type': 'text/plain'}

@app.route('/supersecretpath')
def supersecretpath():
    return "You found it! The flag is: flag{robots_clue}"

@app.route('/level9', methods=['GET', 'POST'])
def level9():
    if request.method == 'POST':
        flag = request.form.get('flag')
        if flag == LEVEL_FLAGS[9]:
            session['level'] = 10
            return redirect(url_for('level10'))  # Assuming level10 exists
        else:
            return render_template('level9.html', message='Wrong flag. Try again.')
    return render_template('level9.html')

@app.route('/level10')
def level10():
    if session.get('level') != 10:
        return redirect(url_for('index'))
    return render_template('level10.html')

@app.route('/level10', methods=['POST'])
def level10_post():
    flag = request.form.get('flag')
    if flag == LEVEL_FLAGS[10]:
        session.clear()
        return "<h2>🎉 Congratulations! You've completed all levels! 🎯</h2>"
    return render_template('level10.html', message='Wrong flag.')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
