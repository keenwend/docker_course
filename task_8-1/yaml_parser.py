import yaml

with open("yaml_file_8-3.yaml") as f:
    templates = yaml.safe_load(f)

print(templates)