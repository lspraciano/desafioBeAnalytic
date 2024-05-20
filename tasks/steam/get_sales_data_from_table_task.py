from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from pages.steam.steam_infos_sales_page import SteamInfosSalesPage


def get_sales_data_from_table_task(
        firefox_web_drive: webdriver,
        firefox_web_driver_waiter: WebDriverWait
) -> list[dict] | None:
    steam_info_sales_page: SteamInfosSalesPage = SteamInfosSalesPage(
        web_driver=firefox_web_drive,
        web_driver_waiter=firefox_web_driver_waiter,
    )

    return steam_info_sales_page.get_table_data()
