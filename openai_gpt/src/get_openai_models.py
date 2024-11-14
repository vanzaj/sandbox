from datetime import datetime
from api import client

models = [(m.id, m.created) for m in client.models.list()]
for model in sorted(models, key=lambda x: x[1]):  # sort by datetime
    print(f"{model[0]}, created: {datetime.fromtimestamp(model[1])}")
