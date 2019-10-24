import yaml

# with open('../data/data.yaml', "r", encoding="utf-8")as f:
#     print(yaml.load(f))


with open('../data/data.yaml', "w", encoding="utf-8") as f:
    data = {"name": "康康", "age": 18}

    yaml.dump(data, f, allow_unicode=True)
