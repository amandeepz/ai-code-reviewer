# AI Code Reviewer

## Overview
A CLI-based AI tool that analyzes source code, detects issues, and provides improvement suggestions using a hybrid approach of rule-based analysis and a locally hosted LLM.

## Features
- Multi-line code input via CLI
- Rule-based bug detection
- AI-powered explanation and suggestions
- Structured output format

## Tech Stack
- Python
- Ollama (Local LLM - Phi)
- CLI

## How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Start Ollama:
ollama run phi

3. Run the program:
python code_reviewer.py

## Example

Input:
int main() {
    int a = 5
    printf("%d", a);
}
END

Output:
Explanation:
...

Issues:
- Missing semicolon
- Missing header

Suggestions:
- Fix syntax
- Add header

## Key Concepts
- Hybrid system (rule-based + AI)
- Prompt engineering
- Local LLM inference
