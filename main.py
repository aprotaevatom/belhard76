# # # from threading import *
# # from multiprocessing import *
# # from time import sleep
# # # from queue import Queue
# #
# # print_lock = RLock()
# # semaphore1 = Semaphore(value=2)
# # barrier = Barrier(parties=3)
# # event = Event()
# # q = Queue()
# #
# # # def _ping():
# # #     for _ in range(10):
# # #         with print_lock:
# # #             print(current_thread().name)
# # #             sleep(1)
# # #
# # #
# # # def ping():
# # #     barrier.wait()
# # #     _ping()
# # #
# # #
# # # threads = [Thread(target=ping) for _ in range(10)]
# # # for thread in threads:
# # #     thread.start()
# #
# #
# # def second():
# #     from random import randint
# #     while True:
# #         a = randint(1, 10)
# #         q.put(a)
# #
# #
# # def first():
# #     while True:
# #         print(q.get())
# #
# #
# # if __name__ == '__main__':
# #     thread1 = Process(target=first)
# #     thread2 = Process(target=second)
# #
# #     thread1.start()
# #     thread2.start()
#
# from asyncio import sleep, current_task, run, create_task, gather, to_thread
#
#
# async def foo():
#     while True:
#         print(current_task().get_name())
#         await sleep(delay=1)
#
#
# async def main():
#     pass
#     # tasks = [create_task(foo()) for _ in range(10)]
#     # for task in tasks:
#     #     await task
#     # await gather(*[foo() for _ in range(10)])
#
#
# run(main())
from asyncio import run

from sqlalchemy import Column, INT, VARCHAR
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


class Base(DeclarativeBase):
    pass


class Category(Base):
    __tablename__ = "categories"

    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(length=32), nullable=False, unique=True)


engine = create_async_engine("sqlite+aiosqlite:///db.db")
async_session_maker = async_sessionmaker(engine)


async def main():
    async with async_session_maker() as session:
        cat = Category(name="Coffee")
        session.add(cat)
        await session.commit()
        await session.refresh(cat)


run(main())
