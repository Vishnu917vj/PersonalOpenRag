from typing import Optional

import httpx

from app.core.config import settings
from app.core.logger import logger


class OpenRouterClient:
    BASE_URL = "https://openrouter.ai/api/v1"

    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {settings.OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        }

    async def chat(
        self,
        messages: list[dict],
        model: Optional[str] = None,
        reasoning: bool = False,
    ) -> dict:

        payload = {
            "model": model or settings.OPENROUTER_MODEL,
            "messages": messages,
        }

        if reasoning:
            payload["reasoning"] = {"enabled": True}

        logger.info("Sending request to OpenRouter API...")
        async with httpx.AsyncClient(timeout=120) as client:
            response = await client.post(
                f"{self.BASE_URL}/chat/completions",
                headers=self.headers,
                json=payload,
            )

            response.raise_for_status()
            logger.info("Received response from OpenRouter API.")
            return response.json()


openrouter = OpenRouterClient()