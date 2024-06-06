# config.py
OPENAI_API_KEY = 'sk-proj-KZF7qrKIMJaK9AcY5TpqT3BlbkFJ504zt1oFY0g6tz2MaPeR'
import openai
from main import OPENAI_API_KEY

# Configuração da chave da API
openai.api_key = OPENAI_API_KEY

def gpt_prompt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

def main():
    print("Bem-vindo à Gerador de Ideias de Startups!")

    # Entrada do Usuário
    user_input = input("Por favor, descreva suas preferências e interesses: ")

    # Geração de Ideias
    startup_ideas = gpt_prompt(user_input)

    # Apresentação das Ideias
    print("\nAqui estão algumas ideias de startups para você:")
    print(startup_ideas)

if __name__ == "__main__":
    main()