# WiFi Calling 规则使用说明

本说明适用于 `WifCall-clash.yaml`、`WifCall-plain.txt` 和 `WifCall-universal.yaml`，这些专用规则文件可在常见 Android、iOS、Windows、macOS 和 Linux 客户端中使用。

## 1. 通用要求

- 目标代理组名称：`WiFiCall`
- 规则类型：`DOMAIN-SUFFIX`、`DOMAIN-KEYWORD`、`IP-CIDR`
- 请确保你的代理配置中存在名为 `WiFiCall` 的代理组或节点

## 2. 专用文件说明

- `WifCall-clash.yaml`：Clash 家族专用，适用于 Clash、ClashX、Clash for Windows、Clash for Android、Clash Premium 等。
- `WifCall-plain.txt`：通用规则列表，适用于 Surge、Shadowrocket、Quantumult X、Quantumult、V2RayN、Qv2ray、Loon、Egeran 以及其他支持标准规则列表的客户端。
- `WifCall-loon.txt`：Loon 专用规则列表，适用于 Loon iOS / Loon macOS。
- `WifCall-universal.yaml`：标准 YAML 规则文件，适用于支持 YAML 导入的客户端。

## 3. 自动生成说明

本仓库使用 `WifCall.yaml` 作为主规则源，并支持从上游配置抓取并合并：

- `scripts/upstreams.yml`：配置上游规则源
- `scripts/fetch-and-merge-upstreams.py`：抓取上游规则源并生成 `WifCall-merged.yaml`
- `scripts/generate-rule-files.py`：从 `WifCall-merged.yaml`（如果存在）或 `WifCall.yaml` 生成其他客户端专用格式文件
- `.github/workflows/auto-update.yml`：在 `main` 分支推送或每日定时运行时自动抓取、生成并提交更新

当前配置的上游源：

- `https://raw.githubusercontent.com/zrt02/T-mobile-wifi-calling-rules/main/T-Mobile.yaml`
- `https://raw.githubusercontent.com/supermiillk/openclash_private/main/WifiCalling-Rules/apple-check.yaml`
- `https://raw.githubusercontent.com/supermiillk/openclash_private/main/WifiCalling-Rules/esim-us.yaml`
- `https://raw.githubusercontent.com/DylanSmith025/WiFicalling_SurgeModule/main/Wi-Fi%20calling.sgmodule`

## 4. Android 客户端

## 3. Android 客户端

### Clash for Android

1. 将 `WifCall-clash.yaml` 放到本地存储或上传为远程文件。
2. 在 Clash for Android 中，进入 “Profiles” / “配置” 页面。
3. 点击 “导入” 并选择本地文件或输入远程 URL。
4. 确认规则文件已加载。
5. 在配置中确保 `WiFiCall` 代理组存在，并绑定到一个可用代理节点。

### V2RayNG / NaiveProxy

1. 如果客户端支持自定义规则文件，将 `WifCall-plain.txt` 导入或添加为规则源。
2. 如果只支持单条规则，需要将 `DOMAIN-SUFFIX` / `DOMAIN-KEYWORD` 转换为客户端支持的格式。
3. 保证 `WiFiCall` 目标组对应到一个实际代理。

### 其他 Android 客户端

- ShadowsocksR Android：如果支持自定义规则文件，可直接导入 `WifCall-plain.txt`；若仅支持纯文本规则，请将 TXT 中规则逐行复制。
- Kitsunebi / Potatso Android：同样可导入标准规则文件，若仅支持远程 URL，可使用静态托管服务。
- 绝大多数支持 `DOMAIN-SUFFIX` / `DOMAIN-KEYWORD` 的客户端都能兼容 `WifCall-plain.txt`。

## 4. iOS 客户端

### Shadowrocket

1. 打开 Shadowrocket。
2. 进入 “配置” 页面。
3. 使用 “导入” 功能导入 `WifCall-plain.txt` 或远程 URL。
4. 进入规则编辑页面，确认规则已加载。
5. 确保 `WiFiCall` 节点组存在并已配置正确代理。

### Loon

1. 打开 Loon。
2. 进入 `配置` -> `规则` 或 `规则列表`。
3. 导入 `WifCall-loon.txt` 本地文件或远程 URL。
4. 确认 `WiFiCall` 代理组已存在，并将规则组与该组绑定。

### Egeran

1. 打开 Egeran。
2. 找到 `规则` 或 `规则列表` 导入选项。
3. 导入 `WifCall-plain.txt` 本地文件或远程 URL。
4. 确认 `WiFiCall` 代理组已存在，并与规则绑定。

### Quantumult X / Quantumult

1. 打开 Quantumult X。
2. 进入 “配置” 页面，选择 “导入” 或 “更多配置”。
3. 添加 `WifCall-plain.txt` 作为规则文件。
4. 在规则中确保 `WiFiCall` 代理组存在。

### Surge iOS

1. 打开 Surge，进入 `配置` -> `模块`。
2. 在 `规则` 部分导入或粘贴 `WifCall-plain.txt`。
3. 确保你的 Surge 配置内存在 `WiFiCall` 代理组，并将此规则文件与该组关联。

### 其他 iOS 客户端

- Kitsunebi / Potatso：支持导入远程规则文件或本地规则文件。
- Shadowrocket：支持标准代理规则文件导入。
- Quantumult / Quantumult X：支持一般规则文件和 `rule-providers` 源。
- Surge for iOS：可导入标准规则文件并绑定至 `WiFiCall` 组。

## 5. Windows 客户端

### Clash for Windows

1. 打开 Clash for Windows。
2. 在 `Profiles` 页面选择 `Import` / `导入`。
3. 导入 `WifCall-clash.yaml` 本地文件或远程 URL。
4. 在配置文件中创建或确认存在名为 `WiFiCall` 的代理组。
5. 如果使用 `rule-providers`，可将文件引用写入主配置：

```yaml
rule-providers:
  WiFiCall:
    type: http
    behavior: classical
    path: ./WifCall-clash.yaml
    url: 'https://example.com/WifCall-clash.yaml'
```

### V2RayN / Shadowsocks-Windows

- V2RayN：如果支持导入外部规则文件，可按相同方式导入；若仅支持本地规则，请复制 `WifCall-plain.txt` 内容到规则列表。
- Shadowsocks-Windows：通常使用 `Pac` 或自定义规则列表，若支持 `DOMAIN-SUFFIX` / `DOMAIN-KEYWORD`，可直接导入 `WifCall-plain.txt`。
- Qv2ray：支持自定义规则源，可使用远程 URL 或本地文件方式加载 `WifCall-plain.txt`。

## 6. macOS 客户端

### ClashX / ClashX Pro

1. 打开 ClashX。
2. 点击 `Profiles` -> `Import`。
3. 导入本地 `WifCall-clash.yaml` 文件或填写远程 URL。
4. 确认 `WiFiCall` 代理组存在并与实际代理节点关联。

### Surge for macOS

1. 打开 Surge。
2. 进入 `Manage Configurations` -> `Rules`。
3. 导入或复制 `WifCall-plain.txt` 内容。
4. 确保 `WiFiCall` 组已配置。

## 7. Linux 客户端

### Clash / Clash Premium

1. 将 `WifCall-clash.yaml` 放到 Linux 机上的一个目录。
2. 在主配置文件中添加 `rule-providers`：

```yaml
rule-providers:
  WiFiCall:
    type: http
    behavior: classical
    path: ./WifCall-clash.yaml
    url: 'file:///path/to/WifCall-clash.yaml'
```

3. 或者直接将其内容合并到 `rules:` 列表中。
4. 确保主配置中存在 `WiFiCall` 组。

### 其他 Linux 代理客户端

- 如果客户端支持读取标准规则文件，可直接导入 `WifCall-plain.txt`。
- 如果客户端只支持规则列表，请将 TXT 内的规则依次复制到其规则项中。

## 7. 注意事项

- `WifCall-universal.yaml` 是通用规则文件，已尽量避免客户端专属语法。
- 如果你的客户端对 `rule-providers` 或 `DOMAIN-KEYWORD` 的兼容性有限，请先测试导入单条规则。
- 若客户端不识别 `WiFiCall` 组名称，可手动改为客户端当前配置中实际代理组名。
