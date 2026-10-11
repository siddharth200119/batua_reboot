from typing import Optional, Any
from pydantic import BaseModel
from fastapi import WebSocket


class WSMessage(BaseModel):
    """
    Standard WebSocket Message format
    """
    status: str
    message: str
    data: Optional[Any] = None


class WSOutput:
    """
    Standard WebSocket response wrapper
    """

    @staticmethod
    async def send(
        websocket: WebSocket,
        data: Optional[Any] = None,
        message: str = "Success",
        status: str = "success",
    ) -> None:
        """
        Send a standardized message through the websocket
        """
        msg = WSMessage(
            status=status,
            message=message,
            data=data,
        )
        await websocket.send_json(msg.model_dump(mode="json"))

    @staticmethod
    async def send_error(
        websocket: WebSocket,
        message: str = "An error occurred",
        data: Optional[Any] = None,
    ) -> None:
        """
        Send an error message through the websocket
        """
        await WSOutput.send(
            websocket=websocket,
            data=data,
            message=message,
            status="error",
        )

    @staticmethod
    async def send_raw_json(
        websocket: WebSocket,
        data: Any,
    ) -> None:
        """
        Send raw JSON data through the websocket without the standard wrapper
        """
        from fastapi.encoders import jsonable_encoder
        await websocket.send_json(jsonable_encoder(data))
