import asyncio
from fastapi import WebSocket, WebSocketDisconnect
from src.models.common import Route, WSOutput
from src.services.health import get_server_stats
from src.utils import logger


async def health_ws(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            stats = await get_server_stats()
            await WSOutput.send(
                websocket,
                data=stats,
                message="Server health status"
            )
            await asyncio.sleep(10)
    except WebSocketDisconnect:
        logger.info("🔌 Health WebSocket disconnected")
    except Exception as e:
        logger.error(f"❌ Error in health_ws: {e}")
        try:
            await WSOutput.send_error(websocket, message=str(e))
        except Exception:
            pass


route = Route(
    function=health_ws,
    method="WEBSOCKET",
    summary="WebSocket server health status",
    description="Streams CPU, RAM, Disk, Database and Redis health information every 10 seconds over WebSocket"
)
