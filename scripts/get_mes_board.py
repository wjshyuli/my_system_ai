import time
from board_date.last_board_data import last_board_data
from logs.logger import get_logger
logger = get_logger(__name__)


def get():
    a=[]
    return a


def fetch_mes_data():
    while True:
        try:
            data = get()

            # 🔥更新全局缓存
            # last_board_data.clear()
            last_board_data.extend(data)


            logger.info("MES数据更新成功")

        except Exception as e:
            logger.info("MES请求失败:", e)

        time.sleep(300)



if __name__ == "__main__":
    fetch_mes_data()