## Sentry 钉钉机器人插件

 - 发送异常信息至钉钉机器人
 - 本插件可兼容 Sentry 自身限流功能
 - 可通过 `docker-compose logs -f --tail=100` 查看插件日志信息 (例如使用 [onpremise](https://github.com/getsentry/onpremise) 部署)

## 安装

```bash
$ pip install sentry-dingtalk-metaapp
```

## 使用

在 `项目` 的`集成(Legacy Integrations)`页面找到 `钉钉机器人` 插件启用并设置 `Access Token`

## 参照仓储

 - [sentry_dingtalk_xz](https://github.com/1018ji/sentry_dingtalk_xz)
