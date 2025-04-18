from flask import Flask, render_template, request

web = Flask(__name__)

@web.route('/')
@web.route('/register')
def homepage():
    return render_template('register.html')

@web.route('/confirmation', methods=['POST'])
def register():
    if request.method == 'POST':
        n = request.form.get('name')
        c = request.form.get('city')
        p = request.form.get('phone_number')
        return render_template('confirm.html', name=n, city=c, phone_number=p)

if __name__ == "__main__":
    web.run(debug=True)
