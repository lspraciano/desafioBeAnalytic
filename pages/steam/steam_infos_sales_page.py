from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select

from resources.windows_handler import focus_windows_by_name, close_windows_by_name


class SteamInfosSalesPage:
    def __init__(
            self,
            web_driver: webdriver,
            web_driver_waiter: WebDriverWait
    ):
        self.page_title: str = "Steam Endless Replayability Fest · BR · SteamDB"
        self.page_url: str = f"https://steamdb.info/sales/"
        self.web_driver: webdriver = web_driver
        self.web_driver_waiter: WebDriverWait = web_driver_waiter

    def open_page(self) -> None:
        self.web_driver.get(self.page_url)
        self.web_driver_waiter.until(EC.element_to_be_clickable((By.ID, "js-filters-reset")))

    def set_pagination_option_by_value(self, value: str) -> None:
        select_field: WebElement = self.web_driver_waiter.until(EC.element_to_be_clickable((By.ID, "dt-length-0")))
        Select(select_field).select_by_value(value=value)

    def set_start_date_filter(self, value: str) -> None:
        start_date: WebElement = self.web_driver_waiter.until(
            EC.element_to_be_clickable((By.ID, "js-input-release-min")))
        start_date.send_keys(value)

    def set_end_date_filter(self, value: str) -> None:
        end_date: WebElement = self.web_driver_waiter.until(
            EC.element_to_be_clickable((By.ID, "js-input-release-max")))
        end_date.send_keys(value)

    def click_button_filter(self) -> None:
        button: WebElement = self.web_driver_waiter.until(
            EC.element_to_be_clickable((By.ID, "js-filter-submit")))
        button.click()

    def focus_page(self) -> None:
        focus_windows_by_name(
            windows_name=self.page_title,
            web_driver=self.web_driver
        )

    def close_window(self) -> None:
        close_windows_by_name(
            windows_name=self.page_title,
            web_driver=self.web_driver
        )

    def get_table_data(self) -> list[dict] | None:
        table_data: list[dict] = []
        table: WebElement = self.web_driver_waiter.until(
            EC.element_to_be_clickable((By.ID, "DataTables_Table_0")))
        rows: list[WebElement] = table.find_elements(By.TAG_NAME, "tr")
        headers: list[dict] = [
            {"name": "col0", "type": "ignore"},
            {"name": "image", "type": "ignore"},
            {"name": "Name", "type": "str"},
            {"name": "%", "type": "float"},
            {"name": "Price", "type": "float"},
            {"name": "Rating", "type": "float"},
            {"name": "Release", "type": "datetime"},
            {"name": "Ends", "type": "datetime"},
            {"name": "Started", "type": "datetime"},
        ]

        for row in rows[1:]:
            row_data: dict = {}
            cells: list[WebElement] = row.find_elements(By.TAG_NAME, "td")

            for index, cell in enumerate(cells):
                current_cell_text: str = cell.text
                current_cell_data_sort: str = cell.get_attribute("data-sort")
                header_name: str = headers[index]["name"]
                header_type: str = headers[index]["type"]

                if current_cell_text == "No data available in table":
                    return None

                if header_type == "ignore":
                    continue

                if header_type != "datetime":
                    dict_cell_data: str = current_cell_text
                else:
                    timestamp: int = int(current_cell_data_sort)
                    date_time: datetime = datetime.utcfromtimestamp(timestamp)
                    dict_cell_data: str = date_time.strftime("%Y-%m-%d %H:%M:%S")

                row_data[header_name]: str = dict_cell_data

            table_data.append(row_data)
        return table_data
