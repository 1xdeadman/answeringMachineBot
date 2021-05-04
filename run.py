from gevent.pywsgi import WSGIServer
from server import app
import click
from os.path import isfile


@click.command()
@click.option("--key", "-k", required=True, help="input path to private key file")
@click.option("--cert", "-c", required=True, help="input path to certificate file")
@click.option("--port", "-p", default=443, type=int, help="input listened port")
@click.option("--host", "-h", default="", help="input listened ip")
def run(key, cert, port, host):
    if not isfile(cert) or not isfile(key):
        print(cert)
        print(key)
        print("Wrong path to cert file or key file")
        exit(0)
    http_server = WSGIServer((host, port), app, keyfile=key, certfile=cert)
    http_server.serve_forever()


if __name__ == '__main__':
    run()