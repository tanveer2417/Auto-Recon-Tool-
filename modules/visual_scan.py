import subprocess

def capture_screenshot(url, output='screenshot.png'):
    try:
        cmd = ['wkhtmltoimage', url, output]
        subprocess.run(cmd, check=True)
        print(f"[+] Screenshot saved as {output}")
    except subprocess.CalledProcessError as e:
        print(f"[!] Screenshot failed: {e}")
