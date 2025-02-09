from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='modul-8')

@app.route('/mypage/me')
def about_me():
    return render_template('about.html')

@app.route('/mypage/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        message = request.form.get('message')
        with open("messages.txt", "a") as file:
            file.write(message + "\n")
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=False)
