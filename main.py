import aiohttp
import asyncio
import argparse
from skeleton import create_app
from skeleton.settings import load_config


try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    print("Uvloop is not available")

parser = argparse.ArgumentParser(description="Skeleton")
parser.add_argument('--host', help="Server host name", default="0.0.0.0")
parser.add_argument('--port', help="Server host connection port", default="5000")
parser.add_argument(
    '--reload', 
    action="store_true", 
    help="Autoreload server by saving project files"
)
parser.add_argument('--config', type=argparse.FileType('r'), help="Config file")

args = parser.parse_args()
app = create_app(config=load_config(args.config))

if args.reload:
    print("Autoreload is active")
    import aioreloader
    aioreloader.start()

if __name__ == '__main__':
    aiohttp.web.run_app(app, host=args.host, port=args.port)