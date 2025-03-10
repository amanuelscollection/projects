from . import orders, order_details, menu, payment_info, resource_management, rewards, customers
# Change 'resource_management' to 'resourceManagement'

from ..dependencies.database import engine

def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    payment_info.Base.metadata.create_all(engine)
    resource_management.Base.metadata.create_all(engine)
    menu.Base.metadata.create_all(engine)
    rewards.Base.metadata.create_all(engine)
    customers.Base.metadata.create_all(engine)
