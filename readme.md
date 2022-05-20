1. git clone https://github.com/matsubVs/ranks-test.git
2. cd ranks-test
3. touch app.env
   1. Заполнить по примеру:</br>
        POSTGRES_USER=<pg_user> <br/>
        POSTGRES_NAME=<db_name> <br/>
        POSTGRES_PASSWORD=<pg_user_pass> <br/>
        SECRET_KEY=<django_secret_key> <br/>
        STRIPE_PUBLISHABLE_KEY=<stripe_publish_key> <br/>
        STRIPE_SECRET_KEY=<stripe_secret_key> <br/>
3. docker-compose build
4. docker-compose run ranks poetry run python manage.py createsuperuser
5. docker-compose up
6. 0.0.0.0:1377/

Чтобы использовать api нужно создать объекты Items или Order
###- Endpoints
- /buy/{item_id}/ -> sessionId для покупки item
- /item/{item_id/ -> HTML страница с кнопкой оплаты
- /order/{order_id} -> sessionId для покупки order
- /order_buy/{order_id} -> HTML страница с кнопкой оплаты

Для использования скидки нужно создать купон в stripe dashboard и создать модель Discount <br/>
*Discount_id основной id купона, а не промокода* <br/> <br/>
Для использование Tax нужно использовать price_id из products в ranks dashboard <br/>
Так как модели item используются без привязки к products из stripe dashboard, использование Tax не реализовано
