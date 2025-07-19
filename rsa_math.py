import math

def gcd(a,b):
    if a == 0 and b == 0:
      raise ValueError("gcd(0,0) is undefined")
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, x1, y1    = extended_gcd(b, a % b)
        g, x, y = g, y1, x1 - (a // b) * y1
        return g, x, y
    
def modular_inverse(e, phi):
    g, x, _ = extended_gcd(e, phi)
    if g != 1:
        raise ValueError ('e dan phi tidak prima')
    return x % phi

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def euler_totient(p,q):
    return (p-1) * (q-1)

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError ("p dan q harus prima")
    n = p * q
    phi = euler_totient(p, q)

    e = 3
    while gcd(e, phi) != 1:
        e+=1
    
    d = modular_inverse(e, phi)

    return ((e,n), (d,n))

def encrypt_rsa(public_key, plaintext):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher


def decrypt_rsa(private_key, ciphertext):
    d, n = private_key
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plain)

if __name__ == "__main__":
    print("===== DEMO RSA CRYPTOSYSTEM =====")
    p, q = 61, 53
    print(f" p = {p}")
    print(f" p = {q}")

    print(f" n = {p * q}")
    print(f" φ(n) = {(p-1)*(q-1)} ")

    public_key, private_key = generate_keypair(p, q)

    print(f"Kunci Publik  (e,n):  {public_key} ")
    print(f"Kunci Privat  (d,n):  {private_key} ")

    pesan_asli = "HELLO WORLD"
    print(f"Pesan asli = {pesan_asli}")

    hasil_enkripsi = encrypt_rsa(public_key, pesan_asli)
    print (f"Hasil Enkripsi: {hasil_enkripsi}")

    hasil_dekripsi= decrypt_rsa(private_key, hasil_enkripsi)
    print (f"Hasil Enkripsi: {hasil_dekripsi}")