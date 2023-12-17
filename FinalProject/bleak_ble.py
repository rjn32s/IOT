"""
Scan/Discovery
--------------
Example showing how to scan for BLE devices.
Updated on 2019-03-25 by hbldh <henrik.blidh@nedomkull.com>
"""

import asyncio
from bleak import discover


async def main():
    devices = await discover()
    for d in devices:
        print(d)


if __name__ == "__main__":
    asyncio.run(main())