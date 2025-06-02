import requests
from html2image import Html2Image

def capture_screenshot(url):
    try:
        hti = Html2Image()
        hti.screenshot(url=url, save_as='screenshot.png')
        print("[+] Screenshot saved as screenshot.png")
    except Exception as e:
        print(f"[!] Error capturing screenshot: {e}")

