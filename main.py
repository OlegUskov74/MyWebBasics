import os
# Импорт встроенной библиотеки для работы веб-сервера
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

# Для начала определим настройки запуска
hostName = "localhost" # Адрес для доступа по сети
serverPort = 8080 # Порт для доступа по сети

class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """
    ROOT_DIR = os.path.dirname(__file__)

    def do_GET(self):
        """
        Метод для обработки входящих GET-запросов
        """
        match self.path:
            case "/main": path = self.ROOT_DIR + "/main.html"
            case "/catalog": path = self.ROOT_DIR + "/catalog.html"
            case "/category": path = self.ROOT_DIR + "/category.html"
            case "/contacts": path = self.ROOT_DIR + "/contacts.html"
            case _: path = self.ROOT_DIR + "/main.html"

        self.send_response(200) # Отправка кода ответа
        self.send_header("Content-type", "text/html") # Отправка типа данных, который будет передаваться
        self.end_headers() # Завершение формирования заголовков ответа

        with open(path, mode="r", encoding="UTF-8") as f:
            self.wfile.write(bytes(f.read(), "utf-8"))  # Тело ответа

if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрах в сети
    # принимать запросы и отправлять их на обработку специальному классу, описанному выше.
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Старт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")