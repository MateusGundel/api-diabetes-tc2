# api-diabetes-tc2
Api criada utilizando Python e FastAPI para desenvolvimento e validação do TCII

## Executando o Projeto

- Crie o ambiente virtual, ative e instale as bibliotecas listadas no requirements.txt
- Execute ```uvicorn app.main:app --reload``` para executar o projeto
- Acesse ```http://127.0.0.1:8000/docs``` para visualizar a documentação e mais informações sobre os endpoints

### As seguintes variáveis devem ser configuradas:
````
DATABASE_URL="postgresql://user:password@url:port/database"
SECRET_KEY="another-secret-key"
FIRST_SUPERUSER="first-email@email.com"
FIRST_SUPERUSER_PASSWORD="first-pass"
WATSON_API_KEY="your-watson-api-key"
WATSON_VERSION="your-watson-version"
WATSON_ASSISTANT_ID="your-watson-application-id"
````