import openai

from database import retrieved_text
from logging_config import logger
from Observability_metrics import QUERY_COUNT, QUERY_TIME


client = openai.OpenAI(
    api_key="sk-gSdp9lNxQ8iPB2VUYOB7DF0Kkx1pi4toasRreNoNEul7hRigfFMNo90t/jFcNp0uCUZkFmUgEFU81madjiwwhF6EMwkKnJXLFmQt3NKo3wg=",
    base_url="https://router.requesty.ai/v1"
)

@QUERY_TIME.time()
def answer_query(query):
    response_text = ""
    retrieved_context = retrieved_text(query)
    logger.info("User asked: %s", query)
    QUERY_COUNT.inc()

    if query:
        try:
            response = client.chat.completions.create(
                model="nebius/deepseek-ai/DeepSeek-V3-0324",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful Discord bot that answers  questions. Always use the provided context if it's relevant. Keep responses complete and concise, between 50-100 words."
                    },
                    {
                        "role": "system",
                        "content": f"Context:\n{retrieved_context}"
                    },
                    {
                        "role": "user",
                        "content": f"{query}"
                    }
                ],

            stream=True,
                max_tokens=150
            )
            logger.info("Bot response sent successfully")


            for chunk in response:
                if chunk.choices[0].delta.content:
                    chunk_content = chunk.choices[0].delta.content
                    response_text += chunk_content


            return response_text.strip()

        except Exception as e:
            print(f"LLM Error: {e}")
            logger.error(f"LLM error : {e}", exc_info=True)
            return "Sorry, I couldn't process your request."

    return "Please provide a query."

