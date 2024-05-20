from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from pages.steam.steam_infos_sales_page import SteamInfosSalesPage


def list_all_sales_data_on_table_task(
        firefox_web_drive: webdriver,
        firefox_web_driver_waiter: WebDriverWait,
        option_value: str = "-1",
        start_date_filter: str | None = None,
        end_date_filter: str | None = None,
):
    steam_info_sales_page: SteamInfosSalesPage = SteamInfosSalesPage(
        web_driver=firefox_web_drive,
        web_driver_waiter=firefox_web_driver_waiter,
    )

    steam_info_sales_page.open_page()

    if start_date_filter:
        steam_info_sales_page.set_start_date_filter(value=start_date_filter)

    if end_date_filter:
        steam_info_sales_page.set_end_date_filter(value=end_date_filter)

    if start_date_filter or end_date_filter:
        steam_info_sales_page.click_button_filter()

    steam_info_sales_page.set_pagination_option_by_value(value=option_value)
