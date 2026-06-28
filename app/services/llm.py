from app.core.openrouter import openrouter
from app.core.logger import logger


class LLMService:

    async def generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ):

        logger.info("Sending request to LLM...")
        messages = [
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ]

        logger.info("Received response from LLM.")
        response = await openrouter.chat(messages)

        return response["choices"][0]["message"]["content"]


llm_service = LLMService()