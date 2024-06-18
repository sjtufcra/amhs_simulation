
import redis as rds
import random
from loguru import logger as log
# 
from create import Car
def addDataToRedis(server = '127.0.0.1',port = 6379,num = 100):
    rdb = rds.Redis(host=server, port=port, db=0)
    with rdb.pipeline() as pipe:
        ketset = set()
        for x in range(num):
            id = createId(ketset,'C')
            my_car = Car(id)
            str = my_car.to_json()
            number = id[1:]
            pipe.set(f"Car:monitor:128.168.11.147_1{number}", mapping=str)

def createId(set,title='C',lenth=5):
    while True:
        num = str(random.randint(1, 99999))[:lenth]
        if num not in set:
            set.add(num)
            id = f'{title}{num}'
            break
    return id 
def main():
    log.add('./redis.log',level='INFO')
    cars = 1000
    addDataToRedis(num = cars);
    log.info(f'success: add {cars} data to redis')

main()