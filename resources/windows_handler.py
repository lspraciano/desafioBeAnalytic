import time

from selenium import webdriver


def focus_windows_by_name(
        windows_name: str,
        web_driver: webdriver,
):
    max_wait_time: int = 5
    current_wait_time: int = 0

    while current_wait_time < max_wait_time:
        all_handles: list[str] = web_driver.window_handles
        for handle in all_handles:
            web_driver.switch_to.window(window_name=handle)
            if web_driver.title == windows_name:
                return

        time.sleep(0.5)
        current_wait_time += 0.5

    raise Exception(
        f"Title: {windows_name} | Maximum wait time exceeded to focus"
    )


def close_windows_by_name(
        windows_name: str,
        web_driver: webdriver,
):
    max_wait_time: int = 5
    current_wait_time: int = 0

    while current_wait_time < max_wait_time:
        all_handles: list[str] = web_driver.window_handles
        for handle in all_handles:
            web_driver.switch_to.window(window_name=handle)
            if web_driver.title == windows_name:
                web_driver.close()
                return

        time.sleep(0.5)
        current_wait_time += 0.5

    raise Exception(
        f"Title: {windows_name} | Maximum wait time exceeded to close by name"
    )


def close_all_windows_except_name(
        windows_name: str,
        web_driver: webdriver,
):
    focus_windows_by_name(
        windows_name=windows_name,
        web_driver=web_driver
    )

    all_handles: list[str] = web_driver.window_handles
    for handle in all_handles:
        web_driver.switch_to.window(window_name=handle)
        if web_driver.title != windows_name:
            web_driver.close()
