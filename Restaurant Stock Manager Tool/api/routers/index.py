from . import customers, orders, order_details, payment_info, menu, rewards,resource_management


def load_routes(app):
    app.include_router(customers.router)
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(payment_info.router)
    app.include_router(menu.router)
    app.include_router(rewards.router)
    app.include_router(resource_management.router)
