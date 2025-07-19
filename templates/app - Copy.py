from flask  import  Flask, render_template, request
from rsa_math import generate_keypair, encrypt_rsa, decrypt_rsa

app = Flask(__name__)

p, q = 61, 53
public_key, private_key = generate_keypair(p, q)

@app.route ('/', methods=['GET', 'POST'])
def index ():
    result = ""
    if request.method == 'POST':
        text = request.form['text']
        action = request.form['action']

        if action == 'encrypt':
            cipher = encrypt_rsa(public_key, text)
            result = " ".join(map(str, cipher))
        elif action == 'decrypt':
            cipher_list = [int(x) for x in text.split()]
            plain = decrypt_rsa(private_key, cipher_list)
            result = plain

    return render_template(
        'index.html',
        public_key=public_key,
        private_key=private_key,
        result=result
    )

if __name__ == '__main__':
    app.run(debug=True)
