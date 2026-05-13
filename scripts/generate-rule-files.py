#!/usr/bin/env python3
import pathlib
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
MERGED_SOURCE = ROOT / 'WifCall-merged.yaml'
SOURCE = MERGED_SOURCE if MERGED_SOURCE.exists() else ROOT / 'WifCall.yaml'

with SOURCE.open('r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

rules = data.get('rules', [])

# write universal YAML
universal_path = ROOT / 'WifCall-universal.yaml'
with universal_path.open('w', encoding='utf-8') as f:
    f.write('# Generated from WifCall.yaml\n')
    yaml.dump({'rules': rules}, f, allow_unicode=True, sort_keys=False)

# write clash YAML
clash_path = ROOT / 'WifCall-clash.yaml'
with clash_path.open('w', encoding='utf-8') as f:
    f.write('# Generated for Clash family from WifCall.yaml\n')
    yaml.dump({'rules': rules}, f, allow_unicode=True, sort_keys=False)

# write plain text rule list
plain_path = ROOT / 'WifCall-plain.txt'
with plain_path.open('w', encoding='utf-8') as f:
    f.write('# Generated from WifCall.yaml\n')
    f.write('# Suitable for Surge / Shadowrocket / Quantumult X / Quantumult / V2RayN / Qv2ray / Egeran / other standard list clients\n')
    for rule in rules:
        if isinstance(rule, str):
            f.write(f'{rule}\n')

# write Loon rule list
loon_path = ROOT / 'WifCall-loon.txt'
with loon_path.open('w', encoding='utf-8') as f:
    f.write('# Generated from WifCall.yaml\n')
    f.write('# Suitable for Loon iOS / Loon macOS\n')
    for rule in rules:
        if isinstance(rule, str):
            f.write(f'{rule}\n')

print('Generated rule files: WifCall-universal.yaml, WifCall-clash.yaml, WifCall-plain.txt, WifCall-loon.txt')
