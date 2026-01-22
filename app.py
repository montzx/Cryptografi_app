import streamlit as st

# =========================
# KEY DEFINITIONS
# =========================
KEYS = {
    "ruby": 11,
    "emerald": 17,
    "diamond": 23,
    "gold": 29,
    "silver": 31
}

# =========================
# DATA TABLE
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
# CRYPTO FUNCTIONS
# =========================
def encrypt(text: str, key_name: str) -> str:
    K = KEYS[key_name]
    text = text.upper().replace(" ", "")
    result = []

    for ch in text:
        if ch not in DATA:
            raise ValueError("Plaintext hanya boleh A–Z")

        d = DATA[ch]
        masked = (d["index"] * 7) + 13 + K
        value = ((d["chance"] + d["multiplier"]) * d["rarity"]) + K
        result.append(f"{masked}:{value}")

    return ".".join(result)


def decrypt(cipher: str, key_name: str) -> str:
    K = KEYS[key_name]
    blocks = cipher.split(".")
    plain = ""

    for block in blocks:
        masked, value = map(int, block.split(":"))
        index = (masked - 13 - K) // 7

        found = False
        for ch, d in DATA.items():
            expected = ((d["chance"] + d["multiplier"]) * d["rarity"]) + K
            if d["index"] == index and expected == value:
                plain += ch
                found = True
                break

        if not found:
            raise ValueError("Key salah atau cipher rusak")

    return plain


# =========================
# STREAMLIT UI
# =========================
st.set_page_config(page_title="Ore–Mask Cipher (Multi-Key)")

st.title("🔐 Ore–Mask Cipher")
st.title("THE FORGE - ROBLOX")
st.caption("Multi-Key Masked Cipher for Secure Text Transformation")

key_choice = st.selectbox("Pilih Key", list(KEYS.keys()))
mode = st.radio("Mode", ["Enkripsi", "Dekripsi"])

if mode == "Enkripsi":
    text = st.text_input("Plaintext (A–Z)")
    if st.button("Enkripsi"):
        try:
            st.code(encrypt(text, key_choice))
        except Exception as e:
            st.error(str(e))
else:
    cipher = st.text_area("Ciphertext")
    if st.button("Dekripsi"):
        try:
            st.code(decrypt(cipher, key_choice))
        except Exception as e:
            st.error(str(e))


