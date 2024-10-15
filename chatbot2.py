import openai
import time

# Wprowadź swój klucz API OpenAI
openai.api_key = 'TWÓJ_KLUCZ_API'

conversation_history = []

def generate_response(prompt):
    for attempt in range(5):  # Próba do 5 razy
        try:
            # Wysyłamy zapytanie do modelu GPT-3.5 Turbo
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Używamy modelu GPT-3.5 Turbo
                messages=conversation_history + [{"role": "user", "content": prompt}]
            )

            # Dodajemy odpowiedź bota do historii rozmowy
            bot_response = response['choices'][0]['message']['content'].strip()
            conversation_history.append({"role": "assistant", "content": bot_response})
            return bot_response

        except openai.error.RateLimitError:
            print("Przekroczyłeś limit zapytań. Czekam...")
            time.sleep(2 ** attempt)  # Exponential backoff (2, 4, 8, 16 sekund itd.)
        except Exception as e:
            print(f"Wystąpił błąd: {e}")
            break

    return "Przepraszam, wystąpił problem z serwerem. Spróbuj ponownie później."

print("Witaj! Jak mogę Ci pomóc? (Napisz 'koniec', aby zakończyć rozmowę)")

while True:
    user_input = input("Ty: ")

    if user_input.lower() == 'koniec':
        print("Bot: Do widzenia!")
        break

    # Generujemy odpowiedź z GPT
    bot_response = generate_response(user_input)
    print(f"Bot: {bot_response}")
