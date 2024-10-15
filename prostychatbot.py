import openai
import time

# Ustaw swój klucz API OpenAI
openai.api_key = 'your-api-key'

def generate_chatgpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response['choices'][0]['message']['content']
    
    # Obsługa błędów API
    except openai.error.RateLimitError:
        print("Przekroczono limit zapytań (Error 429). Oczekiwanie przed ponownym zapytaniem...")
        time.sleep(60)  # Czekaj 60 sekund przed ponownym zapytaniem
        return generate_chatgpt_response(prompt)
    
    except openai.error.APIError as e:
        print(f"Wystąpił błąd API: {e}")
        return "Wystąpił problem z komunikacją z serwerem. Spróbuj ponownie później."

    except openai.error.Timeout as e:
        print(f"Przekroczono czas oczekiwania: {e}")
        return "Serwer nie odpowiedział na czas. Spróbuj ponownie później."
    
    except Exception as e:
        print(f"Nieoczekiwany błąd: {e}")
        return "Wystąpił nieoczekiwany błąd. Spróbuj ponownie później."


def chatbot():
    print("Czatbot ChatGPT jest gotowy do działania! (Wpisz 'exit', aby zakończyć.)")
    while True:
        user_input = input("Ty: ")
        if user_input.lower() == "exit":
            print("Zakończono rozmowę.")
            break
        response = generate_chatgpt_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    chatbot()
