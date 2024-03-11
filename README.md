# Litres

## Проект по автоматизации тестирования интернет магазина

<p align="center">
<img src="resources/logo/Litres-logo-2022.png" width="800" height="200">
</p>

----

### Особенности проекта:

- Удаленный запуск через Jenkins
- Отчетность в allure
- Запись логов, скриншотов и видео
- Оповещение в Telegram
- Протестированы интерфейсы web, api, mobile

### Стек проекта:

Python * Pytest * Selene * (Selenium) * Selenoid * Jenkins * Allure Report * Telegram * Intellij (PyCharm)

<p align="left">
<img align="center" src="resources/logo/python-original-wordmark.svg" width="40" height="40">
<img align="center" src="resources/logo/pytest-original-wordmark.svg" width="40" height="40">
<img align="center" src="resources/logo/selenium-original.svg" width="40" height="40">
<img align="center" src="resources/logo/jenkins-original.svg" width="40" height="40">
<img align="center" src="resources/logo/selenoid-image.jpeg" width="40" height="40">
<img align="center" src="resources/logo/github-original-wordmark.svg" width="40" height="40">
<img align="center" src="resources/logo/allure.png" width="40" height="40">
<img align="center" src="resources/logo/Telegram_logo.webp" width="40" height="40">
<img align="center" src="resources/logo/intellij-original-wordmark.svg" width="40" height="40">
<img align="center" src="resources/logo/androidstudio-original.svg" width="40" height="40">
<img align="center" src="resources/logo/appium_logo.png" width="40" height="40">
<img align="center" src="resources/logo/allure_testops_logo.png" width="40" height="40">
</p>

----

### Какие проверки реализованы в тестах:

#### WEB

- Корзина
-
    - Добавление книги в корзину
-
    - Удаление книги из корзины
- Избранное
-
    - Добавление книги в избранное
-
    - Удаление книги из избранного
-
    - Работа счетчика корзины и избранного
-
    - Добавление книги в отложенное через удаление из корзины
- Авторизация
-
    - Успешная авторизация
-
    - Неуспешная авторизация с неправильным паролем
-
    - Проверка почты для регистрации
-
    - Проверка почты для авторизации
- Поиск книги
-
    - Успешный поиск книги
-
    - Проверка поиска неправильного названия

#### MOBILE

- Авторизация
- Добавление книги в избранное
- Поиск книги

#### API

- Корзина
-
    - Добавление в корзину книги/нескольких книг
-
    - Отображение добавленных книг
- Авторизация
-
    - Авторизация успешная
-
    - Авторизация неуспешная
-
    - Проверка почты для регистрации
-
    - Проверка почты для авторизации
- Поиск
-
    - Поиск книги по названию
-
    - Поиск книги по неправильному названию

----

## Запуск проекта:

### Через Jenkins

Ссылка на [Ссылка на проект в Jenkins]("https://jenkins.autotests.cloud/job/Rolnik_QA_Guru_Diplom_litres/")  
<img src="resources/screens/jenkins_allure.png"  width="800" height="500">

1. Нажмите на кнопку "build with parameters" (собрать с параметрами)  
   <img src="resources/screens/jenkins_inteface.png"  width="190" height="270">
2. Выберите интерфейс тестирования. Доступны API, WEB или Mobile
   Также можно написать комментарий, который будет отправлен в Telegram после окончания сборки

- Нажмите build
  <img src="resources/screens/build_paramters.png">

3. Когда тест будет пройден, можно посмотреть подрбности в отчете Allure  
   Для это нужно нажать на иконку allure отчета <img src="resources/logo/allure.png" width="20" height="20">

----

## Локальный запуск

### Настройка устройства для мобильных тестов

Более подробно можно почитать тут:
<a target="_blank" href="https://autotest.how/appium-setup-for-local-android-tutorial-md">Конспект инструкций по
настройке системы и устройств для локального запуска мобильных тестов на платформе Android</a>

### Подгтовка к запуску

1. Клонируйте репозиторий на свой компьютер при помощи git clone

  ```zsh
git clone
  ```

2. Создайте и активируйте виртуальное окружение

  ```zsh
  python -m venv .venv
  source venv/bin/activate
  ```

3. Установите зависимости с помощью pip

  ```zsh
  pip install -r requirements.txt
  ```

----

#### Для запуска WEB автотестов

используйте команду в терминале

  ```zsh
   pytest tests/web
  ```

#### Для запуска API автотестов

используйте команду в терминале

  ```zsh
   pytest tests/api
  ```

---

#### Для запуска мобильных автотестов

- Запустите сервер локально используя команду

```zsh
appium --base-path /wd/hub
  ```

##### Запуск на личном смартфоне

1. Подключите ваше устройство и включите режим разработчика на нем
2. Используйте данные из команды чтобы заполнить udid в env.local_real_device

  ```zsh
  adb devices
  ```

3. Для запуска используйте команду

  ```zsh
  pytest tests/mobile/android --context=local_real_device
  ```

4. Для получения allure отчета

  ```zsh
  allure serve allure-results
  ``` 

##### Запуск на эмуляторе

1. Запустите эмулятор через Android studio
2. Используйте данные из команды чтобы заполнить udid в env.local_emulator

  ```zsh
  adb devices
  ```

3. Для запуска используйте команду

  ```zsh
  pytest tests/mobile/android --context=local_emulator
  ```

4. Для получения allure отчета

  ```zsh
  allure serve allure-results
  ``` 

---

### Для запуска проекта через browserstack

1. Зарегистрируйтесь на сайте https://app-automate.browserstack.com/
2. Скачайте `.apk` приложение из публичного репозитория. Загрузите его в Browserstack
3. Добавьте ваши "User Name", "Access Key" и ссылку на установленное приложение в файлы env.bstack и env.credentials
4. Для запуска используйте команду

  ```zsh
  pytest --context=bstack
  ```

5. Для получения allure отчета

  ```zsh
  allure serve allure-results
  ```

---

## Отчеты

#### Структура Allure отчета

![This is an image](resources/screens/Allure_report.png)

- Можно раскрыть тесты и увидеть подробности сборки

<p align="center">
<img src="resources/screens/allure_tests.png" width="800" height="500">
</p>
- Можно посмотреть запись прохождения теста  
<p align="center">
<img src="resources/screens/litres_test_web.gif" width="800" height="500">
</p>

### Интеграция с Allure TestOps

> <a target="_blank" href="https://allure.autotests.cloud/project/4124/dashboards">Ссылка на проект в
> AllureTestOps</a>

<p align="center">
<img src="resources/screens/test_ops_dashboard.png" width="800" height="500">
</p>

#### Cписок тест кейсов проекта

![This is an image](resources/screens/Allure-test-cases.png)

---

#### При прохождении тестов через Browserstack можно получить видео прохождения тестов

Пример:
<p align="center">
  <img title="Browsestack video" src="resources/screens/bstack_litres.gif" alt="Video" width="400">
</p>

---

### Telegram: <img src="resources/logo/Telegram_logo.webp" width="20" height="20">

Возможна интеграция в Telegram, для более удобных оповещений.

Нужен бот в Telegram @BotFather и чат с правами администратора.
<p align="center">
<img src="resources/logo/botfaher.png" width="290" height="300">
</p>

Пример отчета в Telegram
<p align="center">
<img src="resources/logo/telegram.png" width="290" height="300">
</p>
