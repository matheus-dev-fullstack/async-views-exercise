import asyncio
import httpx
from django.http import HttpResponse
import time

async def http_call_async():
    start_time = time.time()

    for i in range(1, 11):
        elapsed_time = time.time() - start_time
        true_elapsed_time = elapsed_time + 1
        print(f"{int(true_elapsed_time)} segundos")  
        await asyncio.sleep(1)
        
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org")
        print(r)

    # end_time = time.time()
    # total_elapsed_time = end_time - start_time
    # print(f"Total elapsed time: {total_elapsed_time} seconds")

async def async_view(request):
    await http_call_async() 
    return HttpResponse("Deu tudo certo!")