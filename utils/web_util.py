

from  utils.logger_util import  logger

'''针对场景：点击按钮还未展示，会报异常，那么就多次点击'''
def click_exception(by, element, max_attempts=5):
    def _inner(driver):
        actul_attempts = 0 # 实际点击次数
        while actul_attempts < max_attempts:
            # 进行点击操作
            actul_attempts += 1 # 每次循环，实际点击次数加1
            try:
                # 如果点击过程报错，则直接执行except逻辑，并继续循环
                # 没有报错，则直接return 循环结束
                driver.find_element(by,element).click()
                return True
            except Exception:
                logger.debug("点击的时候出现了一次异常")
        # 当实际点击次数大于最大点击次数时候
        raise Exception("超出了最大点击次数")
    return  _inner



