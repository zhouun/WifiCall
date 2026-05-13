#!/usr/bin/env python3
import pathlib
import yaml
import urllib.request
import urllib.error

ROOT = pathlib.Path(__file__).resolve().parent.parent
LOCAL_SOURCE = ROOT / 'WifCall.yaml'
MERGED_SOURCE = ROOT / 'WifCall-merged.yaml'
UPSTREAMS_CONFIG = ROOT / 'scripts' / 'upstreams.yml'


def load_yaml(path):
    with path.open('r', encoding='utf-8') as f:
        return yaml.safe_load(f) or {}


def fetch_url(url):
    request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(request, timeout=30) as response:
        raw = response.read()
    return raw.decode('utf-8', errors='ignore')


def parse_plain_text(text):
    rules = []
    allowed_prefixes = (
        'DOMAIN-SUFFIX',
        'DOMAIN-KEYWORD',
        'DOMAIN',
        'IP-CIDR',
        'IP6-CIDR',
        'SRC-PORT',
        'DST-PORT',
        'GEOIP',
        'PROCESS-NAME',
        'USER-AGENT',
        'URL-REGEX',
        'FINAL',
    )
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith('#') or (line.startswith('[') and line.endswith(']')):
            continue
        if any(line.startswith(prefix) for prefix in allowed_prefixes):
            rules.append(line)
    return rules


def parse_yaml_text(text, key=None):
    data = yaml.safe_load(text) or {}
    if isinstance(data, dict):
        if key and key in data:
            return data[key] or []
        if 'rules' in data:
            return data['rules'] or []
        for value in data.values():
            if isinstance(value, list):
                return value
        return []
    if isinstance(data, list):
        return data
    return []


def load_upstream_sources():
    if not UPSTREAMS_CONFIG.exists():
        return []
    content = load_yaml(UPSTREAMS_CONFIG)
    return content.get('sources', []) or []


def merge_rules(base_rules, upstream_rules):
    seen = set()
    merged = []
    for rule in base_rules + upstream_rules:
        if not isinstance(rule, str):
            continue
        normalized = rule.strip()
        if not normalized or normalized in seen:
            continue
        seen.add(normalized)
        merged.append(normalized)
    return merged


def main():
    if not LOCAL_SOURCE.exists():
        raise FileNotFoundError(f'Missing source file: {LOCAL_SOURCE}')

    local_data = load_yaml(LOCAL_SOURCE)
    local_rules = []
    if isinstance(local_data, dict) and 'rules' in local_data:
        local_rules = local_data['rules'] or []
    elif isinstance(local_data, list):
        local_rules = local_data

    upstream_sources = load_upstream_sources()
    merged_rules = list(local_rules)

    if upstream_sources:
        print(f'Found {len(upstream_sources)} upstream sources.')
    else:
        print('No upstream sources configured; using local WifCall.yaml only.')

    for source in upstream_sources:
        name = source.get('name', source.get('url', '<unknown>'))
        url = source.get('url')
        source_type = source.get('type', 'plain')
        key = source.get('key')

        if not url:
            print(f'Warning: upstream source {name} has no url configured, skipped.')
            continue

        try:
            print(f'Fetching {name}: {url}')
            content = fetch_url(url)
        except (urllib.error.URLError, urllib.error.HTTPError) as err:
            print(f'Warning: failed to fetch {name}: {err}')
            continue

        if source_type == 'yaml':
            rules = parse_yaml_text(content, key=key)
        else:
            rules = parse_plain_text(content)

        print(f'  Retrieved {len(rules)} rules from {name}.')
        merged_rules = merge_rules(merged_rules, rules)

    if MERGED_SOURCE.exists():
        existing = load_yaml(MERGED_SOURCE).get('rules', []) if MERGED_SOURCE.exists() else []
        if existing == merged_rules:
            print('Merged rules unchanged; no write needed.')
            return

    with MERGED_SOURCE.open('w', encoding='utf-8') as f:
        f.write('# Generated from WifCall.yaml and upstream sources\n')
        yaml.dump({'rules': merged_rules}, f, allow_unicode=True, sort_keys=False)

    print(f'Wrote merged rule file: {MERGED_SOURCE}')


if __name__ == '__main__':
    main()
