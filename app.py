from flask  import  Flask, render_template, request
from rsa_math import generate_keypair, encrypt_rsa, decrypt_rsa
from cipher_utils import encrypt_caesar, decrypt_caesar, hash_sha256, is_integer

app = Flask(__name__)

p, q = 61, 53
rsa_public_key, rsa_private_key = generate_keypair(p, q)

@app.route ('/', methods=['GET', 'POST'])
def index ():
    result = ""
    error = ""
    algorithm = "rsa"
    shift = 3
    text = ""

    if request.method == 'POST':
        algorithm = request.form.get('algorithm', 'rsa')
        action = request.form.get('action', 'encrypt')
        text = request.form.get('text', '')
        shift = request.form.get('shift', '3')

        try:
            if algorithm == 'rsa':
                if action == 'encrypt':
                    cipher = encrypt_rsa(rsa_public_key, text)
                    result = " ".join(map(str, cipher))
                elif action == 'decrypt':
                    if not all(is_integer(x) for x in text.split()):
                        error = "Input harus angka untuk dekripsi RSA"
                    else:
                        cipher_list = [int(x) for x in text.split()]
                        plain = decrypt_rsa(rsa_private_key, cipher_list)
                        result = plain

            elif algorithm == 'caesar':
                if not shift.isdigit():
                    error = "Shift harus angka"
                else:
                    shift = int(shift)
                    if action == 'encrypt':
                        result = encrypt_caesar(text, shift)
                    elif action == 'decrypt':
                        result = decrypt_caesar(text, shift)
            elif algorithm == 'hash':
                if action == 'encrypt':
                    result = hash_sha256(text)
                else:
                    error = "Hashing tidak bisa didekripsi"
        except Exception as e:
            error = f"Error: {str(e)}"
        
    return render_template(
        'index.html',
        public_key=rsa_public_key,
        private_key=rsa_private_key,
        result=result,
        error=error,
        algorithm=algorithm,
        shift=shift,
        input_text=text
    )

if __name__ == '__main__':
    app.run(debug=True)