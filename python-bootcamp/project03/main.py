import asyncio
import os
import aiohttp 
from aioconsole import ainput
from contextlib import suppress
from pathlib import Path
from prettytable import PrettyTable


def get_directory() -> str:
    target_dir = ""
    while len(target_dir) == 0:
        temp = input("Save images to this directory: ").strip()
        if len(temp) == 0:
            print("No input")
        else:
            try:
                os.makedirs(temp, exist_ok=True)
                if os.access(temp, os.W_OK):
                    target_dir = temp
                else:
                    print(f"No write permission for {temp}")
            except OSError:
                print(f"Directory {temp} cannot be created")
    return target_dir

async def put_url(q: asyncio.Queue) -> None:
    while True:
        url = await ainput("Enter an image URL: ")
        if not url.strip():
            break
        await q.put(url.strip())

async def get_url(q: asyncio.Queue, target_dir: str, res) -> None:
    while True:
        url = await q.get()
        status = await download_img(url, target_dir)
        result = {
            "url": url,
            "status": status
        }
        res.append(result)
        q.task_done()

async def download_img(url: str, target_dir: str) -> str:
    timeout = aiohttp.ClientTimeout(total=5)
    try:
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    f_name = Path(url).name
                    f_path = os.path.join(target_dir, f_name)
                    content = await resp.read()
                    with open(f_path, "wb") as f:
                        f.write(content)
                    return "Success"
                else:
                    return "Error"
    except (aiohttp.ClientConnectorError, asyncio.TimeoutError):
        return "Error"
    except Exception:
        return "Error"

async def manager(q: asyncio.Queue, put_url_task: asyncio.Task, get_url_task: asyncio.Task) -> None:
    await put_url_task
    await q.join()
    get_url_task.cancel()
    await get_url_task

def print_results(res) -> None:
    res_Table = PrettyTable(["Link", "Status"])
    for r in res:
        res_Table.add_row([r["url"], r["status"]])
    print(res_Table)

async def main() -> None:
    target_dir = get_directory()
    q = asyncio.Queue()
    res = []
    get_url_task = asyncio.create_task(get_url(q, target_dir, res))
    put_url_task = asyncio.create_task(put_url(q))
    manager_task = asyncio.create_task(manager(q, put_url_task, get_url_task))
    with suppress(asyncio.CancelledError):
        await asyncio.gather(put_url_task, get_url_task, manager_task)
    print_results(res)


if __name__ == "__main__":
    asyncio.run(main())