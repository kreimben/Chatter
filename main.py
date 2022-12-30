import asyncio
import logging
from concurrent.futures import ThreadPoolExecutor

import grpc

from ChatManager import ChatManager
from output.chat_pb2_grpc import add_ChattingServicer_to_server
from servicer.ChattingServicer import ChattingServicer


# os.environ.setdefault('GRPC_VERBOSITY', 'debug')

async def main():
    server = grpc.aio.server(ThreadPoolExecutor(max_workers=10))
    add_ChattingServicer_to_server(
        ChattingServicer(ChatManager()), server
    )
    port = 'localhost:5000'
    server.add_insecure_port(port)
    await server.start()
    print(f'Server starting at {port}')
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    print(f'server run')
    asyncio.run(main())
