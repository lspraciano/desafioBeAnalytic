from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from drivers.firefox.firefox_drive import get_firefox_drive
from tasks.steam.get_sales_data_from_table_task import get_sales_data_from_table_task
from tasks.steam.list_all_sales_data_on_table_task import list_all_sales_data_on_table_task


def get_all_sales_steam_data_routine():
    firefox_web_drive: webdriver.Firefox
    firefox_web_driver_waiter: WebDriverWait

    firefox_web_drive, firefox_web_driver_waiter = get_firefox_drive(
        firefox_on_background=False
    )

    list_all_sales_data_on_table_task(
        firefox_web_drive=firefox_web_drive,
        firefox_web_driver_waiter=firefox_web_driver_waiter,
        start_date_filter="2023-03-01",
        end_date_filter="2023-12-31"
    )

    table_data: list[dict] | None = get_sales_data_from_table_task(
        firefox_web_drive=firefox_web_drive,
        firefox_web_driver_waiter=firefox_web_driver_waiter,
    )

    print(table_data)


if __name__ == "__main__":
    get_all_sales_steam_data_routine()
