import asyncio
import time

async def verify_student():
    print("Fetching attendance...")
    await asyncio.sleep(3)
    print("Student verified")

async def fetch_attendance():
    print("Fetching attendance...")
    await asyncio.sleep(3)
    print("Attendance loaded")

async def fetch_marks():
    print("Fetching marks...")
    await asyncio.sleep(2)
    print("Marks loaded")

async def main():
    start = time.time()
    await verify_student()
    attendence_task = asyncio.create_task(fetch_attendance())
    marks_tasks = asyncio.create_task(fetch_marks())
    await attendence_task
    await marks_tasks
    end  = time.time()
    print(f"\nTotal Time = {end - start:.2f} seconds")

asyncio.run(main())