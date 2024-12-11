1.import pytest
import asyncio

async def delayed_function(delay_time):
    await asyncio.sleep(delay_time)
    return "done"

@pytest.mark.asyncio
async def test_function_timeout(event_loop):
    with pytest.raises(asyncio.TimeoutError):
        await asyncio.wait_for(delayed_function(3), timeout=2) 

2.import pytest
import asyncio

async def task_1():
    await asyncio.sleep(1)
    return "Task 1 done"

async def task_2():
    await asyncio.sleep(2)
    return "Task 2 done"

@pytest.mark.asyncio
async def test_parallel_tasks(event_loop):
    results = await asyncio.gather(task_1(), task_2())
    assert results == ["Task 1 done", "Task 2 done"]

3.import pytest
import aiohttp

async def fetch_data():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://jsonplaceholder.typicode.com/posts/1") as response:
            return await response.json()

@pytest.mark.asyncio
async def test_fetch_data(event_loop):
    data = await fetch_data()

    assert isinstance(data, dict)
    assert "id" in data
    assert data["id"] == 1

4.import pytest
import aiosqlite

async def insert_record():
    async with aiosqlite.connect(":memory:") as db:  
        await db.execute("CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT)")
        await db.execute("INSERT INTO test (name) VALUES (?)", ("Alice",))
        await db.commit()

        async with db.execute("SELECT name FROM test WHERE id=1") as cursor:
            row = await cursor.fetchone()
            return row[0] if row else None

@pytest.mark.asyncio
async def test_insert_record(event_loop):
    result = await insert_record()
    assert result == "Kate" 

5. import pytest
import asyncio

async def task_with_error():
    await asyncio.sleep(1)
    raise RuntimeError("Task failed!")

async def normal_task():
    await asyncio.sleep(1)
    return "All good."

@pytest.mark.asyncio
async def test_handle_task_exceptions(event_loop):
    tasks = [task_with_error(), normal_task()]
    results = await asyncio.gather(*tasks, return_exceptions=True) 

    assert isinstance(results[0], RuntimeError)  
    assert str(results[0]) == "Task failed!"
    assert results[1] == "All good." 
