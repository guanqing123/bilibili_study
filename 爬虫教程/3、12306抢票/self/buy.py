# 导入自动化测试模块
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 打开浏览器
driver = webdriver.Chrome()

# 访问网站
driver.get('https://kyfw.12306.cn/otn/leftTicket/init')

# 输入出发地
driver.find_element(By.ID, 'fromStationText').click()
driver.find_element(By.ID, 'fromStationText').clear()
driver.find_element(By.ID, 'fromStationText').send_keys('杭州')
driver.find_element(By.ID, 'fromStationText').send_keys(Keys.ENTER)

# 输入目的地 00196
driver.find_element(By.ID, 'toStationText').click()
driver.find_element(By.ID, 'toStationText').clear()
driver.find_element(By.ID, 'toStationText').send_keys('衢州')
driver.find_element(By.ID, 'toStationText').send_keys(Keys.ENTER)

# 输入出发时间
driver.find_element(By.ID, 'train_date').click()
driver.find_element(By.ID, 'train_date').clear()
driver.find_element(By.ID, 'train_date').send_keys('2024-11-12')
driver.find_element(By.ID, 'train_date').send_keys(Keys.ENTER)

# 点击查询按钮
driver.find_element(By.ID, 'query_ticket').click()

# 如果 id_card 元素在 2 秒内变得可见，那么代码就会在 2 秒后继续，不会等满 10 秒。只有在 10 秒内条件仍未满足时才会抛出异常
# WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.CSS_SELECTOR, '#queryLeftTable tr:nth-child(3) .btn72'))
# ).click()

# https://www.bilibili.com/video/BV1T541117Nn/?spm_id_from=333.788.player.switch&vd_source=50633961851476a9b0991ae7b138aa23&p=8

try:
    # Wait until the table is loaded
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "queryLeftTable")))
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "queryLeftTable"))
    )
    # Locate the rows in the table
    rows = driver.find_elements(By.XPATH, "//tbody[@id='queryLeftTable']/tr")
    print('rows', rows)
    for row in rows:
        try:
            # Check if there's a train number with class 'number' and text 'D171'
            train_number_element = row.find_element(By.CSS_SELECTOR, "a.number")
            train_number = train_number_element.text
            print('车次：', train_number)

            # 检查车次是否为'D171'
            if train_number == 'G1657':
                # 检查 '一等座' 的余票信息
                seat_info = row.find_element(By.XPATH, ".//td[contains(@aria-label, '一等座')]//div").text

                print('车次：', train_number, 'seat_info', seat_info)
                # 确认座位是否有余票
                if seat_info == "有" or int(seat_info) > 0:
                    # 找到并点击预定按钮
                    book_button = row.find_element(By.CSS_SELECTOR, "a.btn72")
                    book_button.click()
                    print("成功点击 G1657 次列车的预订按钮，有一等座余票。")

                    # 用户名
                    WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.ID, "J-userName"))
                    )
                    driver.find_element(By.ID, 'J-userName').send_keys('15857125375')
                    driver.find_element(By.ID, 'J-password').send_keys('gq131625')
                    driver.find_element(By.ID, 'J-login').click()

                    WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.ID, "id_card"))
                    )
                    driver.find_element(By.ID, 'id_card').send_keys('491X')
                    # driver.find_element(By.ID, 'verification_code').click()

                    # # 选人
                    # time.sleep(1)
                    # label = driver.find_element("xpath", "//label[text()='陈玲']")
                    # checkbox = label.find_element("xpath", "./preceding-sibling::input")

                    # driver.find_element(By.ID, 'sureClick').click()

                    break
        except Exception as e:
            continue
finally:
    input("按 Enter 键退出并关闭浏览器...")
