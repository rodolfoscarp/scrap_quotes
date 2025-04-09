import httpx
from loguru import logger


class APIServices:

    @staticmethod
    def create(endpoint: str, autor: str, text: str, tags: list[str]):
        response = httpx.post(
            url=endpoint,
            data={"autor": autor, "text": text, "tags": tags},
        )

        try:
            response.raise_for_status()
            logger.debug(
                "Registro enviado com sucesso. Status code {}", response.status_code
            )
        except httpx.RequestError as e:
            logger.error("Falha ao executar a requisição: {}", e)
        except httpx.HTTPStatusError as e:
            logger.error(
                "Api retornou uma exceção. Status code {}, message {}",
                e.response.status_code,
                e.response.text,
            )
        except Exception as e:
            logger.exception(e)
