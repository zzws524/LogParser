import os
import asyncio
import typing
import time

global_var=[]

async def say_after(delay,what):
    await asyncio.sleep(delay)
    global_var.append(what)

async def func1():
    tasks_set=set()
    for i in range(4):
        tmpStr='word '+(str)(i+1)
        tmptask=asyncio.create_task(say_after(i,tmpStr))
        tasks_set.add(tmptask)
    #task1=asyncio.create_task(say_after(1,'hello'))
    #task2=asyncio.create_task(say_after(2,'world'))
    #task3=asyncio.create_task(say_after(3,'again'))
    #task4=asyncio.create_task(say_after(1.5,'my'))


    print (f"started at {time.strftime('%X')}")
    done,pending=await asyncio.wait(tasks_set,timeout=2.9,return_when=asyncio.FIRST_EXCEPTION)
    if pending:
        print ("error, not finish")
        os._exit(1)
    print (f"end at {time.strftime('%X')}")
    print (global_var)

if __name__=='__main__':
    asyncio.run(func1())
