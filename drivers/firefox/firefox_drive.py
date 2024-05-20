import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from configuration.configs import settings


def get_firefox_drive(
        firefox_on_background: bool = False
) -> tuple[webdriver.Firefox, WebDriverWait]:
    firefox_download_path: str = os.path.abspath(
        f"{settings.ROOT_PATH_FOR_DYNACONF}/{settings.DOWNLOADS_PATH}/"
    )

    if not os.path.exists(firefox_download_path):
        raise Exception("Download directory path is not valid")

    firefox_options: webdriver.FirefoxOptions = webdriver.FirefoxOptions()

    if firefox_on_background:
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")
        firefox_options.add_argument("--disable-logging")

    firefox_options.set_preference("browser.download.panel.shown", False)
    firefox_options.set_preference("browser.download.animateNotifications", False)
    firefox_options.set_preference("browser.download.dir", firefox_download_path)
    firefox_options.set_preference("browser.download.folderList", 2)
    firefox_options.set_preference("browser.helperApps.alwaysAsk.force", False)
    firefox_options.set_preference("browser.download.manager.showWhenStarting", False)
    firefox_options.set_preference(
        "browser.helperApps.neverAsk.saveToDisk",
        (
            "application/pdf, application/zip, application/octet-stream, "
            "text/csv, text/xml, application/xml, text/plain, "
            "text/octet-stream, application/x-gzip, application/x-tar "
            "application/"
            "vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        ),
    )

    drive_firefox: webdriver.Firefox = webdriver.Firefox(
        options=firefox_options
    )

    firefox_waiter: WebDriverWait = WebDriverWait(
        driver=drive_firefox,
        timeout=settings.WAIT_TIME_IN_SECONDS
    )

    return drive_firefox, firefox_waiter


def clear_firefox_web_drive(
        firefox_web_drive: webdriver,
        firefox_web_driver_waiter: WebDriverWait
) -> None:
    firefox_web_drive.quit()

    del firefox_web_drive
    del firefox_web_driver_waiter
