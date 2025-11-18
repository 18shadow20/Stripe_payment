Django + Stripe Checkout


Требования:

Docker

Настройка проекта:

Создай файл .env в корне проекта с тестовыми ключами Stripe:

STRIPE_PUBLIC_KEY=pk_test_XXXXXXXXXXXXXXXX

STRIPE_SECRET_KEY=sk_test_XXXXXXXXXXXXXXXX

Запуск на сервере:

1.Устанавливаем Docker

2.Копируем проект + .env на сервер

3.Выполнить:

docker-compose build

docker-compose up -d

4.проверка товара: http://127.0.0.1:8000/payment/item/1/
 
 админка: http://127.0.0.1:8000/admin/















