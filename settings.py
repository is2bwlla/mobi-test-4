import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente da .env
load_dotenv()

# Configurações da Azure OpenAI
AZURE_ENDPOINT = os.environ['AZURE_OPENAI_ENDPOINT']
AZURE_API_KEY = os.environ['AZURE_OPENAI_API_KEY']
API_VERSION = os.environ['OPENAI_API_VERSION']
