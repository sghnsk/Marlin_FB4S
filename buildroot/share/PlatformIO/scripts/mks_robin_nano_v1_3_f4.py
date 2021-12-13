#
# buildroot/share/PlatformIO/scripts/mks_robin_nano_v1_3_f4.py
#
Import("env")
import requests


def upload(source, target, env):
    firmware_path = str(source[0])
    upload_host = env.get('UPLOAD_PORT')
    url = f'http://{upload_host}/upload?X-Filename=Robin_Nano35.bin'
    headers = {
        'Content-Type': 'application/octet-stream'
    }
    r = None
    try:
        r = requests.post(
            url,
            data=open(firmware_path, "rb"),
            headers=headers,
        )
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        sys.stderr.write("Failed to upload firmware: %s\n" %
                         ("%s\n%s" % (r.status_code, r.text) if r else str(e)))
        env.Exit(1)


env.Replace(UPLOADCMD=upload)
