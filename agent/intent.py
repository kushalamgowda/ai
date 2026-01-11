from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

intent_prompt = PromptTemplate.from_template(
    """
    Classify the user intent strictly as one of:
    - greeting
    - product_inquiry
    - high_intent

    User message: {message}

    Respond with only the intent label.
    """
)

def detect_intent(message: str) -> str:
    response = llm.invoke(intent_prompt.format(message=message))
    return response.content.strip()
