from dotenv import load_dotenv
import os, requests

load_dotenv()



Api_Key='OPENROUTER_API_KEY'

models=["google/gemma-4-31b-it:free","cohere/north-mini-code:free","google/gemma-4-26b-a4b-it:free","nvidia/nemotron-3-super-120b-a12b:free"]
url="https://openrouter.ai/api/v1/chat/completions"


response_mistral=requests.post(
        "https://api.mistral.ai/v1/chat/completions",
        headers={"Authorization":f"Bearer {os.environ['MISTRAL_API_KEY']}"},
        json={    
        "model": "mistral-small-latest",
        "messages": [{"role": "user", "content": "Hello, Mistral!"}],
        },
    )
if response_mistral.status_code != 200:
    for model in models:
        response2=requests.post(
            url,
            headers={"Authorization":f"Bearer {os.environ[Api_Key]}"},
            json={    
            "model": model,
            "messages": [{"role": "user", "content": "Hello!"}],
            },
        )
        if response2.status_code == 200:
            print(response2.json())
            break
    else:
        print("Il y'a eu une erreur :",response2.status_code)
else:
    print(response_mistral.json())



   