import ollama


# ------------------ INPUT SYSTEM ------------------
def get_code_input():
    print("Paste your code below (type 'END' on a new line to finish):")

    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)

    return "\n".join(lines)


# ------------------ CORE ANALYSIS ------------------
def analyze_code(code):
    issues = []

    # -------- Rule-Based Checks --------
    if "int main()" in code and ";" not in code:
        issues.append("Possible missing semicolon")

    if "printf" in code and "#include" not in code:
        issues.append("Missing required header (e.g., stdio.h)")

    if "=" in code and ";" not in code:
        issues.append("Possible syntax error in assignment")

    # -------- AI Explanation --------
    prompt = f"""
Explain this code briefly and suggest improvements:

{code}
"""

    response = ollama.chat(
        model="phi",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    ai_output = response["message"]["content"]

    # -------- Final Output --------
    formatted = "\n--- Code Review ---\n\n"

    formatted += f"Explanation:\n{ai_output.strip()}\n\n"

    if issues:
        formatted += "Issues:\n"
        for issue in issues:
            formatted += f"- {issue}\n"
    else:
        formatted += "Issues:\nNo major issues detected\n"

    formatted += "\nSuggestions:\n"

    if "printf" in code and "#include" not in code:
        formatted += "- Add required header file (stdio.h)\n"

    formatted += "- Improve variable naming\n"
    formatted += "- Add proper error handling\n"

    return formatted


# ------------------ MAIN ------------------
if __name__ == "__main__":
    code = get_code_input()

    print("\nAnalyzing code...\n")

    try:
        result = analyze_code(code)
        print(result)
    except Exception as e:
        print("Error during AI analysis:", e)
