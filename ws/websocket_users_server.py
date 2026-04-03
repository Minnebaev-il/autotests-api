import asyncio

import websockets
from websockets import ServerConnection


async def echo(websocket: websockets.ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")
        response = f"Сообщение пользователя: {message}"
        await websocket.send(response)

        for _ in range(5):
            await websocket.send(response)


async def main():
    server  = await websockets.serve(echo, 'localhost', 8765)
    print(f"WebSocket сервер запущен на ws://localhost:8765")
    await server.wait_closed()



if __name__ == "__main__":
    asyncio.run(main())