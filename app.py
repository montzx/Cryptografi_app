import streamlit as st

# =========================
# DATA TABLE (KEY)
# =========================
DATA = {
    "A": {"index": 1, "rarity": 2, "chance": 50, "multiplier": 115},
    "B": {"index": 2, "rarity": 3, "chance": 55, "multiplier": 155},
    "C": {"index": 3, "rarity": 2, "chance": 73, "multiplier": 130},
    "D": {"index": 4, "rarity": 3, "chance": 90, "multiplier": 150},
    "E": {"index": 5, "rarity": 3, "chance": 115, "multiplier": 155},
    "F": {"index": 6, "rarity": 1, "chance": 180, "multiplier": 260},
    "G": {"index": 7, "rarity": 2, "chance": 215, "multiplier": 275},
    "H": {"index": 8, "rarity": 3, "chance": 265, "multiplier": 290},
    "I": {"index": 9, "rarity": 3, "chance": 315, "multiplier": 310},
    "J": {"index": 10, "rarity": 3, "chance": 390, "multiplier": 340},
    "K": {"index": 11, "rarity": 4, "chance": 487, "multiplier": 295},
    "L": {"index": 12, "rarity": 4, "chance": 255, "multiplier": 310},
    "M": {"index": 13, "rarity": 4, "chance": 255, "multiplier": 330},
    "N": {"index": 14, "rarity": 4, "chance": 255, "multiplier": 250},
    "O": {"index": 15, "rarity": 4, "chance": 255, "multiplier": 300},
    "P": {"index": 16, "rarity": 4, "chance": 255, "multiplier": 350},
    "Q": {"index": 17, "rarity": 5, "chance": 5000, "multiplier": 525},
    "R": {"index": 18, "rarity": 4, "chance": 569, "multiplier": 333},
    "S": {"index": 19, "rarity": 5, "chance": 777, "multiplier": 300},
    "T": {"index": 20, "rarity": 5, "chance": 813, "multiplier": 350},
    "U": {"index": 21, "rarity": 5, "chance": 1333, "multiplier": 400},
    "V": {"index": 22, "rarity": 5, "chance": 2187, "multiplier": 450},
    "W": {"index": 23, "rarity": 5, "chance": 3003, "multiplier": 500},
    "X": {"index": 24, "rarity": 5, "chance": 3333, "multiplier": 460},
    "Y": {"index": 25, "rarity": 6, "chance": 3666, "multiplier": 550},
    "Z": {"index": 26, "rarity": 6, "chance": 5555, "multiplier": 630},
}

# =========================
# CORE FUNCTIONS
# =========================
def encrypt(text: str) -> str:
    text = text.upper().replace(" ", "")
    result = []

    for ch in text:
        if ch not in DATA:
            raise ValueError(f"Huruf tidak valid: {ch}")

        d = DATA[ch]
        masked_code = (d["index"] * 7) + 13
        encrypt_value = (d["chance"] + d["multiplier"]) * d["rarity"]
        result.append(f"{masked_code}:{encrypt_value}")

    return ".".join(result)


def decrypt(cipher: str) -> str:
    blocks = cipher.split(".")
    plain = ""

    for block in blocks:
        masked_code, encrypt_value = map(int, block.split(":"))
        index = (masked_code - 13) // 7

        found = False
        for ch, d in DATA.items():
            if d["index"] == index:
                expected = (d["chance"] + d["multiplier"]) * d["rarity"]
                if expected == encrypt_value:
                    plain += ch
                    found = True
                    break

        if not found:
            raise ValueError(f"Cipher tidak valid: {block}")

    return plain


# =========================
# STREAMLIT UI
# =========================
st.set_page_config(page_title="Ore–Mask Cipher", layout="centered")

st.title("🔐 Ore–Mask Cipher")
st.caption("Custom Cryptography Algorithm (Educational Purpose)")

mode = st.radio("Pilih Mode", ["Enkripsi", "Dekripsi"])

if mode == "Enkripsi":
    plaintext = st.text_input("Masukkan Plaintext (A–Z, tanpa spasi)")

    if st.button("Enkripsi"):
        try:
            cipher = encrypt(plaintext)
            st.success("Berhasil dienkripsi")
            st.code(cipher)
        except Exception as e:
            st.error(str(e))

else:
    ciphertext = st.text_area("Masukkan Ciphertext")

    if st.button("Dekripsi"):
        try:
            plain = decrypt(ciphertext)
            st.success("Berhasil didekripsi")
            st.code(plain)
        except Exception as e:
            st.error(str(e))
