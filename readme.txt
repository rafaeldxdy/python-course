# CPF Validator 🇧🇷

This is a simple and functional Python script that validates **Brazilian CPF numbers** using the official algorithm from Receita Federal (Brazilian IRS).  
It was originally written by [Rafael Ribeiro](https://github.com/seu-usuario) as part of his Python learning journey and improved with help from AI (ChatGPT).

---

## 📌 What is a CPF?

A CPF (Cadastro de Pessoas Físicas) is the individual taxpayer registry identification in Brazil. It's an 11-digit number where the last two digits are check digits that validate the entire number. This script checks those digits to confirm whether a CPF is valid.

---

## 🧠 How it works

The script:

1. Accepts a CPF from the user (numbers only).
2. Verifies that the format is correct (11 digits).
3. Calculates the two verification digits based on the official algorithm.
4. Compares them with the user input.
5. Displays whether the CPF is valid or not.

It also includes loops to allow checking multiple CPFs and input validation to avoid crashes.

---

## ▶️ How to Run

Make sure you have Python installed.

```bash
python cpf_validator.py
