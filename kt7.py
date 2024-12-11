1.import asyncio
import pytest

@pytest.mark.asyncio
async def test_future_resolves_with_expected_value():
    async def sample_async_function():
        return "expected result"

    result = await sample_async_function()
    assert result == "expected result"

2.import asyncio
import pytest

@pytest.mark.asyncio
async def test_future_rejects_with_expected_exception():
    async def sample_async_function():
        raise ValueError("expected exception")

    with pytest.raises(ValueError, match="expected exception"):
        await sample_async_function()

3.import aiohttp
import pytest

@pytest.mark.asyncio
async def test_http_request_to_api():
    url = "https://jsonplaceholder.typicode.com/todos/1"  # Пример API
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            assert response.status == 200
            data = await response.json()
            assert "userId" in data
            assert data["id"] == 1

4.import aiosqlite
import pytest

@pytest.mark.asyncio
async def test_database_record_insertion():
    async with aiosqlite.connect(":memory:") as db:
        await db.execute("CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT)")
        await db.execute("INSERT INTO test_table (name) VALUES (?)", ("test_name",))
        await db.commit()

        async with db.execute("SELECT name FROM test_table WHERE id = 1") as cursor:
            row = await cursor.fetchone()
            assert row[0] == "test_name"



5. import asyncio
import pytest

@pytest.mark.asyncio
async def test_run_coroutine_in_thread():
    async def nested_async_function():
        await asyncio.sleep(0.1)  # симуляция работы
        return "result from thread"

    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, asyncio.run, nested_async_function())
    assert result == "result from thread"
