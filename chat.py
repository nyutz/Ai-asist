from setup import model, tokenizer

# =====================================
# SYSTEM PROMPT
# =====================================

SYSTEM_PROMPT = """
Kamu adalah AI coding assistant.

Aturan:
- Jawab dengan jelas
- Jika diminta kode, berikan kode lengkap
- Pastikan kode valid
- Jangan gunakan library eksternal kecuali diminta
"""

# =====================================
# MEMORY
# =====================================

history = []

# =====================================
# CHAT FUNCTION
# =====================================

def chat(user_input, max_tokens=256):
    global history

    # simpan input user
    history.append(f"User: {user_input}")

    # bangun context
    context = SYSTEM_PROMPT + "\n"

    # ambil beberapa history terakhir
    context += "\n".join(history[-6:])

    context += "\nAssistant:"

    # tokenize
    inputs = tokenizer(
        context,
        return_tensors="pt"
    ).to("cuda")

    # generate
    outputs = model.generate(
        **inputs,
        max_new_tokens=max_tokens,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.1,
        pad_token_id=tokenizer.eos_token_id
    )

    # decode
    result = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    # ambil jawaban terakhir
    if "Assistant:" in result:
        result = result.split("Assistant:")[-1]

    result = result.strip()

    # simpan jawaban AI
    history.append(f"Assistant: {result}")

    return result
