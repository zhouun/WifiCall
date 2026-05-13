# WifiCall

这是一个面向全平台的 WiFi Calling 规则集，适用于 Clash、Surge、Quantumult X 等支持 `DOMAIN-SUFFIX`、`DOMAIN-KEYWORD` 和 `IP-CIDR` 规则的代理软件。

## 说明

- 覆盖 Apple iOS、Android 以及通用 ePDG / IMS 域名规则
- 包含运营商特定规则和全局通用 3GPP WiFi Calling 域名回退规则
- 目标代理组名称为 `WiFiCall`

## 使用方式

1. 在你的代理配置中引入 `WifCall-clash.yaml`、`WifCall-plain.txt` 或 `WifCall-universal.yaml`
2. 使用支持的规则引擎加载该文件
3. 确保你的代理组里存在 `WiFiCall` 目标

## 专用文件说明

- `WifCall-clash.yaml`：Clash 家族专用，适用于 Clash、ClashX、Clash for Windows、Clash for Android、Clash Premium 等客户端。
- `WifCall-plain.txt`：通用规则列表，适用于 Surge、Shadowrocket、Quantumult X、Quantumult、V2RayN、Qv2ray、Egeran 以及其他支持标准规则列表的客户端。
- `WifCall.list`：标准 `.list` 规则文件，可直接用于支持 `.list` 的客户端或订阅系统。
- `WifCall.snippet`：规则片段文件，适用于 Surge / Shadowrocket / Loon 等支持片段导入的客户端。
- `WifCall-loon.txt`：Loon 专用规则列表，适用于 Loon iOS / Loon macOS。
- `WifCall-universal.yaml`：标准 YAML 规则文件，适用于支持 YAML 导入的客户端。

## 自动生成和更新

本仓库包含 GitHub Actions 自动生成流程：

- `scripts/fetch-and-merge-upstreams.py`：从 `scripts/upstreams.yml` 中的上游源抓取规则并生成 `WifCall-merged.yaml`
- `scripts/generate-rule-files.py`：从 `WifCall-merged.yaml`（如果存在）或 `WifCall.yaml` 生成 `WifCall-universal.yaml`、`WifCall-clash.yaml`、`WifCall-plain.txt`、`WifCall-loon.txt`
- `.github/workflows/auto-update.yml`：在 `main` 分支推送或按计划运行时自动抓取、生成并推送更新

当前配置的上游源：

- `https://raw.githubusercontent.com/zrt02/T-mobile-wifi-calling-rules/main/T-Mobile.yaml`
- `https://raw.githubusercontent.com/supermiillk/openclash_private/main/WifiCalling-Rules/apple-check.yaml`
- `https://raw.githubusercontent.com/supermiillk/openclash_private/main/WifiCalling-Rules/esim-us.yaml`
- `https://raw.githubusercontent.com/DylanSmith025/WiFicalling_SurgeModule/main/Wi-Fi%20calling.sgmodule`

## 平台使用说明

详见 `USAGE.md`，其中包含每种客户端的导入方式和配置提示。

## 规则集内容

`WifCall.yaml` / `WifCall-universal.yaml` 包含：

- Apple 设备基础资格审查规则
- 主要运营商的 ePDG / WiFi Calling 域名和 IP 范围
- 全平台通用回退规则，保证更高命中率
