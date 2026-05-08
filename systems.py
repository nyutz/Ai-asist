from chat import chat

# =====================================
# EVALUATE CODE
# =====================================

def evaluate_code(code):

    prompt = f"""
Periksa kode berikut.

Cek apakah:
- lengkap
- tidak terpotong
- semua variabel terdefinisi
- bisa dijalankan

Jawab hanya:
VALID
atau
INVALID: alasan singkat

Kode:
{code}
"""

    result = chat(prompt)

    return result


# =====================================
# FIX CODE
# =====================================

def fix_code(code, feedback):

    prompt = f"""
Perbaiki kode berikut berdasarkan feedback.

Feedback:
{feedback}

Kode:
{code}

Berikan hanya kode final.
"""

    result = chat(prompt)

    return result


# =====================================
# RETRY SYSTEM
# =====================================

def retry_generation(prompt, max_try=3):

    print("🧠 Generating...")

    code = chat(prompt)

    for i in range(max_try):

        print(f"🔍 Evaluasi ke-{i+1}")

        evaluation = evaluate_code(code)

        print(evaluation)

        # cek valid
        if evaluation.strip().startswith("VALID"):

            print("✅ Kode valid")

            return code

        print("🔧 Memperbaiki...")

        code = fix_code(code, evaluation)

    print("⚠️ Max retry tercapai")

    return code
