import requests
import os
import platform

#Função para limpar a tela
def clear_screen():
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")

#Função para traduzir o texto
def translate_text(text, target_lang, source_lang="en"):
    url = "https://api.mymemory.translated.net/get"
    params = {
        "q": text,
        "langpair": f"{source_lang}|{target_lang}",
    }

    # Faz a requisição GET para a API
    response = requests.get(url, params=params)
    response_json = response.json()

    # Se a resposta não for 200, imprime o erro e retorna None
    if response.status_code != 200:
        print(f"Error {response.status_code}: {response_json.get('message')}")
        return None

    translated_text = response_json.get("responseData", {}).get("translatedText")

    if translated_text:
        return translated_text

    return None

def main():
    # Loop infinito para o usuário digitar o texto que deseja traduzir
    while True:
        clear_screen()
        print("+" + "-" * 60 + "+")
        text = input("Digite o texto que deseja traduzir (ou digite 'sair' para encerrar o programa): ")
        if text.lower() == "sair":
            break

        source_lang = input("Digite o código de idioma do texto original (por exemplo, 'en' para inglês, 'es' para espanhol, etc.): ")
        target_lang = input("Digite o código de idioma para o qual você deseja traduzir (por exemplo, 'en' para inglês, 'es' para espanhol, etc.): ")

        
        translated_text = translate_text(text, target_lang, source_lang)
        if translated_text is not None:
            clear_screen()
            print("+" + "-" * 60 + "+")
            print(f"\033[1m{'Texto original em '}\033[0m({source_lang}): {text}")  # Exibe o texto original com o código de idioma
            print(f"\033[1m{'Texto traduzido em '}\033[0m({target_lang}): {translated_text}")  # Exibe o texto traduzido com o código de idioma
            print("+" + "-" * 60 + "+ \n")
        
        input("\nPressione Enter para continuar...")

    print("Obrigado por usar o tradutor!")

if __name__ == "__main__":
    main()