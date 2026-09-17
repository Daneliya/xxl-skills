---
name: apifox-sync
description: "This skill should be used when the user asks to sync/import/push one or more HTTP API endpoints into Apifox. Trigger phrases include: 同步接口到apifox、把这个接口保存到apifox、把xxx接口导入Apifox、sync endpoint to Apifox、Apifox 导入接口 etc. It determines the target project and branch (including AI branches) in Apifox, builds a single-endpoint OpenAPI 3.0 file from the Spring controller/method, imports it via the Apifox CLI (apifox import), verifies the endpoint was created, cleans up temp files, and reminds the user about AI-branch merge if needed."
---

# Apifox 接口同步

将 Spring Controller 接口同步/导入 Apifox。用户的 Spring 工程是 tcmp-ucenter（临床教学协同管理平台 V3.0），本机已安装并登录 Apifox CLI（账号 xu_xiaolong，版本 ≥2.2.9）。

当用户要求"同步/保存/导入某个接口到 Apifox"时，按以下 SOP 执行。

## 第一步：明确要同步的接口

1. 定位用户指出的 Controller 方法（可通过行号、注释或方法名定位）。
2. 读取方法注解确认：HTTP 方法、完整路径（类级 `@RequestMapping` 前缀 + 方法路径）、`@RequestBody` 入参类型、返回类型。
3. 读取入参类型、嵌套实体（Request/Entity）与返回实体，收集全部字段及中文注释，用于构建 OpenAPI 的 schema 和示例。

## 第二步：检查 Apifox CLI 环境

- 运行 `apifox --version` 确认已安装；若失败，先提示用户安装/登录。
- 用 `apifox project list` 列出项目，确认目标 projectId。默认项目为「临床教学协同管理平台V3.0」= 5350216。若用户未指定，可默认 5350216；若不确定，询问用户。

## 第三步：确定目标分支

- 默认写入主分支 main，除非用户指定 AI 分支或迭代分支。
- 若用户要求"同步到 AI 分支"：用 `apifox branch list --project <id> --type all` 查看分支。若无合适 AI 分支则创建：
  - 命名必须符合规范 `ai/yyyyMMdd-from-<来源分支名去点号>-<功能名>`，例：`ai/20260904-from-V3-1-saveUserPersonWorkList`（来源分支 `V3.1` 中的点去掉写成 `V3-1`）。
  - 执行 `apifox branch create --project <id> --type ai --name <规范名> --from <来源分支>`。
  - AI 分支初始为空，不会自动复制来源资源。
- 注意：若导入命令因 AI 写入权限被拒（提示 Automation caller branch required / 分支受限），必须先让用户选择：① 在 Apifox「项目设置-功能设置-外部 AI 编辑权限」开启直接编辑；② 改用 AI 分支导入。不要擅自替用户做选择。

## 第四步：生成单接口 OpenAPI 3.0 文件

1. 在系统临时目录（Windows 用 `echo $env:TEMP` 获取，如 `C:\Users\<user>\AppData\Local\Temp`）写一个 json 文件，命名 `<方法名>.openapi.json`。
2. 结构要点：
  - `openapi: "3.0.3"`，info 标题标注项目名与版本。
  - paths 只包含目标接口一个 path，method 用 `post/get/put/delete`；summary 取注释标题，description 写清楚语义（如"先删后插、传空列表=清空、仅哪些字段生效"）。
  - 若接口有登录态校验，在 parameters 里加 `Authorization` header（Bearer）说明。
3. 请求体（必须给出完整的 JSON 结构与示例）：
  - 若方法入参是聚合 Request（如 `AllPersonalInfoRequest`），按"接口实际使用字段"精简建模（如 unionId + xxxList）。
  - 在 `requestBody.content["application/json"].schema` 中列出完整字段结构：每个字段的类型、是否必填、中文 `description`、`example`（示例值用可读的真实值，不要留空串或占位符）。
  - 嵌套子对象/附件用 `components/schemas` 定义，并在属性/`items` 中用 `$ref` 引用。
  - 必须同时提供一份**完整、可直接发送的请求体 JSON 示例**（`example`），其字段与 schema 保持一致。
4. 响应体（可能为多层，必须逐层获取并展开）：
  - 外层固定为 `BaseResultEntity` 结构（`code/errorCode/success/message/result`）；**不能只写外层**，`result` 必须按接口实际返回类型逐层展开。
  - 逐层获取方法：从方法签名拿到真实返回类型（如 `SuccessResultEntity<List<CertificateQueryResult>>` → 取 `CertificateQueryResult` 列表），再逐个读取实体类的字段类型与中文注释；遇到自定义对象、`List<对象>`、`Map`、附件对象（如 `FileResult`/`Profile`）必须继续点进该类型，直到基本类型/字符串/日期等叶子字段。
  - 在 `components/schemas` 中为每一层自定义类型单独定义 schema 并用 `$ref` 引用（数组用 `items.$ref`），不要内联堆叠导致层级丢失。
  - 必须提供一份**与 schema 层级一致的完整响应体 JSON 示例**（`example`），嵌套层级要真实反映多层结构。
  - 示例：`BaseResultEntity` → `result: List<CertificateQueryResult>` → `CertificateQueryResult.fileResultList: List<Profile>` → `Profile` 各字段，逐层展开并填充 example。
5. 写入后确保 JSON 语法合法（可用 `Get-Content <文件路径> -Raw | ConvertFrom-Json` 校验）。

## 第五步：导入

```powershell
apifox import --project <projectId> --format openapi --file <临时json绝对路径> [--branch <分支名>]
```

- 默认不传 `--branch` 写入 main；AI 分支场景传 `--branch <AI分支名>`。
- 观察返回统计：期望 `apiCollection.item.createCount >= 1`，`errorCount = 0`。

## 第六步：验证

- 运行 `apifox endpoint list --project <id> [--branch <分支名>]`，用路径关键词过滤，确认接口已存在且 method/path 正确。
- 若创建了 AI 分支：提示用户在 Apifox 客户端确认后，通过 `apifox branch merge`/merge request 把分支合回来源分支（AI 分支修改不会自动写回；24h 无差异会自动归档）。

## 第七步：清理

- 删除临时 OpenAPI json 文件（`Remove-Item`），并确认删除成功（`Test-Path` 返回 False）。
- 不要改动任何 Java/业务代码，除非用户另行要求。

## 注意

- 全程不要在执行导入前修改代码仓库。
- 若导入涉及多个接口（如教育经历+工作经历两个"列表保存"接口），可合并到一个 OpenAPI 文件的多个 paths 中一次性导入。
- 任何涉及权限、目标项目/分支不确定的决策，先询问用户再执行。
