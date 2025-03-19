from langchain_openai import AzureChatOpenAI
from settings import AZURE_ENDPOINT, AZURE_API_KEY, API_VERSION

def create_azure_llm(deployment_name="gpt-4o-mini"):
    """
    Cria e retorna uma instância de LLM da Azure OpenAI

    Args:
        deployment_name (str): Nome do deployment no Azure

    Returns:
        AzureOpenAI: Instância configurada da LLM
    """

    llm = AzureChatOpenAI(
        azure_endpoint=AZURE_ENDPOINT,
        azure_deployment=deployment_name,
        openai_api_key=AZURE_API_KEY,
        openai_api_version=API_VERSION,
        temperature=0
    )
    return llm

