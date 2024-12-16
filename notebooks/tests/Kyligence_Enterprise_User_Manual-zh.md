目录

Introduction

Kyligence	Enterprise	概述

如何使用本手册

快速上手

安装与启动

AI	增强建模

样例数据集

申请许可证

全新功能

内表使用指南

内表功能概述

管理内表

内表数据导入

查询内表

安装部署

安装前置条件

网络端口要求

安装

在	Apache	Hadoop	环境安装

在	Cloudera	CDH	环境安装

在华为	FusionInsight	环境安装

在	Hortonworks	HDP	环境安装

在星环	TDH	环境安装

配置	RDBMS	元数据库

MySQL

安装	MySQL

使用	MySQL	作为元数据库

PostgreSQL

安装	PostgreSQL

使用	PostgreSQL	作为元数据库

元数据库建表语句

查询历史字段表

部署模式

集群部署

服务发现

读写分离部署

资源组部署

1.1

1.2

1.2.1

1.2.2

1.2.2.1

1.2.2.2

1.2.2.3

1.2.3

1.3

1.3.1

1.3.1.1

1.3.1.2

1.3.1.3

1.3.1.4

1.4

1.4.1

1.4.2

1.4.3

1.4.3.1

1.4.3.2

1.4.3.3

1.4.3.4

1.4.3.5

1.4.4

1.4.4.1

1.4.4.1.1

1.4.4.1.2

1.4.4.2

1.4.4.2.1

1.4.4.2.2

1.4.4.3

1.4.4.4

1.4.5

1.4.5.1

1.4.5.2

1.4.5.3

1.4.5.4

1

安全和用户认证

与	LDAP	集成

与	Kerberos	集成

项目级别配置	Kerberos

与第三方用户认证系统集成

与第三方用户认证系统集成样例

系统配置

基本配置参数

Spark	资源动态配置

Hadoop	队列配置

查询缓存配置

HTTPS	配置

Spark	RPC	通信加密

日志滚动配置

Gluten	内表参数配置

升级	KE4	至	KE5

升级至	Kyligence	Enterprise	最新版本

卸载

运维指南

运维概述

许可证容量

容量计费

项目运维

项目首页

工具栏

管理项目

项目设置

任务报警

访问控制

管理用户

管理用户组

数据访问控制

数据权限

项目级别访问权限

表列行级访问权限

系统运维

诊断

系统诊断、任务诊断与查询诊断

查询火焰图

构建火焰图

1.4.6

1.4.6.1

1.4.6.2

1.4.6.2.1

1.4.6.3

1.4.6.3.1

1.4.7

1.4.7.1

1.4.7.2

1.4.7.3

1.4.7.4

1.4.7.5

1.4.7.6

1.4.7.7

1.4.7.8

1.4.8

1.4.9

1.4.10

1.5

1.5.1

1.5.2

1.5.3

1.5.4

1.5.4.1

1.5.4.2

1.5.4.3

1.5.4.4

1.5.4.5

1.5.5

1.5.5.1

1.5.5.2

1.5.5.3

1.5.5.3.1

1.5.5.3.2

1.5.5.3.3

1.5.6

1.5.6.1

1.5.6.1.1

1.5.6.1.2

1.5.6.1.3

2

升级	Session	表工具

CLI	运维工具

环境依赖服务检测

诊断包工具

元数据备份与恢复

回滚工具

守护进程

垃圾清理

查询限流，保护查询稳定

监控

InfluxDB

配置时序数据库	InfluxDB

InfluxDB	维护

指标监控

服务监控

日志类型

审计日志

系统日志

获取技术支持

模型设计指南

数据源

Hive	数据源

Kafka	数据源

其他数据源

集成数据湖

数据抽样

模型设计

模型设计概述

智能建模（推荐）

智能推荐工作原理

基于	SQL	创建模型和索引

常量子查询推荐优化

智能优化索引

索引优化策略

查看智能优化推荐

设置优化建议的生成规则

手动建模

模型概念与操作

模型设计进阶

度量设计

1.5.6.2

1.5.6.3

1.5.6.3.1

1.5.6.3.2

1.5.6.3.3

1.5.6.3.4

1.5.6.4

1.5.6.5

1.5.6.6

1.5.7

1.5.7.1

1.5.7.1.1

1.5.7.1.2

1.5.7.2

1.5.7.3

1.5.8

1.5.8.1

1.5.8.2

1.5.9

1.6

1.6.1

1.6.1.1

1.6.1.2

1.6.1.3

1.6.1.4

1.6.1.5

1.6.2

1.6.2.1

1.6.2.2

1.6.2.2.1

1.6.2.2.2

1.6.2.2.3

1.6.2.2.4

1.6.2.2.4.1

1.6.2.2.4.2

1.6.2.2.4.3

1.6.2.3

1.6.2.4

1.6.2.5

1.6.2.5.1

3

TopN	(Beta)

精确去重计数

近似去重计数

近似	Percentile

相关函数	CORR	(Beta)

COLLECT_SET

Sum	Expression

Count	Distinct	Case	When	Expression

半累加度量

可计算列

缓慢变化维度

聚合索引

明细索引

模型高级设置

模型元数据导入导出

多级分区

精确击中索引的查询优化

整数类型跳过字典编码优化

预计算关联关系

逻辑视图

加载数据

全量加载

增量加载

构建索引

数据完整性

Segment	操作与设置

Segment	合并

任务监控

概念和基本设置

任务操作

任务诊断

常见任务错误原因和解决方案

SQL	查询

数据类型

查询分析

在用户界面执行	SQL	查询

查询样例

SQL	规范参考

异步查询

通过模型视图简化查询

1.6.2.5.1.2

1.6.2.5.1.1

1.6.2.5.1.3

1.6.2.5.1.4

1.6.2.5.1.5

1.6.2.5.1.6

1.6.2.5.1.7

1.6.2.5.1.8

1.6.2.5.1.9

1.6.2.5.2

1.6.2.5.3

1.6.2.5.4

1.6.2.5.5

1.6.2.5.6

1.6.2.5.6.1

1.6.2.5.6.2

1.6.2.5.6.3

1.6.2.5.6.4

1.6.2.5.7

1.6.2.5.8

1.6.3

1.6.3.1

1.6.3.2

1.6.3.3

1.6.3.4

1.6.3.5

1.6.3.5.1

1.6.4

1.6.4.1

1.6.4.2

1.6.4.3

1.6.4.4

1.6.5

1.6.5.1

1.6.5.2

1.6.5.2.1

1.6.5.2.2

1.6.5.2.3

1.6.5.2.4

1.6.5.2.5

4

函数及运算符

运算符

比较运算符

逻辑运算符

算术运算符

字符串运算符

函数

算术函数

字符串函数

日期函数

条件函数

类型转换函数

窗口函数

分组函数

交集函数

聚合函数

Bitmap	函数

其他函数

为查询指定模型优先级

查询历史

查询优化

使用	Left	Join	模型回答等价语义的	Inner	Join	查询

查询	Segment	剪枝

查询下压

下压至原生	SparkSQL

实时功能

软硬件环境要求

使用实时功能

自定义解析器

已知限制

快照管理

快照管理与操作

内表使用指南

内表功能概述

管理内表

内表数据导入

查询内表

数据分析师指南

SQL	查询

数据类型

1.6.5.2.6

1.6.5.2.6.1

1.6.5.2.6.1.1

1.6.5.2.6.1.2

1.6.5.2.6.1.3

1.6.5.2.6.1.4

1.6.5.2.6.2

1.6.5.2.6.2.1

1.6.5.2.6.2.2

1.6.5.2.6.2.3

1.6.5.2.6.2.4

1.6.5.2.6.2.5

1.6.5.2.6.2.6

1.6.5.2.6.2.7

1.6.5.2.6.2.8

1.6.5.2.6.2.9

1.6.5.2.6.2.10

1.6.5.2.6.2.11

1.6.5.2.7

1.6.5.3

1.6.5.4

1.6.5.4.1

1.6.5.4.2

1.6.5.5

1.6.5.5.1

1.6.6

1.6.6.1

1.6.6.2

1.6.6.3

1.6.6.4

1.6.7

1.6.7.1

1.7

1.7.1

1.7.2

1.7.3

1.7.4

1.8

1.8.1

1.8.1.1

5

查询分析

在用户界面执行	SQL	查询

查询样例

SQL	规范参考

异步查询

通过模型视图简化查询

函数及运算符

运算符

函数

比较运算符

逻辑运算符

算术运算符

字符串运算符

算数函数

字符串函数

日期函数

条件函数

类型转换函数

窗口函数

分组函数

交集函数

聚合函数

Bitmap	函数

其他函数

为查询指定模型优先级

查询历史

查询优化

使用	Left	Join	模型回答等价语义的	Inner	Join	查询

查询	Segment	剪枝

查询下压

下压至原生	SparkSQL

与	BI	工具集成

驱动程序

Kyligence	JDBC	驱动

Kyligence	ODBC	驱动

Windows	版本

Linux	版本

Mac	版本

与	BI	工具连接

与	Tableau	集成

1.8.1.2.1

1.8.1.2

1.8.1.2.2

1.8.1.2.3

1.8.1.2.4

1.8.1.2.5

1.8.1.2.6

1.8.1.2.6.1

1.8.1.2.6.1.1

1.8.1.2.6.1.2

1.8.1.2.6.1.3

1.8.1.2.6.1.4

1.8.1.2.6.2

1.8.1.2.6.2.1

1.8.1.2.6.2.2

1.8.1.2.6.2.3

1.8.1.2.6.2.4

1.8.1.2.6.2.5

1.8.1.2.6.2.6

1.8.1.2.6.2.7

1.8.1.2.6.2.8

1.8.1.2.6.2.9

1.8.1.2.6.2.10

1.8.1.2.6.2.11

1.8.1.2.6.3

1.8.1.3

1.8.1.4

1.8.1.4.1

1.8.1.4.2

1.8.1.5

1.8.1.5.1

1.8.2

1.8.2.1

1.8.2.1.1

1.8.2.1.2

1.8.2.1.2.1

1.8.2.1.2.2

1.8.2.1.2.3

1.8.2.2

1.8.2.2.1

6

与	Tableau	Desktop	集成

与	Tableau	Server	集成

启用	Tableau	Server	用户委任

与	Power	BI	集成

与	Power	BI	Desktop	集成

与	Power	BI	Service	集成

与	MicroStrategy	集成

与	MicroStrategy	Secure	Enterprise	集成

与	MicroStrategy	Workstation/Desktop	集成

与	IBM	Cognos	集成

与	Oracle	Business	Intelligence/OBIEE	集成

与	OBIEE	11g	集成

与	OBIEE	12c	集成

OBIEE	设置行级安全性

与	Oracle	BI	Publisher	集成

与	SAP	BusinessObjects/BO	集成

与	BO	Client	集成

与	BO	Server	集成

与	思迈特	SmartBI	Insight	集成

与	帆软	FineBI	集成

与	帆软	FineReport	集成

与	永洪	Yonghong	BI	集成

与	Excel	集成

与	Python	集成

开发者指南

REST	API	v4

访问与安全认证	API

项目设置	API

数据源管理	API

模型	API

模型管理	API

模型构建	API

模型导入导出	API

多级分区模型	API

逻辑视图	API

Segment	管理	API

快照管理	API

内表管理	API

查询	API

异步查询	API

1.8.2.2.1.2

1.8.2.2.1.1

1.8.2.2.1.3

1.8.2.2.2

1.8.2.2.2.1

1.8.2.2.2.2

1.8.2.2.3

1.8.2.2.3.1

1.8.2.2.3.2

1.8.2.2.4

1.8.2.2.5

1.8.2.2.5.1

1.8.2.2.5.2

1.8.2.2.5.3

1.8.2.2.5.4

1.8.2.2.6

1.8.2.2.6.1

1.8.2.2.6.2

1.8.2.2.7

1.8.2.2.8

1.8.2.2.9

1.8.2.2.10

1.8.2.3

1.8.2.4

1.9

1.9.1

1.9.1.1

1.9.1.2

1.9.1.3

1.9.1.4

1.9.1.4.1

1.9.1.4.2

1.9.1.4.3

1.9.1.4.4

1.9.1.4.5

1.9.1.5

1.9.1.6

1.9.1.7

1.9.1.8

1.9.1.9

7

任务	API

许可证容量	API

访问控制权限	API

用户管理	API

用户组管理	API

项目级访问控制权限	API

表行列级权限管理	API

实时功能	API

自定义解析器	Jar	包管理	API

通过	API	实现指标自动发布

使用回调	API	查看构建任务状态

错误码

REST	API	v2

访问与安全认证	API

模型	API

查看模型信息	API

构建模型	API

Segment	管理	API

项目	API

数据源	API

任务	API

查询	API

异步查询	API

访问控制权限	API

用户管理	API

用户组管理	API

项目级访问控制权限	API

数据源扩展	SDK

如何基于数据源扩展	SDK，开发新的数据源连接器

Gbase	数据源连接器

SQL	Transformer	SDK	(Beta)

实时自定义解析器	SDK

术语表：基本概念

常见问题

发行说明

Kyligence	Enterprise	5.2	发行说明

Kyligence	Enterprise	历史版本发行说明

Kyligence	Enterprise	4.6	发行说明

Kyligence	Enterprise	4.5	发行说明

Kyligence	Enterprise	4.3	发行说明

1.9.1.10

1.9.1.11

1.9.1.12

1.9.1.12.1

1.9.1.12.2

1.9.1.12.3

1.9.1.12.4

1.9.1.13

1.9.1.13.1

1.9.1.14

1.9.1.15

1.9.1.16

1.9.2

1.9.2.1

1.9.2.2

1.9.2.2.1

1.9.2.2.2

1.9.2.2.3

1.9.2.3

1.9.2.4

1.9.2.5

1.9.2.6

1.9.2.7

1.9.2.8

1.9.2.8.1

1.9.2.8.2

1.9.2.8.3

1.9.3

1.9.3.1

1.9.3.2

1.9.4

1.9.5

1.10

1.11

1.12

1.12.1

1.12.2

1.12.2.1

1.12.2.2

1.12.2.3

8

Kyligence	Enterprise	4.2	发行说明

Kyligence	Enterprise	4.1	发行说明

Kyligence	Enterprise	4.0	发行说明

Kyligence	Enterprise	3.4	发行说明

Kyligence	Enterprise	3.3	发行说明

Kyligence	Enterprise	3.2	发行说明

Kyligence	Enterprise	3.1	发行说明

Kyligence	Enterprise	3.0	发行说明

联系我们

1.12.2.5

1.12.2.4

1.12.2.6

1.12.2.7

1.12.2.8

1.12.2.9

1.12.2.10

1.12.2.11

1.13

9

Introduction

Kyligence	Enterprise	简介

Kyligence	Enterprise	是	Kyligence	公司开发的企业级智能多维数据库平台，提供在	PB	级数据集上亚秒级标准	SQL	查询
响应，同时支持互联网级的高并发访问，助力业务用户快速发现海量数据中的业务价值，驱动商业决策。其	AI	增强引
擎帮助企业从核心业务查询中识别关键特征和模式，并自动构建和管理分布式数据集市，为业务提供更可靠的指标体

系，进一步缩短数据湖开发流程，释放业务自助分析潜力。

Kyligence	Enterprise	为业务分析师、数据科学家和	IT	工程师提供了统一的分析平台，支持无需编程的智能快速建模，与
主流	BI	工具无缝集成。Kyligence	Enterprise	基于开源	Apache	Kylin	核心，在性能、安全性、可靠性等方面进行了全面
的创新和增强，帮助企业以更高效率实现新一代数据仓库解决方案。

相较于其它技术，Kyligence	Enterprise	具有以下特点：

超高性能、亚秒级查询响应

融合的大数据仓库架构

AI	增强的智能建模和索引优化
标准	SQL	接口，无缝集成	BI
增强的企业级特性

更多信息，请访问	Kyligence	网站:	https://kyligence.io/

关于	Kyligence

Kyligence	由	Apache	Kylin	创始团队于	2016	年创办，致力于打造下一代企业级智能多维数据库，为企业简化数据湖上的
多维数据分析（OLAP）。Apache	Kylin	是开源	OLAP	的领导者，是第一个由中国团队贡献到	Apache	软件基金会
（ASF）的顶级开源项目，已被全球超过	1500	多家公司作为核心大数据分析平台使用。Kyligence	通过	AI	增强引擎从核
心业务查询中识别关键特征和模式，并自动构建和管理分布式数据集市，为业务提供更可靠的指标体系，进一步缩短数

据湖开发流程，释放业务自助分析潜力。Kyligence	的统一	SQL	接口及服务，能够在云端对象存储（如	AWS	S3、Azure
ADLS	等）、多维立方体、高速索引及底层数据源上进行智能路由，为上层分析应用提供成本最优的高性能查询能力，
以支撑商务智能（BI）分析、灵活查询和互联网级数据服务等多类应用场景。

Kyligence	已服务中国、美国、欧洲及亚太的多个银行、证券、保险、制造、零售等行业客户，包括建设银行、浦发银
行、招商银行、平安银行、宁波银行、太平洋保险、中国银联、上汽、YUMC、Costa、UBS、MetLife	等全球知名企
业，并和微软、亚马逊、华为、Tableau	等技术领导者达成全球合作伙伴关系。Kyligence	获得了来自红点、思科、宽带
资本、顺为资本、斯道资本（富达国际自有投资机构）、Coatue	Management、浦银国际、中金资本旗下基金、歌斐资
产、国方资本、ASG、宏兆基金、浦信资本等投资机构的多轮投资。目前公司已经在上海、北京、深圳、厦门、武汉及
美国的硅谷、纽约、西雅图等开设分公司或办事机构。

关于	Apache	Kylin

Apache	Kylin	是全球领先的开源	OLAP	引擎，为海量数据提供亚秒级查询响应能力。2014	年于	eBay	开源项目中诞生，
2015	年毕业成为	Apache	软件基金会的顶级项目，并迅速被全球数千家公司与组织应用于数据分析业务，同时也在	2015
年、2016	年赢得	InfoWorld	Bossie	Awards	年度最佳大数据开源工具。

有关	Apache	Kylin	与	Kyligence	企业版产品比较，请访问这里。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

10

Kyligence	Enterprise	概述

Kyligence	Enterprise	简介

Kyligence	Enterprise	是企业级智能多维数据库平台，帮助企业简化数据湖多维分析。通过学习用户分析行为及数据特
征，自动完成数据模型的准备，极大地加速了对海量数据洞察。Kyligence	Enterprise	基于前沿的增强型大数据计算架
构，实现了	PB	级大规模数据的高并发和亚秒级查询响应，支撑了金融、电信、制造、零售等行业的关键业务分析。

Kyligence	Enterprise	为业务分析师、数据科学家和	IT	工程师提供了统一的分析平台，支持无需编程的智能快速建模，与
主流	BI	工具无缝集成。Kyligence	Enterprise	基于开源	Apache	Kylin	核心，在性能、安全性、稳定性上进行了全面的创
新和增强，帮助企业以更高效率实现新一代数据仓库解决方案。

相较于其它技术，Kyligence	Enterprise	具有以下特点：

高性能高并发，亚秒级查询响应

融合的大数据仓库架构

智能	SQL	查询加速

无缝集成	BI

增强的企业级特性

更多信息，请访问Kyligence网站:	https://kyligence.io/

关于Kyligence

Kyligence	由	Apache	Kylin	创始团队于	2016	年创办，致力于打造下一代企业级智能多维数据库，为企业简化数据湖上的
多维数据分析（OLAP）。Apache	Kylin	是开源	OLAP	的领导者，是第一个由中国团队贡献到	Apache	软件基金会
（ASF）的顶级开源项目，已被全球超过	1500	多家公司作为核心大数据分析平台使用。Kyligence	通过	AI	增强引擎从核
心业务查询中识别关键特征和模式，并自动构建和管理分布式数据集市，为业务提供更可靠的指标体系，进一步缩短数

据湖开发流程，释放业务自助分析潜力。Kyligence	的统一	SQL	接口及服务，能够在云端对象存储（如	AWS	S3、Azure
ADLS	等）、多维立方体、高速索引及底层数据源上进行智能路由，为上层分析应用提供成本最优的高性能查询能力，
以支撑商务智能（BI）分析、灵活查询和互联网级数据服务等多类应用场景。

Kyligence	已服务中国、美国、欧洲及亚太的多个银行、证券、保险、制造、零售等行业客户，包括建设银行、浦发银
行、招商银行、平安银行、宁波银行、太平洋保险、中国银联、上汽、YUMC、Costa、UBS、MetLife	等全球知名企
业，并和微软、亚马逊、华为、Tableau	等技术领导者达成全球合作伙伴关系。Kyligence	获得了来自红点、思科、宽带
资本、顺为资本、斯道资本（富达国际自有投资机构）、Coatue	Management、浦银国际、中金资本旗下基金、歌斐资
产、国方资本、ASG、宏兆基金、浦信资本等投资机构的多轮投资。目前公司已经在上海、北京、深圳、厦门、武汉及
美国的硅谷、纽约、西雅图等开设分公司或办事机构。

关于Apache	Kylin

Apache	Kylin	是全球领先的开源	OLAP	(联机分析处理)	引擎，为海量数据提供亚秒级查询响应能力。2014	年于	eBay	开
源项目中诞生，2015	年毕业于	Apache	顶级项目并迅速被全球数千家公司与组织应用于数据分析业务，同时也在2015
年、2016	年赢得	InfoWorld	Bossie	Awards	年度最佳大数据开源工具。​

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

11

如何使用本手册

如何阅读本手册

本手册根据产品使用旅程分为不同章节，向您介绍	Kyligence	Enterprise	的部署、运维、数据建模及查询，您可以根据自
身需求进行阅读，以下为各章节内容概述：

Kyligence	Enterprise	概述

本章将介绍	Kyligence	Enterprise	并提供快速入门指引。

全新功能

本章将介绍	Kyligence	Enterprise	最新推出的各项功能及其应用场景，方便您随时掌握	Kyligence	Enterprise	的最新动
态。

安装部署

本章将介绍	Kyligence	Enterprise	在不同平台中的部署方法、安全与权限设置等信息。

运维指南

本章将介绍	Kyligence	Enterprise	中的项目管理、日志查询、访问控制台、系统管理、提交技术支持需求等常见运维
操作。

模型设计指南

本章将介绍如何对接数据源，执行模型设计、索引设计和性能调优。

数据分析师指南

本章将介绍如何分析数据、执行	SQL	查询和对接第三方	BI	工具。

开发者指南

Kyligence	Enterprise	提供了可用区管理、项目管理、权限管理等丰富的	REST	API。本章将介绍	Kyligence	Enterprise
中	API	认证方式及各类	API	使用示例，帮助您轻松地将	Kyligence	Enterprise	集成至第三方系统。

术语表

本章将介绍	Kyligence	Enterprise	中常用的概念。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

12

快速上手

快速启动和使用指导

在本章中，我们首先为您介绍如何快速安装和启动	Kyligence	Enterprise，接着基本概念能够帮助您更快得熟悉本产品，
最后您可以根据	AI	增强模式指导完成产品的初步使用。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

13

安装与启动

安装与启动

在本节中，我们将引导您快速安装和启动	Kyligence	Enterprise	5。

在安装前，请确认您已阅读安装前置条件。

下载和安装

快速配置

启动

安装验证

停止

FAQ

下载和安装

1.	 获取	Kyligence	Enterprise	软件包。您可以访问发行说明，选择适合您的版本，并在	Kyligence	Download	下载所需的

二进制包。

2.	 决定安装路径和将要运行	Kyligence	Enterprise	的	Linux	账户。下文所有示例都做如下假设：

假设安装路径为	 	/usr/local/
假设运行	Kyligence	Enterprise	的	Linux	账户为	 	KyAdmin	，下文简称	“Linux	账户”。
在执行下文所有命令时，请留意将上述假设替换为真实的安装路径和	Linux	账户。

3.	 将	Kyligence	Enterprise	软件包拷贝至您需要安装的服务器或虚拟机，并解压至安装路径下。

cd	/usr/local

tar	-zxvf	Kyligence-Enterprise-[Version].tar.gz

下文称该解压目录为	$KYLIN_HOME	或根目录。

4.	 准备	RDBMS	元数据库。	如果您的运行环境中已经安装	PostgreSQL	或者	MySQL，您可以选择其中一个作为元数据

库。

注意：

对于生产环境，我们推荐使用独占的元数据库。您可以使用	Kyligence	Enterprise	自带的	PostgreSQL	作为独占
元数据库。

元数据库库名必须以英文字母开头

请您参考以下章节完成相应配置：

使用	PostgreSQL	作为元数据库
使用	MySQL	作为元数据库

5.	 （可选）安装	InfluxDB。

Kyligence	Enterprise	使用	InfluxDB	保存系统运行时的各项监控信息。如果您不需要查看相关信息，可以跳过此步
骤。强烈建议在生产环境中完成此步骤，并使用相关的监控功能。

cd	$KYLIN_HOME/influxdb

#	install	influxdb

rpm	-ivh	influxdb-1.6.4.x86_64.rpm

更多安装和配置的信息请点击	配置时序数据库	InfluxDB。

6.	 在	HDFS	上创建	Kyligence	Enterprise	的工作目录，并授予	Linux	账户读写该工作目录的权限。

14

安装与启动

默认的工作目录为	 	/kylin	，该目录用于存储模型构建后的数据文件。同时创建目录	 	/kylin/spark-history	，该目
录用于存放	Spark	的运行日志。运行下述命令：

hadoop	fs	-mkdir	-p	/kylin

hadoop	fs	-chown	root	/kylin

hadoop	fs	-mkdir	-p	/kylin/spark-history

hadoop	fs	-chown	root	/kylin/spark-history

注意：如果无法创建目录	 	/kylin/spark-history	，请您在配置文件	 	/conf/kylin.properties		中调整参数
	kylin.engine.spark-conf.spark.eventLog.dir		和	 	kylin.engine.spark-conf.spark.history.fs.logDirectory		为可用的
文件夹。

快速配置

在安装包根目录下的	 	conf		目录，您可以按照如下方法配置文件	 	kylin.properties		中的参数。

1.	 请根据相应的	PostgreSQL	的配置信息，设置如下	 	metadata		参数，注意替换相应的

	{metadata_name}	， 	{host}	， 	{port}	， 	{user}	， 	{password}		值。其中， 	metadata_name		允许的最大长度为28。

kylin.metadata.url={metadata_name}@jdbc,driverClassName=org.postgresql.Driver,url=jdbc:postgresql://{host}:

{port}/kylin,username={user},password={password}

如果您需要了解更多	PostgreSQL	作为元数据库的配置方法，请您查看相应章节使用	PostgreSQL	作为元数据库	。如
果您需要使用	MySQL	作为元数据库的配置方法，请您查看使用	MySQL	作为元数据库章节。

注意：请用字母、数字和下划线命名	 	{metadata_name}	，名称不能以数字开头，比如	 	1a		是非法的， 	a1		是
合法的。

2.	 执行任务时，Kyligence	Enterprise	将会向	Yarn	服务提交构建任务，您可以设置替换以下参数中的	 	{queue}		为您实

际使用的队列，要求构建任务提交到指定队列中。

kylin.engine.spark-conf.spark.yarn.queue={queue}

3.	 配置	ZooKeeper	服务。

Kyligence	Enterprise	使用	ZooKeeper	实现服务发现，确保在集群部署时中，当一个实例启动、停止或意外中断通讯
时，集群中的其他实例能够自动发现并更新状态。具体介绍可参考服务发现章节。

请添加	ZooKeeper	的连接项	 	kylin.env.zookeeper-connect-string={host}:{port}	，并如下修改集群的地址和端口。

kylin.env.zookeeper-connect-string=10.1.2.1:2181,10.1.2.2:2181,10.1.2.3:2181

4.	 (可选)配置	Spark	Client	节点信息	由于当前	Spark	以	yarn-client	模式启动，如果	Kyligence	Enterprise	部署的客户端	IP

信息没有配置在	Hadoop	集群节点的	hosts	文件中，请在	 	kylin.properties		中添加如下配置项：

	kylin.storage.columnar.spark-conf.spark.driver.host={hostIp}		 	kylin.engine.spark-conf.spark.driver.host=
{hostIp}

您可参考如下例子修改	{hostIp}

kylin.storage.columnar.spark-conf.spark.driver.host=10.1.3.71

kylin.engine.spark-conf.spark.driver.host=10.1.3.71

启动

1.	 检查	 	curl		版本。

15

安装与启动

由于安装过程中	 	check-env.sh		需要依赖	GSS-Negotiate	的支持，所以建议您先检查您的	curl	的相关组件，您可以
在环境中使用如下命令：

curl	--version

若界面中显示	GSS-Negotiate	则符合要求，如果没有，您可以重装	curl	或者增加	GSS-Negotiate	的支持。

检查	GSS-Negotiate	依赖

2.	 使用启动脚本启动服务。	运行下述命令以启动	Kyligence	Enterprise。首次启动时，系统会运行一系列脚本校验系统

环境、用户权限等是否满足条件，详情可参考环境检测章节。

$KYLIN_HOME/bin/kylin.sh	start

注意：如果想观察启动的详细进度：

tail	-f	$KYLIN_HOME/logs/kylin.log

如您非首次启动，可运行下述命令快速启动	Kyligence	Enterprise。	快速启动时，系统会跳过一些检查步骤，详情可
参考环境检测章节。

$KYLIN_HOME/bin/kylin.sh	-DskipCheck	start

启动成功后，您将在控制台中看到提示信息。此时可以运行下述命令检查	Kyligence	Enterprise	进程：

			ps	-ef	|	grep	kylin

1.	 获取登录信息。

在启动脚本运行结束后，会将默认用户	 	ADMIN		的随机密码显示在控制台，您需要将此密码保存，如果此密码不慎
丢失，请参考	ADMIN	用户重置密码。

安装验证

当	Kyligence	Enterprise	顺利启动后，您可以打开	Web	浏览器，访问	 	http://{host}:7070/kylin/	。请将其中的	 	host		替
换为具体的机器名、IP	地址或域名，默认端口为	 	7070	。

默认用户名为	 	ADMIN		，默认生成的随机密码将在初次启动	Kyligence	Enterprise	时显示在控制台。初次登陆后，请遵照
密码规则重置管理员密码。

密码长度至少	8	位
密码需要包含至少一个数字、字母、及特殊字符（~!@#$%^&*(){}|:"<>?[];',./`）

16

安装与启动

当您成功登录后，请先上传许可证，许可证申请和上传详情请参考申请许可证章节。上传许可证后，您可以通过样例数

据来验证	Kyligence	Enterprise	的功能。

Kyligence	Enterprise	提供了开源的、专门针对星型模型	OLAP	场景的	SSB（Star	Schema	Benchmark）数据集作为测试数
据集。您可以运行脚本将	SSB	数据集导入	Hive	以验证是否正确安装，SSB	数据集来自于	CSV	文件。

导入样例数据集

运行下述命令向	Hive	中导入	SSB	数据集：

$KYLIN_HOME/bin/sample.sh

该脚本将会在	Hive	中创建	1	个数据库	 	SSB	，	在数据库	 	SSB		中创建	6	张表，并将数据导入其中。

运行成功后，您将在控制台中看到如下提示信息：

Sample	hive	tables	are	created	successfully

我们将在用户手册的多个章节使用	SSB	数据集来讲解	Kyligence	Enterprise	的使用方法。SSB	数据集模拟了在线商城的
交易数据，你可以在样例数据集查看详细介绍。以下为	SSB	数据集的简介：

名称

描述

简介

CUSTOMER

顾客信息表

包括顾客姓名、住址、联系方式等基本信息

DATES

订单日期表

包括对一个订单日期的具体日期、星期、月份、年份等多种日期形式

LINEORDER

订单信息表

包括订单日期、订单数量、订单收益、供应商	ID、商品	ID、顾客	ID
等基本信息

PART

商品信息表

包括商品名称、类别、商标等基本信息

P_LINEORDER

基于订单信息表的
视图

包括订单信息表的所有内容和视图中新增的内容

SUPPLIER

供应商信息表

包括供应商姓名、地址、联系方式等基本信息

验证产品功能

您可以根据	AI	增强模式指导章节完成项目和模型创建。完成后，您已经验证了数据源的添加、模型的创建和索引的构
建等产品的基本功能。

进入导航栏	数据资产	->	模型	界面，您将看到如下图所示的一个样例模型。存储大小	>	0.00	KB	表示已经为该模型加载
数据。

模型列表

17

安装与启动

点击左侧导航栏中的监控，您可以在批数据任务和流数据任务下看到所有任务都成功执行完毕。

任务监控

查询分析验证

当构建索引的任务成功后，进入查询页面，您将在页面左侧看到之前导入的	SSB	数据集及其中的源表。在右侧的查询
编辑器中输入	SQL	语句，即可在样例项目中进行查询分析。例如输入下述	SQL	语句，该	SQL	语句能够查询指定订单时
间范围内不同商品的收入，结果按照收入降序排列。

SELECT	LO_PARTKEY,	SUM(LO_REVENUE)	AS	TOTAL_REVENUE

FROM	SSB.P_LINEORDER

WHERE	LO_ORDERDATE	between	'1993-06-01'	AND	'1994-06-01'

group	by	LO_PARTKEY

order	by	SUM(LO_REVENUE)	DESC

您将在页面下方看到	Kyligence	Enterprise	为您呈现出的查询结果，如下图所示该查询击中了之前创建的样例模型。

查询分析

您也可以使用同样的	SQL	语句在	Hive	上查询，以对比验证查询的结果和响应的速度。

至此	Kyligence	Enterprise	的主要功能验证完毕。

18

安装与启动

停止

运行下述命令以停止运行	Kyligence	Enterprise：

$KYLIN_HOME/bin/kylin.sh	stop

您可以运行下述命令查看	Kyligence	Enterprise	进程是否已停止：

ps	-ef	|	grep	kylin

FAQ

Q：如何修改默认端口？

您可以编辑根目录下的配置文件	 	/conf/kylin.properties	，修改参数	 	server.port		的值至可用的端口。

server.port=7070

Q：Kyligence	Enterprise	支持配置	Kerberos	吗？

支持。如果您的集群启用	Kerberos	安全机制，Kyligence	Enterprise	自带的	Spark	需要正确的配置才能安全地访问您的集
群资源。具体配置方法请参看与	Kerberos	集成章节。

Q：查询下压引擎默认是开启状态吗？

是的，如果您想关闭查询下压引擎，请参考下压查询至SparkSQL。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

19

AI	增强建模

AI	增强模式指导

Kyligence	Enterprise	4.x	起提供由用户主导建模的	AI	增强模式。本节我们为您介绍该模式中产品使用的基本方法。

准备工作

1.	 Kyligence	Enterprise	4.x	起提供项目模式：	AI	增强模式。

AI	增强模式：您可以主导模型设计的环节，手动创建满足业务分析需求的模型。同时，您可以手动设计索
引，并让系统在此基础上根据查询习惯和数据的特征，辅助推荐新索引，实现手动、自动一体化建模的工作。

2.	 我们将使用	SSB	(Star	Schema	Benchmark)	样例数据介绍	AI	增强模式的项目，您可以在导入	Hive	数据源章节了解导

入	SSB	样例数据的具体方法。

添加项目

项目是	Kyligence	Enterprise	的一级管理单位。在一个项目中，您可以设计多个模型并进行查询分析。

请您点击产品左上方项目列表右侧的	+	按钮来添加一个项目，并填写项目名称和项目描述。其中项目名称为必需填写
项，项目描述为选择填写项。建议您填写项目描述，这有助于项目的日后维护。

至此，您已完成一个	AI	增强模式的项目的创建，界面停留在	数据资产	->	数据源	界面，为下一步添加数据源做准备。

添加数据源

项目创建完毕，您需要为项目添加数据源表。之后您在创建模型或查询分析的阶段都将用到此处添加的数据源表。

添加数据源的同时会同步源表的元数据。表的元数据是指描述表特征的数据，如表名、列名、列类型等。

1.	 加载表的元数据

请您在	数据资产	->	数据源	界面，点击左上方	添加数据源	按钮，为您的项目添加数据源表。

选择数据源类型：请选择	Hive	数据源。

选择目标数据源表：展开数据库列表，并选择目标数据源表。

更多与数据源相关的操作请您查看数据源章节。

2.	 表抽样

在同步表的元数据过程中	Kyligence	Enterprise	默认开启源表数据抽样，您可以在	监控	->	任务	界面查看自动触发的
表级数据抽样	任务。任务执行完毕后，您就可以在	数据资产	->	数据源	界面查看源表的抽样数据了。您可以在数据
抽样章节了解更多。

通常来说，表抽样将回答类似如下问题，了解这些问题将有助于之后的模型设计。

表里有多少行？

每一列的基数是多大？即不重复的数据数量。

每一列的列值都有哪些特性？

3.	 数据源界面

如下图所示，我们添加了	Hive	中样例数据集	SSB	中的所有表。左侧为数据源区域，右侧为指定源表的信息。

您可以在右侧查看源表信息，其中所有列为源表字段的特征信息，抽样数据展现了源表中每列数据的形态。

20

AI	增强建模

数据源

创建模型

模型设计是	Kyligence	Enterprise	的核心功能之一，良好的模型设计可以帮助实现更优质的数据分析业务。

1.	 模型设计的原则

模型是语义层的概念。良好的模型能够帮助用户可视化地展现出源表之间的业务关系。

在	Kyligence	Enterprise	中，您可以在一张面板中查看数据源表、完成模型设计、添加维度和度量，便于设计出符合
业务逻辑的模型。模型设计中的几个基本原则：

事实表：一般为具有可统计量化的信息的表。如订单表适合作为事实表，其中有订购数量、订单金额等可以被

统计和量化的列。

维度表：一般为表示分析的业务角度的表。如商品信息表适合作为维度表，其中有商品类别、商品商标等可以

作为分析的业务角度的列。时间表通常作为维度表使用，便于按日	/	周	/	月	/	季	/	年统计业务数据。
维度：一般为可分析的业务角度，如订单日期表示日期维度、商品	ID	表示商品维度。
度量：一般为可统计量化的数值信息，如销售总额、销售总量等。通常为可量化的列与函数一起配合使用，如

SUM、COUNT、TOP_N	等。

2.	 模型设计的方法

请您在数据资产	->	模型	界面创建模型并进入模型编辑界面，可视化的完成多维模型的创建。模型设计的具体方法
将在基本模型设计章节中详细介绍，这里为您简要介绍以下三个步骤：

设计模型：根据业务逻辑选择源表并设置表之间的关联，同时设置事实表和维度表。

添加维度：添加能够满足业务分析的维度。

添加度量：添加能够满足业务分析的度量。您可以在度量章节中查看详细方法。

如下图所示，我们使用	SSB	数据集中的源表构建了模型。

21

AI	增强建模

模型设计

设计索引

模型在语义层上展现了数据源表间的业务逻辑，之后您需要为模型创建索引，索引根据您关注的业务分析模式而定。良

好的索引设计可以提升系统效率、节约存储空间。保存模型设计时往往会提醒您添加索引。

1.	 设计索引的原则

模型设计中添加的维度不一定都能够应用于实际的业务分析，此时预计算所有的维度组合将会带来较大的工作量，

一般会导致构建索引时间较长、数据存储空间较大、甚至系统超负荷运行出错。我们可以通过添加聚合索引、明细

索引改善此类状况。

聚合索引：根据关注的维度组定制构建满足于特定业务分析的索引。如在线商城分析师需要分析不同城市男性

顾客与女性顾客的购买力，则索引中的维度组合为	 	[城市、顾客性别]	。此时其他维度不需要进入索引，如不需
要分析商品类别，则之后也无需构建与商品类别相关的数据。您可以查看聚合索引章节了解更多。

明细索引：明细索引能够支持对明细数据高效的查询。如在线商城分析师需要查看订单明细数据，则在明细索

引中添加	 	[订单号、订单日期、商品	ID、顾客	ID、订单数量、订单金额]	，构建索引并加载数据后，即可高效查看明细数
据。您可以查看明细索引章节了解更多。

2.	 设计索引的方法

编辑聚合索引：点击数据资产	->	模型，点击具体模型进入具体模型页，点击索引，在索引总览页签，点击+索
引	->	聚合组。下图所示为一个聚合组。聚合组中用如下四个概念控制维度的组合数：

包含的维度：从模型中的维度列表中选择需要出现在索引中的维度。

必须维度：必须分析的业务角度对应的维度，如必须按顾客统计信息。

层级维度：具有层级关系的维度，如国家、省份和城市。

联合维度：必须联合在一起出现的维度，如供应商与订单日期必须同时出现。

22

AI	增强建模

编辑聚合索引

添加明细索引：在导航栏数据资产	->	模型	界面，点击具体模型进入具体模型页，点击索引，在索引总览页
签，点击+索引	->	明细索引。您可以选择明细索引中需要的列，设置排序和	ShardBy	列并构建索引。

加载数据

Kyligence	Enterprise	应用预计算技术实现大数据时代查询的亚秒级响应。在创建模型并编辑索引后，您需要为模型加载
数据，加载数据的同时也会根据模型定义构建索引。没有经过数据加载（即没有数据）的模型不能服务于任何查询。您

可以查看加载数据章节了解更多数据加载的具体方法。

1.	 加载数据的原则

设置时间分区列：模型中的事实表中的数据一般会随着时间增加，如在订单表中会随着时间增加新的订单。此

时一般选取订单日期作为时间分区列。设置时间分区列发生在保存模型设计之后。

全量加载：当模型不具有时间分区列，则每一次都会全量加载数据。如需要加载订单表中最新的一周的数据，

由于模型不具有时间分区列，则会重新加载全部数据。您可以查看全量加载章节了解更多。

增量加载：当模型已经构建完毕并投入业务分析，且模型具有时间分区列，您就可以按批次加载新的业务数

据，即增量加载。如每天增量加载订单表中的新数据。增量加载不用重新加载已完成预计算的数据，可以提高

工作效率，节省对资源的使用。您可以查看按日期/时间加载章节了解更多。

2.	 加载数据的方法

加载数据并构建索引的途径有以下几种。

加载数据：在导航栏数据资产	->	模型界面加载指定模型的数据。如果模型具有时间分区列，您可以选择本次
数据加载的时间范围。然后系统会启动任务将对应时间段数据载入并在同时构建索引。

构建索引：点击导航栏数据资产	->	模型，点击具体模型进入具体模型页，点击索引，在索引总览页签编辑并
修改指定模型的聚合索引或明细索引，并选择需要将哪些索引构建至指定的数据范围。

3.	 查看存储大小

您可以在导航栏数据资产	->	模型	界面查看存储列的数据。如果存储大小为	0.00	KB，则表示该模型没有数据。如
果存储大小大于	0.00	KB，则表示已经对该模型加载数据，即该模型拥有预计算好的数据。

如下图所示，模型	Model3	已经加载数据，模型	Model	尚未加载数据。则您的任何查询都不能击中模型	Model。

23

AI	增强建模

模型列表

查询分析

模型加载了数据之后，您可以执行一条查询来分析您的业务数据并且体检	Kyligence	Enterprise	带来的查询分析亚秒级响
应。

1.	 查询分析原则

Kyligence	Enterprise	支持标准的	SQL	查询，当您添加数据源表之后您就可以查询数据了，但是此时查询将下压至
Hive	数据源，当数据量大或查询较复杂时可能会导致查询执行时间较长。

当您完成模型和索引的设计并且加载完数据，再次执行适当的	SQL	查询，此时查询将击中模型，即使用模型中保
存的预计算数据。这样的加速执行可以提速	SQL	几十甚至几百倍。您可以查看查询分析章节了解	SQL	查询的具体
讲解。

您的历史查询将保存在	查询	->	查询历史	界面，您可以查看查询历史章节了解更多。

2.	 查询分析示例

在您导入	SSB	测试数据集后，您可以在导航栏	查询	->	分析	界面的	查询编辑器	输入以下	SQL	查询。我们使用的数
据源	SSB	数据集模拟了在线商城的交易数据。下面	SQL	语句能够查询指定订单时间范围内不同商品的收入，结果
按照收入降序排列。

SELECT	LO_PARTKEY,	SUM(LO_REVENUE)	AS	TOTAL_REVENUE

FROM	SSB.P_LINEORDER

WHERE	LO_ORDERDATE	between	'1993-06-01'	AND	'1994-06-01'

group	by	LO_PARTKEY

order	by	SUM(LO_REVENUE)	DESC

查询结果如下图所示，您可以在查询信息中发现查询对象为	test_model。查询结果展示了在线商城中不同商品的收
入。

24

AI	增强建模

查询结果

任务监控

在使用	Kyligence	Enterprise	的过程中会触发不同的任务，如构建索引、加载数据、抽样表数据的任务。您可以在导航栏
监控	->	任务	界面查看任务列表。更多详细说明请您查看任务监控章节。

任务监控可以帮助您有效的管理	Kyligence	Enterprise	的使用。您可以查看任务的状态来判断操作是否完成、运行环境是
否稳定等。下图展示了当所有的任务都成功完成时的任务监控界面。

任务监控

智能推荐

即使对一些有经验的建模工程师，设计模型和构建索引仍然是一件有挑战且技术性要求较高的工作，模型和索引的维护

又是另一项较为繁重的运维工作。针对这些问题，Kyligence	Enterprise	为	AI	增强模式提供了智能推荐的能力。在该模
式下，用户不仅可以手动建立模型和索引，还可以通过	SQL	自动建立模型。无论是手动建立的模型，还是自动建立的
模型，系统都可以智能地利用查询历史对模型和索引的做进一步的优化。

如何开启或者关闭智能推荐能力？具体如图所示。想要了解更多推荐信息，请参考项目首页章节。

25

AI	增强建模

开启智能推荐

开启智能推荐后，返回到模型页面，您可以查看优化建议信息如下图所示。此时，您可以选择查看一条优化建议的详细

信息，通过单条优化建议，通过部分或全部优化建议等操作。相关的概念以及原理部分，请参考智能推荐章节。

智能推荐

智能推荐模式使得模型运维在更为便捷的同时也更适宜手动调整。更多详细说明请查看模型（索引组）概念与操作章

节。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

26

样例数据集

样例数据集

Kyligence	Enterprise	内置了一个标准的	SSB	数据集（约	5.9	MB），包含了	5	个数据表和	1	个视图表，其中事实表有
60,175	条数据，您可通过该数据集测试或试用各功能模块，快速上手产品。

样例数据集介绍

SSB	样例数据集总共包含了	5	个数据表和	1	个视图表：

表名

类型

说明

LINEORDER

事实表

描述销售订单的明细信息，每一行对应一笔交易订单，包含客户、供应
商、订单金额、销售日期等信息。

P_LINEORDER

基于事实表创
建的视图

描述销售订单的明细信息和一个提前计算好的列（V_REVENUE），其
交易记录与	LINEORDER	表相同。

CUSTOMER

SUPPLIER

DATES

PART

维度表

维度表

维度表

维度表

描述用户的信息，包含用户名称、地址、城市等。

描述供应商的信息，包含供应商名称、地址、电话等。

描述近	7	年的日期信息，如某个日期所在的年份、月份、星期等。

描述零件信息，包含零件的名称、类别、颜色、型号等。

其中，5	个数据表一起构成了整个星型模型的结构，实体-联系图（E-R	图）如下：

实体-联系图

关联关系如下：

LINEORDER	LEFT	JOIN	DATES	ON	LINEORDER.LO_ORDERDATE	=	DATES.D_DATEKEY

LINEORDER	LEFT	JOIN	CUSTOMER	ON	LINEORDER.LO_CUSTKEY	=	CUSTOMER.C_CUSTKEY

LINEORDER	LEFT	JOIN	SUPPLIER	ON	LINEORDER.LO_SUPPKEY	=	SUPPLIER.S_SUPPKEY

LINEORDER	LEFT	JOIN	PART	ON	LINEORDER.LO_PARTKEY	=	PART.P_PARTKEY

27

样例数据集

导入并查看样例数据集

1.	 登录服务器命令行，执行下述格式的命令将	SSB	样例数据集导入	Hive。

$KYLIN_HOME/bin/sample.sh

[!NOTE]

	KYLIN_HOME		需替换为	Kyligence	Enterprise	的安装路径。

2.	 查看样例数据集。

i.	 执行	 	hive		命令进入	Hive	终端。

ii.	 依次执行下述命令查看库表信息。

##	查看数据库列表

show	databases;
##	进入	SSB	数据库

use	ssb;
##	查看	SSB	数据库中的表

show	tables;
##	查询	SUPPLIER	表的记录数

select	count(*)	from	SUPPLIER;

附录：数据表及列介绍

LINEORDER

列名

说明

LO_ORDERKEY

LO_CUSTKEY

LO_PARTKEY

LO_SUPPKEY

LO_ORDERDATE

LO_ORDERPRIORITY

LO_SHIPPRIORITY

LO_LINENUMBER

LO_QUANTITY

LO_EXTENDEDPRICE

LO_ORDTOTALPRICE

LO_DISCOUNT

LO_REVENUE

LO_SUPPLYCOST

LO_TAX

LO_COMMITDATE

订单	ID

顾客	ID

零件	ID

供应商	ID

订单日期

订单优先级

交易优先级

复合主键：L_ORDERKEY，	L_LINENUMBER

数量

额外费用

订单总额

折扣

收入

供应成本

税率

交易日期

28

样例数据集

LO_SHIPMODE

交易模式

CUSTOMER

C_CUSTKEY

C_NAME

C_ADDRESS

C_CITY

C_NATION_PREFIX

C_NATION

C_REGION

C_PHONE

C_MKTSEGMENT

SUPPLIER

S_SUPPKEY

S_NAME

S_ADDRESS

S_CITY

S_NATION_PREFIX

S_NATION

S_REGION

S_PHONE

DATES

D_DATEKEY

D_DATE

D_DAYOFWEEK

D_MONTH

D_YEAR

D_YEARMONTHNUM

D_YEARMONTH

D_DAYNUMINWEEK

D_DAYNUMINMONTH

列名

说明

客户	ID

客户名称

客户地址

客户城市

国家代号

国家

区域

电话

市场部门

列名

说明

供应商	ID

供应商名称

供应商地址

供应商城市

国家代号

国家

区域

电话

列名

说明

日期	ID

日期

星期几

月份

年份

年份数

年月数

周天数

月天数

29

样例数据集

D_DAYNUMINYEAR

D_MONTHINYEAR

D_WEEKNUMINYEAR

D_SELLINGSEASON

D_LASTDAYINWEEKFL

D_LASTDAYINMONTHFL

D_HOLIDAYFL

D_WEEKDAYFL

PART

P_PARTKEY

P_NAME

P_MFGR

P_CATEGORY

P_BRAND

P_COLOR

P_TYPE

P_SIZE

P_CONTAINER

年天数

年月数

年周数

出售季节

星期最后一天

月份最后一天

假日

工作日

列名

说明

零件	ID

零件名称

生产商

种类

品牌

颜色

类型

型号

容量

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

30

申请许可证

申请许可证

许可证是使用	Kyligence	Enterprise	的必要条件，在安装和部署完之后，您需要申请许可证，才能使用本产品。目前
Kyligence	Enterprise	仅提供试用许可证（期限为一个月）。下面将详细介绍申请和更新许可证的流程及具体操作。

申请试用许可证

官网申请

1.	 使用帐号信息登录	Kyligence	帐号中心。如果未申请过帐号，需要先注册	Kyligence	帐号。

2.	 登录后，选择要申请的试用许可证	，并填写一张申请信息表。我们将对您的申请进行审核，通过后，试用许可证将

会通过电子邮件发送给您。

WEB	GUI	申请

注意：只有使用	Azure	Marketplace	的用户才会允许在	Web	端申请许可证。

1.	 启动	Kyligence	Enterprise，在登录页面点击帮助	->	更新许可证会出现下图界面。

31

申请许可证

2.	 点击申请许可证按钮，输入您的企业邮箱，公司名称，用户名称后点击提交即可获得试用许可证，许可证会自动存

储在产品根目录下，然后您可以正常使用	Kyligence	Enterprise。

32

申请许可证

申请正式许可证

1.	 申请和购买	Kyligence	Enterprise	的正式许可证，需要先提供许可证申请文件。您可以在	Kyligence	Enterprise	中，点

击	帮助	->	关于Kyligence	Enterprise。

关于	Kyligence	Enterprise

2.	 然后点击生成许可申请文件。

33

申请许可证

许可证申请文件

3.	 联系您的客户经理，并提供上述的许可申请文件。我们的客户经理将协助您完成剩下的正式许可证申请流程。

加载及更新许可证

1.	 加载：

方法一：请您将许可证文件放在产品的根目录下，重新启动	Kyligence	Enterprise，启动时	Kyligence	Enterprise
会加载产品根目录下的许可证文件。

方法二：首次进入Kyligence	Enterprise，将会有弹窗提醒您加载许可证。

注意：只有使用	Azure	Marketplace	的用户才会有申请许可证的按钮。

34

申请许可证

加载许可证

2.	 更新：如果需要更新许可证，在	Kyligence	Enterprise	登录页面点击帮助	->	更新许可证，可以通过上传许可证文件

或者输入许可证内容完成更新。

35

申请许可证

更新许可证

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

36

全新功能

全新功能

为提升用户用户体验，Kyligence	Enterprise	将定期发布新版本，用于丰富产品功能。本章节将介绍	Kyligence	Enterprise
最新功能及其使用场景，帮助您掌握产品最新动态。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

37

内表使用指南

使用内表

本章将介绍	Kyligence	Enterprise	的全新功能：内表的作用、创建与使用方法、配置项以及注意事项。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

38

内表功能概述

内表功能概述

灵活分析，跳跃的思维火花

Kyligence	的预计算技术可以通过定义模型和索引，帮助您实现大数据量、高并发场景下的亚秒级查询体验	。然而并非
所有的查询分析场景都可以预先定义，而从构建和存储成本角度考虑，也不适合预计算所有维度组合的索引。

在业务分析模式固定之前，分析师往往需要通过灵活探查来挖掘数据价值和规律，亦或是为制作固定报表做准备。	由于
分析维度、度量的多变，数量有限的预计算索引无法完全覆盖所有查询场景，而此时基于内表的现算能力就可以发挥作

用。

什么是内表？

内表（Internal	Table）是指由Kyligence	Enterprise直接管理数据和元数据的表。	相较于原先的数据源表仅导入表元数据
用于建模，内表既保存元数据，又能直接管理用户数据。与传统RDBMS和大多数数仓软件一样，您只需将数据导入内
表，即可进行查询分析。

如何创建内表？

您无需自己编写DDL建表语句，仅需在导入的数据源表页面点击"创建内表"按钮，并完成相关表属性设置后，即可完成
内表创建。	详情请参考管理内表页面。

如何区分数据源表和内表？

查询时无需区分数据源表还是内表，您可以认为它们在Kyligence中是一张表，它只有一个数据库名和表名。区别在于未
开启内表功能或者未创建内表时，该表不直接管理数据，仅用于建模。

如何在项目级开启使用内表功能？

您仅需在项目设置页面，点击"内表设置"标签页，打开内表功能开关即可。

39

内表功能概述

打开内表开关后，您可以在侧边导航栏中看到“内表”页签，点击可以进入内表管理页面。

关于快照功能

在Kyligence	Enterprise	4.x版本及以前，系统支持创建快照表，从Kyligence	Enterprise	5.x开始，当开启内表功能后，快照
功能将不再支持。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

40

管理内表

管理内表

1.	创建内表

Kyligence	Enterprise暂不支持通过SQL	DDL语句创建内表。

当前您可以通过两种方式创建内表：

1.	 在导入数据源表时，勾选“同时加载为内表”，该方式适合在初次导入数据源表的同时批量创建内表。

注意：批量创建内表时，系统默认不会设置分区列等信息，如您需要设置分区列、排序列等信息，请稍后在内表管理页

面进行更新。

1.	 在已导入的数据源表页面点击"创建内表"按钮，并完成相关表属性设置后，即可完成内表创建。

2.	设置内表属性

设置分区列

41

管理内表

内表支持通过设置分区列来提升某些场景下的查询性能。您可以将表中的一个列设置为分区列，该列可以是日期列，也

可以非日期列。但请注意，当且仅当分区列为日期列时，内表可以进行增量加载。	内表不含分区列或分区列为非日期列
时，仅支持全量加载。	我们强烈建议您避免将高基列设置为分区列，生成过多的数据分区可能对查询性能造成负面影
响。

设置主键列（PrimaryKey）和排序列（OrderByKey）

设置主键列和排序列可以提升某些场景下的查询性能。与传统的RDBMS不同，这里的主键列（PrimaryKey）并不是唯
一键约束，仅用于该列在where过滤条件下的查询加速。	需要注意的是，主键列必须是排序列的前缀列。

42

管理内表

您可以点击“	>>	”后进行主键列和排序列的设置

3.	更新内表属性

您可以在内表管理页面进行表属性的更新。

注意：由于内表属性会影响表数据的存储分布方式，在导入数据后您无法再更改分区列等表属性信息。	需要先清空所有
内表数据后再进行修改。

4.	表重载

如果您重载数据源表，内表也将被重载。但是当内表包含数据时无法进行表重载，您需要先清空表数据后再进行表重

载。

5.	清空表数据

您可以在内表管理页面清空内表数据。执行清空表数据操作会同时终止该表所有运行中的数据导入任务。

6.	删除内表

您可以在内表管理页面删除内表，执行删除内表操作将同时清空内表数据并停止运行中的数据导入任务。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

43

内表数据导入

导入内表数据

全量导入

所有内表，无论其是否分区表，都支持全量数据导入。	全量导入适用于数据量大小适中的表，如果表数据量特别大，且

设置了时间分区列，建议使用增量导入的方式。	鼠标移动至需要导入数据的表，点击加载按钮

全量导入无需选择时间范围，系统会将数据源表中的所有数据导入内表。

增量导入

仅设置了时间分区列的表，支持增量导入。增量导入时可以设置导入的起始时间和结束时间，系统会从数据源拉取该时

间范围内的数据导入内表。

44

内表数据导入

请注意：内表并没有唯一键约束与重复数据检查，如果您导入的数据时间范围存在重叠，将可能出现重复数据。如果您

希望更新某些分区数据，可以在删除该分区数据后重新导入。

数据导入任务

提交数据导入任务请求后，您可以在“监控”	->	“批数据任务”中看到运行中的数据导入任务及其运行进度、状态以及日志
等信息。

预加载内表缓存

预加载内表缓存到查询集群	executor	本地磁盘，可以减少查询时对内表文件的访问，从而提高查询性能。

使用参数	 	kylin.internal-table.preloaded-cache.enabled		控制是否开启预加载。参数默认值为	true	，表示开启预加载。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

45

查询内表

查询内表

1.	准备工作

内表查询与模型查询在查询界面上没有区别，详情参考SQL查询

您无需做任何SQL改写，但需要确保所查询的表均已创建了内表并导入数据。

2.	查询内表

在Kyligence	Enterprise的查询界面上，您可以通过勾选“直查内表”来跳过模型匹配阶段。在确定您的查询为灵活查询，
无法通过模型预计算索引回答时，勾选“直查内表”可以节省模型匹配时间，从而提高查询响应速度。

默认不勾选“直查内表”，此时查询引擎将优先进行模型匹配模型预计算索引，当无法通过模型预计算索引回答时，会转
为直查内表。	如果复杂查询的部分子查询能通过模型索引回答，部分不能，系统会尝试通过模型索引和内表联查回答。

3.	下压查询

开启内表功能后，无论查询中的表是否已创建内表，或是否导入数据，查询都不再下压至数据源。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

46

安装部署

安装与配置

在本章中，首先为您介绍	Kyligence	Enterprise	安装的前置条件，接着引导您根据自己的运行环境完成	Kyligence
Enterprise	的快速安装，然后为您介绍	Kyligence	Enterprise	的集群部署和元数据库配置，最后为您介绍一些高级配置。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

47

安装前置条件

安装前置条件

为了保障系统的性能与稳定性，我们建议您将	Kyligence	Enterprise	单独运行在一个独立的	Hadoop	集群上。

下面我们将为您介绍	Kyligence	Enterprise	安装的前置条件。

环境准备

支持的	Hadoop	平台
Java	环境
账户环境

配置元数据库

检查	Zookeeper
HDFS	分布式存储
Spark	StandAlone	集群

推荐资源与配置

集群资源分配

推荐的硬件配置

推荐的	Linux	版本
推荐的客户端配置

Hostname	配置

许可证

支持的	Hadoop	平台

下述企业级数据管理平台及其相应	Hadoop	版本已经过我们的认证和测试：

Cloudera	CDH	5.8	/	6.1	/	6.2	/	6.3

Hortonworks	HDP	2.4
华为	FusionInsight	6.5.1
Apache	Hadoop	2.7.2（从	Kyligence	Enterprise	4.3.3	开始支持）
Cloudera	Data	Platform	(CDP)	7.1（从	Kyligence	Enterprise	4.3.5	开始支持）
华为	FusionInsight	MRS	302（从	Kyligence	Enterprise	4.5.15.2	开始支持）
星环	TDH	6.2.2	（从	Kyligence	Enterprise	4.5.6	开始支持）

其中	Kyligence	Enterprise	需要使用一些组件，请确保每一台服务器都具备以下组件

Hive

HDFS

Yarn

ZooKeeper

Spark

注意：目前本产品会自带	Spark，因此无需您提前安装。如果出于安全和兼容性考虑，您希望将产品安装包中的	Spark
和	Hadoop	相关依赖，替换为环境中已存在的版本，请与	Kyligence	技术支持联系。尽管这样的替换理论上可行，但由
于版本兼容性可能未经测试，您必须在	Kyligence	专家的支持下完成这样的替换。

Java	环境

本产品及其运行的	Hadoop	环境中的所有节点，需要的	Java	环境满足以下条件：

需要您环境的默认	JDK	版本为：JDK	8	(	JDK	1.8_162	或以上小版本)

48

安装前置条件

java	-version

您可以使用以下命令检查您现有环境的	JDK	版本，例如下图显示为	JDK	8

JDK	版本

账户权限

您在运行	Kyligence	Enterprise	时所使用的的	Linux	账户，应当具备访问	Hadoop	集群的权限，包括：

读写	HDFS	上的文件
创建和读取	Hive	表

下面假设使用账户为	 	KyAdmin	，并验证是否具备访问	Hadoop	集群的权限。具体步骤如下：

1.	 测试是否具有	HDFS	读写权限

默认的工作目录为	 	/kylin	，该目录用于存储模型构建后的数据文件。

请手工创建该工作目录并授予权限。一般需要由文件系统管理员	HDFS	用户，为	 	KyAdmin		创建工作目录 	/kylin	，
并且赋予权限。

su	hdfs

hdfs	dfs	-mkdir	/kylin

hdfs	dfs	-chown	KyAdmin	/kylin

hdfs	dfs	-mkdir	/user/KyAdmin

hdfs	dfs	-chown	KyAdmin	/user/KyAdmin

验证	 	KyAdmin		具有读写权限：

hdfs	dfs	-put	<any_file>	/kylin

hdfs	dfs	-put	<any_file>	/user/KyAdmin

2.	 测试	 	KyAdmin		是否具备	Hive	读写权限

假设您有名为	kylinDB	的	Hive	数据库，并且有名为	 	t1		的表，表包含两个字段	 	id,	name	。

验证权限：

#hive

hive>	show	databases;

hive>	use	kylinDB;

hive>	show	tables;

hive>	insert	into	t1	values(1,	"kylin");

hive>	select	*	from	t1;

49

安装前置条件

配置元数据库

本产品需要预先配置元数据库。

我们推荐您使用	Kyligence	Enterprise	安装包中提供的	PostgreSQL	10.7	作为元数据库。具体的安装和配置方法请您参考
使用	PostgreSQL	作为元数据库。

如果您需要使用运行环境中已有的	PostgreSQL	数据库，支持的	PostgreSQL	数据库版本为：

PostgreSQL	9.1	及以上

您也可以选择使用	MySQL	作为元数据库，我们暂时不提供	MySQL	的安装包和	/	或	JDBC	驱动，您需要在运行环境中
提前准备好。具体的安装和配置方法请您参考使用	MySQL	作为元数据库。支持的	MySQL	数据库版本为：

MySQL	5.1	至	5.7，推荐使用	MySQL	5.7

MySQL	8

检查	Zookeeper

可以通过下述步骤快速验证	ZooKeeper	开启	Kerberos	后与本产品的连通性：

1.	 在部署了	ZooKeeper	Client	的节点找到	ZooKeeper	工作目录
2.	 往	 	conf/jaas.conf	文件添加或修改	Client	section:

Client	{

com.sun.security.auth.module.Krb5LoginModule	required

useKeyTab=true

keyTab="/path/to/keytab_assigned_to_kylin"

storeKey=true

useTicketCache=false

principal="principal_assigned_to_kylin";

};

3.	 	export	JVMFLAGS="-Djava.security.auth.login.config=/path/to/jaas.conf"

4.	 	bin/zkCli.sh	-server	${kylin.env.zookeeper-connect-string}
5.	 验证能正常查看	ZooKeeper	节点，例如： 	ls	/
6.	 清理步骤	2	中新增的	Client	section	以及步骤	3	中声明的环境变量	 	unset	JVMFLAGS

如果非官网下载	ZooKeeper,	可以咨询运维人员后进行上述操作。

HDFS	存储，Spark	StandAlone	集群

Kylingence	Enterprise	5	存算分离架构默认采用	HDFS	作为分布式存储，Spark	StandAlone	集群作为计算资源，具体安装
部署请咨询咨询运维人员进行操作。

集群资源分配

为了使	Kyligence	Enterprise	能够高效地完成提交的任务，请您确保使用的	Hadoop	集群的配置满足如下条件：

	yarn.nodemanager.resource.memory-mb		配置项的值不小于	8192	MB
	yarn.scheduler.maximum-allocation-mb		配置项的值不小于	4096	MB
	yarn.scheduler.maximum-allocation-vcores		配置项的值不小于	5

如果您需要在沙箱等虚拟机环境中运行	Kyligence	Enterprise，请您确保该虚拟机环境能够获取如下资源：

处理器个数不小于	4
内存不小于	10	GB
	yarn.nodemanager.resource.cpu-vcores		配置项的值不小于8

50

安装前置条件

推荐的硬件配置

我们推荐您使用下述硬件配置安装	Kyligence	Enterprise：

32	vCore，128	GB	内存
至少1个	1TB	的	SAS	硬盘（3.5寸），7200RPM，RAID1
至少两个	1GbE	的以太网电口，网络端口要求请参照网络端口要求章节。

Spark	StandAlone	集群和	HDFS	分布式存储推荐使用3台独立的物理机，每台物理机配置如下：

48	vCore
256	GB	内存
至少1块	1TB	的	SSD	硬盘

推荐的	Linux	版本

我们推荐您使用下述版本的	Linux	操作系统：

Ubuntu	20.04.x	版本及20以上版本

CentOS	7.x

推荐的客户端配置

CPU：2.5	GHz	Intel	Core	i7
操作系统：macOS	/	Windows	7	/	Windows	10
内存：8G	及以上
浏览器及版本

谷歌	Chrome	50	及以上
Internet	Explorer	11	及以上

Hostname	配置

检查将要安装	Kyligence	Enterprise	节点的	hostname，确保	hostname	中不包括	'_'	字符，否则将无法启动	Kyligence
Enterprise。

许可证

请您在试用本产品前先申请对应的许可证，许可证文件将通过邮件的方式发送至您的邮箱中。请您将许可证放在产品的

安装目录下，具体操作方法请参照申请许可证章节。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:03

51

网络端口要求

网络端口要求

Kyligence	Enterprise	需要与不同的组件进行通信，以下是需要开放给	Kyligence	Enterprise	的端口。该表格中只包含
Hadoop	环境的默认配置，不包含各	Hadoop	平台之间的配置差异。

组件分类

端口要求

端口作用

是否必须

SSH

Kyligence	Enterprise

Kyligence	Enterprise

HDFS

HDFS

Hive

Hive

Zookeeper

Yarn

Yarn

Yarn

Spark

Spark

Spark

Spark

Spark

Influxdb

Influxdb

PostgreSQL

MySQL

22

7070

7443

8020

50010

10000

9083

2181

8088

8090

SSH	连接	KE	所在虚拟机的端口

Kyligence	Enterprise	默认访问端口

Kyligence	Enterprise	HTTPS	默认访问端口

HDFS	接收	Client	连接的	RPC	端口

访问	HDFS	DataNode，数据传输端口

HiveServer2	访问端口

Hive	Metastore	访问端口

Zookeeper	默认端口

Yarn	Web	UI	访问端口

Yarn	Web	UI	HTTPS	访问端口

8050/8032

Yarn	ResourceManager	通信端口

4041

18080

Kyligence	Enterprise	查询引擎	Web	UI	默认端口

Spark	History	Server	端口

(1024,	65535]

Spark	Driver	与	Executor	占用的端口是随机的

7077

Spark	Master	与	Worker	通信端口

8080/8081

Spark	Master	Web	UI	端口

8086

8088

5432

3306

Influxdb	HTTP	端口

Influxdb	RPC	端口

PostgreSQL	默认端口

MySQL	默认端口

是

是

否

是

是

否

是

是

是

否

是

是

否

是

是

是

否

否

是

是

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:03

52

安装

安装

在本章中，将为您介绍	Kyligence	Enterprise	在各个平台的安装步骤及注意事项，最后为您介绍如何卸载	Kyligence
Enterprise。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:03

53

在	Apache	Hadoop	环境安装

在	Apache	Hadoop	环境安装

准备运行环境

首先请确保运行环境分配了充足的资源，如您没有现成的部署环境，您可以通过部署沙箱进行体验。Kyligence
Enterprise	对沙箱的资源要求请参阅安装前置条件。并确保	 	HDFS	、 	YARN	、	 	Hive	、 	ZooKeeper		等组件处于正常状态并
且没有任何警告信息。

Apache	Hadoop	版本支持

Kyligence	Enterprise	支持的	Apache	Hadoop	版本列表：

Apache	Hadoop	2.7.2

注意：暂不支持配置	kerberos	的	Apache	Hadoop	环境。

Apache	Hadoop	版本所需的额外配置

在	 	$KYLIN_HOME/conf/kylin.properties		中添加以下两项配置：

	kylin.env.apache-hadoop-conf-dir		Hadoop	环境中	Hadoop	conf	目录
	kylin.env.apache-hive-conf-dir		Hadoop	环境中	Hive	conf	目录

Apache	Hadoop	版本所需的	jar	包

在	Apache	Hadoop	2.7.2	中，您还需要在	Kyligence	Enterprise	的运行环境中准备	MySQL	的	JDBC	驱动。

此处为您提供	MySQL	5.1	版本的	JDBC	驱动的	jar	文件包的下载链接：https://repo1.maven.org/maven2/mysql/mysql-

connector-java/5.1.41/mysql-connector-java-5.1.41.jar

其余版本的驱动您需要自行准备，请您将对应版本的	MySQL	的	JDBC	驱动放置到	 	$KYLIN_HOME/lib/ext		目录下。

快速安装	Kyligence	Enterprise

准备好了环境之后，请参照快速启动章节安装	Kyligence	Enterprise。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:03

54

在	Cloudera	CDH	环境安装

在	Cloudera	CDH	环境中安装

准备运行环境

首先请确保运行环境分配了充足的资源，如您没有现成的部署环境，您可以通过部署沙箱进行体验。Kyligence
Enterprise	对资源要求请参阅安装前置条件。并确保	 	HDFS	、 	YARN	、 	Hive	、 	ZooKeeper	等组件处于正常状态并且没有
任何警告信息。

Cloudera	CDH	版本支持

Kyligence	Enterprise	支持的	Cloudera	CDH	版本列表：

Cloudera	CDH	5.8	/	6.1	/	6.2	/	6.3

快速安装	Kyligence	Enterprise

准备好了环境之后，请参照快速启动章节安装	Kyligence	Enterprise。

集成	Kerberos

1.	 在安装	YARN	NodeManager	的节点上，添加	Kerberos	对应的用户。如	Kerberos	用户是	 	kylin	，则在	NodeManager

所在的节点的操作系统也应存在	 	kylin		用户。

2.	 将认证所需	 	keytab		文件和	 	krb5.conf		文件放到	 	$KYLIN_HOME/conf/		目录下。
3.	 如果目录	 	$KYLIN_HOME/hadoop_conf		存在，确保该目录下存在	 	krb5.conf		文件，避免构建任务出错：

	java.lang.IllegalArgumentException:	Can't	get	Kerberos	realm

	...

	Caused	by:	KrbException:	Cannot	locate	default	realm

4.	 对于	Cloudera	CDH	平台，请在	 	$KYLIN_HOME/conf/kylin.properties		中设置如下	Kerberos	相关参数。

kylin.kerberos.enabled=true

kylin.kerberos.platform=Standard

kylin.kerberos.principal={your_principal_name}

kylin.kerberos.keytab={your_keytab_name}

注意：	如果您修改了	Kerberos	ticket	生命周期，需要对应修改	Kyligence	Enterprise	中的	ticket	刷新时间间隔。刷新
间隔为	ticket	生命周期的一半或以下，否则可能会出现因	tiket	失效，引起的构建任务卡住及日志大量报错	 	No
valid	credentials	provided	(Mechanism	level:	Failed	to	find	any	Kerberos	tgt)	。	举例说
明： 	$KYLIN_HOME/conf/krb5.conf		中	ticket_lifetime	默认值为	24h，如果您修改为	 	ticket_lifetime	=	12h	，那么您
需要在	 	$KYLIN_HOME/conf/kylin.properties		中添加参数	 	kylin.kerberos.ticket-refresh-interval-minutes	=	360	，
并重启	Kyligence	Enterprise	使之生效。

集成	Sentry

环境准备

请联系您的	Hadoop	管理员来确保您的	CDH	环境中已经启用了	Kerberos	认证，并已按照	CDH	操作手册启用	Sentry	有关
的组件并完成了相关配置，并且启用了	HDFS	ACLs，同时开启了	HDFS	ACLs	和	Sentry	权限同步。

将认证所需	 	krb5.conf		文件放到	 	$KYLIN_HOME/conf/		目录下。

55

在	Cloudera	CDH	环境安装

创建操作系统用户

请确保用于运行	Kyligence	Enterprise	的用户（如： 	ke_user		）及对应用户组（如： 	ke_group		）已经被创建，并将	hive
用户加入	 	ke_group		中。

	$	groupadd	ke_group					#	新建用户组	ke_group
	$	useradd	-g	ke_group	ke_user					#	创建用户	ke_user	并添加到	ke_group	用户组中
	$	usermod	-a	-G	ke_group	hive		#把	hive	用户加入到	ke_group

注意：请确保以上操作在集群的所有节点都执行，以保证权限的成功生效。

创建	Kerberos	用户

1.	 创建	Kerberos	用户	 	ke_user	，在	KDC	部署节点上执行如下命令：

	$	kadmin.local

	kadmin.local	>	addprinc	ke_user

2.	 验证用户

	$	kinit	ke_user

配置	Hive

配置	Hive	Server

1.	 登录	Cloudera	Manager，转到	Hive	服务，单击配置选项卡。
2.	 搜索	Hive	Metastore	访问控制和代理用户组覆盖，找到配置项	 	hadoop.proxyuser.hive.groups	，添加

	ke_group	。

3.	 找到	hive-site.xml	的	Hive	服务高级配置代码段（安全阀），增加如下配置：

名称：	 	hive.metastore.rawstore.impl		值： 	org.apache.sentry.binding.metastore.AuthorizingObjectStore
名称： 	hive.server2.session.hook		值： 	org.apache.sentry.binding.hive.HiveAuthzBindingSessionHook
名称： 	hive.server2.authentication		值： 	KERBEROS
名称： 	hive.server2.enable.doAs		值： 	false

配置	Beeline

1.	 安全环境中需要使用	Beeline	方式访问	Hive，并需要以	Kerberos	用户	hive	操作	Beeline，创建角色，授予权

限。

	$	kinit	hive

	$	beeline	-u	"jdbc:hive2://<HiveServer2>:10000/;principal=hive/{HOST_NAME}@EXAMPLE.COM"

2.	 （可选）如果	hive	没有	admin	权限，赋予	admin	权限

$	create	role	admin;

$	grant	all	on	server	server1	to	role	admin;

$	grant	role	admin	to	group	hive;

3.	 创建一个角色	 	ke_role	，并赋予给组	 	ke_group

	$	create	role	ke_role;

	$	grant	role	ke_role	to	group	ke_group;

56

在	Cloudera	CDH	环境安装

4.	 （可选）如果	Hive	中已经存在	 	ssb		数据库，赋予角色	 	ke_role		查询权限

	$	grant	select	on	database	ssb	to	role	ke_role;

5.	 用于构建的	Hive	数据库，赋予角色	 	ke_role		查询权限（如：default、ssb）

	$	grant	select	on	database	default	to	role	ke_role;

配置	HDFS

为了保证	Kyligence	Enterprise	可以顺利在	HDFS	中读写文件，需要在	HDFS	中执行如下操作：

1.	 使用	Kerberos	用户	 	hdfs		创建对应的工作目录并修改目录权限。

	$	kinit	hdfs

	$	hdfs	dfs	-mkdir	/{working_dir}

	$	hdfs	dfs	-chown	ke_user:ke_group	/{working_dir}

	$	hdfs	dfs	-mkdir	/user/ke_user

	$	hdfs	dfs	-chown	ke_user:ke_group	/user/ke_user

	$	hdfs	dfs	-chmod	-R	775	/{working_dir}

2.	 以	Kerberos	用户	 	hive		操作	Beeline	授予角色	 	ke_role		工作目录和	 	/tmp		所在路径对应	uri	的所有权限。

	$	kinit	hive

	$	beeline	-u	"jdbc:hive2://<HiveServer2>:10000/;principal=hive/{HOST_NAME}@EXAMPLE.COM"

	$	grant	all	on	uri	"hdfs://{namenode}:8020/{working_dir}"	to	role	ke_role;

	$	grant	all	on	uri	"hdfs://{namenode}:8020/tmp"	to	role	ke_role;

	如果	Hadoop	集群启用了	HA，则使用下面的命令来赋予	uri	权限：

	$	grant	all	on	uri	"hdfs://{nameservice}/{working_dir}"	to	role	ke_role;

	$	grant	all	on	uri	"hdfs://{nameservice}/tmp"	to	role	ke_role;

配置	Kyligence	Enterprise

1.	 生成	 	ke_user		用户的	keytab	文件，并将	Kerberos	用户的	keytab	文件拷贝到	 	$KYLIN_HOME/conf/		路径

下， 	{path}	可以是任意您自定义的存放路径。

	$	kadmin.local

	kadmin.local	>	ktadd	-k	/{path}/ke_user.keytab	ke_user

	$	cp	/{path}/ke_user.keytab	$KYLIN_HOME/conf/

2.	 修改	 	$KYLIN_HOME/conf/kylin.properties	，添加或修改如下配置

	kylin.env.hdfs-working-dir={working_dir}

	kylin.kerberos.enabled=true

	kylin.kerberos.platform=Standard

	kylin.kerberos.principal=ke_user

	kylin.kerberos.keytab=ke_user.keytab

3.	 切换到	Kerberos	用户	ke_user，启动	Kyligence	Enterprise

	$	kinit	-kt	${KYLIN_HOME}/conf/ke_user.keytab	ke_user

	$	${KYLIN_HOME}/bin/kylin.sh	start

4.	 更新	 	$KYLIN_HOME/hadoop_conf

57

在	Cloudera	CDH	环境安装

如果您在修改该配置前已经尝试过启动或运行过	 	kylin.sh	，请您将	 	$KYLIN_HOME/hadoop_conf		目录删除后，重新
执行启动脚本。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:03

58

在华为	FusionInsight	环境安装

在华为	FusionInsight	集群上安装

首先请确保运行环境分配了充足的资源，如您没有现成的部署环境，您可以通过部署沙箱进行体验。Kyligence
Enterprise	对沙箱的资源要求请参阅安装前置条件。并确保	 	HDFS	、 	YARN	、 	Hive	、 	ZooKeeper	等组件处于正常状态并
且没有任何警告信息。

Kyligence	Enterprise	支持的华为	FusionInsight	版本列表：

华为	FusionInsight	6.5.1
华为	FusionInsight	MRS	302

注意：

1.	 在华为	FusionInsight	6.5.1	上安装	Kyligence	Enterprise，需要使用	FusionInsight	的	ZooKeeper	组件。

准备运行环境

如果您需要在	FusionInsight	的环境下运行	Kyligence	Enterprise，请在安装前执行下述命令以初始化所需的环境变量：

source	/opt/hadoopclient/bigdata_env	(hadoopclient	为变量)

kinit	<user_name>

快速安装	Kyligence	Enterprise

准备好了环境之后，请参照快速启动章节安装	Kyligence	Enterprise。

集成	Kerberos

准备工作

华为	FusionInsight	平台

1.	 配置	FusionInsight	机机类型账户，该机机类型用户需要拥有如下权限：

HDFS、YARN、Hive	和	ZooKeeper	的相关权限
HDFS	上	Kyligence	Enterprise	工作目录的读/写权限。Kyligence	Enterprise	工作目录在	 	kylin.properties		中的
	kylin.env.hdfs-working-dir		参数指定，默认值为	 	/kylin

2.	 导出该账户的配置（包含	 	keytab		和	 	krb5.conf	文件）。具体操作步骤可以参考如下	FusionInsight	文档，主要步

骤如下：

设置	“机机”类型的账户
导出账户的认证凭据

59

在华为	FusionInsight	环境安装

3.	 将步骤	2	中导出的	 	keytab		文件以及配置文件	 	krb5.conf		放到	 	$KYLIN_HOME/conf/		目录下。
4.	 如果目录	 	$KYLIN_HOME/hadoop_conf		存在，确保该目录下存在	 	krb5.conf		文件，避免构建任务出错：

	java.lang.IllegalArgumentException:	Can't	get	Kerberos	realm

	...

	Caused	by:	KrbException:	Cannot	locate	default	realm

注意：	如果您修改了	Kerberos	ticket	生命周期，需要对应修改	Kyligence	Enterprise	中的	ticket	刷新时间间隔。刷新间隔
为	ticket	生命周期的一半或以下，否则可能会出现因	tiket	失效，引起的构建任务卡住及日志大量报错	 	No	valid
credentials	provided	(Mechanism	level:	Failed	to	find	any	Kerberos	tgt)	。	举例说明： 	$KYLIN_HOME/conf/krb5.conf
中	ticket_lifetime	默认值为	24h，如果您修改为	 	ticket_lifetime	=	12h	，那么您需要在
	$KYLIN_HOME/conf/kylin.properties		中添加参数	 	kylin.kerberos.ticket-refresh-interval-minutes	=	360	，并重启
Kyligence	Enterprise	使之生效。

具体配置

对于华为	FusionInsight	平台，请在	 	$KYLIN_HOME/conf/kylin.properties		中设置如下	Kerberos	相关参数。

kylin.kerberos.platform=FI

kylin.kerberos.principal={your_principle_name}

kylin.kerberos.keytab={your_keytab_name}

kylin.kerberos.enabled=true

kylin.storage.columnar.spark-conf.spark.yarn.access.hadoopFileSystems=hdfs://nameservice

kylin.engine.spark-conf.spark.yarn.access.hadoopFileSystems=hdfs://nameservice

华为	FusionInsight	环境下的特别注意事项

在	HDFS	上创建	Kyligence	Enterprise	的工作目录，并将对应的读写权限赋予启动	Kyligence	Enterprise	的账户。默认的工
作目录为 	/kylin	。同时，Kyligence	Enterprise	需要向	 	/user/{current_user}		目录下写入临时数据，因此也需要创建对
应目录的权限。请您运行下述命令，进行相应权限配置：

hdfs	dfs	-mkdir	/kylin

hdfs	dfs	-chown	root	/kylin

hdfs	dfs	-chmod	755	/tmp/hive-scratch

hdfs	dfs	-mkdir	/user/root

hdfs	dfs	-chown	root	/user/root

60

在华为	FusionInsight	环境安装

提示：您可以在	 	$KYLIN_HOME/conf/kylin.properties		配置文件中修改	Kyligence	Enterprise	工作目录的位置。

如果您所使用的账户在	HDFS	上没有读写权限，请先转至 	hdfs	账户，然后再创建工作目录并授予权限。执行下述命
令：

su	hdfs

hdfs	dfs	-mkdir	/kylin

hdfs	dfs	-chown	root	/kylin

hdfs	dfs	-chmod	755	/tmp/hive-scratch

hdfs	dfs	-mkdir	/user/root

hdfs	dfs	-chown	root	/user/root

更新	 	$KYLIN_HOME/hadoop_conf	：如果您在修改该配置前已经尝试过启动或运行过	 	kylin.sh	，请您将
	$KYLIN_HOME/hadoop_conf		目录删除后，重新执行启动脚本。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:03

61

在	Hortonworks	HDP	环境安装

在	Hortonworks	HDP	环境安装

准备运行环境

首先请确保运行环境分配了充足的资源，如您没有现成的部署环境，您可以通过部署沙箱进行体验。Kyligence
Enterprise	对沙箱的资源要求请参阅安装前置条件。并确保	 	HDFS	、 	YARN	、	 	Hive	、 	ZooKeeper		等组件处于正常状态并
且没有任何警告信息。

Hortonworks	HDP	版本支持

Kyligence	Enterprise	支持的	Hortonworks	HDP	版本列表：

Hortonworks	HDP	2.4

注意：在某些发行版中，如	HDP	2.4	中，您还需要将环境中的	 	hive-site.xml		文件中将	Hive	的默认引擎由	 	tez		修改
为	 	mr	。该文件通常位于	 	/etc/hive/{version}/hive-site.xml	。

<property>

				<name>hive.execution.engine</name>

						<!--	change	tez	to	mr	-->

				<value>tez</value>

</property>

如果您在修改该配置前已经尝试过启动或运行过	 	kylin.sh	。请您将	 	$KYLIN_HOME/hadoop_conf		目录删除后，重新执行
启动脚本。

快速安装	Kyligence	Enterprise

准备好了环境之后，请参照快速启动章节安装	Kyligence	Enterprise。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:03

62

在星环	TDH	环境安装

在星环	TDH	环境安装

首先请确保运行环境分配了充足的资源，如您没有现成的部署环境，您可以通过部署沙箱进行体验。Kyligence
Enterprise	对沙箱的资源要求请参阅安装前置条件。并确保	 	HDFS	、 	YARN	、	 	Hive	、 	ZooKeeper		等组件处于正常状态并
且没有任何警告信息。

Kyligence	Enterprise	支持的星环	TDH	版本列表：

星环	TDH	6.2.2	（从	Kyligence	Enterprise	4.5.6	开始支持）

准备运行环境

如果您需要在星环	TDH	的环境下运行	Kyligence	Enterprise，请在星环	Transwarp	Manager	下载	TDH-Client	到将要安装
Kyligence	Enterprise	的节点上，并执行下述命令以初始化所需的环境变量：

	export	TDH_CLIENT_HOME=${TDH_CLIENT_HOME_PATH}	(TDH_CLIENT_HOME_PATH	变量为	TDH	CLIENT	的主目录)

	source	$TDH_CLIENT_HOME/init.sh

执行完上述命令后，确保	hadoop	命令可用。

星环	TDH	版本所需的额外配置

因为星环	TDH	是在	Docker	中启动的	Hadoop	各项服务，并且默认的是	JDK1.7，而	Kyligence	Enterprise	是部署在宿主机
中，并且需要	JDK1.8，所以需要指定	JDK	版本。在	 	$KYLIN_HOME/conf/kylin.properties		中添加以下四项配置：

kylin.storage.columnar.spark-conf.spark.yarn.appMasterEnv.JAVA_HOME=/usr/java/jdk1.8.0_25

kylin.storage.columnar.spark-conf.spark.executorEnv.JAVA_HOME=/usr/java/jdk1.8.0_25

kylin.engine.spark-conf.spark.yarn.appMasterEnv.JAVA_HOME=/usr/java/jdk1.8.0_25

kylin.engine.spark-conf.spark.executorEnv.JAVA_HOME=/usr/java/jdk1.8.0_25	-

快速安装	Kyligence	Enterprise

准备好了环境之后，请参照快速启动章节安装	Kyligence	Enterprise。

集成	Kerberos

准备工作

星环	TDH	平台

1.	 配置	TDH	Guardian	用户，该用户需要拥有如下权限：

HDFS、YARN、Hive	和	ZooKeeper	的相关权限
Kyligence	Enterprise	依赖的	Hive	数据库的读/写权限

HDFS	上	Kyligence	Enterprise	工作目录的读/写权限。Kyligence	Enterprise	工作目录在	 	kylin.properties		中的
	kylin.env.hdfs-working-dir		参数指定，默认值为	 	/kylin

2.	 导出该账户的配置（包含	 	keytab		和	 	krb5.conf	文件），具体操作步骤可参考星环	TDH	文档。

3.	 将步骤	2	中导出的	 	keytab		文件以及配置文件	 	krb5.conf		放到	 	$KYLIN_HOME/conf/		目录下。

4.	 如果目录	 	$KYLIN_HOME/hadoop_conf		存在，确保该目录下存在	 	krb5.conf		文件，避免构建任务出错：

63

在星环	TDH	环境安装

java.lang.IllegalArgumentException:	Can't	get	Kerberos	realm

...

Caused	by:	KrbException:	Cannot	locate	default	realm

具体配置

对于星环	TDH	平台，请在	 	$KYLIN_HOME/conf/kylin.properties		中设置如下	Kerberos	相关参数。

	kylin.kerberos.platform=TDH

	kylin.kerberos.principal={your_principle_name}

	kylin.kerberos.keytab={your_keytab_name}

	kylin.kerberos.enabled=true

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:03

64

配置	RDBMS	元数据库

配置	RDBMS	元数据存储

Kyligence	Enterprise	2.4+	版本可以支持关系型数据库作为元数据存储，通过使用标准	JDBC	Driver	连接	Metastore	数据
库。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:03

65

MySQL

MySQL

Kyligence	Enterprise	支持将	MySQL	数据库作为元数据存储，安装和使用方法参见：

安装	MySQL
使用	MySQL	作为元数据库

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:03

66

MySQL

安装	MySQL

准备工作

1.	 支持的	MySQL	版本为：

MySQL	5.1	至	5.7，推荐使用	MySQL	5.7

MySQL	8

2.	 您需要在	Kyligence	Enterprise	的运行环境中准备	MySQL	的	JDBC	驱动。

3.	 此处为您提供	MySQL	8	版本的	JDBC	驱动的	jar	文件包的下载链接，兼容从5.6以后的版本：

https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.28/mysql-connector-java-8.0.28.jar

其余版本的驱动您需要自行准备。

4.	 请您将对应版本的	MySQL	的	JDBC	驱动放置到	 	$KYLIN_HOME/lib/ext		目录下。

非	 	root		用户下安装	MySQL

以下以非	 	root		用户	 	abc		在	CentOS	7	上安装	MySQL	5.7	为例说明安装步骤(同时适用于	 	root		用户)。

1.	 新建一个目录 	/home/abc/mysql	，并且将	MySQL	的安装包放置在该目录下，执行以下命令解压	 	rpm		包：

cd	/home/abc/mysql

tar	-xvf	mysql-5.7.37-1.el7.x86_64.rpm-bundle.tar

得到以下RPM安装包：

	mysql-community-common-5.7.37-1.el7.x86_64.rpm		 	mysql-community-libs-5.7.37-1.el7.x86_64.rpm		 	mysql-

community-client-5.7.37-1.el7.x86_64.rpm		 	mysql-community-server-5.7.37-1.el7.x86_64.rpm		 	mysql-community-
devel-5.7.37-1.el7.x86_64.rpm

注意：	请自行准备	MySQL	安装包

2.	 检查系统环境是否安装了其他版本的MySQL

示例1：

rpm	-qa	|	grep	mysql

yum	-y	remove	MySQL-server-5.5.61-1.el6.x86_64

示例2：

rpm	-qa	|	grep	mariadb

yum	-y	remove	mariadb-libs-5.5.68-1.el7.x86_64

3.	 按如下顺序执行命令解压	 	rpm		包

rpm2cpio	mysql-community-common-5.7.37-1.el7.x86_64.rpm	|	cpio	-idmv

rpm2cpio	mysql-community-libs-5.7.37-1.el7.x86_64.rpm	|	cpio	-idmv

rpm2cpio	mysql-community-client-5.7.37-1.el7.x86_64.rpm	|	cpio	-idmv

rpm2cpio	mysql-community-server-5.7.37-1.el7.x86_64.rpm	|	cpio	-idmv

4.	 使用命令	 	vi	~/mysql/etc/my.cnf		编辑配置文件，请您添加以下配置信息：

[client]

port	=	3306

socket=/home/abc/socket/mysql.sock

67

MySQL

[mysql]

no-auto-rehash

socket=/home/abc/socket/mysql.sock

[mysqld]

user=abc

basedir=/home/abc/mysql/usr

datadir=/home/abc/sql_data

socket=/home/abc/socket/mysql.sock

secure-file-priv=/home/abc/mysql_files

port=3306

请您创建上述配置信息中对应的文件夹：

在	 	/home/abc/mysql		路径下创建文件夹	 	usr
在	 	/home/abc		路径下创建文件夹	 	sql_data
在	 	/home/abc		路径下创建文件夹	 	socket
在	 	/home/abc		路径下创建文件夹	 	mysql_files

之后在	 	/home/abc/mysql		路径下执行命令：

./usr/bin/mysql_install_db	--defaults-file=etc/my.cnf	--user=abc	--basedir=/home/abc/mysql/usr	--datadir=/h

ome/abc/sql_data

5.	 在	 	/home/abc/mysql		路径下，执行以下命令启动	MySQL：

./usr/sbin/mysqld	--defaults-file=etc/my.cnf	&

6.	 查看	mysql	5.7	默认密码

cat	./home/abc/.mysql_secret

通过默认密码可登录	mysql	5.7

usr/bin/mysql	-u	root	-p

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:03

68

MySQL

使用	MySQL	作为元数据库

准备工作

1.	 安装	MySQL,如果您未安装	MySQL，请查看安装	MySQL	章节完成安装。

配置	MySQL	为元数据库

以下以	MySQL	5.7	为例说明配置步骤：

1.	 在	MySQL	数据库中新建名为	 	kylin		的数据库

2.	 在	Kyligence	Enterprise	安装目录下的	 	$KYLIN_HOME/conf/kylin.properties		配置文件中，配置	 	kylin.metadata.url	=

{metadata_name}@jdbc	， 	{metadata_name}		需要替换为您需要的元数据表名，如
	kylin_default_instance@jdbc	， 	{metadata_name}		允许的最大长度为29。

注意：如果该表已存在，则会使用现有的表；如果不存在，则会自动创建该表。

具体示例如下：

kylin.metadata.url={metadata_name}@jdbc,driverClassName=com.mysql.jdbc.Driver,url=jdbc:mysql://{host}:{port

}/kylin?useUnicode=true&characterEncoding=utf8,username={user},password={password},maxTotal=50,maxIdle=8

各配置项的含义如下，其中	 	url	， 	username		和	 	password		为必须配置项，其余项若不配置将使用默认配置值：

driverClassName：JDBC	的	driver	类名，默认值为	 	com.mysql.jdbc.Driver	；
url：JDBC	的	url；

host：连接	MySQL	服务器的	IP	地址，默认值为	 	localhost	；
port：连接	MySQL	服务器的端口号，默认值为	 	3306	，您可以根据实际端口号进行配置；
kylin:	元数据库名称。请确保	MySQL	中已创建	 	kylin		数据库；

username：JDBC	的用户名；
password：JDBC	的密码；
maxTotal：最大数据库连接数，默认值为	50
maxIdle：最大等待中的连接数量，默认值为	8
注意：

若您的查询	SQL	包含中文，请在	metadata.url	配置编码为	utf8，避免查询历史出现乱码：

useUnicode=true&characterEncoding=utf8
若您的	LDAP	用户名/用户组名包含中文，请在	metadata.url	配置编码为	utf8，避免查询历史出现乱码以
及权限出现丢失：useUnicode=true&characterEncoding=utf8

3.	 如果需要对	JDBC	密码进行加密，可以使用如下方式：

i.	在${KYLIN_HOME}路径下执行以下命令，获取加密后的密码

./bin/kylin.sh	io.kyligence.kap.tool.general.CryptTool	-e	AES	-s	<password>

ii.	配置	 	kylin.metadata.url		的	 	password		为如下形式

password=ENC('${encrypted_password}')

举例，以下假设	JDBC	密码为	kylin：

首先，加密	JDBC	密码	kylin

69

MySQL

${KYLIN_HOME}/bin/kylin.sh	io.kyligence.kap.tool.general.CryptTool	-e	AES	-s	kylin

AES	encrypted	password	is:

YeqVr9MakSFbgxEec9sBwg==

然后，配置	 	kylin.metadata.url	，如下：

kylin.metadata.url={metadata_name}@jdbc,driverClassName=com.mysql.jdbc.Driver,url=jdbc:mysql://{host}:{port

}/kylin?useUnicode=true&characterEncoding=utf8,username={user},password=ENC('YeqVr9MakSFbgxEec9sBwg=='),max

Total=20,maxIdle=20

4.	 如果需要配置	MySQL	集群模式，url	需要添加	 	replication		或者	 	loadbalance		并在前后两端加入双引号 	"	，示例

如下：

#使用	replication	配置集群模式

	kylin.metadata.url=kylin_default_instance@jdbc,driverClassName=com.mysql.jdbc.Driver,url="jdbc:mysql:repli

cation://localhost:3306,localhost:3307/kylin?useUnicode=true&characterEncoding=utf8",username=root,password

=,maxTotal=20,maxIdle=20

#使用	loadbalance	配置集群模式

	kylin.metadata.url=kylin_default_instance@jdbc,driverClassName=com.mysql.jdbc.Driver,url="jdbc:mysql:loadb

alance://localhost:3306,localhost:3307/kylin?useUnicode=true&characterEncoding=utf8",username=root,password

=,maxTotal=20,maxIdle=20

5.	 请确保在使用	MySQL	时使用的存储引擎是	InnoDB	不是	MyISAM，修改默认存储引擎方式如下：

[mysqld]

default-storage-engine	=	InnoDB

FAQ

Q：JDK	升级至	JDK	8u261	版本后，启动	Kyligence	Enterprise	报错，提示创建	admin	用户失败，怎么办？

A：当您使用	JDK	8u261版本，且元数据库使用	MySQL	5.6	和	5.7	版本时。由于从	JDK	8u261	版本开始禁用了	TLS	1.2
之前的版本，而	MySQL	5.6	和	5.7	版本默认使用的是	TLS	1.0	或	TLS	1.1，而且	MySQL	默认情况下必须建立	SSL	连
接，因此和	TLS	协议冲突，导致了启动	Kyligence	Enterprise	报错，您将在终端看到报错提示为	 	Create	Admin	user
failed	。

您有	2	种解决方式：

方式一：修改元数据配置参数，增加	 	useSSL=false

kylin.metadata.url={metadata_name}@jdbc,driverClassName=com.mysql.jdbc.Driver,url=jdbc:mysql://{host}:{port}/ky

lin?useSSL=false,useUnicode=true&characterEncoding=utf8,username={user},password={password},maxTotal=50,maxIdle

=8

方式二：修改	java	安全文件	 	java.security	，找到下面这段配置，删除	TLSv1,	TLSv1.1

#		jdk.tls.disabledAlgorithms=MD5,	SSLv3,	DSA,	RSA	keySize	<	2048

jdk.tls.disabledAlgorithms=SSLv3,	TLSv1,	TLSv1.1,	RC4,	DES,	MD5withRSA,	DH	keySize	<	1024,	EC	keySize	<	224,	3D

ES_EDE_CBC,	anon,	NULL,	include	jdk.disabled.namedCurves

Q：元数据服务中断后，有什么注意事项？

A：需要恢复元数据服务，恢复后，您需要重启所有	Kyligence	Enterprise	节点，否则可能导致查询失败等未知错误。

Q:	任务提交失败，并且日志中出现	 	max_allowed_packet		相关错误时，应该如何处理？

70

MySQL

A：元数据库	MySQL	默认配置	 	max_allowed_packet		值较小，此配置会限制	Kyligence	Enterprise	节点与元数据库通信时
数据包大小。当任务元数据较为复杂时，如单次提交构建的	Segment	数量过多时，实际通信时数据包大小会超过此限
制。更多内容请参考	MySQL	官方文档

您可以调整	MySQL	配置为	 	max_allowed_packet=256M	来规避此问题。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:03

71

PostgreSQL

PostgreSQL

Kyligence	Enterprise	支持将	PostgreSQL	数据库作为元数据存储，安装和使用方法参见：

安装	PostgreSQL
使用	PostgreSQL	作为元数据库

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:03

72

PostgreSQL

安装	PostgreSQL

准备工作

1.	 Kyligence	Enterprise	推荐使用	PostgreSQL	作为默认元数据库，自带的	PostgreSQL	10.7	安装包包含在产品安装包根

目录下的	 	postgresql		目录中	。

2.	 如果使用其他版本的	PostgreSQL	，请您选择	PostgreSQL	9.1	及以上版本。

3.	 自带的	PostgreSQL	安装包目前支持在	CentOS	6、CentOS	7	和	CentOS	8	中安装，对应关系如下：

以	 	rhel6.x86_64.rpm		结尾的安装包适合	CentOS	6
以	 	rhel7.x86_64.rpm		结尾的安装包适合	CentOS	7
以	 	rhel8.x86_64.rpm		结尾的安装包适合	CentOS	8

请您首先确定	Linux	版本信息再选择对应的安装包进行安装。您可以使用命令	 	uname	-a		查看内核版本，或命令
	cat	/etc/issue		查看系统版本。

4.	 本节我们将演示	PostgreSQL	10.7	在	CentOS	6	上的安装步骤。

	root		用户下安装	PostgreSQL

1.	 在解压	Kyligence	Enterprise	后，你可以进入根目录下的	 	postgresql		目录，并按顺序执行以下命令安装	PostgreSQL

安装包。

rpm	-ivh	postgresql10-libs-10.7-1PGDG.rhel6.x86_64.rpm

rpm	-ivh	postgresql10-10.7-1PGDG.rhel6.x86_64.rpm

rpm	-ivh	postgresql10-server-10.7-1PGDG.rhel6.x86_64.rpm

2.	 初始化	PostgreSQL	数据库

系统已安装	initscripts	服务的执行以下命令：

service	postgresql-10	initdb

系统未安装	initscripts	服务的，在	PostgreSQL	bin	目录执行以下命令：

$PGSQL_HOME/pgsql-10/bin/postgresql-10-setup	initdb
示例：/user/pgsql-10/bin/postgresql-10-setup	initdb

3.	 您需要修改以下两个	PostgreSQL	的配置文件，文件在	 	/var/lib/pgsql/10/data/		目录下：

	pg_hba.conf	：主要用来存放客户端的认证信息。

	postgresql.conf

i.	使用命令	 	vi	pg_hba.conf		打开文件可以看到如下一行初始配置：

host				all													all													127.0.0.1/32												ident

请您将上述配置修改为下面所示，即将最后的	 	ident		修改为	 	md5	：

host				all													all													127.0.0.1/32												md5

73

PostgreSQL

提示：上述修改可以使您匹配本地	（	IP	地址为： 	localhost		或者	 	127.0.0.1		）	的任意用户连接任意数据
库，并通过	 	md5		验证用户密码。

同时，请您在本文件末尾添加如下一行：

host				all													all													0.0.0.0/0															md5

提示：上述修改可以使您匹配任意	IPv4	地址的任意用户连接任意数据库，并通过	 	md5		验证用户密码。

字段说明：

	host	：连接的方式， 	host		代表通过	TCP	/	IP	建立的连接；
第一个 	all	：表示匹配所有数据库；

第二个 	all	：表示匹配所有用户；

	0.0.0.0/0	：表示匹配所有	IPv4	地址；
	md5	：执行	 	md5		验证用户的密码。

提示：	您可以根据实际情况配置相应的匹配规则。

ii.	使用命令	 	vi	postgresql.conf		打开文件并修改如下两条配置：

listen_addresses	=	'*'

#	port	=	5432

字段说明：

	listen_addresses	：指定服务器监听客户端连接的	TCP	/	IP	地址。本字段值的形式为逗号分隔的主机名或数字
IP	地址列表，例如， 	listen_addresses	=	host1,host2,host3		或者	 	listen_address	=
10.1.1.1,10.1.1.2,10.1.1.3	。特殊项	 	*		对应所有可用的	IP	接口。您可以根据需要进行修改。
	port	：端口，默认值为	 	5432	。如果	 	5432		端口被占用，您可以根据实际情况进行修改。

4.	 执行命令	 	service	postgresql-10	start		启动	PostgreSQL

5.	 登录	PostgreSQL	并创建数据库

i.	执行命令	 	su	-	postgres		切换为	 	postgres		用户。

提示:	 	postgres		是	PostgreSQL	安装过程中自动创建的	Linux	用户。

ii.	执行命令	 	/usr/pgsql-10/bin/psql		连接	PostgreSQL	服务器。

以上命令会默认连接到	 	5432		端口。如果您之前在	 	postgresql.conf		配置文件中修改过端口，请您使用	 	-p		选项
连接到配置的端口号。假设您在	 	postgresql.conf		文件中配置的端口号是	 	5433	，请您使用命令	 	/usr/pgsql-
10/bin/psql	-p	5433	。

iii.	Kyligence	Enterprise	中默认使用	 	postgres		作为用户名连接	PostgreSQL，您需要设置	 	postgres		用户的密码，执
行命令	 	ALTER	USER	postgres	PASSWORD	'kylin';		设置用户密码为	 	kylin	。

注意：	请您注意在命令行末尾加上	 	;

iv.	执行命令	 	create	database	kylin;		创建数据库，数据库名称为	 	kylin	。

注意：	请您注意在命令行末尾加上	 	;

v.	您可以通过命令	 	\l		查看数据库是否创建成功，如下图所示，我们已经创建了名称为	 	kylin		的数据库。

74

PostgreSQL

查看	kylin	数据库

非	 	root		用户下安装	PostgreSQL

以下示例是	Linux	用户	 	abc		安装和配置	PostgreSQL。

1.	 您首先创建一个目录	 	/home/abc/postgresql	，然后在该目录下解压并安装	PostgreSQL	的	 	rpm		安装包。

rpm2cpio	postgresql10-libs-10.7-1PGDG.rhel6.x86_64.rpm	|	cpio	-idmv

rpm2cpio	postgresql10-10.7-1PGDG.rhel6.x86_64.rpm	|	cpio	-idmv

rpm2cpio	postgresql10-server-10.7-1PGDG.rhel6.x86_64.rpm	|	cpio	-idmv

注意：请您注意用户	 	abc		至少拥有对文件读写的权利。

2.	 请您编辑	 	~/.bash_profile		文件并在末尾新增配置	 	export	LD_LIBRARY_PATH=/home/abc/postgresql/usr/pgsql-

10/lib	，并使用命令	 	source	~/.bash_profile		使上述对	 	~/.bash_profile		文件的配置生效。

3.	 配置数据库

i.	您可以通过以下命令初始化数据库	：

~/postgresql/usr/pgsql-10/bin/initdb	-A	md5	-U	postgres	-W	-D	~/postgresql/var/lib/pgsql/10/data/

字段说明：

-A	md5:	采用	 	md5		验证的方式验证用户密码
-U	postgres:	指定用户	 	postgres
-W:	设置用户	 	postgres		的密码
-D	~/postgresql/var/lib/pgsql/10/data/:	指定配置文件的存放目录

如下图所示，输入命令后根据提示输入密码并再次确认密码，该密码是	PostgreSQL	中用户	 	postgres		的密码，假
设输入的密码是	 	kylin	。

75

PostgreSQL

初始化数据库

ii.	编辑配置文件

步骤一：您可以通过以下命令创建	Unix	Socket	通信的目录	:

mkdir	~/postgresql/socket

步骤二：您可以按照以下内容编辑配置文件	 	~/postgresql/var/lib/pgsql/10/data/postgresql.conf	：

listen_addresses	=	'*'

unix_socket_directories	=	'/home/abc/postgresql'

#port	=	5432

注意：在配置	Unix	Socket	通信的目录	 	/home/abc/postgresql		时，当前用户至少有对该目录读写的权限。

步骤三：请您在配置文件	 	~/postgresql/var/lib/pgsql/10/data/pg_hba.conf		末尾添加如下一行：

host				all													all													0.0.0.0/0															md5

4.	 执行以下命令启动	PostgreSQL：

~/postgresql/usr/pgsql-10/bin/pg_ctl	-D	~/postgresql/var/lib/pgsql/10/data/	-l	~/postgresql/var/lib/pgsql/1

0/pgstartup.log	start

5.	 执行以下命令通过客户端连接	PostgreSQL：

~/postgresql/usr/pgsql-10/bin/psql	-U	postgres	-h	localhost

以上命令会默认连接到	 	5432		端口。如果您之前在	postgresql.conf	配置文件中修改过端口，请您使用	 	-p		选项连接
到配置的端口号。假设您在	postgresql.conf	文件中配置的端口号是	 	5436	，请您使用以下命令：

~/postgresql/usr/pgsql-10/bin/psql	-U	postgres	-h	localhost	-p	5436

之后，请您根据提示输入密码，即可进入	PostgreSQL	客户端。

76

PostgreSQL

6.	 执行以下命令创建名称为	 	kylin		的数据库：

create	database	kylin;

注意：

请您注意在命令行末尾加上	 	;
您可以通过	 	\l		命令查询	 	kylin		数据库是否创建成功

FAQ

Q：怎样解决非	root	用户初始化	PostgreSQL	时报错	 	libicu18n.so.42:cannot	open	shared	object	file:	no	such	file	or
directory		？

有两种解决方案：

方案一：确保安装	PostgreSQL	的节点可以访问外网，然后在终端输入命令	 	yum	install	libicu-devel		下载	libicui18n。

方案二：访问网站	https://pkgs.org/download/libicu	自行下载需要的包，请根据系统内核选择合适的版本，如	CentOS	6	可
以下载	 	libicu-4.2.1-14.el6.x86_64.rpm	，然后通过命令	 	rpm2cpio	libicu-4.2.1-14.el6.x86_64.rpm	|	cpio	-idmv		解压
该二进制包，并将解压后的内容放在	 	$LD_LIBRARY_PATH		中。如果您不清楚	 	$LD_LIBRARY_PATH	，请参考上述非	 	root		用
户下安装和配置方法的第二步。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:03

77

PostgreSQL

使用	PostgreSQL	作为元数据库

准备工作

1.	 Kyligence	Enterprise	推荐使用	PostgreSQL	作为默认元数据库，自带的	PostgreSQL	10.7	安装包包含在产品安装包根

目录下的	 	postgresql		目录中	。

2.	 如果使用其他版本的	PostgreSQL	，请您选择	PostgreSQL	9.1	及以上版本。
3.	 如果您未安装	PostgreSQL，请查看安装	PostgreSQL	章节完成安装。

配置	PostgreSQL	为元数据库

接下来我们将介绍如何配置	PostgreSQL	为	Kyligence	Enterprise	的元数据库。

1.	 您可以在	Kyligence	Enterprise	安装目录下的	 	/conf/kylin.properties		配置文件中，配置	 	kylin.metadata.url	=

{metadata_name}@jdbc	， 	{metadata_name}		需要替换为您需要的元数据表名，如
	ke_metadata@jdbc	， 	{metadata_name}		允许的最大长度为28。具体示例如下：

kylin.metadata.url={metadata_name}@jdbc,driverClassName=org.postgresql.Driver,url=jdbc:postgresql://{host}:

{port}/kylin,username={user},password={password}

各配置项的含义如下，其中	 	url	， 	username		和	 	password		为必须配置项，其余项若不配置将使用默认配置值：

url：JDBC	的	url，其中：

host：连接	PostgreSQL	服务器的	IP	地址，默认值为	 	localhost	；
port：连接	PostgreSQL	服务器的端口号，默认值为	 	5432	，您可以根据实际端口号进行配置；
kylin:	元数据库名称。请确保	PostgreSQL	中已创建	 	kylin		数据库；

username：JDBC	的用户名，默认值为	 	postgres	；
password：JDBC	的密码，默认值为空，请您根据实际密码进行配置；
driverClassName：JDBC	的	driver	类名，默认值为	 	org.postgresql.Driver	；

vi.	如果需要配置集群模式，多个服务器地址之间使用逗号 	,	分割，同时在	url	前后两端需要添加双引号 	"	，示例
如下：

kylin.metadata.url=ke_metadata@jdbc,driverClassName=org.postgresql.Driver,url="jdbc:postgresql://{host}:{po

rt},{ip}:{port}.../kylin",username=postgres,password=kylin

2.	 如果需要对	JDBC	密码进行加密，可以使用如下方式：

i.	在${KYLIN_HOME}路径下执行以下命令，获取加密后的密码

./bin/kylin.sh	io.kyligence.kap.tool.general.CryptTool	-e	AES	-s	<password>

ii.	配置	 	kylin.metadata.url		的	 	password		为如下形式

password=ENC('${encrypted_password}')

举例，以下假设	JDBC	密码为	kylin：

首先，加密	JDBC	密码	kylin

${KYLIN_HOME}/bin/kylin.sh	io.kyligence.kap.tool.general.CryptTool	-e	AES	-s	kylin

AES	encrypted	password	is:

YeqVr9MakSFbgxEec9sBwg==

78

PostgreSQL

然后如下配置	 	kylin.metadata.url	：

kylin.metadata.url=ke_metadata@jdbc,driverClassName=org.postgresql.Driver,url="jdbc:postgresql://{host}:{po

rt},{ip}:{port}.../kylin",username=postgres,password=ENC('YeqVr9MakSFbgxEec9sBwg==')

FAQ

Q：元数据服务中断后，有什么注意事项？

A：需要恢复元数据服务，恢复后，您需要重启所有	Kyligence	Enterprise	节点，否则可能导致查询失败等未知错误。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:03

79

元数据库建表语句

元数据库建表语句

Kyligence	Enterprise	在运行时会自动创建几张表，如果	Kyligence	Enterprise	没有建表权限，就需要运维人员手动创建，
下文将展示建表语句以及相关的权限。

建表信息

若元数据对应的表为自定义如	 	ke_metadata	，则会分别创建如下	13	张表：

ke_metadata：元数据表，记录了所有元数据信息；

ke_metadata_audit_log	:	元数据历史记录，记录了最近	50	万条元数据的变更历史；

ke_metadata_session_v2	:	在开启配置项	 	spring.session.store-type=jdbc		时存储	session	信息，集群部署时必须配置
并开启此配置项；

注意：Kyligence	Enterprise	4.5.10.0	前，表名为	ke_metadata_session。

ke_metadata_session_v2_attributes	:	同上，存储	session	相关的详细信息。

注意：Kyligence	Enterprise	4.5.10.0	前，表名为	ke_metadata_session_attributes。

ke_metadata_query_history	:	每一条查询的信息

ke_metadata_query_history_realization	:	查询击中的每个索引信息

ke_metadata_rec_candidate	:	优化建议信息

注意：Kyligence	Enterprise	4.6.18.0	及后续版本，表名为	ke_metadata_rec_candidate_v2

ke_metadata_epoch	:	全局及项目级别资源所属	Kyligence	节点的信息

ke_metadata_favorite_rule:	优化建议偏好设置

注意：从	Kyligence	Enterprise	4.6.18.0	开始，新增这张表

ke_metadata_async_task:	推荐任务信息

注意：从	Kyligence	Enterprise	4.6.18.0	开始，新增这张表

ke_metadata_query_history_offset:	查询历史消费记录

注意：从	Kyligence	Enterprise	4.6.18.0	开始，新增这张表

ke_metadata_job_info:	任务元数据

注意：从	Kyligence	Enterprise	4.6.18.0	开始，新增这张表

ke_metadata_job_lock:	节点抢占任务的信息

注意：从	Kyligence	Enterprise	4.6.18.0	开始，新增这张表

建表语句

使用	PostgreSQL	作为元数据库

从	Kyligence	Enterprise	4.6.18.0	开始	，建表语句如下：

CREATE	TABLE	IF	NOT	EXISTS	public.ke_metadata	(

				meta_table_key	varchar(255)	NOT	NULL	COLLATE	"C",

80

元数据库建表语句

				meta_table_content	bytea	NULL,

				meta_table_ts	int8	NULL,

				meta_table_mvcc	int8	NULL,

				CONSTRAINT	ke_metadata_pkey	PRIMARY	KEY	(meta_table_key)

);

CREATE	TABLE	IF	NOT	EXISTS	public.ke_metadata_audit_log	(

				id	bigserial	NOT	NULL,

				meta_key	varchar(255)	NULL	COLLATE	"C",

				meta_content	bytea	NULL,

				meta_ts	int8	NULL,

				meta_mvcc	int8	NULL,

				unit_id	varchar(50)	NULL,

				"operator"	varchar(100)	NULL,

		instance	varchar(100)	NOT	NULL,

				CONSTRAINT	ke_metadata_audit_log_pkey	PRIMARY	KEY	(id)

);

CREATE	TABLE	IF	NOT	EXISTS	public.ke_metadata_session_v2	(

			PRIMARY_ID	CHAR(36)	NOT	NULL,

			SESSION_ID	CHAR(180)	NOT	NULL,

			CREATION_TIME	BIGINT	NOT	NULL,

			LAST_ACCESS_TIME	BIGINT	NOT	NULL,

			MAX_INACTIVE_INTERVAL	INT	NOT	NULL,

			EXPIRY_TIME	BIGINT	NOT	NULL,

			PRINCIPAL_NAME	VARCHAR(200),

			CONSTRAINT	ke_metadata_session_v2_PK	PRIMARY	KEY	(PRIMARY_ID)

);

CREATE	UNIQUE	INDEX	ke_metadata_session_v2_IX1	ON	public.ke_metadata_session_v2	(SESSION_ID);

CREATE	INDEX	ke_metadata_session_v2_IX2	ON	public.ke_metadata_session_v2	(EXPIRY_TIME);

CREATE	INDEX	ke_metadata_session_v2_IX3	ON	public.ke_metadata_session_v2	(PRINCIPAL_NAME);

CREATE	TABLE	IF	NOT	EXISTS	public.ke_metadata_session_v2_ATTRIBUTES	(

			SESSION_PRIMARY_ID	CHAR(36)	NOT	NULL,

			ATTRIBUTE_NAME	VARCHAR(200)	NOT	NULL,

			ATTRIBUTE_BYTES	BYTEA	NOT	NULL,

			CONSTRAINT	ke_metadata_session_v2_ATTRIBUTES_PK	PRIMARY	KEY	(SESSION_PRIMARY_ID,	ATTRIBUTE_NAME),

			CONSTRAINT	ke_metadata_session_v2_ATTRIBUTES_FK	FOREIGN	KEY	(SESSION_PRIMARY_ID)	REFERENCES	public.ke_metada

ta_session_v2(PRIMARY_ID)	ON	DELETE	CASCADE

);

CREATE	TABLE	IF	NOT	EXISTS	public.ke_metadata_query_history	(

				id		serial,

				query_id		VARCHAR(50),

				sql_text		TEXT,

				sql_pattern		TEXT,

				duration		BIGINT,

				total_scan_bytes		BIGINT,

				total_scan_count		BIGINT,

				result_row_count		BIGINT,

				submitter		VARCHAR(255),

				realizations		TEXT,

				server		VARCHAR(50),

				error_type		VARCHAR(50),

				engine_type		VARCHAR(30),

				cache_hit		BOOLEAN,

				query_status		VARCHAR(20),

				index_hit		BOOLEAN,

				query_time		BIGINT,

				month		VARCHAR(10),

				query_first_day_of_month		BIGINT,

				query_first_day_of_week		BIGINT,

				query_day		BIGINT,

				is_table_index_used		BOOLEAN,

				is_agg_index_used		BOOLEAN,

				is_table_snapshot_used		BOOLEAN,

81

元数据库建表语句

				project_name		VARCHAR(100),

				reserved_field_1	VARCHAR(50),

				reserved_field_2	VARCHAR(50),

				reserved_field_3	bytea,

				reserved_field_4	bytea,

				primary	key	(	id	,	project_name	)

);

CREATE	INDEX	ke_metadata_query_history_ix1	ON	public.ke_metadata_query_history	USING	btree	(	query_time	);

CREATE	INDEX	ke_metadata_query_history_ix2	ON	public.ke_metadata_query_history	USING	btree	(	query_first_day_of

_month	);

CREATE	INDEX	ke_metadata_query_history_ix3	ON	public.ke_metadata_query_history	USING	btree	(	query_first_day_of

_week	);

CREATE	INDEX	ke_metadata_query_history_ix4	ON	public.ke_metadata_query_history	USING	btree	(	query_day	);

CREATE	INDEX	ke_metadata_query_history_ix5	ON	public.ke_metadata_query_history	USING	btree	(	duration	);
--从	Kyligence	Enterprise	4.6.1.0	开始，增加下面五个索引

CREATE	INDEX	ke_metadata_query_history_ix8	ON	public.ke_metadata_query_history	USING	btree	(engine_type,project

_name);

CREATE	INDEX	ke_metadata_query_history_ix9	ON	public.ke_metadata_query_history	USING	btree	(submitter);

CREATE	INDEX	ke_metadata_query_history_ix10	ON	public.ke_metadata_query_history	USING	btree	(query_status);

CREATE	INDEX	ke_metadata_query_history_ix11	ON	public.ke_metadata_query_history	USING	btree	(server);

CREATE	INDEX	ke_metadata_query_history_ix12	ON	public.ke_metadata_query_history	USING	btree	(query_id);
--从	Kyligence	Enterprise	4.6.23.0	开始，增加下面两个索引

CREATE	INDEX	ke_metadata_query_history_ix6	ON	public.ke_metadata_query_history	USING	btree	(	project_name	);

CREATE	INDEX	ke_metadata_query_history_ix7	ON	public.ke_metadata_query_history	USING	btree	(	project_name,	subm

itter,	query_time	);

CREATE	TABLE	IF	NOT	EXISTS	public.ke_metadata_query_history_realization	(

				id		serial,

				query_id		VARCHAR(255)	,

				model		VARCHAR(255),

				layout_id		VARCHAR(255),

				index_type		VARCHAR(255),

				duration		BIGINT,

				query_time		BIGINT,

				project_name		VARCHAR(255),

				primary	key(id	,	project_name)

);

CREATE	INDEX	ke_metadata_query_history_realization_ix1	ON	public.ke_metadata_query_history_realization	USING	bt

ree	(	query_time	);

CREATE	INDEX	ke_metadata_query_history_realization_ix2	ON	public.ke_metadata_query_history_realization	USING	bt

ree	(	model	);

CREATE	TABLE	IF	NOT	EXISTS	ke_metadata_rec_candidate_v2	(

				id	serial,

				project	varchar(100),

				model_id	varchar(40),

				unique_flag	varchar(200),

				semantic_version	int,

				type	smallint,

				rec_entity	text,

				depend_ids	text,

				layout_metric	text,

				cost	double	precision,

				total_latency_of_last_day	double	precision,

				hit_count	int,

				total_time	double	precision,

				max_time	double	precision,

				min_time	double	precision,

				query_history_info	bytea,

				state	smallint,

				create_time	bigint,

				update_time	bigint,

				mvcc	bigint,

				reserved_field_1	VARCHAR(50),

				reserved_field_2	bytea,

82

元数据库建表语句

				reserved_field_3	bytea,

				primary	key(id)

);

CREATE	UNIQUE	INDEX	ke_metadata_rec_candidate_v2_idx	ON	public.ke_metadata_rec_candidate_v2	using	btree	(projec

t,	model_id,	unique_flag,	semantic_version);

CREATE	TABLE	IF	NOT	EXISTS	public.ke_metadata_epoch

(

				epoch_id																integer,

				epoch_target												varchar(255)

								constraint	ke_metadata_epoch_epoch_target_uindex

												unique,

				current_epoch_owner					varchar(2000),

				last_epoch_renew_time			bigint,

				server_mode													varchar(10),

				maintenance_mode_reason	varchar(5000),

				mvcc																				bigint,

				reserved_field_1								varchar(50),

				reserved_field_2								bytea,

				reserved_field_3								bytea

);

CREATE	TABLE	IF	NOT	EXISTS	public.ke_metadata_favorite_rule	(

		id	bigserial	not	null,

		project	VARCHAR(255)	not	null,

		type	VARCHAR(255)	not	null,

		query_history_id_offset	BIGINT,

		update_time	BIGINT,

		create_time	BIGINT,

		mvcc	BIGINT	not	null,

		primary	key	(id),

		unique	(project,	type)

);

CREATE	TABLE	IF	NOT	EXISTS	public.ke_metadata_async_task	(

		id	serial	primary	key,

		task_type	VARCHAR(255)	not	null,

		task_key	VARCHAR(255)	not	null,

		project	VARCHAR(255)	not	null,

		task_attributes	TEXT,

		update_time	BIGINT,

		create_time	BIGINT,

		mvcc	BIGINT	not	null,

		unique	(task_type,	task_key)

);

CREATE	TABLE	IF	NOT	EXISTS	public.ke_metadata_query_history_offset	(

		id	bigserial	not	null,

		project	VARCHAR(255)	not	null,

		type	VARCHAR(255)	not	null,

		query_history_id_offset	BIGINT,

		update_time	BIGINT,

		create_time	BIGINT,

		mvcc	BIGINT	not	null,

		primary	key	(id),

		unique	(project,	type)

);

CREATE	TABLE	IF	NOT	EXISTS	public.ke_metadata_job_info	(

		id	SERIAL	PRIMARY	KEY,

		job_id	varchar(100)	UNIQUE	NOT	NULL,

		job_type	varchar(50)	NOT	NULL,

		job_status	varchar(50)	NOT	NULL,

		project	varchar(100)	NOT	NULL,

		subject	varchar(200)	NOT	NULL,

		model_id	varchar(100),

		priority	integer	DEFAULT	3,

		mvcc	bigint,

83

元数据库建表语句

		job_content	bytea	NOT	NULL,

		create_time	bigint,

		update_time	bigint,

		job_duration_millis	bigint	NOT	NULL	DEFAULT	'0'

);

comment	on	column	ke_metadata_job_info.job_duration_millis	is	'total	duration	milliseconds';

create	index	ke_metadata_job_info_ix

				on	ke_metadata_job_info	(project,	job_status,	job_type,	subject);
--从	Kyligence	Enterprise	4.6.21.0	开始，增加索引

create	index	ke_metadata_job_info_project_model_id_ix

				on	ke_metadata_job_info	(project,	model_id);

CREATE	TABLE	IF	NOT	EXISTS	public.ke_metadata_job_lock	(

		id	SERIAL	PRIMARY	KEY,

		project	varchar(100)	NOT	NULL,

		lock_id	varchar(100)	UNIQUE	NOT	NULL,

		lock_node	varchar(50)	DEFAULT	NULL,

		lock_expire_time	timestamptz	DEFAULT	NULL,

		priority	integer	DEFAULT	3,

		create_time	bigint,

		update_time	bigint

);

comment	on	column	ke_metadata_job_lock.lock_id	is	'what	is	locked';

comment	on	column	ke_metadata_job_lock.lock_node	is	'who	locked	it';

comment	on	column	ke_metadata_job_lock.lock_expire_time	is	'when	does	the	lock	expire';

从	Kyligence	Enterprise	4.5.10.0	到	Kyligence	Enterprise	4.6.16.0	，建表语句如下：

CREATE	TABLE	IF	NOT	EXISTS	public.ke_metadata	(

				meta_table_key	varchar(255)	NOT	NULL	COLLATE	"C",

				meta_table_content	bytea	NULL,

				meta_table_ts	int8	NULL,

				meta_table_mvcc	int8	NULL,

				CONSTRAINT	ke_metadata_pkey	PRIMARY	KEY	(meta_table_key)

);

CREATE	TABLE	IF	NOT	EXISTS	public.ke_metadata_audit_log	(

				id	bigserial	NOT	NULL,

				meta_key	varchar(255)	NULL	COLLATE	"C",

				meta_content	bytea	NULL,

				meta_ts	int8	NULL,

				meta_mvcc	int8	NULL,

				unit_id	varchar(50)	NULL,

				"operator"	varchar(100)	NULL,

		instance	varchar(100)	NOT	NULL,

				CONSTRAINT	ke_metadata_audit_log_pkey	PRIMARY	KEY	(id)

);

CREATE	TABLE	IF	NOT	EXISTS	public.ke_metadata_session_v2	(

			PRIMARY_ID	CHAR(36)	NOT	NULL,

			SESSION_ID	CHAR(180)	NOT	NULL,

			CREATION_TIME	BIGINT	NOT	NULL,

			LAST_ACCESS_TIME	BIGINT	NOT	NULL,

			MAX_INACTIVE_INTERVAL	INT	NOT	NULL,

			EXPIRY_TIME	BIGINT	NOT	NULL,

			PRINCIPAL_NAME	VARCHAR(200),

			CONSTRAINT	ke_metadata_session_v2_PK	PRIMARY	KEY	(PRIMARY_ID)

);

CREATE	UNIQUE	INDEX	ke_metadata_session_v2_IX1	ON	public.ke_metadata_session_v2	(SESSION_ID);

CREATE	INDEX	ke_metadata_session_v2_IX2	ON	public.ke_metadata_session_v2	(EXPIRY_TIME);

CREATE	INDEX	ke_metadata_session_v2_IX3	ON	public.ke_metadata_session_v2	(PRINCIPAL_NAME);

CREATE	TABLE	IF	NOT	EXISTS	public.ke_metadata_session_v2_ATTRIBUTES	(

			SESSION_PRIMARY_ID	CHAR(36)	NOT	NULL,

			ATTRIBUTE_NAME	VARCHAR(200)	NOT	NULL,

84

元数据库建表语句

			ATTRIBUTE_BYTES	BYTEA	NOT	NULL,

			CONSTRAINT	ke_metadata_session_v2_ATTRIBUTES_PK	PRIMARY	KEY	(SESSION_PRIMARY_ID,	ATTRIBUTE_NAME),

			CONSTRAINT	ke_metadata_session_v2_ATTRIBUTES_FK	FOREIGN	KEY	(SESSION_PRIMARY_ID)	REFERENCES	public.ke_metada

ta_session_v2(PRIMARY_ID)	ON	DELETE	CASCADE

);

CREATE	TABLE	IF	NOT	EXISTS	public.ke_metadata_query_history	(

				id		serial,

				query_id		VARCHAR(50),

				sql_text		TEXT,

				sql_pattern		TEXT,

				duration		BIGINT,

				total_scan_bytes		BIGINT,

				total_scan_count		BIGINT,

				result_row_count		BIGINT,

				submitter		VARCHAR(255),

				realizations		TEXT,

				server		VARCHAR(50),

				error_type		VARCHAR(50),

				engine_type		VARCHAR(30),

				cache_hit		BOOLEAN,

				query_status		VARCHAR(20),

				index_hit		BOOLEAN,

				query_time		BIGINT,

				month		VARCHAR(10),

				query_first_day_of_month		BIGINT,

				query_first_day_of_week		BIGINT,

				query_day		BIGINT,

				is_table_index_used		BOOLEAN,

				is_agg_index_used		BOOLEAN,

				is_table_snapshot_used		BOOLEAN,

				project_name		VARCHAR(100),

				reserved_field_1	VARCHAR(50),

				reserved_field_2	VARCHAR(50),

				reserved_field_3	bytea,

				reserved_field_4	bytea,

				primary	key	(	id	,	project_name	)

);

CREATE	INDEX	ke_metadata_query_history_ix1	ON	public.ke_metadata_query_history	USING	btree	(	query_time	);

CREATE	INDEX	ke_metadata_query_history_ix2	ON	public.ke_metadata_query_history	USING	btree	(	query_first_day_of

_month	);

CREATE	INDEX	ke_metadata_query_history_ix3	ON	public.ke_metadata_query_history	USING	btree	(	query_first_day_of

_week	);

CREATE	INDEX	ke_metadata_query_history_ix4	ON	public.ke_metadata_query_history	USING	btree	(	query_day	);

CREATE	INDEX	ke_metadata_query_history_ix5	ON	public.ke_metadata_query_history	USING	btree	(	duration	);
--从	Kyligence	Enterprise	4.6.1.0	开始，增加下面五个索引

CREATE	INDEX	ke_metadata_query_history_ix8	ON	public.ke_metadata_query_history	USING	btree	(engine_type,project

_name);

CREATE	INDEX	ke_metadata_query_history_ix9	ON	public.ke_metadata_query_history	USING	btree	(submitter);

CREATE	INDEX	ke_metadata_query_history_ix10	ON	public.ke_metadata_query_history	USING	btree	(query_status);

CREATE	INDEX	ke_metadata_query_history_ix11	ON	public.ke_metadata_query_history	USING	btree	(server);

CREATE	INDEX	ke_metadata_query_history_ix12	ON	public.ke_metadata_query_history	USING	btree	(query_id);
--从	Kyligence	Enterprise	4.6.23.0	开始，增加下面两个索引

CREATE	INDEX	ke_metadata_query_history_ix6	ON	public.ke_metadata_query_history	USING	btree	(	project_name	);

CREATE	INDEX	ke_metadata_query_history_ix7	ON	public.ke_metadata_query_history	USING	btree	(	project_name,	subm

itter,	query_time	);

CREATE	TABLE	IF	NOT	EXISTS	public.ke_metadata_query_history_realization	(

				id		serial,

				query_id		VARCHAR(255)	,

				model		VARCHAR(255),

				layout_id		VARCHAR(255),

				index_type		VARCHAR(255),

				duration		BIGINT,

				query_time		BIGINT,

				project_name		VARCHAR(255),

85

元数据库建表语句

				primary	key(id	,	project_name)

);

CREATE	INDEX	ke_metadata_query_history_realization_ix1	ON	public.ke_metadata_query_history_realization	USING	bt

ree	(	query_time	);

CREATE	INDEX	ke_metadata_query_history_realization_ix2	ON	public.ke_metadata_query_history_realization	USING	bt

ree	(	model	);

CREATE	TABLE	IF	NOT	EXISTS	ke_metadata_rec_candidate	(

				id	serial,

				project	varchar(100),

				model_id	varchar(40),

				unique_flag	varchar(200),

				semantic_version	int,

				type	smallint,

				rec_entity	text,

				depend_ids	text,

				layout_metric	text,

				cost	double	precision,

				total_latency_of_last_day	double	precision,

				hit_count	int,

				total_time	double	precision,

				max_time	double	precision,

				min_time	double	precision,

				query_history_info	bytea,

				state	smallint,

				create_time	bigint,

				update_time	bigint,

				reserved_field_1	VARCHAR(50),

				reserved_field_2	bytea,

				reserved_field_3	bytea,

				primary	key(id)

);

CREATE	UNIQUE	INDEX	ke_metadata_rec_candidate_idx	ON	public.ke_metadata_rec_candidate	using	btree	(project,	mod

el_id,	unique_flag,	semantic_version);

CREATE	TABLE	IF	NOT	EXISTS	public.ke_metadata_epoch

(

				epoch_id																integer,

				epoch_target												varchar(255)

								constraint	ke_metadata_epoch_epoch_target_uindex

												unique,

				current_epoch_owner					varchar(2000),

				last_epoch_renew_time			bigint,

				server_mode													varchar(10),

				maintenance_mode_reason	varchar(5000),

				mvcc																				bigint,

				reserved_field_1								varchar(50),

				reserved_field_2								bytea,

				reserved_field_3								bytea

);

注意：Kyligence	Enterprise	4.5.10.0	以前，上述	ke_metadata_session_v2	和	ke_metadata_session_v2_ATTRIBUTES
的表名应该修改为	ke_metadata_session	和	ke_metadata_session_attributes。对应建表语句如下：

CREATE	TABLE	IF	NOT	EXISTS	public.ke_metadata_session	(

				session_id	varchar(180)	NOT	NULL,

				creation_time	int8	NOT	NULL,

				last_access_time	int8	NOT	NULL,

				max_inactive_interval	int4	NOT	NULL,

				principal_name	varchar(200)	NULL,

				CONSTRAINT	ke_metadata_session_pk	PRIMARY	KEY	(session_id)

);

CREATE	INDEX	ke_metadata_session_ix1	ON	public.ke_metadata_session	USING	btree	(last_access_time);

CREATE	INDEX	ke_metadata_session_ix2	ON	public.ke_metadata_session	USING	btree	(principal_name);

86

元数据库建表语句

CREATE	TABLE	IF	NOT	EXISTS	public.ke_metadata_session_attributes	(

				session_id	varchar(180)	NOT	NULL,

				attribute_name	varchar(200)	NOT	NULL,

				attribute_bytes	bytea	NOT	NULL,

				CONSTRAINT	ke_metadata_session_attributes_pk	PRIMARY	KEY	(session_id,	attribute_name),

				CONSTRAINT	ke_metadata_session_attributes_fk	FOREIGN	KEY	(session_id)	REFERENCES	public.ke_metadata_s

ession(session_id)	ON	DELETE	CASCADE

);

CREATE	INDEX	ke_metadata_session_attributes_ix1	ON	public.ke_metadata_session_attributes	USING	btree	(ses

sion_id);

使用	MySQL	作为元数据库

从	Kyligence	Enterprise	4.6.18.0	开始	，建表语句如下：

CREATE	TABLE	IF	NOT	EXISTS	`ke_metadata`	(
		`META_TABLE_KEY`	varchar(255)	CHARACTER	SET	utf8	COLLATE	utf8_bin	NOT	NULL	comment	'元数据唯一标识',
		`META_TABLE_CONTENT`	longblob	comment	'元数据内容',
		`META_TABLE_TS`	bigint(20)	DEFAULT	NULL	comment	'元数据更新时间',
		`META_TABLE_MVCC`	bigint(20)	DEFAULT	NULL	comment	'元数据当前版本',

		PRIMARY	KEY	(`META_TABLE_KEY`)

)	ENGINE=INNODB;

CREATE	TABLE	IF	NOT	EXISTS	`ke_metadata_audit_log`	(
		`id`	bigint(20)	NOT	NULL	AUTO_INCREMENT	comment	'自增	id',
		`meta_key`	varchar(255)	CHARACTER	SET	utf8	COLLATE	utf8_bin	DEFAULT	NULL	comment	'当前版本	metadata	的主键',
		`meta_content`	longblob	comment	'当前版本	metadata	的内容',
		`meta_ts`	bigint(20)	DEFAULT	NULL	comment	'metadata	更新时间',
		`meta_mvcc`	bigint(20)	DEFAULT	NULL	comment	'metadata	更新时的版本',
		`unit_id`	varchar(50)	DEFAULT	NULL	comment	'更新	metadata	的事务	id',
		`operator`	varchar(100)	DEFAULT	NULL	comment	'更新	metadata	的用户',
		`instance`	varchar(100)	NOT	NULL	comment	'更新	metadata	的节点信息',

		PRIMARY	KEY	(`id`)

)	ENGINE=INNODB;

CREATE	TABLE	IF	NOT	EXISTS	`ke_metadata_session_v2`	(

			`PRIMARY_ID`	CHAR(36)	NOT	NULL,

			`SESSION_ID`	CHAR(180)	NOT	NULL,

			`CREATION_TIME`	BIGINT	NOT	NULL,

			`LAST_ACCESS_TIME`	BIGINT	NOT	NULL,

			`MAX_INACTIVE_INTERVAL`	INT	NOT	NULL,

			`EXPIRY_TIME`	BIGINT	NOT	NULL,

			`PRINCIPAL_NAME`	VARCHAR(200),

			CONSTRAINT	`ke_metadata_session_v2_PK`	PRIMARY	KEY	(`PRIMARY_ID`)

)	ENGINE=InnoDB	ROW_FORMAT=DYNAMIC;

CREATE	UNIQUE	INDEX	ke_metadata_id_session_v2_IX1	ON	ke_metadata_session_v2	(SESSION_ID);

CREATE	INDEX	ke_metadata_session_v2_IX2	ON	ke_metadata_session_v2	(EXPIRY_TIME);

CREATE	INDEX	ke_metadata_session_v2_IX3	ON	ke_metadata_session_v2	(PRINCIPAL_NAME);

CREATE	TABLE	IF	NOT	EXISTS	`ke_metadata_session_v2_ATTRIBUTES`	(

			`SESSION_PRIMARY_ID`	CHAR(36)	NOT	NULL,

			`ATTRIBUTE_NAME`	VARCHAR(200)	NOT	NULL,

			`ATTRIBUTE_BYTES`	BLOB	NOT	NULL,

			CONSTRAINT	`ke_metadata_session_v2_ATTRIBUTES_PK`	PRIMARY	KEY	(`SESSION_PRIMARY_ID`,	`ATTRIBUTE_NAME`),

			CONSTRAINT	`ke_metadata_session_v2_ATTRIBUTES_FK`	FOREIGN	KEY	(`SESSION_PRIMARY_ID`)	REFERENCES	`ke_metadata

_session_v2`(`PRIMARY_ID`)	ON	DELETE	CASCADE)	ENGINE=InnoDB	ROW_FORMAT=DYNAMIC;

CREATE	TABLE	IF	NOT	EXISTS	`ke_metadata_query_history`	(

				id	bigint	not	null	auto_increment,

				`query_id`	VARCHAR(50),

				`sql_text`	TEXT,

				`sql_pattern`	TEXT,

				`duration`	BIGINT,

				`total_scan_bytes`	BIGINT,

				`total_scan_count`	BIGINT,

				`result_row_count`	BIGINT,

87

元数据库建表语句

				`submitter`	VARCHAR(255),

				`realizations`	TEXT,

				`server`	VARCHAR(50),

				`error_type`	VARCHAR(50),

				`engine_type`	VARCHAR(30),

				`cache_hit`	BOOLEAN,

				`query_status`	VARCHAR(20),

				`index_hit`	BOOLEAN,

				`query_time`	BIGINT,

				`month`	VARCHAR(10),

				`query_first_day_of_month`	BIGINT,

				`query_first_day_of_week`	BIGINT,

				`query_day`	BIGINT,

				`is_table_index_used`	BOOLEAN,

				`is_agg_index_used`	BOOLEAN,

				`is_table_snapshot_used`	BOOLEAN,

				`project_name`	VARCHAR(100),

				`reserved_field_1`	VARCHAR(50),

				`reserved_field_2`	VARCHAR(50),

				`reserved_field_3`	longblob,

				`reserved_field_4`	longblob,

				primary	key(`id`,`project_name`)

)	DEFAULT	CHARSET=utf8;

ALTER	table	ke_metadata_query_history	ADD	INDEX	ke_metadata_query_history_ix1(`query_time`);

ALTER	table	ke_metadata_query_history	ADD	INDEX	ke_metadata_query_history_ix2(`query_first_day_of_month`);

ALTER	table	ke_metadata_query_history	ADD	INDEX	ke_metadata_query_history_ix3(`query_first_day_of_week`);

ALTER	table	ke_metadata_query_history	ADD	INDEX	ke_metadata_query_history_ix4(`query_day`);

ALTER	table	ke_metadata_query_history	ADD	INDEX	ke_metadata_query_history_ix5(`duration`);
--从	Kyligence	Enterprise	4.6.1.0	开始，增加下面五个索引

ALTER	table	ke_metadata_query_history	ADD	INDEX	ke_metadata_query_history_ix8(`engine_type`,`project_name`);

ALTER	table	ke_metadata_query_history	ADD	INDEX	ke_metadata_query_history_ix9(`submitter`);

ALTER	table	ke_metadata_query_history	ADD	INDEX	ke_metadata_query_history_ix10(`query_status`);

ALTER	table	ke_metadata_query_history	ADD	INDEX	ke_metadata_query_history_ix11(`server`);

ALTER	table	ke_metadata_query_history	ADD	INDEX	ke_metadata_query_history_ix12(`query_id`);
--从	Kyligence	Enterprise	4.6.23.0	开始，增加下面两个索引

ALTER	table	ke_metadata_query_history	ADD	INDEX	ke_metadata_query_history_ix6(	project_name	);

ALTER	table	ke_metadata_query_history	ADD	INDEX	ke_metadata_query_history_ix7(	project_name,	submitter,	query_t

ime	);

CREATE	TABLE	IF	NOT	EXISTS	`ke_metadata_query_history_realization`	(

		id	bigint	not	null	auto_increment,

		`query_id`	VARCHAR(255)	,

		`model`	VARCHAR(255),

		`layout_id`	VARCHAR(255),

		`index_type`	VARCHAR(255),

		`duration`	BIGINT,

		`query_time`	BIGINT,

		`project_name`	VARCHAR(255),

		primary	key	(`id`,`project_name`)

)	DEFAULT	CHARSET=utf8;

ALTER	table	ke_metadata_query_history_realization	ADD	INDEX	ke_metadata_query_history_realization_ix1(`query_ti

me`);

ALTER	table	ke_metadata_query_history_realization	ADD	INDEX	ke_metadata_query_history_realization_ix2(`model`);

CREATE	TABLE	IF	NOT	EXISTS	`ke_metadata_rec_candidate_v2`	(
		`id`	int	not	null	auto_increment	comment	'自增	id',
		`project`	varchar(100)	comment	'项目名称',
		`model_id`	varchar(40)	comment	'模型	id',
		`unique_flag`	varchar(200)	comment	'唯一标识',
		`semantic_version`	int	comment	'语义版本',
		`type`	tinyint	comment	'类别',
		`rec_entity`	text	comment	'建议内容',
		`depend_ids`	text	comment	'依赖的建议	id',
		`layout_metric`	text	comment	'索引指标',
		`cost`	double	comment	'代价',
		`total_latency_of_last_day`	double	comment	'总延迟',
		`hit_count`	int	comment	'命中次数',

88

元数据库建表语句

		`total_time`	double	comment	'总耗时',
		`max_time`	double	comment	'最大耗时',
		`min_time`	double	comment	'最小耗时',
		`query_history_info`	text	comment	'查询历史信息',
		`state`	tinyint	comment	'状态',
		`create_time`	long	comment	'创建时间',
		`update_time`	long	comment	'更新时间',

		`mvcc`	long	comment	'mvcc',
		`reserved_field_1`	VARCHAR(50)	comment	'保留字段1',
		`reserved_field_2`	longblob	comment	'保留字段2',
		`reserved_field_3`	longblob	comment	'保留字段3',

			primary	key(id)

)	DEFAULT	CHARSET=utf8;

ALTER	TABLE	ke_metadata_rec_candidate_v2	ADD	UNIQUE	ke_metadata_rec_candidate_v2_idx	(project,	model_id,	unique

_flag,	semantic_version);

CREATE	TABLE	IF	NOT	EXISTS	`ke_metadata_epoch`

(

				epoch_id																int(11)										null,

				epoch_target												varchar(255)	NOT	null,

				current_epoch_owner					varchar(2000)				null,

				last_epoch_renew_time			bigint(20)							null,

				server_mode													varchar(10)						null,

				maintenance_mode_reason	varchar(5000)				null,

				mvcc																				bigint(20)							null,

				reserved_field_1								varchar(50)						null,

				reserved_field_2								longblob									null,

				reserved_field_3								longblob									null,

				PRIMARY	KEY	(epoch_target)

)	ENGINE=INNODB	DEFAULT	CHARSET=utf8;

CREATE	TABLE	IF	NOT	EXISTS	`ke_metadata_favorite_rule`	(
		id	bigint	not	null	auto_increment	comment	'自增	id',
		`project`	VARCHAR(255)	not	null	comment	'项目名称',
		`conds`	TEXT	comment	'规则定义',
		`name`	VARCHAR(255)	comment	'规则名称',
		`enabled`	BOOLEAN	comment	'是否启用',
		`update_time`	BIGINT	comment	'更新时间',
		`create_time`	BIGINT	comment	'创建时间',

		`mvcc`	BIGINT	not	null	comment	'mvcc',

		primary	key	(`id`),

		UNIQUE	KEY	(`project`,	`name`)

)	DEFAULT	CHARSET=utf8;

CREATE	TABLE	IF	NOT	EXISTS	`ke_metadata_async_task`	(
		id	bigint	not	null	auto_increment	comment	'自增	id',
		`task_type`	VARCHAR(255)	not	null	comment	'任务类型',
		`task_key`	VARCHAR(255)	not	null	comment	'任务	key',
		`project`	VARCHAR(255)	not	null	comment	'项目名称',
		`task_attributes`	TEXT	comment	'任务属性',
		`update_time`	BIGINT	comment	'更新时间',
		`create_time`	BIGINT	comment	'创建时间',

		`mvcc`	BIGINT	not	null	comment	'mvcc',

		primary	key	(`id`),

		UNIQUE	KEY	(`task_type`,	`task_key`)

)	DEFAULT	CHARSET=utf8;

CREATE	TABLE	IF	NOT	EXISTS	`ke_metadata_query_history_offset`	(
		id	bigint	not	null	auto_increment	comment	'自增	id',
		`project`	VARCHAR(255)	not	null	comment	'项目名称',
		`type`	VARCHAR(255)	not	null	comment	'类别',
		`query_history_id_offset`	BIGINT	comment	'查询历史偏移量',
		`update_time`	BIGINT	comment	'更新时间',
		`create_time`	BIGINT	comment	'创建时间',

		`mvcc`	BIGINT	not	null		comment	'mvcc',

		primary	key	(`id`),

		UNIQUE	KEY	(`project`,	`type`)

)	DEFAULT	CHARSET=utf8;

89

元数据库建表语句

CREATE	TABLE	IF	NOT	EXISTS	ke_metadata_job_info	(
		`id`	bigint(20)	NOT	NULL	AUTO_INCREMENT	comment	'自增	id',
		`job_id`	varchar(100)	NOT	NULL	comment	'任务	id',
		`job_type`	varchar(50)	NOT	NULL	comment	'任务类型',
		`job_status`	varchar(50)	NOT	NULL	comment	'任务状态',
		`project`	varchar(100)	NOT	NULL	comment	'项目名称',
		`subject`	varchar(200)	NOT	NULL	comment	'任务主题',
		`model_id`	varchar(100)	comment	'模型id',
		`priority`	integer	DEFAULT	3		comment	'任务优先级',

		`mvcc`	bigint(10)	comment	'mvcc',
		`job_content`	longblob	NOT	NULL	comment	'任务内容',
		`create_time`	bigint	comment	'创建时间',
		`update_time`	bigint	comment	'更新时间',
		`job_duration_millis`	bigint(10)	NOT	NULL	DEFAULT	'0'	COMMENT	'任务耗时',

		PRIMARY	KEY	(`id`),

		UNIQUE	KEY	uk_job_id	(`job_id`)

)	AUTO_INCREMENT=10000	ENGINE=InnoDB;

create	index	ke_metadata_job_info_ix

				on	ke_metadata_job_info	(project,	job_status,	job_type,	subject)
--从	Kyligence	Enterprise	4.6.21.0	开始，增加索引

create	index	ke_metadata_job_info_project_model_id_ix

				on	ke_metadata_job_info	(project,	model_id);

CREATE	TABLE	IF	NOT	EXISTS	ke_metadata_job_lock	(
		`id`	bigint(20)	NOT	NULL	AUTO_INCREMENT	comment	'自增	id',
		`project`	varchar(100)	NOT	NULL	comment	'项目名称',
		`lock_id`	varchar(100)	NOT	NULL	comment	'锁对象	id',
		`lock_node`	varchar(50)	DEFAULT	NULL	comment	'加锁节点',
		`lock_expire_time`	timestamp	comment	'锁超时时间',
		`priority`	integer	DEFAULT	3	comment	'任务优先级',
		`create_time`	bigint	comment	'创建时间',
		`update_time`	bigint	comment	'更新时间',

		PRIMARY	KEY	(`id`),

		UNIQUE	KEY	uk_lock_id	(`lock_id`)

)	AUTO_INCREMENT=10000	ENGINE=InnoDB;

从	Kyligence	Enterprise	4.5.10.0	到	Kyligence	Enterprise	4.6.16.0，建表语句如下：

CREATE	TABLE	IF	NOT	EXISTS	`ke_metadata`	(
		`META_TABLE_KEY`	varchar(255)	CHARACTER	SET	utf8	COLLATE	utf8_bin	NOT	NULL	comment	'元数据唯一标识',
		`META_TABLE_CONTENT`	longblob	comment	'元数据内容',
		`META_TABLE_TS`	bigint(20)	DEFAULT	NULL	comment	'元数据更新时间',
		`META_TABLE_MVCC`	bigint(20)	DEFAULT	NULL	comment	'元数据当前版本',

		PRIMARY	KEY	(`META_TABLE_KEY`)

)	ENGINE=INNODB;

CREATE	TABLE	IF	NOT	EXISTS	`ke_metadata_audit_log`	(
		`id`	bigint(20)	NOT	NULL	AUTO_INCREMENT	comment	'自增	id',
		`meta_key`	varchar(255)	CHARACTER	SET	utf8	COLLATE	utf8_bin	DEFAULT	NULL	comment	'当前版本	metadata	的主键',
		`meta_content`	longblob	comment	'当前版本	metadata	的内容',
		`meta_ts`	bigint(20)	DEFAULT	NULL	comment	'metadata	更新时间',
		`meta_mvcc`	bigint(20)	DEFAULT	NULL	comment	'metadata	更新时的版本',
		`unit_id`	varchar(50)	DEFAULT	NULL	comment	'更新	metadata	的事务	id',
		`operator`	varchar(100)	DEFAULT	NULL	comment	'更新	metadata	的用户',
		`instance`	varchar(100)	NOT	NULL	comment	'更新	metadata	的节点信息',

		PRIMARY	KEY	(`id`)

)	ENGINE=INNODB;

CREATE	TABLE	IF	NOT	EXISTS	`ke_metadata_session_v2`	(

			`PRIMARY_ID`	CHAR(36)	NOT	NULL,

			`SESSION_ID`	CHAR(180)	NOT	NULL,

			`CREATION_TIME`	BIGINT	NOT	NULL,

			`LAST_ACCESS_TIME`	BIGINT	NOT	NULL,

			`MAX_INACTIVE_INTERVAL`	INT	NOT	NULL,

			`EXPIRY_TIME`	BIGINT	NOT	NULL,

90

元数据库建表语句

			`PRINCIPAL_NAME`	VARCHAR(200),

			CONSTRAINT	`ke_metadata_session_v2_PK`	PRIMARY	KEY	(`PRIMARY_ID`)

)	ENGINE=InnoDB	ROW_FORMAT=DYNAMIC;

CREATE	UNIQUE	INDEX	ke_metadata_id_session_v2_IX1	ON	ke_metadata_session_v2	(SESSION_ID);

CREATE	INDEX	ke_metadata_session_v2_IX2	ON	ke_metadata_session_v2	(EXPIRY_TIME);

CREATE	INDEX	ke_metadata_session_v2_IX3	ON	ke_metadata_session_v2	(PRINCIPAL_NAME);

CREATE	TABLE	IF	NOT	EXISTS	`ke_metadata_session_v2_ATTRIBUTES`	(

			`SESSION_PRIMARY_ID`	CHAR(36)	NOT	NULL,

			`ATTRIBUTE_NAME`	VARCHAR(200)	NOT	NULL,

			`ATTRIBUTE_BYTES`	BLOB	NOT	NULL,

			CONSTRAINT	`ke_metadata_session_v2_ATTRIBUTES_PK`	PRIMARY	KEY	(`SESSION_PRIMARY_ID`,	`ATTRIBUTE_NAME`),

			CONSTRAINT	`ke_metadata_session_v2_ATTRIBUTES_FK`	FOREIGN	KEY	(`SESSION_PRIMARY_ID`)	REFERENCES	`ke_metadata

_session_v2`(`PRIMARY_ID`)	ON	DELETE	CASCADE)	ENGINE=InnoDB	ROW_FORMAT=DYNAMIC;

CREATE	TABLE	IF	NOT	EXISTS	`ke_metadata_query_history`	(

				id	bigint	not	null	auto_increment,

				`query_id`	VARCHAR(50),

				`sql_text`	TEXT,

				`sql_pattern`	TEXT,

				`duration`	BIGINT,

				`total_scan_bytes`	BIGINT,

				`total_scan_count`	BIGINT,

				`result_row_count`	BIGINT,

				`submitter`	VARCHAR(255),

				`realizations`	TEXT,

				`server`	VARCHAR(50),

				`error_type`	VARCHAR(50),

				`engine_type`	VARCHAR(30),

				`cache_hit`	BOOLEAN,

				`query_status`	VARCHAR(20),

				`index_hit`	BOOLEAN,

				`query_time`	BIGINT,

				`month`	VARCHAR(10),

				`query_first_day_of_month`	BIGINT,

				`query_first_day_of_week`	BIGINT,

				`query_day`	BIGINT,

				`is_table_index_used`	BOOLEAN,

				`is_agg_index_used`	BOOLEAN,

				`is_table_snapshot_used`	BOOLEAN,

				`project_name`	VARCHAR(100),

				`reserved_field_1`	VARCHAR(50),

				`reserved_field_2`	VARCHAR(50),

				`reserved_field_3`	longblob,

				`reserved_field_4`	longblob,

				primary	key(`id`,`project_name`)

)	DEFAULT	CHARSET=utf8;

ALTER	table	ke_metadata_query_history	ADD	INDEX	ke_metadata_query_history_ix1(`query_time`);

ALTER	table	ke_metadata_query_history	ADD	INDEX	ke_metadata_query_history_ix2(`query_first_day_of_month`);

ALTER	table	ke_metadata_query_history	ADD	INDEX	ke_metadata_query_history_ix3(`query_first_day_of_week`);

ALTER	table	ke_metadata_query_history	ADD	INDEX	ke_metadata_query_history_ix4(`query_day`);

ALTER	table	ke_metadata_query_history	ADD	INDEX	ke_metadata_query_history_ix5(`duration`);
--从	Kyligence	Enterprise	4.6.1.0	开始，增加下面五个索引

ALTER	table	ke_metadata_query_history	ADD	INDEX	ke_metadata_query_history_ix8(`engine_type`,`project_name`);

ALTER	table	ke_metadata_query_history	ADD	INDEX	ke_metadata_query_history_ix9(`submitter`);

ALTER	table	ke_metadata_query_history	ADD	INDEX	ke_metadata_query_history_ix10(`query_status`);

ALTER	table	ke_metadata_query_history	ADD	INDEX	ke_metadata_query_history_ix11(`server`);

ALTER	table	ke_metadata_query_history	ADD	INDEX	ke_metadata_query_history_ix12(`query_id`);
--从	Kyligence	Enterprise	4.6.23.0	开始，增加下面两个索引

ALTER	table	ke_metadata_query_history	ADD	INDEX	ke_metadata_query_history_ix6(	project_name	);

ALTER	table	ke_metadata_query_history	ADD	INDEX	ke_metadata_query_history_ix7(	project_name,	submitter,	query_t

ime	);

CREATE	TABLE	IF	NOT	EXISTS	`ke_metadata_query_history_realization`	(

		id	bigint	not	null	auto_increment,

		`query_id`	VARCHAR(255)	,

91

元数据库建表语句

		`model`	VARCHAR(255),

		`layout_id`	VARCHAR(255),

		`index_type`	VARCHAR(255),

		`duration`	BIGINT,

		`query_time`	BIGINT,

		`project_name`	VARCHAR(255),

		primary	key	(`id`,`project_name`)

)	DEFAULT	CHARSET=utf8;

ALTER	table	ke_metadata_query_history_realization	ADD	INDEX	ke_metadata_query_history_realization_ix1(`query_ti

me`);

ALTER	table	ke_metadata_query_history_realization	ADD	INDEX	ke_metadata_query_history_realization_ix2(`model`);

CREATE	TABLE	IF	NOT	EXISTS	`ke_metadata_rec_candidate`	(

		`id`	int	not	null	auto_increment,

		`project`	varchar(100),

		`model_id`	varchar(40),

		`unique_flag`	varchar(200),

		`semantic_version`	int,

		`type`	tinyint,

		`rec_entity`	text,

		`depend_ids`	text,

		`layout_metric`	text,

		`cost`	double,

		`total_latency_of_last_day`	double,

		`hit_count`	int,

		`total_time`	double,

		`max_time`	double,

		`min_time`	double,

		`query_history_info`	text,

		`state`	tinyint,

		`create_time`	long,

		`update_time`	long,

		`reserved_field_1`	VARCHAR(50),

		`reserved_field_2`	longblob,

		`reserved_field_3`	longblob,

			primary	key(id)

)	DEFAULT	CHARSET=utf8;

ALTER	TABLE	ke_metadata_rec_candidate	ADD	UNIQUE	%s_idx	(project,	model_id,	unique_flag,	semantic_version);

CREATE	TABLE	IF	NOT	EXISTS	`ke_metadata_epoch`

(

				epoch_id																int(11)										null,

				epoch_target												varchar(255)	NOT	null,

				current_epoch_owner					varchar(2000)				null,

				last_epoch_renew_time			bigint(20)							null,

				server_mode													varchar(10)						null,

				maintenance_mode_reason	varchar(5000)				null,

				mvcc																				bigint(20)							null,

				reserved_field_1								varchar(50)						null,

				reserved_field_2								longblob									null,

				reserved_field_3								longblob									null,

				PRIMARY	KEY	(epoch_target)

)	ENGINE=INNODB	DEFAULT	CHARSET=utf8;

注意：Kyligence	Enterprise	4.5.10.0	前，上述	ke_metadata_session_v2	和	ke_metadata_session_v2_ATTRIBUTES	的
表名应该修改为	ke_metadata_session	和	ke_metadata_session_attributes。对应建表语句如下：

CREATE	TABLE	IF	NOT	EXISTS	`ke_metadata_session`	(

		`SESSION_ID`	varchar(180)	NOT	NULL,

		`CREATION_TIME`	bigint(20)	NOT	NULL,

		`LAST_ACCESS_TIME`	bigint(20)	NOT	NULL,

		`MAX_INACTIVE_INTERVAL`	int(11)	NOT	NULL,

		`PRINCIPAL_NAME`	varchar(200)	DEFAULT	NULL,

		PRIMARY	KEY	(`SESSION_ID`),

		KEY	`KE_METADATA_SESSION_IX1`	(`LAST_ACCESS_TIME`),

92

元数据库建表语句

		KEY	`KE_METADATA_SESSION_IX2`	(`PRINCIPAL_NAME`)

)

CREATE	TABLE	IF	NOT	EXISTS	`ke_metadata_session_ATTRIBUTES`	(

		`SESSION_ID`	varchar(180)	NOT	NULL,

		`ATTRIBUTE_NAME`	varchar(200)	NOT	NULL,

		`ATTRIBUTE_BYTES`	blob	NOT	NULL,

		PRIMARY	KEY	(`SESSION_ID`,`ATTRIBUTE_NAME`),

		KEY	`KE_METADATA_SESSION_ATTRIBUTES_IX1`	(`SESSION_ID`),

		CONSTRAINT	`ke_metadata_session_ATTRIBUTES_FK`	FOREIGN	KEY	(`SESSION_ID`)	REFERENCES	`ke_metadata_sessi

on`	(`SESSION_ID`)	ON	DELETE	CASCADE

)

最小运行权限

如果需要	Kyligence	Enterprise	能够正常使用，至少要授予以上表格如下的权限。假设用户为	 	kylinuser	，

使用	PostgreSQL	作为元数据库

从	Kyligence	Enterprise	4.6.18.0	开始，授权语句为:

GRANT	SELECT	ON	TABLE	public.ke_metadata	TO	kylinuser;

GRANT	INSERT	ON	TABLE	public.ke_metadata	TO	kylinuser;

GRANT	UPDATE	ON	TABLE	public.ke_metadata	TO	kylinuser;

GRANT	DELETE	ON	TABLE	public.ke_metadata	TO	kylinuser;

GRANT	SELECT	ON	TABLE	public.ke_metadata_audit_log	TO	kylinuser;

GRANT	INSERT	ON	TABLE	public.ke_metadata_audit_log	TO	kylinuser;

GRANT	UPDATE	ON	TABLE	public.ke_metadata_audit_log	TO	kylinuser;

GRANT	DELETE	ON	TABLE	public.ke_metadata_audit_log	TO	kylinuser;

GRANT	SELECT	ON	TABLE	public.ke_metadata_session_v2	TO	kylinuser;

GRANT	INSERT	ON	TABLE	public.ke_metadata_session_v2	TO	kylinuser;

GRANT	UPDATE	ON	TABLE	public.ke_metadata_session_v2	TO	kylinuser;

GRANT	DELETE	ON	TABLE	public.ke_metadata_session_v2	TO	kylinuser;

GRANT	SELECT	ON	TABLE	public.ke_metadata_session_v2_attributes	TO	kylinuser;

GRANT	INSERT	ON	TABLE	public.ke_metadata_session_v2_attributes	TO	kylinuser;

GRANT	UPDATE	ON	TABLE	public.ke_metadata_session_v2_attributes	TO	kylinuser;

GRANT	DELETE	ON	TABLE	public.ke_metadata_session_v2_attributes	TO	kylinuser;

GRANT	SELECT	ON	TABLE	public.ke_metadata_query_history	TO	kylinuser;

GRANT	INSERT	ON	TABLE	public.ke_metadata_query_history	TO	kylinuser;

GRANT	UPDATE	ON	TABLE	public.ke_metadata_query_history	TO	kylinuser;

GRANT	DELETE	ON	TABLE	public.ke_metadata_query_history	TO	kylinuser;

GRANT	SELECT	ON	TABLE	public.ke_metadata_query_history_realization	TO	kylinuser;

GRANT	INSERT	ON	TABLE	public.ke_metadata_query_history_realization	TO	kylinuser;

GRANT	UPDATE	ON	TABLE	public.ke_metadata_query_history_realization	TO	kylinuser;

GRANT	DELETE	ON	TABLE	public.ke_metadata_query_history_realization	TO	kylinuser;

GRANT	SELECT	ON	TABLE	public.ke_metadata_rec_candidate_v2	TO	kylinuser;

GRANT	INSERT	ON	TABLE	public.ke_metadata_rec_candidate_v2	TO	kylinuser;

GRANT	UPDATE	ON	TABLE	public.ke_metadata_rec_candidate_v2	TO	kylinuser;

GRANT	DELETE	ON	TABLE	public.ke_metadata_rec_candidate_v2	TO	kylinuser;

GRANT	SELECT	ON	TABLE	public.ke_metadata_epoch	TO	kylinuser;

GRANT	INSERT	ON	TABLE	public.ke_metadata_epoch	TO	kylinuser;

GRANT	UPDATE	ON	TABLE	public.ke_metadata_epoch	TO	kylinuser;

GRANT	DELETE	ON	TABLE	public.ke_metadata_epoch	TO	kylinuser;

GRANT	SELECT	ON	TABLE	public.ke_metadata_favorite_rule	TO	kylinuser;

GRANT	INSERT	ON	TABLE	public.ke_metadata_favorite_rule	TO	kylinuser;

GRANT	UPDATE	ON	TABLE	public.ke_metadata_favorite_rule	TO	kylinuser;

GRANT	DELETE	ON	TABLE	public.ke_metadata_favorite_rule	TO	kylinuser;

93

元数据库建表语句

GRANT	SELECT	ON	TABLE	public.ke_metadata_async_task	TO	kylinuser;

GRANT	INSERT	ON	TABLE	public.ke_metadata_async_task	TO	kylinuser;

GRANT	UPDATE	ON	TABLE	public.ke_metadata_async_task	TO	kylinuser;

GRANT	DELETE	ON	TABLE	public.ke_metadata_async_task	TO	kylinuser;

GRANT	SELECT	ON	TABLE	public.ke_metadata_query_history_offset	TO	kylinuser;

GRANT	INSERT	ON	TABLE	public.ke_metadata_query_history_offset	TO	kylinuser;

GRANT	UPDATE	ON	TABLE	public.ke_metadata_query_history_offset	TO	kylinuser;

GRANT	DELETE	ON	TABLE	public.ke_metadata_query_history_offset	TO	kylinuser;

GRANT	SELECT	ON	TABLE	public.ke_metadata_job_info	TO	kylinuser;

GRANT	INSERT	ON	TABLE	public.ke_metadata_job_info	TO	kylinuser;

GRANT	UPDATE	ON	TABLE	public.ke_metadata_job_info	TO	kylinuser;

GRANT	DELETE	ON	TABLE	public.ke_metadata_job_info	TO	kylinuser;

GRANT	SELECT	ON	TABLE	public.ke_metadata_job_lock	TO	kylinuser;

GRANT	INSERT	ON	TABLE	public.ke_metadata_job_lock	TO	kylinuser;

GRANT	UPDATE	ON	TABLE	public.ke_metadata_job_lock	TO	kylinuser;

GRANT	DELETE	ON	TABLE	public.ke_metadata_job_lock	TO	kylinuser;

GRANT	SELECT	ON	SEQUENCE	public.ke_metadata_audit_log_id_seq	TO	kylinuser;

GRANT	UPDATE	ON	SEQUENCE	public.ke_metadata_audit_log_id_seq	TO	kylinuser;

GRANT	SELECT	ON	SEQUENCE	public.ke_metadata_query_history_id_seq	TO	kylinuser;

GRANT	UPDATE	ON	SEQUENCE	public.ke_metadata_query_history_id_seq	TO	kylinuser;

GRANT	SELECT	ON	SEQUENCE	public.ke_metadata_query_history_realization_id_seq	TO	kylinuser;

GRANT	UPDATE	ON	SEQUENCE	public.ke_metadata_query_history_realization_id_seq	TO	kylinuser;

GRANT	SELECT	ON	SEQUENCE	public.ke_metadata_rec_candidate_v2_id_seq	TO	kylinuser;

GRANT	UPDATE	ON	SEQUENCE	public.ke_metadata_rec_candidate_v2_id_seq	TO	kylinuser;

GRANT	SELECT	ON	SEQUENCE	public.ke_metadata_favorite_rule_id_seq	TO	kylinuser;

GRANT	UPDATE	ON	SEQUENCE	public.ke_metadata_favorite_rule_id_seq	TO	kylinuser;

GRANT	SELECT	ON	SEQUENCE	public.ke_metadata_async_task_id_seq	TO	kylinuser;

GRANT	UPDATE	ON	SEQUENCE	public.ke_metadata_async_task_id_seq	TO	kylinuser;

GRANT	SELECT	ON	SEQUENCE	public.ke_metadata_query_history_offset_id_seq	TO	kylinuser;

GRANT	UPDATE	ON	SEQUENCE	public.ke_metadata_query_history_offset_id_seq	TO	kylinuser;

GRANT	SELECT	ON	SEQUENCE	public.ke_metadata_job_info_id_seq	TO	kylinuser;

GRANT	UPDATE	ON	SEQUENCE	public.ke_metadata_job_info_id_seq	TO	kylinuser;

GRANT	SELECT	ON	SEQUENCE	public.ke_metadata_job_lock_id_seq	TO	kylinuser;

GRANT	UPDATE	ON	SEQUENCE	public.ke_metadata_job_lock_id_seq	TO	kylinuser;

从	Kyligence	Enterprise	4.5.10.0	到	Kyligence	Enterprise	4.6.16.0，授权语句为:

GRANT	SELECT	ON	TABLE	public.ke_metadata	TO	kylinuser;

GRANT	INSERT	ON	TABLE	public.ke_metadata	TO	kylinuser;

GRANT	UPDATE	ON	TABLE	public.ke_metadata	TO	kylinuser;

GRANT	DELETE	ON	TABLE	public.ke_metadata	TO	kylinuser;

GRANT	SELECT	ON	TABLE	public.ke_metadata_audit_log	TO	kylinuser;

GRANT	INSERT	ON	TABLE	public.ke_metadata_audit_log	TO	kylinuser;

GRANT	UPDATE	ON	TABLE	public.ke_metadata_audit_log	TO	kylinuser;

GRANT	DELETE	ON	TABLE	public.ke_metadata_audit_log	TO	kylinuser;

GRANT	SELECT	ON	TABLE	public.ke_metadata_session_v2	TO	kylinuser;

GRANT	INSERT	ON	TABLE	public.ke_metadata_session_v2	TO	kylinuser;

GRANT	UPDATE	ON	TABLE	public.ke_metadata_session_v2	TO	kylinuser;

GRANT	DELETE	ON	TABLE	public.ke_metadata_session_v2	TO	kylinuser;

GRANT	SELECT	ON	TABLE	public.ke_metadata_session_v2_attributes	TO	kylinuser;

GRANT	INSERT	ON	TABLE	public.ke_metadata_session_v2_attributes	TO	kylinuser;

94

元数据库建表语句

GRANT	UPDATE	ON	TABLE	public.ke_metadata_session_v2_attributes	TO	kylinuser;

GRANT	DELETE	ON	TABLE	public.ke_metadata_session_v2_attributes	TO	kylinuser;

GRANT	SELECT	ON	TABLE	public.ke_metadata_query_history	TO	kylinuser;

GRANT	INSERT	ON	TABLE	public.ke_metadata_query_history	TO	kylinuser;

GRANT	UPDATE	ON	TABLE	public.ke_metadata_query_history	TO	kylinuser;

GRANT	DELETE	ON	TABLE	public.ke_metadata_query_history	TO	kylinuser;

GRANT	SELECT	ON	TABLE	public.ke_metadata_query_history_realization	TO	kylinuser;

GRANT	INSERT	ON	TABLE	public.ke_metadata_query_history_realization	TO	kylinuser;

GRANT	UPDATE	ON	TABLE	public.ke_metadata_query_history_realization	TO	kylinuser;

GRANT	DELETE	ON	TABLE	public.ke_metadata_query_history_realization	TO	kylinuser;

GRANT	SELECT	ON	TABLE	public.ke_metadata_rec_candidate	TO	kylinuser;

GRANT	INSERT	ON	TABLE	public.ke_metadata_rec_candidate	TO	kylinuser;

GRANT	UPDATE	ON	TABLE	public.ke_metadata_rec_candidate	TO	kylinuser;

GRANT	DELETE	ON	TABLE	public.ke_metadata_rec_candidate	TO	kylinuser;

GRANT	SELECT	ON	TABLE	public.ke_metadata_epoch	TO	kylinuser;

GRANT	INSERT	ON	TABLE	public.ke_metadata_epoch	TO	kylinuser;

GRANT	UPDATE	ON	TABLE	public.ke_metadata_epoch	TO	kylinuser;

GRANT	DELETE	ON	TABLE	public.ke_metadata_epoch	TO	kylinuser;

GRANT	SELECT	ON	SEQUENCE	public.ke_metadata_audit_log_id_seq	TO	kylinuser;

GRANT	UPDATE	ON	SEQUENCE	public.ke_metadata_audit_log_id_seq	TO	kylinuser;

GRANT	SELECT	ON	SEQUENCE	public.ke_metadata_query_history_id_seq	TO	kylinuser;

GRANT	UPDATE	ON	SEQUENCE	public.ke_metadata_query_history_id_seq	TO	kylinuser;

GRANT	SELECT	ON	SEQUENCE	public.ke_metadata_query_history_realization_id_seq	TO	kylinuser;

GRANT	UPDATE	ON	SEQUENCE	public.ke_metadata_query_history_realization_id_seq	TO	kylinuser;

GRANT	SELECT	ON	SEQUENCE	public.ke_metadata_rec_candidate_id_seq	TO	kylinuser;

GRANT	UPDATE	ON	SEQUENCE	public.ke_metadata_rec_candidate_id_seq	TO	kylinuser;

注意：Kyligence	Enterprise	4.5.10.0	前，授权语句为：

GRANT	SELECT	ON	TABLE	public.ke_metadata	TO	kylinuser;

GRANT	INSERT	ON	TABLE	public.ke_metadata	TO	kylinuser;

GRANT	UPDATE	ON	TABLE	public.ke_metadata	TO	kylinuser;

GRANT	DELETE	ON	TABLE	public.ke_metadata	TO	kylinuser;

GRANT	SELECT	ON	TABLE	public.ke_metadata_audit_log	TO	kylinuser;

GRANT	INSERT	ON	TABLE	public.ke_metadata_audit_log	TO	kylinuser;

GRANT	UPDATE	ON	TABLE	public.ke_metadata_audit_log	TO	kylinuser;

GRANT	DELETE	ON	TABLE	public.ke_metadata_audit_log	TO	kylinuser;

GRANT	SELECT	ON	TABLE	public.ke_metadata_session	TO	kylinuser;

GRANT	INSERT	ON	TABLE	public.ke_metadata_session	TO	kylinuser;

GRANT	UPDATE	ON	TABLE	public.ke_metadata_session	TO	kylinuser;

GRANT	DELETE	ON	TABLE	public.ke_metadata_session	TO	kylinuser;

GRANT	SELECT	ON	TABLE	public.ke_metadata_session_attributes	TO	kylinuser;

GRANT	INSERT	ON	TABLE	public.ke_metadata_session_attributes	TO	kylinuser;

GRANT	UPDATE	ON	TABLE	public.ke_metadata_session_attributes	TO	kylinuser;

GRANT	DELETE	ON	TABLE	public.ke_metadata_session_attributes	TO	kylinuser;

GRANT	SELECT	ON	TABLE	public.ke_metadata_query_history	TO	kylinuser;

GRANT	INSERT	ON	TABLE	public.ke_metadata_query_history	TO	kylinuser;

GRANT	UPDATE	ON	TABLE	public.ke_metadata_query_history	TO	kylinuser;

GRANT	DELETE	ON	TABLE	public.ke_metadata_query_history	TO	kylinuser;

GRANT	SELECT	ON	TABLE	public.ke_metadata_query_history_realization	TO	kylinuser;

GRANT	INSERT	ON	TABLE	public.ke_metadata_query_history_realization	TO	kylinuser;

GRANT	UPDATE	ON	TABLE	public.ke_metadata_query_history_realization	TO	kylinuser;

GRANT	DELETE	ON	TABLE	public.ke_metadata_query_history_realization	TO	kylinuser;

95

元数据库建表语句

GRANT	SELECT	ON	TABLE	public.ke_metadata_rec_candidate	TO	kylinuser;

GRANT	INSERT	ON	TABLE	public.ke_metadata_rec_candidate	TO	kylinuser;

GRANT	UPDATE	ON	TABLE	public.ke_metadata_rec_candidate	TO	kylinuser;

GRANT	DELETE	ON	TABLE	public.ke_metadata_rec_candidate	TO	kylinuser;

GRANT	SELECT	ON	TABLE	public.ke_metadata_epoch	TO	kylinuser;

GRANT	INSERT	ON	TABLE	public.ke_metadata_epoch	TO	kylinuser;

GRANT	UPDATE	ON	TABLE	public.ke_metadata_epoch	TO	kylinuser;

GRANT	DELETE	ON	TABLE	public.ke_metadata_epoch	TO	kylinuser;

GRANT	SELECT	ON	SEQUENCE	public.ke_metadata_audit_log_id_seq	TO	kylinuser;

GRANT	UPDATE	ON	SEQUENCE	public.ke_metadata_audit_log_id_seq	TO	kylinuser;

GRANT	SELECT	ON	SEQUENCE	public.ke_metadata_query_history_id_seq	TO	kylinuser;

GRANT	UPDATE	ON	SEQUENCE	public.ke_metadata_query_history_id_seq	TO	kylinuser;

GRANT	SELECT	ON	SEQUENCE	public.ke_metadata_query_history_realization_id_seq	TO	kylinuser;

GRANT	UPDATE	ON	SEQUENCE	public.ke_metadata_query_history_realization_id_seq	TO	kylinuser;

GRANT	SELECT	ON	SEQUENCE	public.ke_metadata_rec_candidate_id_seq	TO	kylinuser;

GRANT	UPDATE	ON	SEQUENCE	public.ke_metadata_rec_candidate_id_seq	TO	kylinuser;

使用	MySQL	作为元数据库

从	Kyligence	Enterprise	4.6.18.0	开始，授权语句为:

GRANT	Delete	ON	kylin.ke_metadata	TO	'kylinuser'@'%';

GRANT	Insert	ON	kylin.ke_metadata	TO	'kylinuser'@'%';

GRANT	Select	ON	kylin.ke_metadata	TO	'kylinuser'@'%';

GRANT	Update	ON	kylin.ke_metadata	TO	'kylinuser'@'%';

GRANT	Delete	ON	kylin.ke_metadata_audit_log	TO	'kylinuser'@'%';

GRANT	Insert	ON	kylin.ke_metadata_audit_log	TO	'kylinuser'@'%';

GRANT	Select	ON	kylin.ke_metadata_audit_log	TO	'kylinuser'@'%';

GRANT	Update	ON	kylin.ke_metadata_audit_log	TO	'kylinuser'@'%';

GRANT	Delete	ON	kylin.ke_metadata_session_v2	TO	'kylinuser'@'%';

GRANT	Insert	ON	kylin.ke_metadata_session_v2	TO	'kylinuser'@'%';

GRANT	Select	ON	kylin.ke_metadata_session_v2	TO	'kylinuser'@'%';

GRANT	Update	ON	kylin.ke_metadata_session_v2	TO	'kylinuser'@'%';

GRANT	Delete	ON	kylin.ke_metadata_session_v2_ATTRIBUTES	TO	'kylinuser'@'%';

GRANT	Insert	ON	kylin.ke_metadata_session_v2_ATTRIBUTES	TO	'kylinuser'@'%';

GRANT	Select	ON	kylin.ke_metadata_session_v2_ATTRIBUTES	TO	'kylinuser'@'%';

GRANT	Update	ON	kylin.ke_metadata_session_v2_ATTRIBUTES	TO	'kylinuser'@'%';

GRANT	Delete	ON	kylin.ke_metadata_query_history	TO	'kylinuser'@'%';

GRANT	Insert	ON	kylin.ke_metadata_query_history	TO	'kylinuser'@'%';

GRANT	Select	ON	kylin.ke_metadata_query_history	TO	'kylinuser'@'%';

GRANT	Update	ON	kylin.ke_metadata_query_history	TO	'kylinuser'@'%';

GRANT	Delete	ON	kylin.ke_metadata_query_history_realization	TO	'kylinuser'@'%';

GRANT	Insert	ON	kylin.ke_metadata_query_history_realization	TO	'kylinuser'@'%';

GRANT	Select	ON	kylin.ke_metadata_query_history_realization	TO	'kylinuser'@'%';

GRANT	Update	ON	kylin.ke_metadata_query_history_realization	TO	'kylinuser'@'%';

GRANT	Delete	ON	kylin.ke_metadata_rec_candidate_v2	TO	'kylinuser'@'%';

GRANT	Insert	ON	kylin.ke_metadata_rec_candidate_v2	TO	'kylinuser'@'%';

GRANT	Select	ON	kylin.ke_metadata_rec_candidate_v2	TO	'kylinuser'@'%';

GRANT	Update	ON	kylin.ke_metadata_rec_candidate_v2	TO	'kylinuser'@'%';

GRANT	Delete	ON	kylin.ke_metadata_epoch	TO	'kylinuser'@'%';

GRANT	Insert	ON	kylin.ke_metadata_epoch	TO	'kylinuser'@'%';

GRANT	Select	ON	kylin.ke_metadata_epoch	TO	'kylinuser'@'%';

GRANT	Update	ON	kylin.ke_metadata_epoch	TO	'kylinuser'@'%';

GRANT	Delete	ON	kylin.ke_metadata_favorite_rule	TO	'kylinuser'@'%';

96

元数据库建表语句

GRANT	Insert	ON	kylin.ke_metadata_favorite_rule	TO	'kylinuser'@'%';

GRANT	Select	ON	kylin.ke_metadata_favorite_rule	TO	'kylinuser'@'%';

GRANT	Update	ON	kylin.ke_metadata_favorite_rule	TO	'kylinuser'@'%';

GRANT	Delete	ON	kylin.ke_metadata_async_task	TO	'kylinuser'@'%';

GRANT	Insert	ON	kylin.ke_metadata_async_task	TO	'kylinuser'@'%';

GRANT	Select	ON	kylin.ke_metadata_async_task	TO	'kylinuser'@'%';

GRANT	Update	ON	kylin.ke_metadata_async_task	TO	'kylinuser'@'%';

GRANT	Delete	ON	kylin.ke_metadata_query_history_offset	TO	'kylinuser'@'%';

GRANT	Insert	ON	kylin.ke_metadata_query_history_offset	TO	'kylinuser'@'%';

GRANT	Select	ON	kylin.ke_metadata_query_history_offset	TO	'kylinuser'@'%';

GRANT	Update	ON	kylin.ke_metadata_query_history_offset	TO	'kylinuser'@'%';

GRANT	Delete	ON	kylin.ke_metadata_job_info	TO	'kylinuser'@'%';

GRANT	Insert	ON	kylin.ke_metadata_job_info	TO	'kylinuser'@'%';

GRANT	Select	ON	kylin.ke_metadata_job_info	TO	'kylinuser'@'%';

GRANT	Update	ON	kylin.ke_metadata_job_info	TO	'kylinuser'@'%';

GRANT	Delete	ON	kylin.ke_metadata_job_lock	TO	'kylinuser'@'%';

GRANT	Insert	ON	kylin.ke_metadata_job_lock	TO	'kylinuser'@'%';

GRANT	Select	ON	kylin.ke_metadata_job_lock	TO	'kylinuser'@'%';

GRANT	Update	ON	kylin.ke_metadata_job_lock	TO	'kylinuser'@'%';

从	Kyligence	Enterprise	4.5.10.0	到	Kyligence	Enterprise	4.6.16.0，授权语句为:

GRANT	Delete	ON	kylin.ke_metadata	TO	'kylinuser'@'%';

GRANT	Insert	ON	kylin.ke_metadata	TO	'kylinuser'@'%';

GRANT	Select	ON	kylin.ke_metadata	TO	'kylinuser'@'%';

GRANT	Update	ON	kylin.ke_metadata	TO	'kylinuser'@'%';

GRANT	Delete	ON	kylin.ke_metadata_audit_log	TO	'kylinuser'@'%';

GRANT	Insert	ON	kylin.ke_metadata_audit_log	TO	'kylinuser'@'%';

GRANT	Select	ON	kylin.ke_metadata_audit_log	TO	'kylinuser'@'%';

GRANT	Update	ON	kylin.ke_metadata_audit_log	TO	'kylinuser'@'%';

GRANT	Delete	ON	kylin.ke_metadata_session_v2	TO	'kylinuser'@'%';

GRANT	Insert	ON	kylin.ke_metadata_session_v2	TO	'kylinuser'@'%';

GRANT	Select	ON	kylin.ke_metadata_session_v2	TO	'kylinuser'@'%';

GRANT	Update	ON	kylin.ke_metadata_session_v2	TO	'kylinuser'@'%';

GRANT	Delete	ON	kylin.ke_metadata_session_v2_ATTRIBUTES	TO	'kylinuser'@'%';

GRANT	Insert	ON	kylin.ke_metadata_session_v2_ATTRIBUTES	TO	'kylinuser'@'%';

GRANT	Select	ON	kylin.ke_metadata_session_v2_ATTRIBUTES	TO	'kylinuser'@'%';

GRANT	Update	ON	kylin.ke_metadata_session_v2_ATTRIBUTES	TO	'kylinuser'@'%';

GRANT	Delete	ON	kylin.ke_metadata_query_history	TO	'kylinuser'@'%';

GRANT	Insert	ON	kylin.ke_metadata_query_history	TO	'kylinuser'@'%';

GRANT	Select	ON	kylin.ke_metadata_query_history	TO	'kylinuser'@'%';

GRANT	Update	ON	kylin.ke_metadata_query_history	TO	'kylinuser'@'%';

GRANT	Delete	ON	kylin.ke_metadata_query_history_realization	TO	'kylinuser'@'%';

GRANT	Insert	ON	kylin.ke_metadata_query_history_realization	TO	'kylinuser'@'%';

GRANT	Select	ON	kylin.ke_metadata_query_history_realization	TO	'kylinuser'@'%';

GRANT	Update	ON	kylin.ke_metadata_query_history_realization	TO	'kylinuser'@'%';

GRANT	Delete	ON	kylin.ke_metadata_rec_candidate	TO	'kylinuser'@'%';

GRANT	Insert	ON	kylin.ke_metadata_rec_candidate	TO	'kylinuser'@'%';

GRANT	Select	ON	kylin.ke_metadata_rec_candidate	TO	'kylinuser'@'%';

GRANT	Update	ON	kylin.ke_metadata_rec_candidate	TO	'kylinuser'@'%';

GRANT	Delete	ON	kylin.ke_metadata_epoch	TO	'kylinuser'@'%';

GRANT	Insert	ON	kylin.ke_metadata_epoch	TO	'kylinuser'@'%';

GRANT	Select	ON	kylin.ke_metadata_epoch	TO	'kylinuser'@'%';

GRANT	Update	ON	kylin.ke_metadata_epoch	TO	'kylinuser'@'%';

97

元数据库建表语句

注意	：Kyligence	Enterprise	4.5.10.0	前，授权语句为：

GRANT	Delete	ON	kylin.ke_metadata	TO	'kylinuser'@'%';

GRANT	Insert	ON	kylin.ke_metadata	TO	'kylinuser'@'%';

GRANT	Select	ON	kylin.ke_metadata	TO	'kylinuser'@'%';

GRANT	Update	ON	kylin.ke_metadata	TO	'kylinuser'@'%';

GRANT	Delete	ON	kylin.ke_metadata_audit_log	TO	'kylinuser'@'%';

GRANT	Insert	ON	kylin.ke_metadata_audit_log	TO	'kylinuser'@'%';

GRANT	Select	ON	kylin.ke_metadata_audit_log	TO	'kylinuser'@'%';

GRANT	Update	ON	kylin.ke_metadata_audit_log	TO	'kylinuser'@'%';

GRANT	Delete	ON	kylin.ke_metadata_session	TO	'kylinuser'@'%';

GRANT	Insert	ON	kylin.ke_metadata_session	TO	'kylinuser'@'%';

GRANT	Select	ON	kylin.ke_metadata_session	TO	'kylinuser'@'%';

GRANT	Update	ON	kylin.ke_metadata_session	TO	'kylinuser'@'%';

GRANT	Delete	ON	kylin.ke_metadata_session_ATTRIBUTES	TO	'kylinuser'@'%';

GRANT	Insert	ON	kylin.ke_metadata_session_ATTRIBUTES	TO	'kylinuser'@'%';

GRANT	Select	ON	kylin.ke_metadata_session_ATTRIBUTES	TO	'kylinuser'@'%';

GRANT	Update	ON	kylin.ke_metadata_session_ATTRIBUTES	TO	'kylinuser'@'%';

GRANT	Delete	ON	kylin.ke_metadata_query_history	TO	'kylinuser'@'%';

GRANT	Insert	ON	kylin.ke_metadata_query_history	TO	'kylinuser'@'%';

GRANT	Select	ON	kylin.ke_metadata_query_history	TO	'kylinuser'@'%';

GRANT	Update	ON	kylin.ke_metadata_query_history	TO	'kylinuser'@'%';

GRANT	Delete	ON	kylin.ke_metadata_query_history_realization	TO	'kylinuser'@'%';

GRANT	Insert	ON	kylin.ke_metadata_query_history_realization	TO	'kylinuser'@'%';

GRANT	Select	ON	kylin.ke_metadata_query_history_realization	TO	'kylinuser'@'%';

GRANT	Update	ON	kylin.ke_metadata_query_history_realization	TO	'kylinuser'@'%';

GRANT	Delete	ON	kylin.ke_metadata_rec_candidate	TO	'kylinuser'@'%';

GRANT	Insert	ON	kylin.ke_metadata_rec_candidate	TO	'kylinuser'@'%';

GRANT	Select	ON	kylin.ke_metadata_rec_candidate	TO	'kylinuser'@'%';

GRANT	Update	ON	kylin.ke_metadata_rec_candidate	TO	'kylinuser'@'%';

GRANT	Delete	ON	kylin.ke_metadata_epoch	TO	'kylinuser'@'%';

GRANT	Insert	ON	kylin.ke_metadata_epoch	TO	'kylinuser'@'%';

GRANT	Select	ON	kylin.ke_metadata_epoch	TO	'kylinuser'@'%';

GRANT	Update	ON	kylin.ke_metadata_epoch	TO	'kylinuser'@'%';

建表权限

如果使用	Kyligence	Enterprise	自动建表，请注意从以下版本升级时，有元数据表变更，请确保用户有建表和建索引的权
限：

跨	4.5.10.0	版本升级，如从	4.5.10.0	之前升级到	4.5.10.0	及之后版本；
跨	4.6.18.0	版本升级，如从	4.6.18.0	之前升级到	4.6.18.0	及之后版本；
跨	4.6.23.0	版本升级，如从	4.6.23.0	之前升级到	4.6.23.0	及之后版本；

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:03

98

查询历史字段表

查询历史字段表

从	Kyligence	Enterprise	4.1.0	开始，系统使用	RDBMS	存储查询历史。每一份元数据都会储存两张查询历史相关的表：

query_history	表：每一条查询的信息
query_history_realization	表：查询击中的每个索引信息

query_history	表

字段名称

描述

id

cache_hit

duration

engine_type

error_type

server

index_hit

自增主键

查询是否击中缓存

执行查询的时长

四种查询对象，蓝色名称表示查询击中模型（索引组），RDBMS	表示查询下压至关
系型数据库，HIVE	表示查询下压至	Hive，CONSTANTS	表示查询常量，空白表示查
询失败

查询异常时的异常信息

提交查询的主机地址，如果主机地址不存在，则显示IP地址

查询是否击中索引

is_agg_index_used

查询是否击中维度聚合索引

is_table_index_used

查询是否击中表明细索引

is_table_snapshot_used

查询是否击中维度表

month

提交查询的月份，按月统计查询历史时需要用到该字段

query_first_day_of_month

查询时间本月的初始时间，按月统计查询历史时需要用到该字段

query_first_day_of_week

查询时间本周的初始时间，按周统计查询历史时需要用到该字段

query_day

query_id

query_status

query_time

realizations

查询时间当天的初始时间，按天统计查询历史时需要用到该字段

查询的	ID	号

两种查询状态，SUCCEEDED	表示查询成功，FAILED	表示查询出现异常

查询开始时间

由模型	ID	号、Layout	ID	号和索引类型拼接成的字符串，格式为
modelId#layoutId#indexType

result_row_count

查询结果行数

sql_text

sql_pattern

submitter

查询的	SQL	语句

查询的	SQL	语句的	sql	pattern，SQL	加速时需要用到该字段。

提交查询的	Kyligence	Enterprise	用户

total_scan_bytes

查询总共扫描字节数

total_scan_count

查询总共扫描行数

project_name

项目名称

reserved_field_1

保留字段,目前暂未使用

reserved_field_2

保留字段,目前暂未使用

99

查询历史字段表

reserved_field_2

保留字段,目前暂未使用

reserved_field_3

从	4.2	开始，该字段用于记录无法智能推荐索引的原因

reserved_field_4

保留字段,目前暂未使用

query_history_realization	表

字段名称

描述

query_time

查询开始时间，格式为	unix	时间戳

duration

查询耗时

index_type

三种索引类型，Table	Index	表示表明细索引，Agg	Index	表示聚合索引，Table	Snapshot	表示维度
表

layout_id

Layout	ID	号

model

模型的	ID	号

query_id

查询的	ID	号

project_name

项目名称

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:03

100

部署模式

部署模式

本章介绍了几种	Kyligence	Enterprise	目前支持的部署模式，以实现高性能、高稳定性和高可用。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

101

集群部署

集群部署

Kyligence	Enterprise	所有的状态信息都存储在RDBMS元数据库中（如PostgreSQL/MySQL）中。您可以启用多个
Kyligence	Enterprise	节点以部署负载均衡集群，使各个节点分担查询压力且互为备份，从而提高服务的可用性。其部署
架构如图所示：

部署架构

上图中，需要用户安装部署的组件分别是：

RDBMS	元数据库（PostgreSQL/MySQL）
时序数据库	(InfluxDB)
Kyligence	节点

Load	Balancer

以下会分别对这些组件进行说明

元数据库和时序数据库的说明

Kyligence	Enterprise	使用	RDBMS	数据库存储元数据，请参考配置RDBMS元数据库。

Kyligence	Enterprise	使用时序数据库存储	Metrics	信息（主要供监控使用），请参考配置时序数据库InfluxDB。

Kyligence	Enterprise	节点说明

目前本产品支持多节点的部署方式。查询会被分布到各个节点，任务也可以被所有类型的节点提交，但所有构建任务都

会被提交到任务节点，并且只有任务节点能执行构建任务。

查询节点：查询节点可以做查询，也可以提交构建任务，但是不能执行构建任务。

任务节点：任务节点可以执行构建任务以及元数据更新操作，但是不能执行查询任务。

	all		节点： 	all		节点能承担查询节点及任务节点所有能力。

102

集群部署

Kyligence	Enterprise	节点配置

如果您需要将多个	Kyligence	Enterprise	节点组成集群，请参考	Kyligence	Manager	产品手册中的Kyligence	Enterprise	服务
及实例管理搭建集群。

注意：

请尽量保证	Kyligence	节点部署在同一	Hadoop	集群。如您需要配置读写分离，请您参考读写分离章节。
系统第一次启动时，如果同时启动多个	 	all		节点，系统管理员	 	ADMIN		默认生成的随机密码，只会打印在一个节
点的控制台。如果	 	ADMIN		密码不慎遗失，也可以参考	ADMIN	用户重置密码	重置密码。

Kyligence	Enterprise	负载均衡

Kyligence	Enterprise	集群可以使用负载均衡服务，请参考	Kyligence	Manager	产品手册中的Gateway	服务及实例管理安装
负载均衡服务。

Kyligence	Enterprise	任务引擎多活

Kyligence	Enterprise	任务节点负责调度和执行构建任务，以及进行元数据请求操作。通常由用户所指定的集群中的一个
或多个节点担当此角色。

在	Kyligence	Enterprise	4.2.0	及之后的版本中，支持多个任务节点以"多活"模式工作，即每个处于健康状态的任务节点都
有执行构建任务的能力。如果某个充当任务引擎的实例发生故障退出，集群中的其他的任务引擎节点会接管发生故障节

点上面运行的任务并继续运行。

需要说明的是，由于项目锁的存在，任务分配到节点时，项目是分配最小单位，即一个项目中所有的构建任务都只能在

一个任务节点执行。不同的项目及对应的构建任务可以在不同的任务节点执行。

如果您需要开启该功能，则在多个	Kyligence	Enterprise	节点的	 	$KYLIN_HOME/conf/kylin.properties		配置文件中配置
	kylin.server.mode=all		或者	 	kylin.server.mode=job		。

需在所有	Kyligence	Enterprise	节点配置如下参数，且所有节点配置相同：

kylin.server.leader-race.heart-beat-timeout=60

kylin.server.leader-race.heart-beat-interval=30

kylin.job.ssh-username=username

kylin.job.ssh-password=password

	kylin.server.leader-race.heart-beat-timeout	代表心跳检测的超时时间，默认值	60	秒。当一个任务节点超过	60	秒没有
发出心跳，则代表该节点不可用，该节点持有的项目就会被别的节点抢占。	 	kylin.server.leader-race.heart-beat-
interval	代表发起心跳的时间间隔，默认值	30	秒，代表每个任务节点每隔	30	秒发送一次心跳。	 	kylin.job.ssh-
username		代表	Kyligence	各节点之间的	ssh	登陆用户名，如果已配置免密登陆可以不填该参数。	 	kylin.job.ssh-
password		代表	Kyligence	各节点之间的	ssh	登陆密码，如果已配置免密登陆可以不填写该参数。

加密	kylin.job.ssh-password

如果需要对	kylin.job.ssh-password	进行加密，可以使用如下方式：

i.在 	${KYLIN_HOME}	路径下执行以下命令，获取加密后的密码

./bin/kylin.sh	io.kyligence.kap.tool.general.CryptTool	-e	AES	-s	<password>

ii.配置	kylin.job.ssh-password	为如下形式

kylin.job.ssh-password=ENC('${encrypted_password}')

103

集群部署

已知问题

1.	 一定要开启	Session	共享，否则会导致请求转发不可用。方法为在各个节点的 	$KYLIN_HOME/conf/kylin.properties

中配置	 	spring.session.store-type=jdbc	。

2.	 在多台机器中部署	Kyligence	Enterprise	时，一定要确保节点间没有时差，可以通过	ntp	来同步集群中的节点时间。
3.	 在某个	Kyligence	Enterprise	任务节点突然故障时，可能会导致被该节点持有的项目无法发出元数据的修改请求，需
要等待别的任务节点接管相应的项目后才可以继续发出请求。相应的提示为： 	系统正在尝试恢复服务，请稍候进行尝试	。

4.	 当所有的	Kyligence	Enterprise	任务节点都出现故障时，在	 	query		节点中无法发出元数据的修改请求，相应的提示

为： 	系统中暂无活跃的任务节点，请联系系统管理员进行检查并修复	。

5.	 当前需要各个节点之间配置免密登陆，或者保证各节点之间的	ssh	登陆信息是一致的。

注意：

任务引擎多活特性默认为开启状态，但在仅有一个	 	all		或者	 	job		节点的情况下，考虑到性能问题，建议您关闭
单节点下多活的特性。您可通过在任务节点的 	$KYLIN_HOME/conf/kylin.properties		中配置	 	kylin.server.leader-
race.enabled=false	，关闭该功能

如果想从关闭多活特性转为开启状态，除了将上述开关注释或者修改为	 	true		还需要通过调用	Rest	API	更新对应
信息，具体请参阅项目设置	API。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

104

服务发现

服务发现

Kyligence	Enterprise	从	2.0	版本开始支持服务发现，即在多个	Kyligence	Enterprise	实例组成的集群中，当一个	Kyligence
Enterprise	实例启动、停止或意外中断通讯时，集群中的其他实例能够自动发现并更新状态。在	Kyligence	Enterprise	版
本中新增了基于	Apache	Curator	框架的服务发现功能，相较于之前的版本更为稳定易用。

如果您想要使用服务发现，那么您应当在	 	$KYLIN_HOME/conf/kylin.properties		文件中配置	ZooKeeper	的地址，例如：

kylin.env.zookeeper-connect-string=host1:2181,host2:2181,host3:2181

配置完成后，请重新启动	Kyligence	Enterprise。在重新启动时，每个	Kyligence	Enterprise	实例会在	ZooKeeper	上进行注
册，从而使得集群中的任何一个	Kyligence	Enterprise	实例都能够通过	ZooKeeper	发现其他的实例。

Kyligence	Enterprise	在	ZooKeeper	上进行注册时，默认使用	hostname	作为节点名，如果您运行	Kyligence	Enterprise	的集
群无法通过	DNS	等服务自动将主机名解析为对应的	IP	地址，您需要在启动	Kyligence	Enterprise	前
	$KYLIN_HOME/conf/kylin.properties		添加以下配置，以避免	Kyligence	Enterprise	实例之间通信错误，例如：

spring.cloud.zookeeper.discovery.instance-host=10.1.2.3

该配置强制	Kyligence	进程在服务注册的时候使用所配置的具体	IP	地址，确保其他实例能够直接通过该	IP	地址发现
它。如果遇到需要该配置项的情况，建议在每个实例的 	kylin.properties		文件中添加该值。

注意：上述举例的	IP	地址需要替换为当前	Kyligence	实例所在节点的	IP	地址。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

105

读写分离部署

读写分离部署

Kyligence	Enterprise	基于	Hadoop	进行的任务主要被分为构建和查询两种，如果这两种任务使用的是同一套Hadoop	资
源，那构建和查询之间可能会发生资源抢占，导致其不够稳定快速。

Kyligence	Enterprise	允许用户构建和查询使用不同的	Hadoop	集群，前者中存在很多写操作，称为构建集群，而后者中
则以只读操作为主，称为查询集群。构建任务会被发送到构建集群，构建完成后系统将数据写入查询集群，通过查询集

群进行查询任务。

通过读写分离部署，您可以完全隔离构建和查询两种工作负载，让它们各自独立运行，避免它们之间的相互影响及可能

引发的性能不稳定。

检查和准备工作

由于牵涉到两套	Hadoop	环境，请仔细阅读和执行下述环境检查。

1.	 请确认要用到的构建集群和查询集群的	Hadoop	版本一致，且满足	Kyligence	Enterprise	安装的必要条件。

2.	 请确认在	Kyligence	Enterprise	服务器上安装和配置了查询集群和构建集群的	Hadoop	客户端，并确认	 	hdfs

， 	hive		等命令能够正常使用，且	Hadoop	集群上的服务和资源能够正常访问。

3.	 如果两个集群都启用了	HDFS	NameNode	HA，请确保两个集群的	HDFS	nameservice	名称不同。如果相同，请修改

其中某个集群的	nameservice	以避免冲突。

提示：对于	FusionInsight，通常默认安装即使用 	nameservice=hacluster	，这意味着未经事前规划的两个集群
将必定重名。所以在FusionInsight环境下，需要对两个HDFS集群配置别名。具体配置方法，参考如下：	分别
登录两个集群管理	web	页面，选择yarn选项卡，从配置项中找到 	dfs.distcp	，添加nameservice别名。例如：
查询集群所使用的HDFS的别名为 	readcluster	，构建集群所使用的HDFS的别名为 	writecluster	。找
到 	dfs.namenode.rpc-adress	配置项，添加远程namenode监听的完全限定的RPC地址。也可通过集群 	hdfs-
site.xml	文件配置，原理同上。

如果两个集群开启了Kerberos，需添加此配置：

kylin.engine.spark-conf.spark.yarn.access.hadoopFileSystems=hdfs://readcluster,hdfs://writecluster,hd
fs://hacluster，Kyligence	Enterprise	4.5.10以后版本推荐使用这个参数：kylin.engine.spark-conf.spark.kerber

os.access.hadoopFileSystems=hdfs://readcluster,hdfs://writecluster,hdfs://hacluster
部署在查询集群的节点需单独配置：

kylin.storage.columnar.spark-conf.spark.yarn.access.hadoopFileSystems=hdfs://readcluster,hdfs://write
cluster,hdfs://hacluster，Kyligence	Enterprise	4.5.10以后版本推荐使用这个参数：kylin.storage.columnar.spa

rk-conf.spark.kerberos.access.hadoopFileSystems=hdfs://readcluster,hdfs://writecluster,hdfs://haclust

er
由于查询下压时需要用到构建集群上的数据，需添加此配置：

kylin.storage.columnar.spark-conf.spark.sql.hive.specific.fs.location=hdfs://writecluster

4.	 请确认构建集群和查询集群可以在无须额外验证的情况下互相连通。

提示：您可以尝试从构建集群的任一节点上拷贝文件至查询集群的任一节点，以验证两个集群之间的安全性

和网络连通状况。

5.	 由于构建过程会在两个集群之间移动大量数据，请尽量缩短查询集群和构建集群之间的网络延迟。

6.	 如果两个集群开启了	Kerberos，需要确保以下配置：

构建集群和查询集群属于不同的域

构建集群和查询集群已配置互信

安装和配置读写分离部署

106

读写分离部署

下面说明如何在	Hadoop	集群中部署	Kyligence	Enterprise	读写分离模式。

1.	 首先在	Kyligence	Enterprise	服务器上，解压	Kyligence	Enterprise	安装包到统一的安装路径下。以下称此安装路径

为	 	$KYLIN_HOME	。

2.	 在	Kyligence	Enterprise	服务器准备好构建集群和查询集群的	hadoop	conf，查询集群的	hadoop	配置放到

	$KYLIN_HOME/hadoop_conf		目录，构建集群的	hadoop	配置放到	 	$KYLIN_HOME/write_hadoop_conf		目录，同时把构建
集群的	hive-site.xml	分别放到以上2个目录中，并且把	hive-site.xml	拷贝两份，分别命名为	hiveserver2-site.xml	和
hivemetastore-site.xml。

如果开启了	Kerberos	认证，需要将构建集群的	krb5.conf	文件拷贝到	 	$KYLIN_HOME/write_hadoop_conf		目录，将查询
集群的	krb5.conf	文件拷贝到	 	$KYLIN_HOME/hadoop_conf		目录。

3.	 设置配置：

	kylin.engine.submit-hadoop-conf-dir=$KYLIN_HOME/write_hadoop_conf

	##	Kyligence	Enterprise	服务所用的	HDFS	路径。将	{working_dir}	替换为真实路径，并注意使用绝对路径，例如	hdfs://kyli

n

	kylin.env.hdfs-working-dir={working_dir}

4.	 如果两个集群开启了	Kerberos，还需要进行以下额外配置：

	kylin.storage.columnar.spark-conf.spark.yarn.access.hadoopFileSystems=hdfs://readcluster,hdfs://writeclust

er

	kylin.engine.spark-conf.spark.yarn.access.hadoopFileSystems=hdfs://readcluster,hdfs://writecluster

5.	 如果开启了	Kerberos	验证机制，需要做以下检查，避免构建任务出错：

	java.lang.IllegalArgumentException:	Can't	get	Kerberos	realm

	...

	Caused	by:	KrbException:	Cannot	locate	default	realm

确保目录	 	$KYLIN_HOME/conf		下存在认证所需的	 	keytab		文件和	 	krb5.conf		文件
如果目录	 	$KYLIN_HOME/hadoop_conf		存在，确保该目录下存在	 	krb5.conf		文件
如果目录	 	$KYLIN_HOME/write_hadoop_conf		存在，确保该目录下存在	 	krb5.conf		文件

6.	 默认情况下所有的数据文件都存储在查询集群，也可选择将构建任务的平表数据独立存放在构建集群，在

	$KYLIN_HOME/kylin.properties		中配置，将	{working_dir}	替换为真实路径，并注意使用绝对路径：

#	如	hdfs://writecluster/kylin

kylin.env.hdfs-write-working-dir={working_dir}

注意：

使用该功能，如果需要保证之前在查询集群存储的平表数据仍然可用，需要执行额外的	shell	脚本进行迁移操
作，将查询集群的平表数据迁移到构建集群。脚本位于	 	$KYLIN_HOME/sbin/prepare-flat-table.sh	，可传入	 	--
help		了解功能细节，迁移数据对集群负载较大，请谨慎操作。
该配置参数一定要在系统级别配置，不要在项目级别进行配置，否则垃圾清理会遗漏该部分文件（即	HDFS	的
	/.../flat_table		目录）

至此，读写分离配置完毕。

注意：

读写分离模式下， 	$KYLIN_HOME/bin/sample.sh		不可用。 	$KYLIN_HOME/bin/check-env.sh		支持分别检测查询集群和构
建集群配置的Yarn队列是否可用，以及检测是否可以正常向配置的队列提交Spark任务。
读写分离模式下， 	kylin.properties		内	 	kylin.engine.spark-conf.spark.yarn.queue		需要配置为构建集群的队列。

107

读写分离部署

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

108

资源组部署

资源组部署

企业在统一平台架构下，为了实现在各个业务部门之间数据与资源的隔离，保障部门间应用不相互影响，Kyligence
Enterprise	支持了资源组部署模式。不同部门的项目可以绑定不同的资源组，不同的资源组独占一套	Kyligence	Enterprise
进程资源，从而实现了应用程序资源的隔离。

资源组与项目的请求绑定类型

资源组与项目的请求绑定类型分为如下两种：

查询请求：该请求绑定的资源组将仅用于响应该项目的查询请求，因此请您确保查询请求绑定的资源组下最少有一

个	All	角色或	Query	角色的实例。
构建请求：该资源组将仅用于响应该项目的构建请求，因此请您确保构建资源组下最少有一个	All	角色或一个	Job
角色的实例。

如何使用

资源组功能需要	Kyligence	Manager	4.5	配合使用，使用请参考	Kyligence	Manager	4.5	手册。

多租户部署

从	Kyligence	Enterprise	4.6.7	版本开始，支持隔离不同租户的存储数据及	Kerberos	访问认证权限。您必须使用	Kyligence
Manager	4.6.4.1	及以上版本，且通过资源组模式部署	Kyligence	集群，然后在	Kyligence	Enterprise	实例中配置相应系统
级参数：

##	在所有实例配置以下参数以开启多租户模式

kylin.multi-tenant.enabled=true

##	按照租户权限在实例级设置	HDFS	上	Kyligence	Enterprise	的工作目录，一个资源组内的实例配置同样的值：

kylin.env.hdfs-working-dir={working_dir}

##（可选）按照租户权限在实例级设置	Kerberos	的访问认证信息，，一个资源组内的实例配置同样的值：

kylin.kerberos.enabled=true

kylin.kerberos.platform=xxx

kylin.kerberos.principal={your_principal_name}

kylin.kerberos.keytab={your_keytab_name}

请注意如果从非多租户模式迁移到多租户模式，需要迁移	HDFS	中的数据，因为开启多租户模式后，各个租户的构建数
据会保存在各自的	HDFS	路径中，且租户间无法相互访问。

除此，我们还支持配置查询或构建的	Yarn	队列以隔离计算资源，您可查看	Hadoop	队列配置了解更多。

在下面的图例中，将租户	1	和租户	2	需要的	Kyligence	Enterprise	资源分别添加到资源组	1	和	资源组	2	中，然后将计算资
源、存储资源和访问认证信息配置到相应的	Kyligence	Enterprise	实例中。那么对于租户	1：

所有请求将由资源组	1	中的	Kyligence	Enterprise	实例响应，以独享构建/查询资源；
构建数据将存储在租户	1	指定的	HDFS	路径下，以隔离数据保证数据安全；
Kerberos	认证权限将根据租户	1	的权限生效，以控制访问权限；
构建/查询任务将由租户	1	指定的	Yarn	队列执行，以独享计算资源。

109

资源组部署

110

资源组部署

多租户部署

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

111

安全和用户认证

安全和用户认证

本章节将为您介绍	Kyligence	Enterprise	如何与	LDAP、Kerberos、第三方用户基础，实现用户认证。

Kyligence	产品支持使用国产密码（SM2、SM3、SM4）对数据和元数据进行可靠加密，并获得了国家相关部门认证。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:03

112

与	LDAP	集成

与	LDAP	集成

Kyligence	Enterprise	支持与	LDAP	服务集成用于实现用户认证，本章节将以	OpenLDAP	为例，描述如何配置	Kyligence
Enterprise	与	LDAP	服务集成	。

LDAP	环境准备

启用	LDAP	认证之前，需要一个运行的	LDAP	服务器，请联系您的	LDAP	管理员以获取必要的信息，如服务器连接信
息、人员和组织结构等。

安装	OpenLDAP

如果您环境中没有可用的	LDAP	服务器，则需要额外安装，推荐使用	OpenLDAP	Server	2.4，它是一个开源的、基于
OpenLDAP	Public	License	的实现，并且也是最流行的	LDAP	服务器之一，可以从官网下载：http://www.openldap.org/	。

OpenLDAP	服务器的安装，依系统不同而略有区别。这里以	CentOS	6.4	为例进行介绍：

检查是否已经安装

sudo	find	/	-name	openldap*

如果没有安装，使用	yum	安装：

sudo	yum	install	-y	openldap	openldap-servers	openldap-clients

配置	LDAP

cp	/usr/share/openldap-servers/slapd.conf.obsolete	/etc/openldap/slapd.conf

cp	/usr/share/openldap-servers/DB_CONFIG.example	/var/lib/ldap/DB_CONFIG

mv	/etc/openldap/slapd.d{,.bak}

修改	 	slapd.conf	，以给	example.com	公司配置为例，步骤如下：

设置目录树的后缀	将	 	suffix	"dc=my-domain,dc=com"		修改为： 	suffix	"dc=example,dc=com"

设置	LDAP	管理员的	DN	将	 	rootdn	"cn=Manager,dc=my-domain,dc=com"		修改为： 	rootdn
"cn=Manager,dc=example,dc=com"

设置	LDAP	管理员的密码	修改	 	rootpw	secret	，将	 	secret		使用密文密码代替；	如果要创建一个新的加
密密码，请使用下面的命令：

slappasswd

输入要设置的密码，加密值会被输出在终端界面，请将此值拷贝在	 	rootpw		这一行，如：

rootpw				{SSHA}vv2y+i6V6esazrIv70xSSnNAJE18bb2u

为配置文件修改权限

		chown	ldap.ldap	/etc/openldap/*

		chown	ldap.ldap	/var/lib/ldap/*

新建目录	 	/etc/openldap/cacerts

113

与	LDAP	集成

		mkdir	/etc/openldap/cacerts

启动服务

		sudo	service	slapd	start

新建文件	 	example.ldif	（包括三个用户，两个组）

#	example.com

dn:	dc=example,dc=com

objectClass:	dcObject

objectClass:	organization

o:	Example,	Inc.

dc:	example

#	Manager,	example.com

dn:	cn=Manager,dc=example,dc=com

cn:	Manager

objectClass:	organizationalRole

#	Users,	example.com

dn:	cn=Users,dc=example,dc=com

cn:	Users

objectClass:	organizationalRole

objectClass:	top

#	jack	example.com

dn:	cn=jack,cn=Users,dc=example,dc=com

objectClass:	inetOrgPerson

objectClass:	organizationalPerson

objectClass:	person

objectClass:	top

cn:	jack

sn:	jack	wang

mail:	jack@example.io

userPassword::	ZXhhbXBsZTEyMw==

#jimmy	example.com

dn:	cn=jimmy,cn=Users,dc=example,dc=com

objectClass:	inetOrgPerson

objectClass:	organizationalPerson

objectClass:	person

objectClass:	top

cn:	jimmy

sn:	jimmy	wang

mail:	jimmy@example.io

userPassword::	ZXhhbXBsZTEyMw==

#	People,	example.com

dn:	ou=People,dc=example,dc=com

ou:	People

cn:	People

objectClass:	organizationalRole

objectClass:	top

#	johnny,	People,	example.com

dn:	cn=johnny,ou=People,dc=example,dc=com

mail:	johnny@example.io

ou:	Manager

cn:	johnny

sn:	johnny	wang

objectClass:	inetOrgPerson

objectClass:	organizationalPerson

objectClass:	person

objectClass:	top

114

与	LDAP	集成

userPassword::	ZXhhbXBsZTEyMw==

#	jenny,	People,	example.com

dn:	cn=jenny,ou=People,dc=example,dc=com

mail:	jenny@example.io

ou:	Analyst

cn:	jenny

sn:	jenny	liu

objectClass:	inetOrgPerson

objectClass:	organizationalPerson

objectClass:	person

objectClass:	top

userPassword::	ZXhhbXBsZTEyMw==

#	oliver,	People,	example.com

dn:	cn=oliver,ou=People,dc=example,dc=com

objectClass:	inetOrgPerson

objectClass:	organizationalPerson

objectClass:	person

objectClass:	top

cn:	oliver

sn:	oliver	wang

mail:	oliver@example.io

ou:	Modeler

userPassword::	ZXhhbXBsZTEyMw==

#	Groups,	example.com

dn:	ou=Groups,dc=example,dc=com

ou:	Groups

objectClass:	organizationalUnit

objectClass:	top

#	itpeople,	Groups,	example.com

dn:	cn=itpeople,ou=Groups,dc=example,dc=com

cn:	itpeople

objectClass:	groupOfNames

objectClass:	top

member:	cn=johnny,ou=People,dc=example,dc=com

member:	cn=oliver,ou=People,dc=example,dc=com

#	admin,	Groups,	example.com

dn:	cn=admin,ou=Groups,dc=example,dc=com

cn:	admin

member:	cn=jenny,ou=People,dc=example,dc=com

member:	cn=jack,cn=Users,dc=example,dc=com

objectClass:	groupOfNames

objectClass:	top

注意： 	kylin.security.ldap.user-search-base		参数仅支持以下两种格式的值。

示例1： 	ou=People,dc=example,dc=com
示例2： 	cn=Users,dc=example,dc=com

通过命令导入用户信息

/usr/bin/ldapadd	-x	-W	-D	"cn=Manager,dc=example,dc=com"	-f	example.ldif

此时将提示输入密码，输入管理员的密码后，完成导入操作。

修改用户密码

管理员可以使用如下命令强制修改用户密码，过程中需要输入新密码、确认新密码、输入管理员密码

ldappasswd	-xWD	cn=Manager,dc=example,dc=com	-S			cn=jenny,ou=People,dc=example,dc=com

115

与	LDAP	集成

在	Kyligence	Enterprise	中进行配置

配置	LDAP	服务器的信息

在	 	$KYLIN_HOME/conf/kylin.properties		中配置	LDAP	服务器的	URL，提供必要的用户名和密码。为安全起见，这
里的密码需要通过加密算法	AES	进行加密，您可以运行下面的命令来获得加密后的密码：

$KYLIN_HOME/bin/kylin.sh	io.kyligence.kap.tool.general.CryptTool	-e	AES	-s	your_password

具体配置如下：

kylin.security.ldap.connection-server=ldap://<your_ldap_host>:<port>

kylin.security.ldap.connection-username=<your_user_name>

kylin.security.ldap.connection-password=<your_password_encrypted>

样例配置如下：

kylin.security.ldap.connection-server=ldap://127.0.0.1:389

kylin.security.ldap.connection-username=cn=Manager,dc=example,dc=com

kylin.security.ldap.connection-password=${your_password_encrypted}

提供检索用户信息的模式

例如从某个节点开始查询，需要满足哪些条件等。样例配置如下：

#定义用户的查找范围

kylin.security.ldap.user-search-base=ou=People,dc=example,dc=com

#定义用于查找用户的规则，按照用户名匹配

kylin.security.ldap.user-search-pattern=(&(cn={0}))

#定义权限组的查找范围

kylin.security.ldap.user-group-search-base=ou=Groups,dc=example,dc=com

#定义用于查找用户所属权限组的规则，{0}通过	userDN	匹配，或{1}通过	username	匹配

kylin.security.ldap.user-group-search-filter=(|(member={0})(memberUid={1}))

#定义用于查找用户的类型

kylin.security.ldap.user-search-filter=(objectClass=person)

#定义用于查找权限组的类型

kylin.security.ldap.group-search-filter=(|(objectClass=groupOfNames)(objectClass=group))

#定义用于查找权限组中用户成员的规则，按照权限组名称和类型匹配

kylin.security.ldap.group-member-search-filter=(&(cn={0})(objectClass=groupOfNames))

配置供系统集成的服务账户	样例配置如下：

#	LDAP	service	account	directory

kylin.security.ldap.service-search-base=ou=People,dc=example,dc=com

kylin.security.ldap.service-search-pattern=(&(cn={0}))

kylin.security.ldap.service-group-search-base=ou=Groups,dc=example,dc=com

配置管理员群组

在	Kyligence	Enterprise	中，可将一个	LDAP	群组映射成管理员角色，需要修改配置文件
	$KYLIN_HOME/conf/kylin.properties		，将配置项	 	kylin.security.acl.admin-role		设置为	LDAP	组名（大小写敏
感）。在当前例子中，将	LDAP	中组	 	admin		定义为	Kyligence	Enterprise	管理员，那么这里应该设置为：

116

与	LDAP	集成

kylin.security.acl.admin-role=admin

如果用户的	LDAP	采用自定义的	user-identifier-attr	，需要修改以下三个配置项，以	 	user-identifier-attr		为	 	sn
为例：

kylin.security.ldap.user-search-pattern=(&(sn={0}))

kylin.security.ldap.service-search-pattern=(&(sn={0}))

kylin.security.ldap.user-identifier-attr=sn

分页和范围检索

当	LDAP	policy	限制获取的最大的分页大小时（MaxPageSize），此时需要配置如下参数，用来获取所有用户，	默
认值1000，该值应该小于等于	MaxPageSize：

kylin.security.ldap.max-page-size=1000

当	LDAP	policy	限制范围检索时（MaxValRange），此时需要配置如下参数，使用范围检索来获取组下的所有用
户，默认值1500，	该值应该小于等于	MaxValRange：

kylin.security.ldap.max-val-range=1500

启用	LDAP

在	 	$KYLIN_HOME/conf/kylin.properties		中设置如下参数开启	LDAP，然后重启	Kyligence	Enterprise	生效。

kylin.security.profile=ldap

启用	LDAP	DN	大小写敏感

在	 	$KYLIN_HOME/conf/kylin.properties		中设置如下参数启用	LDAP	DN	大小写敏感，然后重启	Kyligence	Enterprise
生效。

```properties	kylin.system.property.org.springframework.ldap.core.keyCaseFold=none

LDAP	用户信息缓存

用户通过	LDAP	认证登录	Kyligence	Enterprise	后，其信息会被	Kyligence	Enterprise	缓存以减轻访问	LDAP	服务器的
开销。用户可以在	 	kylin.properties		中对用户信息缓存时间（秒）和最大缓存用户数目进行配置，默认值如下：

kylin.server.auth-user-cache.expire-seconds=300

kylin.server.auth-user-cache.max-entries=100

启用	LDAP	后，不能通过	Kyligence	Enterprise	管理用户/用户组，相关功能无法使用。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:03

117

与	Kerberos	集成

与	Kerberos	集成

Kyligence	支持集成	Kerberos，具体配置方法请参考安装与卸载章节中各平台安装手册进行集成。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:03

118

与	Kerberos	集成

项目级别配置	Kerberos

在开启了	Kerberos	集成后，从	4.1.0	版本开始	Kyligence	还支持项目级别配置不同的	Kerberos	用户。从而实现了不同项
目拥有不同的源数据加载权限，为企业级用户的安全管控提供了更加精细化的管理能力。

环境准备

开启项目级	Kerberos	集成，需要满足以下条件

1.	 环境中已开启	Kerberos	且在	Kyligence	中完成相关配置，具体请参考	与	Kerberos	集成
2.	 启动	Kyligence	的	Kerberos	用户需要拥有所有项目集成的	Kerberos	用户的	Hive	访问权限的合集
3.	 配置在项目上的	Kerberos	用户需要配置属于	Hive	用户组
4.	 更换项目配置的	Kerberos	用户时，绑定用户的	Hive	权限需要大于该项目已加载的数据源

如何开启

1.	 在	 	kylin.properties		文件中添加配置： 	kylin.kerberos.project-level-enabled=true
2.	 添加配置后启动	Kyligence，此时点击左侧导航栏中的设置，在高级设置界面找到Kerberos	配置，开启并填写内容

即可完成对应配置。

Project_with_kerberos

相关配置

配置项

默认值

描述

kylin.kerberos.project-
level-enabled

false

项目级别	Kerberos	开关，默认为	 	false	，表示不开启项目级	Kerberos。

kylin.source.hive.table-
access-filter-enabled

false

当项目级	Kerberos	开启时，该参数生效，表示是否在加载数据源时按照用
户权限展示源表，默认为	 	false	，表示不会在加载数据源时验证用户对源
表的权限，此时将展示全部	Hive	源表，当用户选择源表并提交加载时将验
证表权限，对没有权限的表将无法加载。当配置为	 	true		时，表示在加载
数据源展示源表时就验证表权限，仅展示用户有权限的表，表数量很多时，
可能会导致数据源页面加载较慢。

kylin.source.hive.table-
access-cache-enabled

true

在上述	2	个参数配置为	 	true		时，该参数生效，默认为	 	true	，表示缓存
用户表权限信息，此时验证表权限时将优先从缓存中取值，表数量很多时，
可以优化数据源页面的加载性能。

119

与	Kerberos	集成

access-cache-enabled

可以优化数据源页面的加载性能。

kylin.source.hive.table-
access-cache-size

100000

当	 	kylin.source.hive.table-access-cache-enabled		为	 	true		时，该参数生
效，表示用户表权限缓存大小。

kylin.source.hive.table-
access-cache-ttl

7d

当	 	kylin.source.hive.table-access-cache-enabled		为	 	true		时，该参数生
效，表示用户表权限缓存失效时间。

已知限制

1.	 开启该功能后，需要重新刷新数据源缓存后才可以生效
2.	 当前仅支持数据源加载功能使用不同的	Kerberos	账号权限读取，构建任务等相关功能仍以启动	Kyligence	的

Kerberos	用户提交

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:03

120

与第三方用户认证系统集成

与第三方用户认证系统集成

Kyligence	Enterprise	除了支持与	LDAP	集成实现用户认证外，还支持与第三方用户认证系统集成，可以将登录时的用户
认证工作委托于第三方系统。

默认情形下，Kyligence	Enterprise	有自己的用户管理系统，实现登录用户的认证与授权。当用户登录	Kyligence
Enterprise	时，系统会校验当前用户的用户名与密码，认证通过后完成登录。在此之外，Kyligence	Enterprise	开放了用户
认证的扩展接口，用户可以在这个接口中实现与第三方用户认证系统的对接，从而取代系统默认的用户认证，完成用户

校验与登录。

本文将介绍	Kyligence	Enterprise	实现与第三方用户认证系统集成的原理。

实现原理

原理如下图所示：

与第三方用户认证系统集成

与第三方用户认证系统的集成关键在于实现自定义的第三方用户认证扩展类，在其中完成与第三方用户认证系统的对

接，调用第三方系统的接口完成对用户名密码的校验，实现用户的登录认证。

实现方法

Kyligence	Enterprise	自带一个样例，向您展示如何从源代码编译到打包部署一个自定义的第三方用户认证扩展。详细介
绍请参考与第三方用户认证系统集成样例。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:03

121

与第三方用户认证系统集成

与第三方用户认证系统集成样例

与第三方用户认证系统集成	介绍了	Kyligence	Enterprise	实现与第三方用户认证系统集成的概念和原理。

本文将介绍	Kyligence	Enterprise	实现与第三方用户认证系统集成的实现方法，并举例说明如何进行开发实现。

实现方法

Kyligence	Enterprise	自带一个样例，向您展示如何从源代码编译到打包部署一个自定义的第三方用户认证扩展。下面向
您介绍这个样例工程。

一、搭建开发环境

拷贝	 	$KYLIN_HOME/samples/static-user-manager.tar.gz	，解压后目录为一个完整的样例程序，将其拷贝到工作目录后，
在项目的	lib	目录中加入以下jar包，并将其添加到项目依赖中。

您可以在	IDE	中打开并编译这个样例程序。

样例会创建一个基于内存的用户系统，该系统中包含两个用户	admin	和	test，admin	拥有管理员权限，test	拥有浏览权
限。

二、实现对接第三方用户认证系统的	Java	类

第三方用户认证的扩展点包含三个类：

OpenAuthenticationProvider:	用于校验登录用户是否合法等
OpenUserService:	用于返回用户列表，检查用户是否存在，返回管理员列表等
OpenUserGroupService:	用于返回用户组列表，返回用户组成员等
LogoutSuccessHandler:	用户登出成功的回调（默认使用
org.springframework.security.web.authentication.logout.SimpleUrlLogoutSuccessHandler）

下面会通过样例模版分别介绍如何实现这四个类。

1.	 OpenAuthenticationProvider	类的自定义实现模板

public	class	StaticAuthenticationProvider	extends	OpenAuthenticationProvider	{

				@Override

				public	boolean	authenticateImpl(Authentication	authentication)	{

								String	username	=	(String)	authentication.getPrincipal();

								UserDetails	userDetails	=	getUserService().loadUserByUsername(username);

								String	password	=	(String)	authentication.getCredentials();

122

与第三方用户认证系统集成

								if	(password.equals(userDetails.getPassword()))	{

												return	true;

								}

								return	false;

				}

}

authenticateImpl(Authentication	authentication)	该方法用来校验用户名密码是否合法，即是否允许用户登录。该
方法的参数为一个	Authentication	的对象，该对象有两个关键属性：

principal	登录页面传递过来的用户名
credentials	登录页面传递过来的密码
其他方法请根据您的实际需求进行覆盖实现

2.	 OpenUserService	类的自定义实现模版

public	class	StaticUserService	extends	OpenUserService	{

					private	final	List<ManagedUser>	users	=	new	ArrayList<>();

							@PostConstruct

							public	void	init()	{

								ManagedUser	admin	=	new	ManagedUser();

								admin.addAuthorities(Constant.ROLE_ADMIN);

								admin.setPassword("123456");

								admin.setUsername("admin");

								admin.setDisabled(false);

								admin.setLocked(false);

								users.add(admin);

								ManagedUser	test	=	new	ManagedUser();

								test.addAuthorities(Constant.ROLE_ANALYST);

								test.setPassword("123456");

								test.setUsername("test");

								test.setDisabled(false);

								test.setLocked(false);

								users.add(test);

							}

										@Override

							public	List<ManagedUser>	listUsers()	{

											return	users;

					}

							@Override

							public	List<String>	listAdminUsers()	{

								List<String>	admins	=	new	ArrayList<>();

								for	(ManagedUser	user	:	users)	{

										if	(user.getAuthorities().contains(new	SimpleGrantedAuthority(Constant.ROLE_ADMIN)))	{

												admins.add(user.getUsername());

										}

								}

								return	admins;

							}

							@Override

							public	boolean	userExists(String	s)	{

								for	(ManagedUser	user	:	users)	{

										if	(s.equals(user.getUsername()))	{

												return	true;

										}

								}

								return	false;

							}

										@Override

							public	UserDetails	loadUserByUsername(String	s)	{

								for	(ManagedUser	user	:	users)	{

										if	(s.equals(user.getUsername()))	{

123

与第三方用户认证系统集成

												return	user;

										}

								}

								throw	new	UsernameNotFoundException("Invalid	username	or	password.");

							}

							@Override

							public	void	completeUserInfo(ManagedUser	user)	{}

}

init()	方法用来做一些初始化的操作，该方法必须用	@PostConstruct	注解标注。在本例中我们做了创建两个用
户的操作。

listUsers()	方法用来返回所有用户，该方法的返回值是一个	ManagedUser	的集合。ManagedUser	包含几个关键
属性：

username：用户名
password：用户密码
disabled：是否禁用
locked：是否锁定
authorities：用户角色

​	在本例我们直接返回初始化之后的用户列表	users

listAdminUsers()	方法用来返回所有的角色为管理员的用户，该方法返回值是一个由用户名组成的List。在本例
中我们直接过滤出	users	中角色为	admin	的用户返回

userExists(String	s)	方法用来根据用户名返回用户是否存在。在本例中我们直接遍历	users	进行判断

loadUserByUsername(String	s)	方法用来返回一个用户。在本例中我们直接在	users	中进行查找。

completeUserInfo(ManagedUser	user)	方法用来做一些用户信息补充的操作。

注意：	在	Kyligence	Enterprise	中	completeUserInfo	是返回用户后必须的一个环节，所以即使您不需要在
completeUserInfo	中做什么事情，也要有一个空的实现。

其他方法请根据您的实际需求进行覆盖实现

3.	 OpenUserGroupService	类的自定义实现模板：

public	class	StaticUserGroupService	extends	OpenUserGroupService	{

							@Autowired

							UserService	userService;

							@Override

							public	List<ManagedUser>	getGroupMembersByName(String	s)	{

								try	{

												List<ManagedUser>	ret	=	new	ArrayList<>();

												List<ManagedUser>	managedUsers	=	userService.listUsers();

												for	(ManagedUser	user	:	managedUsers)	{

														if	(user.getAuthorities().contains(new	SimpleGrantedAuthority(s)))	{

																ret.add(user);

														}

												}

												return	ret;

								}	catch	(Exception	e)	{

														throw	new	RuntimeException("");

								}

							}

							@Override

							public	List<String>	getAllUserGroups()	{

								List<String>	groups	=	new	ArrayList<>();

								groups.add(Constant.ROLE_ADMIN);

124

与第三方用户认证系统集成

								groups.add(Constant.ROLE_ANALYST);

								return	groups;

					}

}

getGroupMembersByName(String	s)	返回用户组内的所有用户。在本例中，直接根据上述	UserService	中的用户
返回。

getAllUserGroups()	返回所有的用户组。在本例中，直接返回了一个静态的用户组集合。

其他方法请根据您的实际需求进行覆盖实现

注意：	如果您的用户管理系统没有用户组的概念，那您仅需在上述两个方法中保持空的实现即可。

4.	 LogoutSuccessHandler	类的自定义实现模板：

	public	class	StaticLogoutSuccessHandler	extends	SimpleUrlLogoutSuccessHandler	{

					private	static	final	Logger	logger	=	LoggerFactory.getLogger(StaticLogoutSuccessHandler.class);

					public	void	callback()	{

									logger.info("Logout	success	handler	callback	success...");

					}

					@Override

					public	void	onLogoutSuccess(HttpServletRequest	request,	HttpServletResponse	response,	Authentication	a

uthentication)	throws	IOException,	ServletException	{

									super.handle(request,	response,	authentication);

									callback();

					}

	}

三、打包、部署与调试

1.	 Maven	生成	jar	包

mvn	package	-DskipTests

在	target	目录下找到包含了扩展点实现的	jar	包。

2.	 部署	jar	包

当	Java	类已经准备好并打包完毕后，将该	jar	包放入路径 	$KYLIN_HOME/lib/ext	。

3.	 配置

在	 	conf/kylin.properties		中增加如下配置，并重启	Kyligence	Enterprise	生效。

#	配置安全模式为	custom

kylin.security.profile=custom

#	配置	OpenAuthenticationProvider

kylin.security.custom.authentication-provider-class-name=StaticAuthenticationProvider

#	配置	OpenUserService

kylin.security.custom.user-service-class-name=StaticUserService

#	配置	OpenUserGroupService

kylin.security.custom.user-group-service-class-name=StaticUserGroupService

#	配置	LogoutSuccessHandler

kylin.security.custom.logout-success-handler=StaticLogoutSuccessHandler

125

与第三方用户认证系统集成

4.	 登录	Kyligence	Enterprise	并认证

重新启动	Kyligence	Enterprise	后，系统的用户认证便已经与第三方应用集成了。登录系统时，输入的用户名和密码
将会由集成的第三方应用进行登录认证。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:03

126

系统配置

系统配置

在集群结点上安装产品后，还需要对	Kyligence	Enterprise	的参数进行配置。这些参数的配置能够将	Kyligence	Enterprise
接入现有的	Apache	Hadoop	和	Apache	Hive	环境中，并且可以根据实际环境中的条件对	Kyligence	Enterprise	进行性能优
化。

我们将在本章节介绍	Kyligence	Enterprise	的配置文件，配置项的详细含义，推荐的配置参数以及配置重写等内容。

Kyligence	Enterprise	配置文件一览表

组件名

文件名

描述

Kyligence
Enterprise

Kyligence
Enterprise

conf/kylin.properties

该文件是	Kyligence	Enterprise	使用的全局配置文件，包括和
Kyligence	Enterprise	有关的全部配置项。具体配置项的含义将在基
本配置参数章节详细介绍。

conf/kylin.properties.override

该文件是用户建立，文件中的配置项及参数将会覆盖
kylin.properties	中对应配置项的默认值

Hadoop

hadoop_conf/core-site.xml

该文件是	Hadoop	使用的全局配置文件，用于定义系统级别的参
数，如	HDFS	URL、Hadoop	临时目录等。

Hadoop

hadoop_conf/hdfs-site.xml

该文件用于配置	HDFS	参数，如	NameNode	与	DataNode	存放位
置、文件副本个数、文件读取权限等。

Hadoop

hadoop_conf/yarn-site.xml

该文件用于配置	Hadoop	集群资源管理系统参数，如
ResourceManager	与	NodeManager	的通信端口，Web	监控端口等。

Hadoop

hadoop_conf/mapred-
site.xml

该文件用于配置	Map	Reduce	参数，如	Reduce	任务的默认个数，任
务能够使用内存的默认上下限等。

Hive

hadoop_conf/hive-site.xml

该文件用于配置	Hive	运行参数，如	Hive	数据存放目录，数据库地
址等。

注意：

若无特殊说明，本手册中出现的配置文件如	 	kylin.properties		均指代上述一览表中相应的配置文件。

修改	Kyligence	Enterprise	的系统配置

若需要在文件	kylin.properties	或	kylin.properties.override	中新增/变更系统配置

1.	 未被	Kyligence	Manager	管理，请到相应的配置文件中操作，执行启动/重启后生效。

2.	 已被	Kyligence	Manager	管理（即在	Kyligence	Manager	页面上关联的	Kyligence	Enterprise	实例）请在	Kyligence

Mananger	页面上修改实例	Kyligence	Enterprise	的参数配置，执行启动/重启后生效。

注意：不能在	Kyligence	Enterprise	自行修改系统配置,	您必须先在	Kyligence	Manager	页面上解除关联，否则在
Kyligence	Manager	上的任何启动、停止操作之后，修改的配置失效。

从	4.6.0.0	开始	在Kyligence	Enterprise	执行启动/重启会报错，内容如下

Operation	failed!	This	instance	of	Kyligence	Enterprise	has	been	managed	by	Kyligence	Manager,	you	ca

n't	modify	configuration	in	Kyligence	Enterprise.	Please	go	to	Kyligence	Manager	If	you	need	to	modif

y	the	configuration	file.

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

127

基本配置参数

基本配置参数

常用配置项

	kylin.properties		在	Kyligence	Enterprise	的配置文件中占据重要位置。以下是该文件中的常用配置项及具体含义：

配置项

描述

server.port

Kyligence	Enterprise	服务所用的端口，默认是	 	7070	。

kylin.env.ip-address

Kyligence	Enterprise	服务所在节点网络地址存在	ipv6	格式时，可以通过此配
置项指定	ipv4	格式，默认是	 	0.0.0.0

kylin.env.hdfs-working-dir

Kyligence	Enterprise	服务所用的	HDFS	路径。默认值为	HDFS	上的	 	kylin/	，
子目录为元数据库路径中的表名。例如，元数据库路径参数值为
	ke_metadata@jdbc	，则该	HDFS	路径默认值是 	/kylin/ke_metadata	。请预先
确保启动	Kyligence	Enterprise	实例的用户有读写该目录的权限。

kylin.env.zookeeper-connect-string

ZooKeeper	的地址，没有默认值，此参数必须在启动前手动配置好，否则
Kyligence	Enterprise	无法启动。

kylin.metadata.url

Kyligence	Enterprise	元数据库路径。默认值为	PostgreSQL	中的	 	ke_metadata
表，用户可以手动修改参数值以自定义的名称命名元数据库。在同一个集群
上部署多个	Kyligence	Enterprise	实例时，可以为每个实例配置一个独有的元
数据库路径，以实现多个实例间的隔离。例如，Production	实例设置该值为
	ke_metadata_prod	，Staging	实例设置该值为	 	ke_metadata_staging	，那么在
Staging	实例中的操作不会对	Production	实例产生任何影响。

kylin.metadata.ops-cron

定时备份元数据、垃圾清理的定时任务	cron	表达式，默认值是	 	0	0	0	*	*
*	。

kylin.metadata.audit-log.max-size

审计日志的最大记录行数，默认值是	 	500000	，4.6.9.0	版本之前的默认值为
	3000000	。

kylin.metadata.compress.enabled

是否开启元数据及审计日志的内容压缩，默认值为	 	true	。

kylin.server.mode

kylin.web.timezone

Kyligence	Enterprise	实例的运行模式，参数值可以是	 	all		,	 	query		,	 	job		中
的一个，默认值为	 	all	。 	query		模式表示该服务仅用于	SQL	查询，不用于
构建任务的调度及元数据更新； 	job		模式表示该服务仅用于任务构建和元数
据更新，无法提供查询服务； 	all		模式表示该服务同时用于任务调度，元数
据更新和	SQL	查询。

Kyligence	Enterprise	的	REST	服务所使用的时区。默认值为本地机器的系统的
时区。用户可以根据具体应用的需要修改此参数，更多参数选项请参考	List
of	tz	database	time	zones	中的	 	TZ	database	name		列。

kylin.web.export-allow-admin

是否允许	Admin	用户导出查询结果到	CSV	文件，默认值是	true。

kylin.web.export-allow-other

是否允许非	Admin	用户导出查询结果到	CSV	文件，默认值是	true。

kylin.web.stack-trace.enabled

错误提示弹窗是否显示详情，默认值是	false。开始生效版本：4.1.1

kylin.web.data-binder.auto-grow-
collection-limit

表单请求中数组入参的最大限制，默认值是	256，通过修改此参数可以限制
导出模型时单次导出的模型个数。开始生效版本：4.6.15

kylin.env

Kyligence	Enterprise	部署的用途，可以是	 	DEV	、 	PROD	、 	QA	。出厂默认值
为	 	PROD	。在	 	DEV		模式下一些开发者功能将被启用。

kylin.circuit-breaker.threshold.project

允许创建项目的最大个数，默认值是	 	100

kylin.circuit-breaker.threshold.model

单个项目允许创建模型的最大个数，默认值是	 	100

kylin.query.force-limit

限制查询返回结果的条数，默认不限制，默认值为：-1。BI	工具往往会发送
类似	select	from	fact_table	的查询语句，对于数据特别多的表格，数据返回时
间较长，会造成	BI	工具的长时间卡顿。该参数通过为	select	语句强制添加
LIMIT	分句，达到缩短数据返回时间的效果。启动该功能的方法为将该配置
项的值设置为正整数，如	 	1000	，该值会被用在	LIMIT	分句，查询语句最终

128

基本配置参数

kylin.query.max-result-rows

kylin.query.init-sparder-async

项的值设置为正整数，如	 	1000	，该值会被用在	LIMIT	分句，查询语句最终
会被转化成	select	from	fact_table	limit	1000。该参数可在*项目级别重写。

该参数限制了查询返回结果的最大行数，并作用于所有连接方式，包括用户
界面、异步查询、JDBC	Driver	与	ODBC	Driver。该参数有效取值范围为不超
过	2147483647	的正整数。默认值为	0，表示不设限制。除此参数之外，限制
返回结果行数的方式还有：SQL中最外层的limit条件、前端界面中的limit条件
和	kylin.query.force-limit参数（该参数仅针对于	select	语句生效）。当这些条
件同时触发时，最终的返回结果行数为：	SQL	limit	>	min(前端	limit,
kylin.query.max-result-rows)	>	kylin.query.force-limit。	该参数可在*项目级别重
写。

该参数默认为	 	true		，指	sparder	异步启动，即	Kyligence	Enterprise	的	web
服务和查询	spark	服务启动分开运行；若设置为	 	false		，当	sparder	服务启
动完成后，	Kyligence	Enterprise	的	web	服务才可正常服务

kylin.circuit-breaker.threshold.query-
result-row-count

该参数为SQL查询返回的结果集的最大行数，默认为 	2000000	，若超过最大
行数，后端将抛出异常。

kylin.query.timeout-seconds

kylin.query.convert-create-table-to-
with

kylin.query.replace-count-column-
with-count-star

kylin.query.match-partial-inner-join-
model

查询超时时间，默认值为	 	300		秒。查询执行时间超过	300	秒将报错： 	Query
timeout	after:	300s	。最小值为	 	5		秒，配置的值小于	 	5		秒	也按照	 	5		秒
生效。

一些	BI	工具会在查询中创建临时表或中间表。将该参数设置为	 	true		可以
将查询中创建表的语句转成	with	语句，当后续查询需要使用到该临时表或中
间表时，会被转化成包含	With	的查询语句。修改这个配置后，创建中间表或
临时表的查询可以击中可匹配的模型，默认为	 	false	。

该参数默认为 	false		，指在模型中设置	COUNT(column)	度量后，包含
COUNT(column)	的	SQL	语句才可以击中模型。若没有设置相应的
COUNT(column)	度量，但仍然希望在	SQL	中调用该函数，可以将该参数设
置为	 	true	，此时系统将使用	COUNT(constant)	度量来近似代替对应的
COUNT(column)	度量。	COUNT(constant)	将计算包括	Null	值的所有值。

该参数默认为 	false		，指多表	inner	join	的模型不支持回答	inner	join	部分匹
配的	SQL。举例如下：假设	A、B、C	为三张表，默认情况下，A	inner	join	B
的	SQL	只能用	A	inner	join	B	的模型或者	A	inner	join	B	left	join	C	的模型来回
答，不能用	A	inner	join	B	inner	join	C	的模型来回答。若将该参数设置为
	true	，A	inner	join	B	的	SQL	可以用	A	inner	join	B	的模型或者	A	inner	join	B
left	join	C	来回答，也可以用	A	inner	join	B	inner	join	C	的模型来回答。

kylin.query.use-tableindex-answer-
non-raw-query

该参数默认为 	false		，指聚合查询只可以用聚合索引回答，若将该参数设置
为	 	true	，此时系统允许使用对应的明细索引来回答聚合查询。

kylin.query.layout.prefer-aggindex

该参数默认为 	true		，指聚合索引和明细索引进行索引比较选择时，优先选
择聚合索引。

kylin.storage.columnar.spark-
conf.spark.yarn.queue

kylin.storage.columnar.spark-
conf.spark.master

kylin.job.retry

Spark	查询集群使用的	YARN	队列名称。

Spark	的部署一般分为	Spark	on	YARN	模式，Spark	on	Mesos	模式，和
standalone	模式，我们默认使用	YARN	模式下的	Spark	作查询任务。该配置参
数可以指定	Kyligence	Enterprise	所使用	standalone	模式下的	spark	集群，使
Kyligence	Enterprise	将任务提交到指定的	spark-master-url。

任务自动重试次数，默认值为	0，即任务出错时不会进行自动重试。启用该
参数（设置为大于	0	的值）会作用于任务中每一个具体步骤的重试次数，当
该具体步骤完成后，将重置该参数。

kylin.job.retry-interval

任务重试的间隔，默认值为	 	30000	，单位毫秒。当配置了上述任务重试次数
后，该参数才生效。

kylin.job.max-concurrent-jobs

kylin.job.node-max-concurrent-jobs

单个项目构建任务并发数限制，默认为	20。提交新构建任务时，如果超出了
系统允许的任务并发数限制，那么该提交的构建任务会进入任务队列。当有
运行的任务完成时，	Kyligence	Enterprise	会以先进先出	(FIFO)	的方式调度队
列中的任务执行。

单个	job	节点（或	all	节点）任务并发数限制，默认为	30。当节点达到任务并
发数量限制后，就不再执行新的任务。直到有运行的任务完成时，	Kyligence
Enterprise	会以先进先出	(FIFO)	的方式调度队列中的任务执行。

129

基本配置参数

kylin.scheduler.schedule-job-timeout-
minute

任务执行超时时间，默认值为	 	0	，单位分钟，默认不启用。当配置了上述任

务执行超时时间后，该参数才生效。任务执行超过超时时间，会变为	Error	状
态。

kylin.garbage.storage.cuboid-layout-
survival-time-threshold

HDFS	上的无效文件的阈值，在执行命令行工具进行垃圾清理时，超过此阈
值的	HDFS	上的无效文件会被清理，默认值为	 	7d	，表示	7	天。HDFS	上的
无效文件包括过期的索引、过期的快照、过期的字典等。同时会根据索引优
化策略清理性价比较低的索引。

kylin.garbage.storage.executable-
survival-time-threshold

过期任务的阈值，超过此阈值的并且已经完成的元数据任务会被清理，默认
值为	 	30d	，表示	30	天。

kylin.storage.quota-in-giga-bytes

每个项目的存储配额，默认值为	 	10240	，单位是	GB。

kylin.influxdb.address

InfluxDB	的地址，默认值是	 	localhost:8086	。

kylin.influxdb.username

InfluxDB	的用户名，默认值是	 	root	。

kylin.influxdb.password

InfluxDB	的密码，默认值是	 	root	。

kylin.metrics.influx-rpc-service-bind-
address

如果修改了	influxdb	配置文件	/etc/influxdb/influxdb.conf中的	 	#	bind-address
=	"127.0.0.1:8088"	，需要同步更新此参数。该参数会影响到打诊断包时对指
标监控数据的收集。

kylin.security.user-password-encoder

用户密码的加密算法。默认是	BCrypt	算法：
org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder，如果要使
用	Pbkdf2	算法，将该值配置成	org.springframework.security.crypto.password。
注意：请不要随意更改这个配置项，否则可能会导致用户无法登录

kylin.web.session.secure-random-
create-enabled

默认为	false，使用	UUID	生成	sessionId，开启后使用	JDK	的	SecureRandom
随机数，在经过	MD5	加密生成	sessionId。注意：如果开启了该功能，请先使
用升级Session表工具进行	session	表的升级，否则用户登录时会报错。

kylin.web.session.jdbc-encode-
enabled

默认为	false，sessionId	不加密直接保存进数据库，开启后	sessionId	会加密保
存到数据库。注意：如果配置了加密功能，请先使用升级Session表工具进行
session表的升级，否则用户登录时会报错。

kylin.server.cors.allow-all

配置	Kyligence	Enterprise	是否允许跨域请求， 	true		允许所有的跨域行
为， 	false		禁止所有的跨域行为，默认为 	false

kylin.server.cors.allowed-origin

kylin.storage.columnar.spark-
conf.spark.driver.host

kylin.engine.spark-
conf.spark.driver.host

指定允许跨域的白名单，多个域名使用逗号	 	,		分开，比如
	http://domain1.com.cn,http://domain2.com.cn	，4.5.10.0	版本之前支持配置
为	 	*		表示全部域名。kylin.server.cors.allow-all	配置为	 	true		时，此参数生
效。

配置	Kyligence	Enterprise	查询节点	Spark	Driver	所在机器的	IP	信息

配置	Kyligence	Enterprise	构建节点	Spark	Driver	所在机器的	IP	信息

kylin.engine.sanity-check-enabled

配置	Kyligence	Enterprise	在构建时是否开启	Sanity	Check，默认值为	 	true

kylin.job.finished-notifier-url

在构建任务完成时，会向该	url	通过	HTTP	请求发送任务状态信息

kylin.diag.obf.level

诊断包的脱敏等级。 	RAW		代表不脱敏， 	OBF		代表脱敏。配置	 	OBF		会脱敏
	kylin.properties		文件中的用户名、密码等敏感信息（请参考诊断包工具章
节），默认值为	 	OBF	。

kylin.diag.task-timeout

诊断包的各个子任务超时时间，默认超时时间是3分钟

kylin.diag.task-timeout-black-list

诊断包子任务超时黑名单（以逗号分隔子任务），在超时黑名单里面的子任
务不受超时时间控制，会一直运行直到结束，默认值是	 	METADATA	, 	LOG
当前的可选值列表如下：METADATA，AUDIT_LOG，	CLIENT，
JSTACK，CONF，HADOOP_CONF，BIN，HADOOP_ENV，
CATALOG_INFO，SYSTEM_METRICS，MONITOR_METRICS，
SPARK_LOGS，SPARDER_HISTORY，KG_LOGS，LOG，JOB_TMP，
JOB_EVENTLOGS

kylin.query.queryhistory.max-size

全部项目的查询历史总留存条数，默认为	10000000

130

基本配置参数

kylin.query.queryhistory.max-size

全部项目的查询历史总留存条数，默认为	10000000

kylin.query.queryhistory.project-max-
size

单个项目的查询历史留存条数，默认为	1000000

kylin.query.queryhistory.survival-
time-threshold

全部项目的查询历史保留时间，默认为	30d，表示	30	天，还支持其他单位：
毫秒	ms，微秒	us，分钟	m	或者	min，小时	h

kylin.query.engine.spark-scheduler-
mode

查询引擎的调度策略，默认为	FAIR（公平调度），可选值为	SJF（最小作业
优先调度）。填写其他值时将默认使用	FAIR	调度策略。

kylin.query.realization.chooser.thread-
core-num

查询引擎中，模型匹配线程池的核心线程数，默认为	5。	注意:当核心线程数
设置为小于	0	时，将会导致此线程池不可用，从而导致整个查询引擎不可用

kylin.query.realization.chooser.thread-
max-num

查询引擎中，模型匹配线程池的最大线程数，默认为	50。	注意:当最大线程
数设置为小于等于	0	或者小于核心线程数时，将会导致此线程池不可用，从
而导致整个查询引擎不可用

kylin.query.memory-limit-during-
collect-mb

限制查询获取数据时，Kyligence	Enterprise	消耗的内存大小，单位为	mb	，默
认为	5400mb

kylin.query.auto-model-view-enabled

自动为模型生成view.	当开启后，会为每一个模型自动生成一个view。用户可
以直接查询该	view。view会被命名为	{project	name}.{model	name}。view	会
包含模型定义的所有表，以及维度度量中所引用的的列。

kylin.streaming.job.max-concurrent-
jobs

实时功能专用。最大spark任务数量，数据摄取任务数与自动合并任务数的总
和。

kylin.streaming.kafka-
conf.maxOffsetsPerTrigger

kylin.streaming.job-status-watch-
enabled

实时功能专用。限流参数，单次拉取的最大消息条数。0	表示不限流。

实时功能专用。是否开启任务监控；true表示开启，false表示不开启。

kylin.streaming.job-retry-enabled

实时功能专用。是否开启任务失败重试；true表示开启，false表示不开启。

kylin.streaming.job-retry-interval

实时功能专用。任务失败重试间隔，如再次失败，间隔会成倍增加，默认值
为：5m，单位：分钟。

kylin.streaming.job-retry-max-interval

实时功能专用。任务失败重试最大间隔，达到最大值，重试间隔不会增加，
默认值为：30m，单位：分钟。

kylin.engine.streaming-metrics-
enabled

实时功能专用。是否开启任务	metrics	监控，true	表示开启，false	表示不开
启，默认为	false

kylin.engine.streaming-segment-
merge-interval

实时功能专用。实时	Segment	合并调度间隔，每	60s	扫描元数据中是否存在
可合并的	Segment，默认值为：60s，单位：秒。

kylin.engine.streaming-segment-clean-
interval

实时功能专用。Segment	清理间隔：单位：小时。Segment	合并后，会按照这
个参数定时删除合并前的	Segment。默认值为：2h，单位：小时。

kylin.engine.streaming-segment-
merge-ratio

实时功能专用。Segment	合并比率，合并后	Segment	大小可超过合并阈值的
最大比例，默认值为：1.5

kylin.streaming.jobstats.survival-time-
threshold

实时功能专用。单位：天。实时流统计记录保持的时长，默认为7天。

kylin.streaming.spark-
conf.spark.yarn.queue

kylin.streaming.spark-
conf.spark.port.maxRetries

实时功能专用。实时功能独立使用的队列名称。

实时功能专用。端口占用重试次数。

kylin.streaming.kafka.starting-offsets

实时功能专用。从	Kafka	的哪个offset开始消费，默认值是	latest，从最近数据
开始消费。

kylin.storage.columnar.spark-
conf.spark.sql.view-truncate-enabled

允许spark	view	在加载表和查询时丢失精度，默认值为false。从	4.6.12.0	版本
之后，需要另外设置配置项	 	kylin.storage.columnar.spark-
conf.spark.sql.legacy.useCurrentConfigsForView=true		才能生效。

kylin.engine.spark-

允许spark	view	在构建时丢失精度，默认值为false。在	 	KE-4.6.12.0		版本之

131

基本配置参数

kylin.engine.spark-
conf.spark.sql.view-truncate-enabled

允许spark	view	在构建时丢失精度，默认值为false。在	 	KE-4.6.12.0		版本之
后，需要另外设置配置项	 	kylin.engine.spark-

conf.spark.sql.legacy.useCurrentConfigsForView=true		才能生效。

kylin.source.hive.databases

配置数据源加载的数据库列表，无默认值，系统级和项目级皆可配置，项目
级别的优先级大于系统级别。

kylin.build.resource.read-
transactional-table-enabled

是否开启支持	Hive	事务表功能，默认值	true。开启本功能后，您还可以配置
	kylin.source.hive.beeline-params		参数进行自定义	Hive	连接，不配置时将
使用默认连接。

kylin.source.hive.beeline-params

Hive	beeline	连接参数，配置示例： 	-u
'jdbc:hive2://<HiveServer2>:10000/;principal=hive/{HOST_NAME}@EXAMPLE.COM'

kylin.query.replace-dynamic-params-
enabled

JDBC	查询是否开启动态参数绑定，默认值为	flase，表示不开启，更多信息
参考	Kyligence	JDBC	驱动

kylin.second-storage.route-when-ch-
fail

kylin.second-storage.query-pushdown-
limit

kylin.query.project-merge-with-bloat-
enabled

kylin.query.project-merge-bloat-
threshold

开启分层存储时，匹配基础明细索引的查询是否仅通过分层存储回答，默认
值为	 	0	，表示当分层存储无法回答时，通过	HDFS	上的基础明细索引回答，
配置为	 	1		表示当分层存储无法回答时，查询下压，配置为	 	2		表示当分层
存储无法回答查询时，查询失败。

当查询结果集较大时，使用分层存储的查询性能可能会下降。该参数表示：
是否开启通过	limit	语句限定明细查询是否使用分层存储，默认值为	 	0	，表
示不开启。如果需要开启，可配置具体的数值，如配置为	 	100000		表示	limit
后的数值	<=	100000	的明细查询可以通过分层存储回答，明细查询不包含
limit	语句或	limit	后的数值	>	100000	时将不使用分层存储回答。

在解析	SQL	的过程中，特定相邻节点的合并可以提高总体的查询吞吐量，但
是在极端情况下，可能对JVM的GC产生较大压力，导致查询失败。这个参数
表示：是否判断两个节点合并带来的收益，来决定是否进行合并，以此来减
轻合并可能带来的内存压力。默认值为	 	true	，表示开启。如果需要关闭，
将其配置为 	false	。从	4.6.23.0	版本开始，参数作废，请使用
	kylin.query.project-merge-bloat-threshold

在	4.6.23.0	之前版本，表示相邻节点合并的控制阈值，参数说明：将合并后
包含的子节点数计为m，待合并的两个节点各自包含的子节点数分别记为a,
b。则当m	>	a	+	b	+	threshold时不进行合并。可见，参数值越小，则约束越严
格。当参数小于0，永远不进行合并。参数默认值为 	0	。从	4.6.23.0	版本开
始，参数默认值为	 	100	，用于控制	SQL	嵌套子查询和外层查询中的	project
是否合并。遵循	calcite	的原始实现，默认值	100。举例：1)	select	a,	b	from
(select	c+d	as	a,	select	e+f	as	b	from	t)	在生成	SQL	执行计划的时候，如果没有
超过阈值，那么生成的执行计划等价于这条	SQL	生成的执行计划	select	c+d,
e+f	from	t。可以简单理解为对原始	SQL	的一种简化来提高执行效率。

kylin.query.async-query.max-
concurrent-jobs

配置异步查询队列后，异步查询任务的最大个数。当任务数达到限制后，异
步查询报错。默认值是	0，表示不限制异步查询任务数。

kylin.query.using-metadata-answer-
minmax-of-dimension

允许对维度的	min/max	查询使用元数据回答，默认值	true。从	4.6.12.0	版本开
始生效。如果查询仅击中快照，为保证查询结果准确，将由快照回答。

kylin.query.calcite.aggregate-
pushdown-enabled

查询优化是否开启聚合下推规则，默认值	true，表示开启。开启时，如果外
层查询聚合中使用的列都来源于左边的子查询，那么这种聚合就会被下推到
左边的这个子查询，从而优化查询性能。

kylin.storage.columnar.spark-
conf.spark.cleaner.periodicGC.interval

按照时间间隔定时执行	Full	GC，默认值是	 	30min	，支持的时间单位为小时
	h	，分钟	 	min	，秒	 	s

kylin.query.engine.periodicGC.crontab

按照	cron	表达式定时执行	Full	GC，默认值是	 	-	，表示未生效，此时会按照
	kylin.storage.columnar.spark-conf.spark.cleaner.periodicGC.interval		的配
置执行	Full	GC，当配置为具体的	cron	表达式
后， 	kylin.storage.columnar.spark-conf.spark.cleaner.periodicGC.interval
将失效。

配置重写

132

基本配置参数

配置文件	 	kylin.properties		中的配置项较多，如果仅需要修改其中的几项配置，可以在	 	$KYLIN_HOME/conf		路径下新建
名称为	 	kylin.properties.override		的文件，并将需要修改的配置项写在该文件中，文件中的配置项及参数将会覆盖
	kylin.properties		中对应配置项的默认值。在系统升级中，您仅需复制文件	 	kylin.properties.override		到新版本的
	KYLIN_HONE/conf		路径下，即可实现配置升级。

JVM	参数

在配置文件	 	$KYLIN_HOME/conf/setenv.sh.template		中，给出了	 	KYLIN_JVM_SETTINGS		示例配置。默认配置使用的内存较
少，您可以根据自己的实际情况调节。该项配置的默认值如下:

export	KYLIN_JVM_SETTINGS="-server	-Xms1g	-Xmx8g	-XX:+UseG1GC	-XX:MaxGCPauseMillis=200	-XX:G1HeapRegionSize=16m

	-XX:+PrintFlagsFinal	-XX:+PrintReferenceGC	-verbose:gc	-XX:+PrintGCDetails	-XX:+PrintGCTimeStamps	-XX:+PrintGC

DateStamps	-XX:+PrintAdaptiveSizePolicy	-XX:+UnlockDiagnosticVMOptions	-XX:+G1SummarizeConcMark		-Xloggc:$KYLIN

_HOME/logs/kylin.gc.$$		-XX:+UseGCLogFileRotation	-XX:NumberOfGCLogFiles=10	-XX:GCLogFileSize=64M	-XX:+HeapDump

OnOutOfMemoryError	-XX:HeapDumpPath=${KYLIN_HOME}/logs"

若您需要更改它，您需要复制一份，并将其命名为	 	setenv.sh		并将其放入	 	$KYLIN_HOME/conf/		文件夹中，然后修改其
中的配置。其中，参数"-XX:+HeapDumpOnOutOfMemoryError	-XX:HeapDumpPath=${KYLIN_HOME}/logs"	的配置可以
在发生内存溢出错误时，生成日志文件帮助诊断，日志文件的默认路径是	${KYLIN_HOME}/logs	，您可以根据实际需
求，切换日志存放的路径。

export	JAVA_VM_XMS=1g								#kylin启动时的JVM初始内存。
export	JAVA_VM_XMX=8g								#kylin启动时的JVM最大内存。
export	JAVA_VM_TOOL_XMS=1g			#工具类启动时的JVM初始内存。
export	JAVA_VM_TOOL_XMX=8g			#工具类启动时的JVM最大内存。

如果未设置	JAVA_VM_TOOL_XMS	的值，那么	JAVA_VM_TOOL_XMS	的值会使用	JAVA_VM_XMS	的值，同理未设
置	JAVA_VM_TOOL_XMX	的值时，JAVA_VM_TOOL_XMX	会使用	JAVA_VM_XMX	的值。

注意：1.	部分比较特殊的工具类，比如	guardian.sh，check-2100-hive-acl.sh，get-properties.sh，不受
JAVA_VM_TOOL_XMS，JAVA_VM_TOOL_XMX	配置的影响。

	2.	JAVA_VM_TOOL_XMS	和	JAVA_VM_TOOL_XMX	两个配置项自	KE	4.1.8	版本新增并生效，旧版本升级时需要您手动配置它们。

配置参数修改时	Kyligence	Enterprise	的热启动说明

在启动	Kyligence	Enterprise	时，系统会默认加载配置文件	 	kylin.properties		中定义的参数。如果您修改了参数，需要
重新启动	Kyligence	Enterprise	才能使新参数值生效。

生产环境推荐配置

在	 	$KYLIN_HOME/conf/		路径下，我们准备了两套可用的出厂配置方案： 	production		和	 	minimal	。前者是默认方案，适
用于实际生产环境；后者使用较少的资源，适用于沙箱等资源有限的环境。如果您的单点环境资源有限，可以切换到

	minimal		配置。请您在	 	$KYLIN_HOME/conf/kylin.properties		中取消以下配置项的注释，然后重启	Kyligence	Enterprise
使之生效。

#	KAP	provides	two	configuration	profiles:	minimal	and	production(by	default).

#	To	switch	to	minimal:	uncomment	the	properties

#	kylin.storage.columnar.spark-conf.spark.driver.memory=512m

#	kylin.storage.columnar.spark-conf.spark.executor.memory=512m

#	kylin.storage.columnar.spark-conf.spark.executor.memoryOverhead=512m

#	kylin.storage.columnar.spark-conf.spark.executor.extraJavaOptions=-Dhdp.version=current	-Dlog4j.configuration

=spark-executor-log4j.properties	-Dlog4j.debug	-Dkap.hdfs.working.dir=${kylin.env.hdfs-working-dir}	-Dkap.metad

ata.identifier=${kylin.metadata.url.identifier}	-				Dkap.spark.category=sparder	-Dkap.spark.project=${job.proj

ect}	-XX:MaxDirectMemorySize=512M

#	kylin.storage.columnar.spark-conf.spark.yarn.am.memory=512m

133

基本配置参数

#	kylin.storage.columnar.spark-conf.spark.executor.cores=1

#	kylin.storage.columnar.spark-conf.spark.executor.instances=1

与	Spark	相关的配置项

与	Spark	相关的配置项请您参阅官方文档	Spark	Configuration。以下我们介绍一些在	Kyligence	Enterprise	中与查询和构建
任务相关的配置项。

以	 	kylin.storage.columnar.spark-conf		开头的配置项：

该类配置项后半部分为在	Kyligence	Enterprise	中查询任务使用的	Spark	参数，推荐配置文件	 	kylin.properties		中的默
认参数如下：

Properties	Name

Min

Prod

kylin.storage.columnar.spark-conf.spark.driver.memory

kylin.storage.columnar.spark-conf.spark.executor.memory

kylin.storage.columnar.spark-conf.spark.executor.memoryOverhead

kylin.storage.columnar.spark-conf.spark.yarn.am.memory

kylin.storage.columnar.spark-conf.spark.executor.cores

kylin.storage.columnar.spark-conf.spark.executor.instances

512m

512m

512m

512m

1

1

4096m

12288m

3072m

1024m

5

4

Kyligence	Enterprise	中还加入了定制化的	Spark	参数，只影响查询时生成	Spark	执行计划的行为。在配置文件
	kylin.properties		中的默认参数如下：

Properties	Name

Default

Description

kylin.storage.columnar.spark-
conf.spark.sql.cartesianPartitionNumThreshold

-1

以	 	kylin.engine.spark-conf		开头的参数：

Spark	执行计划中	Cartesian	Partition	的数量阈值。达
到或超过阈值后，此条查询便会中断。如果该值为空
或负数，则将	spark.executor.cores
spark.executor.instances	100	的计算结果作为该熔断阈
值。

该类配置项后半部分为在	Kyligence	Enterprise	中构建任务使用的	Spark	参数，默认不做配置参数，系统会在构建任务时
根据集群环境信息自动调整参数。如果您在	 	kylin.properties		中配置了这些参数，则会优先使用	 	kylin.properties		中
的配置。

kylin.engine.spark-conf.spark.executor.instances

kylin.engine.spark-conf.spark.executor.cores

kylin.engine.spark-conf.spark.executor.memory

kylin.engine.spark-conf.spark.executor.memoryOverhead

kylin.engine.spark-conf.spark.sql.shuffle.partitions

kylin.engine.spark-conf.spark.driver.memory

kylin.engine.spark-conf.spark.driver.memoryOverhead

kylin.engine.spark-conf.spark.driver.cores

如果您需要启用	Spark	RPC	通信加密，可以参考	Spark	RPC	通信加密	章节。

Spark	Context	Canary相关配置

Sparder	Canary是用来监控Sparder运行状态的组件，它会定时检查当前Sparder是否在正常运行，如果运行状态异常，比
如Sparder意外退出或者无响应，Sparder	Canary会创建新的Sparder实例。

配置项

描述

134

基本配置参数

kylin.canary.sqlcontext-
enabled

kylin.canary.sqlcontext-
threshold-to-restart-
spark

kylin.canary.sqlcontext-
period-min

kylin.canary.sqlcontext-
error-response-ms

kylin.canary.sqlcontext-
type

是否开启Sparder	Canary功能，默认是	 	false	。

当检测异常次数超过此阈值，重启spark	context

检查时间间隔，默认是	 	3		分钟

单次检测超时时间，默认是	 	3		分钟，如果单次检测超时代表spark	context无响应

检测方式，默认是	 	file		，此方法通过向 	kylin.env.hdfs-working-dir	目录写入一个
parquet文件来确认spark	context是否还在正常运行。还可以配置为	 	count		,	通过执行累
加操作来确认spark	context是否正常运行

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

135

Spark	资源动态配置

Spark	资源动态配置

Spark	中，所谓资源单位一般指的是	executors	，和	Yarn	中的	Containers	一样，在	Spark	On	Yarn	模式下，通常使用	num-
executors	来指定	Application	使用的	executors	数量，而	executor-memory	和	executor-cores	分别用来指定每个	executor	所
使用的内存和虚拟CPU核数。

以	Kyligence	Enterprise	为例，如果用户使用	Kyligence	Enterprise	的时候使用的是固定的资源分配策略，启动时候指定
num-executors	3，那么每个	Kyligence	Enterprise	instance	都会一直占用４个	YARN	的	Container（１个固定用于
application	master，3个用于	executor	），这4个资源就会一直被占用着，只有当用户退出时才会释放。但是，如果可以
将资源分配的策略设置为	Dynamic	Resource	Allocation，则	Spark	可以根据	Kyligence	Enterprise查询的负载情况，动态的
增加和减少	executors，从而大幅度节省资源。

Spark动态资源分配详细介绍请见官方文档：http://spark.apache.org/docs/2.4.1/job-scheduling.html#dynamic-resource-

allocation

Spark动态资源分配配置方法

概览

Spark	动态资源分配需要配置两处：一处是集群的资源管理器相关配置，会根据资源管理器的不同（YARN、Mesos、
Standalone）有不同的配置方式。另外，动态资源分配还需要配置	spark-default.conf	文件（在	Kyligence	Enterprise中，可
以直接配置	kylin.properties	文件，Kyligence	Enterprise	会自动转换为	spark	的配置），此处配置相对固定。

资源管理器配置

CDH

1.	 登入	Cloudera	Manager，选择	YARN	configuration，找到	NodeManager	Advanced	Configuration	Snippet	(Safety	Valve)

for	yarn-site.xml，配置如下：

<property>

					<name>yarn.nodemanager.aux-services</name>

	<value>mapreduce_shuffle,spark_shuffle</value>

				</property>

<property>

					<name>yarn.nodemanager.aux-services.spark_shuffle.class</name>

	<value>org.apache.spark.network.yarn.YarnShuffleService</value>

				</property>

1.	 将 	$KYLIN_HOME/spark/yarn/spark-<version>-yarn-shuffle.jar	文件拷贝出来，放到	Hadoop	节点的	/opt/lib/kap/	目录

下（路径可修改）。

在	Cloudera	Manager	中找到	NodeManager	Environment	Advanced	Configuration	Snippet	（Safety	Valve），配置:

	YARN_USER_CLASSPATH=/opt/lib/kap/*

则	yarn-shuffle.jar	文件会被加入	Node	Manager	启动时的	classpath	中。

2.	 保存配置并重启	在	Cloudera	Manager	中，选择	actions	-->	deploy	client	configuration，保存后，重启所有	service。

HDP

1.	 登陆	Ambari	管理页面，选择	Yarn	->	Configs	->	Advanced，通过	Filter	找到以下配置项并进行更改：

	yarn.nodemanager.aux-services.spark_shuffle.class=org.apache.spark.network.yarn.YarnShuffleService

2.	 保存配置并重启

136

Spark	资源动态配置

Kyligence	Enterprise配置

配置	Spark	动态资源分配需要在	Spark	的配置文件中添加一些配置项以开启该服务。由于在	Kyligence	Enterprise	中可以
通过在	kylin.properties	中进行配置来直接覆盖	Spark	中的配置，因此只需要在	kylin.properties	中进行如下配置：

	kylin.storage.columnar.spark-conf.spark.dynamicAllocation.enabled=true

	kylin.storage.columnar.spark-conf.spark.dynamicAllocation.maxExecutors=5

	kylin.storage.columnar.spark-conf.spark.dynamicAllocation.minExecutors=1

	kylin.storage.columnar.spark-conf.spark.shuffle.service.enabled=true

	kylin.storage.columnar.spark-conf.spark.dynamicAllocation.initialExecutors=3

更多配置项可以参考：	http://spark.apache.org/docs/latest/configuration.html#dynamic-allocation

Spark动态资源分配验证

配置完成后，启动	Kyligence	Enterprise，在	executor	页面中可以观察当前的	executor	数目。

由于	executor	处于空闲状态，因此一定时间后会被撤除，直至达到配置项中设定的最小值。

提交查询。一定时间后会观察到	executor	数目增加，但不会超过配置项中设定的最大值。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

137

Hadoop	队列配置

Hadoop	队列配置

在多租户的场景下，多位租户为了安全地共享一个大型集群，需要对计算资源进行隔离及调配。Kyligence	Enterprise	支
持对每个实例及每个项目单独设置	YARN	队列，以实现计算资源的调配隔离。

实例级	YARN	队列配置

默认情况下，Kyligence	Enterprise	的构建任务会发送到集群的	 	default		队列中。给实例配置单独的队列之前，首先需要
在	YARN	队列中添加一个新的队列。

在下面的截图中，我们创建了一个新的	YARN	队列	 	learn_kylin	。

随后，修改 	kylin.properties	，为构建或者查询任务配置需要使用的队列（YOUR_QUEUE_NAME	为您配置的	YARN
队列名称）。

构建配置：kylin.engine.spark-conf.spark.yarn.queue=YOUR_QUEUE_NAME

查询配置：kylin.storage.columnar.spark-conf.spark.yarn.queue=YOUR_QUEUE_NAME

如上图所示在本例中查询任务的	YARN	队列被改为	 	learn_kylin	。我们可以触发一个查询任务来验证队列是否已被修
改。

138

Hadoop	队列配置

在	YARN	资源管理器中，可以看到刚才触发的任务已经进入到	 	learn_kylin		队列中。

类似的，您也可以将其他实例配置到不同的	YARN	队列中以实现计算资源的隔离。

项目级	YARN	队列配置

系统管理员可以在产品	Web	UI	的设置	->	高级设置	->	YARN	资源队列中设置项目的	YARN	队列，详细方法请您参考项
目设置。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

139

查询缓存配置

查询缓存配置

为了提升执行相同查询的效率，Kyligence	Enterprise	系统自带查询缓存并默认开启。

注意：为了保障数据一致性，查询下压不会击中缓存。

使用系统默认缓存

Kyligence	Enterprise	自带查询缓存功能并默认开启，具体的缓存配置参数如下。您可以在产品安装目录
	$KYLIN_HOME/conf		下的配置文件	 	kylin.properties		中进行修改。

注意：除了查询缓存功能开关支持项目级配置之外，其他所有下述配置需要重启后方能生效。

配置项

描述

默认值

可选值

kylin.query.cache-enabled

是否开启查询缓存，当该参数开启，下述参数才生效。

true

false

查询被缓存的条件

由于内存资源可能是有限的，Kyligence	Enterprise	不会默认缓存每条查询的结果。目前产品会有选择性的对性能较慢且
结果集不是特别大的查询进行缓存。一条查询是否会被缓存，由以下几个参数影响：满足序号为	1、2、3	配置项中任意
一项，且同时满足序号	4	配置项时，查询会被缓存。

序号

配置项

描述

默认值

默认值单位

1

2

3

4

kylin.query.cache-threshold-duration

查询延迟大于该值

kylin.query.cache-threshold-scan-count

查询扫描的行数大于该值

2000

10240

毫秒

行

kylin.query.cache-threshold-scan-bytes

查询扫描的数据量大于该值

1048576

字节

kylin.query.large-query-threshold

查询结果集小于该值

1000000

单元格

Ehcache	缓存配置

Kyligence	Enterprise	默认使用	Ehcache	作为查询缓存，您可以通过配置	Ehcache	来控制查询缓存的大小和策略。您可以
通过修改以下配置项来替换默认的查询缓存配置文件，更多的	Ehcache	配置项请参考官网	ehcache文档。

配置项

描述

默认值

kylin.cache.config

ehcache.xml	文件的路径。您可以在	 	${KYLIN_HOME}/conf/		下新建
格式为	 	xml		的文件来替换默认的查询缓存配置文件，如
	ehcache2.xml	，并且修改配置项的值为：
	file://${KYLIN_HOME}/conf/ehcache2.xml	。

classpath:ehcache.xml

Redis	缓存配置

支持单机模式、集群模式、哨兵模型部署，不支持主从模式。由于	Ehcache	查询缓存是进程级的，在不同进程或不同节
点之间并不共享，因此在集群部署模式下，当后续相同查询路由至不同	Kyligence	Enterprise	节点时，一个进程查询执行
结果的缓存无法被另一个进程使用。因此，我们支持使用	Redis	集群作为分布式查询缓存，在所有	Kyligence	Enterprise
节点间共享。具体的参数和配置方法如下(推荐Redis	4.0	或	5.0	或	5.0.5)：

配置项

描述

默认值

kylin.cache.redis.enabled

是否开启	Redis	集群用于查询缓存

false

可
选
值

true

140

查询缓存配置

kylin.cache.redis.enabled

是否开启	Redis	集群用于查询缓存

kylin.cache.redis.cluster-
enabled

kylin.cache.redis.sentinel-
enabled

是否开启	Redis	集群模式

是否开启	Redis	哨兵模式

false

false

false

true

true

true

kylin.cache.redis.hosts

Redis	主机地址，单机/集群模式下，是所有节点的	IP	和
端口；哨兵模式下，为哨兵节点的	IP	和端口。多个值请
使用逗号进行分割。如
kylin.cache.redis.hosts=localhost:6379,localhost:6380

localhost:6379

kylin.cache.redis.sentinel-
master

开启	Redis	哨兵模式时生效，哨兵监控的	master	节点的名
称，需和	 	redis.conf		中的	master	名称一致

kylin.cache.redis.expire-
time-unit

kylin.cache.redis.expire-
time

Redis	缓存保留单位，EX为秒，PX为毫秒

EX

PX

Redis	缓存保留时间

86400

kylin.cache.redis.password

Redis密码

已知限制

由于当前	Query	节点与	All/Job	节点存在元数据存在同步差异，redis	缓存开关	 	kylin.cache.redis.enabled=true		需要和
	kylin.server.store-type=jdbc		一起配置。

注意：Redis密码可以明文配置，也可以加密。加密方法请参考：	使用	MySQL	作为元数据存储

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

141

HTTPS	配置

HTTPS	配置

Kyligence	Enterprise	4.x	版本起提供了	HTTPS	连接配置，该配置默认关闭，如您需要启用，请参考下述方法。

使用系统自带证书

Kyligence	Enterprise	自带	HTTPS	认证证书，如果您选择使用系统自带的证书，只需要在产品安装目录下的配置文件
	$KYLIN_HOME/conf/kylin.properties		中添加或修改以下配置：

#	开启	HTTPS	连接配置

kylin.server.https.enable=true
#	访问端口

kylin.server.https.port=7443

默认的访问端口是	 	7443	，启动产品之前请执行下述指令查看端口是否被占用。如果端口已被占用，请修改为有效的端
口号。

netstat	-tlpn	|	grep	7443

修改配置后请重启	Kyligence	Enterprise，之后访问您设定好的端口即可。例如，端口设置为	7443	时，访问地址为
	https://localhost:7443/kylin/index.html		。

注意：因为系统自带的证书是自行产生的，如果访问的时候浏览器出现安装证书存在问题的提示，请忽略。

使用其他证书

Kyligence	Enterprise	支持第三方的证书，您只需要提供生成的证书文件，并且在产品安装目录下的配置文件
	$KYLIN_HOME/conf/kylin.properties		中添加或修改以下配置：

#	开启	HTTPS	连接配置

kylin.server.https.enable=true
#	访问端口

kylin.server.https.port=7443
#	证书的格式，目前	Tomcat	8	只支持JKS，PKCS11，PKCS12这三种格式

kylin.server.https.keystore-type=JKS
#	证书文件所在的位置

kylin.server.https.keystore-file=${KYLIN_HOME}/server/.keystore
#	证书文件密码

kylin.server.https.keystore-password=changeit
#	密钥对的别名，可选配置项，如果没有则不需要设置

kylin.server.https.key-alias=tomcat

加密	kylin.server.https.keystore-password

如果需要对	kylin.server.https.keystore-password	进行加密，可以使用如下方式：

i.在 	${KYLIN_HOME}	路径下执行以下命令，获取加密后的密码

./bin/kylin.sh	io.kyligence.kap.tool.general.CryptTool	-e	AES	-s	<password>

ii.配置	kylin.server.https.keystore-password	为如下形式

kylin.server.https.keystore-password=ENC('${encrypted_password}')

142

HTTPS	配置

修改配置过后请重启	Kyligence	Enterprise，之后访问您设定好的端口即可。例如，端口设置为7443时，访问地址为
	https://localhost:7443/kylin/index.html		。

注意：如果您使用的不是系统提供的	SSL	证书，并且您将证书放在了	 	$KYLIN_HOME		下的任意位置，则您在进行
系统升级之前需要将证书备份，并且在升级之后，您需要在配置文件中重新指定证书文件的位置，所以我们推荐

您将证书放在一个独立目录下。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

143

Spark	RPC	通信加密

Spark	RPC	通信加密

Kyligence	Enterprise	支持配置与	Spark	节点间通信加密，可以提高内部通信时的安全性，防止特定的安全性攻击。

更多	Spark	RPC	通信加密详细介绍，请见Spark	Security	。

该功能默认关闭，如您需要启用，请参考下述方法进行配置。

Spark	RPC	通信加密配置

1、请参照	Spark	Security	确保	Spark	集群中已开启	RPC	通信加密。	2、在	 	$KYLIN_HOME/conf/kylin.properties		中进行以
下配置，以开启	Kyligence	Enterprise	节点和	Spark	集群通信加密

###	spark	rpc	encryption	for	build	jobs

kylin.storage.columnar.spark-conf.spark.authenticate=true

kylin.storage.columnar.spark-conf.spark.authenticate.secret=kylin

kylin.storage.columnar.spark-conf.spark.network.crypto.enabled=true

kylin.storage.columnar.spark-conf.spark.network.crypto.keyLength=256

kylin.storage.columnar.spark-conf.spark.network.crypto.keyFactoryAlgorithm=PBKDF2WithHmacSHA256

###	spark	rpc	encryption	for	query	jobs

kylin.engine.spark-conf.spark.authenticate=true

kylin.engine.spark-conf.spark.authenticate.secret=kylin

kylin.engine.spark-conf.spark.network.crypto.enabled=true

kylin.engine.spark-conf.spark.network.crypto.keyLength=256

kylin.engine.spark-conf.spark.network.crypto.keyFactoryAlgorithm=PBKDF2WithHmacSHA256

Spark	RPC	通信加密验证

配置完成后，启动	Kyligence	Enterprise，验证查询和构建任务可以正常执行即可。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

144

日志滚动配置

日志滚动配置

Kyligence	Enterprise	的日志目录	 	$KYLIN_HOME/logs/		下面的	 	shell.stderr	、	 	shell.stdout	、	 	kylin.out	、
	access_log.yyyy-MM-dd.log	四个日志文件，默认情况下定时触发日志滚动检查。

注意：所有下述配置需要重启后方能生效。

配置项

描述

默认值

kylin.env.log-rotate-enabled

是否启用 	crontab	检查日志滚动

kylin.env.log-rotate-check-cron

日志滚动检查的 	crontab	时间设置

kylin.env.max-keep-log-file-number

日志滚动保留的最大文件数量

true

33

10

kylin.env.max-keep-log-file-threshold-
mb

触发日志滚动的文件大小

256，单位为
MB

kylin.server.accesslog-max-days

access_log日志滚动保留的最大文件数
量

10

可选
值

false

默认定时滚动策略

使用定时滚动策略需要设置参数	 	kylin.env.log-rotate-enabled=true		(默认)，同时也需要确保运行	Kyligence	Enterprise
的用户可以使用	 	logrotate		和	 	crontab	命令添加定时任务。

使用定时滚动策略时，Kyligence	Enterprise	会在启动或重启时根据	 	kylin.env.log-rotate-check-cron		参数添加或更新
	crontab		任务，会在退出时移除添加的	 	crontab		任务。

已知限制

若定时滚动策略条件不满足，Kyligence	Enterprise	将只在启动时触发日志滚动检查，每次执行	 	kylin.sh	start		命
令时，根据参数	 	kylin.env.max-keep-log-file-number		和	 	kylin.env.max-keep-log-file-threshold-mb		来进行日志滚
动。若	Kyligence	Enterprise	长时间运行，则可能存在日志文件过大的情况。
使用	 	crontab		控制日志滚动时，滚动操作由	 	logrotate		命令实现，若日志文件过大，则在滚动期间可能会发生日
志的丢失。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

145

Gluten	内表参数配置

Gluten	内表参数配置

Kyligence	Enterprise	默认采用	Gluten	作为内表的下压查询引擎，分别支持	Spark	on	Yarn	和	Spark	Stand	Alone	两种计算
资源管理方式来分配查询和构建资源。对于生产环境的配置，请仔细查阅本文档并保证对应的	Gluten	参数已经正确配
置。

1.	Spark	on	Yarn	最小参数配置

1.1.	Yarn	Client	模式

Kyligence	Enterprise	的配置文件	 	kylin.properties	，该文件位于	 	$KYLIN_HOME/conf		目录下。

#	gluten	for	query

kylin.storage.columnar.spark-conf.spark.gluten.sql.columnar.backend.ch.runtime_config.storage_configuration.dis

ks.hdfs.endpoint=hdfs://olivernameservice/

#	gluten	for	build

kylin.engine.spark-conf.spark.gluten.sql.columnar.backend.ch.runtime_config.storage_configuration.disks.hdfs.en

dpoint=hdfs://olivernameservice/

1.2.	Yarn	Cluster	模式

#	gluten	for	query

kylin.storage.columnar.spark-conf.spark.gluten.sql.columnar.backend.ch.runtime_config.storage_configuration.dis

ks.hdfs.endpoint=hdfs://olivernameservice/

#	gluten	for	build

kylin.engine.spark-conf.spark.gluten.sql.columnar.libpath=libch.so

kylin.engine.spark-conf.spark.yarn.appMasterEnv.LD_PRELOAD=$PWD/libch.so

kylin.engine.spark-conf.spark.gluten.sql.columnar.backend.ch.runtime_config.storage_configuration.disks.hdfs.en

dpoint=hdfs://olivernameservice/

1.2.	Kerberos	认证

目前	Kerberos	认证仅支持在	Spark	on	Yarn	的模式下开启。

#	need	upload	keytab	file	to	yarn	container

kylin.query.engine.sparder-additional-files=${KYLIN_HOME}/conf/4xuser.keytab,${KYLIN_HOME}/server/libch.so,${KY

LIN_HOME}/server/conf/spark-executor-log4j.xml,${KYLIN_HOME}/server/conf/spark-appmaster-log4j.xml,${KYLIN_HOME

}/lib/libasyncProfiler-linux-x64.so,${KYLIN_HOME}/lib/libasyncProfiler-linux-arm64.so

#	kerberos	for	query

kylin.storage.columnar.spark-conf.spark.kerberos.keytab=${KYLIN_HOME}/conf/4xuser.keytab

kylin.storage.columnar.spark-conf.spark.kerberos.principal=4xuser@KYLIN.COM

kylin.storage.columnar.spark-conf.spark.kerberos.access.hadoopFileSystems=hdfs://olivernameservice/

kylin.storage.columnar.spark-conf.spark.gluten.sql.columnar.backend.ch.runtime_config.hdfs.hadoop_security_auth

entication=kerberos

#	kerberos	for	build

kylin.engine.spark-conf.spark.yarn.dist.files=${KYLIN_HOME}/conf/4xuser.keytab,${KYLIN_HOME}/server/libch.so

kylin.engine.spark-conf.spark.kerberos.keytab=${KYLIN_HOME}/conf/4xuser.keytab

kylin.engine.spark-conf.spark.kerberos.principal=4xuser@KYLIN.COM

kylin.engine.spark-conf.spark.kerberos.access.hadoopFileSystems=hdfs://olivernameservice/

kylin.engine.spark-conf.spark.gluten.sql.columnar.backend.ch.runtime_config.hdfs.hadoop_security_authentication

=kerberos

2.	Spark	Stand	Alone	最小参数配置

146

Gluten	内表参数配置

#	Query	on	Stand	Alone

kylin.storage.columnar.spark-conf.spark.master=spark://${SPARK_MASTER_HOST}:7077

kylin.storage.columnar.spark-conf.spark.gluten.sql.columnar.backend.ch.runtime_config.hdfs.libhdfs3_conf={path

for	hdfs-site.xml}

kylin.storage.columnar.spark-conf.spark.gluten.sql.columnar.executor.libpath={path	for	libch.so}

kylin.storage.columnar.spark-conf.spark.executorEnv.LD_PRELOAD={path	for	libch.so}

kylin.storage.columnar.spark-conf.spark.gluten.sql.columnar.backend.ch.runtime_config.reuse_disk_cache=false

kylin.storage.columnar.spark-conf.spark.gluten.sql.executor.jar.path={path	for	gluten.jar}

#	Build	on	Stand	Alone

kylin.engine.spark-conf.spark.master=spark://${SPARK_MASTER_HOST}:7077

kylin.engine.spark-conf.spark.gluten.sql.columnar.backend.ch.runtime_config.hdfs.libhdfs3_conf={path	for	hdfs-s

ite.xml}

kylin.engine.spark-conf.spark.gluten.sql.columnar.executor.libpath={path	for	libch.so}

kylin.engine.spark-conf.spark.executorEnv.LD_PRELOAD={path	for	libch.so}

kylin.engine.spark-conf.spark.gluten.sql.columnar.backend.ch.runtime_config.reuse_disk_cache=false

kylin.engine.spark-conf.spark.gluten.sql.driver.jar.path={path	for	gluten.jar}

kylin.engine.spark-conf.spark.gluten.sql.executor.jar.path={path	for	gluten.jar}

3.	gluten	配置说明

3.1.	gluten	相关文件默认路径

	libch.so		位于	 	$KYLIN_HOME/server/		， 	$SPARK_HOME/	目录下
	gluten.jar		位于	 	$KYLIN_HOME/lib/ext/	， 	$SPARK_HOME/jars/	目录下

3.2.	参数配置说明

查询和构建的	spark	配置需要分别配置，查询配置前缀为	 	kylin.storage.columnar.spark-conf		，构建配置前缀为
	kylin.engine.spark-conf	。

参数名

spark.gluten.enabled

spark.gluten.sql.columnar.libpath

spark.memory.offHeap.enabled

spark.memory.offHeap.size

默认值

true

${KYLIN_HOME}/server/libch.so

true

12g

spark.gluten.sql.columnar.backend.ch.runtime_config.storage_configuration.disks.hdfs.endpoint

spark.gluten.sql.columnar.backend.ch.runtime_config.storage_configuration.disks.hdfs.metadata_path

/tmp/ch_metadata_kylin

spark.gluten.sql.columnar.backend.ch.runtime_config.storage_configuration.disks.hdfs_cache.path

/tmp/hdfs_cache_kylin

spark.gluten.sql.columnar.backend.ch.runtime_config.storage_configuration.disks.hdfs_cache.max_size

256Gi

spark.gluten.sql.columnar.backend.ch.runtime_config.path

spark.gluten.sql.columnar.backend.ch.runtime_config.tmp_path

/tmp/gluten_default

/tmp/kyligence_glt/tmp_ch

spark.gluten.sql.columnar.backend.ch.runtime_config.use_current_directory_as_tmph

true

spark.gluten.sql.columnar.backend.ch.runtime_config.hdfs.libhdfs3_conf

/etc/hadoop/conf/hdfs-site.xml

spark.gluten.sql.columnar.executor.libpath

spark.executorEnv.LD_PRELOAD=$PWD/libch.so

libch.so

$PWD/libch.so

147

Gluten	内表参数配置

spark.gluten.sql.executor.jar.path

${KYLIN_HOME}/lib/ext/gluten.jar

spark.gluten.sql.columnar.backend.ch.runtime_config.reuse_disk_cache

spark.master

spark.kerberos.keytab

spark.kerberos.principal

spark.kerberos.access.hadoopFileSystems

false

yarn

spark.gluten.sql.columnar.backend.ch.runtime_config.hdfs.hadoop_security_authentication

NONE

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

148

升级	KE4	至	KE5

升级至	Kyligence	Enterprise	5.x

本章将介绍如何从	Kyligence	Enterprise	4.x	升级到最新的5.x版本。

在	5.x	版本中对元数据做了较大重构，因此需要对元数据进行迁移操作，数据文件无需迁移。

元数据迁移

元数据迁移分3步进行：1.	4.x	备份元数据；2.	使用	5.x	内置的工具升级元数据；3.	在	5.x	版本导入元数据。

1.	KE	4.x	备份元数据

在	KE	4.x	中执行下述命令，	 	{METADATA_BACKUP_PATH}		需要替换为备份目录,	细节可参考	元数据备份与恢复

$KYLIN_HOME/bin/metastore.sh	backup	{METADATA_BACKUP_PATH}

2.	升级元数据

前置操作

配置	KE	5.x	并确保可以正常启动,	至少需要配置	 	metadata_url	、 	zk		等参数，若元数据使用的是mysql，则同时也需要
提供mysql相关jar包。

升级操作

在	KE	5.x	中执行下述升级命令

bin/kylin.sh	org.apache.kylin.common.persistence.metadata.MigrateKEMetadataTool	{inputPath}	{outputPath}

参数说明

	input		为元数据备份到目录，绝对路径。对于	4.6.18	及之后的版本，input	路径需要包含	core_meta

	output		为元数据迁移后保存的目录，绝对路径，需要指定	file://	前缀以及	core_meta	子目录，	如
	file:///tmp/ke_meta/2021-11-26-16-20-31_kylingo/core_meta

注意：前缀中包含了两个	/，路径本身也需要以	/	开头，所以	 	file:		和	 	tmp		之间共有3个	/

3.	KE	5.x	导入元数据

在	KE	5.x	中执行下述命令导入元数据， 	{METADATA_RESTORE_PATH}		为迁移后的元数据，不需要指定特定前缀和后缀，如
	/tmp/ke_meta/2021-11-26-16-20-31_kylingo/

$KYLIN_HOME/bin/metastore.sh	restore	{METADATA_RESTORE_PATH}

兼容性

该升级工具支持	4.6.18	之前及之后的元数据，对于	4.6.18	之后的版本，可以直接使用；对于4.6.18	之前的元数据，会忽
略	4.6.18	版本中拆分出来的元数据，包括	job、async_task、queryHistoryOffset、favorite,	建议先升级至	4.6.18，再进行迁
移

注意事项

149

升级	KE4	至	KE5

元数据迁移及导入过程中，内存中可能会存在大量中间值，若遇到OOM	问题，请调整内存参数后重试

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:03

150

升级至	Kyligence	Enterprise	最新版本

升级至	Kyligence	Enterprise	5.x	最新版本

本章将介绍如何从	Kyligence	Enterprise	5.x	的早期版本升级到最新版本。	升级分为主要版本的升级和次要版本的升级。
版本号前两位发生变化的是主要版本的升级，比如从	5.1.x	升级到	5.2.x。版本号前两位不发生变化则是次要版本升级，
比如从	5.0.7	升级到	5.0.8。	次要版本升级风险较小，升级前只需备份元数据即可。主要版本升级由于变化较大，推荐在
升级前除了备份元数据之外，条件允许的话，也备份索引数据，以最大程度地保证数据安全。

注意：

为了保障生产的安全稳定，我们不建议直接在生产环境升级	Kyligence	Enterprise。我们推荐您准备一个测试
环境进行升级的测试，直到在测试环境可以稳定使用	Kyligence	Enterprise	后，才在生产环境升级。
由于涉及元数据结构变更，您暂时无法直接使用该章节中介绍的方式从	5.0.x	版本升级至	5.1.x	版本，或者从
5.1.x	版本升级至	5.2.x	版本。若您有此类升级需求，请联系	Kyligence	技术支持团队获取帮助。

升级前的准备工作

1.	 确保没有正在进行中（即等待、运行、错误和暂停）的构建任务，确保所有任务都是完成状态（即成功或者终

止）。	对于进行中的任务，您可以等待它们完成，或者终止它们。

2.	 Kyligence	Enterprise	5.x	所在节点及其运行的	Hadoop	集群中的所有节点，需要的	Java	环境是	JDK	8	(64	bit)	及以

上，您可以通过以下命令查看	JDK	版本：

java	-version

3.	 停止所有	Kyligence	Enterprise	实例，确保没有活动的	Kyligence	Enterprise	进程影响升级。

$KYLIN_HOME/bin/kylin.sh	stop

ps	-ef	|	grep	kylin

4.	 当您的环境配置了	Zookeeper	并开启	Kerberos	认证，不标准的	Kerberos	配置可能导致	Kyligence	Enterprise	构建任

务报错。	可以通过下述步骤快速验证	ZooKeeper	开启	Kerberos	后与本产品的连通性：

i.	 在部署了	ZooKeeper	Client	的节点找到	ZooKeeper	工作目录

ii.	 往	 	conf/jaas.conf	文件添加或修改	Client	section:

			Client	{

				com.sun.security.auth.module.Krb5LoginModule	required

				useKeyTab=true

				keyTab="/path/to/keytab_assigned_to_kylin"

				storeKey=true

				useTicketCache=false

				principal="principal_assigned_to_kylin";

				};

1.	 	export	JVMFLAGS="-Djava.security.auth.login.config=/path/to/jaas.conf"

2.	 	bin/zkCli.sh	-server	${kylin.env.zookeeper-connect-string}

3.	 验证能正常查看	ZooKeeper	节点，例如： 	ls	/

4.	 清理步骤	2	中新增的	Client	section	以及步骤	3	中声明的环境变量	 	unset	JVMFLAGS		如果非官网下载	ZooKeeper,	可以

咨询运维人员后进行上述操作。

数据备份

为了最大程度保障数据的安全性，在升级前必需备份元数据。另对于主要版本升级，还建议额外备份索引数据。

151

升级至	Kyligence	Enterprise	最新版本

备份元数据	您可以通过以下命令备份元数据：

$KYLIN_HOME/bin/metastore.sh	backup

备份索引数据（仅对主要版本升级）

请先确认您	HDFS	上有足够空间：

hdfs	dfs	-df	-h	/

通过以下命令确认	Kyligence	Enterprise	工作目录的大小：

提示：工作目录由配置文件	 	$KYLIN_HOME/conf/kylin.properties		中的	 	kylin.env.hdfs-working-dir		参数
指定，默认值为	 	/kylin	。

hdfs	dfs	-du	-h	/kylin

如果空间允许，请备份索引数据：

hadoop	distcp	/kylin	/kylin_temp

确认备份目录	 	/kylin_temp		与原目录大小基本相同。

升级脚本执行步骤

升级过程主要分为以下几步：

拷贝许可证文件

拷贝	 	$KYLIN_HOME/conf		目录下的配置文件
拷贝	 	$KYLIN_HOME/lib/ext		目录下的文件
拷贝原有	Kyligence	目录下的自定义目录，如您自定义的一些文件或调度脚本等

注意：该步骤会拷贝仅在原有按照路径下的目录，不包括	 	metadata_backups		， 	work		文件夹

解压并运行升级脚本

解压缩新版的	Kyligence	Enterprise	安装包:

tar	-zxvf	Kyligence-Enterprise-{version-env}.tar.gz

在解压目录中，运行升级脚本：

Usage:	upgrade.sh	<old-kylin-home>	[--silent]

<old-kylin-home>			Specify	the	old	version	of	the	Kyligence	Enterprise

																			installation	directory.	If	not	specified,	use	KYLIN_HOME	by	default.

--silent											Optional,	don't	enter	interactive	mode,	automatically	complete	the	upgrade.

解压新版本安装包。假设新版本解压路径为	 	UNPACK_HOME	，旧版本安装目录为	 	OLD_KYLIN_HOME
执行升级脚本：

$UNPACK_HOME/bin/upgrade.sh	$OLD_KYLIN_HOME

进入	“交互升级模式”，根据提示和实际情况确认指令（y/n）来完成升级。

成功后， 	OLD_KYLIN_HOME		目录首先会被删除，然后	 	UNPACK_HOME		会被重命名成	 	OLD_KYLIN_HOME	，所以
	KYLIN_HOME		不变。	注意事项：
升级模式为	“原地升级”	，即升级程序会先自动备份	 	OLD_KYLIN_HOME		并压缩为	 	OLD_KYLIN_HOME_TIMESTAMP.tar.gz	，

152

升级至	Kyligence	Enterprise	最新版本

然后原地进行升级。升级后的	 	KYLIN_HOME		不变。
升级完成后，在	 	$UNPACK_HOME/logs		下会生成升级日志，其中包含升级过程中的操作细节。
参数	 	--silent		允许升级脚本进入	“无声升级模式”，无需客户确认操作指令。建议在	Kyligence	技术支持的确认下
使用。

升级前需要先关闭Kyligence	Enterprise	和	Grafana。
如果升级失败，再次执行升级脚本前，需要先删除 	$UNPACK_HOME/logs	目录，否则将报错如下：

"Update	failed!	Please	check	if	the	install	package	path	is	the	latest	version,	or	delete	logs	folder."

验证升级后	Kyligence	Enterprise	是否正常工作

提示：

如果升级后有任何问题，请及时联系	Kyligence	技术支持以寻求帮助。
在测试期间，请不要执行垃圾清理以保证最大程度的数据安全性。

确认	Kyligence	Enterprise	Web	UI	能够正常显示、登录。

进行构建、查询等基本操作，观察是否能正常工作及耗时是否正常。	如果您升级前存在一些需要新版本修复的问
题，请升级后及时测试新版本是否解决了您的问题。

检验集成	Kyligence	Enterprise	的第三方系统是否能够成功工作，如使用	JDBC	进行查询的客户端、如调用	REST
API	进行查询的客户端、如	BI	工具等。
Kyligence	提供对数工具帮助您核对升级前后查询结果的一致性和正确性，当跨多个版本升级、或升级后的版本有
查询相关的行为变更时，建议您进行相关验证。如需使用，请联系您的服务顾问。

升级成功，清除备份文件与数据

经过测试确认过功能全部可用后，您可以删除在升级前备份的元数据、安装目录和索引	数据，以节省空间。

升级失败，回滚到之前版本

建议您在决定回滚之前，先联系	Kyligence	技术支持获取帮助。Kyligence	技术支持通常能帮您解决升级过程遇到的
常见问题。

停止并确认没有正在运行的	Kyligence	Enterprise	进程：

$KYLIN_HOME/bin/kylin.sh	stop

ps	-ef	|	grep	kylin

恢复原	Kyligence	Enterprise	安装目录，更新	 	KYLIN_HOME		环境变量：

rm	-rf	$KYLIN_HOME

tar	-zxf	$OLD_KYLIN_HOME_TIMESTAMP.tar.gz

cd	$OLD_KYLIN_HOME

export	KYLIN_HOME=`pwd`

恢复元数据

$KYLIN_HOME/bin/metastore.sh	restore	{your_backup_metadata_folder}	--after-truncate

（可选）恢复索引数据

hdfs	dfs	-rmr	/kylin

hadoop	distcp	/kylin_temp	/kylin

重新启动	Kyligence	Enterprise

153

升级至	Kyligence	Enterprise	最新版本

$KYLIN_HOME/bin/kylin.sh	start

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:03

154

卸载

卸载

在本节中，我们将为您介绍卸载	Kyligence	Enterprise	的步骤。

完整卸载	Kyligence	Enterprise	并清除所有相关数据的步骤如下：

1.	 在所有	Kyligence	Enterprise	节点上运行下述命令以停止	Kyligence	Enterprise	实例：

$KYLIN_HOME/bin/kylin.sh	stop

2.	 （可选的）数据备份

为以防万一，可以完全卸载前先备份元数据，以便在需要的时候恢复：

	$KYLIN_HOME/bin/metastore.sh	backup

提示：我们建议您在随后将元数据拷贝至更可靠的存储设备上。

3.	 请您查看	 	$KYLIN_HOME/conf/kylin.properties		配置文件以确定工作目录的名称。假设您的相应配置项为：

kylin.hdfs.working.dir=/kylin

请您运行下述命令删除工作目录：

hdfs	dfs	-rm	-r	/kylin

4.	 请您查看	 	$KYLIN_HOME/conf/kylin.properties		配置文件以确定元数据表的名称。假设您的元数据表名称为

	kylin_metadata	，相应配置项为：

kylin.metadata.url=kylin_metadata@jdbc

请您在终端运行下述命令删除元数据表：

如果您使用	PostgreSQL	作为元数据库：

配置	PostgreSQL	用户密码的环境变量，假设	PostgreSQL	的用户密码为	 	kylin	：

export	PGPASSWORD=kylin

执行下述命令以删除元数据表：

/usr/pgsql-10/bin/psql	-h	{hostname}	-p	{port}	-U	{user}	-d	{database}	-c	"drop	table	if	exists	{m

etadataUrl}"

字段含义如下：

hostname：PostgreSQL	的主机地址；
port：PostgreSQL	服务器的端口号；
user：使用	PostgreSQL	的用户名称；
database：PostgreSQL	中的元数据库名称；
metadataUrl：PostgreSQL	中的元数据表名称，在此例中为	 	kylin_metadata	。
您也可以登录	PostgreSQL，执行语句	 	drop	table	if	exists	{metadataUrl}		直接删除元数据表。

155

卸载

如果您使用	MySQL	作为元数据库，执行下述命令以删除元数据表：

mysql	-h{hostname}	-u	{root}	-p{password}	-D	{database}	-e	"drop	table	if	exists	{metadataUrl}"

字段含义如下：

hostname：MySQL	的主机地址；
user：使用	MySQL	的用户名称；
password：使用	MySQL	的用户密码，请您注意	 	-p	与密码之间没有空格。
database：MySQL	中的元数据库名称；
metadataUrl：MySQL	中的元数据表名称，在此例中为	 	kylin_metadata	。

您也可以登录	MySQL，执行语句	 	drop	table	if	exists	{metadataUrl}		直接删除元数据表。

5.	 在所有	Kyligence	Enterprise	节点上运行下述命令以删除	Kyligence	Enterprise	安装：

rm	-rf	$KYLIN_HOME

至此，Kyligence	Enterprise	卸载完成。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:03

156

运维指南

系统运维

本章介绍了如何进行系统运维工作。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

157

运维概述

运维概述

作为	Kyligence	Enterprise	的运维人员，有以下基本运维职责和工作：

为了保障	Kyligence	Enterprise	服务的正常运行，运维人员可以对	Kyligence	Enterprise	的日志进行监控，确保进程的
稳定运行。

为了确保构建任务的正常，运维人员可以使用邮件通知或	Web	UI	的监控页面对任务进行监控。
为了确保	Kyligence	Enterprise	对集群资源的正常使用，运维人员需要经常查看	YARN	上	Spark	任务队列的闲忙程
度，以及	HDFS	的存储情况。
为了避免由于环境因素造成的数据丢失或系统崩溃，运维人员应该做好数据备份及灾难恢复的计划。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

158

许可证容量

许可证容量

为保证	Kyligence	Enterprise	系统健康，请留意许可证容量，并始终保持系统在许可证容量的范围内运行。可以将鼠标悬
停在任一页面的顶部状态栏服务状态处，随时了解当前系统的使用情况。

服务状态

许可证包含以下容量控制：

已使用数据量：系统中已加载的数据量。

已使用节点：系统中同时运行的服务进程数。

容量计算有以下几种状态：

正常：系统在容量范围内运行，一切正常。

超额：加载数据量或者活跃进程数超过许可证上限。此时，系统将不能继续加载新数据，无法启动任何增量构建任

务，而查询则不受影响。这时常用的处理方法有：

若是数据量超额，可以通过删除	Segment	的方法清理掉一些历史数据，从而降低加载数据量，让系统恢复正
常。

若是节点数超额，可以停止一些	Kyligence	Enterprise	服务进程，让系统恢复正常。
您也可以联系	Kyligence	销售，扩容许可证容量。

获取失败	：个别情况下，系统有可能在计算数据容量时因无法访问源数据系统而处于“获取失败”状态。通常，系统
可以在下一次计算容量时自行恢复。若长时间无法恢复，请及时联系	Kyligence	技术支持，避免系统出现更多异常
而无法使用。

注意：

当从低版本升级至	4.2	版本后，包含维度表项目的容量会显示为获取失败，此时您需要在该类项目下，对于包含
维度表的模型进行一次构建或者刷新	Segment	操作即可恢复容量计算。

如果同一维度表在不同模型下被多次使用，只需要刷新其中一个模型下的任一	Segment	即可。

点击顶部状态栏中的系统管理，接着点击左侧导航栏中系统容量	，可以查看许可证容量的详情，并按项目和表查看数据
量明细。在项目级数据量明细中，还可以筛选并修复状态为获取失败的项目。

159

许可证容量

系统容量页面

数据容量的计算和规划

已使用数据量指已经载入	Kyligence	Enterprise	的数据量。遵循以下规则计算：

只计算加载到系统中且参与到索引索引构建的列的大小。

以解压后的文本形态计算数据量，避免不同压缩算法引入的不确定性。

在一个项目中，一张表即使参与多个模型也只计算一次。在不同的项目中，一张表将根据使用情况被多次计算。

为了作容量规划，常常需要估算将来系统的数据用量。下面以样例数据集为例，介绍一种简便的估算方法，只需将数据

导出为文本形态，观察其大小即可。

事实表的容量估算

先大致确定事实表中将会载入系统的列，应包含所有的维度和度量。例如完整的事实表可能有	100	列，但将会载入
系统用作分析的也许只有	30	列，则下面只需计算这	30	列。导出一段时间的数据到文本文件，获得其解压缩后的文
本形态的数据大小。

以	SSB.LINEORDER	表为例，可以运行如下	Hive	命令估算其载入系统后的容量。

hive	-f	export_fact.sql	>	export_fact.out

其中	 	export_fact.sql		文件的内容为：

SELECT

		LO_ORDERKEY

		,LO_CUSTKEY

		,LO_PARTKEY

		,LO_SUPPKEY

		,LO_ORDERDATE

		,LO_ORDERPRIOTITY

		,LO_SHIPPRIOTITY

		,LO_LINENUMBER

		,LO_QUANTITY

		,LO_EXTENDEDPRICE

160

许可证容量

		,LO_ORDTOTALPRICE

		,LO_DISCOUNT

		,LO_REVENUE

		,LO_SUPPLYCOST

		,LO_TAX

		,LO_COMMITDATE

		,LO_SHIPMODE

FROM

		SSB.LINEORDER

WHERE

		LO_ORDERDATE>='1992-02-01'	and	LO_ORDERDATE<'1993-02-01'

;

导出的	 	export_fact.out		的字节大小即为其载入系统后的容量的一个估算。

wc	--bytes	export_fact.out

对于较大的事实表，建议只导出一小段时间的数据，再作乘法估算整体数据量。

维度表的容量估算

相对庞大的事实表而言，维度表通常很小且内容稳定，在估算时可以考虑忽略不计。

如果确要计算维度表，可以将整表导出为文本形态，观察其大小。

以	SSB	数据集中的四张维度表为例，可以运行如下	Hive	命令估算维度表载入系统后的容量。

hive	-f	export_lookup.sql	>	export_lookup.out

其中	 	export_lookup.sql		文件的内容为：

SELECT	*	FROM	SSB.CUSTOMER;

SELECT	*	FROM	SSB.SUPPLIER;

SELECT	*	FROM	SSB.DATES;

SELECT	*	FROM	SSB.PART;

导出的	 	export_lookup.out		的字节大小即为上述维度表载入系统后的容量的一个估算。

wc	--bytes	export_lookup.out

最后，加总所有事实表和维度表的估算即得完整的容量估算结果。通常，如果估算得比较保守，比如事实表上导出了足

够多的列，维度表导出了整表，那么真实加载后的数据量应当略小于上述的估算结果。

容量告警

系统支持当集群容量使用率超过指定阈值时，发送通知邮件。

如需开启容量超额邮件告警功能，需要在系统配置文件	kylin.properties	中配置如下内容：

#	邮件告警总开关

kylin.job.notification-enabled=true
#	容量告警开关

kylin.capacity.notification-enabled=true
#	使用	SSL	方式

kylin.job.notification-mail-enable-starttls=true
#	邮件服务器地址

kylin.job.notification-mail-host=example.com
#	邮件服务器端口

kylin.job.notification-mail-port=587

161

许可证容量

#	邮箱用户

kylin.job.notification-mail-username=user
#	邮箱密码

kylin.job.notification-mail-password=123456
#	发件人

kylin.job.notification-mail-sender=user@example.com
#	收件人，支持多个收件人，逗号隔开

kylin.capacity.notification-emails=user@example.com
#	容量告警阈值，数字表示，示例：填写阈值80，则在超过80%时告警

kylin.capacity.over-capacity-threshold=80

邮件告警机制：

在首次超过阈值时发送告警邮件，超过之后不重复发送

超过阈值之后容量恢复到阈值以下，再次触发超过阈值，会重新发送告警邮件

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

162

容量计费

容量计费

Kyligence	Enterprise	中计费的容量是载入	KE	系统中的数据的原始文本大小，即载入	KE	模型中的事实表、维度表或者
维度表快照的行和列所对应的非压缩的文本形态的字节大小。

容量计费的原则

1.	 一个项目的容量等于，该项目下所有去重后的数据表的容量之和。

2.	 当某张表在一个项目中使用多次时，按照容量最大的那一次使用进行计费。

3.	 总的容量等于，所有项目的容量的和。

容量计费的计算方法

1.	符号说明

N：平表的行数，平表的概念请参考	基本模型设计	章节。

n：平表采样的行数。

v_f：事实表采样的容量，通过采样计算出来。

V_f：事实表的估算容量，通过事实表每	n	行占用	v_f	的单位容量估算出来。

v_d：维度表采样的容量，通过采样计算出来。

V_d：维度表的估算容量，通过维度表每	n	行占用	v_d	的单位容量估算出来。

V_d_r:	维度表快照的真实容量。

N_d：总的维度表行数。

2.	计算平表行数：

计算平表的行数为	N	行。

3.	计算事实表容量

3.1	事实表采样：从平表采样	n	行，其容量为	v_f。平表的行数和容量相关信息，请参考	许可证容量	章节。

3.2	估算事实表容量：V_f	=	v_f	/	n	*	N。

4.	计算维度表容量

4.1	若维度表开启了快照，直接采用快照容量，作为维度表容量：V_d	=	V_d_r。

4.2	若维度表没有开启快照，维度表的容量通过采用估算，与事实表容量计算方法一致。

4.2.1	维度表采样：从平表采样	n	行，其容量为	v_d，计算的是平表中使用到的维度表中的列。

4.2.2	估算维度表容量：V_d	=	v_d	/	n	*	N_d。

5.	计算单个项目计费容量

单个项目计费容量	=	Sum(项目内所有事实表	V_f)	+	Sum(项目所有维度表	V_d)。

163

容量计费

6.	系统计费容量

系统计费容量	=	Sum(系统内所有的单个项目计费容量)。

注意点

1.	 事实表与维度表为	1:m	或者	m:n	时，平表会出现数据膨胀导致容量超算。此时仍然使用上述的方法计算，多算的部

分，根据数据膨胀的倍数，给予折扣。

2.	 可计算列的容量计费是按引用的原始列，而不是结果列进行计算。

3.	 在一个项目中，同一张表用于多个模型的，容量不会被重复计算；在不同的项目中，同一张表多次使用会被多次计

算。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

164

项目运维

项目运维

本节介绍了如何进行项目运维工作。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

165

项目首页

项目首页

Kyligence	Enterprise	首页信息丰富。进入首页后您可以获得当前项目的数据源、查询历史、数据模型等基本信息，也可
以通过它提供的功能模块迅速切换到查看数据特征、执行查询语句以及连接第三方	BI	工具。此外，首页还包含了
Kyligence	Enterprise	4.x	起提供的智能推荐能力。

Kyligence	Enterprise	4.x	起系统配备了	AI	增强引擎（即智能推荐），但新建项目时该模式是默认关闭的，因此首页如下
图所示。此时，如果您点击开启智能推荐，AI	增强引擎会被激活，从而您可以以一种更智能的方式去优化已经存在的
模型或者创建新的模型。

关闭智能推荐的首页

开启智能推荐之后，首页如下图所示。此时，您可以查看到模式、规则、优化建议等信息。当系统存在尚未优化的查询

历史，点击智能推荐就可以生成新的优化建议。待优化任务执行完毕，数据资产模块会生成一个	NEW	标签以及显示待
接受的优化建议数量。当您点击了查看这个按钮后再重新回到首页，数据资产模块的	NEW	标签会消失。如果所有的查
询已经被优化，那么按钮智能推荐不可用。此外，还可以使用高级模式这个功能去导入指定的查询以创建新模型或生成

优化建议。

166

项目首页

开启智能推荐的首页

接下来，我们将详细介绍主页的每个模块的具体内容。

AI	增强引擎
数据源

查询历史

数据特征

数据资产

快速查询

连接	BI

AI	增强引擎

AI	增强引擎是	Kyligence	Enterprise	4.x	新增的一个重要特性。通过使用	AI	增强引擎，您可以更方便的创建模型，更智
能地优化一个已经存在的模型。开启智能模式后，您可以看到模式、规则、以及优化建议的信息，点击高级模式您可以

使用	SQL	建模的能力去创建模型或者优化模型。更详细的概念与原理请请参考智能推荐章节。

模式会告知您系统已学习并生成了多少个优化建议模式，这些优化建议的模式可以分为两大类：新增索引的模式和

删除索引的模式。

规则用于配置优化建议的生成规则，它用于筛选哪些	SQL	可以被优化以及设定每次推荐给用户多少条新增索引的
优化建议。

优化建议会告诉您系统累计接受的优化建议数量，包括具体有多少条新增索引建议，多少条删除索引建议。

数据源

数据源模块为您提供了当前项目加载了多少个数据库，多少张源表。通过点击管理，您可以直接跳转到数据源页面，执

行诸如加载数据源表、表采样、重载等操作。

查询历史

167

项目首页

查询历史模块为您统计了在过去一周执行的查询数量（并不包含当天的查询历史数据）。点击查看，您可以快速的跳转

到查询历史页面。

数据特征

数据特征模块为您查看表的采样信息提供了快速跳转的能力。

数据资产

数据资产模块汇总了当前项目中的模型数量以及所有模型的建议总量。点击查看，您可以快速的跳转到模型页面。

快速查询

快速查询模块为您执行查询提供了快速的跳转能力。

连接	BI

连接	BI模块可链接到手册中关于连接第三方	BI	工具的章节。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

168

工具栏

工具栏

Kyligence	Enterprise	的顶部工具栏如下图所示。

工具栏

顶部工具栏的信息包括：

项目下拉列表

存储配额

服务状态

系统管理

帮助

中英文切换

用户信息

项目下拉列表

项目下拉列表位于工具栏的左侧，显示的内容是当前项目。如果	Kyligence	Enterprise	是初次安装启动，那么项目下拉列
表为空。列表的左侧的图标可以用于展开和收起导航栏，列表的右侧图标	 	+		用于创建新的的项目，新创建的项目会被
默认设置为当前项目。

存储配额

从	4.6.3.0	版本开始，该功能默认关闭，可通过配置系统级参数 	kylin.storage.check-quota-enabled	为 	true	打开此功
能。当打开时，单击存储配额，页面将浮现下图所示的提示信息：

169

工具栏

存储配额

已使用：该项目已使用的存储配额比例，括号中的数值分别表示已使用的存储配额和已分配的存储配额。其中，存

储配额默认为	10	TB，如需调整，请参见项目配置。

存储的数据主要包含构建好的模型和索引数据、构建任务的输出、字典文件等。更多介绍，见容量计费。

低效存储：在设定的时间窗口内查询频率较低的索引，默认情况下，如果索引在过去	1	个月内的查询频率低于	5
次，则被定义为低效存储。如需调整，请参见项目配置。

[!NOTE]

您可以手动清理低效存储（开启	AI	增强模式下），也可以设置定时清理（如	AI	增强模式未开启），更多介
绍，见垃圾清理。

服务状态

点击服务状态的绿色图标会有如下图所示的提示框。图中第一行显示的是系统当前时间。第二行显示的是已使用数据量

的百分比。第三行显示的是当前使用的节点信息，右边的图标	 	>		可以展开查看到具体的节点详细信息。

服务状态

系统管理

系统管理员登录	Kyligence	Enterprise	后，点击顶栏的系统管理按钮，进入系统管理页面，详细介绍请参考项目管理章
节。

帮助

帮助可以链接到	Kyligence	Enterprise	手册、Kyligence	支持中心、更新许可证以及关于	Kyligence	Enterprise。

中英文切换

中英文切换按钮方便您根据需要查看不同语言的页面。

170

工具栏

用户信息

最右边展示的是当前的登录用户信息，点击可以修改密码以及注销。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

171

管理项目

管理项目

本章将介绍什么是项目以及如何管理项目。

关于项目

项目是	Kyligence	Enterprise	的一级管理单位。在一个项目中，您可以设计多个模型并进行查询分析。由于系统设置在项
目级别进行隔离，您可以对不同的项目设置不同的运维偏好。

管理项目

系统管理员登录	Kyligence	Enterprise	后，点击顶栏的系统管理按钮，进入系统管理页面，点击左侧导航栏项目标签进入
项目管理页面。

注意：如果没有项目存在，则不能进入系统管理页面，您可以在产品主页添加项目后再进入系统管理页面。

在项目管理页面，系统管理员可以在项目列表中查看项目的信息，还可以添加项目、删除项目、备份项目、授予其他用

户项目级别访问权限。

项目列表

添加项目

系统管理员有两种方法可以添加新项目：

在系统管理	->	项目管理页面，点击项目列表上方的	+	项目按钮

在产品主页，点击顶部工具栏左侧的	+（添加项目）按钮

在弹窗中填写项目名称和项目描述。其中项目名称为必需填写项，项目描述为选择填写项。建议您填写项目描述，这有

助于项目的日后维护。

172

管理项目

添加项目

注意：	项目名是不区分大小写的,	所以不能和已有的项目名重复。

删除项目

在项目管理页面，选择要删除的项目，点击右侧操作栏下的...(更多操作）图标按钮，选择删除。

系统管理员可以在弹出窗口中确认删除项目，项目被删除后将不能恢复，且相关的数据会被清除。

如果项目中有运行、等待、暂停状态的任务，需要先终止任务，才可以删除项目。

更改项目所有者

在项目管理页面，选择要更改所有者的项目，点击右侧操作栏下的...(更多操作），选择变更所有者。仅系统管理员具有
更改项目所有者的权限。

授予用户项目级别访问权限

在项目管理页面，选择要授权的项目，点击右侧操作栏下的授权图标按钮，进行项目的权限设置。您可以在项目级别访

问权限了解详细方法。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

173

项目设置

项目配置

在界面左侧导航栏中，点击设置，您可以根据业务需求在项目级别修改相关配置。

项目配置

所有配置大致分为三部分：

基本设置

高级设置

重写模型/索引组设置

基本设置

1.	通用信息

在这部分您能查看当前项目名称，项目类型，智能推荐模式开关，项目描述，以及您可以修改项目描述。

174

项目设置

通用信息

2.	存储设置

从	4.6.3.0	版本开始，该功能默认关闭，可通过配置系统级参数 	kylin.storage.check-quota-enabled	为 	true	打开此功
能。当打开时，在这部分您能查看当前项目的存储配额，也就是存储的上限，默认为10TB。

下图所示是存储设置所在的位置：

存储设置

3.	索引优化

在这部分您能设置低效存储，默认每个月查询频次低于	0	的加速查询和索引会被认为是低效存储，低效存储的定义请参
考工具栏。

低效存储的时间窗口可以选择是天，周，月

175

项目设置

低效存储

4.	查询下压

当您没有任何能够回答查询的模型，或者当您需要执行定制的模型无法满足查询时，可以使用查询下压，将该查询下压

至	Spark	SQL，从而在查询中获取更灵活的使用体验。默认该配置是开启的。下图是配置查询下压的位置。

查询下压

5.	Segment	设置

在这部分是和	Segment	相关的设置，包含	Segment	合并、留存阈值、支持创建保留	Segment。

Segment	合并是指系统在检测到足够数量的	Segment	且这些	Segment	包含的索引一致时，将自动合并	Segment。以下为
两个参数的设置方法：

自动合并：您可以选择自动合并时间范围为	1	小时	/	1	天	/	1	周	/	1月	/	1	季度	/	1	年（均为自然概念）	的	Segment。

176

项目设置

自然概念举例：自然周表示周一至周日。自然月表示某月第一天至该月最后一天。自然年表示某年第一天至该	年
最后一天。

变动范围：系统延迟一段时间（即变动范围）后，才会触发自动合并	Segment。您可以设置变动范围	为	N	小时	/	天
/	周	/	月	/	季度	/	年（均为自然概念），N	为整数，默认为	0.

使用场景：在实际业务中，由于	ETL	过程的延迟，例如业务常常需要每天刷新过去	N	天的数据。在自动合并
时，为了减少资源浪费，通过设置变动范围，阻止系统自动合并过去	N	天	待刷新的	Segment。
示例：	每天生成	1	个	Segment	且自动合并范围为	1	周时，过去	1	周一共有	编号	01-07	共	7	个	Segment，

变动范围为	0	天，系统将自动合并	01-07	Segment；
变动范围为	1	天（表示业务需要在次日刷新编号	07	Segment），因此系统将不会合并	01-07	Segment；
在第	2	周开始，新增编号	08	的	Segment	后，系统才会合并	01-07	Segment。
变动范围为	2	天（表示业务需要在次日刷新编号	06-07	Segment），因此系统将不会合并	01-07
Segment；	在第	2	周开始，新增编号	08-09	这	2	个	Segment	后，系统才会合并	01-07	Segment。

留存阈值，在	Kyligence	Enterprise	中最大的保存	Segment	的时间范围，支持设置天、月、年为单位。如留存阀值为	1
年，则	1	年之前的	Segment	将会被自动移除。

支持创建保留	Segment，该选项开启后，您可以在	Segment	列表页面直接创建一个不包含任何索引的	Segment	(保留
Segment)。请注意，查询命中保留	Segment	时将会通过下压查询回答。

您可以根据查询场景选择是否创建保留	Segment，创建保留	Segment	可以帮助系统判断模型中索引数据的完整性，同时
也提供给用户控制查询行为的方式。

查询场景举例：若您在查询时，指定了开放性的时间范围（where	datatime	>	'2000')	或不加时间范围，此时系统难
以判断模型是否满足索引数据完整性。当此时的	Kyligence	Enterprise	中索引在	2000-2001，2001-2002	的时间范围
内已构建完整，而	Hive	中还存在	2002-2003	的数据，对于同一条查询（where	datatime	>	'2000')	，在	Kyligence
Enterprise	中查询击中的索引仅返回	2000-2002	的数据，而下压至	Hive	将会存在	2002-2003	的数据。因此，您可
以在	2002-2003	的数据在	Kyligence	Enterprise	完成构建之前，先创建	2002-2003	的保留	segment，再进行查询，这
样就可以得到查询下压后的完整的查询结果。

下图所示为	Segment	设置的示例界面。

Segment	设置

6.	优化建议规则

您可以自定义优化建议规则，系统将按照定义的规则筛选历史查询，并根据筛选出的历史查询生成优化建议。对于不满

足规则的查询，系统将不对其进行智能推荐。

177

项目设置

点击左侧导航栏中的设置	，在基本设置页面中您可以找到优化建议偏好设置。系统支持对查询用户和查询延迟进行规则
开关和设置，规则之间是或的关系，即查询只要匹配任意一个规则，系统就会考虑对其进行智能推荐。同时您可设置可

见的新增索引优化建议上限。

优化建议规则

详细介绍及设置方法，见设置优化建议的生成规则。

高级设置

本模块包含	5	部分的设置：默认数据库，任务提醒，	YARN	资源队列、暴露可计算列和自定义项目配置。

1.	默认数据库

在使用	SQL	查询时，如果查询的表在默认数据库下，则	SQL	查询语句中的表名前可以不加数据库名。建议不要修改默
认数据库，修改后可能会导致历史	SQL	语句无法使用和无法击中模型。

下图是默认数据库所在的位置：

178

项目设置

默认数据库

2.	任务提醒

当您想要第一时间收到任务的信息，您可以在任务提醒模块设置您的邮箱地址并指定需要收到邮件的任务状态。一旦有

加载了空数据或是有指定状态的任务，系统都会给您发送邮件提醒，邮件样式如下图所示：

任务提醒

具体配置请参考	任务报警

3.	YARN	资源队列

系统管理员可以设置项目的	YARN	队列，该队列资源用于刷新数据、合并数据、构建索引、加载数据、抽样表数据等
非查询类任务。系统默认将任务提交至	YARN	的	default	队列。YARN	队列名对大小写敏感，请务必保证所设置的队列
是可用的，否则	YARN	会依据当前的	Scheduler	Policy	做出判断，任务可能会执行失败或者被提交至	default	队列。

下图是	YARN	资源队列所在的位置：

179

项目设置

4.	暴露可计算列

YARN	资源队列

管理员可以通过该配置项控制当前项目的可计算列暴露与否。当该配置开启时，Kyligence	Enterprise	将会在返回的表结
构中展示当前项目中定义的可计算列，反之则隐藏可计算列。该配置会影响你通过JDBC，ODBC，或者BI	工具看到的
表结构，因此不建议频繁改动该配置。

在AI	增强模式中，该选项默认开启。

项目暴露可计算列

5.	自定义项目配置

管理员可通过自定义项目配置，添加额外需要的项目配置项。您可以点击	+	配置按钮，在弹窗中输入配置项及参数值，
然后点击确定。如果需要修改或删除已经添加的配置项，您可以点击列表右侧的编辑或删除按钮。以上操作即时生效。

自定义项目配置

重写模型设置

目前本产品支持在模型级别重写特定的配置项，包括自动合并、变动范围、留存设置、spark	executor	资源大小，以及其
他自定义设置。

点击模型列表最右边的操作下的+（添加重写设置项）按钮：

180

项目设置

模型复写

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

181

任务报警

任务报警

Kyligence	Enterprise	提供了邮件通知的功能，可以在构建数据为空或者指定任务状态时，向运维人员发送电子邮件，便
于进行下一步的故障排查或者增量构建。

通过电子邮件实现任务报警的操作步骤如下：

步骤一：在配置文件	 	$KYLIN_HOME/conf/kylin.properties		中进行如下设置：

kylin.job.notification-enabled=true	#	设置为true将开启邮件通知功能

kylin.job.notification-mail-enable-starttls=true
kylin.job.notification-mail-host=outlook.office365.com	#	设置该项为邮件的SMTP服务器地址
kylin.job.notification-mail-username=xxx@kyligence.io	#	设置该项为邮件的SMTP登录用户名
kylin.job.notification-mail-password=xxxxx	#	设置该项为邮件的SMTP登录密码
kylin.job.notification-mail-sender=xxxx@kyligence.io	#设置该项为邮件的发送邮箱地址

提示：	kylin.job.notification-mail-password	配置支持加密，可以使用如下方式将其加密

i.	在 	${KYLIN_HOME}	路径下执行以下命令，获取加密后的密码

	./bin/kylin.sh	io.kyligence.kap.tool.general.CryptTool	-e	AES	-s	<password>

ii.	配置	kylin.job.notification-mail-password	为如下形式

		kylin.job.notification-mail-password=ENC('${encrypted_password}')

设置完毕后，重新启动	Kyligence	Enterprise	使配置生效。

步骤二：在项目配置页面进行如下设置：

将需要被通知人员的电子邮箱地址填入项目设置页面的	高级设置	-->	邮件提醒，如下图所示：

任务提醒

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

182

访问控制

访问控制

本章主要介绍了	Kyligence	Enterprise	如何保证安全，以及如何对用户及用户组进行权限管理并实现多粒度的安全控制：

管理用户

管理用户组

管理数据访问控制

数据权限

项目级别访问权限

表列行级访问权限

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

183

管理用户

管理用户

本章将介绍什么是用户以及如何管理用户。

关于用户

所有使用	Kyligence	Enterprise	的用户都需要使用账号和对应密码登录。Kyligence	Enterprise	实例中的每个用户是唯一
的，即不需要在同一实例的不同项目上反复创建同一个用户。	Kyligence	Enterprise	默认会初始化一个用户	 	ADMIN	。用
户	 	ADMIN		是内置的系统管理员，系统管理员拥有整个系统的所有权限。

管理用户

系统管理员登录	Kyligence	Enterprise	后，点击顶栏的	系统管理	按钮，进入系统管理页面，点击左侧导航栏	用户	标签进
入用户管理页面。

注意：

1.	 除系统管理员以外，仅创建用户并不能让用户获得任何项目上的访问权限。
2.	 除系统管理员以外，其他用户需要在项目级别被赋予访问权限才能使用项目上的功能。

添加用户

在用户管理页面，系统管理员可以点击	+	用户	按钮来增加新用户。在弹出窗口中，输入用户名，密码，确认密码，选
择用户角色是系统管理员还是普通用户，点击确定。

tips:	用户名是不区分大小写的,	所以不能和已有的用户名重复。

编辑用户角色

在用户管理页面，选择要修改角色的用户，点击右侧操作栏下的	…（更多操作）图标按钮。然后在下拉选择框中点击编
辑角色。

在弹出窗口中，系统管理员可以选择修改用户角色。角色分为系统管理员和普通用户。

删除用户

在用户管理页面，选择要删除的用户，点击右侧操作栏下的	…（更多操作）图标按钮。然后在下拉选择框中点击	删
除，

系统管理员可以弹出窗口中确认删除用户，用户被删除后将不能恢复，删除用户将删除用户在所有项目上的访问权限。

启用/禁用用户

在用户管理页面，选择要启用	/	禁用的用户，点击右侧操作栏下的	…（更多操作）图标按钮。然后在下拉选择框中点击
启用	/	禁用，用户状态对应为	ENABLED	/	DISABLED。

系统管理员可以启用或禁用用户，用户被禁用后将不可再登录系统。

ADMIN	用户重置密码

在用户管理页面，选择要进行密码重置的用户，点击右侧操作栏下的	重置密码	图标按钮。

在弹出窗口中，系统管理员可以更改密码，需重复输入两次新密码。

184

管理用户

初始的	ADMIN	账户密码在首次登陆后，需要被修改。如需重置密码，执行如下命令：

$KYLIN_HOME/bin/admin-tool.sh	admin-password-reset

执行成功后，	ADMIN	账户将重新生成随机密码并显示在控制台，当您登录时需要修改密码，其他账户密码将保持不
变。当配置参数	 	kylin.metadata.random-admin-password.enabled=false		时，将不会生成随机密码，默认密码为
	KYLIN	。如果要把	 	kylin.metadata.random-admin-password.enabled		的参数值从	 	false		改成	 	true		之后，需要将
Kyligence	Enterprise	节点全部重启之后，重置	ADMIN	账号得密码时，才能生成随机密码并展示在控制台。

Kyligence	Manager	最佳实践

如果您通过	Kyligence	Manager	管理	Kyligence	Enterprise	集群，建议为该集群单独设置一个共用的	Kyligence
Enterprise	系统管理员用户（避免使用初始	ADMIN	账户），密码尽量不修改，专用于	Kyligence	Manager	连接并操
作	Kyligence	Enterprise。

若您已使用了初始	ADMIN	账户（请检查	Kyligence	Manager	中的	 	kyligence.manager.kylin.username		值），在
Kyligence	Enterprise	侧重置了密码，请立即到	Kyligence	Manager	更新	 	kyligence.manager.kylin.password		值，重启
Kyligence	Manager；若未在	Kyligence	Manager	更新密码，登录	Kyligence	Enterprise	的	ADMIN	账户会被频繁锁住，
无法登录。	请参考	Kyligence	Enterprise	相关的配置。

普通用户重置密码

点击界面右上方的	<用户名>	-->	设置。

在弹出窗口中，用户可以重置密码，需要提供旧密码并重复输入两次新密码。

对用户分组

如果要将某个用户分配到特定组，执行以下操作：

1.	 在用户管理页面，选择要进行分组的用户。
2.	 点击右侧操作栏下的	分配到用户组	图标按钮。
3.	 在	可选用户组	中勾选需要将用户分配到的组，点击向右箭头（	>	）	，该组将进入	已选用户组。
4.	 点击	确定，用户将进入选定的组中。

修改用户组

如果要修改用户所在的组，执行以下操作：

1.	 在用户管理页面，选择要修改分组的用户。
2.	 点击右侧操作栏下的	分配到用户组	图标按钮。
3.	 在	已选用户组	中勾选需要将用户分配到的组，点击向左箭头（	<	）	，该组将进入	可选用户组。
4.	 点击	确定，用户将从选定的组中移出。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

185

管理用户组

管理用户组

本章将介绍什么是用户组以及如何管理用户组。

关于用户组

用户组是一组用户的集合，用户组中的用户通过用户组共享相同的访问权限。Kyligence	Enterprise	默认会初始化四个用
户组，对应名称为	ALL_USERS、ROLE_ADMIN、ROLE_ANALYST	和	ROLE_MODELER，其中	ALL_USERS	组是一
个默认的用户组，用户被创建后，即进入该组，也就是说，所有用户都包含在	ALL_USERS	用户组中。ALL_USERS	和
ROLE_ADMIN	用户组不能被修改或删除。系统管理员可以对除	ALL_USERS	以外的其他组进行批量添加或删除用户，
也可以将某个用户添加到除	ALL_USERS	以外的多个组中。用户组在整个	Kyligence	Enterprise	实例中不能重名。

关于用户组权限

系统管理员可以对用户组赋予项目级权限。在对用户组赋予项目级权限时，用户组中的用户会继承所属组的相应权限。

当某用户属于多个用户组时，该用户同时具有从不同用户组赋予的项目级权限。

管理用户组

系统管理员登录	Kyligence	Enterprise	后，点击顶栏的	系统管理	按钮，进入系统管理页面，点击左侧导航栏	用户组	标签
进入用户组管理页面。

创建用户组

在用户组管理页面，系统管理员可以点击	+	用户组	按钮来添加新组。

在弹出窗口中，系统管理员可以输入组名，点击确定。

删除用户组

在用户组管理页面，选择要删除的用户组，点击右侧操作栏下的	删除	图形按钮。

系统管理员可以弹出窗口中确认删除用户组，用户组被删除后将不能恢复，删除用户组后，用户组内的所有用户不会被

删除，但所有赋予该用户组的权限将被删除。

为组分配用户

1.	 在用户组管理页面，选择要分配用户的组。
2.	 点击右侧操作栏下的分配用户图形按钮。
3.	 在弹出窗口的未分配的用户中，勾选需要分配到该组的用户，点击向右箭头（	>	)，该用户将进入已分配组用户。
4.	 点击确定，用户将分配到该组。

修改用户所在组

参见本章管理用户。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

186

数据访问控制

管理数据访问控制

Kyligence	Enterprise	提供了丰富的企业级安全控制能力。通过为用户或用户组授予角色的方式，实现数据访问相关操作
的精细化管控。

角色级别

角色

说明

root

系统

项目

超级管理员

即初始的ADMIN账号所属角色，全局只有一个

系统管理员

由	ADMIN	创建，可以有多个

普通用户

由	ADMIN	/系统管理员创建，可以有多个

普通用户细分出	4	种角色，分别是项目管理员	、建模人员	、运维人员	、查询人员。更多请看项目级别访问权
限。

数据权限

数据权限表示有关数据资源的权限。分为：数据管理、数据查询。

数据管理权限，即：授予/收回用户的数据查询权限

1.	 管理用户数据查询的能力（从	Kyligence	Enterprise	4.5.19.0	开始）
2.	 管理用户表行列级访问能力

数据查询权限

1.	 数据查询的能力
2.	 表行列级访问的能力

如：给用户在项目中开启查询权限，用户将拥有该项目下所有库表的查询权限，如果需要限制用户访问的权限，可通过

设置行列级权限进行管控

注意：

KE	4.5.19.0	前的版本，默认所有角色自带数据查询权限；
从	KE4.5.19.0	开始，	除超级管理员	ADMIN	外，其他角色是否有查询权限，将取决于系统配置项
	kylin.security.acl.data-permission-default-enabled=true	（所有角色默认有查询权限），并可以由有数据查询权

限的角色关闭/开启数据查询权限。

详细请看数据权限。

其他

超级账号默认不受数据访问控制，拥有可以访问所有数据的权限。

系统暂时不支持模型级别的操作权限控制。``

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

187

数据访问控制

数据权限

数据权限表示有关数据资源的权限。分为：数据管理、数据查询。

数据管理权限，即：授予/收回用户的数据查询权限

1.	 管理用户数据查询的能力（从	Kyligence	Enterprise	4.5.19.0	开始）
2.	 管理用户表行列级访问能力

数据查询权限

1.	 数据查询的能力：
2.	 表行列级访问的能力

如：给用户在项目中开启查询权限，用户将拥有该项目下所有库表的查询权限，如果需要限制用户访问的权限，可通过

设置行列级权限进行管控

关闭数据查询权限

KE	4.5.19.0	前的版本，所有用户有数据查询权限。从KE	4.5.19.0	开始，可以关闭用户的数据查询权限。

已知限制：	使用实时功能加载源表时，关闭用户的数据查询权限后，用户仍然可以查看样例数据。

关闭系统管理员的数据查询权限

1.	 进入系统管理页面，选择要关闭数据查询权限的用户，点击右侧操作栏下的	…（更多操作）图标按钮。然后在下拉

选择框中点击数据权限。

2.	 在弹出窗口中，关闭开关。

关闭系统管理员的数据查询权限

关闭普通用户数据查询权限

1.	 进入系统管理	项目授权页面，选择要关闭数据查询权限的用户、用户组，关闭数据权限。

188

数据访问控制

关闭普通用户的数据查询权限

默认关闭数据权限

从	KE	4.5.19.0	开始，新增用户如需默认关闭数据查询权限，添加系统配置， 	kylin.security.acl.data-permission-
default-enabled=false

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

189

数据访问控制

项目级别访问权限

项目级别访问权限决定用户或用户组在	Kyligence	Enterprise	中能否访问一个项目。Kyligence	Enterprise	项目内有四种角
色，分别是	Project	Admin（项目管理员）、Management（建模人员）、Operation（运维人员）	和	Query（查询人
员）。

PROJECT	ADMIN（项目管理员）：默认拥有项目内的所有权限，负责对项目进行整体运维和管理以及授权等操
作。

MANAGEMENT（建模人员）：负责加载数据源、设计模型/索引、构建索引和维护任务状态。
OPERATION（运维人员）：负责构建索引，维护任务状态。
QUERY（查询人员）：需要项目中的表或者模型/索引的查询权限。

系统管理员登录	Kyligence	Enterprise	后，点击顶栏的	系统管理	按钮，进入系统管理页面，点击左侧导航栏	项目	标签进
入项目管理页面。

管理员在项目上为用户分配了角色后，用户会相应地继承数据源、模型等访问权限。表列行级的权限设置请参见表列行

级访问权限。

赋予项目访问权限

1.	 选择需要赋予权限的项目，点击右侧操作栏下的	授权	图标进入授权界面。
2.	 点击	+	用户/用户组	来为用户/用户组授予权限。
3.	 选择按	用户或	用户组	的类型授权，然后输入需要赋权的用户/用户组，选择要赋予的角色，点击	提交。

赋予项目访问权限

修改项目访问权限

1.	 选择需要修改权限的项目，点击右侧操作栏下的	授权	图标进入授权界面。
2.	 在列表中选择用户/用户组，然后点击右侧操作栏下的	编辑	图标按钮。
3.	 修改用户/用户组的访问权限后点击	提交。

删除项目访问权限

190

数据访问控制

1.	 选择需要删除权限的项目，点击右侧操作栏下的	授权	图标进入授权界面。
2.	 在列表中选择用户/用户组，然后点击右侧操作栏下的	删除	图标按钮。

注意：	当用户或用户组的项目级权限被删除时，用户或用户组在项目上的所有权限也会被删除，这包括用户或用
户组在项目上的表级、行级及列级权限。

数据权限控制

设置系统级配置参数kylin.security.allow-project-admin-grant-acl=false后，每个项目中的项目管理员无权给用户或用户组分
配表/行/列访问权限，但仍可以查看用户或用户组的表/行/列级访问权限。

详细请看数据权限。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

191

数据访问控制

表列行级访问权限

表级访问权限

介绍

表级访问权限控制了用户/用户组在	Kyligence	Enterprise	中能查询的表。当用户/用户组被限制了对某表的权限时，用户/
用户组不能查询该表。

管理员可以对用户/用户组赋予表级访问权限，所有在当前项目有访问权限的用户/用户组，默认可以访问及查询所
有同步到当前项目中的表。

当用户/用户组的项目权限被删除，或用户/用户组被彻底从系统中删除时，对应的表级权限也会随之被删除。
当表从项目中被删除时，所有用户/用户组的表级权限也会被连带删除。
当表从项目中被重载时，所有用户/用户组的表级权限仍保留。

示例

以下我们将以具体的例子说明设置表级访问权限后的产品行为：

当一个用户不可访问表	 	SSB.SUPPLIER		时，该用户在该项目下或是上层	BI	工具中均不能看到对应的表。

设置表级访问权限

192

数据访问控制

数据源中不显示该表

此时查询该表，可以看到查询结果报错。

193

数据访问控制

列级访问权限

介绍

查询结果报错

列级访问权限限制了用户/用户组在表上能访问的列。如果用户/用户组在某列的访问权限被限制了，用户/用户组不可以
查询这个列。

管理员可以对用户/用户组赋予列级访问权限，所有在当前项目有访问权的用户/用户组，默认可以访问及查询所有
同步到当前项目中的表的所有列。

当用户/用户组的项目权限被删除，或用户/用户组被彻底从系统中删除时，对应的列级权限也会随之被删除。
当表从项目中被删除时，所有用户/用户组的列级权限也会被连带删除。
当表从项目中被重载时，所有用户/用户组的列级权限仍保留。

提示：	当用户/用户组查询	 	select	*	from	Table		时，如表上有用户/用户组没有权限的列，那么查询将仅返回用
户/用户组可以访问的列，没有权限的列不会返回。

示例

以下我们将以具体的例子说明设置列级访问权限后的产品行为。

当一个用户不可访问列	 	SSB.CUSTOMER.C_NATION		时，此时该用户在该表下无法看到该列。

194

数据访问控制

设置列级访问权限

该表下无法看到该列

此时使用	 	select	*	from	SSB.CUSTOMER		查询时，返回结果无	 	SSB.CUSTOMER.C_NATION	。而直接查询该列，或是以该列作
为表连接主键进行查询，可以看到查询结果报错。

195

数据访问控制

查询该表不可见该列

查询结果报错

行级访问权限

介绍

行级访问权限限制了用户/用户组在表上可访问的行，行级访问权限通常都被用在限制非常敏感的数据。行级权限会转
换成查询中的	Where	语句附加在用户的查询后。	行级权限由过滤器与过滤组构成。过滤器可以单独存在，也可以存在
于过滤组之中。同一过滤组内的过滤器之间的逻辑运算符统一为	 	AND		或者	 	OR		。	过滤组与过滤器、过滤组与过滤组
之间的逻辑运算符也统一为	 	AND		或者	 	OR		。

管理员可以对用户/用户组设置行级访问权限，所有在当前项目有访问权的用户/用户组，默认可以访问及查询所有
同步到当前项目中的表的所有行。

如果用户/用户组在某列中定义了行级访问权限，用户/用户组的查询结果将仅包含定义的结果，不管是通过模型，
索引还是查询下压。

当用户/用户组的项目权限被删除，或用户/用户组被彻底从系统中删除时，用户/用户组的行级权限也会随之被删
除。

当表从项目中被删除时，所有用户/用户组的行级权限也会被连带删除。
当表从项目中被重载时，所有用户/用户组的行级权限仍保留。

示例

以下我们将以具体的例子说明设置行级访问权限后的产品行为。

196

数据访问控制

点击+	添加为一位用户可访问表	 	SSB.CUSTOMER		添加一个过滤器。

选择过滤器

添加过滤条件。	注意：	过滤条件值的总数不超过	100	个。

197

数据访问控制

添加过滤器成功

再添加一个过滤组。	注意：	过滤器和过滤组的总数不超过	100	个。

198

数据访问控制

选择过滤组

添加过滤组成功

在过滤组中添加两个过滤器。	注意：	单个过滤组内过滤器的总数不超过	100	个。

199

数据访问控制

添加过滤组中的过滤器

现在我们有了一个过滤器和一个过滤组，其中第二个过滤组中还有两个过滤器。我们还可以通过下拉菜单来设置过滤器

与过滤器、过滤器与过滤组之间的逻辑运算符。

200

数据访问控制

编辑运算符

对于未使用到表	 	SSB.CUSTOMER		的查询，例如	 	select	*	from	SSB.LINEORDERS	，则本例中所设置的行级权限不会运用到
该查询上。

对于使用到表	 	SSB.CUSTOMER		的查询，无论查询中是否包含列	 	C_REGION	，行级权限均会被运用到该查询上。

例如：

	select	C_NAME	from	SSB.LINEORDER	inner	join	SSB.CUSTOMER	on	LO_CUSTKEY	=	C_CUSTKEY

实际上相当于	：

select	C_NAME	from	SSB.LINEORDER	inner	join	SSB.CUSTOMER	on	LO_CUSTKEY	=	C_CUSTKEY

where	(

								(

											(CUSTOMER.C_REGION	in	('1',	'2')	OR	CUSTOMER.C_REGION	like	'A%')

								)	AND	(

											(CUSTOMER.C_CUSTKEY	in	(1,	2))	AND	(CUSTOMER.C_REGION	in	('1',	'2')	OR	CUSTOMER.C_REGION	like	'A%')

								)

						)

而用户查询无权限访问的行时，返回结果将为空：

201

数据访问控制

返回结果为空

设置表列行级访问权限

1.	 在	系统管理->项目页面，系统管理员可以授予用户/用户组项目级访问权限，具体方法请您查阅项目级别访问权

限。

2.	 选中需要授权的项目，点击右侧操作栏下的	授权，并进入授权界面。

3.	 点击左侧箭头图标，展开需要授权的用户/用户组，界面显示该用户/用户组拥有访问权限的表列行。

授予表行列级访问权限

4.	 点击编辑按钮，勾选需要授予访问权限的表和列。默认没有任何行级访问限制，即用户可以访问列中所有的行。

202

数据访问控制

编辑表行列级访问权限

5.	 点击行级访问列表中+添加按钮，在弹窗中选择列然后输入可以访问的行。支持	IN	或	LIKE	规则设置行级权限，通

过右侧的	+/-	按钮增加或减少行级访问权限，完成后点击提交。

设置行级权限

6.	 对于已授予的行级访问权限，可以点击右侧的...按钮进行编辑或删除。

203

数据访问控制

编辑行级访问权限

7.	 确认当前设置的表列行级访问权限无误后点击提交。

注意事项

授权操作对用户/用户组以白名单的形式展示，即为用户/用户组添加的表行列权限为可访问。
默认情况下，用户/用户组被添加至项目后，将自动授予该项目下的所有表及行列的访问权限。您可以修改配置文
件中的配置项	 	kylin.acl.project-internal-default-permission-granted	，设置成	 	false		后，用户/用户组被添加至
项目后，默认不被授予任何表列行权限，系统管理员可以手动的选择表并设置访问权限。

用户/用户组的访问权限取可访问的最大结果集	（并集）。

如用户	 	user1		有表	 	table1		的访问权限，用户	 	user1		在用户组	 	group1		中，且用户组	 	group1		有表
	table2		的访问权限，此时用户	 	user1		同时可以访问表	 	table1		和	 	table2	。
如用户组	 	group1		有表	 	table1		和	 	table2	的访问权限，用户组	 	group2		有表	 	table2		和	 	table3		的访问权
限，用户	 	user1		属于用户组	 	group1		和	 	group2		，此时	 	user1		同时拥有表	 	table1	、 	table2		和	 	table3
的访问权限。

仅系统管理员用户可以进行表行列级访问全选的	增/删/改	操作。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

204

系统运维

系统运维

本章将介绍	Kyligence	Enterprise	的诊断方法、运维工具等，包含下述内容：

诊断

系统诊断、任务诊断与查询诊断

查询火焰图

构建火焰图

升级	Session	表工具
CLI	运维工具

环境依赖服务检测

诊断包工具

元数据备份与恢复

回滚工具

守护进程

查询稳定的保护策略

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

205

诊断

诊断

您可以通过	Kyligence	Enterprise	导出日志信息，将其提供给运维人员或	Kyligence	技术支持进行问题诊断。此外，您还
可以通过火焰图对查询性能进行诊断。

系统诊断、任务诊断与查询诊断

查询火焰图

构建火焰图

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

206

诊断

系统诊断、任务诊断与查询诊断

用户在使用	Kyligence	Enterprise	过程中可能会遇到各类问题，例如任务运行失败、SQL	查询失败、SQL	查询时间过长
等。为了帮助高效解决这些问题，Kyligence	Enterprise	提供了诊断包功能，可以将有关的日志信息打包成压缩包，供运
维人员或	Kyligence	技术支持分析问题原因。

该功能包含了三部分：系统诊断、任务诊断和查询诊断。除了本章介绍的在页面上打诊断包的方法之外，您还可以通过

脚本打诊断包，具体命令以及各诊断包内容，详见诊断包工具。

通过网页生成系统诊断包

系统诊断包包含整个	Kyligence	Enterprise	实例的诊断信息，生成系统诊断包需要如下操作：

通过网页生成系统诊断包

1.	 进入系统管理页面，点击左下角的诊断按钮。

注意：暂只有系统管理员才能通过网页生成系统诊断包。

2.	 选择时间范围：可以选择最近一小时、最近一天、最近三天、最近一个月，或者自定义时间范围。

注意：选择的时间范围必须包含	Kyligence	Enterprise	发生问题的时间段。

3.	 选择服务器。

注意：如果	Kyligence	Enterprise	部署在多节点上，需要确定发生问题的节点，并在生成系统诊断包时选择正
确的服务器名字，否则有可能系统诊断包中不包含问题的有关信息。

4.	 点击生成并下载：生成诊断包后，将自动触发下载任务，如果生成诊断包失败，您可以在界面上查看失败详情。

207

诊断

通过网页生成任务诊断包

任务诊断包包含某个任务的诊断信息，生成任务诊断包需要如下操作：

通过网页生成任务诊断包

1.	 登入Kyligence	Enterprise后，点击左侧导航栏监控，在任务列表页面中某个任务的操作栏内，点击下载任务诊断包

按钮。

2.	 选择服务器。
3.	 点击生成并下载：生成诊断包后，将自动触发下载任务，如果生成诊断包失败，您可以在界面上查看失败详情。

通过网页生成查询诊断包

查询诊断包包含某个查询的诊断信息，生成查询诊断包需要如下操作：

通过网页生成查询诊断包

208

诊断

1.	 登入Kyligence	Enterprise后，点击左侧导航栏查询，在查询历史页面中某个查询的操作栏内，点击下载查询诊断包

按钮。

2.	 点击生成并下载：生成诊断包后，将自动触发下载任务，如果生成诊断包失败，您可以在界面上查看失败详情。

默认情况下，所有具有项目查询权限的用户，都可以下载查询诊断包，以便于查询问题诊断。	由于查询诊断包中包含部
分配置信息，如果您希望收缩下载查询诊断包的相关权限，可以在	 	$KYLIN_HOME/conf/kylin.properties		添加配置
	kylin.security.allow-non-admin-generate-query-diag-package=false	，只允许系统管理员和具有项目	ADMIN	权限的普
通用户下载查询诊断包。

FAQ

Q:	三种诊断包所包含的内容有哪些差异？

三种诊断包所包含的内容，详见诊断包工具。

Q:	如果遇到打包超时怎么办？

请您在	 	$KYLIN_HOME/conf/kylin.properties		中适当调大	 	kylin.diag.package.timeout-seconds		的参数（单位为秒，默认
超时时间是一小时）后重启	Kyligence	Enterprise。

Q:	如果打包完成后，页面没有自动下载诊断包怎么办？

如果打包成功，但是自动下载失败，您可以点击左下方的手动下载，选择您想下载的诊断包后，点击下载按钮手动进行

下载。

Q:	Kyligence	Enterprise	所使用的	hostname	包含下划线( 	_	)时，生成诊断包发生异常怎么办？

请您在	 	$KYLIN_HOME/kylin.properties.override		中加个服务发现的参数	 	spring.cloud.zookeeper.discovery.instance-
host=IP		重启	Kyligence	Enterprise。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

209

诊断

查询火焰图

Kyligence	Enterprise	内置了	async-profiler，当需要使用火焰图对查询性能进行诊断时，用户可以通过调用	API	接口对
Spark	Driver	和	Executor	生成查询火焰图。

由于生成火焰图为系统级别，对所有项目都会有影响，该功能只有	Admin	用户有权限使用。

可配置参数

配置项

描述

kylin.query.async-profiler-enabled

是否开启生成功能，默认开启。开启后可以通过调用	API	触发生成和下载火
焰图

kylin.query.async-profiler-result-
timeout

收集火焰图结果的最大等待时间，如果超时会直接返回，默认	60s

kylin.query.async-profiler-profile-
timeout

收集火焰图结果的最长超时时间，如果超时会停止收集，默认	5min，防止
过长时间收集

开始生成火焰图

通过调用下面接口开始生成火焰图

Kyligence	Enterprise

GET	 	http://host:port/kylin/api/query/profile/start?params={params}

URL	Parameters

	params	,	可选,	String,	指定async-profiler	参数，默认为	 	start,event=cpu	(profile	cpu	使用情况)。	其他可配置的
参数可以参考	https://github.com/jvm-profiling-tools/async-profiler

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

Kyligence	Cloud

通过	curl	的方式在终端使用命令获取，详细信息参照上述	Kyligence	Enterprise	中的请求，如：

curl	-X	GET	\

'http://host:port/kylin/api/query/profile/start'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	en'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

停止生成火焰图，并下载结果

在开始生成火焰图之后，可以调用下面的接口停止生成火焰图，并下载结果

Kyligence	Enterprise

GET	 	http://host:port/kylin/api/query/profile/dump?params={params}

210

诊断

URL	Parameters

	params	,	可选,	String，	指定async-profiler	参数，默认为	 	flamegraph	(把结果收集为火焰图)，其他可配置的参
数可以参考	https://github.com/jvm-profiling-tools/async-profiler

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

Kyligence	Cloud

通过	curl	的方式在终端使用命令获取，详细信息参照上述	Kyligence	Enterprise	中的请求，如：

curl	-X	GET	'http://host:port/kylin/api/query/profile/dump'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	en'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-o	'asyncProfiler.tar.gz'

已知限制

1.	 该功能目前支持的平台为	Linux	X64	以及标准的	ARM	架构机器。
2.	 生成火焰图过程中可能会影响	Kyligence	Enterprise	的性能，请避免在生产环境长时间生成火焰图。
3.	 火焰图结果只能被下载一次。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

211

诊断

构建火焰图

Kyligence	Enterprise	内置了	async-profiler，当需要使用火焰图对构建任务性能进行诊断时，用户可以通过调用	API	接口
对	Spark	Driver	和	Executor	生成查询火焰图。

由于生成火焰图为系统级别，对所有项目都会有影响，该功能只有	Admin	用户有权限使用。

可配置参数

配置项

描述

kylin.engine.async-profiler-enabled

是否开启生成功能，默认开启。开启后可以通过调用	API	触发生成和下载
火焰图

kylin.engine.async-profiler-result-
timeout

收集火焰图结果的最大等待时间，如果超时会直接返回，默认	60s

kylin.engine.async-profiler-profile-
timeout

收集火焰图结果的最长超时时间，如果超时会停止收集，默认	5min，防止
过长时间收集

开始生成火焰图

通过调用下面接口开始生成火焰图

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	en

	Accept-Language:	zh

	Content-Type:	application/json;charset=utf-8

Kyligence	Enterprise

有两种生成方式

GET	 	http://host:port/kylin/api/jobs/profile/start_project?project={projectName}&step_id={jobStepId}&params=
{params}

URL	Parameters

	project	,	必填，String，指定当前构建任务所在的	projectName，无默认值
	step_id	,	必填，String，指定当前构建任务具体执行的	jobStepId，可在	YARN	界面找到对应提交的
Application，复制其	Name	除去	 	job_step_		剩下的部分
	params	,	可选,	String,	指定async-profiler	参数，默认为	 	start,event=cpu	(profile	cpu	使用情况)

GET	 	http://host:port/kylin/api/jobs/profile/start_appid?app_id={yarnAppId}&params={params}

URL	Parameters

	app_id	,	必填，String，指定当前构建任务提交至	YARN	的	Application	ID
	params	,	可选,	String,	指定async-profiler	参数，默认为	 	start,event=cpu	(profile	cpu	使用情况)

Kyligence	Cloud

通过	curl	的方式在终端使用命令获取，详细信息参照上述	Kyligence	Enterprise	中的请求，如：

curl	-X	GET	\

'http://host:port/kylin/api/jobs/profile/start_project?project={projectName}&step_id={jobStepId}'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

212

诊断

-H	'Accept-Language:	en'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

停止生成火焰图，并下载结果

在开始生成火焰图之后，可以调用下面的接口停止生成火焰图，并下载结果

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	en

	Accept-Language:	zh

	Content-Type:	application/json;charset=utf-8

Kyligence	Enterprise

有两种获取方式

GET	 	http://host:port/kylin/api/jobs/profile/dump_project?project={projectName}&step_id={jobStepId}&params=
{params}

URL	Parameters

	project	,	必填，String，指定当前构建任务所在的	projectName，无默认值
	step_id	,	必填，String，指定当前构建任务具体执行的	jobStepId，可在	YARN	界面找到对应提交的
Application，复制其	Name	除去	 	job_step_		剩下的部分
	params	,	可选,	String，	指定async-profiler	参数，默认为	 	flamegraph	(把结果收集为火焰图)

GET	 	http://host:port/kylin/api/jobs/profile/dump_appid?app_id={yarnAppId}&params={params}

URL	Parameters

	app_id	,	必填，String，指定当前构建任务提交至	YARN	的	Application	ID
	params	,	可选,	String,	指定async-profiler	参数，默认为	 	flamegraph	(把结果收集为火焰图)

Kyligence	Cloud

通过	curl	的方式在终端使用命令获取，详细信息参照上述	Kyligence	Enterprise	中的请求，如：

curl	-X	GET	'http://host:port/kylin/api/jobs/profile/dump_project?project={projectName}&step_id={jobStepId}'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	en'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-o	'build_asyncProfiler.tar.gz'

已知限制

1.	 该功能目前支持的平台为	Linux	X64	以及标准的	ARM	架构机器。
2.	 生成火焰图过程中可能会影响	Kyligence	Enterprise	的性能，请避免在生产环境长时间生成火焰图。
3.	 涉及到的构建火焰图参数均为系统级参数，请勿在其他级别进行设置，可能会引起异常行为。
4.	 	params		支持配置的参数可以参考	https://github.com/jvm-profiling-tools/async-profiler

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

213

升级	Session	表工具

升级	Session	表工具

当配置了	 	kylin.web.session.secure-random-create-enabled=true		或者	 	kylin.web.session.jdbc-encode-enabled=true		后
需要升级	session	表，否则用户无法登录

使用过程

输入命令进行升级，举例如下：

$KYLIN_HOME/bin/kylin.sh	io.kyligence.kap.tool.upgrade.UpdateSessionTableCLI

注意：升级过程中可能由于权限原因导致更新失败，此时需要运维人员手动执行更新	session	表的语句

更新语句

使用	PostgreSQL	作为元数据库

ALTER	TABLE	ke_metadata_session	ALTER	COLUMN	SESSION_ID	TYPE	VARCHAR(180)	,	ALTER	COLUMN	SESSION_ID	SET	NOT	NUL

L;

ALTER	TABLE	ke_metadata_session_ATTRIBUTES	ALTER	COLUMN	SESSION_ID	TYPE	VARCHAR(180)	,	ALTER	COLUMN	SESSION_ID

SET	NOT	NULL;

使用	MySQL	作为元数据库

ALTER	TABLE	ke_metadata_session	MODIFY	COLUMN	SESSION_ID	VARCHAR(180)	NOT	NULL;

ALTER	TABLE	ke_metadata_session_ATTRIBUTES	MODIFY	COLUMN	SESSION_ID	VARCHAR(180)	NOT	NULL;

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

214

CLI	运维工具

CLI	运维工具

本章主要介绍如何利用命令行界面（Command-Line	Interface）工具进行系统的日常维护工作。如环境检测工具、元数据
工具和诊断包工具。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

215

CLI	运维工具

环境检测

在	Kyligence	Enterprise	运行之前，我们提供环境检测工具来帮助您提前查看环境中潜在的问题。当您第一次启动
Kyligence	Enterprise	时，启动脚本将自动运行环境检测工具。

使用方法

第一次启动	Kyligence	Enterprise	时系统会自动进行环境检测。如果环境检测执行失败，则再次启动产品时，系统会再次
运行此工具。一旦环境检测执行成功，则再次启动不会自动运行此工具。

如果您需要再次进行环境检测，请运行以下命令：

$KYLIN_HOME/bin/check-env.sh

检测项目

以下表格说明了检测工具具体的检测内容：

检测项目

Kerberos

操作系统版
本和系统命
令

Hadoop	配
置文件

描述

首先查看用户配置中是否开启了	Kerberos，如果没有开启，则跳过检测，如果开启了，则执行以
下操作:
1.	检查	Kerberos	命令是否存在
2.	初始化	Kerberos

目前	Kyligence	Enterprise	只支持在	Linux	操作系统上运行。除了操作系统，还会检测	 	hadoop		和
	yarn		命令是否存在，此两个命令如果不存在，需要确认	Hadoop	客户端是否正常。

Kyligence	Enterprise	会将系统中	Hadoop	相关配置文件复制到产品安装路径下的一级目录
	$KYLIN_HOME/hadoop_conf	，例如	 	core-site.xml	、 	hdfs-site.xml	、 	yarn-site.xml	、 	hive-
site.xml	等。此项检测会检查 	$KYLIN_HOME/hadoop_conf	目录是否存在，并且是否包含重要的配置
文件。

HDFS	工作
目录

1.	HDFS	工作目录是否存在
2.	如果存在，当前用户是否有读写权限

Java	版本

目前我们只支持	Java	1.8	以上的版本

服务器端口

检测服务器端口是否被占用

Spark

1.	检测集群资源大小是否小于当前配置的资源大小，例如	executor	cores	以及	executor	instances。
2.	检测	Spark	可用性
3.	检测配置的提交查询任务和构建任务的	Yarn	队列是否合法
4.	检测配置的	driver	host	地址是否合法

Spark	历史
目录

用户可以配置一个	HDFS	目录存放	Spark	的日志，所以此项会检测该目录是否存在，并且是否有
读写权限。

元数据库

是否能正常连接到元数据库，并且能操作元数据。

InfluxDB

1.	能正常连接到	InfluxdDB
2.	当前用户是否有读写权限

ZooKeeper

检测服务发现是否可以正常使用

ClickHouse

检测是否连接到分层存储

KylinConfig

检测kylin.properties	的配置项，必须以	kylin	/	kap	/	spring	/	server开头

查询历史

检测	RDBMS	数据库中，当前用户对存储查询历史相关表	query_history、query_history_realization
是否有读写权限

216

CLI	运维工具

快速启动

如您非首次启动，可运行下述命令快速启动	Kyligence	Enterprise。

$KYLIN_HOME/bin/kylin.sh	-DskipCheck	start

系统会为您跳过以下检查步骤，以缩短启动时间。

检查元数据是否正常，包括管理员用户是否存在，session表字段是否正确
检查	ZooKeeper	地址是否配置
检查	Spark	相关的	HDFS	路径是否存在。	如果存在，当前用户是否有读写权限
在未开启守护进程时，确保无重复的启动进程

检查	Stop	的用户是否为	Start	用户

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

217

CLI	运维工具

诊断包工具

用户在使用	Kyligence	Enterprise	过程中可能会遇到各类问题，例如模型构建失败、SQL	查询失败、SQL	查询时间过长
等。为了帮助高效解决这些问题，Kyligence	Enterprise	提供了诊断包功能，可以将有关的日志信息打包成压缩包，供运
维人员或	Kyligence	技术支持分析问题原因。

该功能包含了三部分：系统诊断、任务诊断和查询诊断。

通过脚本生成诊断包

FusionInsight	环境下需要先执行	 	source	/opt/hadoopclient/bigdata_env	，其中	 	hadoopclient		为变量。

生成系统诊断包	执行	 	$KYLIN_HOME/bin/diag.sh	[-startTime	<START_TIMESTAMP>	-endTime	<END_TIMESTAMP>]	[-destDir
<DESTINATION_DIR>]		来生成系统诊断包，默认生成时间范围为最近三天。日志的起始时间戳的单位为unix时间戳，
可以根据自己的需要自行配置。	例如，可以在Linux中运行 	echo	$((`date	+%s`*1000))	来获取当前的unix时间戳。

生成任务诊断包	执行	 	$KYLIN_HOME/bin/diag.sh	-job	<jobid>	[-destDir	<DESTINATION_DIR>]		来生成任务诊断包，其
中请将	 	<jobid>		代替为实际的任务	ID	号。

生成查询诊断包	执行	 	$KYLIN_HOME/bin/diag.sh	-project	<project>	-query	<queryid>	[-destDir	<DESTINATION_DIR>]
来生成查询诊断包，其中请将	 	<queryid>		代替为实际的查询	ID	号，将	 	<project>		代替为实际查询的所在项目名
字。

诊断包存放地址	通过脚本生成的诊断包默认会存放在	 	$KYLIN_HOME/diag_dump/		下，也可以通过修改	 	-destDir		这
一参数来指定存放位置。

注意：为了避免诊断包占用大量存储，请及时清理	 	$KYLIN_HOME/diag_dump/	目录。

不包含元数据文件	若诊断包中不需要包含元数据文件，	可在参数中添加	 	-includeMeta	false

包含元数据审计日志	诊断包中默认不包含元数据审计日志，	若诊断包中需要包含元数据审计日志，	可在参数中添
加	 	-includeAuditLog	true		或者在 	kylin.properties	中增加配置项 	kylin.diag.include-auditlog=true

诊断包内容

系统诊断包内容

	/conf	： 	$KYLIN_HOME/conf	。

	/hadoop_conf	： 	$KYLIN_HOME/hadoop_conf	。

	/metadata	：元数据文件。

	/logs	： 	$KYLIN_HOME/logs/kylin.log	，系统诊断包会截取指定时间范围内的日志。

	/spark_logs	：系统诊断包中会包含时间范围内的所有查询	Spark	executor	日志和查询	Spark	executor	的	GC	日志。
不包括构建任务	Spark	executor	日志，如需相关日志，请生成对应任务诊断包。
	/sparder_history	：系统诊断包中会包含时间范围内的所有	Sparder	日志。
	/system_metrics	：系统诊断包中指定时间范围内的系统监控指标。

	/audit_log	：系统诊断包中指定时间范围内的元数据审计日志（默认不包含）。

	/job_tmp	：优化建议日志。

	/client	：操作系统资源占用情况，Hadoop	的版本和	Kerberos	信息。
	/bin	：程序启动，管理执行文件。

	/monitor_metrics	：系统的监控统计信息。

	/rec_candidate	：模型的优化建议。

	/write_hadoop_conf	： 	$KYLIN_HOME/write_hadoop_conf	，构建集群的	hadoop	配置（未配置读写分离时不会有该目
录）。

218

CLI	运维工具

文件	 	catalog_info	：安装包目录结构。
文件	 	commit_SHA1	：git-commit	的版本号。
文件	 	hadoop_env	：hadoop	环境变量。
文件	 	info	：许可证，诊断包的信息和主机名称。
文件	 	kylin_env	：kyligence	Enterprise	版本，操作系统的信息，Java的信息，git-commit	的信息。
文件	 	time_used_info	：诊断包里生成各个文件的时间统计信息。

任务诊断包内容

	/conf	： 	$KYLIN_HOME/conf	。

	/hadoop_conf	： 	$KYLIN_HOME/hadoop_conf	。

	/job_history	：任务执行历史信息，主要包含Yarn	Application的执行信息。
	/metadata	：元数据文件。

	/logs	： 	$KYLIN_HOME/logs/kylin.log	，任务诊断包会截取指定任务执行过程中产生的日志。

	/spark_logs	：任务诊断包中会包含指定任务执行过程中产生的所有	Spark	executor	日志。
	/system_metrics	：任务诊断包中会包含指定任务执行过程中产生的系统监控指标。

	/audit_log	：任务诊断包中会包含指定任务执行过程中的审计日志（默认不包含）。

	/job_tmp	：任务诊断包中会包含指定任务执行过程中产生的临时文件，日志和优化建议日志。

	/yarn_application_log	：任务诊断包中会包含指定任务对应的	yarn	application	生成的日志。
	/client	：操作系统资源占用情况，Hadoop	的版本信息和	Kerberos	信息。
	/bin	：程序启动，管理执行文件。

	/monitor_metrics	：系统的监控统计信息。

	/rec_candidate	：模型的优化建议。

	/write_hadoop_conf	： 	$KYLIN_HOME/write_hadoop_conf	，构建集群的	hadoop	配置（未配置读写分离时不会有该目
录）。

文件	 	catalog_info	：安装包目录结构。
文件	 	commit_SHA1	：git-commit	的版本号。
文件	 	hadoop_env	：hadoop	环境变量。
文件	 	info	：许可证，诊断包的信息和主机名称。
文件	 	kylin_env	：Kyligence	Enterprise	版本，操作系统的信息，Java的信息，git-commit	的信息。
文件	 	time_used_info	：诊断包里生成各个文件的时间统计信息。

查询诊断包内容

	/conf	： 	$KYLIN_HOME/conf	。

	/hadoop_conf	： 	$KYLIN_HOME/hadoop_conf	。

	/metadata	：指定项目下所有模型的元数据。

	/logs	： 	$KYLIN_HOME/logs/kylin.log	，指定查询的日志	log。
	/spark_logs	：查询诊断包中会包含时间范围内的所有	Spark	executor	日志和查询	Spark	executor	的	GC	日志。
	/sparder_history	：查询诊断包中会包含时间范围内的所有	Sparder	日志。
	/client	：操作系统资源占用情况，Hadoop	的版本信息和	Kerberos	信息。
文件	 	catalog_info	：安装包目录结构。
文件	 	commit_SHA1	：git-commit	的版本号。
文件	 	hadoop_env	：hadoop	环境变量。
文件	 	info	：许可证，诊断包的信息和主机名称。
文件	 	kylin_env	：Kyligence	Enterprise	版本，操作系统的信息，Java的信息，git-commit	的信息。
文件	 	time_used_info	：诊断包里生成各个文件的时间统计信息。

多节点诊断

219

CLI	运维工具

目前暂时没有接口获知集群里有哪些节点，需要您自行记录下部署的节点，然后去各个节点分别打诊断包，打诊断包的

方法与上面的说明相同。

诊断包脱敏

诊断包脱敏功能能够隐藏诊断包中的敏感信息，如用户名、密码、IP	信息等，在帮助用户解决问题的同时，能够满足用
户的数据安全要求。

您可以通过以下配置项开启诊断包脱敏功能：

##	诊断包的脱敏等级。RAW	代表不脱敏，OBF	代表脱敏

kylin.diag.obf.level=OBF
##	诊断包中	IP	是否脱敏。false	代表不脱敏，true	代表脱敏，配置	kylin.diag.obf.level=OBF	时生效，脱敏	IP	可能会导致生成诊断包
变慢

kylin.diag.ip-obf-enabled=false

配置开启后，通过	Web	UI	或通过终端	CLI	工具生成的诊断包都将脱敏。系统将脱敏	 	KYLIN_HONE/conf		目录下所有以
	kylin.properties		开头的文件，脱敏时会扫描所有的配置项，包含	 	password	、	 	user	、 	zookeeper.zk-
auth	、 	source.jdbc.pass		的配置项都会被脱敏，脱敏方式是将配置项的值替换为	 	<hidden>	。开启	IP	脱敏配置后，IP
也将替换为 	<hidden>	。

常见问题

问：为什么生成的系统诊断包日志内容不完整？

答：日志的提取是基于文本的匹配（基于分钟级别的时间字符串），若发现内容不完整，有可能是指定的时间戳在转换

为时间字符串时，在日志中没法匹配到相应的行，可以尝试修改时间范围重新打诊断包。

问：为什么生成的诊断包中	 	system_metrics		目录缺失内容？

答： 	system_metrics		目录包含系统监控指标，产品使用	InfluxDB	存储系统监控指标。InfluxDB	备份数据时，需要指定
RPC	端口，请确认	 	$KYLIN_HOME/conf/kylin.properties		中的配置项	 	kylin.metrics.influx-rpc-service-bind-address		是
否配置正常。

问：生成诊断包时遇到	Out	of	Memory	(OOM)	问题，如何解决？

答：请在	 	conf/setenv.sh		文件中调大	 	JAVA_VM_XMX		的值，该值建议调整为元数据大小的	4	倍以上，即如果元数据大小
为	1G，那么请将该值设置成	4G	或者	4G	以上。

问：为什么导出的模型优化建议的文件为0KB？

答：模型如果没有优化建议，那么对应的模型生成的优化建议就会为0KB。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

220

CLI	运维工具

元数据备份与恢复

Kyligence	Enterprise	实例是无状态的服务，所有的状态信息都存储元数据中，因此备份与恢复元数据是运维工作中一个
至关重要的环节，可以在由于误操作导致整个实例或某个	Model	异常时将	Kyligence	Enterprise	快速从备份中恢复出来。

元数据分为系统级别和项目级别。

元数据备份

一般来说，在每次进行故障恢复或者系统升级之前，对元数据进行备份是一个良好的习惯，这可以保证在操作失败后有

回滚的可能，在最坏情况下依然保持系统的稳定性。

此外，元数据备份也是故障查找的一个工具，当系统出现故障导致前端频繁报错，通过下载并查看元数据往往能对确定

元数据是否存在问题提供帮助。

元数据可以通过命令行进行备份，具体操作如下：

备份系统级别的元数据

$KYLIN_HOME/bin/metastore.sh	backup	METADATA_BACKUP_PATH

参数说明：

	METADATA_BACKUP_PATH		-	可选，表示备份的元数据保存路径，默认值为	 	${KYLIN_HOME}/meta_backups/

备份项目级别的元数据

$KYLIN_HOME/bin/metastore.sh	backup-project	PROJECT_NAME	METADATA_BACKUP_PATH

参数说明：

	ROJECT_NAME		-	必选，需要备份的项目名称，如	learn_kylin
	METADATA_BACKUP_PATH		-	可选，表示备份的元数据保存路径，默认值为	 	${KYLIN_HOME}/meta_backups/

元数据恢复

Kyligence	Enterprise	中需要用命令行进行元数据恢复。

恢复系统级别的元数据

$KYLIN_HOME/bin/metastore.sh	restore	METADATA_RESTORE_PATH	[--after-truncate]

示例：

./bin/metastore.sh	restore	meta_backups/2019-12-19-14-18-01_backup/

参数说明：

	METADATA_BACKUP_PATH		-	必选，表示需要被恢复的元数据的保存路径，默认值为	 	${KYLIN_HOME}/meta_backups/
	--after-truncate		-	可选，如果加上这个参数，那么会完全恢复系统的元数据，否则只会将被删除和被修改的
元数据恢复，新增的元数据依然会保留。

恢复项目级别的元数据

$KYLIN_HOME/bin/metastore.sh	restore-project	PROJECT_NAME	METADATA_RESTORE_PATH	[--after-truncate]

221

CLI	运维工具

示例：

./bin/metastore.sh	restore-project	projectA	meta_backups/2019-12-19-14-18-01_backup/

参数说明：

	PROJECT_NAME		-	必选，表示需要被恢复的项目名称
	METADATA_BACKUP_PATH		-	必选，表示需要被恢复的元数据的保存路径，默认值为	 	${KYLIN_HOME}/meta_backups/
	--after-truncate		-	可选，如果加上这个参数，那么会完全恢复项目的元数据，否则只会将被删除和被修改的
元数据恢复，新增的元数据依然会保留。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

222

CLI	运维工具

回滚工具

当使用人员发生了误操作导致元数据或数据丢失，或者	Kyligence	Enterprise	发生未知问题而处于不可用状态时，您可以
通过回滚工具回退到指定时刻，避免误操作带来的影响。

注意：回滚工具是一种紧急时刻救援工具，请尽量避免在不了解风险的情况下随意使用。

工具介绍

使用过程

停止	Kyligence	Enterprise	集群所有节点服务；

使用工具进行回滚，举例如下：

$KYLIN_HOME/bin/rollback.sh		--project	project_example	--time	'2020-09-01	15:20:19'

观察日志，确认项目、模型、用户、Segment、任务等元数据的版本差异；

根据提示输入确认信息，确保您知晓回滚的影响；

完成回滚，开启	Kyligence	Enterprise	集群的节点服务。

参数说明如下：

	-p，--project	<arg>		：项目名（可选）， 	<arg>		为项目名
	-t,	--time	<arg>	：回滚的历史时间点（必选），可选值为保留历史版本时间至今的任意时间点	 	<arg>		为回退到
的具体时间，类型为	 	yyyy-MM-dd	HH:mm:ss
	--skip-check-data		：忽略检查资源文件是否存在（可选）

使用场景

以下为运维过程中使用回滚工具的一种典型场景，介绍了在产品出现不可知问题时，如何使用该工具进行回退，并对问

题进行降级。

AI	增强模式项目	 	rollback_example		下生成了优化建议。用户在9月1号16点06分，查看优化建议页面，并接受了优
化建议，那么该项目的模型以及索引相关的元数据就被更新了。

这时候可以看到生成了系统推荐的索引，但是此时出现了不可知问题，导致该索引无法正常构建，且影响到了整个

集群的健康，此时产品也处于无法操作状态。

为了保障生产可用，可以使用回滚工具，将该这个项目的元数据和数据回退到9月1号15点20分。

$KYLIN_HOME/bin/rollback.sh		--project	rollback_example	--time	'2020-09-01	15:20:19'

可以看到该项目已经回到事故发生之前的状态，系统推荐的索引消失，集群也回到了稳定状态。

223

CLI	运维工具

回滚完毕

在完成回滚后，还需要对发生的问题进行降级。在该例中，您可以点击设置，在基本设置页面中暂时先关闭智能推

荐功能，并及时与	Kyligence	技术支持团队进行沟通。

在产品问题修复后，您可以重新开始使用智能推荐功能。

与元数据备份和恢复工具的区别

现在	Kyligence	Enterprise	已经提供元数据备份与恢复工具，通过该工具在一定程度上可以保护元数据不丢失。但是该工
具存在部分局限：

无法回退至指定的时刻，只能回退至过去备份过的版本；

该回退工具较为暴力且直接，有可能出现回退后元数据不可用的情况。例如一些文件因为元数据不存在，被系统作

为垃圾清理了，这时候对应的备份元数据就不可用了。

相关配置

使用回滚工具的前提是：在需要回滚到的时间范围内，资源数据（索引数据，字典数据，Snapshot	数据等）没有被删
除。相关配置如下：

	kylin.storage.time-machine-enabled		：是否开启回滚功能，默认值为	 	false	。该配置开启后，系统会避免主动删
除资源数据，以保证资源数据在需要保留的时间范围内不会被删除。

	kylin.storage.resource-survival-time-threshold		：资源数据保留时长（索引数据，字典数据，Snapshot	数据

224

CLI	运维工具

等），默认值为	 	7d	。每次回滚后，已保留时长都会归为	0，意味着资源文件实际保留的时间在某些情况下会超过
该设定时间。数字单位说明： 	d	（天）、 	h	（小时）、 	m	（分钟）。

注意点和常见报错

下面是在使用该工具的过程中可能会碰到的一些报错和注意点。

注意点

使用该回滚工具，会把任务执行的状态回滚到历史时刻的状态，Kyligence	Enterprise	启动后会自动重新触发任务执
行。

开启该回滚工具后，可能会导致被保留的垃圾文件变多，占用更多的存储空间。且设置保留期后，使用垃圾清理工

具并不能清理在保留期内的已经过期的资源数据。

工具执行过程中，如果再次运行该工具，每一次运行都会保留一份当前元数据的备份在	 	{working-
dir}/_current_backup		目录下，以时间区分文件名。
指定的回滚时间不能大于当前时间。

使用工具之前必须要关闭集群下所有实例，不然有可能会造成数据不一致的状况。

如果您手动删除了一个项目的字典数据，而后又重新生成，使用该工具有可能会造成字典数据和索引数据不一致。

如果刚升级至新版本的	Kyligence	Enterprise	，并且升级后就开启了	 	kylin.storage.time-machine-enabled		配置，需
要先等待所设置的保留期时间，才能保证该工具可以正常回滚。

回滚到历史时刻时，使用的	Snapshot	数据也是历史时刻的	Snapshot	数据，所以无法保证	SCD1	生效。
如果指定的回滚时间小于元数据备份的最小时间，回滚将无法进行。

回滚工具的回滚范围不包括历史优化建议和被用户手动删除的项目。

常见报错

使用回滚工具，会把任务执行的状态回退到历史时刻的状态，KE	启动后会重新触发执行。
开启时光机后，会导致保存的垃圾文件变多，占用更多的存储空间，在保留期内使用垃圾清理工具并不能清理在保

留期内的已经过期的资源数据。

工具执行过程中，如果多次运行，每一次运行都会保留一份当前元数据的备份在	 	{working-dir}/_current_backup
目录下，以时间区分文件名。

用户指定的时间不能大于当前时间。

使用工具之前必须要关闭所有的服务节点，不然会造成数据不一致的状况。

如果用户手动删除了一个项目的字典数据，然后重新生成字典数据，使用回滚工具会造成字典数据和模型数据不一

致的情况。

用户在刚升级开启了	 	kylin.storage.time-machine-enabled		配置后，需要等待过了一个配置的保留期时间，才能保
证在保留期时间范围内，任意时间回滚。

用户回滚到历史时刻，使用的	snapshot	数据也是历史时刻的	snapshot	数据，而不是使用的最新的	snapshot	数据。
如果用户指定的回滚时间，小于元数据备份的最小时间，是不能进行回滚的。

	dectect	port	available	failed	,	检测端口失败，需要关闭集群的服务节点。
	check	storage	data	available	failed	，	检测资源文件失败，您可以使用	 	--skip-check-data		参数进行强行回滚。
	restore	current	metadata	failed,	please	restore	the	metadata	database	manually	，	元数据回滚失败，而且使用当
前备份覆盖也失败。此时请您与	Kyligence	技术支持团队进行沟通，避免误操作造成元数据丢失。

附录

以下为该工具执行回滚的详细过程：

备份当前元数据

检查集群是否停止

从备份目录找到元数据的	Snapshot	文件，然后重放	 	auditlog		日志到用户指定时间
对比元数据差异，提示用户

等待用户确认

225

CLI	运维工具

检查元数据指向的资源文件是否可用

回滚元数据，如果回滚失败，会使用当前元数据的备份覆盖回来

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

226

守护进程

Kyligence	Enterprise	守护进程

为了保持	Kyligence	Enterprise	始终健康活跃，从	Kyligence	Enterprise	4.2.0	开始，系统增加了守护进程的功能，这个守护
进程会监控	Kyligence	Enterprise	是否处于健康状态，如果检测到	Kyligence	Enterprise	处于不健康状态，则会执行重启或
服务降级操作。

使用说明

开启

守护进程默认是关闭的，如果要开启它，需要在全局配置文件	 	$KYLIN_HOME/conf/kylin.properties		中，增加配置
	kylin.guardian.enabled	=	true	。

注意：以下所有配置生效的前提是	 	kylin.guardian.enabled	=	true

如果配置开启守护进程，则在启动	Kyligence	Enterprise	后会自动启动一个守护进程，这个进程是和环境变量
	KYLIN_HOME		绑定的，也就是说每个	Kyligence	Enterprise	实例有且只有一个守护进程与之对应。

守护进程说明：

进程号记录在	 	$KYLIN_HOME/kgid		文件中。

进程的日志输出在	 	$KYLIN_HOME/logs/guardian.log		文件中。

守护进程会定时去检查	Kyligence	Enterprise	的健康状态，第一次检查的时间延迟是由参数	 	kylin.guardian.check-
init-delay		配置（单位：分钟），默认为	5	分钟，之后检查的时间间隔是由参数	 	kylin.guardian.check-interval
配置（单位：分钟），默认为	1	分钟检查一次。

检查项

守护进程目前会去检查	Kyligence	Enterprise	4	个方面的健康状况：

Kyligence	Enterprise	进程状态

守护进程通过	Kyligence	Enterprise	的进程号判断它是否处于健康状态，如果进程号文件	 	$KYLIN_HOME/pid		存在，而
对应的进程不存在，说明此时	Kyligence	Enterprise	处于异常宕机状态，则守护进程会去重新启动它。

Spark	Context	重启失败检查

如果	Spark	Context	重启失败次数	>=	阈值，则守护进程会去重启	Kyligence	Enterprise。这个功能默认打开，如果要
关闭它，可以在	 	$KYLIN_HOME/conf/kylin.properties		中，增加配置	 	kylin.guardian.restart-spark-fail-restart-
enabled	=	false	，失败次数阈值由参数	 	kylin.guardian.restart-spark-fail-threshold		配置，默认值为	3。

Bad	Query	被取消失败检查

注意：一些查询会由于异常原因被强行关闭，此时该查询为	Bad	Query，常见情况为超时查询。

由于某些原因，Bad	Query	可能杀不死，如果一直杀不死的话，可能会长期占用资源，如果守护进程检查到有	Bad
Query	被取消次数	>=	阈值，则守护进程会去重启	Kyligence	Enterprise。这个功能默认打开，如果要关闭它，可以在
	$KYLIN_HOME/conf/kylin.properties		中，增加配置	 	kylin.guardian.kill-slow-query-fail-restart-enabled	=
false	，取消次数阈值由参数	 	kylin.guardian.kill-slow-query-fail-threshold		配置，默认值为	3。

Full	GC（Garbage	Collection，Java	中的垃圾回收机制）	时长占比检查

守护进程检测	Kyligence	Enterprise	的	JVM	在最近一段时间内（ 	kylin.guardian.full-gc-check-factor	*
kylin.guardian.check-interval	）Full	GC	时长占比，如果占比超过参数	 	kylin.guardian.full-gc-duration-ratio-
threshold		配置的阈值（默认	75%），则守护进程会去重启	Kyligence	Enterprise，这个功能默认开启，如果想要关

227

守护进程

闭它，可以在	 	$KYLIN_HOME/conf/kylin.properties		中，增加配置	 	kylin.guardian.full-gc-duration-ratio-restart-
enabled	=	false	。

守护进程高可用

为了保证守护进程的高可用，Kyligence	Enterprise	也会周期性的去检查守护进程的状态，如果发现守护进程不存在了，
则自动把它启动起来。这个功能默认打开，如果想要关闭它，可以在	 	$KYLIN_HOME/conf/kylin.properties		中，增加配置
	kylin.guardian.ha-enabled	=	false	。第一次检查的时间延迟是由参数	 	kylin.guardian.ha-check-init-delay		配置（单
位：分钟），默认为	5	分钟，之后检查的时间间隔是由参数	 	kylin.guardian.ha-check-interval		配置（单位：分钟），
默认为	1	分钟检查一次。

Kyligence	Enterprise	内存溢出（Out	of	Memory）自动重启

守护进程支持在	Kyligence	Enterprise	的	JVM	出现	OOM	时重启	Kyligence	Enterprise。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

228

垃圾清理

垃圾清理

在	Kyligence	Enterprise	运行一段时间后，系统可能会产生一定数量的垃圾文件，垃圾文件可能会占用大量的存储空间，
这时就需要进行垃圾清理。

垃圾清理能提高	Kyligence	Enterprise	系统运行的稳定性和性能。有效的垃圾清理不仅能节约存储空间，还能保证
Kyligence	Enterprise	所处的集群生态健康。

默认推荐的定时垃圾清理方式

默认设置下，系统将每日凌晨	0	点自动进行垃圾清理。

如需修改定时垃圾清理的时间和频率，通过在	 	$KYLIN_HOME/conf/kylin.properties		中进行参数调整。默认配置为
	kylin.metadata.ops-cron=0	0	0	*	*	*	，指的是每日凌晨	0	点进行垃圾清理，配置项中从左到右的参数分别表示：
秒，分，时，日，月，周几。通过修改	cron	配置，用户可定制垃圾清理时间，例如，每周六晚	11	点清理，则相应
配置应更改为	 	kylin.metadata.ops-cron=0	0	23	*	*	6	。

自动垃圾清理默认4小时超时，超时后自动终止。默认配置为	 	kylin.metadata.ops-cron-timeout=4h	。

系统定时清理垃圾文件前，会自动备份元数据到	HDFS	路径	 	{kylin.env.hdfs-working-
dir}/{MetadataIdentitiy}/_backup/{yyyy-MM-dd-HH-mm-ss}_backup/metadata.zip	。

关于	cron	配置的更多详细资料可以参考	CronTrigger	介绍。

垃圾清理范围

垃圾清理的范围包括：

无效或过期的元数据：

查询历史。

全部项目的查询历史总数，超过此阈值条数	 	kylin.query.queryhistory.max-size=10000000	(默认)	的查询历
史会被清理。

单个项目的查询超过此阈值条数	 	kylin.query.queryhistory.project-max-size=1000000	(默认)	的查询历史会
被清理。

全部项目的查询历史时间，超过此阈值	 	kylin.query.queryhistory.survival-time-threshold=30d	(默认	30
天)	的查询历史会被清理。此配置还支持单位：毫秒	ms，微秒	us，分钟	m	或	min，小时	h。
清理查询历史时会分多次从数据库删除查询历史记录，每一次删除的记录数上限默认为	2000	条，由
	kylin.query.queryhistory.single-deletion-size=2000	(默认)	配置决定。可以通过修改该配置来增加或者
减少单次删除数据的上限。

实时任务状态/记录表。超过此阈值	 	kylin.streaming.jobstats.survival-time-threshold=7d	(默认	7	天)	的实时任
务会被清理。

无效的优化建议表数据。

过期的容量计费元数据。超过此阈值	 	kylin.garbage.storage.sourceusage-survival-time-threshold=90d	(默认	90
天)	的容量计费信息会被清理。
无效或过期的项目相关元数据。

超过此阈值的	 	kylin.garbage.storage.executable-survival-time-threshold=30d	(默认	30	天)，并且已经完
成的元数据任务会被清理。

审计日志。超过此阈值条数	 	kylin.metadata.audit-log.max-size=500000	（默认）	的审计日志会被清理。

无效或过期的	HDFS	数据：

异步查询结果文件。超过此阈值	 	kylin.query.async.result-retain-days=7d		(默认	7	天)	的	HDFS	异步查询结果
文件会被清理。

HDFS	上无效或过期的文件。包括无效或过期的索引、快照、字典等。

229

垃圾清理

超过此阈值	 	kylin.garbage.storage.cuboid-layout-survival-time-threshold=7d		(默认	7	天)	的HDFS	上的无
效文件会被清理。

HDFS	上的低效索引。

低效存储是指在一定的时间区间内使用频率低于某个阈值的索引和其下构建的数据。您可以在项目的设置

>	基本设置	>	索引优化	>	低效存储中进行某个项目下低效存储定义的配置。
如果关闭智能推荐，垃圾清理时会根据索引优化策略清理性价比较低的索引。您还可以通过点击仪表盘>
存储配额>低效存储下的清除按钮进行手动清理。
如果开启智能推荐，垃圾清理时低效存储的清理不再触发，相应的低效索引会被转为模型优化建议，仪表

盘中也不会出现清理垃圾的按钮。

HDFS	上	 	{working-dir}		下的	spark-history	和	sparder-history	目录的	eventlog	文件

spark-history	记录了构建任务的	eventlog，目录下最后修改时间早于	 	min(当前时间	-
kylin.garbage.storage.executable-survival-time-threshold(默认	30	天)	，系统中最早任务历史的创建时间)		的
eventlog	文件会被清理。
sparder-history	记录了查询任务的	eventlog，目录下最后修改时间早于	 	min(当前时间	-
kylin.query.queryhistory.survival-time-threshold(默认	30	天)	，	系统中最早查询历史的查询时间)		且相应节点处
于启动状态的	eventlog	文件会被清理。如果，子目录中部分文件过期，那么其中的第一个	eventlog	文件不
会被删除。

注意：默认的定时垃圾清理方式，从	Kyligence	Enterprise	4.5.16.0	版本开始及之后，才会清理无效或过期的
HDFS	数据。从	Kyligence	Enterprise	4.6.14.0	版本开始及之后，才会清理	sparder-history	和	spark-history	目
录。

兼容历史上支持的垃圾清理工具

注意：为兼容历史上已经提供的命令行工具清理，之前已提供的工具行为没有改变，已使用此方式的用户可以根

据实际情况逐渐废弃此方式。未使用此工具的用户无需关注此部分内容。

Kyligence	Enterprise	提供了垃圾清理命令行工具，用于	HDFS	数据的检查与清理，从而保证系统处于良好的运行状态。
请您在终端执行如下命令：

$KYLIN_HOME/bin/kylin.sh	io.kyligence.kap.tool.routine.RoutineTool

在不加任何参数执行此命令时，它只会列出	HDFS	中可以清理的数据，但并不会执行真正的清理动作。

此命令支持标准的短参数和长参数，参数说明如下：

	-m，	--metadata	：执行元数据垃圾清理。

	-c，	--cleanup	：执行数据垃圾清理。不带此参数时，工具不会对	HDFS	数据作任何修改。
	-p	[project...],	--projects=[project...]	:	指定待清理的项目。指定多个项目时请使用逗号,隔开。不带此参数
时，工具会对所有项目进行清理。

	-h，	--help	：打印帮助信息。

	-r	number	：访问云环境对象存储时，每秒请求次数。 	-r	10		代表每秒请求	10	次。可使用此参数限制垃圾清理工
具，对云环境对象存储的请求频率，避免超过请求频率限制而出错。

	-t	number	：访问云环境对象存储失败时，请求重试次数。 	-t	3		代表重试	3	次。

在清理	spark-history	和	sparder-history	时有以下注意事项：

因	sparder-history，spark-history	不分项目存储，使用命令行工具	RoutineTool	时，如果使用	-p	参数指定了项目，则
不会清理	sparder-history，spark-history	文件；
因	sparder-history	日志是按照节点存储的，定时垃圾清理任务只能清理启动节点的	sparder-history	日志，而命令行工
具	RoutineTool	可以清理所有节点的	sparder-history	日志（即使节点未启动）；
要求	Kyligence	Enterprise	集群的	spark-history，sparder-history	目录独占。在删除时，不区分文件类型，即目录下，
所有文件只要符合过期标准均会被清理；

多租户部署模式下，由于存储隔离，spark-history	可能清理不全。

230

垃圾清理

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

231

查询限流，保护查询稳定

查询限流，保护查询稳定

查询资源通常是有限的，在某些时段查询量突然增大，或者出现少量大查询抢占过多资源时，可能会出现查询资源竞

争，导致整体查询性能出现大幅波动。

为了避免上述情况，我们可以采用查询限流策略，通过拒绝或限制一小部分的大查询性能，来保证绝大部分的小查询不

受影响，保证查询的整体稳定性。

查询分类

通过长期观察发现，我们可以将查询大致分为两类：大查询和小查询。他们具有不同的典型特点：

大查询：数量少，占用资源多，大查询的波动对查询整体稳定性要求影响大。

小查询：数量多，每个小查询占用资源少，保护小查询，可以有效保证查询的整体稳定性。

根据这两类查询的特点，我们设计了不同的查询限流策略，可以根据需要进行选择。详见下文两种查询限流策略。

同时，针对大查询和小查询的判定，我们也提供了参数，允许用户根据实际情况进行微调。详见下文大查询的判定。

两种查询限流策略

策略一：小查询优先调度策略

开启小查询优先调度策略后，小查询将被优先调度，大查询被后置调度。

在	 	kylin.properties		中设置	 	kylin.query.query-limit-enabled	=	true		以开启小查询优先调度策略。默认值为	false。

策略二：大查询拒绝策略

不同于策略一的大查询后置调度，使用策略二，达到	Spark	任务负载上限后，将会直接拒绝大查询。Spark任务负载指的
是Spark集群中处于Pending状态的任务数与处于Running状态的任务数的比值。该策略需要Ops	Plan的配合来收集任务负
载指标，并在指标数值到达上限时，触发对大查询的拒绝。

在	 	kylin.properties		中设置	 	kylin.query.share-state-switch-implement	=	jdbc	，默认值为	close。

其中	Spark任务负载上限，默认值为	50	，一般不建议修改。

如需配置	Ops	Plan	以开启大查询拒绝策略，请联系	Kyligence	技术支持团队	获取帮助。

大查询的判定

影响上述查询限流策略的效果，一个重要的因素是大查询的判定。我们既提供了默认值，也允许根据实际查询和系统情

况进行灵活调整。

主要原理：

系统主要把数据扫描行数作为判断是否为大查询的依据。一条查询数据扫描行数的加和，当这个值超过阈值，即判定为

大查询，否则为小查询。这个值和查询结果在页面上显示的	“查询扫描记录数”	有可能是不同的，这个行数是指在剪枝
后，扫描的	parquet	文件的行数。

大查询的判定设置：

系统提供了判定是否为大查询的，数据扫描行数阈值的初始阈值设置，也提供了自动更新此阈值机制，下面将详细介绍

相关参数的配置。

如需调整，在	 	kylin.properties		中调整以下参数：

	kylin.query.big-query-source-scan-rows-threshold	：判定是否为大查询的，数据扫描行数初始阈值。默认值为

232

查询限流，保护查询稳定

	-1		，表示用户没有指定，系统在启动时自动计算初始阈值。此外，这个阈值可以在系统运行过程中通过收集查询
信息，自动进行更新以适应集群的环境。

	kylin.query.auto-adjust-big-query-rows-threshold-enabled	：是否自动更新上述阈值。默认值	false，设置为	true	表
示开启自动更新。

	kylin.query.big-query-threshold-update-interval-second	：自动更新上述阈值的间隔。默认值	10800，单位秒。
	kylin.query.big-query-second	：自动更新上述阈值时，大查询需要满足的时间限制，默认值	10，单位秒。

另外，当查询包含	limit	时，也可以开启下面优化，使自动更新阈值更精准，避免大查询误判。

	kylin.query.apply-limit-info-to-source-scan-rows-enabled	：是否应用	limit	信息优化扫描行数估算。默认值
false。

另外，当下压引擎资源充足时，对于大查询可以不拒绝，转成下压查询。

	kylin.query.big-query-pushdown	：是否开启大查询下压。默认值	false。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

233

监控

监控

Kyligence	Enterprise	提供了指标监控和核心服务监控功能，帮助用户及时获取运行状况，本章包含以下内容：

InfluxDB

配置时序数据库	InfluxDB
InfluxDB	维护

指标监控

服务监控

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

234

InfluxDB

InfluxDB

从	Kyligence	Enterprise	4.1.0	开始，系统使用时序数据库	InfluxDB	记录系统的监控信息，本节介绍配置和维护的方法。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

235

InfluxDB

配置时序数据库	-	InfluxDB

准备工作

从	Kyligence	Enterprise	4.1.0	开始，系统使用	RDBMS	存储查询历史，仅使用	InfluxDB	记录系统的监控信息。若您需要
这些信息，则需要预先配置时序数据库	InfluxDB	用于存储系统的监控信息等数据。

我们推荐您使用	Kyligence	Enterprise	安装包中提供的	InfluxDB	1.6.4	作为内置数据库。InfluxDB	安装包	 	influxdb-
1.6.4.x86_64.rpm		位于产品安装包根目录下的	 	influxdb		目录中。

如果您需要使用运行环境中已有的	InfluxDB	数据库，支持的数据库版本为：

InfluxDB	1.6.4	及以上

您可以使用如下命令检查您当前环境中的	InfluxDB	的版本。

service	influxdb	version

	root		用户下安装和配置方法

以下方法适用于安装和配置	InfluxDB	1.6.4	数据库。

1.	 使用如下命令查看环境中是否已经安装	InfluxDB

service	influxdb	status

若尚未安装，您可以进入相应目录，并使用如下命令安装	InfluxDB

cd	$KYLIN_HOME/influxdb

rpm	-ivh	influxdb-1.6.4.x86_64.rpm

2.	 启动	InfluxDB	数据库

service	influxdb	start

默认的，你可以在	 	/var/log/influxdb		查看	Influxdb	的日志。

3.	 如果您的	InfluxDB	端口号出现冲突，您可以使用编辑命令进行修改端口配置。

	vi	/etc/influxdb/influxdb.conf

请您注意以下	3	点：

修改	RPC	端口：初始配置为	 	bind-address	=	"127.0.0.1:8088"	，您可以将	 	8088		端口修改为可用端口，如
	18087	。

修改	HTTP	端口：初始配置为	 	bind-address	=	":8086"	，您可以将	 	8086		端口修改为可用端口，如	 	18086	。
设置	 	reporting-disabled	=	true	,	即关闭定时向	influxdata.com	汇报数据。

4.	 InfluxDB	默认无需用户名和密码即可访问，如果您需要，您可以通过以下方法配置密码：

i.	 登录	InfluxDB

influx	-port	18086

236

InfluxDB

提示：请您根据实际端口号替代上述命令中的	 	18086

ii.	 创建管理员用户和用户密码

CREATE	USER	admin	WITH	PASSWORD	'admin'	WITH	ALL	PRIVILEGES

iii.	 打开配置文件，并修改信息	 	[http]	auth-enabled	=	true		以开启安全登录

vi	/etc/influxdb/influxdb.conf

iv.	 重启	InfluxDB	并重新登录	InfluxDB

service	influxdb	restart

influx	-port	18086	-username	admin	-password	admin

5.	 在	Kyligence	Enterprise	的安装目录下编辑配置文件	 	kylin.properties		修改相应的	InfluxDB	配置信息。注意替换相

应的	 	ip:http_port	， 	user	， 	pwd	， 	ip:rpc_port		值。

vi	$KYLIN_HOME/conf/kylin.properties

###修改如下配置

kylin.influxdb.address=ip:http_port

kylin.influxdb.username=user

kylin.influxdb.password=pwd

kylin.metrics.influx-rpc-service-bind-address=ip:rpc_port

注意：	如果部署了多个	Kyligence	节点，则每一个	Kyligence	节点都需要在	 	kylin.properties		中配置上述Influxdb
配置，并指向同一个	Influxdb	实例。

6.	 支持对influxdb密码的加密

如果需要对influxdb密码进行加密，可以使用如下方式：

i.	在${KYLIN_HOME}路径下执行以下命令，获取加密后的密码

./bin/kylin.sh	io.kyligence.kap.tool.general.CryptTool	-e	AES	-s	<password>

ii.	配置kylin.influxdb.password为如下形式

kylin.influxdb.password=ENC('${encrypted_password}')

iii.	以influxdb的密码为kylin为例

首先，加密influxdb的密码kylin

${KYLIN_HOME}/bin/kylin.sh	io.kyligence.kap.tool.general.CryptTool	-e	AES	-s	kylin

AES	encrypted	password	is:

YeqVr9MakSFbgxEec9sBwg==

然后，配置kylin.influxdb.password，如下：

kylin.influxdb.password=ENC('YeqVr9MakSFbgxEec9sBwg==')

7.	 启动	Kyligence	Enterprise。

237

InfluxDB

非	 	root		用户下安装和配置方法

以下方法适用于安装和配置	InfluxDB	1.6.4	数据库。

1.	 假设以用户	 	abc		的身份安装，新建一个目录并拷贝	InfluxDB	安装包至该目录，然后解压安装包安装

InfluxDB。 	influxdb-1.6.4.x86_64.rpm		安装包位于	 	$KYLIN_HOME/influxdb		目录下。

mkdir	/home/abc/influx

cp	$KYLIN_HOME/influxdb/influxdb-1.6.4.x86_64.rpm	/home/abc/influx

cd	/home/abc/influx

rpm2cpio	influxdb-1.6.4.x86_64.rpm	|	cpio	-idmv

2.	 编辑配置文件，并将全局的	 	/var/lib		替换为	 	/home/abc/influx	，您也可以根据实际情况修改	 	bind-adddress		中

的端口配置。

vi	/home/abc/influx/etc/influxdb/influxdb.conf

3.	 使用如下命令启动	InfluxDB。

nohup	./usr/bin/influxd	run	-config	/home/abc/influx/etc/influxdb/influxdb.conf	&

默认的，你可以在	 	/home/abc/influx/var/log/influxdb		中查看	Influxdb	的日志。

4.	 其他的相关配置请您参考本节第二段 	root		用户下安装和配置方法。特别的，如果需要重启	Influxdb	服务，则需要

使用如下命令，而不能使用参考章节中的	 	service	restart		命令。

ps	-ef	|	grep	influxdb

kill	{pid}

5.	 启动	Kyligence	Enterprise。

InfluxDB	连通性

为了保证	InfluxDB	服务良好的连通，建议您在启动	InfluxDB	后先进行一些测试。

在终端输入命令行登陆	InfluxDB：

/home/abc/influx/usr/bin/influx	-port	18086	-username	${username}	-password	${pwd}

如果登录失败，您可以在配置文件	 	influxdb.conf		中设置为	 	auth-enabled=true	，然后再次尝试登陆。
登录成功后，执行一些简单的查询以检测	InfluxDB	是否配置正确：

show	databases;

如果查询失败，并提示	 	authorization	failed	，请确定登录的用户是否有足够的权限。

更多关于	InfluxDB	连通性的问题，请您查看	InfluxDB	维护章节。

（可选）配置	HTTPS	方式连接	InfluxDB

使用	HTTPS	方式连接	InfluxDB	前，需要先开启	InfluxDB	的	HTTPS	连接方式。启用	InfluxDB	的	HTTPS	请参考官方文
档：Enabling	HTTPS	with	InfluxDB。

如果您使用的	InfluxDB	已经开启	HTTPS	方式连接，请在	 	$KYLIN_HOME/conf/kylin.properties		配置文件中设置如下参
数：

238

InfluxDB

kylin.influxdb.https.enabled=true

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

239

InfluxDB

InfluxDB	维护

本节将介绍基本的	InfluxDB	维护方法。

服务连通性

当出现InfluxDB无法连接时，可以从以下几个方面去定位问题：

1.	 执行	 	service	influxdb	status	，确认	InfluxDB	是否正常启动。若没有启动，可以通过查看

	/var/log/influxdb/influxd.log		或者	 	/var/log/messages		来找出服务被终止的原因，同时执行 	service	influxdb
restart		重新启动服务并观察日志确认服务能够正常完成启动。（正常启动后可以通过	 	influx	-host	?	-port	?		连
接到服务）

2.	 服务启动过程中发现端口被占用，执行	 	netstat	-anp	|	grep	influxdb_port		查看占用端口的进程，并通过	 	ps	-ef

|	grep	pid		查看占用端口的具体程序来决定是杀掉占用程序还是修改InfluxDB服务的端口。

3.	 当	Kyligence	Enterprise	与	InfluxDB	安装在不同的节点时，可以通过在	Kyligence	Enterprise	节点执行	 	telnet

influxdb_ip	influxdb_port		来确认两个节点之间是否能够正常通信，若不能正常通信，可以查看安装	InfluxDB	的
节点上是否配置了防火墙（ 	service	iptables	status	）或者直接联系系统管理员帮忙查看网络环境。

日志管理

日志配置

InfluxDB	默认将日志写入到标准错误输出流	stderr	中，InfluxDB	在启动时默认将	stderr	重定向到了
	/var/log/influxdb/influxd.log		文件中。所以要修改InfluxDB的默认日志路径，可以重新指定	stderr	的重定向
路径，例如：修改	 	/etc/default/influxdb		文件，在里面添加 	STDERR=/path/to/influxdb.log	配置项，最后重
启服务即可（ 	service	influxdb	restart	）

InfluxDB	默认开启了	HTTP	访问日志，这部分日志通常量比较大，可以通过修改	 	[http]	log-enabled	=	false
并重启服务来关闭该部分日志输出。

日志清理

InfluxDB	自身并没有提供对日志进行定期清理的功能，默认是使用	logrotate（linux系统默认安装）来管理日志。配置文
件位于	 	/etc/logrotate.d/influxdb	，默认按天滚动，保留七天。

备份与恢复

InfluxDB	提供了数据的备份与恢复功能。

备份

influxd	backup	-portable	-database	KE_METRIC	-host	127.0.0.1:8089	/path/to/backup

恢复

要求指定的数据库在InfluxDB中存在，否则执行恢复操作将会报错。

influxd	restore	-portable	-database	KE_METRIC	-host	127.0.0.1:8089	/path/to/backup

注意:	在您执行命令时，请替换	KE_METRIC	为您想要备份的数据库名，替换	127.0.0.1:8089	为您实际的	InfluxDB
所在机器的	IP	和端口，替换	 	/path/to/backup		为您想要备份的路径。

监控与诊断

240

InfluxDB

内存监控

查看	runtime

运行以下命令可以了解GC、内存使用等具体情况：	 	influx	-database	KE_METRIC	-execute	"show	stats	for
'runtime'"

请主要关注几个参数：

HeapAlloc	->	堆内存大小
Sys	->	从系统中获得的内存总字节数
NumGC	->	GC次数
PauseTotalNs	->	GC	停顿总时长

查看InfluxDB索引占用内存情况

	show	stats	for	'indexes'

观察	InfluxDB	内存状态

运行以下命令：

	pidstat	-rh	-p	PID	5

若发现内存占用率过高或者GC次数过于频繁，建议您加大内存。

提示:	建议您把	InfluxDB	单独放在一个内存较高的机器，数据的读取和写入速度都直接依赖内存中的索
引。

磁盘监控

运行以下命令查看磁盘情况：

		pidstat	-d	-p	PID	5

当发现磁盘读写负载过高时，可以考虑将WAL目录与data目录分别映射到不同的磁盘上，以减少读写操作的相互影
响。

1.	 运行	 	vi	/etc/default/influxdb		编辑配置文件。

2.	 修改配置项	 	[data]	dir	=	"/var/lib/influxdb/data"		和	 	wal-dir	=	"/var/lib/influxdb/wal"	，将WAL目录和

data目录指向不同的磁盘。

查看	99%	的写入和读取响应时间

1.	 写入：

SELECT	non_negative_derivative(percentile("writeReqDurationNs",	99))	/	non_negative_derivative(max("wr

iteReq"))	/	(1000	*	1000)	AS	"Write	Request"

FROM	"_internal".."httpd"

WHERE	time	>	now()	-	10d

GROUP	BY	time(1h)	fill(0)

2.	 读取：

SELECT	non_negative_derivative(percentile("queryReqDurationNs",	99))	/	non_negative_derivative(max("qu

eryReq"))	/	(1000	*	1000)	AS	"Query	Request"

FROM	"_internal".."httpd"

WHERE	time	>	now()	-	10d

GROUP	BY	time(1h)

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

241

指标监控

指标监控

系统默认每分钟收集一次指标数据，包括存储、查询、构建任务、元数据、清理机制等，监控数据存放在配置指定的

InfluxDB	中，通过	Grafana	展示。可以帮助管理员透视系统的运行状况，以便做好风险预估工作。

注意：由于	Grafana	依赖于	InfluxDB，所以请确保您已经根据	InfluxDB	配置正确且正常启动	InfluxDB，才可使用
Grafana。

Grafana

1.	 工作目录： 	$KYLIN_HOME/grafana
2.	 配置目录： 	$KYLIN_HOME/grafana/conf
3.	 启动grafana命令： 	$KYLIN_HOME/bin/grafana.sh	start
4.	 关闭grafana命令： 	$KYLIN_HOME/bin/grafana.sh	stop

配置更改请参考	Grafana	官网手册	Configuration。

启动成功后打开浏览器访问	Grafana，默认端口：3000，用户名：admin，密码：admin

仪表盘

默认仪表盘 	Kyligence	Enterprise	一共有十个模块：Cluster，Summaries，Models，Queries，Favorites，Jobs，
Cleanings，Metadata	Operations，Transactions，每个模块的定义请参考指标含义。如需更改仪表盘配置请参考	Grafana	官
网手册	Provisioning	Grafana。

面板

每一个指标对应一个具体的监控面板。

时间跨度

242

指标监控

Dashboard右上角快捷选择时间跨度，时间跨度：表示指标观察所在的时间区间。

数据粒度

位于	Dashboard	左上角下拉选择，数据粒度：auto,	1m,	5m,	10m,	30m,	1h,	6h,	12h,	1d,	7d,	14d,	30d（auto	是根据时间跨度
自动调节粒度，比如时间跨度	30min	对应的粒度	5min，再如时间跨度	24h	对应的粒度	4h）。

指标含义

Cluster：集群相关指标
Summaries：全局概览指标
Models：模型相关指标
Queries：查询相关指标
Favorites：Favorite	Query	相关指标
Jobs：任务状态相关指标
Cleanings：清理机制相关指标
Metadata	Operations：元数据操作相关指标
Transactions：事务机制相关指标

243

指标监控

提示：下列表格中"关联项目”表示指标是否与项目相关，"Y"表示指标与项目相关，"N"表示指标与项目无关。"关
联节点"表示是否每个节点都会上传该指标，"Y"表示指标与节点相关，"N"表示指标与节点无关。

Cluster：集群相关指标

名称

build_unavailable_duration

query_unavailable_duration

Summaries：全局概览指标

含义

集群构建不可用时间

集群查询不可用时间

关联项目

N

N

名称

含义

关联
项目

关联节点

备注

summary_exec_total_times

所有指标采集累计次数

summary_exec_total_duration

所有指标采集累计耗时

num_of_projects

系统当前项目总数

storage_size_gauge

系统当前存储空间占用

num_of_users

系统当前承载用户数

num_of_hive_tables

系统当前承载数据表总数

num_of_hive_databases

系统当前承载数据库总数

summary_of_heap

usage_of_heap

count_of_garbage_collection

time_of_garbage_collection

Kyligence	Enterprise	节点堆内
存情况

Kyligence	Enterprise	节点堆内
存使用率

Kyligence	Enterprise	节点垃圾
回收次数

Kyligence	Enterprise	节点垃圾
回收总时间

garbage_size_gauge

系统垃圾当前存储空间占用

sparder_restart_total_times

sparder	累计重启次数

query_load

spark	sql	的负载

cpu_cores

kylin.properties	中配置的查询
用的cup核数

N

N

N

Y

N

Y

Y

N

N

N

N

Y

N

N

N

Models：模型相关指标

Y(all,	job,
query)

Y(all,	job,
query)

评估指标采集成本

评估指标采集成本

N

N

N

N

N

Y(all,	job,
query)

Y(all,	job,
query)

Y(all,	job,
query)

Y(all,	job,
query)

-

-

-

-

-

-

-

-

-

N

参考"垃圾"定义

Y(all,	job,
query)

"Sparder"	是内置查
询引擎

Y(all,
query)

Y(all,
query)

-

参考	"与	Spark	相关
的配置项"

名称

含义

关联项目

关联节点

model_num_gauge

模型数时间变化曲线

non_broken_model_num_gauge

健康模型数时间变化曲线

last_query_time_of_models

模型最后访问时间

hit_count_of_models

storage_of_models

查询击中模型次数

模型存储大小

Y

Y

Y

Y

Y

N

N

N

N

N

244

指标监控

segments_num_of_models

模型中segments的数量

model_build_duration

model_wait_duration

number_of_indexes

expansion_rate_of_models

模型构建时长

模型等待时长

模型索引数

模型膨胀率

model_build_duration(avg)

模型构建平均时长

Queries：查询相关指标

Y

Y

Y

Y

Y

Y

N

N

N

N

N

N

名称

含义

关联
项目

关联节
点

备
注

count_of_queries

查询累计次数

num_of_query_per_host

节点查询数量

count_of_queries_hitting_agg_index

击中聚合索引的查询数量

ratio_of_queries_hitting_agg_index

击中聚合索引的查询比例

count_of_queries_hitting_table_index

击中表索引的查询数量

ratio_of_queries_hitting_table_index

击中表索引的查询比例

count_of_pushdown_queries

下压查询的数量

ratio_of_pushdown_queries

下压查询的比例

count_of_queries_hitting_cache

击中缓存的查询数量

ratio_of_queries_hitting_cache

击中缓存的查询比例

count_of_queries_less_than_1s

查询时间小于	1	秒的查询数量

ratio_of_queries_less_than_1s

查询时间小于	1	秒的查询比例

count_of_queries_between_1s_and_3s

查询时间在	1	秒和	3	秒之间的查询数量

ration_of_queries_between_1s_and_3s

查询时间在	1	秒和	3	秒之间的查询比例

count_of_queries_between_3s_and_5s

查询时间在	3	秒和	5	秒之间的查询数量

ratio_of_queries_between_3s_and_5s

查询时间在	3	秒和	5	秒之间的查询比例

count_of_queries_between_5s_and_10s

ratio_of_queries_between_5s_and_10s

查询时间在	5	秒和	10	秒之间的查询数
量

查询时间在	5	秒和	10	秒之间的查询比
例

Y

N

Y

Y

Y

Y

Y

Y

Y

Y

Y

Y

Y

Y

Y

Y

Y

Y

Y(all,
query)

Y(all,
query)

Y(all,
query)

Y(all,
query)

Y(all,
query)

Y(all,
query)

Y(all,
query)

Y(all,
query)

Y(all,
query)

Y(all,
query)

Y(all,
query)

Y(all,
query)

Y(all,
query)

Y(all,
query)

Y(all,
query)

Y(all,
query)

Y(all,
query)

Y(all,
query)

-

-

-

-

-

-

-

-

-

-

-

-

-

-

-

-

-

-

245

指标监控

例

count_of_queries_greater_than_10s

查询时间大于	10	秒的查询数量

ratio_of_queries_greater_than_10s

查询时间大于	10	秒的查询比例

count_of_timeout_queries

超时查询的数量

count_of_failed_queries

失败查询的数量

mean_time_of_query_per_host

节点平均查询时间

99%_of_query_latency

gt10s_query_rate_5-minute

failed_query_rate_5-minute

pushdown_query_rate_5-minute

百分之九十九的查询都能在这个耗时内
完成

耗时超过	10	秒的查询，5	分钟内每秒钟
发生的次数

失败的查询，5	分钟内每秒钟发生的次
数

下压的查询，5	分钟内每秒钟发生的次
数

scan_bytes_of_99%_queries

99%	的查询扫描数据量小于这个值

query_scan_bytes_of_host

每个	Kyligence	Enterprise	节点的扫描数
据量

mean_scan_bytes_of_queries

查询的平均扫描数据量

Favorites：Favorite	Query	相关指标

名称

含义

fq_accepted_total_times

fq_proposed_total_times

fq_proposed_total_duration

failed_fq_proposed_total_times

fq_adjusted_total_times

fq_adjusted_total_duration

fq_update_usage_total_times

用户提交	Favorite
Query	累计次数

后台触发	Favorite
Query	累计次数

后台触发	Favorite
Query	累计耗时

后台触发	Favorite
Query	失败累计次数

调整	Favorite	Query
累计次数

调整	Favorite	Query
累计耗时

更新	Favorite	Query
使用统计信息累计次
数

关
联
项
目

Y

Y

Y

Y

Y

Y

关联
节点

Y(all,
job,
query)

N

N

N

Y(all,
job,
query)

Y(all,
job,
query)

Y

N

query)

Y(all,

query)

Y(all,
query)

Y(all,
query)

Y(all,
query)

Y(all,
query)

Y(all,
query)

Y(all,
query)

Y(all,
query)

Y(all,
query)

Y(all,
query)

Y(all,
query)

Y(all,
query)

-

-

-

-

-

-

-

-

-

-

-

-

Y

Y

Y

Y

N

Y

Y

Y

Y

Y

N

Y

备注

-

-

-

参考"Pushdown"定义

-

-

-

246

指标监控

fq_update_usage_total_duration

failed_fq_update_usage_total_times

fq_tobeaccelerated_num_gauge

fq_accelerated_num_gauge

fq_failed_num_gauge

fq_accelerating_num_gauge

fq_pending_num_gauge

fq_blacklist_num_gauge

Jobs：任务状态相关指标

名称

num_of_jobs_created

num_of_jobs_finished

num_of_running_jobs

num_of_pending_jobs

num_of_error_jobs

count_of_error_jobs

finished_jobs_total_duration

job_duration_99p

更新	Favorite	Query
使用统计信息累计耗
时

更新	Favorite	Query
使用统计信息失败累
计次数

系统当前待加速
Favorite	Query	总数

系统当前已加速
Favorite	Query	总数

系统当前加速失败
Favorite	Query	总数

系统当前加速中
Favorite	Query	总数

系统当前处于阻断状
态的	Favorite	Query
总数

系统当前处于黑名单
中的	Favorite	Query
总数

Y

N

Y

Y

Y

Y

Y

Y

N

N

N

N

N

N

-

-

-

-

-

-

Favorite	Query	缺少必要的条
件，例如列名不存在，需要用
户干预

Y

N

参考"黑名单"定义

含义

关联项目

关联节点

任务创建累计总数

任务完成累计总数

正在运行的任务数量

正在等待执行的任务数量

失败的任务数量

失败的任务累计总数

任务完成累计耗时

任务耗时99分布

Y

Y

Y

Y

Y

Y

Y

Y

Y

Y

Y

Y

Y

Y

Y(all,	job)

Y(all,	job)

N

N

N

Y(all,	job)

Y(all,	job)

Y(all,	job)

Y(all,	job)

Y(all,	job)

Y(all,	job)

Y(all,	job)

Y(all,	job)

Y(all,	job)

job_step_attempted_total_times

任务尝试累计次数

failed_job_step_attempted_total_times

失败任务尝试累计次数

job_resumed_total_times

job_discarded_total_times

job_duration

job_wait_duration

Cleanings：清理机制相关指标

任务恢复累计次数

任务丢弃累计次数

任务构建时长

任务等待时长

名称

含义

关联项目

关联节点

storage_clean_total_times

存储空间清理累计次数

storage_clean_total_duration

存储空间清理累计耗时

failed_storage_clean_total_times

存储空间清理失败累计次数

N

N

N

Y(all,	job,	query)

Y(all,	job,	query)

Y(all,	job,	query)

247

指标监控

failed_storage_clean_total_times

存储空间清理失败累计次数

N

Y(all,	job,	query)

Metadata	Operations：元数据操作相关指标

名称

metadata_clean_total_times

metadata_backup_total_times

metadata_backup_total_duration

failed_metadata_backup_total_times

metadata_ops_total_times

metadata_success_ops_total_times

Transactions：事务机制相关指标

关
联
项
目

Y

Y

Y

Y

N

N

关联
节点

Y(all,
job,
query)

Y(all,
job,
query)

Y(all,
job,
query)

Y(all,
job,
query)

Y(all,
job,
query)

Y(all,
job,
query)

含义

元数据清
理累计次
数

元数据备
份累计次
数

元数据备
份累计耗
时

元数据备
份失败累
计次数

元数据日
常操作累
计次数

元数据日
常操作失
败累计次
数

备注

-

区分项目和全局

区分项目和全局

区分项目和全局

每天固定时间（可配置）：自动备份元数
据；rotate	audit_log；清理元数据和存储空
间；调整fq；清理query	history。

-

名称

含义

关联项目

关联节点

备注

transaction_retry_total_times

事务重试累计次数

transaction_latency_99p

事务执行耗时99分布

Y

Y

Y(all,	job,	query)

区分项目和全局

Y(all,	job,	query)

区分项目和全局

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

248

服务监控

服务监控

从	4.1.0	版本后，Kyligence	Enterprise	给用户提供了核心服务的监控功能，帮助用户获取对应的监控状态，完成日常的运
维工作。

Kyligence	Enterprise	的核心功能可以分为查询服务于构建服务的功能，目前针对这两个核心功能的提供了以下的监控方
式：

1.	 查询功能：Kyligence	Enterprise	集群查询节点都会收集当前节点的查询状态，并记录到	InfluxDB	中。
2.	 构建功能：Kyligence	Enterprise	集群	All	节点会收集当前所有构建作业的状态，根据算法判断是否存在堆积和异常

情况，并记录到	InfluxDB	中。

当前提供两个	Rest	API	进行监控与数据查看，也可以集成该接口至自己的监控告警平台实现	Kyligence	服务监控

获取	Kyligence	Enterprise	集群最新的查询和构建功能状态，如果出现	 	WARNING		和	 	CRASH	，表示集群处于不稳定状
态

获取	Kyligence	Enterprise	集群一段时间内查询和构建功能的不可用时长，并且可以根据其中的详细监控数据来回顾
和追踪问题。

使用方式

获取当前集群状态

	GET	http://host:port/kylin/api/monitor/status

HTTP	Header

Accept:	application/vnd.apache.kylin-v4-public+json

Accept-Language:	en

Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

'http://host:port/kylin/api/monitor/status'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	en'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'

响应字段

	active_instances		当前集群中活跃节点数
	query_status		集群查询功能状态	，分为	GOOD	/	WARNING	/	CRASH
	job_status		集群构建功能状态	，分为	GOOD	/	WARNING	/	CRASH
	job		所有具备构建功能节点的状态	，详情中将展示各实例信息与状态
	query		所有具备查询功能节点的状态	，详情中将展示各实例信息与状态

响应示例

{

				"code":	"000",

				"data":	{

								"active_instances":	1,

								"query_status":	"GOOD",

								"job_status":	"GOOD",

								"job":	[

												{

																"instance":	"sandbox.hortonworks.com:7070",

249

服务监控

																"status":	"GOOD"

												}

								],

								"query":	[

												{

																"instance":	"sandbox.hortonworks.com:7070",

																"status":	"GOOD"

												}

								]

				},

				"msg":	""

}

获取指定范围内集群运行详情

	GET	http://host:port/kylin/api/monitor/status/statistics

HTTP	Header

Accept:	application/vnd.apache.kylin-v4-public+json

Accept-Language:	en

Content-Type:	application/json;charset=utf-8

URL	Parameters

	start		-	 	必选		 	Long		时间戳，统计集群指定时间大于等于该时间内的监控数据
	end		-	 	必选		 	Long		时间戳，统计集群指定时间小于该时间内的监控数据

Curl	请求示例

curl	-X	GET	\

		'http://host:port/kylin/api/monitor/status/statistics?start=1583562358466&end=1583562358466'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	en'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应字段

	Start		监控数据的起始时间，会按监控数据的打点周期向下取整。当打点间隔为	1	分钟时，此时仅会统计到
分钟级别。例如传参为	 	1587353550000		时，则会转化为	 	1587353520000	。因此统计时获取的数据可能有差异。
	end		监控数据的结束时间，会按监控数据的打点周期向下取整。当打点间隔为	1	分钟时，此时仅会统计到分
钟级别。例如传参为	 	1587353550000		时，则会转化为	 	1587353520000	。因此统计时获取的数据可能有差异。
	interval		监控数据的打点周期，默认为	60000	毫秒	（1	分钟）
	job		所有具有构建功能节点的详细信息，和不可用时长/次数，不可用时长单位为毫秒
	query		所有具有查询功能节点的详细信息，和不可用时长/次数，不可用时长单位为毫秒

响应示例

{

				"code":"000",

				"data":{

								"start":1584151560000,

								"end":1584151680000,

								"interval":60000,

								"job":[

												{

																"instance":"sandbox.hortonworks.com:7070",

																"details":[

																				{

																								"time":1584151572650,

																								"status":"GOOD"

																				},

																				{

																								"time":1584151632770,

250

服务监控

																								"status":"GOOD"

																				}

																],

																"unavailable_time":0,

																"unavailable_count":0

												}

								],

								"query":[

												{

																"instance":"sandbox.hortonworks.com:7070",

																"details":[

																				{

																								"time":1584151609142,

																								"status":"GOOD"

																				},

																				{

																								"time":1584151669142,

																								"status":"GOOD"

																				}

																],

																"unavailable_time":0,

																"unavailable_count":0

												}

								]

				},

				"msg":""

}

已知问题

1.	 查询检测目前仅会发送常量查询，不会扫描到	HDFS	文件
2.	 InfluxDB	组件目前暂无高可用方案，因此可能当	InfluxDB	不可用时，可能存在部分数据缺失
3.	 大量删除及终止任务可能会影响到节点状态的判断
4.	 由于系统监控依赖于配置	InfluxDB，若在未配置	InfluxDB	的时候仍然开启系统监控功能（默认开启），可能造成

日志中出现一定无用报错。所以当未配置	InfluxDB	时，建议在	 	kylin.properties		中配
置 	kylin.monitor.enabled=false		以关闭系统监控功能。关闭系统监控功能后，将无法通过	Grafana	或	Kyligence
Manager	查看新的监控数据。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

251

日志类型

日志类型

本章主要介绍日志的类型、存储位置以及查看方式，包含以下内容：

审计日志

系统日志

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

252

审计日志

审计日志

基本概念

在数据库中，	Audit	Log	主要用于监视并记录对数据的操作行为，简单理解为日志。

Kyligence	Enterprise	实例是无状态的服务，所有的状态信息都存储元数据中，让数据发生变更的所有操作，都会创建或
修改元数据，元数据的改动被包含在一个数据库事务中，同时，每一次对元数据的修改会记录在审计日志中，相当于元

数据每个版本的快照。引入	Audit	Log	机制，不仅可以通过	Audit	Log	对元数据进行监控，还能有助于灾备恢复。

注意：Audit	Log	仅能视为元数据的日志，用于监控及排查问题，可通过它修复部分元数据。如果要保证系统稳
定，需要确保元数据正确性并及时备份元数据。

Kyligence	Enterprise	第一次启动时，根据您在配置文件	 	kylin.properties		中，针对配置项	 	kylin.metadata.url		填写的
元数据表名，在元数据库中创建名为	 	{identifier}_audit_log		的审计表，相对于	metadata	表多了	 	_audit_log		后缀。

例如：

	kylin.metadata.url=ke_metadata@jdbc,driverClassName=org.postgresql.Driver,url=jdbc:postgresql://sandbox:5432/kylin,

username=postgres,password=

元数据库名为	 	kylin		，元数据表名为	 	ke_metadata	，Audit	Log	表名为	 	ke_metadata_audit_log		。

在	Kyligence	Enterprise	中，默认使用	PostgreSQL	作为元数据库，后续以	PostgreSQL	作为示例。

Audit	Log	表字段说明

name

id

type（postgresql）

type(mysql)

description

bigserial

bigint

自增	id

meta_key

varchar(255)

varchar(255)

metadata	的	key，与	metadata	表中的
META_TABLE_KEY	字段对应

meta_content

bytea

longblob

当前版本的	metadata	的内容，当进行删除操作时，此项
值为	NULL

meta_ts

bigint

meta_mvcc

bigint

bigint

bigint

更新时间戳，当进行删除操作时，此项值为	NULL

metadata	的版本，从	0	开始，当进行删除操作时，此项
值为	NULL

varchar(255)

varchar(255)

事务	id

varchar(255)

varchar(255)

操作的	username

varchar

varchar

操作的实例信息

unit_id

operator

instance

版本信息

metadata	表中的	 	meta_table_key		字段与	audit	log	表中的	 	meta_key		进行关联。

元数据版本：在	metadata	表中， 	meta_table_mvcc		字段记录每项元数据的最新版本号；

审计日志版本：在	audit	log	表中， 	meta_mvcc		字段记录版本号，可根据	 	meta_key		字段筛选查看某一项元数据的所
有历史版本；

功能

通过审计日志，可以实现如下功能：

253

审计日志

查看所有	/	某项元数据的更改记录及对应的操作用户
查看某次事务中对哪些元数据进行了修改

查看某段时间内的审计日志

助于元数据灾备恢复

样例

工具

PostgreSQL	客户端工具：DBeaver

表说明

元数据表信息

如图，meta_key	字段为元数据项，meta_content	为元数据值。meta_key	值以 	/_global	开头表示全局的
metadata， 	/project_name		开头表示某个项目的	metadata， 	/UUID		是全局唯一识别码，作为一份元数据的标识符。

例如：

	_global/user/ADMIN		表示	ADMIN	用户的元数据信息，具体信息在	meta_content	字段；
	_global/project/kylin.json		表示名为	kylin	项目的元数据信息；
	/${project_name}/model_desc/${model_id}		表示某个项目的模型描述信息；

基本操作

1.	 查看某项	metadata	的历史记录

254

审计日志

select	*	from	ke_metadata_audit_log	where	meta_key	=	'/_global/project/default.json';

2.	 查看某个模型的历史记录

select	*	from	ke_metadata_audit_log	where	meta_key	=	'/project/model_desc/49529000-c161-4013-bb80-9a78f4f02

48d.json'

3.	 查看某次事务中都对哪些	metadata	进行了修改

select	*	from	ke_metadata_audit_log	where	unit_id	=	'6090bfb5-2401-4176-8475-fe6fd82bc439';

4.	 查看某时间段内	metadata	的审计日志

select	*	from	ke_metadata_audit_log	where	meta_ts	>	1325376000000	and	meta_ts	<	1328054400000	;

5.	 关联	metadata	表，查看某个用户历史记录变化

select	a.meta_mvcc,	a.meta_content,	b.meta_table_mvcc,	b.meta_table_content	from	ke_metadata_audit_log	a	le

ft	join	ke_metadata	b	on	a.meta_key	=	b.meta_table_key	where	a.meta_key	=	'/_global/user/ADMIN'

实际场景示例

监控用户密码是否被修改

ADMIN	用户非常重要，不允许系统管理员之外的人修改密码，可对	meta_key	为	 	/_global/user/ADMIN		的
meta_content	内容进行监控，其中有一个字段为	password，如果这个值发生变化，说明密码被修改。

修改密码前后	meta_mvcc	字段版本号增加，meta_content	字段中	password	值发生变化，并且	default_password	的值也由
true	变为	false：

监控模型是否被修改

255

审计日志

假设项目名称为	kylin，模型名称为	test_model	的表连接关系不允许修改，可以在	Kyligence	Enterprise	模型页面，查
看某个模型的	JSON	格式，其中的	uuid	表示模型	id，那么对应的	meta_key	为 	/kylin/model_desc/${model_id}	，监
控对应的	meta_mvcc	字段值是否增长，如果有变化说明模型被修改。

第二条记录是对模型的时间分区列的格式进行改变，并且两条记录的	unit_id	字段值不一样，说明这两次更改是在不同
事务进行的，查看	operator	字段操作用户为	ADMIN：

配置说明

在	Kyligence	Enterprise	配置文件	 	kylin.properties		中，有以下关于审计日志的配置项，可根据需要进行修改。请确保
审计日志所在的节点有足够的磁盘空间。

	kylin.metadata.audit-log.max-size=500000		审计日志默认存储最近	500,000	行，默认每天凌晨会对多余的操作日志
进行清理，可以修改该配置项进行调整。

导出	Audit	Log

Audit	Log	存在数据库中，可通过	Kyligence	Enterprise	提供的工具，将指定时间范围内的数据导出到本地作为备份，或
着在遇到问题时，将其导出后作为	Kyligence	Enterprise	工单的附件提交，方便技术支持人员进行问题定位。

有以下两种方法，在	KE	节点上执行命令：

1.	 使用打诊断包命令：	 	${KYLIN_HOME}/bin/diag.sh

默认会获取最近	3	天的	Audit	Log，存放于诊断包目录的	 	audit_log/${starttime}_${endtime}.jsonl		文件中；

1.	 使用	AuditLogTool	工具：	 	${KYLIN_HOME}/bin/kylin.sh	io.kyligence.kap.tool.AuditLogTool	-startTime	${starttime}

-endTime	${endtime}	-dir	${target_dir}

	${starttime}		和	 	${endtime}		表示获取指定范围的	Audit	Log，格式是毫秒单位的时间戳，如
	1579868382749	；

256

审计日志

	${target_dir}		指定您	Audit	Log	文件的存放目录，生成的	Audit	Log	存放于
	${target_dir}/${starttime}_${endtime}		文件中；

导入	Audit	Log

如果您在本地有已经导出的	Audit	Log	文件，想通过数据库进行查看分析，可使用以下方式进行导入。

在已有	Kyligence	Enterprise	环境的机器上，使用	AuditLogTool	工具： 	${KYLIN_HOME}/kylin.sh
io.kyligence.kap.tool.AuditLogTool	-restore	-table	${target_table_name}	-dir	${auditlog_dir}

	${target_table_name}		参数指定要生成的	Audit	Log	表名，注意不要与该	Kyligence	Enterprise	环境中已有的	Audit
Log	表重名。
	${auditlog_dir}		参数指定	Audit	Log	文件所在的目录；

命令执行完成后，会在	 	${KYLIN_HOME}/conf/kylin.properties		文件中该配置项	 	kylin.metadata.url		指定的元数据库下
生成	Audit	Log	表。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

257

系统日志

系统日志

Kyligence	Enterprise	顺利启动后，默认会在安装目录下生成 	logs/	目录，所有	Kyligence	Enterprise	运行过程中生成的日
志文件会保存在该目录中。

日志文件

Kyligence	Enterprise	生成的日志文件如下：

	kylin.log

该文件是主要的日志文件，其中与	Kyligence	Enterprise	相关的日志级别默认是DEBUG。

	kylin.out

该文件是标准输出的重定向文件，一些非	Kyligence	Enterprise	生成的标准输出（如	tomcat	启动输出、Hive	命令行输出
等）将被重定向到该文件。

	kylin.gc

该文件是	Kyligence	Enterprise	的	Java	进程记录的	GC(Garbage	Collection)	日志。为避免多次启动，旧文件被覆盖，该日
志使用了进程号作为文件名后缀（如	 	kylin.gc.20003.0.current	）。

	access_log

该文件是	Kyligence	Enterprise	的	Tomcat	访问日志，负责记录所有的	HTTP	请求响应信息。比如	User-Agent，访问的
URL	等。

	jstack.timed.log

该文件是	Kyligence	Enterprise	的	Java	线程堆栈日志，负责记录和定位一些线程运行情况。为避免浪费存储，该文件最大
保留20个。超过最大值时，新文件默认会覆盖创建最早的日志文件。

注意:因为	jstack	的运行依赖于	jvm	在	/tmp	目录下写入的	.java_pid	文件，如果该文件被删除（比如配置了定时清
理/tmp的脚本），会导致	jstack	无法正常运行，从而不会产生	jstack.timed.log	文件

	check-env.out

该文件是执行 	check-env.sh	脚本标准输出的重定向文件。

	check-env.error

该文件是执行 	check-env.sh	脚本错误信息的日志文件。

	shell.stderr

该文件是在命令行界面执行操作生成的日志文件。

	shell.stdout

该文件是在命令行界面执行操作的标准输出的重定向文件。

	kylin.security.log

258

系统日志

该文件是记录系统启动、停止、升级、登录登出的日志文件。

注意：当使用	LDAP	服务实现用户认证时，每次登录失败会记录两条日志。因为使用	LDAP	服务时，如果登录失
败，会尝试另一种方式进行认证。

	kylin.schedule.log

该文件记录任务调度相关的日志，日志级别是DEBUG。

	kylin.query.log

该文件记录查询相关的日志，日志级别是DEBUG。

	kylin.smart.log

该文件记录推荐相关的日志，日志级别是DEBUG。

	kylin.build.log

该文件记录构建相关的日志，日志级别是DEBUG。

	kylin.metadata.log

该文件记录元数据和事务操作相关的日志，日志级别是DEBUG。

	dump.hprof

Kyligence	Enterprise	内存溢出时，该文件会将全部	heap	转储下来，方便排查内存溢出的原因。

注意：当您内存设置较大且发生内存溢出情况时，该文件	dump.hprof	会占据较大存储空间，可能导致您的磁盘空
间不足，节点异常。可手动清理该历史文件。

日志分析

以查询为例，在	Web	UI	执行一个查询，当查询结束，我们会在 	kylin.query.log	看到如下日志片段：

==========================[QUERY]===============================

Query	Id:	8586e718-67b4-c840-61b4-a8898415a154

SQL:	select	lo_revenue	as	from	p_lineorder;

User:	ADMIN

Success:	true

Duration:	1.243

Project:	ssb100_10

Realization	Names:	[AUTO_MODEL_P_LINEORDER_1]

Index	Layout	Ids:	[30001]

Snapshot	Names:	[]

Is	Partial	Match	Model:	[false]

Scan	rows:	[35000]

Total	Scan	rows:	35000

Scan	bytes:	[246530]

Total	Scan	Bytes:	246530

Result	Row	Count:	280

Shuffle	partitions:	1

Hit	Exception	Cache:	false

Storage	Cache	Used:	false

Storage	Cache	Type:	null

Is	Query	Push-Down:	false

Is	Prepare:	false

Is	Timeout:	false

Time	Line	Schema:	massage,end	calcite	parse	sql,end_convert_to_relnode,end_calcite_optimize,end_plan,collect_ol

ap_context_info,end	select	realization,end_rewrite,to_spark_plan,seg_pruning,fetch_file_status,shard_pruning,ex

259

系统日志

ecuted_plan,collect_result

Time	Line:	6,1,4,11,0,0,1,1,14,6,0,0,1,1198

Message:	null

Is	forced	to	Push-Down:	false

User	Agent:	null

Scan	Segment	Count:	1

Scan	File	Count:	1

Is	Refused:	false

==========================[QUERY]===============================

上述片段中主要字段的介绍如下：

	Query	Id	：	查询	ID
	SQL	：	查询所用	SQL	语句
	User	：	执行查询的用户名
	Success	：	查询结果状态标志，true	执行成功，false	执行失败
	Duration	：	查询耗时（单位：秒）
	Project	：	查询使用的项目名称
	Realization	Names	：	查询击中的模型名称
	Index	Layout	Ids	：	查询命中的	layout	的	ID
	Snapshot	Names	：	查询击中的	snapshot
	Is	Partial	Match	Model	：	部分击中模型，比如A	left	B，你单查表A
	Scan	rows	：	查询扫描的数据行数
	Total	Scan	rows	：	查询扫描的数据总行数
	Scan	bytes	：	查询扫描的数据字节数
	Total	Scan	Bytes		：	查询扫描的数据总字节数
	Result	Row	Count	：	查询返回的数据行数
	Shuffle	partitions	：	spark	查询参数，影响	shuffle	过后生成多少个	partition/task。由	kylin.query.engine.sparkl-sql-
shuffle-parittions	或者动态计算得出，计算公式：	min（数据大小估算出的值，	spark	集群总核数）
	Hit	Exception	Cache	：	是否击中失败查询的缓存
	Storage	Cache	Used	：	是否击中成功查询的缓存
	Storage	Cache	Type	：	击中查询的缓存类型
	Is	Query	Push-Down	：是否是下压查询

	Is	Prepare	：	是否是探测查询（	BI	发送过来的查询此项会为	true	）
	Is	Timeout	：	是否超时
	Time	Line	Schema	：	查询模块中的步骤
	Time	Line	：	查询模块中每一个步骤的耗时（毫秒）
	Message	：查询页面提示信息，查询成功此项为	null
	Is	forced	to	Push-Down	：	是否强制下压
	User	Agent	：	提交查询所使用的环境信息
	Scan	Segment	Count	：	扫描	segment	数量
	Scan	File	Count	：	扫描文件数量
	Is	Refused	：是否触发查询限流规则而被拒绝执行

日志配置

Kyligence	Enterprise使用	log4j2	对日志进行配置，用户可以编辑	 	$KYLIN_HOME/server/conf/		目录中的	 	kylin-server-
log4j.xml		文件，对日志级别、路径等进行修改。	修改后，需要重启Kyligence	Enterprise使配置生效。

所有以	kylin	开头，log	结尾的日志的配置在 	kylin-server-log4j.xml		中，配置代码如下

								<Routing	name="routing">

												<Routes	pattern="{%	math	%}{ctx:logCategory}">

																<Route>

																				<RollingFile	name="rolling-${ctx:logCategory}"

260

系统日志

																																	fileName="${env:KYLIN_HOME}/logs/kylin.${ctx:logCategory}.log"

																																	filePattern="${env:KYLIN_HOME}/logs/kylin.${ctx:logCategory}.log.%i">

																								<Policies>

																												<SizeBasedTriggeringPolicy	size="268435456"/>

																								</Policies>

																								<DefaultRolloverStrategy	max="10"/>

																								<PatternLayout	pattern="%d{ISO8601}	%-5p	%X{request.project}[%t]	%c{2}	:	%mask{%m}%n"/>

																				</RollingFile>

																</Route>

																<Route	ref="server"	key="{%	endmath	%}{ctx:logCategory}"/>

												</Routes>

								</Routing>

在默认配置下，当日志文件达到256MB时触发日志滚动，保留最近10个日志文件

如果您需要对其中某个日志文件（比如kylin.query.log）进行单独的配置,	您需要在上述配置代码中	Routes	配置下新增一
个	Route	,将	key	配置为对应的日志文件名字（query，schedule等）	需要注意的是，新增的route需要配置在现有的route之
前,	否则不会生效

下面是一个例子，修改kylin.query.log的滚动策略为每天零点触发，备份最近5个log

<Route	key="query">

				<RollingFile	name="rolling-${ctx:logCategory}"	fileName="${env:KYLIN_HOME}/logs/kylin.${ctx:logCategory}.lo

g"	filePattern="${env:KYLIN_HOME}/logs/kylin.${ctx:logCategory}.log.%i">

								<Policies>

												<CronTriggeringPolicy	schedule="0	0	0	*	*	?"/>

								</Policies>

								<DefaultRolloverStrategy	max="5"	/>

								<PatternLayout	pattern="%d{ISO8601}	%-5p	%X{request.project}[%t]	%c{2}	:	%mask{%m}%n"	/>

				</RollingFile>

</Route>

如果您需要对	kylin.log	进行单独配置，您可以修改	RollingRandomAccessFile	配置，比如将保留文件数量修改为	5

<RollingRandomAccessFile	name="server"	fileName="${env:KYLIN_HOME}/logs/kylin.log"	append="true"

																									filePattern="${env:KYLIN_HOME}/logs/kylin.log.%i"	immediateFlush="false"	>

				<Policies>

								<SizeBasedTriggeringPolicy	size="268435456"/>

				</Policies>

				<DefaultRolloverStrategy	max="5"/>

				<PatternLayout	pattern="%d{ISO8601}	%-5p	%X{request.project}[%t]	%c{2}	:	%mask{%m}%n"/>

</RollingRandomAccessFile>

日志里的错误码

日志错误码的格式是	Kyligence	Enterprise-AABBBCCC，AA指的是报错的模块，BBB是更细的业务报错，CCC错误编号

AA

描述

00

10

20

30

40

50

公共类

界面类

查询类

构建类

系统类

工具类

BBB

描述

261

系统日志

000

001

002

003

004

005

006

007

008

009

010

011

012

013

014

015

016

017

018

019

020

021

022

023

024

025

026

027

028

通用

项目

模型

用户

用户组

密码

列

表

数据库

度量

维度

可计算列

索引

任务

sql表达式

许可证

邮箱

文件

kerberos

catalog

推荐

服务器

segment

诊断包

权限

脚本

元数据

加速

json

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

262

获取技术支持

获取技术支持

Kyligence	提供对	Kyligence	Enterprise	的原厂支持，企业级用户可以在	Kyligence	支持中心	使用知识库功能自助搜索获得
相应的答案，或者通过工单快速提交相关的支持请求。

以下是	Kyligence	支持中心	的使用教程：

知识库

创建工单

查看工单

关闭工单

用户手册与发布声明

知识库

1.	 点击左侧导航栏中的知识库标签，进入知识库界面。

2.	 您可以通过输入关键词来搜索是否有已有的知识库文章来解决您的问题。

创建工单

1.	 点击我的工单	-->	+	创建工单，进入创建工单界面

263

获取技术支持

2.	 在创建工单界面，在相应位置填选标题、环境、严重性、问题分类、问题描述，可通过添加附件按钮上传诊断包、

图片等附件从而更详实地描述问题，最后请点击提交按钮，完成工单的创建流程。

注意：

i.	 严重性请根据问题对业务的影响范围进行选择，如不符，Kyligence	技术支持会根据实际情况做相应调

整。

ii.	 如何生成诊断包请参考诊断包工具章节。
iii.	 附件最大支持上传	2GB。

查看工单

在我的工单界面可以看到所有工单的摘要信息，可以通过点击工单号进入工单详情页面。

工单状态一般分为处理中、待您回复、待您确认和已关闭四种状态。

关闭工单

您可以在工单详情页面点击关闭工单按钮，从而关闭工单。

264

获取技术支持

关闭工单

在关闭工单后，请您进行工单满意度调查，我们期待您的反馈意见以便提高我们的服务质量。

用户手册与发布声明

用户手册

在知识库界面的右侧，可以找到用户手册的模块。通过单击用户手册模块下对应版本的链接，能够浏览相应

Kyligence	Enterprise	版本最新的用户手册。

发布声明

在支持中心主页的中下侧，可以看到发布声明版块，点击模块内的链接，可以看到	Kyligence	旗下产品最新的发布
声明

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

265

模型设计指南

模型设计指南

本章将介绍如何对接数据源，进行模型设计以及性能调优。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

266

数据源

加载数据源

Kyligence	Enterprise	支持多数据源融合（如	Hive、Kafka、GBase	等），即把不同的数据源接入	Kyligence，并通过
Kyligence	对外暴露统一查询接口，屏蔽不同数据源的技术细节，提供统一的数据口径和业务语义层。

您可以单击下述链接了解如何加载不同的数据源：

Hive	数据源
Kafka	数据源
其他数据源

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

267

Hive	数据源

Hive	数据源

在数字化转型背景下，企业往往需要挖掘出最有价值的数据以便进一步支撑决策和业务发展，而传统数仓解决方案在面

对海量数据时往往只能提供分钟级甚至小时级的查询响应。

面对海量数据下的分析场景，您可以组合	Apache	Hive	和	Kyligence	Enterprise	实现	PB	级数据规模下的亚秒级查询响
应。

其中，Apache	Hive	是可实现大规模分析的分布式容错数据仓库软件，可以将结构化的数据映射为数据表，配合
Kyligence	Enterprise	提供的多维立方体预计算技术，大幅提升查询速度，助力业务分析师和数据科学家快速发现数据内
在价值，驱动商业决策。

本文介绍如何为项目加载	Hive	数据源，以便进行模型设计和数据分析。

注意事项

暂不支持	Hive	数据源中类型为	Map、Array、Struct	和	Binary	的列，这些列在加载源表时会被跳过。
支持在可计算列表达式中使用	Hive	UDF（用户自定义函数），或者在加载数据源时加载包含	Hive	UDF	的视图，但
暂不支持加载	Hive	3	版本包含	UDF	的视图，其他版本的视图在加载时如遇问题可联系	Kyligence	获取解决方案。

操作步骤

1.	 登录	Kyligence	Enterprise，登录的账号需为：

系统管理员账号。

拥有目标项目的管理员或项目管理员角色的账号。

2.	 在页面顶部，选择目标项目。

如果尚未具备项目，见创建项目。

3.	 在左侧导航栏，选择数据资产	>	数据源。

4.	 单击添加数据源，在弹出的对话框中选择	Hive	并单击下一步。

选择	Hive	数据源

5.	 在文本框中输入关键字并按回车键，找到并单击目标数据库或数据表，然后单击加载。

本文以	Kyligence	Enterprise	提供的样例数据集为例进行演示。

268

Hive	数据源

加载数据表

[!NOTE]

默认开启了表级数据抽样，系统将对表中列的基数和样例格式等进行抽样统计，便于您在设计模型时参

考列值分布信息。

一次最多可加载	1000	张表。如果按照数据库加载表，则所提交的数据库下的表总和应小于等于	1000；
若单次提交多个数据库，且库下的表较多，您可以分次加载避免超过限制；若单个数据库下的表超过

1000	张，则无法按库加载，您需要输入表进行加载。

按库加载时，当库下的表已加载，则不会重复加载，提交后将跳过已加载的表

常见问题

问：已经在	Hive	中准备数据库或数据表，但在加载时找不到？

答：Kyligence	Enterprise	会定时获取源表的元数据，如果在加载时找不到该表，可能是由于源表的元数据发生了变
更，此时可单击立即刷新，等待系统获取最新的元数据。

问：如何加载	Hive	事务表？

答：在加载前，您需要在配置文件中设置	 	kylin.build.resource.read-transactional-table-enabled=true	。同时需要
配置	 	kylin.source.hive.beeline-params		参数自定义	Hive	beeline	连接，更多信息，见配置基本参数。	使用注意事
项：

支持事务表的为	Hadoop	平台为	Cloudera	Data	Platform(CDP)	和星环	TDH。其中	CDP	支持事务表的文件格式为
orc，TDH	支持事务表的文件格式为	orc、text、sequence、parquet。
对于事务表、范围分区表、或范围分区事务表，暂不支持下压查询；暂不支持在模型保存界面自动获取时间分

区列的时间格式，需要手动选择时间格式；也不支持对这些表的快照进行增量刷新，请设置为全量刷新。

Kyligence	Enterprise	会在事务表所在的数据库创建外表，因此需要有相关数据库的写权限，若外表创建失败，
会导致构建失败。

269

Hive	数据源

问：除	Hive	数据源以外，Kyligence	Enterprise	还支持哪些数据源？

答：Kyligence	Enterprise	支持丰富的数据源，包括	Hive、Kafka，此外还可通过	SDK	扩展其他数据源（如
GBase）。如需支持更多的数据源，请联系	Kyligence。

问：Kyligence	Enterprise	支持的数据库名、表名、列名规则是什么？

答：

数据库名：支持字母、数字和下划线（_）组成。不支持纯数字、纯下划线、下划线开头。
表名：同数据库名。

列名：

支持字母、数字和下划线（_）组成。不支持纯数字。
如果需要支持中文，需要	Hive	设置	UTF-8	编码（Hive	默认为	latin	编码）。

查询：特殊字符字段需要用双引号	"	包裹。

后续步骤

设计模型

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

270

Kafka	数据源

Kafka	数据源

随着企业对用户体验、服务质量及决策时效性的要求不断提高，实时分析已广泛应用与各类场景，如个性化的精准营

销、实时的指标分析等。

Kyligence	Enterprise	通过结合开源分布式事件流平台	Apache	Kafka，实现数据实时分析能力（即实时功能），可将数据
分析的时效性从	T+1	降低至	T+0，在分钟级数据延时的情况下依然可以保持亚秒级查询响应。

企业可通过	Kyligence	Enterprise	实现了数据平台的统一，同时满足离线和实时两种数据的处理和分析需求，降低了企业
数据平台的建设与成本。

关于如何使用	Kyligence	实时功能，请参见：

软硬件环境要求：介绍使用实时功能需要具备的软硬件环境要求。

使用实时功能：介绍如何加载	Kafka	数据源以及如何在模型、索引中使用该功能。
已知限制：介绍某些高级功能和	Kafka	数据的一些使用限制。

[!NOTE]

需具备	Kyligence	Enterprise	高级版证书才能使用本功能，详细信息请联系	Kyligence	客户经理。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

271

其他数据源

其他数据源

Kyligence	Enterprise	采用了可插拔设计，您可以通过连接器轻松扩展更多的数据源，目前	Kyligence	Enterprise	支持的数
据源为：

GBase

MySQL

Impala

ClickHouse

Oracle	11g

Greenplum

TiDB

Doris

GaussDB	DWS

CirroData

Google	BigQuery

根据您的部署环境，部分数据源连接器可能需要定制化开发，您可以联系	Kyligence	客户经理获取相关解决方案。不同
数据源的加载方法类似，可参考扩展数据源。

此外，Kyligence	还开放了数据源扩展	SDK，方便您对接其他数据源，满足个性化需求。具体操作，见开发数据源连接
器。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

272

集成数据湖

集成数据湖

Kyligence	Enterprise	支持集成数据湖：

从	4.6.9.0	版本开始，支持集成	Delta	Lake
从	4.6.16.0	版本开始，支持集成	Iceberg
从	4.6.22.0	版本开始，支持集成	Hudi

根据您的部署环境，使用前可能需要定制化开发，您可以联系	Kyligence	客户经理获取相关解决方案。

集成	Delta	Lake

您可以创建	Hive	表映射至	Delta	Lake	文件，然后在	Kyligence	Enterprise	加载	Hive	数据源中对应的表，即可连接	Delta
Lake，使用建模、构建、查询等功能。

前置条件

建议使用	Delta	Lake	2.1.0	版本

用	Spark-sql	创建	Hive	外表映射至	Delta	Lake	文件，可参考下例：

bin/spark-shell	\

						--conf	spark.master=local	\

						--conf	spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension	\

						--conf	spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog

spark.sql("create	table	kylin_sales_delta	using	delta	location	\"abfss://data@test.dfs.core.chinacloudapi.c

n/sampledata/kylin_sales_delta\";")

使用方式

在	Kyligence	Enterprise	中加载	Hive	数据源中	Delta	Lake	对应的表，即可无感集成	Delta	Lake	数据湖，使用方式与普通的
Hive	表一致，可使用	Delta	Lake	表建模，进行模型查询、下压查询、Delta	Lake	与	Hive	联合下压查询。

注意事项

当	Delta	Lake	表结构发生变更后，需要在	Kyligence	Enterprise	中重载表。

基于	Delta	Lake	表最新版本的数据进行构建查询，未使用到	Time	Travel(时间旅行）的特性。

如果需要使用分层存储，请在开启分层存储后修改配置，重启	Kyligence	Enterprise	后生效：

kylin.storage.columnar.spark-conf.spark.sql.extensions=io.kyligence.kap.query.SQLPushDownExtensions,io.delt

a.sql.DeltaSparkSessionExtension

kylin.engine.spark-conf.spark.sql.extensions=io.kyligence.kap.query.SQLPushDownExtensions,io.delta.sql.Delt

aSparkSessionExtension

集成	Iceberg

您可以创建	Hive	视图表映射至	Iceberg	中的表，然后在	Kyligence	Enterprise	加载	Hive	数据源中对应的表，即可连接
Iceberg，使用建模、构建、查询等功能。

前置条件

273

集成数据湖

建议使用	Iceberg	0.12～0.14	版本

配置	Spark	参数连接	Iceberg，并用	Spark-sql	创建	Hive	视图表映射至	Iceberg	表，请将所有视图表放置在单独的库
下，可参考下例

bin/spark-shell	\

				--conf	spark.master=local	\

				--conf	spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions	\

				--conf	spark.sql.catalog.kylin=org.apache.iceberg.spark.SparkCatalog	\

				--conf	spark.sql.catalog.kylin.type=hadoop	\

				--conf	spark.sql.catalog.kylin.warehouse=hdfs://namenode:8020/iceberg

spark.sql("CREATE	OR	REPLACE	VIEW	SSB_ICE.iceberg_date_view	AS	select	*	from	kylin.SSB_ICE.DATES_ICE")

将	Iceberg	SDK	Jar	包放置在	 	$KYLIN_HOME/spark/jars		目录下，您可联系	Kyligence	客户经理获取	Jar	包

根据实际的存储，可能需要连接存储的	Jar	包，您可以联系	Kyligence	客户经理确认

参数配置

在	 	kylin.properties		添加	Iceberg	相关配置

#	配置查询相关的	Spark	配置
#	开启查询的	iceberg	扩展

kylin.storage.columnar.spark-conf.spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension,org.apache.icebe

rg.spark.extensions.IcebergSparkSessionExtensions

kylin.storage.columnar.spark-conf.spark.sql.catalog.kylin=org.apache.iceberg.spark.SparkCatalog
#	底层的	iceberg	目录实现

kylin.storage.columnar.spark-conf.spark.sql.catalog.kylin.type=hadoop
#	iceberg	仓库目录的基本路径

kylin.storage.columnar.spark-conf.spark.sql.catalog.kylin.warehouse=hdfs://namenode:8020/iceberg

#	配置构建相关的	Spark	配置
#	开启构建的	iceberg	扩展

kylin.engine.spark-conf.spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension,org.apache.iceberg.spark.e

xtensions.IcebergSparkSessionExtensions

kylin.engine.spark-conf.spark.sql.catalog.kylin=org.apache.iceberg.spark.SparkCatalog
#	底层的	iceberg	目录实现

kylin.engine.spark-conf.spark.sql.catalog.kylin.type=hadoop
#	iceberg	仓库目录的基本路径

kylin.engine.spark-conf.spark.sql.catalog.kylin.warehouse=hdfs://namenode:8020/iceberg

使用方式

在	Kyligence	Enterprise	中加载	Hive	数据源中	Iceberg	对应的表，即可无感集成	Iceberg	数据湖，使用方式与普通的	Hive
表一致，可使用	Iceberg	表建模，进行模型查询、下压查询、Iceberg	表与	Hive	联合下压查询。

注意事项

当	Iceberg	表结构发生变更后，需要重新创建	Hive	视图表，然后再在	Kyligence	Enterprise	中重载表。

基于	Iceberg	表最新版本的数据进行构建查询，未使用到	Time	Travel(时间旅行）的特性。

如果需要使用分层存储，请在开启分层存储后修改配置，重启	Kyligence	Enterprise	后生效：

kylin.storage.columnar.spark-conf.spark.sql.extensions=io.kyligence.kap.query.SQLPushDownExtensions,io.delt

a.sql.DeltaSparkSessionExtension,org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions

kylin.engine.spark-conf.spark.sql.extensions=io.kyligence.kap.query.SQLPushDownExtensions,io.delta.sql.Delt

aSparkSessionExtension,org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions

274

集成数据湖

集成	Apache	Hudi

您可以创建	Hudi	表同步至	Hive	，然后在	Kyligence	Enterprise	加载	Hive	数据源中对应的表，即可连接	Hudi，使用建
模、构建、查询等功能。

前置条件

建议使用	Apache	Hudi	0.13.1	版本

用	Spark-sql	创建	Hudi	表并同步到	hive，可参考下例：

bin/spark-shell	\

						--conf	spark.master=local	\

						--conf	spark.sql.extensions=org.apache.spark.sql.hudi.HoodieSparkSessionExtension	\

						--conf	spark.sql.catalog.spark_catalog=org.apache.spark.sql.hudi.catalog.HoodieCatalog	\

						--conf	spark.serializer=org.apache.spark.serializer.KryoSerializer

spark.sql("create	table	hudi_test.hudi_cow_pt_tbl6	(id	bigint,name	string,dt	date)	using	hudi	tblproperties

	(type	=	'cow',primaryKey	=	'id')	partitioned	by	(dt)	location	'hdfs://cdp716-master01.kylin.com:8020/user/

hive/warehouse/hudi_test.db/hudi_cow_pt_tbl6'")

将	Hudi	SDK	Jar	包放置在	$KYLIN_HOME/spark/jars	目录下，您可联系	Kyligence	客户经理获取	Jar	包

在	 	kylin.properties		配置文件中添加以下配置项，否则当	Hudi	表结构发生变更后，Kyligence	Enterprise	无法获取
更新

kylin.storage.columnar.spark-conf.spark.sql.metadataCacheTTLSeconds=1

使用方式

在	Kyligence	Enterprise	中加载	Hive	数据源中	Hudi	对应的表，即可无感集成	Hudi	数据湖，使用方式与普通的	Hive	表一
致，可使用	Hudi	表建模，进行模型查询、下压查询、Hudi	与	Hive	联合下压查询。

注意事项

当	Hudi	表结构发生变更后，需要在	Kyligence	Enterprise	中重载表。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

275

数据抽样

执行数据抽样

Kyligence	提供了数据抽样功能方便您对表中的数据进行分析，通过数据抽样，您可通过列的基数、最大值、最小值等
信息掌握表的数据特征，方便您更好地设计模型。

已知限制

暂不支持对	Kafka	数据源执行数据抽样。

操作步骤

Kyligence	Enterprise	支持在加载数据源是同时完成执行数据抽样，您也可以通过下述步骤执行数据抽样。

1.	 登录	Kyligence	Enterprise，登录的账号需为：

系统管理员账号。

拥有目标项目的管理员或项目管理员角色的账号。

2.	 在页面顶部，选择目标项目。

如果尚未具备项目，见创建项目。

3.	 在左侧导航栏，选择数据资产	>	数据源。

4.	 在数据源区域框中选择目标表，然后单击右上角的

	图标。

单击抽样图标

5.	 在弹出的对话框中，填写数据抽样的行数（范围为：10,000	~	20,000,000），单击提交。

抽样的行数越多，抽样结果越准确，但也会消耗更多的资源和时间，您可以根据实际需求设定抽样行数。如需查看

任务执行的进度，您可以选择左侧导航栏的监控	>	批数据任务。

6.	 （可选）查看抽样结果。

单击所有列页签，查看抽样统计信息，如抽样的行数（估算值），每列的基数、最小值、最大值等。

276

数据抽样

查看抽样统计信息

单击抽样数据页签，可查看该表的前十条数据明细信息。

查看数据明细

常见问题

问：抽样结果中，列的中文注释显示为乱码。

277

数据抽样

答：通常为编码设置问题，可通过	Hive	客户端确认源	Hive	表的中文注释是否有乱码。如果有乱码，则需要调整
MySQL	元数据库的编码。以	CDH	平台为例，修改编码的步骤如下：

1.	 登录	CDH	平台所属的服务器。
2.	 执行	 	mysql	-uroot	-p		命令，输入密码即可登录	MySQL	数据库。
3.	 执行	 	use	metastore;		命令进入	metastore	数据库。
4.	 将下述列的编码修改为	utf8，相关命令可参考	ALTER	TABLE	Statement。

COLUMNS_V2	表中的	COMMENT	列
TABLE_PARAMS	表中的	PARAM_VALUE	列
PARTITION_KEYS	表中的	PKEY_COMMENT	列

相关文档

设计模型

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

278

模型设计

设计模型

本章将介绍	Kyligence	Enterprise	使用的核心环节：模型设计和索引设计，高级度量设计，以及数据加载等。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

279

模型设计概述

模型设计概述

Kyligence	中的模型（Model）由多个数据表及其关联关系（Join	Relationship）构成。Kyligence	采用多维建模理论，为
数据表建立星型或雪花模型，同时结合	Kyligence	的预计算技术，在查询时直接读取计算结果，无需遍历所有数据，可
实现	PB	级数据规模下的亚秒级查询响应。

海量数据下的分析挑战

面对海量数据的查询分析场景，虽然可以通过某些技术手段提升计算和存储速度，但是无法改变查询的时间复杂度，即

查询时间与数据量依旧呈线性增长的趋势。

假设查询	1	亿条数据记录需要耗时	1	分钟，那么查询	100	亿	条数据记录则约需要	1	小时	40	分钟，如果企业需要对往年
积累的业务数据进行整体分析或增加查询复杂度（例如增加分析维度），查询会变得异常缓慢甚至出现查询超时。

通过	Kyligence	预计算加速查询

Kyligence	通过预计算技术可避免数据量增长带来的计算压力，即对模型中定义的维度组合提前完成数据的聚合计算，
然后将运算结果保存为索引用以加速查询。此外，Kyligence	还融合了并行计算和列式存储技术，大幅提升了计算和存
储速度。

采用预计算技术后，索引的规模仅由维度的基数决定，不会再随数据量的增长而线性增长。以在线交易的数据分析为

例，采用	Kyligence	预计算技术后，在维度不变的情况下，即使交易数据量增长	10	倍，查询的速度也几乎不会变化，可
保持计算时间的复杂度为	O(1)，帮助企业高效分析数据。

280

模型设计概述

如何设计模型与索引

智能建模（推荐）

Kyligence	Enterprise	内置	AI	增强引擎，可基于您上传的	SQL	查询语句自动建立模型，同时，支持根据企业的数据特征
和查询习惯，利用机器学习算法预测业务分析场景，提供模型与索引设计建议，您仅需简单地接受优化建议即可快速优

化模型，降低了建模的难度，帮助您快速上手。	具体操作，见智能建模。

手动建模

281

模型设计概述

除智能建模外，您还可以根据业务需求自行设计模型与索引。Kyligence	为您提供了详细的教程帮助您一步步完成模型
中维度、度量、关联关系、索引等基础设置，具体操作，见手动建模。

模型设计进阶

Kyligence	Enterprise	还围绕模型和索引提供了更多高级能力，帮助您高效地挖掘企业数据价值：

加速模型设计：内置精确去重、Top	N	等常用高级度量，方便您直接引用。
优化索引效率：通过索引剪枝技术筛选出有意义的维度，提升索引构建效率。

提升查询性能：通过智能分层存储实现在未进行预计算的情况下快速冷启动进行查询，提升超多维度下的灵活分析

和明细查询的性能。

更多介绍，见模型设计进阶。

了解基础概念

Kyligence	Enterprise	基于多维数据建模理论，将复杂的概念抽象为具体的功能模块，从而降低了数据建模难度。下述基
础概念帮助您更好地管理模型与索引：

维度（Dimension）：观察数据的角度，可用来描述对象的属性或特征，例如商品类型。
度量（Measure）：被聚合的统计值，一般是连续值，例如商品的销售额。
模型（Model）：由多个数据表及其关联关系（Join	Relationship）构成，并定义了维度和度量信息。
预计算（Pre-computation）：将数据按照模型中维度组合进行聚合计算，并将结果保存为索引，用以加速数据查
询。

索引（Index）：用于加速数据查询，包含：

聚合索引（Aggregate	Index）：本质是由多个维度和度量的组合并聚合计算而成，适合回答聚合查询，比如某
年的销售总额。

明细索引（Table	Index）：本质是大宽表的多路索引，适合回答精确到记录的明细查询，比如某用户的最近
100	笔交易。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

282

智能建模（推荐）

智能建模（推荐）

传统方式下，模型的开发与设计极大程度上依赖模型开发人员的经验，具有较高的使用门槛。Kyligence	强大的	AI	增强
引擎可以帮助用户自动创建模型和索引，同时还会持续根据查询历史提供模型优化建议，极大降低了大数据分析的门

槛。

AI	增强引擎的核心能力如下：

智能创建模型：Kyligence	AI	增强引擎通过分析	SQL	查询语句，自动解析其中的维度、度量等关键信息并引导您完
成模型的创建。您无需模型设计经验即可获得符合特定查询语句的模型，将更多的精力聚焦在业务本身。

智能优化索引：索引可用于加速数据查询，Kyligence	AI	增强引擎通过分析业务用户的查询习惯和源数据特征持续
优化索引。您仅需一键接受建议即可精准高效优化索引，结合预计算技术为索引加载数据，可快速降低查询响应时

间。

相关文档

智能推荐工作原理

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

283

智能建模（推荐）

智能推荐工作原理

Kyligence	智能推荐功能以	AI	增强引擎为核心，可覆盖模型设计的完整链路，包含创建模型、生成索引以及通过持续提
供优化建议，实现模型结构和索引随业务而变化，从而精准契合业务需求。本文将介绍智能推荐的相关工作原理。

基于	SQL	智能建模

在您提供	SQL	查询语句后，Kyligence	将自动解析其中的维度、度量等关键信息，引导您完成模型的创建。此外，如果
Kyligence	检测到现有模型可以匹配某些	SQL	查询，还会引导您将其转换为优化建议，帮助您控制模型数量。

您可以通过如下方式提供	SQL	查询语句：

网页：将	SQL	查询语句以	TXT	或	SQL	文件的形式上传。
API	接口：将	SQL	查询语句以传入参数值的形式发起调用。

基于查询历史优化索引

Kyligence	AI	增强引擎通过分析业务用户的查询习惯和源数据特征持续优化索引，同时结合评分机制和生成规则，将分
析结果以优化建议的方式推送给您。

评分机制

Kyligence	通过内置的评分机制衡量索引的潜在价值，初步筛选高价值的索引并临时记录在内部，后续将通过生成规则
对其进行过滤，支持的评分机制如下：

评分机制

生效条件

公式

基于最近时间范
围的查询次数
（默认）

4.5.7	版本开始支持

Revenue =

∑timeW indow

queryCount

说明

●	Revenue	为
接受建议可能
带来的收益评
分。
●	queryCount
为优化建议对
应的查询次
数。

284

智能建模（推荐）

基于查询历史的
平均加权耗时公
式

需将	kylin.properties	文件中
	kylin.smart.update-cost-
method		参数的值修改为
	TIME_DECAY	。

Revenue = Σt × e

k

−k

●	Revenue	为

接受建议可能
带来的收益评
分。
●	tk	为第	k	天
命中该模式的
查询平均耗
时。

生成规则

在将评分筛选后的索引作为优化建议之前，Kyligence	还会基于下述规则进一步筛选：

规则

说明

系统规则

自动过滤精确命中索引或无法匹配已有模型的查询，提升索引有效率。

自定义规
则

您还可以通过查询耗时、命中规则、优化建议数量等规则进行过滤，具体操作，见设置优化建议的
生成规则。

优化建议类型

Kyligence	生成的优化建议主要为新增或删除索引，以及相关维度、度量、可计算列的调整，您可以在	模型列表页查看
系统推送的优化建议，评估是否接受。

类型

说明

新增索引

通过新增精准匹配查询的索引，帮助您显著降低相关查询的响应时间。

删除索引

通过删除冗余或低频等索引，帮助您节约存储空间，降低模型膨胀率。
更多介绍，见索引优化策略。

常见问题

问：在系统资源紧张的情况下，可以通过什么参数来调整智能推荐占用的资源？

答：您可以通过调低系统配置文件中下述参数的值，降低智能推荐占用的资源。

		#	该参数用于控制每一次定时任务最多处理的查询语句数量

		kylin.favorite.query-history-accelerate-max-size=100000

		#	该参数用于控制每一个批次最多处理的查询语句数量

		kylin.query.query-history-stat-batch-size=1000

问：智能推荐功能在不同版本下什么不同吗？

答：Kyligence	Enterprise	4	版本开始支持智能推荐功能，各版本中该功能的说明如下：

版本

说明

4.0

4.1

4.2

支持一键加速获得想要的模型，但是无法手动干预（在	4.1	及以上版本已停用）。

支持结合查询习惯和数据源特征生成优化建议，以便持续优化模型和索引。

深度优化功能，降低优化建议和响应时间等。
注意：从	4.1	升级至	4.2	后，优化建议无法向后兼容，系统会基于查询历史重新生成，即在	4.1	版本生成
的优化建议需手动删除或忽略。

4.2.2

支持从	Kyligence	Enterprise	首页执行模型优化，如果和定期执行的优化建议生成任务冲突，系统将自动
中断后台任务，优先执行从首页发起的模型优化任务。

4.5.6

停用	 	kylin.metadata.top-recs-filter-cron		参数。默认按天进行统计，避免因频繁刷新增加系统负载。

285

智能建模（推荐）

4.5.6

停用	 	kylin.metadata.top-recs-filter-cron		参数。默认按天进行统计，避免因频繁刷新增加系统负载。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

286

智能建模（推荐）

基于	SQL	创建模型和索引

在	Kyligence	中，模型由多个数据表及其关联关系（Join	Relationship）构成，并定义了维度和度量信息。上传	SQL	查询
语句后，Kyligence	会自动解析其中的维度、度量等关键信息并引导您完成模型的创建。您无需模型设计经验即可获得
符合特定查询语句的模型，显著缩短模型开发周期。

准备工作

加载数据源，本文以	SSB	样例数据集演示操作流程。
将准备好的	SQL	查询语句保存至	TXT	或	SQL	格式的文件中，本文使用的	SQL	查询语句如下：

SELECT

CUSTOMER.C_NATION,	CUSTOMER.C_CITY,	CUSTOMER.C_REGION,	DATES.D_YEAR,	DATES.D_DATE,	PART.P_BRAND

,sum(P_LINEORDER.LO_SUPPLYCOST),	sum(P_LINEORDER.LO_REVENUE),count(1)

FROM

"SSB"."P_LINEORDER"	as	"P_LINEORDER"

LEFT	JOIN	"SSB"."CUSTOMER"	as	"CUSTOMER"	ON	"P_LINEORDER"."LO_CUSTKEY"="CUSTOMER"."C_CUSTKEY"

LEFT	JOIN	"SSB"."DATES"	as	"DATES"	ON	"P_LINEORDER"."LO_ORDERDATE"="DATES"."D_DATEKEY"

LEFT	JOIN	"SSB"."PART"	as	"PART"	ON	"P_LINEORDER"."LO_PARTKEY"="PART"."P_PARTKEY"

LEFT	JOIN	"SSB"."SUPPLIER"	as	"SUPPLIER"	ON	"P_LINEORDER"."LO_SUPPKEY"="SUPPLIER"."S_SUPPKEY"

group	by	CUSTOMER.C_NATION,	CUSTOMER.C_CITY,	CUSTOMER.C_REGION,	DATES.D_YEAR,	DATES.D_DATE,	PART.P_BRAND;

[!NOTE]

文件大小不可超过	5	MB，多个	SQL	查询语句之间使用英文分号（;）分隔。

操作步骤

1.	 登录	Kyligence	Enterprise，登录的账号需为：

系统管理员账号。

拥有目标项目的项目管理员角色的账号。

2.	 为项目开启智能推荐功能，如果尚未具备项目，见创建项目。

i.	 在首页单击开启智能推荐。

ii.	 在弹出的对话框中单击确认开启。

3.	 在左侧导航栏，选择数据资产	>	模型。

4.	 选择	+	模型	>	SQL	建模。

287

智能建模（推荐）

SQL	建模

5.	 在弹出的对话框中单击上传，选择并上传包含	SQL	查询语句的文件，然后单击下一步。

6.	 在确认导入的	SQL	对话框中，查看解析出的	SQL	查询语句，确认无误后单击下一步。

[!NOTE]

Kyligence	会将相似的	SQL	查询语句进行合并，您可以选择待导入的	SQL	查询语句，也可以对其进行修
改和删除

如果	Kyligence	检测到现有模型可以匹配某些	SQL	查询，还会引导您将其转换为优化建议，帮助您控制
模型数量。

7.	 在预览对话框中，检查新模型的维度、度量、可计算列等信息，您也可以修改下述配置。

288

智能建模（推荐）

预览模型信息

模型名称：由系统自动生成，格式为	 	AUTO_MODEL_事实表名称_编号	，您也可以手动调整，仅支持数字、英文字母
和下划线（ 	_	）。模型名称最长	127	字符，当事实表名称过长时，系统会从尾部自动截断事实表名称，保证
自动生成的模型名称小于等于	127	字符，被截断时，模型名称格式为	 	AUTO_MODEL_尾部截断的事实表名称_TRUNC_编
号	。

添加基础索引：基础索引包含基础聚合索引和基础明细索引，其中基础聚合索引包含模型内全部维度和度量，

基础明细索引包含模型内全部维度和度量中使用的列。	推荐保持选中，避免频繁的下压查询而增加查询响应时
间，基础索引默认随模型变化而自动更新。

8.	 单击确定，系统将自动为您创建模型和索引。

后续操作

刚刚创建完成的索引尚未完成数据加载，您需要对其执行构建数据操作（即预计算）。	完成构建后，该索引即可用于加
速查询。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

289

智能建模（推荐）

常量子查询推荐优化

在很多业务的数据分析场景中，常量子查询是比较常见的	SQL	用法。在	4.6.15.0	之前版本中，SQL	关联关系中包含常
量子查询时，无法通过智能推荐生成预期的索引，可能导致索引构建后查询性能仍未达预期。

从	Kyligence	Enterprise	4.6.15	版本开始，您可以通过以下配置，启动对	SQL	关联关系中包含常量子查询场景的推荐优
化，该参数支持系统级或项目级配置：

##	参数默认值为	false，表示未启用该功能

kylin.query.scalar-subquery-join-enabled	=	true

查询示例

下面以	Kyligence	Enterprise	的样例数据集为例，有关样例数据集的更多信息请参考样例数据集。

SELECT	D_DATEKEY,	DATE_TIME,	count(*),	sum(D_YEAR)	sy

FROM	(SELECT	'1995-03-01'	AS	DATE_TIME

						UNION	ALL

						SELECT	'1995-03-02'	AS	DATE_TIME

						UNION	ALL

						SELECT	'1995-03-03'	AS	DATE_TIME)	t1

									LEFT	JOIN	SSB.DATES	t2	ON	t2.D_DATEKEY	<=	t1.DATE_TIME

									AND	t2.D_DATEKEY	>=	CONCAT(SUBSTR(t1.DATE_TIME,	1,	8),	'01')

GROUP	BY	D_DATEKEY,	DATE_TIME

产品默认行为无法通过智能推荐生成包含度量	 	SUM(D_YEAR)		的索引；开启该配置参数后，则可以生成包含维度为
	D_DATEKEY	、度量为	 	SUM(D_YEAR)		， 	count(*)		的索引，成功推荐出符合预期的索引优化建议。

已知限制

1.	 暂不支持聚合函数为	 	count	distinct		时的索引推荐和	SQL	建模，如上述例子中当	 	sum(D_YEAR)		变为

	count(distinct	D_YEAR)		时则无法推荐；

2.	 暂不支持聚合函数的参数是表达式时的索引推荐和	SQL	建模，如上述例子中当	 	sum(D_YEAR)		变为	 	sum(D_YEAR+1)

时则无法推荐。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

290

智能建模（推荐）

智能优化索引

Kyligence	通过索引加速数据查询，其内置的	AI	增强引擎可通过分析业务用户的查询习惯和源数据特征持续提供索引优
化建议，保证索引可以及时适应业务变化，精准契合业务需求。

更多信息，请阅读下述文档。

索引优化策略

查看智能优化推荐

设置优化建议的生成规则

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

291

智能建模（推荐）

索引优化策略

索引优化是	Kyligence	AI	增强引擎的核心能力之一，除会通过推荐高价值索引帮助降低查询响应外，还会通过索引优化
策略发现低价值索引并生成类型为删除的优化建议。当您接受了该建议后，Kyligence	将自动删除相关索引，帮助您降
低索引构建压力和存储开销。本文介绍索引优化的策略。

被包含策略（推荐）

当	Kyligence	AI	增强引擎检测到索引存在包含关系，则生成删除索引的优化建议，采纳该建议不会影响查询效率。

对于明细索引，该包含关系需同时满足下述条件：

维度存在包含关系，且排序相同，例如有维度	A、B、C，那么明细索引	[A,	B,	C]	可以包含明细索引	[A,	C]	和
[B,	C]，但是不能包含	[C,	A]	或	[C,	B]。
ShardBy	列相同。

对于聚合索引，该包含关系需同时满足下述条件：

维度完全一致且度量集合存在包含关系，例如有维度	A、B、C，度量	M1、M2、M3，那么聚合索引	[A,	B,	C,
M1,	M2,	M3]	可以包含聚合索引	[A,	B,	C,	M1]	和	[A,	B,	C,	M2,	M3]，但是不能包含	[A,	C,	M2]	或	[A,	C,	M1,
M3]。
ShardBy	列相同。

[!NOTE]

明细索引和聚合索引之间不存在包含关系。

相似策略

当	Kyligence	AI	增强引擎检测到聚合索引之间的相似度，则生成删除索引的优化建议，采纳改建议可能会对查询效率产
生一定影响。

相似索引需同时满足下述条件：

聚合组生成的聚合索引具有父子关系（即维度为包含关系），例如有维度	A、B、C，度量	M1、M2，那么聚合索
引	[A,	B,	C,	M1,	M2]	与	[A,	C,	M1,	M2]	存在父子关系。
父子索引的行数比例大于阈值，由子索引行数除以父索引行数得出，默认为	0.9。

如需调整该阈值，请修改配置文件中	 	kylin.index.similarity-ratio-threshold		参数的值。

父子索引的行数差值小于阈值，默认为	1	亿。

如需调整该阈值，请修改配置文件中	 	kylin.index.beyond-similarity-bias-threshold		参数的值。

父子索引的	ShardBy	列相同。

低频策略

Kyligence	AI	增强引擎会自动分析某个时间窗口内（如每天、每周等）索引的使用次数，当低于某个值时则生成删除索
引的优化建议，采纳改建议可能会对查询效率产生一定影响。

292

智能建模（推荐）

如需调整低频策略，您可以登录	Kyligence	Enterprise，在设置页面的索引优化区域框中修改。

应用索引优化策略

您可以修改配置文件中	 	kylin.index.optimization-level		参数的值，为自定义索引和	AI	增强推荐的索引应用索引优化
策略。

参数值

说明

对自定义索引和	AI	增强引擎推荐的索引均不做任何处理。

●	对自定义索引不做任何处理。
●	对	AI	增强引擎推荐的索引执行被包含策略。

●	对自定义索引不做任何处理。
●	对	AI	增强引擎推荐的索引执行被包含策略和低频策略。

●	对自定义索引执行相似策略。
●	对	AI	增强引擎推荐的索引执行被包含策略和低频策略。

0

1

2（默认）

3

常见问题

问：如果采用了	AI	增强引擎推荐的索引，然后又通过修改聚合组得到了相同的索引，Kyligence	会同时保存这两个
索引吗？

答：不会。为避免重复构建索引增加存储开销，Kyligence	仅保留由	AI	增强引擎推荐的索引并将其来源转换为自定
义索引。

问：如果根据优化建议删除了索引，还需要删除其他文件吗？

答：此操作删除的是索引元数据，该索引对应的构建数据仍存储在	HDFS	文件系统中，您可以通过自动或手动的方
式进行清理，具体操作，见垃圾清理。

问：什么是	ShardBy	列？

答：ShardBy	列可以使数据均匀的分散在多个数据片上，提高并行性和查询效率，通常会将基数较大的列作为
ShardBy	列。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

293

智能建模（推荐）

查看智能优化推荐

传统模式下，即使在模型开发完成后，开发人员仍需经常调整索引以响应业务需求。Kyligence	AI	增强引擎通过分析查
询历史和源数据特征自动生成优化建议，帮助用户便捷灵活地调整索引，及时跟进业务需求的变化。

操作步骤

1.	 登录	Kyligence	Enterprise，登录的账号需为：

系统管理员。

拥有目标项目的管理员、项目管理员角色。

2.	 在左侧导航栏，选择数据资产	>	模型。

3.	 查看模型是否存在优化建议，单击

	图标查看优化建议详情。

294

智能建模（推荐）

4.	 在优化建议标签页，查看优化建议的详细信息。

本案例中，优化建议为新增聚合索引，您可以单击内容列的
为删除，您可以在备注中查看具体原因以评估是否通过该建议。

	图标查看详细的维度、度量信息。如果建议类型

5.	 选中优化建议前的复选框，单击通过。

6.	 添加新的索引后，您还需要为其执行构建操作，由	Kyligence	基于索引进行预计算以加速数据查询。

i.	 单击索引总览页签。

ii.	 找到刚新建的索引，单击其操作列的

	图标。

如果索引较多，您也可以筛选状态为未构建的索引。

iii.	 在弹出的对话框中，选中时间范围前的复选框，单击构建索引。

如需查看任务执行进度，您可以左侧导航栏的监控	>	批数据任务。

常见问题

问：如何调整优化建议的生成规则？

答：您可以根据业务需求自定义生成规则，例如设置查询耗时、命中规则、优化建议的数量上限等，具体操作，建

议设置优化建议的生成规则。

问：索引优化的策略是？

答：Kyligence	支持低频策略、被包含策略、相似策略，通过这些策略帮助您降低构建压力和存储开销。详细介
绍，见索引优化策略。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

295

智能建模（推荐）

设置优化建议的生成规则

Kyligence	Enterprise	智能推荐功能可基于查询历史、数据特征、SQL	建模等生成索引或模型优化建议，从而降低模型设
计门槛，提升查询响应速度。本文介绍如何设置优化建议的生成规则。

前提条件

已开启智能推荐功能。

[!NOTE]

如未开启，可在	Kyligence	Enterprise	平台的首页，单击开启智能推荐。

背景信息

启用智能推荐后，系统生成的优化建议将会临时记录在内部，随即根据统计分析和推送规则进行推送。您可以在首页查

看系统推送的优化建议，并评估是否接受此建议。

更多信息，见基本概念及功能原理。

操作步骤

1.	 登录	Kyligence	Enterprise	平台，登录的账号需为：

系统管理员。

拥有目标项目的管理员、项目管理员角色。

2.	 在左侧导航栏，单击设置。

3.	 在基本设置页签，找到优化建议偏好设置区域框。

4.	 根据业务需求设置分别下述参数，然后单击保存。

296

智能建模（推荐）

优化建议偏好设置

用户规则：选择是否打开该开关，开启后可选择用户或用户组，系统将仅对这些用户或用户组执行的	SQL	查
询生成优化建议。

查询耗时：设置查询耗时的时间范围（默认为	5	~	3600	秒），系统将仅对耗时在该范围的	SQL	查询生成优化
建议。

命中规则：组合设置下述参数可筛选出命中次数高的索引，帮助您过滤出高价值的索引。

例如时间范围为	2	天，命中次数为	30，则表示最近	2	天，某条优化建议被命中	30	次，该条建议将会推送给
您。

时间范围：统计最近多少天内的索引命中数（默认为	2	天），从当天开始计算。

命中次数：设置索引命中的次数（默认为	30	次），后续可根据系统推送的优化建议数再次调整。

优化建议数量上限：组合设置下述参数可调整优化建议的推送数量和频率。

[!NOTE]

本参数仅对基于查询历史生成的优化建议生效。

优化建议：将优化建议按照命中次数从高到低排序，将排名靠前的建议推送给用户，默认为前	20	条。
推荐频率：设置所有优化建议的推送频率（默认为	2	天）。

5.	 在基本设置页签，找到屏蔽列设置区域框来指定屏蔽列。

选择是否打开该开关，开启后可通过关键字搜索指定的表后添加列，系统将不会对已屏蔽的列生成优化建议。

该设置对事实表无效，具体来说，如果屏蔽列在建模的时候被探测到属于事实表，那么屏蔽列起不到屏蔽作

用。

屏蔽列用于处理缓慢变化维，尤其是希望对部分列使用SCD	type	1	，另外一些列使用	SCD	type	2的场景。	如果

297

智能建模（推荐）

您开启智能推荐，屏蔽列将不被推荐到优化建议中，适用于	AS-IS	（SCD	type	1）分析场景。
设置生效后，事实表中的外键将代替被屏蔽的列被推荐到优化建议中，完成索引构建后可通过外键来衍生查询

表中的列。

如果索引中已经使用了屏蔽列，需要人工删除包含这些列的索引，以实现	AS-IS	（SCD	type	1）。
如果您希望对另一些列实现	AS-WAS	（SCD	type	2），则可以将这些列加入索引。

[!NOTE]

4.6.2版本起，原屏蔽表功能被屏蔽列代替，通过在项目级别设置参数kylin.metadata.table-exclusion-
enabled=true可见到屏蔽列相关设置。
您可以通过屏蔽表上的所有列以达到原来屏蔽表的效果。

原屏蔽表相关参数	 	kylin.engine.build-excluded-table=true	已无效

[屏蔽列进阶说明]

对于关联关系，在雪花模型中，	A	join	B(on	a1	=	b1)	and	B	join	C	(on	b2	=	c2)	时，b2	不能是屏蔽列，否
则关联关系断链导致无法推荐索引。

可计算列的设计表明了需要预计算，屏蔽列的设计表明了不要预计算，本身就互不相容，所以原则上不

推荐定义屏蔽列相关的可计算列。特别地，屏蔽列关联的可计算列和度量如果命中索引，可能导致数据

不对。

依赖屏蔽列的可计算列，不会在智能推荐时被复用。更进一步，开启配置	kylin.metadata.only-reuse-user-
defined-computed-column=true（默认false）	后，推荐时只会复用模型上用户自定义的可计算列，也就是
说不会创建新的	CC_AUTO	开头的可计算列，也不会复用这种以	CC_AUTO	开头的可计算列。
查询时，不开启屏蔽列设置，默认不带外键的索引回答查询的优先级高于使用带外键的索引实时关联

snapshot。但开启屏蔽列，并设置	kylin.query.snapshot-preferred-for-table-exclusion=true	后，会优先选择外
键索引+快照响应查询；此参数默认为	ture	。如果设置为false，则优先考虑索引回答。

常见问题

问：优化建议偏好设置的生效级别是什么？

答：生效级别为项目级。如需在模型级别屏蔽某个表（即不参与预计算和生成索引），请在建模时取消预计算关联

关系。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

298

手动建模

手动建模

Kyligence	采用多维建模理论，为数据表建立星型或雪花模型，同时结合	Kyligence	的预计算技术，在查询时直接读取计
算结果，无需遍历所有数据，可实现	PB	级数据规模下的亚秒级查询响应。

操作流程

Kyligence	中的模型由多个数据表及其关联关系（Join	Relationship）构成。本案例中，用到了基于现实商业应用的	SSB
数据集。我们希望能从年份、城市、供应商名称及品牌等维度分析产品和供应商信息，为实现这些多维度分析目标，我

们将通过	Kyligence	Enterprise	创建模型，并设置待分析的维度和度量，具体步骤如下：

步骤

步骤一：创建模型并
添加事实/维度表

步骤二：建立表的关
联关系

说明

创建新模型后，添加待分析的事实表和维度表，后续我们分析的数据即来源于这些表。

为事实表的外键和维度表的主键建立关联关系，实现事实表和维度表的关联查询。

步骤三：为模型添加
维度和度量

设置数据分析所需的维度和度量，后续可基于维度和度量的组合进行预计算以加速数据
查询。

步骤四：保存模型并
设置加载方式

保存模型的设置，并为后续的预计算指定数据加载方式。例如选择为增量加载时，后续
可根据时间范围加载部分数据，提升数据加载效率。

步骤一：创建模型并添加事实/维度表

1.	 登录	Kyligence	Enterprise，登录的账号需为：

系统管理员。

拥有目标项目的管理员或项目管理员角色。

2.	 创建模型。

i.	 在左侧导航栏，选择数据资产	>	模型。

ii.	 单击	+	模型。

iii.	 在弹出的对话框中，填写模型名称和描述，单击提交。

模型名称仅支持数字、大小写英文字母和下划线（_）。

3.	 在跳转到的模型编辑页面中，为模型添加事实表。

事实表用于存储事实记录，即保存了最细粒度的业务过程数据（例如商品销售记录表），通常作为模型中的主表。

i.	 在左侧的数据源区域框中，找到目标事实表（本案例为	P_LINEORDER）。

[!NOTE]

如果数据源区域框中没有任何表，请先加载数据源。

ii.	 将目标表拖动至页面中心区域，然后选择设置为事实表。

299

手动建模

设置事实表

4.	 为模型添加维度表。

维度表也称维表或查找表（Lookup	Table），用于存储事实表中经常重复出现的属性，例如日期、地理位置等，可
提升事实表中维度的管理效率，降低事实表的大小。

i.	 在左侧的数据源区域框中，找到目标维度表。

ii.	 将目标表拖动至页面中心区域。

如需添加多个维度表，您需要重复执行本步骤。如下图所示，本案例中共添加了	1	个事实表和	4	个维度表。

添加表

步骤二：建立表的关联关系

1.	 在模型编辑页面中，通过拖拽的方式为事实表的外键与维度表的主键建立关联。

300

手动建模

建立表关联

2.	 在弹出的对话框中，根据下述说明完成设置。

关联关系设置

表的关联关系：包含	3	个下拉框，其中第	1	个和第	3	个下拉框为待关联的表，第	2	个下拉框为表的关联类型，
当前支持	LEFT（左连接）	和	INNER（内连接）。
表关系：选择外键和主键之间的映射关系，当前支持一对一或多对一、一对多或多对多。

预计算关联关系：选择是否将关联的表依据映射关系展开成一张平表，默认为选中状态，关于该功能的详细介

绍及适用场景，见预计算关联关系。

列的关联关系：包含	3	个下拉框，其中第	1	个和第	3	个下拉框为待关联的列，第	2	个下拉框为列的关联类型，
默认为相等关系（=），关联关系需满足下述条件：

列的关联关系不可重复定义，且两张表仅可使用同样的条件连接一次

301

手动建模

至少包含一个关联关系（=）
关联关系	≥	和	<	必须成对出现，且位于中间的列必须一致，例如	B≥A，C＜A。

3.	 单击确定。

如需建立多个表的关联关系，请重复执行步骤	1	至	3。本案例中，我们为表建立了	4	条关联关系并形成了星型模
型。

星型模型

对应的	SQL	语句为：

P_LINEORDER	LEFT	JOIN	DATES	ON	P_LINEORDER.LO_ORDERDATE	=	DATES.D_DATEKEY

P_LINEORDER	LEFT	JOIN	CUSTOMER	ON	P_LINEORDER.LO_CUSTKEY	=	CUSTOMER.C_CUSTKEY

P_LINEORDER	LEFT	JOIN	SUPPLIER	ON	P_LINEORDER.LO_SUPPKEY	=	SUPPLIER.S_SUPPKEY

P_LINEORDER	LEFT	JOIN	PART	ON	P_LINEORDER.LO_PARTKEY	=	PART.P_PARTKEY

步骤三：为模型添加维度和度量

1.	 为模型添加维度。

i.	 在模型编辑页面中，从维度表中拖拽要分析的维度列到维度区域框中。

如需批量添加维度，您可以单击维度区域框	+	图标，然后在各个表中勾选需要添加的维度。您也可以通过在搜
索框直接搜索列名或选择使用文本识别功能批量添加维度。

302

手动建模

添加维度

ii.	 在弹出的对话框中，设置维度名称。

默认为列名，支持中文、大小写英文字母、数字、空格及特殊字符 	(_	-()%?)

iii.	 单击确定。

本案例中，我们依次添加了年份（DATE	表的	D_YEAR	列）、客户所属城市（CUSTOMER	表的	CITY	列）、
供应商名称（SUPPLIER	表的	S_NAME	列）和品牌（PART	表的	P_BRAND	列）维度。

2.	 为模型添加度量。

i.	 在模型编辑页面中，从事实表中拖拽要分析的维度列到度量区域框中。

添加度量

ii.	 在弹出的对话框中，根据下述说明完成设置。

名称：默认为列名，支持中文、大小写英文字母、数字、空格及特殊字符 	(_	-()%?)

函数：默认为	SUM(column)（即求和），Kyligence	内置丰富的基础和高级函数（如精确去重、计算	TopN
等），更多介绍，见高级度量。

303

手动建模

列：显示作为度量的列，无需调整。

注释（可选）：填写具有业务意义的注释信息。

iii.	 单击提交。

本案例中，我们添加了收入（P_LINEORDER	表的	LO_REVENUE	列）和供应成本（P_LINEORDER	表的
LO_SUPPLYCOST	列）度量，并分别计算其总值。

3.	 （可选）如需基于现有的列执行复杂的处理与计算，可为模型添加可计算列。更多介绍，见可计算列。

步骤四：保存模型并设置加载方式

1.	 在模型编辑页面的右下角，单击保存。

2.	 在弹出的对话框中，完成下述设置。

保存并设置加载方式

选择加载方式：

全量加载：对源表的所有数据，按照维度和度量的组合进行加载和预计算。

增量加载：可对源表指定时间范围内的数据，按照维度和度量的组合进行加载和预计算，选择为此选项

时，您还需要设置下述参数：

分区表：固定为事实表。

时间分区列：选择分区表中类型为时间的列。

时间格式：选择时间格式，如果忘记格式，您可以单击
式并自动填写。

	图标，Kyligence	将自动获取列的时间格

高级设置：通过数据筛选来过滤空值数据或符合特定条件的数据，多个过滤条件使用	 	AND		或	 	OR		连接，例如
	BUYER_ID	<>	0001	AND	COUNT_ITEM	>	1000	OR	TOTAL_PRICE	=	1000	。

添加基础索引：包含下述索引，默认情况下会随着模型内维度和度量的改变而自动更新。

基础聚合索引：包含模型内全部维度和度量。

304

手动建模

基础明细索引：包含模型内全部维度和度量中使用的列。

3.	 单击提交。

保存完成后，您可以单击提示对话框中的查看索引，可查看到	Kyligence	自动创建的基础聚合索引和基础明细索
引。

后续步骤

刚刚创建完成的基础索引尚未完成数据加载，您需要对其执行构建数据操作（即预计算）。完成构建后，该索引即可用

于加速查询。

[!NOTE]

由于基础索引可加速的查询场景较少，为提升查询效率，您需要为模型增加更多索引，具体操作，见聚合索引和

明细索引。

常见问题

问：设置时间分区列后，保存时报错？

答：时间分区列的时间格式与目标格式不匹配引起。Kyligence	支持的时间格式为： 	yyyyMMdd	、	 	yyyy-MM-
dd	、 	yyyy/MM/dd	、 	yyyy-MM-dd	HH:mm:ss	、 	yyyy-MM-dd	HH:mm:ss.SSS	、 	yyyy-MM	、 	yyyyMM	、 	yyyy-MM-

dd'T'HH:mm:ss.SSS'Z'	。此外，还支持自定义时间格式，需满足下述要求：

可使用	yyyy,	MM,	dd,	HH,	mm,	ss,	SSS	中的部分要素正序组合。
可使用短横线（-）、正斜线（/）、英文冒号（:）和空格作为分隔符。
使用无格式字母时，需用英文单引号（'）包裹，例如	'T'	将被识别为	T。

[!NOTE]

当自定义时间格式设置为	 	yyyyMMddHHmmss		时，对应	Hive	表中的列类型需为	String，否则可能造成数据识别
错误。

问：修改了同一模型中的多个表后，执行重载表时发生报错？

答：目前仅支持单表重载，请为每个表单独执行修改和重载操作，避免修改多个表后再执行重载操作。

问：模型上线规则是什么样的？

答：模型中的索引构建完成后会自动上线。然而在某些情况下，用户可能会在一段时间内持续构建历史数据用于创

建新的报表或者用于测试，在此期间希望模型不回答任何查询直到所有数据构建完成。因此，在这个场景下，我们

提供了一个模型级别的参数配置用于手动控制模型的上线开关	 	kylin.model.offline	，默认值为	 	false	，在模型重
写页面修改为	 	true		后，模型在构建任务完成后也不会自动上线。通过这个参数，用户就可以避免模型在补数期间
错误回答查询的情况。

305

手动建模

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

306

模型概念与操作

模型概念与操作

模型设计指基于数据表和多维建模理论，建立星型或雪花型模型。模型设计主要包含以下内容：

定义事实表与维度表

定义表与表的关联关系

定义维度和度量

模型列表

您可以手动创建并设计模型。以下介绍模型列表的内容：

1.	 登录本产品	Web	UI，切换进入具体项目。

2.	 点击进入导航栏	数据资产	->	模型	界面，主页面将以列表形式显示已有的模型。下图所示为	AI	增强模式中的模型

列表：

模型列表的字段介绍：

模型名称：包含模型名字、状态、最近更新时间。

状态：四种模型状态。

ONLINE	表示模型上线，可以服务于查询分析。
OFFLINE	表示模型下线，不能服务于查询分析。当您需要编辑已存在的模型时，我们建议您先使模
型下线。

BROKEN	表示模型损坏，不能服务于查询分析。一般发生在模型中的源表发生变化，如删除源表会导
致该状态。

WARNING	表示模型状态异常，仅可服务部分查询，但是查询数据可能存在不一致等问题。一般发生
在	Segment	存在空洞或者模型中存在空索引未构建。

最近更新时间：最近一次更新模型的时间。

操作：鼠标悬浮在模型名称区域，可看到对模型可进行的操作，您可以在本文模型操作中了解详细方法。

所有者：创建模型的用户。

描述：模型的描述。

优化建议：系统根据查询历史和模型使用情况，对当前模型提供的一些优化建议，包含对维度、度量、可计算

列、明细索引的新增和删除，还有对聚合索引的新增、删除和修改。

提示：优化建议只出现在开启了智能推荐模式的AI	增强模式中。开启方式请您参考项目设置。

事实表：模型中的事实表。

模型类型：模型的类型，分为离线模型、实时模型、融合模型。

使用量：过去	30	天内，SQL	查询击中模型的次数。间隔	30	分钟更新一次。

行数：模型下已构建数据的行数。

存储：模型下已构建数据的存储大小，是所有	Segment	中数据的存储大小总和。

307

模型概念与操作

提示：当开启分层存储时，会展示加载到分层存储中的数据的存储大小总和。

膨胀率:	模型下已构建数据的存储大小和对应的源表数据的存储大小的比值。膨胀率	≈	存储数据大小	/	源表大
小。

提示：当存储数据小于1GB时，膨胀率不做显示。

索引数量：模型下索引数量。

模型操作

鼠标悬浮在模型名称区域，可看到对模型可进行的操作，以下介绍详细信息：

编辑：点击铅笔形状的图标，进入模型编辑页面。

构建索引：为模型加载数据，您可以在弹窗中选择加载的数据范围。

优化建议：系统提供的模型或索引优化建议，选择完成后点击通过，相应的修改会体现在模型或索引中。

提示：优化建议只出现在开启了智能推荐的	AI	增强模式中。开启方式请您参考项目设置。

分区设置：为模型设置时间分区列。

导出模型：导出模型元数据。

注意：由于锁定状态的索引会在新索引构建完成后被删除，所以导出的模型元数据中将不包含锁定状态的索

引。

导出	TDS：导出模型的	TDS	文件。

重命名：修改模型的名称。

克隆：复制一个完全一样的模型，您可以定义这个新模型的名称。新模型与原模型具有同样的事实表、维度表、表

间关联、维度、度量、可计算列、时间分区列、聚合索引、明细索引等，但是新模型不具有数据，您需要手动为该

模型加载数据。

注意：由于锁定状态的索引会在新索引构建完成后被删除，所以克隆的模型中将不包含锁定状态的索引。

变更所有者：修改模型的所有者，仅系统管理员和项目管理员具有修改模型所有者的权限。

删除：删除模型，同时删除模型中保存的数据。

清空：清空模型已加载的所有数据。

模型下线：ONLINE	/	WARNING	状态下使模型下线，下线的模型不能服务于任何查询。

模型上线：OFFLINE	状态下使模型上线，上线的模型可以服务于查询分析。

注意：请您注意当模型状态为	BROKEN	时，您只能执行删除模型的操作。

模型详情

模型中包含了	Segment	和索引。你可以点击模型名称以展开模型的详情，如下图所示：

308

模型概念与操作

索引组详情

基本信息：查看总览的详情，您可以在模型总览部分了解详情。

数据特征：查看模型中的表采样信息。

Segment：查看	Segment	的详情，您可以在Segment	操作与设置章节了解详情。
索引：查看模型索引展示以及列表。

索引总览：查看模型下索引总览。

优化建议：查看模型优化建议，通过智能推荐了解详情。

聚合组：您可以查看已定义的聚合组或者新增聚合组，通过聚合索引章节了解详情。

明细索引：您可以查看已定义的明细索引或者新增明细索引，通过明细索引章节了解详情。

开发者：查看模型开发者信息。

JSON：查看模型的所有信息。Kyligence	Enterprise	用	 	JSON		格式的数据描述了模型的设计信息、维度信息、
度量信息等信息。

SQL：模型中的表和列的相关信息组成的	SQL	语句，如表之间的关联关系。

模型总览

在模型列表页面展开某个模型后，您可以看到模型总览页面，帮助快速掌握模型信息。

309

模型概念与操作

展开模型

在此页面，您可以查看模型的	ER	图。

查看	ER	图

您也可以直接查看模型包含的维度和度量信息。

310

模型概念与操作

查看维度信息

查看度量信息

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

311

模型设计进阶

模型设计进阶

本章将基于样例数据集，重点介绍	AI	增强模式下模型设计的基本思想和相关步骤。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

312

模型设计进阶

度量设计

在	AI	增强模式	的项目中，您可以自定义模型的度量。

此小节主要介绍了模型设计中的度量设计。Kyligence	Enterprise	不仅提供了	SUM、MAX、MIN	和	COUNT	等基本度
量，还提供了	TopN，精确去重计数，近似去重计数，近似	Percentile，COLLECT_SET	等高级度量。

在模型编辑界面，您有三种添加度量的方式：

注意：请您完成模型设计之后再进行度量设计，并在模型编辑界面点击右侧的	M	按钮以展开度量列表。

拖拽添加：将希望定义为度量的列从模型中拖拽至度量列表区域，然后在弹窗中编辑度量。

单独添加：点击度量列表上方的第一个	+（增加）按钮，然后在弹窗中编辑度量。

批量添加：点击度量列表上方中间的	+（批量增加）按钮，然后在弹窗中批量添加度量。

注意：批量添加的度量函数仅包括	SUM、MAX、MIN、COUNT	和	COUNT	DISTINCT	(Precisely)，如果您
需要添加其他高级度量，请您选择前两种方式。

已知限制

SUM	度量在计算的列类型是	 	decimal(P,D)		时，精度为	 	P+10	，最大精度为	38，并且不支持自定义精度。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

313

模型设计进阶

Top	N	度量	（Beta）

我们在生活中也总是看到“世界100强公司”、“最受欢迎的20大电子产品”等新闻标题的报道。Top	N	分析也是数据分析场
景中常常遇到的需求。因而易见，人们普遍认同分析顶级项对大多数数据分析都是很有价值也很有必要的。在大数据时

代，这种需求显现得越来越强，因为明细数据集越来越大。在没有预计算的情况下，得到一个分布式大数据集的	Top-N
结果需要很长时间，导致点对点查询的效率很差。

在本产品	v2.1	版本中，我们引入了	Top-N	度量，旨在在索引构建的时候预计算好需要的	Top-N。在查询阶段，
Kyligence	Enterprise	就可以迅速获取并返回	Top-N	记录。这样，查询性能就远远高于没有	Top-N	预计算结果的查询性
能，使得分析师对数据的查询更有力。

在	Kyligence	Enterprise	AI	增强模式	的项目中，您可以自定义	Top-N	度量。

注意：这里的	Top-N	度量是一个近似的实现，为了更好的应用它，你需要更多的了解	Top-N	背后的算法和数据分
布的结构。

Top-N	查询语句

下文以	Kyligence	Enterprise	AI	增强模式指引中创建的项目为例，介绍	Top-N	的度量设置。该项目选取了	Hive	数据源中
的	SSB	数据集，并需要完成模型设计和索引构建（包括加载数据）。没有索引和数据的模型，无法服务任何查询。您
可以查看基本模型设计章节了解模型设计的方法。

我们将使用其中的事实表	 	SSB.P_LINEORDER	。这张样例表模拟了在线集市的交易数据，内含多个维度和度量列。这里我
们仅用其中的四列即可： 	LO_ORDERDATE	， 	LO_SUPPKEY	， 	LO_PARTKEY		和	 	LO_ORDTOTALPRICE	。下表为这些列的简介。

列名

描述

LO_ORDERDATE

订单日期

LO_SUPPKEY

LO_PARTKEY

LO_ORDTOTALPRICE

供应商	ID	号，”1“	代表	”Supplier#000000001“

商品	ID	号

订单总额

基数

2384

20

2023

-

方法1：该在线集市需要查询供应商中特定时段内订单总额最高的	100	种商品。请点击左侧导航栏查询->分析，在查询
编辑器中输入以下查询语句：

SELECT	LO_PARTKEY,	SUM(LO_ORDTOTALPRICE)	AS	TOTAL_AMOUNT

FROM	SSB.P_LINEORDER

WHERE	LO_ORDERDATE	between	'1993-06-01'	AND	'1994-06-01'

AND	LO_SUPPKEY	in	(1)

group	by	LO_PARTKEY

order	by	SUM(LO_ORDTOTALPRICE)	DESC

limit	100

查询结果显示如下：

314

模型设计进阶

SQL	查询结果

方法2：为了在海量数据集上得到理想的查询性能结果，我们推荐在创建模型时，对目标列创建	Top-N	度量并进行预计
算。请您在创建模型的界面，根据如下方法添加度量。请您填写度量名称，如	 	TOTAL_AMOUNT	，选择函数为	TOP_N，选
择函数参数为	Top	100，最后请从列的下拉列表中选择目标列。

315

模型设计进阶

添加	Top-N	度量界面

度量添加完毕并且保存模型后，您需要进入编辑聚合索引界面，根据您的业务场景，将对应的维度和度量添加至适当的

聚合组，提交后会生成新的聚合索引。在本示例中新的索引将包含维度	 	LO_ORDERDATE	， 	LO_SUPPKEY	， 	LO_PARTKEY		和
度量	 	SUM(LO_ORDTOTALPRICE)	，您需要构建索引和加载数据以完成对目标列的预计算。系统将自动重新构建索引和加载
数据以完成对目标列的预计算。您可以在任务监控界面查看索引构建的进度，索引构建完毕后，您就可以使用	Top-N
的方法查询销量最好的商品了。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

316

模型设计进阶

精确去重计数

Count	Distinct	是一个对大多数数据分析师都很常用的函数。本产品	v2.1版本开始，通过位图算法支持了	Count	Distinct
精确查询。对于数据类型为	tinyint，	smallint	和	int	的数据，将把数据对应的值直接打入位图中。对于数据型为	long，
string	和其他的数据，产品将他们编码成字符串放入字典，然后再将对应的值打入位图。返回的度量结果是已经序列化
的位图数据，而不仅是计算的值。这确保了不同的	segment	中，甚至跨越不同的	segment	来上卷，结果也是正确的。

在	Kyligence	Enterprise	AI	增强模式	的项目中，您可以自定义	Count	Distinct	精确去重计数的度量。

查询前提

在使用	Count	Distinct	查询之前，您需要确认目标列是否预存了	Count	Distinct	的预计算结果。您可以在导航栏	数据资产
->	模型，选择需要查看度量的模型，点击编辑进入模型编辑页，点击页面右上方M展开度量表来查看度量的详细信息。
如果目标列已经被进行过	Count	Distinct	的预计算（函数（Function）为	count_distinct	并且	返回类型（Return	Type）为
bitmap），则表示此列可以直接进行	Count	Distinct	的精确去重计数。否则，你需要创建类型为	Count	Distinct	的新度量
来存储目标列的预计算结果。

Count	Distinct	精确查询设置

下文以	Kyligence	Enterprise	AI	增强模式指引中创建的项目为例，介绍	Count	Distinct	近似去重计数的度量设置。该项目
选取了	Hive	数据源中的	SSB	数据集，并需要完成模型设计和索引构建（包括加载数据）。没有索引和数据的模型，无
法服务任何查询。您可以查看基本模型设计章节了解模型设计的方法。

请您在创建模型的界面，根据如下方法添加度量。请您填写度量名称，如	 	DISTINCT_CUSTOMER	，选择函数为
COUNT_DISTINCT，之后请选择函数参数中的误差选项,最后请从列的下拉列表中选择目标列。

产品提供	Count	Distinct	的近似值查询和精确值查询。如需要得到某列的精确去重预计算值，你应选择基于位图
（bitmap）算法的返回类型：Precisely。这种精确去重的度量能够在存储资源充足的情况下返回一个非常精确的结果。
例如，如果查询数据为百万级，则返回的一个结果的大小将为百兆左右。

Count	Distinct	精确去重计数查询因为使用位图算法，所以需要消耗的资源也较多，在使用	Count	Distinct	精确去
重计数查询计算具有亿级基数的表时，请咨询	Kyligence技术支持	评估集群资源是否充足。

317

模型设计进阶

添加	Count	Distinct	精确去重计数度量界面

度量添加完毕并且保存模型后，您需要进入编辑聚合索引界面，根据您的业务场景，将对应的维度和度量添加至适当的

聚合组，提交后会生成新的聚合索引，您需要构建索引和加载数据以完成对目标列的预计算。您可以在任务监控界面查

看索引构建的进度，索引构建完毕后，您就可以使用	Count	Distinct	的方法查询精确去重计数了。

如果您选择从	0	开始创建模型并添加	Count	Distinct	类型的度量值，请您为创建的模型添加索引并加载数据。没有索引
和数据的模型，无法服务任何查询。您可以查看基本模型设计章节了解模型设计的方法。

关于	Count	Distinct	的近似查询请参见近似去重计数。

参考文献

Use	Count	Distinct	in	Apache	Kylin	(Yerui	Sun)

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

318

模型设计进阶

近似去重计数

Count	Distinct	是一个对大多数数据分析师都很常用的函数，用于计算一个（多重）集合中不重复元素个数。但是在大数
据场景下计算精准的	Count	Distinct	值，成本是比较昂贵的。本产品	v2.1	版本开始，通过	HyperLogLog	算法支持了
Count	Distinct	近似值计算，并提供了从	9.75%	到	1.22%	几种不同的误差率以支持不同的查询需求。

提示：如果你不要求非常精准的查询结果，这种近似的	Count	Distinct	查询就可以在有限的存储资源条件下，返回
一个相对准确的查询结果。

在	Kyligence	Enterprise	AI	增强模式	的项目中，您可以自定义	Count	Distinct	近似去重计数的度量，并且给您提供了	5	种
误差选项：

Error	Rate	<	9.75%

Error	Rate	<	4.88%

Error	Rate	<	2.44%

Error	Rate	<	1.72%

Error	Rate	<	1.22%

查询前提

下文以	Kyligence	Enterprise	AI	增强模式指引中创建的项目为例，介绍	Count	Distinct	近似去重计数的度量设置。该项目
选取了	Hive	数据源中的	SSB	数据集，并需要完成模型设计和索引构建（包括加载数据）。没有索引和数据的模型，无
法服务任何查询。您可以查看基本模型设计章节了解模型设计的方法。

在查询	Count	Distinct	之前，您需要确认建立的模型中是否已经建立了对应的	Count	Distinct	度量。具体的查看方法，可
以在导航栏	数据资产	->	模型	进入模型编辑界面查看度量详细信息。如果度量中包含以目标列作为参数的	Count	Distinct
近似度量（函数（Function）为	count_distinct	并且	返回类型（Return	Type）为	hllc），则表示此列可以直接进行	Count
Distinct	的近似去重查询。否则，您需要创建类型为	Count	Distinct	的新度量来存储目标列的预计算结果。

编辑度量

请您在创建模型的界面，根据如下方法添加度量。填写度量名称，如	 	DISTINCT_SHIPPRIOTITY	，选择函数为
COUNT_DISTINCT，之后请选择函数参数中的误差选项，最后请从列的下拉列表中选择目标列。

319

模型设计进阶

添加	Count	Distinct	近似去重计数度量界面

度量添加完毕并且保存模型后，点击弹窗中添加索引进入模型索引页面，您需要点击聚合组标签下的+(添加聚合组），
根据您的业务场景，将对应的维度和度量添加至适当的聚合组，提交后会生成新的聚合索引，您需要构建索引和加载数

据以完成对目标列的预计算。您可以在任务监控界面查看索引构建的进度。索引构建完毕后，您就可以使用	Count
Distinct	查询近似去重计数，比如以下	SQL。

SELECT	COUNT(DISTINCT	P_LINEORDER.LO_SHIPPRIOTITY)

FROM	SSB.P_LINEORDER

如果您选择从	0	开始创建模型并添加	Count	Distinct	类型的度量值，请您为创建的模型添加索引并加载数据。没有索引
和数据的模型，无法服务任何查询。您可以查看基本模型设计章节了解模型设计的方法。

关于	Count	Distinct	的精确查询信息请参见精确去重计数介绍。

参考文献

Use	Count	Distinct	in	Apache	Kylin	(Yerui	Sun)

320

模型设计进阶

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

321

模型设计进阶

近似	Percentile

Kyligence	Enterprise	支持	Percentile	函数。在	V2.5.4	以上的版本中，函数名称改为	PERCENTILE_APPROX，二者用法相
同。如果您预定义了百分比度量，则此类	SQL	查询可以实现亚秒级延迟。

该函数提供三种返回类型： 	percentile(100)	、 	percentile(1000)		和	 	percentile(10000)	，表示精确度逐步提升，同时
占用的存储资源也越多。一般场景中，我们推荐您使用	 	percentile(100)		即可。

在	Kyligence	Enterprise	AI	增强模式	的项目中，您可以自定义	PERCENTILE_APPROX	的度量。

PERCENTILE_APPROX	简介

PERCENTILE_APPROX	函数返回数值的第	p	个百分位数的值，其语法如下：

percentile_approx({measure},	p,	B)

其中	measure	为要查询的度量，p	为	0	到	1	之间的百分比数字，包含	0	和	1，B	控制近似精度，B	越大，结果的精确度越
高。PERCENTILE_APPROX	函数用插值法来确定第	p	个百分位数的值。

使用场景

下文以	Kyligence	Enterprise	AI	增强模式指引中创建的项目为例，介绍	Percentile	函数的度量设置。该项目选取了	Hive	数
据源中的	SSB	数据集，并需要完成模型设计和索引构建（包括加载数据）。没有索引和数据的模型，无法服务任何查
询。您可以查看基本模型设计章节了解模型设计的方法。

我们将使用其中的事实表	 	SSB.P_LINEORDER	。这张样例表模拟了在线集市的交易数据，内含多个维度和度量列。这里我
们仅用其中的两列即可： 	LO_SUPPKEY	， 	LO_ORDTOTALPRICE	。下表为列的简介。

列名

描述

LO_SUPPKEY

LO_ORDTOTALPRICE

供应商	ID	号

订单总额

我们希望查询每个供应商的订单总额中数据在第	50	个百分比的值，查询示例如下：

SELECT	LO_SUPPKEY,	percentile_approx(LO_ORDTOTALPRICE,	0.5)	AS	ORDER_TOTAL_PRICE

FROM	SSB.P_LINEORDER

GROUP	BY	LO_SUPPKEY

322

模型设计进阶

在未添加	PERCENTILE_APPROX	度量之前，如果您开启了查询下压，查询将被下压至	Hive。

使用方法

请您在创建模型的界面，根据如下方法添加类型为	PERCENTILE_APPROX	的度量。请您填写度量名称，如
	PERCENTILE_ORDTOTALPRICE	，选择函数为	PERCENTILE_APPROX。之后请选择函数参数中的返回类型，这里的返回类
型即上述语法中的	B，B	值越大，结果的精确度越高。我们提供三种返回类型：	 	percentile(100)	、 	percentile(1000)
或	 	percentile(10000)	。最后请从列	的下拉列表中选择目标列。

323

模型设计进阶

添加	PERCENTILE_APPROX	度量界面

度量添加完毕并且保存模型后，点击弹窗中添加索引进入模型索引页面，您需要点击聚合组标签下的+(添加聚合组），
根据您的业务场景，将对应的维度和度量添加至适当的聚合组，提交后会生成新的聚合索引。在本示例中新的索引将包

含维度	 	LO_SUPPKEY		和度量	 	percentile_approx(LO_ORDTOTALPRICE,	p,	100)	，您需要构建索引使之可用。在任务监控界
面您可以查看索引构建的进度，索引构建完毕后，您就可以使用	PERCENTILE_APPROX	的方法查询近似值了。

在导航栏	查询	->	分析	界面重新输入上述	SQL	语句提交查询，查询结果返回每个供应商的订单总额中数据在第	50	个百
分比的值。

324

模型设计进阶

SQL	查询结果

注意事项

在	V2.5.4	以上的版本中，函数名称由	percentile	改为	PERCENTILE_APPROX,	同时也兼容	percentile	的用法。当查询击
中模型时（无论是否有定义	percentile_approx	度量)，二者用法和效果相同，返回结果均为估算的百分位数;	当查询下压
时，查询结果由下压引擎直接提供，其中	percentile	函数将提供准确的百分位数，PERCENTILE_APPROX	函数会提供估
算的百分位数。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

325

模型设计进阶

相关性函数	CORR	(Beta)

相关性系数通常在统计中用于测量两个变量间的相关性强弱。在本产品	V4.5.5版本以上，支持使用相关系数函数，函数
名为	corr。计算相关性的算法采用的是	Pearson	correlation。

CORR	简介

CORR	函数返回数值为衡量两个变量之间的线性关系。结果为double类型，范围为	-1	至	+1（包括	-1	和	+1），其中	1	表
示精确的正向线性关系，比如一个变量中的正向更改即表示另一个变量中对应量级的正向更改，0	表示变量之间没有线
性关系，而	−1	表示精确的反向关系。

使用的规则如下：

corr({col1}，{col2}),	col1,	col2	为要计算的度量。其中需要注意的是，在当前版本中，所支持度量的数据类型为：
bigint，integer，int4，long8，tinyint，smallint，decimal，double，float，real	和	numeric。日期类型暂不支持计
算。

查询示例如下：

SELECT	corr(ITEM_COUNT,	PRICE)

FROM	TEST_KYLIN_FACT

使用方法

首先，在编辑模型界面，点击添加新的度量。

添加度量页面

第二步，选择	corr	函数，并选取对应希望计算相关性的列。

326

模型设计进阶

选择CORR表达式

第三步，保存模型并构建相关索引后，即可到分析页面进行查询。

327

模型设计进阶

注意事项

SQL	查询

1.	 由于	corr	度量需要预计算的特殊性，该度量可能会在模型上创建一系列的内部度量（对普通用户隐藏）和cc列，

Kyligence	Enterpise会自动管理这些内部度量。对于cc列，如果你希望删除这些自动生成的cc列，需要先删除对应的
corr度量。

2.	 如果所选取的列包含null值，可能导致计算结果不正确，可以通过在保存模型时设置数据筛选条件过滤掉null值

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

328

模型设计进阶

COLLECT_SET

从	v4.0.11	版本后，Kyligecnce	Enterprise	支持	COLLECT_SET	函数，它以数组形式返回一组唯一的值，其语法为
	COLLECT_SET(column)	。在智能模式中，系统会根据您的查询推荐包含	COLLECT_SET	度量的索引。在	AI	增强模式
中，您可以自定义	COLLECT_SET	度量。

使用场景

下文以	Kyligence	Enterprise	AI	增强模式指引中创建的项目为例，介绍	COLLECT_SET	函数的度量设置。该项目选取了
Hive	数据源中的	SSB	数据集，并需要完成模型设计和索引构建（包括加载数据）。没有索引和数据的模型，无法服务
任何查询。您可以查看基本模型设计章节了解模型设计的方法。

我们将使用其中的事实表	 	SSB.P_LINEORDER	。这张样例表模拟了在线集市的交易数据，内含多个维度和度量列。这里我
们仅用其中的两列即可： 	LO_CUSTKEY	， 	LO_ORDERDATE	。下表为列的简介：

列名

LO_CUSTKEY

LO_ORDERDATE

描述

顾客	ID	号

订单日期

我们希望查询每个顾客的订单日期组合，订单日期以数组形式返回去重后的值，查询示例如下：

SELECT	LO_CUSTKEY,	COLLECT_SET(LO_ORDERDATE)

FROM	SSB.P_LINEORDER

GROUP	BY	LO_CUSTKEY

在未添加类型为	COLLECT_SET	的度量之前，查询将下压至	Hive，根据源表的数量级，结果返回时间可能需要数分
钟。

使用方法

请您在创建模型的界面，根据如下方法添加类型为	COLLECT_SET	的度量。请您填写度量名称，如
	COLLECT_SET_ORDERDATE	，选择函数为	COLLECT_SET。最后请从列的下拉列表中选择目标列，如
	P_LINEORDER.LO_ORDERDATE	。

329

模型设计进阶

添加	COLLECT_SET	度量界面

度量添加完毕并且保存模型后，点击弹窗中添加索引进入模型索引页面，您需要点击聚合组标签下的+(添加聚合组），
根据您的业务场景，将对应的维度和度量添加至适当的聚合组，提交后会生成新的聚合索引。在本示例中新的索引将包

含维度	 	LO_CUSTKEY		和度量	 	COLLECT_SET(LO_ORDERDATE)	，您需要构建索引和加载数据以完成对目标列的预计算。您可
以在任务监控界面查看索引构建的进度，索引构建完毕后，您就可以使用	COLLECT_SET	函数执行相应的查询并且使
用预计算数据了。

再次查询上述	SQL，获得以下结果：

330

模型设计进阶

查询结果

如果您选择从	0	开始创建模型并添加	COLLECT_SET	类型的度量值，可以查看基本模型设计章节了解模型设计的方
法。

在实际的应用场景中，您可以将	COLLECT_SET	函数与其他函数结合使用，以适用更多的分析场景。如以下查询结合
了	CONCAT_WS	函数，它将订单日期组成的数组中的值拼接为字符串，并且以	 	;		分割：

SELECT	LO_CUSTKEY,	CONCAT_WS(';',	COLLECT_SET(LO_ORDERDATE))

FROM	SSB.P_LINEORDER

GROUP	BY	LO_CUSTKEY

331

模型设计进阶

查询结果

注意：CONCAT_WS	函数在查询时仅支持与	COLLECT_SET	函数结合使用。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

332

模型设计进阶

Sum	Expression

在很多业务的数据分析场景中，sum(expression)	是比较常见的	SQL	用法。

在之前版本中，需要通过创建表索引或可计算列的方式满足该类查询。而在	v4.1.2	版本后，支持通过模型直接回答部分
sum(expression)	的查询。

使用方法

该功能默认为关闭状态，需在	 	$KYLIN_HOME/conf/kylin.properties		中配置参数开启。

kylin.query.convert-sum-expression-enabled=true

目前在	Kyligence	Enterprise	中支持了以下五种	sum(expression)	函数：

sum(case	when)

sum(column	*	constant)

sum(constant)

sum(cast(case	when))
sum(if)（从	v	4.6.13.0	版本开始）

这里我们将以产品自带的样例数据集为例说明具体用法。有关样例数据集的更多信息请参考样例数据集。

sum(case	when)	函数

以下面	SQL	为例：

select

		sum(case	when	ORDERPRIOTITY='1-URGENT'	then	ORDTOTALPRICE	else	null	end)

from	LINEORDER

要执行它，启用	sum(expression)	功能后，还需如下设置模型：

将	 	when		子句中出现的所有列定义为维度，如此例中的	 	ORDERPRIOTITY		维度
将	 	then		子句中出现的所有列定义为	Sum	度量，如此例中的	 	sum(ORDTOTALPRICE)		度量

然后，模型即可执行上述	SQL。

sum(column*constant)	函数

以下面	SQL	为例：

select	sum(ORDTOTALPRICE	*	3)	from	LINEORDER

要执行它，启用	sum(expression)	功能后，还需如下设置模型：

将	Sum	函数中的列定义为	Sum	度量，如此例中的	 	sum(ORDTOTALPRICE)		度量

然后，模型即可执行上述	SQL。

sum(constant)	函数

以下面	SQL	为例：

select	sum(3)	from	LINEORDER

333

模型设计进阶

要执行它，只需启用	sum(expression)	功能即可，无需在模型上做其他设置。

sum(cast(case	when))	函数

以下面	SQL	为例：

select	sum(cast((case	when	ORDERPRIOTITY='1-URGENT'	then	ORDTOTALPRICE	else	null	end)	as	bigint))	from	LINEORDE

R

要执行它，在启用	sum(expression)	功能即后，还需如下设置模型：

将	 	when		子句中出现的所有列定义为维度，如此例中的	 	ORDERPRIOTITY		维度
将	 	then		子句中出现的所有列定义为	Sum	度量，如此例中的	 	sum(ORDTOTALPRICE)		度量

然后，模型即可执行上述	SQL。

sum(if)	函数

从	Kyligence	Enterprise	4.6.13.0	开始，支持	case-when	的等价表达式使用	if	改写。

以下面	SQL	为例：

select	sum(if(ORDERPRIOTITY='1-URGENT',	ORDTOTALPRICE,	null))	from	LINEORDER

要执行它，启用	sum(expression)	功能后，还需如下设置模型：

将	 	if		表达式中的第一个参数中出现的所有列定义为维度，如此例中的	 	ORDERPRIOTITY		维度
将	 	if		表达式中的第二个和第三个参数中出现的所有列定义为	Sum	度量，如此例中的	 	sum(ORDTOTALPRICE)		度量

然后，模型即可执行上述	SQL。

已知限制

1.	 由于对于	null	值的处理较为复杂，因此在当前版本中暂时不支持解析	 	sum(column+column)		或

	sum(column+constant)		等类型的函数。如您需要需要使用这些函数，您可以通过创建可计算列或表索引满足上述需
求。

2.	 在当前版本中暂时不支持	 	topN		与	 	sum(case	when)		同时使用。 	count(distinct)	， 	collect_set	， 	percentile		与

	sum(case	when)		可以同时使用，但是不能使用单一索引一次性全部回答。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

334

模型设计进阶

Count	Distinct	Case	When	Expression

在一些业务的数据分析场景中，会遇到	Count	Distinct	Case	When	Expression	的	SQL	用法。

在之前版本中，如果希望通过模型预计算加速此类查询，一般需要将	Case	When	Expression	设置为可计算列，再设置
Count	Distinct	Computed	Column	度量，以回答此类查询。

从	Kyligence	Enterprise	V4.3.3	版本开始，我们针对此类查询提供了专门的优化，允许用户只需要设置	Count	(Distinct
Column)	度量，	系统利用预计算结果，加少量的	Case	When	Expression	在线计算，即可完整回答查询，减少了模型设置
的复杂度，提高用户体验。

使用方法

1、开启优化

该功能默认为关闭状态，支持系统级或项目级开启。

系统级开启，在	$KYLIN_HOME/conf/kylin.properties	中配置参数开启。项目级开启，在设置-高级设置-自定义项目配置
中添加配置开启。

kylin.query.convert-count-distinct-expression-enabled=true

2、支持的	Count	Distinct	Case	When	Expression	语法

count(distinct	case	when	{condition}	then	{column}	else	null	end)

注意：

a.	{condition}	为维度列表达式，例如	 	cal_dt	=	'2012-01-01'	。

b.	{column}	必须被设置为	 	count	(distinct	column)		度量。

c.选择函数参数中的误差选项时必须选择返回类型：Precisely，否则不能触发该语法的优化（见下图）

335

模型设计进阶

添加	Count	Distinct	精确去重计数度量界面

功能开启后，符合上述语法的查询，可以被包含 	condition		表达式中的维度列和	 	count(distinct	column)	度量的索引回
答。

示例:

count(distinct	(case	when	cal_dt	=	date'2012-01-01'	then	price	else	null	end))

可以被包含	 	cal_dt		维度， 	count(distinct	price)		度量的索引回答

已知限制

1.	 else	后只能为	null，暂不支持其他常量的情况，如	 	case	when	...	then	column1	else	1	end	。	从KE	4.5.4	GA	版本开
始，else	后可以为	cast(null	as	 	type	)，如	 	case	when	...	then	column1	else	cast(null	as	double)	end	。需要注意的
是， 	type		尽量与	 	column1	的	类型相同或者为同一大类，否则将可能不符合sql语法而报错，或者无法应用上此功
能。大类指的是同为数值型、日期型、布尔型等。

336

模型设计进阶

2.	 case	后只支持一对	 	when	..	then	..	，暂不支持多对的情况，如	 	case	when	..	then	column1	when	...	then	column2

else	null	end	。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

337

模型设计进阶

半累加度量	(Beta)

度量可以分为累加度量、半累加度量和不可累加度量，数据按照其业务属性，需要应用不同类型的度量对其进行聚合，

以产生具有实际业务意义的聚合结果。因为半累加度量的聚合方式介于累加度量和不可累加度量之间，我们先对后两者

进行简单说明。

累加度量作用的对象是：使用统一规则，按照不同维度累加后都是有实际意义的业务数据。在真实的业务场景中，比较

常见的是对订货量的求和，我们既可以按照客户维度进行求和，聚合后的结果表示每个客户的总订货量；也可以按照时

间维度进行求和，聚合后的结果表示一段时间内的总订货量。可见，这两个结果都可以作为反映订货量变化的指标。

不可累加度量作用的对象是：累加的结果是没有实际意义的业务数据。比如价格，商品类别，即使使用数字表示，但是

累加的结果也是没有意义的，我们常对其使用的度量为计数(Count	Distinct)等。

半累加度量介于前两者之间，这类度量作用的对象是某些情况下累加有意义，但在特定情况下不可累加，累加出的结果

是无意义的。这类数据最常见的是账户余额，余额可以按照客户维度进行累加，表示每个客户的账户余额汇总，但不能

按照时间维度进行每日资金余额的汇总操作，对每日余额的汇总是没有意义的，而是需要取最新日期对应的余额数据，

这类度量就是半累加度量。在很多业务的数据分析场景中，半累加度量可以用于处理证券、账户余额、人力资源等业务

领域。

本产品从	v4.6.2.0	版本开始，实现了对半累加度量的支持。在	Kyligence	Enterprise	中定义聚合函数为	SUM_LC	的度量
时，可以启用半累加度量，指定半累加函数和时间维度，即可实现度量的半累加行为。Kyligence	Enterprise	在聚合计算
时，对于每一个	Group	By	结果集的多条记录，只取时间维度上最靠后的记录，如果时间最靠后有多条记录，再将它们
进行正常的累加。

使用方法

半累加功能要求事实表包含随时间变化的快照数据，比如产品库存快照，或账户余额快照。快照数据要求每一个记录时

间点上都有所有账号的一条记录，比如下面的	SEMI_SCENE	表。

TX_DATE

ACCOUNT

EXPENSE

INCOME

BALANCE

2018-01-01

2018-01-01

2018-01-01

2018-02-15

2018-02-15

2018-02-15

account_a

account_b

account_c

account_a

account_b

account_c

100

200

300

0

0

0

0

0

0

200

300

50

1000

800

500

1200

1100

550

SEMI_SCENE	表中有两个记录时间点，分别是	2018-01-01	和	2018-02-15，且每个时间点上都有	3	个账号的记录，是标准
的快照数据。

在这种情形下，就可以将账户余额	BALANCE	定义为半累加度量，在交易时间	TX_DATE	维度上对账户余额进行聚合取
最后的记录。下面是如何定义该半累加度量。

1.	 以	SEMI_SCENE	为事实表创建模型。

2.	 在度量版面添加度量，选择	SUM_LC(column1,column2)	函数。

3.	 选择	BALANCE	为列，TX_DATE	为时间维度。

4.	 半累加函数为	LastChild，是当前唯一支持的函数。

5.	 完成其他模型信息并保存。

338

模型设计进阶

339

模型设计进阶

构建加载数据后，就可以查询。例如：

1.	 分析每个账户支出总额、收入总额和账户余额

SELECT	ACCOUNT,	SUM(EXPENSE),SUM(INCOME),SUM_LC(BALANCE,TX_DATE)

FROM	SEMI_SCENE

GROUP	BY	ACCOUNT

结果为

account_a,	100,	200,	1200

account_b,	200,	300,	1100

account_c,	300,	50,	550

2.	 获得	2018	年	1	月底的所有账户余额

SELECT	ACCOUNT,	SUM_LC(BALANCE,TX_DATE)

FROM	SEMI_SCENE

WHERE	TX_DATE	<=	'2018-01-31'

GROUP	BY	ACCOUNT

结果为

account_a,	1000

account_b,	800

account_c,	500

3.	 分析	2018	年所有账户的总支出、总收入、总账户余额

SELECT	SUM(EXPENSE),SUM(INCOME),SUM_LC(BALANCE,TX_DATE)

FROM	SEMI_SCENE

WHERE	YEAR(TX_DATE)	=	2018

结果为

600,	550,	2850

4.	 分析	2018	年每个月所有账户的总支出、总收入、总账户余额

SELECT	MONTH(TX_DATE),SUM(EXPENSE),SUM(INCOME),SUM_LC(BALANCE,TX_DATE)

FROM	SEMI_SCENE

WHERE	YEAR(TX_DATE)	=	2018

GROUP	BY	MONTH(TX_DATE)

结果为

1,	600,	0,	2300

2,	0,	550,	2850

注意事项和已知限制

半累加度量不支持明细索引和查询下压。

半累加度量中的时间维度列，不支持的数据类型为tinyint,	float,	double,	decimal,	bool。

340

模型设计进阶

半累加度量中的时间维度列，如果是维表中的列，则事实表和维度表关联关系中必须勾选预计算关联关系。

如果模型关联关系中存在"一对多或多对多"导致数据膨胀，查询结果可能与用户期望不符。

如果开启智能推荐，查询中必须使用	SUM_LC	语法才可以推荐半累加度量。

半累加度量列如果为	decimal	类型，字段中如果包含	NULL	值，可能导致结果不正确。

如果事实表中并非完整的快照数据，查询的结果可能与用户的期望不符。

比如下面的数据集，在	2018-02-15	时间点上缺失	2	条记录：

TX_DATE

ACCOUNT

EXPENSE

INCOME

BALANCE

2018-01-01

2018-01-01

2018-01-01

2018-02-15

此时查询

account_a

account_b

account_c

account_a

100

200

300

0

0

0

0

200

1000

800

500

1200

		SELECT	ACCOUNT,	SUM_LC(BALANCE,TX_DATE)

		FROM	SEMI_SCENE

		GROUP	BY	ACCOUNT

结果为

		account_a,	1200

		account_b,	800

		account_c,	500

可能与期望	2018-02-15	时刻	account_b	和	account_c	余额不存在即为零不符。

此外，如果在	2018-02-15	时刻有多条	account_a	的记录，也会导致查询结果有歧义。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

341

模型设计进阶

可计算列

可计算列(Computed	Column)	是为了充分利用	Kyligence	Enterprise	的预计算能力而在模型中预先定义的数据列。通过将
相对复杂的在线计算转换成基于可计算列的预计算，查询的性能将会得到大幅提升。此外，可计算列支持将数据的转

换、重定义等操作预先定义在模型中，增强数据语义层。通过定义可计算列，用户可以重用已有的业务逻辑代码。

本节将介绍	Kyligence	Enterprise	中支持的可计算列，包括可计算列的基本概念和使用方法，以及可计算列支持的函数。

基本概念

命名：	支持字母、数字和下划线，不支持纯数字或者以下划线开头的命名。

表达式：	指可计算列的实际计算逻辑。可计算列的表达式可以并且只可以使用当前模型中事实表或者维度表上的
列。

复用与嵌套：

可计算列是按模型隔离的，但它们会隐式的绑定事实表，同一个表达式不能在不同的模型上创建不同名称的可

计算列。

同一个项目下，可计算列严格意义上说不存在跨模型复用，如果需要复用，需要在不同模型上分别定义一个名

称和表达式完全一致的可计算列。

同一个模型下，可计算列的表达式里面可以嵌套其它的可计算列，支持多层嵌套。

特殊注意事项：

同一个表达式不能在不同的模型上创建不同名称的可计算列。以同一个项目下的两个模型	 	M1		和	 	M2		详细说明：

如果	 	M1		和	 	M2		的事实表相同（都为	 	T1		），且	 	M1		上定义了可计算列	 	CC1	=	T1.C1	+	T1.C2	， 	M2		上创建
可计算列的时候，不能创建可计算列	 	CC2	=	T1.C1	+	T1.C2	，但可以创建可计算列	 	CC1	=	T1.C1	+	T1.C2	；
如果	 	M1		和	 	M2		的事实表相同（都为	 	T1		），且	 	M1		上定义了可计算列	 	CC1	=	T1.C1	+	T1.C2	， 	M2		上创建
可计算列的时候，不能创建可计算列	 	CC2	=	T1.C1	+	T1.C2	，但可以创建可计算列	 	CC2	=	T1.C1	*	T1.C2	；

其他注意事项：

可计算列默认且只能定义在事实表上，定义后不可修改名称，可以修改表达式。

可计算列的表达式可以使用当前模型中任意表上的列，但是如果模型中的多个表存在相同的列名时，请务必保

证列的名称都满足	 	表的别名.列名		的形式。
可计算列的名称不可与事实表或者维度表上的列同名，这可能会导致非预期的错误。

可计算列的表达式中不可使用聚合函数，如	 	SUM	， 	MIN	，	 	MAX		等。
请勿以常量表达式定义可计算列，以免查询出错，例如： 	power(cast(2	as	double),	2)	。

如果函数表达式中含有列名为关键字的列时，暂时无法被推荐为可计算列。更多关于关键字的介绍，请查看

SQL	规范参考章节中的查询关键字部分。
当前可计算列仅支持	Hive	数据源。
AI	增强模式下暂不支持基于	JDBC	格式的语法表达式创建可计算列。例如： 	{FN	CONVERT(PRICE,
SQL_BIGINT)}	。

可计算列的表达式如果包含有非字母开头或包含特殊字符的表名或者列名，需要在表名或者列名上加双引号。

示例： 	"100_KYLIN_SALES"."100_PRICE"	*	"100_KYLIN_SALES"."200_ITEM_COUNT"	。

从	4.6.6.0	版本开始，可计算列可以作为时间分区列，但有如下已知限制：

不支持可计算列作为多级分区列；

不支持流模型中可计算列作为分区列；

不支持探测时间分区列的时间格式，也不支持构建时获取	Segment	的数据范围；
部分报错提示不准确，需在日志中排查问题。

从	4.6.6.0	版本开始，可计算列可以作为关联键，但有以下已知限制：

不支持	SCD2	模型；
不支持推荐出可计算列作为关联键的模型；

342

模型设计进阶

关联键中的可计算列表达式只能包含事实表的列，否则构建或建模可能报错；

关联键中的可计算列表达式为单个列或常量时，查询无法命中模型；

关联键中的可计算列表达式为嵌套可计算列时，隐式查询无法命中模型；

部分报错提示不准确，需在日志中排查问题。

创建可计算列

如何创建可计算列？	我们以下面的一个场景为例：模型中有一个事实表	 	P_LINEORDER	，包含以下列：

	LO_EXTENDEDPRICE	：	交易价格
	LO_QUANTITY	：	交易数量
	LO_ORDERDATE	：	订单日期

我们想在这张事实表上定义两个可计算列， 	T_PRICE_PER_ITEM		用于表示单个项目的交易总价， 	YEAR_OF_ORDER		用于表
示订单年份。它们的计算逻辑如下：

	T_PRICE_PER_ITEM	=	P_LINEORDER.LO_EXTENDEDPRICE	*	P_LINEORDER.LO_QUANTITY

	YEAR_OF_ORDER	=	YEAR(P_LINEORDER.LO_ORDERDATE)

首先，点击下图所标示的可计算列按钮	CC，这时会弹出可计算列窗口。

可计算列窗口

其次，点击可计算列窗口中的	+，系统会弹出添加可计算列对话框，您需要填入如下信息：

列名：	定义可计算列的名称；
表达式：可计算列的计算逻辑。

343

模型设计进阶

添加可计算列

再次，点击提交按钮，系统会验证可计算列的名称以及可计算列表达式的内容是否合法，如果不合法请根据提示做相应

的修改。待创建完可计算列，模型的事实表上可以看到新生成的可计算列	 	T_PRICE_PER_ITEM	，如下图所示：

344

模型设计进阶

模型中的可计算列

最后，在当前模型的维度窗口中点击	+，可以基于已经创建好的可计算列	 	YEAR_OF_ORDER		添加新维度，如下图所示：

添加基于可计算列的维度

在当前模型的度量窗口中点击	+，可以基于已经创建好的可计算列	 	T_PRICE_PER_ITEM		添加新度量	 	TOTAL_PRICE	，如下
图所示：

345

模型设计进阶

添加基于可计算列的度量

编辑可计算列

在某些情况下，我们需要根据业务需求的变动调整可计算列的表达式。此时，我们可以通过编辑模型直接修改可计算列

的表达式。

346

模型设计进阶

修改可计算列

但是需要注意的是，当前该功能存在较多限制，请仔细阅读以下限制后进行使用：

暂不支持修改可计算列名称

暂不支持修改嵌套可计算列的表达式。若修改的可计算列已被同模型中其他可计算列嵌套，则修改失败，提交模型

修改时会收到类似提示信息： 	模型[model_name]的嵌套可计算列[column_name]已经包含可计算列[column_name]	。

表达式的变更可能会刷新模型下相关的索引，会以弹窗的形式告知用户。

表达式的变更可能会使度量不合法，并自动删除度量、度量相关的聚合组与索引，会以弹窗的形式告知用户。

在索引中使用可计算列

到目前为止，我们在模型中定义了可计算列，并且基于可计算列添加了新的维度和度量。	但是如果需要体现预计算的优
势，我们需要索引中使用新添加的基于可计算列的维度和度量。

您可以在聚合索引或表明细索引中使用可计算列，以下我们以聚合索引为例进行说明。

首先，请您在数据资产-》模型页面点击指定模型名称以展开更多信息，再点击索引进入索引总览页面，如下图所示，
点击+索引以添加索引。

编辑聚合组

添加新的维度并提交，待索引构建成功后，我们完成了创建可计算列，基于可计算列创建维度和度量，并在索引中保存

基于可计算列的预计算数据。

查询可计算列

在模型中创建可计算列之后，可计算列将作为事实表上的一个扩展列，它和事实表上的原始普通列没有差别。为了通过

可计算列来提升查询性能，您需要在创建索引时使用可计算列。

1.	 查询下压

如果可计算列没有被定义为维度，也没有被用来创建索引，那么该可计算列无法起到提升查询性能的作用。但是如

果您开启了查询下压选项，那么您仍可以在	SQL	中查询该可计算列。此时	Kyligence	Enterprise	会分析当前查询，
并将该可计算列翻译成相应的表达式并下压至计算引擎实现可计算列的查询。

比如，在模型中定义了可计算列	 	T_PRICE_PER_ITEM	，	其表达式为	 	LO_EXTENDEDPRICE	*	LO_QUANTITY	，然后执行如下
SQL	语句：

select	sum(T_PRICE_PER_ITEM)	from	SSB.P_LINEORDER

这条查询会先被翻译成如下	SQL	语句：

347

模型设计进阶

select	sum(LO_EXTENDEDPRICE	*	LO_QUANTITY)	from	SSB.P_LINEORDER

语句翻译完毕后再下压至计算引擎。

注意：	在查询可计算列时，定义可计算列模型中的	join	关系必须被包含在SQL中。

2.	 显式查询

使用可计算列的名称作为查询字段或者函数参数的查询称为可计算列的显式查询。例如：

select	sum(T_PRICE_PER_ITEM)	from	SSB.P_LINEORDER

3.	 隐式查询

使用可计算列的逻辑表达式作为查询字段或者函数参数的查询，称为可计算列的隐式查询。例如：

select	sum(LO_EXTENDEDPRICE	*	LO_QUANTITY)	from	SSB.P_LINEORDER

在	Kyligence	Enterprise	4.x	中，表达式	 	LO_EXTENDEDPRICE	*	LO_QUANTITY		会被转换成可计算列	 	T_PRICE_PER_ITEM	，
从而原始查询会被翻译成如下	SQL	语句：

select	sum(T_PRICE_PER_ITEM)	from	SSB.P_LINEORDER

当度量	 	sum(T_PRICE_PER_ITEM)		已经在某个聚合索引中被预计算，那么查询的性能将会得到极大的提升。

嵌套可计算列

可计算列的表达式可以嵌套其它可计算列。基于一个已有的可计算列创建新的可计算列称为可计算列的嵌套。	嵌套可计
算列的表达式规范与可计算列的表达式规范一致。

下面我们介绍创建嵌套可计算列	 	D_PRICE_PER_ITEM	=	2	*	T_PRICE_PER_ITEM	，其中	 	D_PRICE_PER_ITEM		表示嵌套可计算
列， 	T_PRICE_PER_ITEM		表示已经创建的可计算列，具体步骤如下：

第一步：在编辑模型页面定义一个可计算列	 	T_PRICE_PER_ITEM	，点击提交。

348

模型设计进阶

添加可计算列

第二步：定义一个新的可计算列	 	D_PRICE_PER_ITEM	，并在表达式中引用第一个可计算列，其表达式为	 	2	*
T_PRICE_PER_ITEM	。

349

模型设计进阶

引用可计算列

点击提交后产品会自动检验可计算列表达式的合法性，通过合法性校验后您可以在可计算列窗口中看到如上图所示的可

计算列信息。

创建嵌套可计算列时，请您确定输入的可计算列实际存在且名称正确，否则提交时会收到提示信息： 	Computed	Column

${Computed	Column	Name}	use	nonexistent	column(s):${Column	Name}	，您可以修改后重新提交。

高级函数的使用

由于可计算列的计算是直接下沉到数据源进行处理的，而	Kyligence	Enterprise	4.x	的下压查询引擎基于	Spark	SQL，因此
可计算列的表达式定义需要符合	Spark	SQL	的语法。

使用案例

有关可计算列函数的具体使用案例，请参考	Kyligence	官网的技术博客：

https://cn.kyligence.io/blog/kap-2-4-new-feature-computed-column/

350

模型设计进阶

已知限制

如果在智能模式项目中存在一个或以上包含可计算列的索引组，则该智能模式项目暂时无法连接	Kyligence	MDX。

在	Kyligence	Enterprise	4.0.11	版本中，连接	Kyligence	MDX	时，暂时无法在	AI	增强模式中通过查询下压查询可计
算列。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

351

模型设计进阶

缓慢变化维度

在多维分析场景中，维度表可能随着时间发生变动，比如产品表、客户表中的属性可能会不定期的发生变化，而这些属

性很可能是多维分析中需要使用的维度，这种情形下需要根据查询分析的特定需求对这种变化进行处理，业界称之为缓

慢变化维度（Slowly	Changing	Dimension,	SCD）的处理。详细介绍可以参照wikipedia。

一般来说，最为常见的缓慢变化维度的处理方法有类别	1	(Type	1)	和类别	2	(Type	2)：

类别	1：维度表中直接覆盖原值，查询时只能使用最新的维度属性，反应维度最新状态(As	Is)。
类别	2：维度表中添加新的记录，通常增加有效期字段来区分，记录维度表所有历史变化，从而使得历史可追溯。
在查询时一般使用当时的维度属性，反应历史事实(As	Was)。

对于类别	2	(Slowly	Changing	Dimension	2，后称	SCD2	)，仅支持基于拉链表(History	Table)的模型中，原理图如下:

SCD2模型

拉链表	(	History	Table	)

拉链表存储的是记录的基本信息以及每条记录的生命周期，对记录的变更会增加新的一行，并且修改历史记录的生命周

期。通过记录的生命周期，可以查询历史记录，也可以查询最新的记录。

例如下面SCD2_SALES表，该销售员在对应业务区	(	SALES_DPT	)	所处的时间区间为	[	START_DATE	,	END_DATE	)	。

SALES_PK

SALES_ID

SALES_NAME

SALES_DPT

START_DATE

END_DATE

1

2

3

4

1

2

3

1

张三

李四

王五

张三

南区

北区

东区

北区

1992/1/1

1992/1/1

1992/1/1

1993/1/1

1993/1/1

1994/1/2

1995/1/3

1994/1/1

352

模型设计进阶

5

6

7

2

3

1

李四

王五

张三

东区

南区

西区

1994/1/2

1995/1/3

1994/1/1

9999/1/1

9999/1/1

9999/1/1

从表中可以看出张三：

在1992年1月1日到1993年1月1日期间在南区工作，
在1993年1月1日到1994年1月1日期间在北区工作，
并且从1994年1月1日开始到目前都在西区工作。

张三每切换一次工作地点，就会增加新的一行记录，并且修改上一份记录的截止日期。

基于拉链表的连接条件

为了能够查询拉链表的历史信息，往往会使用事实表对拉链表记录的开始和结束日期进行过滤，即 	LO_ORDER	DATE	>=

START_DATE	AND	LO_ORDERDATE	<	END_DATE		如下图所示，

拉链表模型	连接条件

为了使用拉链表满足对缓慢维度的需求，您可以在导航栏	设置	->	高级设置	->	支持拉链表开启对支持拉链表的功能。如
下图所示，

353

模型设计进阶

支持拉链表开关

开启后，您将可以非等值的连接关系来建模和查询，包括三种非等值的关联关系对：

	>=		和	 	<
	>=		和	 	<=
	>		和	 	<=

关闭后，已有的SCD2模型将会被下线。
需要开启配置	 	kylin.model.non-equi-join-recommendation-enabled=true		才能支持针对拉链表的查询语句的推荐，该
配置可以项目级别生效，默认值为	 	false	，表示不开启。

目前基于拉链表的连接条件存在如下约束:

列的连接条件不可重复定义

列必须至少包含一个	=	的连接条件
两张表仅可使用同样的条件连接一次

现在还不支持在	Kyligence	MDX	和	Kyligence	Insight	中使用文档提及的包含非等值条件的连接关系的模型
默认情况下，即使使用	LEFT	JOIN	也需要完全匹配模型，才能使用包含拉链表的模型回答查询。

基于拉链表的SCD2模型

对于SCD2，可以通过基于拉链表的连接条件，达到历史可追溯的目的。

如下图所示，为了查询销售员在每个工作地点的销售总收入，将订单日期和工作时间区间关联。

354

模型设计进阶

拉链表模型

355

模型设计进阶

拉链表模型	连接条件

对于销售员张三而言，从1992年到目前不同地区的订单年收入数据均可查询，如下表所示：

D_YEAR

SALES_NAME

SALES_DPT

TOTAL_REVENUE

1992

1993

1994

1995

1996

1997

1998

张三

张三

张三

张三

张三

张三

张三

南区

北区

西区

西区

西区

西区

西区

3711706590

3882401031

3626302199

3733096229

3487903587

3725031606

2101112606

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

356

模型设计进阶

聚合索引

在所有基于预计算的	OLAP	引擎中，维度灾难是一个广为诟病的问题。在	v2.1	之前的版本中，Kyligence	Enterprise	试图
通过一些基本的技术解决这个问题，也确实在某些程度上减轻了问题的严重性。而在之后的实践中，我们发现这些基本

技术缺乏系统性的设计思维，也无法解决更多更普遍的问题。于是在	Kyligence	Enterprise	v2.1	及之后的版本中，我们重
新设计了聚合组的设计机制使得本产品能够更好的服务于所有索引的设计场景。

本节的主要内容如下：

背景介绍

Kyligence	Enterprise	通过预计算提高了查询的性能，而聚合索引组则包含了所有维度不同的组合，每一种组合即为一个
索引。随着维度数量的增加，索引的数量也会急剧增加。比如，一个有	3	种维度的聚合索引组里，总共包括	7	个索引。
如下图所示，当增加	1	个维度时，索引数目翻倍变成	15	个。即使	Kyligence	Enterprise	使用可扩展的计算框架（Spark）
和分布式的存储（HDFS）来计算和存储聚合索引组，当数据增长到原来的几倍后，聚合索引组仍然会增长到一个难以
接受的大小。

聚合索引组

为了缓解索引的构建压力，Kyligence	Enterprise	引入了一系列的高级设置，帮助您筛选出真正需要的索引。这些高级设
置包括聚合组（Aggregate	Group）、必需维度（Mandatory	Dimension）、层级维度（Hierarchy	Dimension）和联合维度
（Joint	Dimension）。

编辑聚合索引

点击左侧导航栏数据资产	->	模型进入模型列表页面，再点击指定模型名称以展开更多信息。您可以点击索引，再点击
索引总览标签下的	+	索引下的聚合组进入聚合索引编辑页面。您也可以从聚合组标签下的	+（添加聚合组）按钮进入页
面。并在下图所示的弹窗中编辑聚合索引，将维度和度量根据分析场景定义在不同的聚合组。

357

模型设计进阶

编辑聚合索引

步骤一：维度设置

初始界面是对聚合组—1的编辑界面。首先您需要进行维度设置，选择包含的维度，点击	+	添加或者右上角的编辑选择
聚合组—1需要包含的所有维度，您可以在如下图所示的弹窗左侧中通过选择或搜索列名的方式筛选包含的维度，并在
弹窗右侧对所选的列进行拖拽排序。您也可以点击文本识别批量选择聚合组—1需要包含的所有维度。Kyligence
Enterprise	会根据您选择的维度构建所有维度不同的组合，即为构建聚合索引。

维度设置

358

模型设计进阶

随后您可以在聚合组—1中设置必需维度、层级维度和联合维度，也可以使用文本识别批量添加所需维度。这三个设置
中的维度必须是已放入包含的维度中的维度。

维度设置

注意：由于层级维度和联合维度中可以包含多个维度组，当您使用文本识别添加维度时，每进行一次识别将自动

创建一个新的维度组。因此，若想修改已存在维度组中的维度，可以点击维度组右侧的	"-"	按钮先清空该维度
组，再重新进行文本识别并生成最新的维度组。

您可以按需添加聚合组，在编辑完毕所有聚合组后，点击左下角索引数旁按钮，在聚合组名称旁会显示对该聚合组预估

的索引数量，在页面左下角索引数旁会显示所有聚合组的索引数量，这可以帮助用户了解当前聚合索引组构建的复杂

度。

我们建议您将查询中常用的分组维度、过滤维度按照基数从大到小的方式选入聚合组，这将提升查询性能。例如您经常

按照供应商	ID	 	SUPPKEY		和商品	ID	 	PARTKEY		查询分析，您需要将维度	 	SUPPKEY		和维度	 	PARTKEY		添加到聚合组中，您
可以在	数据资产	->	数据源	界面了解相关列的基数，如果	 	SUPPKEY		的基数大于	 	PARTKEY		的基数，则建议您首先选择
	SUPPKEY		加入包含的维度。

由于在实际的业务场景中会添加的维度数量较多，我们对包含的维度和必需维度提供了一键清空功能。层级维度和联合

维度需分组清空，可以通过点击维度组右侧的"-"按钮一键清空该组的维度，当仅剩一个维度组时将无法直接清空，可先
点击"+"按钮先新增一个空维度组再进行清空操作。

步骤二：度量设置

在度量设置中，默认为全选模型中定义的所有度量。您可以根据分析场景，将所选维度对应的度量定义在聚合组中。聚

合索引仅包含选入聚合组内的度量。无论您是否在模型中手动添加度量，聚合组中都至少存在一个度量	 	COUNT_ALL	，它
表示	 	COUNT(*)	。

359

模型设计进阶

度量设置

下面我们会分别介绍各聚合组的实现原理和应用场景实例。

聚合组（Aggregate	Group）

用户根据自己关注的维度和度量组合，可以划分出自己关注的组合大类，这些大类在	Kyligence	Enterprise	里面被称为聚
合组。例如本章开始展示的聚合索引组，如果用户仅仅关注维度	AB	与度量	M1	的组合和维度	CD	与度量	M2	的组合，
那么该聚合索引组则可以被分化成两个聚合组，分别是聚合组	AB-M1	和聚合组	CD-M2。如下图所示，生成的索引数目
从	15	个缩减成了	7	个。

在单个聚合组中，您不需要将与选入的维度不相关的度量放入聚合组，这样做可以减少构建成本和存储空间。

360

模型设计进阶

聚合组

用户关心的聚合组之间可能包含相同的维度，例如聚合组	ABC	和聚合组	BCD	都包含维度	B	和维度	C。如果两个聚合组
包含的度量相同，那么这些聚合组之间会衍生出相同的索引，例如聚合组	ABC	会产生索引	BC，聚合组	BCD	也会产生
索引	BC。这些索引不会被重复生成，一个索引	BC	为两个聚合组所共有，如下图所示。

共有的聚合组

361

模型设计进阶

根据业务场景，您可以选择是否需要添加一个包含所有聚合组内已定义的维度和度量的索引。该索引可以回答跨聚合组

的查询，但是查询性能将有所下降，同时添加该索引将带来一定的存储与构建开销。您可以在设置	->	模型设置中点击+
（添加重写设置项），通过选择设置项	 	is-base-cuboid-always-valid		来定义。

有了聚合组用户就可以用粗粒度地对索引进行筛选，获取自己想要的维度和度量组合。

聚合组的应用实例

假设创建一个交易数据的聚合索引，它包含了以下一些维度：顾客	ID	 	buyer_id	、交易日期	 	cal_dt	、付款的方式
	pay_type	和买家所在的城市	 	city	。有时候，分析师需要通过分组聚合	 	city	、 	cal_dt		和	 	pay_type		来获知不同消费
方式在不同城市的应用情况。有时候，分析师需要通过聚合	 	city	、 	cal_dt		和	 	buyer_id		来查看顾客在不同城市的消
费行为。在上述的实例中，推荐建立两个聚合组，包含的维度和方式如下图所示：

聚合组	1	中包含的维度：	 	[cal_dt,	city,	pay_type]

聚合组	2	中包含的维度：	 	[cal_dt,	city,	buyer_id]

在不考虑其他干扰因素的情况下，这样的聚合组将节省不必要的	3	个索引： 	[pay_type,	buyer_id]	、 	[city,	pay_type,
buyer_id]		和	 	[cal_dt,	pay_type,	buyer_id]		，节省了存储资源和构建索引的执行时间。

案例1：

Select	cal_dt,	city,	pay_type,	count(*)	from	table

Group	by	cal_dt,	city,	pay_type

则它将击中索引	 	[cal_dt,	city,	pay_type]

案例2:

Select	cal_dt,	city,	buyer_id,	count(*)	from	table

Group	by	cal_dt,	city,	buyer_id

362

模型设计进阶

则它将击中索引	 	[cal_dt,	city,	buyer_id]

案例3：

如果有一条不常用的查询：

Select	pay_type,	buyer_id,	count(*)from	table

Group	by	pay_type,	buyer_id

则没有现成的索引会被击中。此时	Kyligence	Enterprise	会通过在线计算的方式，从现有的索引中计算出合适的结果。

必需维度（Mandatory	Dimension）

用户有时会对某一个或几个维度特别感兴趣，所有的查询请求中都存在	 	group	by		这个维度，那么这个维度就被称为必
需维度，只有包含此维度的索引会被生成。以本文中的聚合索引组为例，假设维度	A	是必要维度，那么生成的聚合索引
组则如下图所示，维度数目从	15	变为	8。

使用必要维度降维

363

模型设计进阶

降维之后的聚合索引组

必需维度的应用实例

假设一个交易数据的聚合索引，它具有很多普通的维度，如交易时间	 	order_dt	，交易的地点	 	location	，交易的商品
	product		和支付类型	 	pay_type		等。其中，交易时间就是一个被高频作为分组条件	 	group	by		的维度。如果将交易时
间	 	order_dt		设置为必要维度，包含的维度和组合方式如下图：

364

模型设计进阶

必要维度实例

层级维度	（Hierarchy	Dimension）

用户选择的维度中常常会出现具有层级关系的维度。例如对于国家（country）、省份（province）和城市（city）这三个
维度，从上而下来说国家／省份／城市之间分别是一对多的关系。也就是说，用户对于这三个维度的查询可以归类为以

下三类：

1.	 	group	by	country
2.	 	group	by	country,	province	（等同于	 	group	by	province	）
3.	 	group	by	country,	province,	city	（等同于	 	group	by	country,	city		或者	 	group	by	city	）

以本文开始所示的聚合索引组为例，假设维度	A	代表国家，维度	B	代表省份，维度	C	代表城市，那么	ABC	三个维度可
以被设置为层级维度，生成的聚合索引组如下图所示。例如，索引	 	[A,	C,	D]		=	索引	 	[A,	B,	C,	D]	，索引	 	[B,	D]		=
索引	 	[A,	B,	D]	，因而索引	 	[A,	C,	D]		和索引	 	[B,	D]		就不必重复存储。

365

模型设计进阶

层级维度

下图展示了	Kyligence	Enterprise	按照前文的方法将冗余的索引剪枝从而形成下图的聚合索引组结构，索引数目从	15	减
小到	7。

366

模型设计进阶

使用层级维度降维

层级维度的应用实例

假设一个交易数据的聚合索引，它具有很多普通的维度，像是交易的城市	 	city	，交易的省	 	province	，交易的国家
	country	，	和支付类型	 	pay_type	等。分析师可以通过按照交易城市、交易省份、交易国家和支付类型来聚合，获取不
同层级的地理位置消费者的支付偏好。在上述的实例中，建议在已有的聚合组中建立一组层级维度（国家	 	country	／
省	 	province	／城市	 	city	），包含的维度和组合方式如下图：

367

模型设计进阶

层级维度实例

聚合组中包含的维度： 	[country,	province,	city，pay_type]

层级维度：	 	[country,	province,	city]

案例1：

当分析师想从城市维度获取消费偏好时：

SELECT	city,	pay_type,	count(*)	FROM	table	GROUP	BY	city,	pay_type

则它将从索引	 	[country,	province,	city,	pay_type]		中获取数据。

案例2：

当分析师想从省级维度获取消费偏好时：

SELECT	province,	pay_type,	count(*)	FROM	table	GROUP	BY	province,	pay_type

则它将从索引	 	[country,	province,	pay_type]		中获取数据。

案例3：

当分析师想从国家维度获取消费偏好时：

368

模型设计进阶

SELECT	country,	pay_type,	count(*)	FROM	table	GROUP	BY	country,	pay_type

则它将从索引	 	[country,	pay_type]		中获取数据。

案例4：

如果分析师想获取不同粒度地理维度的聚合结果时：

SELECT	country,	city,	count(*)	FROM	table	GROUP	BY	country,city

则它将从索引	 	[country,	province,	city]		中获取数据。

联合维度（Joint	Dimension）

用户有时并不关心维度之间各种细节的组合方式，例如用户的查询语句中仅仅会出现	 	group	by	A,	B,	C	，而不会出现
	group	by	A,	B		或者	 	group	by	C		等等这些细化的维度组合。这一类问题就是联合维度所解决的问题。例如将维度	A、
B	和	C	定义为联合维度，Kyligence	Enterprise	就仅仅会构建索引	ABC，而索引	AB、BC、A	等索引都不会被生成。最终
的聚合索引组结果如下图所示，索引数目从15减少到	3。

联合维度

联合维度的应用实例

假设创建一个交易数据的聚合索引，它具有很多普通的维度，像是交易日期	 	cal_dt	，交易的城市	 	city	，顾客性别
	sex_id		和支付类型	 	pay_type		等。分析师常用的分析方法为通过按照交易时间、交易地点和顾客性别来聚合，获取不
同城市男女顾客间不同的消费偏好，例如同时聚合交易日期	 	cal_dt	、交易的城市	 	city		和顾客性别	 	sex_id		来分组。
在上述的实例中，推荐在已有的聚合组中建立一组联合维度，包含的维度和组合方式如下图所示：

369

模型设计进阶

聚合组中包含的维度： 	[cal_dt,	city,	sex_id，pay_type]

联合维度：	 	[cal_dt,	city,	sex_id]

案例1：

SELECT	cal_dt,	city,	sex_id,	count(*)	FROM	table	GROUP	BY	cal_dt,	city,	sex_id

则它将从索引	 	[cal_dt,	city,	sex_id]		中获取数据

案例2：

如果有一条不常用的查询：

SELECT	cal_dt,	city,	count(*)	FROM	table	GROUP	BY	cal_dt,	city

则没有现成的完全匹配的索引，Kyligence	Enterprise	会通过在线计算的方式，从现有的索引中计算出最终结果。

基数乘积

基数乘积：指联合维度中，各个维度字段基数的乘积，维度基数的数据来源于源数据表的采样结果，基数乘积用来表示

这个联合索引中维度的最大排列组合数(即这个索引的最大条数)。

基数乘积不会参与索引的创建过程，仅仅用来辅助创建聚合组的联合维度。一般情况，为了保障该联合维度中维度的查

询性能，一个联合维度的基数乘积不建议超过10万，特别情况(联合维度中的维度肯定在一起查询)可以不关注基数乘积
的值。

最大维度组合数

聚合组的使用很好得解决了索引数量爆炸问题，但为了达到优化效果用户需要对数据模型有一定了解，这对于初级用户

有一定使用难度。这一章将介绍一种简单的索引剪枝工具——最大维度组合数（MDC），最大维度组合数表示一个索
引能够包含的最大维度数。这个剪枝方法能够避免生成大的索引（包含维度数目过多的索引），从而减少构建索引的开

销。该剪枝方法适用的场景为大多数查询语句访问的维度不多于	N	的情况，这里的	N	是可以配置的最大维度组合数参
数。

注意：V4.1.0	版本及以上才提供该功能。

查询维度数的计算方法

370

模型设计进阶

接下来我们介绍计算查询中维度数的方法。查询的维度数，也就是查询对应索引中维度的数量，对于普通维度，一个维

度即算做1。对于联合维度组合和层级维度组，我们将同在一个联合维度组的维度当做一个整体，即为一个维度；同理
一个层级维度组也当做一个维度。而必要维度在查询维度计算中，不算做维度。如下例所示：

select	count(*)	from	table	group	by	column_mandatory,	column_joint1,	column_joint2,	column_hierarchy1,	column_h

ierarchy2,	column_normal

该查询涉及到一个必要维度，属于一个联合维度组的两个维度，属于一个层级维度组的两个维度及一个普通维度。根据

上述计算查询维度数的方法，该查询涉及的查询维度数为3个维度。

剪枝原理图

索引生成图

如上图所示，该图为一个维度为7时的索引生成图，为了方便理解剪枝功能，该生成图部分内容进行了省略。

当最大维度组合数设置为4时，包含多于4个维度的索引会被剪裁掉，如：ABCDEF,	ABCDEG,	ABCDE,	ABCDF	等。

当最大维度组合数设置为3时，包含多于3个维度的索引会被剪裁掉，如：ABCDEF,	ABCDEG,	ABCD,	ABCE	等。

考虑到索引构建过程中性能问题，如果您在模型设置中选择生成一个包含所有聚合组内已定义的维度和度量的索引，则

该索引不会被剪裁。同时根据上一节关于查询维度计算方法，当一个索引中含有必要维度，联合维度组和层级维度组

时，这两个维度组均算做一个维度，必要维度不算做维度。因此在使用自动剪枝功能时需要考虑到当含有以上维度组或

者必要维度时，索引的实际所含维度数。

设置最大维度组合数（MDC）

这一小节将介绍如何设置最大维度组合数。点击	+（添加聚合组），用户可以在编辑聚合索引页面设置全部聚合组级别
的最大维度组合数和单个聚合组级别的最大维度组合数，如下图所示。在输入框中输入正整数，并点击确定，即保存了

最大维度组合数设置。

注意：最大维度组合数设置在正式提交编辑聚合索引后才会生效。

371

模型设计进阶

最大维度组合数

全部聚合组级别的最大维度组合数作用于所有聚合组，单个聚合组级别的最大维度组合数只对单个聚合组生效。单个聚

合组级别的最大维度组合数的优先级高于全部聚合组级别的最大维度组合数。具体设置的规则如下：

1.	 若单个聚合组没有设置最大维度组合数，此聚合组的最大维度组合数将会被全部聚合组级别的最大维度组合数覆
盖。可以看到，设置全部聚合组级别的最大维度组合数为2后，聚合组的索引数量从32下降为19，总的索引数变为
20。除了一个包含所有聚合组内已定义的维度和度量的索引，包含多于2个维度的索引都被剪裁掉了。

全部聚合组级别的最大维度组合数

2.	 若单个聚合组设置了最大维度组合数，此聚合组的索引维度数只被此单个聚合组的最大维度组合数所限制。

372

模型设计进阶

单个聚合组级别的最大维度组合数

3.	 若全部聚合组级别的最大维度组合数留空，意味着用户关闭了全部聚合组级别的最大维度组合数设置。此时未单独
设置过最大维度组合数的聚合组生成的索引中维度数量不受限制。设置过单个聚合组级别的最大维度组合数的聚合

组不受影响。

注意事项

一方面该剪枝方法能够显著减少维度索引中包含的索引数目，另一方面一些需要访问许多维度的复杂查询则会命中较大

的索引，造成大量的在线计算，最终导致查询速度变慢。和其他的剪枝方法一样，该方法是一种数据模型的妥协和权

衡，要在存储空间和查询速度间进行取舍。当多数查询访问的维度数目不多时，该方法能起到显著的作用。

同时，根据实验室测试数据发现，当聚合组中维度数较大时，触发检测索引数时可能需要数分钟，在此期间页面可能会

出现卡顿现象，请您耐心等待。以下是实验室测试数据结果，请您根据实际场景进行参考：

1个聚合组，包含1000个维度，设置最大维度组合数为1时，检测平均耗时3.1分钟
1个聚合组，包含1500个维度，设置最大维度组合数为1时，检测平均耗时13.9分钟
3个聚合组，每个包含500个维度时，设置最大维度组合数为1，检测平均耗时3分钟

查看聚合索引

点击左侧导航栏	数据资产	->	模型进入模型列表页面，并点击指定模型名称，在索引->索引总览中即可查看聚合索引的
详情。

373

模型设计进阶

索引详情

索引列表中可以在搜索框输入索引	ID	或者索引内容筛选索引，索引内容包括索引中所包含的维度、度量和表中所包含
的列，索引内容为模糊筛选，索引	ID	为精确筛选。点击内容栏中的按钮可以查看索引详情，在	AI	增强模式下，自定义
明细索引可以进行查看详情、编辑和删除，其余索引只可以查看详情和删除。	索引列表顶部的模型数据范围表示索引中
已加载的数据的时间范围，如果是全量加载则显示全量加载。

支持批量删除索引，首先勾选待删除的索引，然后点击列表上方的删除按钮进行删除。

支持在无基础索引或是缺失某个基础索引的时候进行添加，点击	+	索引	即可在下拉框中添加基础索引。

索引列表字段说明：

Index	ID：索引	ID；

存储：索引的中预计算数据的存储大小；

使用次数：查询命中该索引的次数；

来源：系统推荐索引表示索引由系统推荐而来，自定义索引表示索引由用户自定义而来；

状态：索引的状态，分为四种：

未构建：尚未构建的索引，您可以点击构建索引按钮构建全部未构建的索引；

构建中：索引正在构建中，在任务监控界面有相应的构建任务正在执行；

在线：索引已经构建完毕，可以服务于查询；

锁定：由于修改了聚合组，即将被删除的索引可能处于锁定状态，依然可以服务于查询。

提示：当您修改聚合组并保存时，可能会刷新一些聚合索引。如对某个聚合组添加度量会刷新该聚合组

对应的所有聚合索引，在	Kyligence	Enterprise	中，对应的行为是删除原来的索引并添加新的索引。系统
为了保证您的服务可用，尤其是查询服务可用，在新的索引构建完成前会将原来的索引置于锁定状态，

您的查询依然可以由锁定状态的索引回答。当新的索引构建完成后，相应的锁定状态的索引将被删除，

此时，您的查询将由新的索引回答。

如果修改聚合组仅会导致部分索引被删除，则不会出现锁定状态的索引。索引被删除后无法恢复。

内容：索引内容。

操作：可对当前索引进行的操作，如构建。

374

模型设计进阶

点击内容中的图标，您可以看到每个索引的详细情况。对于聚合索引，顺序是维度在先，度量在后，维度显示为表.列，
对于明细索引，您将看到所添加进该索引的所有列、顺序和	shardby	列的情况。

聚合索引详情

详情页面字段说明：

最后更新时间：最近一次更新索引的时间。

内容：维度、度量或是表中的列、顺序、shardby	列。
类型：维度或度量。

基数：列的基数，由采样后获得。

Shard	By：该索引的	ShardBy	列。

高级设置

在	AI	增强模式的聚合索引中，您可以设置	ShardBy	列，数据将按照该列分片存储以提高查询效率。您可以将查询中常
用的过滤维度或分组维度按照基数从大到小设置为	ShardBy	列。目前仅支持设置一个	ShardBy	列。

注意：所有的自定义聚合索引都将使用同样的	ShardBy	列。

点击左侧导航栏数据资产	->	模型进入模型列表界面，再点击指定模型名称以展开模型的更多信息，您可以在索引-聚合
组标签下找到高级设置按钮。

在高级设置中，您可以选择需要被设置为	ShardBy	列的维度。

更新	ShardBy	列后会使所有包含	ShardBy	列的聚合索引失效并且重新构建索引，保存时勾选立即构建索引会触发新的索
引构建，如果不勾选可以后续通过点击构建索引按钮进行构建。

375

模型设计进阶

高级设置

ShardBy	列与	Join	优化

有时	join	两边的子查询可能分别匹配上两个索引，Kyligence	Enterprise	在计算时会从这两个索引中取出预计算的数据再
做	join	运算。当子查询返回结果的基数比较高的时候，join	的耗时也会相应变多，此时可以通过	ShardBy	列的配置来优
化这样的高基列	join	场景。

如果希望使用该功能，需要在	kylin.properties	中配置

kylin.storage.columnar.expose-sharding-trait=true

当	 	kylin.storage.columnar.expose-sharding-trait		开关开启时(默认开启)，Kyligence	Enterprise	会把	ShardBy	列的信息
暴露给执行引擎	Spark，由于	ShardBy	列设置在构建时已经对数据做了分片，所以在用	ShardBy	列作为	Join	条件执行
Join	时，可以节省掉原本在	Join	前对于数据的	Shuffle，以提升	Join	尤其是高基列	Join	的性能。

该功能当前存在以下限制

1.	 由于	ShardBy	列只能设置一个，所以只支持优化	Join	条件中有且只有该	ShardBy	列的	Join

使用案例

对于SQL

select	org_id,	cust_id,	sum1,	sum2

from	(

				select	org_id,	cust_id,	sum(....)	sum1

				from	fact

				where	dt	=	...

				group	by	org_id,	cust_id

)	T1

inner	join	(

				select	cust_id,	sum(...)	sum2

				from	fact

				where	dt	=	...

				group	by	cust_id

)	T2	on	T1.cust_id	=	T2.cust_id

376

模型设计进阶

可以通过分别构建两个聚合索引，然后	Join	两个聚合索引的结果进行查询。为了优化	Join	性能，我们可以对于索引对
应的模型设置	join	key	 	cust_id		为	 	ShardBy		列。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

377

模型设计进阶

明细索引

为了支持对明细数据进行高效的查询，产品提供了明细索引功能。您可以根据经常需要查询的明细字段，预定义和计算

像表一样的明细索引。对于不常用的明细查询，可以通过查询下压获得结果。

创建明细索引

在导航栏	数据资产	->	模型	界面，点击模型名称进入模型信息页，接着点击索引，在索引总览标签下点击+	索引->明细
索引进入添加明细索引的页面。您也可以通过明细索引标签下的+按钮（添加明细索引）进入页面。您可以在下图所示
的弹窗中编辑明细索引，同时您还可以设置顺序和	ShardBy	列。

添加明细索引

编辑明细索引

弹窗左侧可以看到指定模型中维度表和事实表中的所有被定义为维度或被度量引用列的名称以及字段类型。您也可以根

据需求点击列图标，选择列名按首字母升序或降序排列，或点击类型图标筛选字段类型。	您可以通过点击全选、点击所
需列、或直接在搜索框中搜索列名的方式选择需要添加至明细索引的列，也可以通过文本识别批量粘贴文本，并自动识

别选择列。弹窗左下角可以看见已选列数量及列的总数量。

排序明细索引中的列

随后您可在弹窗右侧看到明细索引中的已选择列。已选择的列默认按照基数降序排列，基数信息需要在采样后获得对应

数值。此外，您可以按照基数或者列调整排序规则，也可以通过拖拽排序的方式设置对应列的顺序。合理地设置明细索

引中列的顺序，可以显著提高明细索引的查询效率。	在明细索引中排序靠前的列，作为查询过滤条件时将获得更高的效

378

模型设计进阶

率。因此推荐您将各列按照实际情况下作为过滤条件的概率进行排序。

设置	ShardBy	列

将鼠标移至您想要设置为	ShardBy	的列，可以在右侧看到对应图标按钮，点击该按钮即可将此列设为	ShardBy，当图标
变为绿色时表示设置成功。如需替换	ShardBy	列，重复上述操作即可完成替换。	在设置明细索引时，用户可以选择	1	列
设置为	ShardBy	或不指定	ShardBy。如果用户指定了	ShardBy	的列，则明细数据将按照该列的值分片。如果用户没有指
定	ShardBy	的列，则默认将根据所有列中的数据进行分片。	选择适当的	ShardBy	列，可以使明细数据较为均匀的分散在
多个数据片上，提高并行性，进而获得更理想的查询效率。建议选择基数较大的列作为	ShardBy	列，以避免数据分散不
均匀。

您可以创建多个明细索引，在明细索引构建完毕之后，即可对相应数据进行明细查询。

查看明细索引

在导航栏数据资产	->	模型界面，点击模型名称，并点击索引，在索引总览的标签下，可查看明细索引详情。

点击状态旁的图标可以在明细索引详情中看到明细索引的列、顺序和	shardby	列详情。对于自定义明细索引，您可以点
击编辑按钮进行编辑，也可以点击删除按钮删除。对于系统推荐明细索引，您可以进行删除，但不能进行编辑。

支持在无基础索引或是缺失某个基础索引的时候进行添加，点击	+	索引	即可在下拉框中添加基础索引。

查看明细索引

索引列表更多的信息，如索引状态，请您查看聚合索引章节。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

379

模型设计进阶

模型高级设置

本章节将介绍应用于模型的高级设置。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

380

模型设计进阶

模型元数据管理

Kyligence	Enterprise	实例是无状态的服务，所有的状态信息都存储元数据中，模型是	Kyligence	Enterprise	集群的核心资
产，模型元数据是详细描述模型信息的内容。

模型在不同环境中的移动，是实际生产的重要过程，因此元数据的导入和导出是运维工作中一个至关重要的环节，

Kyligence	Enterprise	提供导入导出模型元数据功能。

模型发布

在很多企业中，为了保障生产环境的稳定性，对生产环境的模型发布和变更十分严格。客户往往需要额外部署一套独立

的开发环境用于数据开发和测试验证（可能还有一套测试环境），而把数据模型从开发环境迁移到生产环境就是模型发

布的过程。同时这一过程中需要经过严格的评审，要确保模型在迁移中的完整、准确，元数据的导出和导入就是迁移工

作中一个至关重要的环节。

模型元数据导出

导出内容

381

模型设计进阶

模型元数据导出，可以将指定的单个或多个模型导出	zip	格式压缩包。

导出的模型元数据范围是：

包含模型定义信息，如模型引用的表、表关系、分区列、可计算列、过滤条件、度量、维度、聚合组、索引内容

等。

不包含	Segment	信息、构建数据、索引状态等信息。

同时您可以选择是否包含优化建议、模型重写设置、多级分区模型子分区值。选中导出后，如果目标系统存在同名

模型，导入时将直接覆盖目标模型的优化建议、模型重写设置和多级分区模型子分区值。

特别说明

为了确保文件完整性，请勿解压文件或修改文件内容。文件名称后半部分为文件完整性校验码，如需修改文件名增

加识别度，请保持校验码不变。

导出操作

导出单个模型

点击左侧导航栏数据资产-》模型进入模型列表页面，通过单个模型的	...	(更多操作)	-	导出模型	，可以将指定的模
型以	zip	压缩包的格式导出。

导出多个模型

您可以在模型列表页面，点击	导出模型	按钮，选择模型，导出多个模型。
或者点击页面最上方状态栏右侧的系统管理按钮，在项目列表页面，在单个项目	操作	-	...(更多操作)	-	导出模
型，选择模型，导出多个模型。

382

模型设计进阶

模型元数据导入

导入操作

您可以在模型列表页面，点击	+模型	后面的下拉按钮，选择	导入模型，上传模型元数据压缩包。

383

模型设计进阶

或者进入系统管理页面，在项目列表页面，选择模型元数据要导入的项目，在	操作	-	...(更多操作)	-	导入模型，上
传模型元数据压缩包。

选择操作类型

解析元数据包，系统会以	模型名称	作为区分模型的唯一标识别，匹配目标系统与元数据包中的模型元数据。模型经系
统解析后会有三种操作可供选择：	覆盖、	新建、不导入，下面将详细介绍这三种操作默认出现、和是否可作为下一步
操作的条件：

注意：	如果系统数据源存在表，但是项目内未加载表，则会自动加载系统数据源表到项目中。同时可能会导致Broken状
态的模型恢复。

不导入

操作说明：系统无法导入模型，或者用户主动选择不继续导入此模型。

默认出现的条件：将要导入的模型，在目标系统数据源中找不到表、列，或者列的数据类型不一致。

是否可切换为其他操作：不可以。

覆盖

操作说明：目标系统中已存在同名模型，且模型不存在重大变化，系统推荐以元数据包中的模型，覆盖目标系

统中的同名模型。

其中模型不存在重大变化的标准为：

事实表和维表完全一致。

表关联关系完全一致，包括表连接条件、表关系、列连接条件。

分区列及格式完全一致，包括模型加载方式（全量与增量），不包括多级分区子分区值差异。

数据过滤条件变化完全一致。

默认出现的条件：目标系统中已存在同名模型，且模型不存在重大变化。

是否可切换为其他操作：可以切换为新建，或不导入。手动切换为新建时，请同时将模型名称改为目标系统中

不存在的名称，以免模型名称冲突。

注意：覆盖时可能会导致部分已构建数据的删除，导入前做好模型备份以及确认。

新建

384

模型设计进阶

操作说明：目标系统中不存在同名模型，并且将要导入的模型，在目标系统数据源中的表、列都存在，且列的

数据类型一致。或目标系统中存在同名模型，且模型存在重大变化。模型重大变化参考覆盖操作上述说明。

默认出现的条件：同操作说明的两种情况。

是否可切换为其他操作：可以切换为不导入。

选中将要导入的模型时，右侧会显示将要导入的模型，与当前项目中同名模型、数据源的差异。差异会分为四类：未找

到、增加、删除、更改显示。

模型导入后，可能需要对新增的索引进行构建，才可以服务于相关的查询。

一些实践指导

对优化建议的处理

Kyligence	智能推荐的原理是，根据系统的查询历史，使用机器学习来优化系统模型，所以通常生产环境的查询历史作
用于系统模型索引优化才有较高价值。如上述说明，在部分企业中对生产环境的变更控制十分严格，包括模型、索引的

优化，我们建议通过如下方式来兼顾两者：

在生产环境中开启智能推荐，将系统自动生成的优化建议，随模型一起导出并导入到测试环境，在测试环境中接受优化

建议，接受优化建议会带来维度、度量、索引等的增加或减少，对变更后的模型进行测试与评审完成后，再重新导出并

导入回生产环境。

对模型重写设置的处理

不同的环境中对模型重写设置可能有不同要求，您在导出模型时可以选择是否同时导出模型重写设置，之后在导入模型

时覆盖会覆盖目标系统的同名模型重写设置。

对多级分区子分区值的处理

不同的环境多级分区子分区值一般是不同的，对于开启支持多级分区功能的模型，您在导出模型时可以选择是否同时导

出多级分区子分区值，之后在导入模型时覆盖会覆盖目标系统的同名模型的多级分区子分区值。导入时被删除的子分区

值构建数据将被同时删除。

385

模型设计进阶

模型元数据导出和导入相关	API

您也可以通过	API	导出导入模型元数据，详细请参照：模型导入导出	API

已知限制

模型导入后无法撤销，请提前做好模型备份。

只支持在版本号前两位相同的版本间导出导入。如	Kyligence	Enterprise	4.2.x	版本导出的模型元数据包，不支持在
Kyligence	Enterprise	4.3.x	导入。

前两位相同的版本间模型导出导入时，存在少数情况，高版本导出的模型无法在低版本导入。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

386

模型设计进阶

多级分区(Beta)

什么是多级分区

Kyligence	Enterprise	多级分区指模型除了根据时间分区列进行分区管理，还可以根据子分区进行分区管理。

在一些分析场景中，除了根据日期或时间进行分区管理外，还在这基础上需要根据其他的维度，如地区、分行等，进行

分区管理，我们称之为子分区。例如，对于一些跨地区开展业务的用户，不同地区由于时差、业务结束时间等不同，数

据完成准备地时间也各不相同。用户可以将地区设置为子分区，当某一地区的数据在完成数据准备后，可以立即构建当

前地区的数据，构建完成即可服务于该分区的查询分析。由此减少了子分区间的互相依赖，数据构建和查询更加灵活。

Kyligence	Enterprise	多级分区目前只支持二级分区。

如何开启多级分区功能

您可以在模型	设置-高级设置-多级分区，开启或关闭支持多级分区。

设置多级分区

注意：	关闭模型多级分区时，使用了多级分区的模型将会自动下线。若需上线需要删除子分区后才可以上线或将此选项
开启。

387

模型设计进阶

关闭多级分区

设置模型子分区

开启支持多级分区后，您可以在数据资产-模型-	+模型创建模型，并在保存模型时选择添加子分区列，目前支持作为子
分区列的类型为	tinyint,smallint,int/integer,bigint,double,decimal,timestamp,date,varchar,char,boolean。

388

模型设计进阶

或者您也可以在模型列表-...(更多操作)-分区设置对子分区列进行调整。

管理模型子分区值

您也可以在模型列表-...(更多操作)-子分区值设置中对添加、删除或搜索子分区值。

添加子分区值时，系统不进行正确性校验，系统允许添加尚未存在的子分区值。查询时子分区值必须与此子分区值完全

一致才可以匹配（大小写敏感，不支持通配符匹配），请确保添加的子分区值符合您的预期。

构建子分区

构建新时间范围的	Segment	时，您可以点击模型列表-构建索引，并指定构建时的子分区值

389

模型设计进阶

当Segment已存在，但是该	Segment	下只有部分子分区已经构建时，您可以在模型列表页面，点击模型名称进入模型信
息页，再点击Segment	查看已构建子分区，或继续构建尚未构建的子分区

390

模型设计进阶

如果您需要合并	Segment	，需要保证子分区值一致。

子分区有三种状态，分别是：

ONLINE	：表示已经构建完成，可以服务于查询
LOADING：表示正在构建中
REFRESHING：表示正在刷新中，刷新中仍可服务于查询

多级分区下的查询行为

Kyligence	Enterpris	系统回答查询时，主要有以下规则：

Segment	时间范围定义了模型可以回答的时间范围。当查询指定未定义的时间范围时，此部分数据返回空。

Segment	子分区定义了模型可以回答的子分区值范围。如果查询指定了模型未定义过的子分区值，此部分数据返回
空。如果查询指定了包含时间范围下未构建的子分区，将使用查询下压。

索引在	Segment	中的时间范围和子分区值范围中，如果全部可以满足并服务于查询，则优先使用索引回答，如果无
法全部满足，则使用查询下压回答（开启查询下压的前提）。

下面介绍常见的案例帮助理解，假设模型中存在	4个	Segment，且所在项目已开启查询下压

Segment	1，时间范围是	[2015-2016)，构建的子分区为	Partition	1、Partition	2，包含索引	Index	A、Index	B
Segment	2，时间范围是	[2016-2017)，构建的子分区为	Partition	1、Partition	2、Partition	3，包含索引	Index	A、Index

C
Segment	3，时间范围是	[2017-2018)，构建的子分区为	Partition	1、Partition	2、Partition	4，包含索引	Index	A、Index
B、Index	C
Segment	4，时间范围是	[2018-2019)，不存在于系统中，为了方便理解，代号	Segment	4
Segment	5，时间范围是	[2019-2020)，保留	Segment，不包含子分区和索引

391

模型设计进阶

当有如下几种模式的查询时，系统将以这种方式回答查询：

Case	1:	查询不带任何时间分区条件

系统将回答所有	Segment	总时间范围的查询结果，此例中即	Segment	1、	Segment	2、	Segment	3、	Segment	5	的时间范围

Case	2：查询指定了特定的时间分区	[2015-2016)，但是未指定任何模型子分区值

系统将判断	Index	A	和	Index	B	是否可以回答查询，如何可以回答则由索引回答，否则由查询下压引擎回答

Case3：查询指定了特定的时间分区	[2015-2017)，同时指定了模型子分区值等于	Partition	1	、	Partition	2

系统将判断	Index	A	、	Index	B	、Index	C	是否可以回答查询，如何可以回答则由索引回答，否则由查询下压引擎回答

Case4	：查询指定了特定的时间分区	[2015-2016)，同时指定了模型子分区值等于	Partition	3

查询指定了	Segment	1	下未构建的	Partition	3，系统将需要通过查询下压引擎回答

Case5	：查询指定了特定的时间分区	[2015-2018)，同时指定了模型子分区值等于	Partition	5

Partition	5未在模型中定义，系统将返回	No	Data

Case6	：查询指定了特定的时间分区	[2015-2019)，同时指定了模型子分区值等于	Partition	1

此时查询中包含了未定义的时间范围[2018-2019)，此部分数据为空。仅根据	2015-2018	年范围内，Partition	1	范围内，
Index	A、Index	B、Index	C	是否可以回答查询，如何可以回答则由索引回答，否则由查询下压引擎回答。

Case7：查询指定了特定的时间分区	[2015-2020)，同时指定了模型子分区值等于	Partition	1

查询中包含了一个未构建任何索引数据的	Segment，可以判断出索引一定无法全部满足查询包含的时间范围，系统将通
过查询下压引擎回答。

已知限制

Kyligence	Enterprise	多级分区目前只支持二级分区。
合并	Segment	时，需要保证子分区值一致。
请尽量控制子分区值个数在	2000	个以内。如果分区值个数太多或平均长度太大，在提交构建任务或其他操作时，
可能会超过元数据库通信时数据包大小限制而报错。更多详细信息请参考下方	FAQ。

FAQ

392

模型设计进阶

Q:	因子分区值个数太多而出现	 	max_allowed_packet	、 	innodb_log_file_size		相关错误时，应该如何处理？

错误	1:

提示：界面上提示	 	MySQL	元数据库返回结果超过配置限制。请联系管理员在	MySQL	中将配置	“max_allowed_packet”	调整至	256M。	。

原因：元数据库	MySQL	默认配置	 	max_allowed_packet		值较小，此配置会限制	Kyligence	Enterprise	节点与元数据库通信
时数据包大小。当子分区值个数太多时，实际通信时数据包大小会超过此限制。更多内容请参考	MySQL	官方文档

解决：您可以调整	MySQL	配置为	 	max_allowed_packet=256M	来规避此问题。

错误	2:

提示：构建失败，kylin.log	日志中提示	 	The	size	of	BLOB/TEXT	data	inserted	in	one	transaction	is	greater	than	10%	of
redo	log	size.	Increase	the	redo	log	size	using	innodb_log_file_size

原因：单次事务写入到	mysql	redo	log	的数据量超过了	innodb_log_file_size	的	10%.

解决：参考	MySQL	官方文档	调大	 	innodb_log_file_size		配置项，需要重启	mysqld	服务，请谨慎操作。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

393

模型设计进阶

精确击中索引的查询优化

从	Kyligence	Enterprise	4.0.13	版本开始，系统增强了对精确击中索引的查询的优化（查询中包含维度刚好跟选中的索引
的维度一致），同时增强了该场景下查询精确去重的速度。

通过以下设置，即可启动对精确去重查询的优化:

1.	 构建一个模型，该模型包含精确去重度量

2.	 修改模型的配置，在设置界面对模型添加自定义设置:	 	kylin.query.fast-bitmap-enabled=true

3.	 构建该模型

4.	 使用精确击中索引语句查询

配置适用范围

该配置仅适用于模型级别

查询示例

以	Kyligence	Enterprise	的样例数据集	TPC-H	为例，事实表	LINEITEM	模拟了交易数据的记录。以下查询语句可以获得
不同销售日期下面的订单数量。

SELECT		COUNT(distinct	LINEITEM.L_ORDERKEY),

								LINEITEM.L_SHIPDATE

FROM	TPCH_FLAT_ORC_5.LINEITEM

JOIN	TPCH_FLAT_ORC_5.ORDERS

ON	TPCH_FLAT_ORC_5.LINEITEM.L_ORDERKEY	=	TPCH_FLAT_ORC_5.ORDERS.O_ORDERKEY

GROUP	BY		LINEITEM.L_SHIPDATE

1.	 创建模型:

394

模型设计进阶

创建模型

2.	 切换到模型设置界面：

395

模型设计进阶

3.	 输入配置开启该功能:

设置

4.	 添加索引:

396

模型设计进阶

5.	 构建完成后，查询精确匹配索引的	SQL	语句	，对比之前有明显提升:

优化前查询

397

模型设计进阶

优化后查询

1.	 优化前后执行计划对比

398

模型设计进阶

399

模型设计进阶

已知限制

1.	 该操作会导致构建时间变长，存储变大一倍左右

2.	 从没有开启到开启状态，需要重刷索引

3.	 当查询没有精确击中索引，或查询的时间范围跨过多个	Segment	时，无法使用开启参数后构建的索引回答，查询可

能下压。

上述例子中当存在	Segment	1(19920101～19921231)，Segment	2(19930101～19931231)，查询的时间范围为
19920101～19931231	时，无法使用索引回答查询；

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

400

模型设计进阶

整数类型跳过字典编码优化

从	Kyligence	Enterprise	4.0.13	版本开始，系统支持对整数类型不需要字典编码

通过以下设置，即可启动对精确去重查询的优化:

1.	 构建一个模型,该模型包含精确去重度量

2.	 修改模型的配置,在设置界面对模型添加自定义设置:	 	kylin.query.skip-encode-integer-enabled=true

3.	 构建该模型

配置适用范围

该配置仅适用于模型级别

注意事项

1.	 该操作能提高构建性能,如果数据散列严重可能导致膨胀率过高
2.	 该参数如果值变了需要重刷整个模型

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

401

模型设计进阶

预计算关联关系

预计算关联关系是指将模型中关联的表依据映射关系展开成一张平表，然后基于平表构建索引。默认情况下，Kyligence
Enterprise	会对每一个关联关系执行预计算并生成平表（包含维度、度量和可计算列所引用的列），本文介绍预计算关
联关系的原理及特性。

原理介绍

本文以事实表	Fact	与维度表	Dim	为例，介绍预计算关联关系对生成平表的影响，假设表的结构与数据如下：

Fact	表

Dim	表

1

2

3

1

1

2

3

col1

col2

col3

a

b

c

AAA

BBB

CCC

col1

col2

col3

A1

A2

B1

C1

AAAA

BBBB

CCCC

DDDD

如果将	Fact	表与	Dim	表执行内连接并且启用预计算关联关系，则生成的平表如下：

Fact.col1

Fact.col2

Fact.col3

Dim.col1

Dim.col2

Dim.col3

1

1

2

3

a

a

b

c

AAA

AAA

BBB

CCC

1

1

2

3

A1

A2

B1

C1

AAAA

BBBB

CCCC

DDDD

如果仅将	Fact	表与	Dim	表执行内连接，但不启用预计算关联关系，则生成的平表如下：

Fact.col1

Fact.col2

Fact.col3

1

2

3

[!NOTE]

a

b

c

AAA

BBB

CCC

此场景下，平表的生成不依赖维度表，维度表在构建的过程中会以快照的形式存储至	Kyligence	Enterprise。

特性对比

402

模型设计进阶

为平衡性能与成本，您可以在设计模型时，基于业务需求和数据特征选择是否开启预计算关联关系，详细对比如下：

查
询
性
能

较
好

构
建
时
长

较
长

存
储
开
销

较
大

新查询
场景适
应性

一般

一
般

较
短

较
小

较好

影响

●	维度表的所有列都可以设置为维度，也可以用于定义度量或
可计算列。
●	如果开启了	AI	增强引擎，可基于关联关系的主键及维度表生
成索引优化建议。

●	维度表的列不能被设置成维度，也不能用于定义度量或者可
计算列，即无法被索引引用。
●	查询会同时击中索引及相应的维表快照，然后通过实时关联
查询来得到结果。
●	如果开启了	AI	增强引擎，关联关系的主键不会被推荐成维
度，外键会代替主键生成索引。
当处于雪花模型时，如果外键对应的是维度表，且该表被设置
为屏蔽表或未开启预计算关联关系，那么不会生成相应的索
引。

是否启用
预计算关
联关系

是

否

常见问题

问：模型已经启用了预计算关联关系，如果将其关闭会有什么影响？

答：如果关闭预计算关联关系，Kyligence	将会自动删除相关的索引、维度、度量和可计算列，请谨慎操作。

问：当表关系为一对多或多对多时，开启预计算关联关系有什么注意事项？

答：由于该场景下衍生维度查询会被禁用，此时如果被关联表上的列没有被设置成维度，则无法生成索引，也无法

使用聚合索引或者明细索引加速查询。

问：某个列被设置为屏蔽列后，对预计算关联关系有什么影响？

答：即使开启了预计算关联关系，默认该列在添加索引时会被隐藏，除非手动打开"显示在优化建议中被屏蔽的
列"设置。

问：如何将某个列从屏蔽列中移除？

答：您可以在	Kyligence	Enterprise	的设置页面中，调整屏蔽列设置规则。

403

模型设计进阶

设置屏蔽列

问：屏蔽列和不启用预计算关联关系有什么区别？

答：主要区别如下：

类别

生效级别

应用场景

屏蔽列

项目级

通常用于始终需要查询最新数据的场景，在创建索引时，以关联关系中
对应的外键代替被屏蔽的列固化到索引中。

不启用预计算关联关系

模型级

通常用于降低存储成本、提升构建效率的场景，例如对一对多或多对多
的关联关系不启用预计算关联关系。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

404

模型设计进阶

逻辑视图（Logical	View）

逻辑视图是一个从	4.6.4	版本新引入的概念，是在	Kyligence	Enterprise	产品里维护的一种特殊的视图。创建完成
后，您可以像普通的	Hive	视图那样来使用它。
逻辑视图功能默认关闭，您可以设置	 	kylin.source.ddl.logical-view.enabled=true		以打开此功能
所有的逻辑视图都在同一数据库下，您可以通过如下参数设置它们所在的数据库名称，注意不能与普通的	Hive	库
重名：

	kylin.source.ddl.logical-view.database=KYLIN_LOGICAL_VIEW

逻辑视图功能推荐的浏览器版本为谷歌	Chrome	60	及以上。

主操作流程

1.	 登录	Kyligence	Enterprise，登录的账号需为：

系统管理员。

拥有目标项目的管理员或项目管理员角色。

拥有建模人员权限的用户。

2.	 点击数据资产->逻辑视图可以到逻辑视图的主页面，左侧可以输入	SQL	语句，右侧有三个分页，分别可以进行逻

辑视图表管理、数据源加载和显示语法规则。

主界面

3.	 在	SQL	输入框输入	 	Create	Logical	View	as	...		语句以创建逻辑视图，注意不要带数据库名。

4.	 创建完成后，需要加载源表后以供建模使用。由于新增了逻辑视图，需要先点击"立即刷新"以更新缓存，然后找到

新创建的逻辑视图，完成加载。

405

模型设计进阶

加载逻辑视图

删除逻辑视图

1.	 在逻辑视图的主页面，左侧可以输入	SQL	语句： 	DROP	LOGICAL	VIEW	logical_view_db.your_logical_view;		以删除逻

辑视图，注意必须带数据库名。

删除逻辑视图

查看/编辑逻辑视图

1.	 在逻辑视图的主界面，点击'逻辑视图表'（L）分页，可以看到所有创建的逻辑视图，本项目的会置顶，属于其他项

目的会置灰。

2.	 点击视图旁的铅笔图标以进行查看/编辑

406

模型设计进阶

进入编辑逻辑视图

3.	 在这个页面可以查看建表语句。

4.	 如需编辑表定义，可以点击	'create	->	replace'	图标。

407

模型设计进阶

编辑逻辑视图

5.	 可以看到编辑框中的	 	Create	Logical	View		被替换为了	 	Replace	Logical	View	，之后输入要修改的建表语句。如下

示例，添加了	 	where	1=1		的条件。

408

模型设计进阶

替换逻辑视图

6.	 点击保存，即完成了逻辑视图的编辑。

注意事项

1.	 逻辑视图必须统一创建在同一虚拟数据库下。（可以通过配置项确定数据库名称）
2.	 为避免用户借助逻辑视图超越已有的项目权限，在逻辑视图里用到的来源表需要已经加载到数据源，且用户仅能加

载/编辑同一项目下创建的逻辑视图。

3.	 从	Kyligence	Enterprise	4.6.19.0	版本开始，逻辑视图支持	RDBMS	JDBC	数据源，部分数据源可能需要定制化开发，

您可以联系	Kyligence	获取相关解决方案。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

409

加载数据

加载数据

按照模型和索引的定义，计算并存储数据的过程就是加载数据。本章以样例数据为例，介绍数据的三种加载方式和过

程：

本章节也会介绍	Segment	操作与设置，用于管理	Segment。

Segment	操作与设置
Segment	合并

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

410

全量加载

全量加载

当您希望加载源表中的所有数据时，您可以选择全量加载数据。本节主要内容如下：

AI	增强模式下的全量加载

AI	增强模式下，数据加载是在模型级别操作的。如果您没有为模型设置时间分区列，则每一次为该模型加载数据时都
会全量加载。全量加载的模型中只能有最多一个	Segment，因此后续不需要合并	Segment。

以下以样例数据集为例，介绍在	Web	UI	触发全量加载的方法：

1.	 在模型列表中选择需要全量加载数据的模型，点击构建索引按钮。

全量加载数据

2.	 系统将提示您为模型加载所有数据，包括模型中已经加载过的数据。

全量加载提示

411

全量加载

注意：如果您第一次为一个模型加载数据，上述提示中的存储大小会是	0.00	KB，因为该模型没有被加载过
数据，即模型中没有数据。

3.	 之后，可以在监控	->	任务页面查看触发的构建索引任务。

4.	 当数据加载完毕后，您可以在模型列表中查看详情，在	Segment	标签仅有一个	Segment	且被标注为全量加载。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

412

增量加载

增量加载

当您的业务数据随着时间增长时，您可以选择按日期	/	时间增量加载数据。本节主要内容如下：

AI	增强模式下增量加载数据

如果在某模型设置了时间分区列，则可以按日期	/	时间为该模型增量地加载数据。以下以样例数据集为例，介绍在	Web
UI	触发增量加载数据的方法。

1.	 初次加载	打开本产品的	Web	UI，并进入相应项目，在模型列表界面选择构建索引。

步骤一：点击构建索引按钮。

步骤二：选择构建范围，并点击增量构建按钮。该操作将触发增量加载的任务。

提示：

您可以点击时间范围右侧的按钮，该按钮会帮助您获取最新的可加载时间范围。鼠标悬浮于按钮上会显

示获取最新数据范围。

当您第一次加载历史数据且数据量很大时，可能会导致构建时间较长及资源利用较多等情况。请您根据

您的数据量，模型复杂度，可用资源等情况来选择加载范围。

413

增量加载

已知限制

Segment	的起始时间必须大于	 	1970-01-02	。

步骤三：在监控	->	任务界面可以看到对应的任务，且数据范围显示为步骤二中选择的范围。

步骤四：任务执行完毕回到模型信息界面，可以看到模型有一个	Segment，且该	Segment	的开始时间和结束时间与步骤
二中选择的时间一致。

1.	 增量加载

在初次加载数据完成并形成一个	Segment	之后，我们可以开始加载第二个	Segment	中的数据，从而实现不断地向模
型中增量加载新的数据，但需要保证	Segment	之间的时间区间不能有重叠。

提示：

当新加载	Segment	包含或等于已存在	Segment	，此时存在重叠。可通过打开配置	 	kylin.build.segment-
overlap-enabled		(模型级、项目级、系统级，默认关闭），来支持此类型的重叠。
新	Segment	构建过程中，被覆盖的	Segment	仍能支持查询。构建完成后，被覆盖的	Segment	将会被删
除。

此类型覆盖仅支持未开启分层存储的批模型且构建的	Segment	须包含所有索引。

增量加载的步骤与上面介绍的步骤一致。您可以在模型列表中找到模型，单击构建索引按钮，然后在弹窗中选择增

量构建的时间范围。为保障所加载数据的连续性，Kyligence	Enterprise	自动将新一次加载的起始时间更新为上次加
载的结束日期。

提示：通常情况下，按日期	/	时间的增量加载以周或天为单位，请根据您的数据更新频率和业务需求，合理
设置增量加载的时间周期。

待加载数据的任务执行完成，我们可以回到模型信息界面，可以看到此时模型有两个	Segment。

数据加载完毕

2.	 新增	Segment

414

增量加载

除了通过上述方式外，还可以通过直接添加	Segment	的方式，增加模型的服务区间。点击	Segment	列表下的	+
Segment	按钮，然后在弹窗中选择保存并构建索引。提交后将同样生成对应的构建任务，在构建任务完成后将会看
到第三个	Segment	。

注：如希望使用此功能，需先打开支持创建保留	Segment	开关，更多信息，见项目设置。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

415

构建索引

构建索引

随着业务场景的变更与演化，模型中的部分索引仅需要在最新的一段时间内保留，从而节省构建与存储成本。因此

Kyligence	在	4.2	版本之后提供了更加灵活的索引构建方式。

构建索引

在模型的索引总览页面下，我们可以看到模型中索引的组成和基本信息。在右侧的索引列表中，我们可以通过筛选部分

索引，仅构建索引至部分所需的	Segment	中。例如，由于业务变更，源表中新增部分字段用于分析。因此需要对模型新
增部分索引至最新一个月的	Segment，以减少构建成本。如下图所示，我们可以选择所有新增且未构建的索引，并点击
构建索引按键。

构建索引

然后选择最新一个月的	Segment，并点击构建索引按键生成对应的任务。如果您希望能够通过并发来提高构建效率，也
可以构建多个	Segment	数据时勾选拆分多个任务并发构建的勾选框，系统将自动地按照所选的	Segment	数量拆分多个任
务并发执行。

构建索引至指定	Segment

416

构建索引

删除索引

同样地，与构建索引相似。您也可以选择删除指定	Segment	中的部分索引来减少存储和构建开销。例如，仅删除过去一
年中，使用频率较低的索引来节省一些存储开销。如下图所示，我们可以在索引列表中点击删除按键来选择全部删除或

者从部分	Segment	中删除。

需要注意的是：如果删除了	Segment	中的索引，则可能会由于索引缺失而路由至查询引擎回答，此时可能会带来一定的
查询性能下降。

删除索引

快速补全索引

由于支持了更加灵活的索引构建能力，可以预期到不同的	Segment	中可能会有不同的索引。为了保障查询能够有比较稳
定的性能，我们还是推荐您在一段时间后尽可能将	Segment	中的索引补全。因此针对索引不完整时，我们可以通过点击
索引数据范围后的图标快速补全所有索引。

查看索引不完整的范围

417

构建索引

如下图所示，点击对应图标后将会展示出当前所有索引数不全的	Segment，此时您可以通过全选所有	Segment	后点击构
建索引快速补全。

补全索引

数据行数核对

若您需要调整或清理历史数据，而对	Hive	源表历史数据进行了修改，导致数据行数发生变化。此时您在已加载至
Kyligence	Enterprise	的时间范围构建新索引，会发生数据不一致现象，导致相关查询结果可能不一致。为了避免此现
象，我们提供了数据行数核对参数，您可以通过如下配置参数检查	Segment	中新构建索引与已有索引的数据行数是否一
致。

配置项

描述

kylin.build.data-count-check-enabled

是否开启索引数据行数核对功能，默认值	 	false	，表示不开启。

当您开启数据行数核对功能，触发构建索引任务后，我们将会在新索引要构建至的每个	Segment	中分别核对新构建索引
和已有索引的数据行数。若新构建索引与已有索引数据行数不一致，将跳过在不一致的	Segment	中构建新索引，在其余
数据行数一致的	Segment	中将正常构建新索引。

数据行数核对

如果您希望新索引能构建至数据不一致的	Segment	中，您可以刷新整个	Segment	以更新所有索引的数据，或恢复	Hive
源表历史数据后重新构建。如允许数据在同一	Segment	的不同索引间不一致，则可以关闭数据核对功能（不推荐）。

注意事项：

若	Hive	历史数据内容有过更新，但行数未发生变化，本参数无法进行有效检测

418

构建索引

开启该功能可能会延长索引补数的构建任务时间

暂不支持在二级分区中进行数据行数核对

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

419

数据完整性

索引数据完整性

若您在查询时希望	Kyligence	Enterprise	使用模型中的索引回答查询，则需要确保使用的索引在查询的全部时间范围内均
完成构建，否则将导致查询下压（若已开启查询下压功能）或查询报错。为尽量避免因索引未完整构建而影响查询性

能，我们将在本节为您介绍	Kyligence	Enterprise	中基于索引数据完整性的默认查询规则。

索引数据完整性的默认行为

为使构建索引更加灵活地适应多变的业务场景，并节约构建和存储成本，Kyligence	Enterprise	从	4.2	版本开始允许索引
只在部分	Segment	中构建，这也同时带来了潜在的索引数据不完整问题，在部分场景可能影响查询性能。为了保证查询
性能，需要确保查询要击中的索引在查询的时间范围内对应的全部	Segment	中构建完整，否则查询将下压或报错。索引
数据不完整包括：

仅	Segment	不完整：可能因您构建索引时选择的	Segment	的时间区间不连续导致。
仅索引不完整：可能在您后续新增索引时，仅将指定索引构建到部分Segment导致。
Segment	和索引都不完整：即上述两种情况均存在。

因此，当您的模型中存在索引数据不完整的情况时，建议在查询前按需补齐不完整的索引及	Segment，再进行查询。

为了帮助您更好地理解	Kyligence	Enterprise	中的默认查询规则以及索引数据完整性的概念，下面将用图示举例。

如图，您可以将下图中的每行理解为一段连续时间范围构建的	Segment；每列理解为一个索引；行和列交叉且有填充的
单元格代表在对应	Segment	中构建完成的索引；无填充的空白格代表索引未在	Segment	中构建；虚线部分表示尚未在
Kyligence	Enterprise	中添加该时间区间对应的	Segment。

提示：若	Segment	中没有已构建完成的索引，则为一个空	Segment，也是保留	Segment，下图中的	Segment	3	即为
一个保留	Segment。保留	segment	的设置方法和具体操作请参考	Segment	设置	和	Segment	操作	小节。

Segment	和索引情况

对应的查询结果

查询的
时间范
围

2000-
2001

2000-

对应的	Segment

SQL	1（预期击
中	Index	A）

SQL	2（预期击
中	Index	B）

SQL	3（预期击
中	Index	C）

Segment	1

命中索引

命中索引

查询下压

420

数据完整性

2000-
2002

2000-

2003

2003-
2004

2003-
2005

2000-
2005

不加时
间范围

Segment	1+2

命中索引

查询下压

查询下压

Segment	1+2+3

查询下压

查询下压

查询下压

无对应	Segment

命中索引（查询
结果为空）

命中索引（查询
结果为空）

命中索引（查询
结果为空）

Segment	5（存在未添加	Segment
的时间范围）

Segment	1+2+3+5（存在未添加
Segment	的时间范围）

命中索引

查询下压

查询下压

查询下压

查询下压

查询下压

查询下压

查询下压

查询下压

可见，	Kyligence	Enterprise	判断查询可以命中模型的原则是，查询击中的所有	Segment	中，都存在同一条构建完的索
引，且这条索引的维度和度量可以满足查询，就能成功击中模型。

若未开启查询下压开关，上表中的	“查询下压”	替换为	“查询报错”。

接受索引数据不完整的查询规则

Kyligence	Enterprise	从	4.6.9.0	开始提供配置参数	 	kylin.query.index-match-rules=use-vacant-indexes	。该参数支持使用
部分已构建完成的索引数据来回答查询，无需再补全索引至所有	Segment，可在系统级和项目级生
效。 	kylin.query.index-match-rules		默认值为空，为原有查询行为，即遵循索引数据完整性。

当有新增分析场景，对应着需要新增索引，新索引在已存在的	Segment	中补数需要一定时间，补数期间业务急需用数，
且用户可能更关注查询性能，而可以接受数据尚不完整；或者当业务模式有变更，部分索引无需在过去很久的时间区间

补数，而查询又会因为索引数据不完整而无法通过索引回答。当您遇到以上业务场景，可以选择升级至	Kyligence
Enterprise	4.6.9	及以后版本，并配置该参数，帮助您根据使用场景自行控制查询行为。

当您选择开启该参数，系统依然会以索引数据完整性为第一优先级，即优先选择可以回答查询的索引中，索引数据范围

与查询时间范围最完整匹配的，若可回答的索引未在任意一个	Segment	中构建，或系统中尚未添加	Segment，则查询返
回空结果。若尚未添加可以回答查询的索引，会保持原有行为，查询下压或者报错。需注意的是，开启该参数后的查询

结果可能与查询底层数据源不一致。

开启该参数后，查询行为将发生变化，查询结果举例如下：

421

数据完整性

Segment	和索引情况

开启参数后	vs.	不开启参数，对于同一条	SQL	1（预期击中	Index	A）对应的查询结果如下：

查询
的时
间范
围

2000-
2001

2000-
2002

2000-
2003

2002-
2003

2003-
2004

2003-
2005

2000-
2005

不加
时间
范围

对应的	Segment

接受索引数据不完整性的查询规则（参
数 	kylin.query.index-match-rules=use-
vacant-indexes	）

基于索引数据完整性的查询规则
（默认 	kylin.query.index-
match-rules		为空）

Segment	1

命中索引（返回	Segment	1	的数据）

命中索引（返回	Segment	1	的数
据）

Segment	1+2

Segment	1+2+3

命中索引（返回	Segment	1	和	2	的数
据）

命中索引（返回	Segment	1	和	2
的数据）

命中索引（返回	Segment	1	和	2	的数
据）

查询下压

Segment	3

命中索引（查询结果为空）

查询下压

无对应	Segment

命中索引（查询结果为空）

命中索引（查询结果为空）

Segment	5（存在未添
加	Segment	的时间范
围）

Segment
1+2+3+5（存在未添
加	Segment	的时间范
围）

命中索引（返回	Segment	5	的数据）

命中索引（返回	Segment	5	的数
据）

命中索引（返回	Segment	1，2	和	5	的数
据）

查询下压

命中索引（返回	Segment	1，2	和	5	的数
据）

查询下压

已知限制

开启分层存储且当索引数据不完整时，无法选择分层存储回答查询。

当您开启了分层存储，查询击中基础明细索引，若分层存储中的数据完整（索引数据范围可以完整覆盖查询时间范

围），则通过分层存储回答，若分层存储中的数据不完整（索引数据范围小于查询时间范围），则通过	HDFS	中的基础
明细索引回答，也就是说，在这种情况下，即使分层存储中的数据比	HDFS	中的数据更完整，也无法回答查询。

422

数据完整性

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

423

Segment	操作与设置

Segment	操作与设置

Segment	是模型（索引组）经过数据加载后形成的数据块。Segment	的生成以分区列为依据。对于有分区列的模型（索
引组），可以拥有一个或多个	Segment，对于没有分区列的模型（索引组），只能拥有一个	Segment。

查看	Segment

在导航栏	数据资产	->	模型	界面，您可以在指定模型的	Segment	标签下查看	Segment	详情列表。

Segment	列表

Segment	列表的字段介绍：

开始时间：Segment	中加载数据的开始时间。如果为全量加载则显示"全量加载“。

结束时间：Segment	中加载数据的结束时间。如果为全量加载则显示"全量加载“。

索引数：Segment	中包含的索引数/模型索引总数。

状态：Segment	状态。您可以在本文	Segment	状态查看具体介绍。

最后更新时间：Segment	的最后更新时间。

行数：Segment	中数据的行数。

存储大小：Segment	中数据的存储大小。

提示：当开启分层存储时，会展示加载到分层存储中的数据的存储大小。

操作：对指定	Segment	的操作，目前仅支持查看详情。

Segment	状态

您可以在	Segment	列表中查看	Segment	的状态。Segment	有以下	6	种状态：

ONLINE（在线）：Segment	可以通过已经加载数据的索引或查询下压，服务于查询分析。
WARNING	（警告）：Segment	中的数据已经加载完毕并且可以提供于查询分析，但是对应的源表数据可能发生变
更，因此存在数据不一致的风险，我们建议您重刷该	Segment	下所有索引数据。
LOCKED（锁定）：正在被刷新或被合并的	Segment	将处于锁定状态下。
LOADING（加载中）：正在加载该	Segment	对应的数据。
REFRESHING（刷新中）：刷新指定	Segment	时自动生成新的	Segment，这个新的	Segment	处于刷新中。当刷新
完毕，将自动删除旧的	Segment。
MERGING（合并中）：合并指定	Segment	时自动生成新的	Segment，这个新的	Segment	处于合并中。当合并完
毕，将自动删除旧的	Segment。

424

Segment	操作与设置

Segment	操作

进入导航栏	数据资产	->	模型	界面，共有以下	6	类对	Segment	的操作：

+	Segment：添加	Segment	来为模型定义可服务查询的数据范围。在范围内的查询将通过索引或下压回答，超出范
围的查询结果为空。该按钮位于	Segment	列表上方。

注意：	需要在	设置	->	基本设置	->	Segment	设置	中，开启	支持创建保留	Segment，才会出现	+	Segment	操
作按钮。

查看详情：查看指定模型的指定	Segment	的详情。该按钮位于	Segment	列表最右侧。您可以查看存储空间、
Segment	的时间范围等详细信息。

刷新：刷新指定模型的指定	Segment	中的数据。该操作支持批量刷新，刷新按钮位于	Segment	列表上方。

注意：只能刷新在线状态（ONLINE）和警告状态（WARNING）下的	Segment。

合并：选择指定的	Segment	并合并为一个	Segment。合并按钮位于	Segment	列表上方。

注意：只能合并在线状态（ONLINE）和警告状态（WARNING）下的	Segment。

删除：删除指定模型的指定	Segment。该操作支持批量删除，删除按钮位于	Segment	列表上方。

修复：补全模型下不连续的	Segment，该操作当且仅当模型中的	Segment	出现空洞时出现在	Segment	列表上方。

Segment	设置

您可以在导航栏	设置	->	Segment	设置	模块设置合并	Segment	，留存阈值等参数。具体配置方法请参考	项目配置。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

425

Segment	操作与设置

Segment	合并

在增量构建模式下，Segment	数量越多，运行时可能需要聚合多个	Segment	才能完成查询，导致查询性能下降。同时大
量的小文件会给	HDFS	Namenode	带来压力，影响	HDFS	性能。Kyligence	Enterprise	提供了一种机制来控制	Segment	数
量-	Segment	合并	。

手动合并

您可以在	Web	GUI	界面或使用	Segment	管理	API，将多个	Segment	合并。

在	Web	GUI

1.	 在数据资产	->	模型	->	Segment	列表，选择需要合并的	Segments
2.	 在下拉列表点击“合并”，检查满足	3	个条件（包含的索引一致、子分区值一致、时间范围连续）后，提交合并任
务。	系统会提交一个类型为“合并数据”的任务。在任务完成前，原有	Segment	仍然可用。任务完成后，被新的
Segment	替代。为节省系统资源，原有	Segment	将被回收和清理。

自动合并

合并	Segment	非常简单，但是需要不定期手动触发合并，当生产环境中有多个项目、模型时，逐个触发合并的操作会变
得十分繁琐，因此	Kyligence	Enterprise	提供了Segment	自动合并方案。

自动合并设置

自动合并策略

挑选	Segment
尝试合并

注意事项

自动合并设置

根据业务需要，支持对项目、模型分别设置自动合并。如果二者合并策略不同，系统采用模型级设置。

项目级：适用于一个项目有相同的合并策略。

模型级：用于一个项目下，不同模型的自动合并策略不同。

具体配置方法请参考	项目配置	的	Segment	设置和重写模型设置。

自动合并策略

合并时机：每当项目中有新的	Segment	状态变为完成时，系统会触发一次自动合并的尝试
时间阈值：允许用户设置最多	6	层的时间阈值，层级越大，时间阈值越大。用户可选择多个层级（如周、月）。	注
意：天、周、月分别表示自然天、自然周、自然月。

层级

时间阈值

1

2

3

4

5

6

小时

天

周

月

季度

年

426

Segment	操作与设置

挑选	Segment

触发自动合并时，系统尝试从层级最大的时间阈值，跳过时间长度大于等于阈值的	Segment，挑选其余符合条件的
Segment（包含的索引一致、子分区值一致，时间范围连续）

尝试合并

当	Segment	加起来时间长度达到阈值就合并，待合并任务完成后，系统会再次触发一次自动合并的尝试；否则系统会使
用下一个层级的时间阈值，重复此寻找过程。直到所有选定的层级都没有满足条件的	Segment，停止尝试。

注意事项

周的自动合并受月约束，即一个周如果跨月/季度/年，则分别合并（见例2）。
合并	Segment	过程中	HDFS	存储空间可能超过阈值限制，导致合并失败。

自动合并举例

例1
例2

例1

已开启自动合并，指定时间阈值为	周、月。现有	A~F	六个连续的	Segment。

Segment（初始）

时间范围

时间长度

A

B

C

D

E

F

2022-01-01	~	2022-01-31

2022-02-01	~	2022-02-06

2022-02-07	~	2022-02-13

2022-02-14	~	2022-02-20

2022-02-21	~2022-02-25

2022-02-26	周六

1	个月

1	周

1	周

1	周

5	天

1	天

随后新增	Segment	G	(2022-02-27	周日)	。

现在有A~G	7	个	Segment	存在，系统首先尝试按月合并，由于	Segment	A	时间长度大于等于阈值（1	个月），它会
被排除。接下来的	B-G加起来少于	1	个月未达到阈值（	1	个月）,因此不满足按月合并。
系统会尝试下一层级的时间阈值，即按周合并。系统重新扫描所有	Segment,	发现	A、	B、C和D	时间长度均大于等
于阈值（1	周），因此会跳过它们。接下来的	E-G	加起来达到	阈值（1	周），合并为	Segment	X.
随着	X	加入，会触发系统按照重新开始合并尝试，但是因为已经没有满足自动合并的条件，尝试终止。

Segment（增加	G，触发合并）

时间范围

时间长度

A

B

C

D

X（原E-G）

此时新增	Segment	H(	2022-02-28）

2022-01-01	~	2022-01-31

1	个月

2022-02-01	~	2022-02-06

2022-02-07	~	2022-02-13

2022-02-14	~	2022-02-20

2022-02-21	~	2022-02-27

1	周

1	周

1	周

1	周

427

Segment	操作与设置

触发系统尝试按月合并，除	A	以外的所有	Segment	加起来达到阈值（1	个月），	B-H	合并为	Segment	Y。
随着	Y	加入，	会触发系统合并尝试，但已经没有满足自动合并的条件，尝试终止。

Segment（增加	H，触发合并）

时间范围

时间长度

A

Y	（原B-H）

例2

2022-01-01	~	2022-01-31

2022-02-01	~	2022-02-28

1	个月

1	个月

现有	A~F	六个连续的	Segment，它们的时间长度均为	1	天，此时开启自动合并，指定时间阈值为周。

Segment（初始）

时间范围

A

B

C

D

E

F

周一	2021-12-27

周二	2021-12-28

周三	2021-12-29

周四	2021-12-30

周五	2021-12-31

周六	2022-01-01

随后新增	Segment	G（周日	2022-01-02），时间长度	1	天。

此时有	7	个连续的Segment，形成一个跨年的自然周。系统尝试按周合并，A-E	合并为新的	Segment	X。

Segment（增加	G，触发第一次合并）

时间范围

X（原A-E）

周一至周五（2021-12-27	~	2021-12-31）

F

G

周六	2022-01-01

周日	2022-01-02

随着	X	加入，会触发系统按周合并，F-G	合并为新的	Segment	Y。

Segment（增加	X，触发第二次合并）

时间范围

X（原A-E）

Y（原	F-G）

周一至周五（2021-01-27	~	2021-01-31）

周六至周日（2022-02-01	~	2022-02-02）

随着	Y	加入，再次触发系统按周合并的尝试，已经没有时间长度达到	1	周（不跨年）的	Segment，尝试终止。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

428

任务监控

任务监控

Kyligence	Enterprise	4.x	起引入了任务监控模块，您可以在任务列表查看相关信息并执行操作。

任务的构建发生在您使用	Kyligence	Enterprise	的过程中，如构建索引、刷新源表数据等都会触发不同的任务。

为了让您更清晰地了解不同任务的触发方法，阅读本章之前，我们建议您先阅读以下章节：

数据源

SQL	查询
模型（索引组）

快照管理

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

429

概念和基本设置

任务概念和设置

您在使用	Kyligence	Enterprise	的过程中会构建不同的任务。本节我们为您介绍任务的类型和设置，主要内容如下：

任务类型

Kyligence	Enterprise	目前有以下种类任务：

构建索引：新建索引的任务。

加载数据：对已有模型	/	索引的增量加载数据的任务。
合并数据：合并	Segment	的任务。
刷新数据：刷新	Segment	的任务。
抽样表数据：对源表数据进行数据抽样的任务。

构建快照：新建快照的任务。

刷新快照：刷新快照的任务。

加载子分区数据：多级分区模型，加载子分区数据的任务。

刷新子分区数据：多级分区模型，刷新子分区数据的任务。

加载数据到分层存储：对已有模型加载数据至分层存储的任务。

删除分层存储	-	项目：删除已加载至分层存储中项目数据的任务。
删除分层存储	-	模型：删除已加载至分层存储中模型数据的任务。
删除分层存储	-	Segment：删除已加载至分层存储中的	Segment	数据的任务。
删除分层存储	-	索引：删除已加载至分层存储中的基础明细索引数据的任务。
加载内表	-	加载数据到内表的任务。

如下图所示，您可以在导航栏	监控	->	任务	中查看任务，我们已经创建了不同类型的任务：

任务列表

1.	 构建索引：新建索引并加载索引内数据的任务。

AI	增强模式中在导航栏	数据资产	->	模型	构建模型的索引时会触发该任务。

提示：构建索引的详细方法请您查看聚合索引。

2.	 加载数据：对已有模型	/	索引的增量加载数据的任务。

注意：加载数据的开始时间必须大于已经加载的数据的结束时间。

AI	增强模式中在导航栏	数据资产	->	模型	加载指定模型中指定时间范围内的数据会触发该任务。

3.	 合并数据：系统在检测到足够数量的	Segment	时，将自动触发合并数据的任务。您可以在导航栏	设置	->	Segment

设置	模块设置合并	Segment	的参数。详细方法您可以参考	Segment	操作与设置。

4.	 刷新数据：刷新	Segment	的任务。

430

概念和基本设置

AI	增强模式中在导航栏	数据资产	->	模型	刷新指定模型中指定	Segment	的数据会触发该任务。

注意：如果你同时刷新	n	个	Segment，则会触发	n	个刷新数据的任务，且按照原有	Segment	的时间顺序
排列在任务队列中，您可以在	监控	->	任务	界面的任务中查看。

5.	 抽样表数据：对源表数据进行数据抽样的任务。该任务可以获得源表数据特征。抽样表数据任务可以自动触发或手

动触发。

自动触发：当您在导航栏	数据资产	->	数据源	添加数据源时会自动触发该任务。

提示：数据抽样为默认开启选项，如果您手动关闭数据抽样，则任务不会被触发。

手动触发：您可以在导航栏	数据资产	->	数据源	对指定源表进行数据抽样任务，点击右上方抽样或重载即可触
发该任务。

提示：重载选项会重新加载源表元数据。

6.	 构建快照：新建快照的任务。仅在开启快照管理之后，手动添加快照时才会出现。

7.	 刷新快照：刷新快照的任务。仅在开启快照管理之后，手动刷新快照时才会出现。
8.	 加载子分区数据：开启多级分区，且模型为多级分区模型，加载子分区数据的任务。
9.	 刷新子分区数据：开启多级分区，且模型为多级分区模型，刷新子分区数据的任务。

任务详情

您可以在导航栏	监控	->	任务	中，点击左侧三角按钮展开并查看任务详情，其中一些要素包括任务步骤、等待时间和持
续时间、日志详情和任务参数等：

1.	 任务步骤：	根据每种任务类型，对任务进行一级和二级任务步骤细分，便于用户更好地了解任务执行情况。	以构

建索引和加载数据类型任务为例，一级任务步骤有：

检测资源

加载数据到索引

更新元数据

加载	Gluten	缓存

其中加载数据到索引步骤又细分为二级任务步骤：

等待	yarn	资源
构建或刷新快照

物化事实表视图

生成全局字典

生成平表

获取平表统计信息

分层构建索引

更新平表统计信息

注意：

任务可能会根据实际情况，只执行上述其中部分步骤。

使用参数	 	kylin.index.preloaded-cache.enabled		控制是否开启加载	Gluten	缓存步骤。参数默认值为	true	，表
示开启加载	Gluten	缓存步骤。

2.	 等待时间和持续时间：

任务等待时间为，因并发度限制或资源限制等产生的等待时间。

任务持续时间为任务实际执行时间，不包括任务暂停时间。

3.	 日志详情： 	kylin.log		中任务相关日志，可辅助进行任务异常诊断。

4.	 任务参数：任务相关的	Spark	参数，可辅助任务异常诊断。

431

概念和基本设置

提示：细分的二级任务步骤、任务参数，从	Kyligence	Enterprise	4.5.3	版本开始引入。

任务设置

您可以在导航栏的	设置	界面中的	高级设置	设置	邮件提醒	的相关信息，如下图所示

任务设置

您可以填写您的邮箱，并选择开启不同类型的任务提醒。

提示：您可以对不同的项目进行不同的任务提醒设置。

FAQ

Q：为什么我的任务没有报错却被暂停了？

我们根据不同类型的任务对实际业务的影响程度，设置了任务的优先级，分类如下：

优先任务：加载数据；

次级任务：构建索引、合并数据、刷新数据；

当您某个模型	/	索引组的次级任务报错时，这个模型	/	索引组的其他同级别任务会被暂停。但不同模型	/	索引组的次级
任务不会被影响。

Q：为什么我之前完成的任务从任务列表消失了？

Kyligence	Enterprise	界面中最多保留	30	天的任务记录，超过	30	天的任务记录您可以在安装包部署文件中查询。

Q：Kyligence	Enterprise	有没有任务并发数限制？如果提交任务时，超出了系统允许的并发数怎么办？

Kyligence	Enterprise	默认根据您可用的系统资源自动控制任务并发数量，您可以修改系统配置文件	 	kylin.properties
中的参数	 	kylin.job.auto-set-concurrent-jobs		来关闭自动控制。

关闭自动控制后，Kyligence	Enterprise	默认单个项目最大任务并发数为	20，可以通过修改系统配置文件
	kylin.properties		中的参数	 	kylin.job.max-concurrent-jobs		来更改。

提交新任务时，如果超出了系统允许的任务并发数限制，那么该提交的任务会进入任务队列。当有运行的任务完成时，

Kyligence	Enterprise	会以先进先出	(FIFO)	的方式调度队列中的任务执行。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

432

任务操作

任务操作

您可以在	Kyligence	Enterprise	的任务监控界面执行对任务的操作，本节我们为您讲述任务的状态和操作含义。主要内容
如下：

任务状态

任务有以下	6	种状态：

等待状态（PENDING）：任务等待被调度执行的状态。

执行状态（RUNNING）：任务正常运行的状态，可以查看已经执行的进度，该进度以百分数形式展现。

暂停状态（STOPPED）：暂停正常执行的任务的状态。

报错状态（ERROR）：任务遇到无法继续执行的问题，界面显示报错的状态。

终止状态（DISCARDED）：任务报错终止执行的状态，终止的任务立即停止并释放所有资源。

提示：当任务的执行对象已经不存在或者发生变动，系统将自动终止该任务。

完成状态（FINISHED）：任务正常执行完毕的状态。

您可以在导航栏	监控	->	任务	界面查看任务状态信息，如下图所示：

任务状态

标号	1：执行状态。
标号	2：暂停状态。
标号	3：完成状态。
标号	4：报错状态。
标号	5：终止状态。
标号	6：批量操作选中任务。
标号	7：操作单一任务。

常见操作

恢复：从任务的某个中间步骤开始，继续执行任务。

提示：处于报错状态的任务，用户在排查或解决问题后，通过此操作来重试执行。

重启：放弃中间步骤结果，从	0	开始重新执行任务。

提示：处于报错状态的任务，如果任务的执行对象发生变动，如源表变化，我们建议您重启该任务，此时将

删除之前的任务记录，重新开始触发一个新的任务。

433

任务操作

暂停：暂停当前任务并释放所有相关资源。

终止：终止任务，并释放所有资源。

提示：终止任务之后，该任务不能被撤销也不能重启恢复。

删除：删除任务。

刷新列表：刷新任务列表的信息。

跨项目任务操作

作为系统管理员，在任务监控界面，您可以在项目列表中选择全部项目，查看所有项目下的任务信息。此时任务列表中

会出现项目列，您可以跨项目批量操作任务。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

434

任务诊断

任务诊断

任务在执行过程中可能会遇到各类问题，为了帮助高效解决这些问题，Kyligence	Enterprise	提供了任务诊断包功能，可
以将有关的日志信息打包成压缩包，供运维人员或	Kyligence	技术支持分析问题原因。

通过	Web	UI	查看任务执行日志

您可以在导航栏的	监控	-	>	批数据任务/流数据任务	界面查看任务的执行日志。如下图所示点击标号	1	展开任务详情图
标，然后在任务详情下查看日志详情，在弹窗中查看指定任务首尾各	100	行内容的执行日志。您可以点击标号	3	下载全
部日志链接来下载全量日志。

提示：如果一个任务有多个步骤，您可以查看每一步的执行日志。

任务日志

通过脚本生成任务诊断包：

FusionInsight	环境下需要先执行	 	source	/opt/hadoopclient/bigdata_env	，其中	 	hadoopclient		为变量。

执行	 	$KYLIN_HOME/bin/diag.sh	-job	<jobid>		生成任务诊断包，其中请将	 	<jobid>		代替为实际的任务	ID	号，您可以在
导航栏的	监控	-	>	批数据任务/流数据任务	界面查看任务	ID	号。如下图所示点击标号	1	位置的图标展开指定任务详情，
在右侧标号	2	位置查看任务	ID	号。

任务	ID

诊断包默认存放在	 	$KYLIN_HOME/diag_dump/		目录下。

435

任务诊断

解压诊断包之后，您可以在相应目录或文件下查看诊断包信息：

	/conf	： 	$KYLIN_HOME/conf		目录下的配置信息。
	/hadoop_conf	： 	$KYLIN_HOME/hadoop_conf		目录下的配置信息。
	/metadata	：元数据文件。

	/logs	：指定任务执行过程中产生的日志。

	/spark_logs	：指定任务执行过程中产生的所有	spark	executor	日志。
	/system_metrics	：指定任务执行过程中产生的系统监控指标。

	/audit_log	：指定任务执行过程中的审计日志（默认不包含）。

	/job_tmp	：指定任务执行过程中产生的临时文件，日志和优化建议日志。

	/yarn_application_log	：指定任务对应的	yarn	application	生成的日志。
	/client	：操作系统资源占用情况，hadoop	的版本和	kerberos	信息。
	/monitor_metrics	：指定任务的节点监控日志。

	/write_hadoop_conf	： 	$KYLIN_HOME/write_hadoop_conf	，构建集群的	hadoop	配置（未配置读写分离时不会有该目
录）。

文件	 	catalog_info	：安装包目录结构。
文件	 	commit_SHA1	：git-commit	版本号。
文件	 	hadoop_env	：hadoop	环境变量。
文件	 	info	：许可证，诊断包的信息和主机名称。
文件	 	kylin_env	：kyligence	Enterprise	版本，操作系统的信息，Java	的信息，git-commit	的信息。

提示:	若诊断包中不需要包含元数据文件，	可在参数中添加	 	-includeMeta	false

通过网页生成任务诊断包

任务诊断包包含某个任务的诊断信息，生成任务诊断包需要如下操作：

通过网页生成任务诊断包

1.	 在任务列表页面中某个任务的操作栏内，点击下载任务诊断包按钮。
2.	 选择服务器。
3.	 点击生成并下载：生成诊断包后，将自动触发下载任务，如果生成诊断包失败，您可以在界面上查看失败详情。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

436

常见任务错误原因和解决方案

常见任务错误原因和解决方案

构建类任务在执行过程中可能会发生各类问题，导致任务失败，通常任务详情中会直接展示简要的错误原因和错误描

述，本文会对一些常见的错误原因和对应的解决方案进行总结，辅助解决问题。

模型增量构建时，时间分区列的时间格式错误

错误码：	KE-030001003
错误描述：	模型时间分区设置中，时间分区列的时间格式，与数据源中实际的时间格式不一致。日志中关键信息
为： 	date	format	not	match	。

解决方案：

1.	 修改模型时间分区列时间格式，与数据源中实际时间格式保持一致:

请参考	模型设计方法	中步骤七：设置时间分区列和数据过滤条件修改时间分区列格式。

2.	 若坚持使用此格式，可以选择关闭时间分区列时间格式校验，在 	kylin.properties		中修改系统参数为

	kylin.engine.check-partition-col-enabled=false	。

注意：此种方式虽然可以绕过此处时间格式校验，但可能导致其他问题，请谨慎使用。

构建时发生	OOM	异常

错误码：	KE-030001004
错误描述：	任务构建过程中，Spark	Driver/Executor	发生OOM，日志中关键信息为： 	OutOfMemoryError	。
解决方案：

1.	 调整	spark.sql.shuffle.partitions

在构建过程中，如果出现	MetadataFetchFailedException,	executor	lost，oom	问题，可以尝试调整以下参数

kylin.engine.spark-conf.spark.sql.shuffle.partitions

这个参数决定:	在	aggregate	或者	join	执行时候	partitions	的个数，该值默认是200。

2.	 提高构建的资源

通常来讲，使用更多的资源，可以显著的提高执行性能和容错性。	通过以下参数调整构建使用的资源	:

kylin.engine.spark-conf.spark.executor.instances

kylin.engine.spark-conf.spark.executor.cores

kylin.engine.spark-conf.spark.executor.memory

kylin.engine.spark-conf.spark.executor.memoryOverhead

构建时空间不足

错误码：	KE-030001005
错误描述：	构建任务报错，磁盘空间不足，日志中关键信息为： 	No	space	left	on	device	。
解决方案：

1.	 请检查	Kyligence	Enterprise	和构建所使用的集群磁盘空间，及时清理无效文件或者扩容。
2.	 尝试清理	Kyligence	Enterprise	的低效存储，请参考	存储配额	。
3.	 shuffle	no	left	space	on	device	问题，可以适当提高	executor	instance	个数，来使用更多的计算资源。

kylin.engine.spark-conf.spark.executor.cores

kylin.engine.spark-conf.spark.executor.instances

437

常见任务错误原因和解决方案

构建时类未发现

错误码：	KE-030001006
错误描述：	构建时类未发现，日志中关键信息为： 	ClassNotFoundException		。
解决方案：

1.	 缺少	Mysql	驱动( 	java.lang.ClassNotFoundException:	com.mysql.jdbc.Driver	)

请参考	使用	MySQL	作为元数据库	设置	Mysql	作为元数据库。

未发现Kerberos	realm

错误码：	KE-030001007
错误描述：	构建时Kerberos未正确配置，导致Kerberos	realm	缺失，日志中关键信息为： 	Can't	get	Kerberos	realm
。

解决方案：

1.	 检查Kerberos配置

i.	 对于	Yarn	Cluster	和	Yarn	Client	模式，都应当检查	{KYLIN_HOME}/conf/	与

{KYLIN_HOME}/hadoop_conf/	中的	krb5.conf	文件配置是否正确。

ii.	 如果是	Yarn	Cluster	模式，请重点检查	{KYLIN_HOME}/spark/conf/spark-env.sh	中的	Kerberos	配置。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

438

SQL	查询

SQL	查询

本章将介绍如何在	Kyligence	Enterprise	中执行	SQL	查询语句，以及	Kyligence	Enterprise	支持的	SQL	语法和使用规范。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

439

数据类型

数据类型

Kyligence	已支持的数据类型列表如下：

字段类型

说明

取值范围

tinyint

小整数值

(-128，127)

smallint

大整数值

(-32,768，32,767)

int/integer

大整数值

(-2,147,483,648，2,147,483,647)

bigint

极大整数值

(-9,223,372,036,854,775,808，9,223,372,036,854,775,807)

float

double

单精度浮点
数值

双精度浮点
数值

decimal

小数值

timestamp

时间戳，纳
秒级精度

date

日期值

varchar

变长字符串

char

定长字符串

boolean

布尔类型

(-3.402823466E+38，-1.175494351E-38)，0，(1.175494351E-38，
3.402823466351E+38)

(-1.7976931348623157E+308，-2.2250738585072014E-308)，0，
(2.2250738585072014E-308，1.797693134	8623157E+308)

---

---

---

---

---

---

注意：double	类型计算存在精度不准确问题。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

440

查询分析

查询分析

Kyligence	Enterprise	是企业级智能多维数据库平台，您可以通过构建索引来完成预计算和数据加载，实现海量数据下的
亚秒级查询响应。

与普通查询的执行过程不同，Kyligence	Enterprise	在执行	SQL	时会用预计算结果代替在线计算，极大地减少在线计算
量，并提升查询性能。

预计算查询执行过程

与普通查询的执行过程不同，Kyligence	Enterprise	在执行	SQL	时会用预计算结果代替在线计算，极大地减少在线计算
量，并提升查询性能。为了便于理解，执行过程简化后可以描述为：

1.	 解析	SQL	语句，提取查询中所有的	 	FROM		子句。

2.	 为每个	 	FROM		子句寻找与之匹配的且代价最小的模型。	与之匹配需满足以下几点：

	FROM		子句中出现的表和它们间的关联必需与模型中定义事实表和维表的关联一致。留意	 	LEFT	JOIN		与
	INNER	JOIN		是不匹配的。
对于聚合查询， 	GROUP	BY		子句中的聚合列必需是模型中定义的维度，同时	 	SELECT		子句中的聚合函数必需是
模型中定义的度量。

对于非聚合查询（即不带聚合函数），模型中必需定义有表明细索引，否则匹配失败。同时查询中所有的列都

必需包含在表明细索引中。

代价最小指当有多个可能的匹配（模型/索引）时，Kyligence	Enterprise	会根据执行代价最低的原则，自动挑选一个
最优的匹配。比如，表明细索引其实也可以匹配聚合查询，但由于需要作在线聚合运算，执行代价很高。因此，用

表明细索引匹配聚合查询是最后的选择，只会发生在所有模型的聚合索引都无法匹配的时候。

3.	 若所有	 	FROM		子句均匹配成功，那么	Kyligence	Enterprise	将使用模型下的索引执行查询。

查询中所有的	 	FROM		子句将被替换成预计算结果，然后执行并获得查询结果。如果您在	Web	UI	执行查询，查询成
功后，可以在屏幕下方的查询对象条目中找到命中模型的名字。详见在用户界面执行	SQL	查询。

4.	 若有个别	 	FROM		子句无法找到匹配的模型或索引组，那么	Kyligence	Enterprise	无法用模型或索引组执行查询。

查询将报错，出错信息为	 	no	model	found		或	 	no	realization	found	。

作为特例，如果查询下压被启用，那么	Kyligence	Enterprise	将不会报错，而是转发这种无法匹配的查询到下压查询
引擎执行。更多请见查询下压的详细介绍。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

441

查询分析

在用户界面执行	SQL	查询

打开	Kyligence	Enterprise	的	Web	UI，进入导航栏	查询	->	分析	界面。如下图所示左边为您添加的数据源表，即所有可
以查询的表。右边为查询分析面板，在上方的查询编辑器中输入	SQL	语句并点击查询，将在下方显示结果。下面详述
不同标识对应的解释。

分析界面

执行	SQL	查询

在输入框中输入	SQL	语句，点击查询按钮即可进行查询。在右下角提交按钮旁有一个	Limit	输入框，如果	SQL	语句中
不含	Limit	子句，则该	SQL	语句会拼接一个默认	Limit	值。如果	SQL	语句中有	Limit	子句则以	SQL	语句为准。假如用
户想去掉	Limit	限制，可以反选	Limit	前的选择框。

select	LO_ORDERDATE,	count(*)

from	SSB.P_LINEORDER

group	by	LO_ORDERDATE

查询结果成功返回并在下方显示查询信息。您可以看出该查询执行时间为	0.13	秒，并且查询对象中显示该查询击中了模
型。

同时，点击查询	ID	后箭头图标，可以直接打开	Spark	UI	中关于该查询的页面。在该页面，用户可以方便的看到该	SQL
在	Spark	中的执行流程。

442

查询分析

当您在进行慢查询优化时，需要了解查询的具体执行步骤，定位耗时原因。可点击展开响应时间，以查看当前查询的详

细执行步骤及耗时，辅助分析。

443

查询分析

查询耗时

注意：

1.	 仅支持	SELECT	查询语句。
2.	 若开启了查询下压，当查询无法击中模型（索引组）时，将会重定向到下压查询引擎执行。这时可能耗时稍

长。此时查询对象可能显示为	Hive，即查询下压至	Hive。

3.	 若查询不需要	Spark	计算，例如击中查询缓存，常量查询等，则不会有箭头打开	Spark	UI。
4.	 当查询使用分层存储时，查询扫描记录数需要手动获取。

停止查询

点击查询按钮后，点击相同位置的停止按钮，即可停止此次查询。

444

查询分析

查询被停止后，展示此次查询的查询	ID	和报错文案。

此外，点击该查询的关闭按钮也会停止此次查询。

保存查询

与用户账号关联，用户将能够从不同的浏览器甚至机器上获取已保存的查询。在查询编辑器下方点击保存查询按钮，将

会在弹窗中提示输入名称和描述来保存当前查询。

445

查询分析

保存查询

已保存的查询

在查询编辑器的右上方点击已保存的查询按钮查看所有保存的查询。弹窗中将显示已保存的查询列表，您可以勾选查询

前方的选择框，然后点击查询按钮来重新执行查询。

446

查询分析

已保存的查询

查询结果展现

默认情况下，Kyligence	Enterprise	会以表格形式展示数据。您可以在查询结果右上方的筛选框中搜索查询内容，该搜索
方式为模糊搜索。如输入	 	1992	，则查询结果中的每一行都将包含	 	1992	，如图所示为	1992	年每天的订单量。也可以
点击导出按钮将查询结果导出到	CSV	文件。

查询结果展现

查询可视化

除了表格，Kyligence	Enterprise	还支持可视化展示查询结果，实现快速洞察。

447

查询分析

目前支持：折线图，柱状图，饼图。

查询可视化

其他执行	SQL	查询的方式

与BI工具集成

注意事项

如果查询既可以用索引回答也可以用快照回答，将会优先由快照回答。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

448

查询分析

查询样例

我们以	Kyligence	Enterprise	的样例数据集为例介绍	SQL	的查询方式。首先请您通过AI	增强模式指引完整创建一个	AI	增
强模式的项目，构建索引并当所有任务成功执行完毕后，请您进入	查询	->	分析	页面。请您在查询编辑器中输入	SQL
语句，然后单击提交按钮。

下面我们将介绍	SQL	查询的例子和相应的结果。

提示：你可以在样例数据集章节查看样例数据集的介绍，你也可以在	Kyligence	Enterprise	的模型编辑界面查看模
型。

单表行数统计

SELECT	COUNT(*)	FROM	P_LINEORDER

这条	SQL	用于查询	P_LINEORDER	表中总行数，您可以同时在	Hive	中执行同样的查询进行性能对比。在我们的对比
中，Hive	查询耗时	29.711	秒，Kyligence	Enterprise	查询耗时	2.18	秒。

多表连接

select

P_LINEORDER.LO_SUPPKEY

,	P_LINEORDER.LO_PARTKEY

,	PART.P_NAME

,	SUPPLIER.S_CITY

,	sum(LO_QUANTITY)

from	P_LINEORDER

left	join	PART	on	P_LINEORDER.LO_PARTKEY	=	PART.P_PARTKEY

left	join	SUPPLIER	on	P_LINEORDER.LO_SUPPKEY	=	SUPPLIER.S_SUPPKEY

group	by

P_LINEORDER.LO_SUPPKEY

,	P_LINEORDER.LO_PARTKEY

,	PART.P_NAME

,	SUPPLIER.S_CITY

这条	SQL	将事实表	P_LINEORDER	和两张维度表	PART	和	SUPPLIER	根据外键进行了左连接。在笔者的对比试验中，
Hive	查询耗时	28.164	秒，Kyligence	Enterprise	查询耗时	2.06	秒。

全表查询

SELECT	*	FROM	P_LINEORDER

假如没有创建表明细索引，Kyligence	Enterprise	默认并不对原始数据的明细进行保存，因此该查询将不会击中模型。但
是	Kyligence	Enterprise	默认开启查询下压引擎，该条查询将通过查询下压至	Spark	SQL	返回结果。您可以查看下压至原
生	SparkSQL	章节了解更多。

如果您希望	Kyligence	Enterprise	支持原始数据的保存和查询，可以创建相关列的表明细索引并加载数据。您可以查看表
明细索引章节了解更多。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

449

查询分析

SQL	规范参考

Kyligence	Enterprise	支持	ANSI	SQL	2003，以下列举了支持的基本	SQL	语句。

支持语法

statement:

|		query

query:

						values

		|		WITH	withItem	[	,	withItem	]*	query

		|			{

										select

						|		selectWithoutFrom

						|		query	UNION	[	ALL	|	DISTINCT	]	query

						|		query	INTERSECT	[	ALL	|	DISTINCT	]	query

						}

						[	ORDER	BY	orderItem	[,	orderItem	]*	]

						[	LIMIT	{	count	|	ALL	}	]

						[	OFFSET	start	{	ROW	|	ROWS	}	]

						[	FETCH	{	FIRST	|	NEXT	}	[	count	]	{	ROW|	ROWS	}	]

withItem:

						name

						['('	column	[,	column	]*	')'	]

						AS	'('	query	')'

orderItem:
						expression	[	ASC	|	DESC	]［	NULLS	FIRST	|NULLS	LAST	］

select:

						SELECT	[	ALL	|	DISTINCT]

										{	*	|	projectItem	[,	projectItem	]*	}

						FROM	tableExpression

						[	WHERE	booleanExpression	]

						[	GROUP	BY	{	groupItem	[,	groupItem	]*	}]

						[	HAVING	booleanExpression	]

						[	WINDOW	windowName	AS	windowSpec	[,windowName	AS	windowSpec	]*	]

selectWithoutFrom:

						SELECT	[	ALL	|	DISTINCT	]

										{	*	|	projectItem	[,	projectItem	]*	}

projectItem:

						expression	[	[	AS	]	columnAlias	]

		|		tableAlias	.	*

tableExpression:

						tableReference	[,	tableReference	]*
		|		tableExpression	[	NATURAL	]［(	LEFT	|	RIGHT	|	FULL	)	[	OUTER	]	］	JOINtableExpression	[	joinCondition	]

joinCondition:

						ON	booleanExpression

		|		USING	'('	column	[,	column	]*	')'

tableReference:

						tablePrimary

						[	matchRecognize	]

						[	[	AS	]	alias	[	'('	columnAlias	[,columnAlias	]*	')'	]	]

tablePrimary:

						[	[	catalogName	.	]	schemaName	.	]tableName

						'('	TABLE	[	[	catalogName	.	]	schemaName.	]	tableName	')'

450

查询分析

		|			[LATERAL	]	'('	query	')'

		|		UNNEST	'('	expression	')'	[	WITH	ORDINALITY	]

		|			[LATERAL	]	TABLE	'('	[	SPECIFIC	]	functionName	'('	expression	[,	expression	]*')'	')'

values:

						VALUES	expression	[,	expression	]*

groupItem:

						expression

		|			'('')'

		|			'('expression	[,	expression	]*	')'

		|		GROUPING	SETS	'('	groupItem	[,	groupItem	]*	')'

windowRef:

						windowName

		|		windowSpec

windowSpec:

						[windowName	]

						'('

						[	ORDER	BYorderItem	[,	orderItem	]*	]

						[	PARTITION	BY	expression	[,	expression]*	]

						[

										RANGE	numericOrIntervalExpression	{PRECEDING	|	FOLLOWING	}

						|		ROWS	numericExpression	{	PRECEDING	|	FOLLOWING	}

						]

				')'

注意：不同版本实现反馈可能会有不同，如有问题请咨询技术服务团队。

SQL	关键字

以下为	Kyligence	Enterprise	中	SQL的关键字，请尽可能避免使用关键字做为标识符。

A,	ABS,	ABSOLUTE,	ACTION,	ADA,	ADD,	ADMIN,	AFTER,	ALL,ALLOCATE,	ALLOW,	ALTER,	ALWAYS,	AND,	ANY,

APPLY,	ARE,	ARRAY,ARRAY_MAX_CARDINALITY,	AS,	ASC,	ASENSITIVE,	ASSERTION,	ASSIGNMENT,

ASYMMETRIC,	AT,	ATOMIC,	ATTRIBUTE,	ATTRIBUTES,AUTHORIZATION,	AVG,	BEFORE,	BEGIN,

BEGIN_FRAME,BEGIN_PARTITION,	BERNOULLI,	BETWEEN,	BIGINT,	BINARY,	BIT,BLOB,	BOOLEAN,	BOTH,

BREADTH,	BY,	C,	CALL,	CALLED,CARDINALITY,	CASCADE,	CASCADED,	CASE,	CAST,	CATALOG,

CATALOG_NAME,	CEIL,	CEILING,	CENTURY,	CHAIN,	CHAR,CHARACTER,	CHARACTERISTICS,

CHARACTERS,CHARACTER_LENGTH,	CHARACTER_SET_CATALOG,	CHARACTER_SET_NAME,

CHARACTER_SET_SCHEMA,CHAR_LENGTH,	CHECK,	CLASSIFIER,	CLASS_ORIGIN,	CLOB,	CLOSE,COALESCE,

COBOL,	COLLATE,	COLLATION,	COLLATION_CATALOG,	COLLATION_NAME,	COLLATION_SCHEMA,	COLLECT,

COLUMN,	COLUMN_NAME,	COMMAND_FUNCTION,	COMMAND_FUNCTION_CODE,	COMMIT,

COMMITTED,CONDITION,	CONDITION_NUMBER,	CONNECT,	CONNECTION,	CONNECTION_NAME,

CONSTRAINT,	CONSTRAINTS,	CONSTRAINT_CATALOG,	CONSTRAINT_NAME,	CONSTRAINT_SCHEMA,

CONSTRUCTOR,	CONTAINS,	CONTINUE,CONVERT,	CORR,	CORRESPONDING,	COUNT,

COVAR_POP,COVAR_SAMP,	CREATE,	CROSS,	CUBE,	CUME_DIST,	CURRENT,CURRENT_CATALOG,

CURRENT_DATE,CURRENT_DEFAULT_TRANSFORM_GROUP,	CURRENT_PATH,CURRENT_ROLE,

CURRENT_ROW,	CURRENT_SCHEMA,CURRENT_TIME,

CURRENT_TIMESTAMP,CURRENT_TRANSFORM_GROUP_FOR_TYPE,	CURRENT_USER,CURSOR,

CURSOR_NAME,	CYCLE,	DATA,	DATABASE,	DATE,	DATETIME_INTERVAL_CODE,

DATETIME_INTERVAL_PRECISION,DAY,	DEALLOCATE,	DEC,	DECADE,	DECIMAL,	DECLARE,	DEFAULT,

DEFAULTS,	DEFERRABLE,	DEFERRED,	DEFINE,	DEFINED,	DEFINER,	DEGREE,	DELETE,	DENSE_RANK,	DEPTH,

DEREF,	DERIVED,	DESC,DESCRIBE,	DESCRIPTION,	DESCRIPTOR,	DETERMINISTIC,	DIAGNOSTICS,	DISALLOW,

DISCONNECT,	DISPATCH,	DISTINCT,	DOMAIN,	DOUBLE,	DOW,	DOY,	DROP,	DYNAMIC,	DYNAMIC_FUNCTION,

DYNAMIC_FUNCTION_CODE,	EACH,ELEMENT,	ELSE,	EMPTY,	END,	END-EXEC,	END_FRAME,END_PARTITION,

EPOCH,	EQUALS,	ESCAPE,	EVERY,	EXCEPT,	EXCEPTION,	EXCLUDE,	EXCLUDING,	EXEC,	EXECUTE,	EXISTS,

451

查询分析

EXP,EXPLAIN,	EXTEND,	EXTERNAL,	EXTRACT,	FALSE,	FETCH,	FILTER,	FINAL,	FIRST,	FIRST_VALUE,	FLOAT,

FLOOR,	FOLLOWING,	FOR,FOREIGN,	FORTRAN,	FOUND,	FRAC_SECOND,	FRAME_ROW,	FREE,FROM,	FULL,

FUNCTION,	FUSION,	G,	GENERAL,	GENERATED,	GET,GLOBAL,	GO,	GOTO,	GRANT,	GRANTED,	GROUP,

GROUPING,GROUPS,	HAVING,	HIERARCHY,	HOLD,	HOUR,	IDENTITY,	IMMEDIATE,	IMMEDIATELY,

IMPLEMENTATION,	IMPORT,	IN,	INCLUDING,	INCREMENT,	INDICATOR,	INITIAL,	INITIALLY,	INNER,INOUT,

INPUT,	INSENSITIVE,	INSERT,	INSTANCE,	INSTANTIABLE,	INT,INTEGER,	INTERSECT,	INTERSECTION,

INTERVAL,	INTO,	INVOKER,	IS,	ISOLATION,	JAVA,	JOIN,	JSON,	K,	KEY,	KEY_MEMBER,	KEY_TYPE,	LABEL,	LAG,

LANGUAGE,	LARGE,	LAST,	LAST_VALUE,	LATERAL,	LEAD,LEADING,	LEFT,	LENGTH,	LEVEL,	LIBRARY,	LIKE,

LIKE_REGEX,	LIMIT,LN,	LOCAL,	LOCALTIME,	LOCALTIMESTAMP,	LOCATOR,	LOWER,	M,	MAP,	MATCH,

MATCHED,	MATCHES,	MATCH_NUMBER,MATCH_RECOGNIZE,	MAX,	MAXVALUE,	MEASURES,

MEMBER,MERGE,	MESSAGE_LENGTH,	MESSAGE_OCTET_LENGTH,	MESSAGE_TEXT,	METHOD,	MICROSECOND,

MILLENNIUM,	MIN,MINUS,	MINUTE,	MINVALUE,	MOD,	MODIFIES,	MODULE,	MONTH,	MORE,	MULTISET,

MUMPS,	NAME,	NAMES,	NATIONAL,	NATURAL,NCHAR,	NCLOB,	NESTING,	NEW,	NEXT,	NO,	NONE,	NORMALIZE,

NORMALIZED,	NOT,	NTH_VALUE,	NTILE,	NULL,	NULLABLE,	NULLIF,	NULLS,	NUMBER,	NUMERIC,	OBJECT,

OCCURRENCES_REGEX,	OCTETS,	OCTET_LENGTH,	OF,	OFFSET,	OLD,	OMIT,	ON,	ONE,	ONLY,OPEN,	OPTION,

OPTIONS,	OR,	ORDER,	ORDERING,	ORDINALITY,	OTHERS,	OUT,	OUTER,	OUTPUT,	OVER,	OVERLAPS,	OVERLAY,

OVERRIDING,	PAD,	PARAMETER,	PARAMETER_MODE,	PARAMETER_NAME,	PARAMETER_ORDINAL_POSITION,

PARAMETER_SPECIFIC_CATALOG,	PARAMETER_SPECIFIC_NAME,	PARAMETER_SPECIFIC_SCHEMA,	PARTIAL,

PARTITION,	PASCAL,	PASSTHROUGH,	PAST,	PATH,	PATTERN,	PER,	PERCENT,PERCENTILE_CONT,

PERCENTILE_DISC,	PERCENT_RANK,	PERIOD,PERMUTE,	PLACING,	PLAN,	PLI,	PORTION,

POSITION,POSITION_REGEX,	POWER,	PRECEDES,	PRECEDING,	PRECISION,PREPARE,	PRESERVE,	PREV,

PRIMARY,	PRIOR,	PRIVILEGES,PROCEDURE,	PUBLIC,	QUARTER,	RANGE,	RANK,	READ,	READS,

REAL,RECURSIVE,	REF,	REFERENCES,	REFERENCING,	REGR_AVGX,REGR_AVGY,	REGR_COUNT,

REGR_INTERCEPT,	REGR_R2,REGR_SLOPE,	REGR_SXX,	REGR_SXY,	REGR_SYY,	RELATIVE,	RELEASE,

REPEATABLE,	REPLACE,	RESET,	RESTART,	RESTRICT,	RESULT,RETURN,	RETURNED_CARDINALITY,

RETURNED_LENGTH,	RETURNED_OCTET_LENGTH,	RETURNED_SQLSTATE,	RETURNS,REVOKE,	RIGHT,	ROLE,

ROLLBACK,	ROLLUP,	ROUTINE,	ROUTINE_CATALOG,	ROUTINE_NAME,	ROUTINE_SCHEMA,	ROW,ROWS,

ROW_COUNT,	ROW_NUMBER,	RUNNING,	SAVEPOINT,	SCALE,	SCHEMA,	SCHEMA_NAME,	SCOPE,

SCOPE_CATALOGS,	SCOPE_NAME,	SCOPE_SCHEMA,	SCROLL,	SEARCH,	SECOND,	SECTION,	SECURITY,	SEEK,

SELECT,	SELF,	SENSITIVE,	SEQUENCE,	SERIALIZABLE,	SERVER,	SERVER_NAME,	SESSION,	SESSION_USER,SET,

SETS,	SHOW,	SIMILAR,	SIMPLE,	SIZE,	SKIP,	SMALLINT,	SOME,	SOURCE,	SPACE,	SPECIFIC,	SPECIFICTYPE,

SPECIFIC_NAME,	SQL,SQLEXCEPTION,	SQLSTATE,	SQLWARNING,	SQL_BIGINT,	SQL_BINARY,	SQL_BIT,

SQL_BLOB,	SQL_BOOLEAN,	SQL_CHAR,	SQL_CLOB,	SQL_DATE,	SQL_DECIMAL,	SQL_DOUBLE,	SQL_FLOAT,

SQL_INTEGER,	SQL_INTERVAL_DAY,	SQL_INTERVAL_DAY_TO_HOUR,	SQL_INTERVAL_DAY_TO_MINUTE,

SQL_INTERVAL_DAY_TO_SECOND,	SQL_INTERVAL_HOUR,	SQL_INTERVAL_HOUR_TO_MINUTE,

SQL_INTERVAL_HOUR_TO_SECOND,	SQL_INTERVAL_MINUTE,	SQL_INTERVAL_MINUTE_TO_SECOND,

SQL_INTERVAL_MONTH,	SQL_INTERVAL_SECOND,	SQL_INTERVAL_YEAR,

SQL_INTERVAL_YEAR_TO_MONTH,	SQL_LONGVARBINARY,	SQL_LONGVARCHAR,	SQL_LONGVARNCHAR,

SQL_NCHAR,	SQL_NCLOB,	SQL_NUMERIC,	SQL_NVARCHAR,	SQL_REAL,	SQL_SMALLINT,	SQL_TIME,

SQL_TIMESTAMP,	SQL_TINYINT,	SQL_TSI_DAY,	SQL_TSI_FRAC_SECOND,	SQL_TSI_HOUR,

SQL_TSI_MICROSECOND,	SQL_TSI_MINUTE,	SQL_TSI_MONTH,	SQL_TSI_QUARTER,	SQL_TSI_SECOND,

SQL_TSI_WEEK,	SQL_TSI_YEAR,	SQL_VARBINARY,	SQL_VARCHAR,	SQRT,	START,	STATE,	STATEMENT,STATIC,

STDDEV_POP,	STDDEV_SAMP,	STREAM,	STRUCTURE,	STYLE,	SUBCLASS_ORIGIN,	SUBMULTISET,	SUBSET,

SUBSTITUTE,SUBSTRING,	SUBSTRING_REGEX,	SUCCEEDS,	SUM,	SYMMETRIC,SYSTEM,	SYSTEM_TIME,

SYSTEM_USER,	TABLE,	TABLESAMPLE,	TABLE_NAME,	TEMPORARY,	THEN,	TIES,	TIME,	TIMESTAMP,

TIMESTAMPADD,	TIMESTAMPDIFF,	TIMEZONE_HOUR,TIMEZONE_MINUTE,	TINYINT,	TO,	TOP_LEVEL_COUNT,

TRAILING,	TRANSACTION,	TRANSACTIONS_ACTIVE,	TRANSACTIONS_COMMITTED,

TRANSACTIONS_ROLLED_BACK,	TRANSFORM,	TRANSFORMS,	TRANSLATE,

TRANSLATE_REGEX,TRANSLATION,	TREAT,	TRIGGER,	TRIGGER_CATALOG,	TRIGGER_NAME,

TRIGGER_SCHEMA,	TRIM,	TRIM_ARRAY,	TRUE,TRUNCATE,	TYPE,	UESCAPE,	UNBOUNDED,	UNCOMMITTED,

UNDER,	UNION,	UNIQUE,	UNKNOWN,	UNNAMED,	UNNEST,UPDATE,	UPPER,	UPSERT,	USAGE,	USER,

452

查询分析

USER_DEFINED_TYPE_CATALOG,	USER_DEFINED_TYPE_CODE,	USER_DEFINED_TYPE_NAME,

USER_DEFINED_TYPE_SCHEMA,USING,	VALUE,	VALUES,	VALUE_OF,	VARBINARY,	VARCHAR,VARYING,

VAR_POP,	VAR_SAMP,	VERSION,	VERSIONING,	VIEW,	WEEK,	WHEN,	WHENEVER,	WHERE,	WIDTH_BUCKET,

WINDOW,WITH,	WITHIN,	WITHOUT,	WORK,	WRAPPER,	WRITE,	XML,	YEAR,	ZONE.

标识符

标识符为	SQL	查询中使用的表名、列名以及其他元数据。没有使用引号的标识符，如	emp	，需要以字母开头并且只能
包含字母、数字及下划线。没有使用引号的标识符在查询时会隐式地被转换成全大写。

带引号的标识符，如	"Employee	Name"，以双引号开头及结尾。这种标识符基本可以包含任何字符，包括空格或其他标
点符号。如果您希望在标识符中包含双引号，使用另一个双引号来将其转义，例如：An	employee	called	""Fred""."

标识符和引用的对象进行匹配是大小写敏感的。没有使用引号的标识符会隐式地被转换成全大写，如果查询对象在创建

时也没有使用引号，它的名字也会被转换成全大写，因此标识符和查询对象可以进行匹配。

转义关键字

如果您的列名或表名是关键字，您需要使用双引号对其进行转义。

例如表	DATES	包含列	YEAR。这列的列名和	Kyligence	Enterprise	的关键字	YEAR	重复。如下图所示，如果用户直接对
YEAR	进行查询，查询会返回报错，因为	Kyligence	Enterprise	查询引擎无法分辨该列是关键字还是列名。

关键字命名列名导致查询失败

如上文所述，这时候您只要在列名两端加上双引号就可以正常查询了。

453

查询分析

双引号大写列名获得查询结果

转义引号

如果您查询的值中包含单引号，您可以用另一个单引号对查询进行转义。

转义单引号

但是查询的值中的双引号是不需要转义的。

454

查询分析

转义双引号

日期查询

如果您进行查询的关键字中包含日期类型的列，您可以参照以下两种日期查询语法范例：

第一种：

select	LO_LINENUMBER,	LO_ORDERDATE,	LO_ORDTOTALPRICE

from	SSB.P_LINEORDER

where	LO_ORDERDATE	=	date	'1992-06-03'

455

查询分析

日期查询示例	1

第二种：

select	LO_LINENUMBER,	LO_ORDERDATE,	LO_ORDTOTALPRICE

from	SSB.P_LINEORDER

where	LO_ORDERDATE	=	cast	(	'1992-06-03'	as	date)

456

查询分析

日期查询示例	2

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

457

查询分析

异步查询

异步查询支持用户异步地执行	SQL	查询，并提供更高效的数据导出方式。比如如果一条	SQL	查询的结果集	过大（百万
条结果）或	SQL	执行时间过长，通过异步查询，可以高效地把查询结果集导出，实现自助取数	等各种应用场景。

目前异步查询仅支持调用	REST	API	方式，关于如何使用异步查询	API，请阅读	-	异步查询	API	。

为异步查询结果，配置留存时间

异步查询支持在	 	kylin.properties		进行以下配置：

	kylin.query.async.result-retain-days=7d		：异步查询结果在HDFS上的留存时间，默认为	7	天，即超过	7	天的异步
查询结果及相关文件将被清理

为异步查询，配置单独的集群队列

一般情况下，异步查询和普通查询使用相同的集群队列即可。在一些高级场景下，如果希望避免异步查询影响普通查

询，可以针对异步查询部署单独的队列。具体的配置方式如下：

1.	 开启异步查询部署单独的集群队列设置。将 	kylin.query.unique-async-query-yarn-queue-enabled		设为 	true	，支持
项目级配置和系统级配置，项目级配置的优先级高于系统级配置。	若均未配置，则异步查询与普通查询使用相同的
集群队列。

2.	 指定异步查询使用的队列。支持三个级别进行指定，优先级从高到低依次为:

查询级别，通过	API	请求参数	 	spark_queue		进行指定
项目级别，项目设置	 	kylin.query.async-query.spark-conf.spark.yarn.queue		进行指定
系统级别，配置文件	 	/conf/kylin.properties		中设置	 	kylin.query.async-query.spark-conf.spark.yarn.queue
进行指定

提示：若三种均未配置，默认队列为	 	default

3.	 设置配置:	 	kylin.query.async-query.submit-hadoop-conf-dir=$KYLIN_HOME/async_query_hadoop_conf

4.	 将异步查询集群的	hadoop	配置放到	 	$KYLIN_HOME/async_query_hadoop_conf		目录下，同时把构建集群的	 	hive-

site.xml		分别放到此目录中。

如果开启了	Kerberos	认证，需要将	 	krb5.conf		文件拷贝到	 	$KYLIN_HOME/async_query_hadoop_conf		目录。

5.	 如果异步查询集群、查询集群和构建集群之间开启了	Kerberos	认证，还需要进行以下额外配置：

		kylin.storage.columnar.spark-conf.spark.yarn.access.hadoopFileSystems=hdfs://readcluster,hdfs://asyncquer

ycluster,hdfs://writecluster

		kylin.query.async-query.spark-conf.spark.yarn.access.hadoopFileSystems=hdfs://readcluster,hdfs://asyncque

rycluster,hdfs://writecluster

		kylin.engine.spark-conf.spark.yarn.access.hadoopFileSystems=hdfs://readcluster,hdfs://asyncquerycluster,h

dfs://writecluster

6.	 一般情况下，上述配置即可满足要求。在一些更高级的场景中，可通过	Kyligence	专家指导，在	 	kylin.properties

中配置	spark	的相关配置，以实现更精细的控制。

配置以 	kylin.query.async-query.spark-conf		开头，如下所示：

kylin.query.async-query.spark-conf.spark.yarn.queue=default

kylin.query.async-query.spark-conf.spark.executor.extraJavaOptions=-Dhdp.version=current	-Dlog4j.configuration=

spark-executor-log4j.properties	-Dlog4j.debug	-Dkylin.hdfs.working.dir=${kylin.env.hdfs-working-dir}	-Dkap.meta

data.identifier=${kylin.metadata.url.identifier}	-Dkap.spark.category=sparder	-Dkap.spark.project=${job.project

458

查询分析

}	-Dkap.spark.mountDir=${kylin.tool.mount-spark-log-dir}	-XX:MaxDirectMemorySize=896M

kylin.query.async-query.spark-conf.spark.yarn.am.extraJavaOptions=-Dhdp.version=current

kylin.query.async-query.spark-conf.spark.driver.extraJavaOptions=-Dhdp.version=current

kylin.query.async-query.spark-conf.spark.port.maxRetries=128

kylin.query.async-query.spark-conf.spark.driver.memory=4096m

kylin.query.async-query.spark-conf.spark.sql.driver.maxCollectSize=3600m

kylin.query.async-query.spark-conf.spark.executor.memory=12288m

kylin.query.async-query.spark-conf.spark.executor.memoryOverhead=3072m

kylin.query.async-query.spark-conf.spark.yarn.am.memory=1024m

kylin.query.async-query.spark-conf.spark.executor.cores=5

kylin.query.async-query.spark-conf.spark.executor.instances=4

kylin.query.async-query.spark-conf.spark.task.maxFailures=1

kylin.query.async-query.spark-conf.spark.ui.port=4041

kylin.query.async-query.spark-conf.spark.locality.wait=0s

kylin.query.async-query.spark-conf.spark.sql.dialect=hiveql

kylin.query.async-query.spark-conf.spark.sql.constraintPropagation.enabled=false

kylin.query.async-query.spark-conf.spark.ui.retainedStages=300

kylin.query.async-query.spark-conf.spark.hadoop.yarn.timeline-service.enabled=false

kylin.query.async-query.spark-conf.spark.hadoop.hive.exec.scratchdir=${kylin.env.hdfs-working-dir}/hive-scratch

kylin.query.async-query.spark-conf.hive.execution.engine=MR

kylin.query.async-query.spark-conf.spark.sql.crossJoin.enabled=true

kylin.query.async-query.spark-conf.spark.broadcast.autoClean.enabled=true

kylin.query.async-query.spark-conf.spark.sql.objectHashAggregate.sortBased.fallbackThreshold=1

kylin.query.async-query.spark-conf.spark.sql.hive.caseSensitiveInferenceMode=NEVER_INFER

kylin.query.async-query.spark-conf.spark.sql.sources.bucketing.enabled=false

kylin.query.async-query.spark-conf.spark.yarn.stagingDir=${kylin.env.hdfs-working-dir}

kylin.query.async-query.spark-conf.spark.eventLog.enabled=true

kylin.query.async-query.spark-conf.spark.history.fs.logDirectory=${kylin.env.hdfs-working-dir}/sparder-history

kylin.query.async-query.spark-conf.spark.eventLog.dir=${kylin.env.hdfs-working-dir}/sparder-history

kylin.query.async-query.spark-conf.spark.eventLog.rolling.enabled=true

kylin.query.async-query.spark-conf.spark.eventLog.rolling.maxFileSize=100m

kylin.query.async-query.spark-conf.spark.sql.cartesianPartitionNumThreshold=-1

kylin.query.async-query.spark-conf.parquet.filter.columnindex.enabled=false

kylin.query.async-query.spark-conf.spark.master=yarn

kylin.query.async-query.spark-conf.spark.submit.deployMode=client

已知限制

异步查询不支持查询缓存。

当	SQL	的	select	列中包含	 	,;{}()=		时，在结果文件中会将这些字符转化为	 	_	。
异步查询不支持查询下压至	JDBC	数据源。

行为变更

自	4.6.4	版本后，为了解决返回大量结果的性能问题，产品进行了变更， 	include_header	参数被移至提交异步查询
的API，下载查询结果API中的 	include_header	参数将不起作用。请参考异步查询	API以了解更多细节。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

459

查询分析

通过模型视图简化查询

从	4.5.2	版本开始，引入了模型视图，支持将模型中的表根据关联关系打平后对外暴露，用户可直接通过模型名称查询
数据，而无需写全源表的关联关系，从而简化	SQL	语句或在	BI	工具及应用程序中二次建模的过程。

如何使用

提供系统级和项目级参数以开启模型视图功能，默认为关闭，若需使用模型视图，您可以根据需求在系统级或项目级配

置以下参数：

kylin.query.auto-model-view-enabled=true

模型视图包含模型中的所有维度和度量列，数据已经根据关联关系和筛选条件完成整合。当您查询某个模型时，在

	from		子句中可以直接写	 	项目名称.模型名称		来表示模型视图。

如图模型的关联关系如下：

模型关联关系

查询语句如下：

select	C_NAME,	sum(LO_QUANTITY)	as	total_quantity

from	kyligence.model

group	by	C_NAME

460

查询分析

通过模型视图简化查询

注意事项：

模型视图不支持行列级访问权限设置，若需要设置行列级权限，请不要使用模型视图，具体影响如下：

对模型视图包含的列设置权限，会导致所有用模型视图的查询失败；

对行设置访问权限无效，仍然可以查询到无权限的行数据。

如果数据源中存在与	 	项目名称.模型名称		同名的表，将使用数据源的表回答查询；
模型视图不支持查询下压，如果查询无法击中模型，将失败；

修改模型名称，相当于更改了模型视图的名称，此时，之前包含旧模型视图名称的查询将不可用；

在	BI	工具中连接模型视图

您可以在	BI	工具中连接模型视图，以减少在	BI	工具中的二次建模工作。首先需要在系统级或项目级配置参数
	kylin.query.auto-model-view-enabled=true	，然后就可以在	BI	工具连接	Kyligence	Enterprise	时，选择连接项目下的模
型视图，最后通过模型视图进行分析。

注意事项：

不建议在	Tableau	中连接模型视图，您可以在	Kyligence	Enterprise	中导出模型的	TDS	文件，该方式可以避免重复建
模，且成熟度较高，可查看与	Tableau	Desktop	集成	章节了解更多；
在	BI	工具中连接模型视图时尚存在一些兼容性问题，使用前请联系	Kyligence	评估方案可行性，目前已知问题如
下：

在	Power	BI	中连接模型视图，可能存在读取中文字段乱码的问题；

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

461

查询分析

函数及运算符

本节介绍适用于查询的函数和运算符。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

462

查询分析

运算符

Kyligence	Enterprise	支持如下运算符：

比较运算符

逻辑运算符

算术运算符

字符串运算符

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

463

查询分析

比较运算符

运算符

描述

语法

示例

<

<=

>

>=

<>

小于

小于或等于

大于

大于或等于

不等于

A<B

A<=B

A>=B

A>=B

A<>B

Profit	<	Cost

Profit	<=Cost

Profit	>Cost

Profit	>=Cost

Profit1<>Profit2

IS	NULL

判断值是否为	NULL

value	IS	NULL

profit	IS	NULL

IS	NOT
NULL

IS
DISTINCT
FROM

IS	NOT
DISTINCT
FROM

BETWEEN

判断值是否不为	NULL

判断两个值是否不相等，其中
有值为	NULL	时当作相等。

判断两个值是否相等，其中有
值为	NULL	时当作相等。

value	IS	NOT
NULL

value1	IS
DISTINCT	FROM
value2

value1	IS	NOT
DISTINCT	FROM
value2

profit	IS	NOT	NULL

profit1	IS	DISTINCT	FROM	profit2

profit1	IS	NOT	DISTINCT	FROM
profit2

如果具体的值大于等于	value1
且小于等于	value2，返回结果为
真

A	BETWEEN
value1	AND
value2

profit	BETWEEN	1	AND	1000	Date
BETWEEN	'2016-01-01'	AND	'2016-12-
30'

NOT
BETWEEN

如果具体的值大于等于	value1
且小于等于	value2，返回结果为
假

value1	NOT
BETWEEN	value2
AND	value3

profit	NOT	BETWEEN	1	AND	1000
Date	NOT	BETWEEN	'2016-01-01'
AND	'2016-12-30'

string1	是否和	string2	的样式匹
配，其中	string1	和	string2	为字
符串类型

string1	LIKE
string2

name	LIKE	'%frank%'

string1	是否和	string2	的样式不
匹配，其中	string1	和	string2	为
字符串类型

string1	NOT	LIKE
string2	[	ESCAPE
string3	]

name	NOT	LIKE	'%frank%'

string1	是否和	string2	按正则表
达式匹配

string1	SIMILAR
TO	string2

name	SIMILAR	TO	'frank'

string1	是否和	string2	按正则表
达式不匹配

string1	NOT
SIMILAR	TO
string2

name	NOT	SIMILAR	TO	'frank'

LIKE

NOT	LIKE

SIMILAR
TO

NOT
SIMILAR
TO

已知限制

目前	SIMILAR	TO	ESCAPE	语法，仅限于支持在	SQL	语句中添加并且击中模型的场景，其他场景如添加可计算
列、推荐等暂不支持。

字符串文字如果包含特殊符号需要转义后再进行对比，转义符号为	 	\		，例如匹配	 	\kylin		时实际需要写作
	\\kylin		。对于	 	SIMILAR	TO		以及	 	NOT	SIMILAR	TO		函数使用的是正则匹配，因此会额外进行一次转义处理。例
如，对于	 	\\\\kylin		来说，使用	 	SIMILAR	TO		函数对比	 	\kylin		以及	 	\\kylin		的结果均是	 	true		。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

464

查询分析

逻辑运算符

本节介绍	Kyligence	Enterprise	支持的逻辑运算符。逻辑命题的值有	TRUE、FALSE	和	UNKNOWN，	以下以	 	boolean
指代一个逻辑命题。

运算符

描述

语法

示例

AND

是否条件1	boolean1	和	条件2	boolean2	都为真

是否条件1	boolean1	或	条件2	boolean2	为真

boolean1	AND
boolean2

Name	='frank'	AND
gender='M'

boolean1	OR
boolean2

Name='frank'	OR
Name='Hentry'

是否	boolean	不为真;	如果	boolean	为	UNKNOWN
则返回	UNKNOWN

NOT	boolean

NOT	(NAME	='frank')

OR

NOT

IS	FALSE

是否	boolean	为假;	如果	boolean	为	UNKNOWN	则
返回假

boolean	IS
FALSE

Name	='frank'	IS
FALSE

IS	NOT
FALSE

IS	TRUE

IS	NOT
TRUE

是否	boolean	不为假;	如果	boolean	为	UNKNOWN
则返回真

boolean	IS	NOT
FALSE

Name	='frank'	IS	NOT
FALSE

是否	boolean	为真;	如果	boolean	为	UNKNOWN	则
返回假

boolean	IS
TRUE

Name	='frank'	IS
TRUE

是否	boolean	不为真;	如果	boolean	为	UNKNOWN
则返回真

boolean	IS	NOT
TRUE

Name	='frank'	IS	NOT
TRUE

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

465

查询分析

算术运算符

运算符

描述

语法

示例

+

-

*

/

加号

减号

乘号

除号

A+B

A-B

A*B

A/B

Cost+Profit

Revenue-Cost

Unit_Price*Quantity

Total_Sale/Quantity

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

466

查询分析

字符串运算符

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

467

查询分析

函数

Kyligence	Enterprise	支持如下函数：

算术函数

字符串函数

日期函数

条件函数

类型转换函数

窗口函数

分组函数

交集函数

聚合函数

其他函数

Bitmap	函数

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

468

查询分析

算术函数

语法

说明

示例

基
本
查
询

查
询
下
压

可
定
义
为
可
计
算
列

可
推
荐
为
可
计
算
列

可
用
于
模
型
数
据
筛
选

ABS(numeric)

CEIL(numeric)

FLOOR(numeric)

MOD(numeric1,
numeric2)

SQRT(numeric)

CBRT(numeric)

返回数字（numeric）
的绝对值

返回大于或者等于数字
（numeric）的最小整
数

返回小于或者等于数字
（numeric）的最大整
数

返回被除数
（numeric1）与除数
（numeric2）相除的余
数，	结果的符号与被
除数相同

返回数字（numeric）
的平方根

返回数字（numeric）
的立方根

	ABS(-2)		=	2

✔

✔

✔

✔

✔

	CEIL(-2.2)		=	-2

✔

✔

✔

✔

✔

	FLOOR(-2.2)		=	-3

✔

✔

✔

✔

✔

	MOD(-3,	2)		=	-1

✔

✔

	SQRT(16)		=	4.0

✔

✔

✔

✔

✔

	CBRT(27.0)		=	3.0

✔

✔

✔

✔

✔

HYPOT(numeric1,
numeric2)

返回

	HYPOT(3,	4)		=	5.0

✔

✔

✔

✔

✔

LN(numeric)

返回数字（numeric）
的自然对数

	LN(2)		=
0.6931471805599453

✔

✔

✔

✔

✔

LOG(base,	numeric)

LOG10(numeric)

LOG1P(numeric)

LOG2(numeric)

返回数字（numeric）
以（base）为底的对数

返回数字（numeric）
以	10	为底的对数

返回数字（numeric	+
1）的自然对数

返回数字（numeric）
以	2	为底的对数

	LOG(10,	100)		=	2.0

✔

✔

✔

✔

✔

	LOG10(100)		=	2.0

✔

✔

✔

✔

✔

	LOG1P(0)		=	0.0

✔

✔

✔

✔

✔

	LOG2(2)		=	1.0

✔

✔

✔

✔

✔

EXP(numeric)

返回	e	的	numeric	次幂

	EXP(1)		=
2.718281828459045

✔

✔

✔

✔

✔

EXPM1(numeric)

POWER(numeric1,
numeric2)

RAND([seed])

返回	e	的	numeric	次幂
减	1

返回数字（numeric1）
乘幂（numeric2）的结
果

生成一个大于等于	0	且
小于	1	的随机实数
-	 	seed	： 	可选		用于初
始化随机数生成器

	EXPM1(0)		=	0.0

✔

✔

✔

✔

✔

	POWER(5,2)		=	25.0

✔

✔

✔

✔

✔

	RAND(15)		=
0.45951471073476047

✔

✔

469

查询分析

COS(numeric)

SIN(numeric)

TAN(numeric)

COT(numeric)

ACOS(numeric)

ASIN(numeric)

ATAN(numeric)

始化随机数生成器

返回数字（numeric）
的余弦

	COS(5)		=
0.28366218546322625

✔

✔

✔

✔

✔

返回数字（numeric）
的正弦

	SIN(5)		=
-0.9589242746631385

✔

✔

✔

✔

✔

返回数字（numeric）
的正切

	TAN(5)		=
-3.380515006246586

✔

✔

✔

✔

✔

返回数字（numeric）
的余切

	COT(5)		=
-0.2958129155327455

✔

✔

✔

✔

✔

返回数字（numeric）
的反余弦

	ACOS(0.8)		=
0.6435011087932843

✔

✔

✔

✔

✔

返回数字（numeric）
的反正弦

	ASIN(0.8)		=
0.9272952180016123

✔

✔

✔

✔

✔

返回数字（numeric）
的反正切

	ATAN(0.8)		=
0.6747409422235527

✔

✔

✔

✔

✔

ATAN2(numeric1,
numeric2)

返回坐标	(numeric1,
numeric2)	的反正切

	ATAN2(0.2,	0.8)		=
0.24497866312686414

✔

✔

✔

✔

✔

COSH(numeric)

SINH(numeric)

TANH(numeric)

返回数字（numeric）
的双曲余弦值

返回数字（numeric）
的双曲正弦值

返回数字（numeric）
的双曲正切值

	COSH(0)		=	1.0

✔

✔

✔

✔

✔

	SINH(0)		=	0.0

✔

✔

✔

✔

✔

	TANH(0)		=	0.0

✔

✔

✔

✔

✔

DEGREES(numeric)

将弧度（numeric）转
成角度

	DEGREES(5)		=
286.4788975654116

✔

✔

✔

✔

✔

PI

返回无限接近	π	的数字

	PI		=
3.141592653589793

✔

✔

RADIANS(numeric)

将角度（numeric）转
成弧度

	RADIANS(90)		=
1.5707963267948966

✔

✔

✔

✔

✔

BROUND(numeric1,
numeric2)

将数字（numeric1）取
数字（numeric2）位小
数，向下取整

	BROUND(8.23,	1)		=
8.2
	BROUND(2.5)		=	2.0

ROUND(numeric1,
numeric2)

将数字（numeric1）取
数字（numeric2）位小
数，四舍五入

	ROUND(2.53,	1)		=
2.5
	ROUND(2.5)		=	3

✔

✔

✔

✔

✔

✔

✔

✔

✔

✔

RINT(numeric)

SIGN(numeric)

CONV(numeric,
from_base,	to_base)

CONV(string,
from_base,	to_base)

TRUNCATE(numeric1,
numeric2)

返回值最接近数字
（numeric）的整数，
double	类型。

返回数字（numeric）
的符号

返回数字（numeric）
从基数（from_base）
转换到基数
（to_base）的结果

返回字符串类型的数字
（string）从基数
（from_base）转换到
基数（to_base）的结
果

将数字（numeric1）截
断到数字（numeric2，

	RINT(12.3456)		=
12.0

✔

✔

✔

✔

✔

	SIGN(-5)		=	-1.0

✔

✔

✔

✔

✔

	CONV(-10,	16,	-10)
=	-16

✔

✔

✔

✔

✔

	CONV('100',	2,	10)
=	4

✔

✔

✔

✔

✔

	TRUNCATE(5.55555,2)
=	5.55

✔

✔

✔

✔

✔

470

查询分析

numeric2)

断到数字（numeric2，
默认为	0）

=	5.55

✔

✔

✔

✔

✔

FACTORIAL(numeric)

返回数字（numeric）
的阶乘，如果数字
（numeric）大于	20，
则返回	null

注意：

	FACTORIAL(5)		=	120

✔

✔

✔

✔

✔

	POWER		函数中的参数如果是类似于	 	CAST(2	AS	DOUBLE)		这种常量转换，可能会导致可计算列推荐失败。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

471

查询分析

字符串函数

语法

说明

示例

CHAR_LENGTH(string)

CHARACTER_LENGTH(string)

UPPER(string)

LOWER(string)

POSITION(string1	IN	string2)

返回字符串
（string）长度

返回字符串
（string）长度

返回字符串
（string）为全大写

返回字符串
（string）为全小写

返回字符串
（string1）在字符串
（string2）中的位置

TRIM(	{	BOTH	\	LEADING\
TRAILING	}	string1	FROM
string2)

去掉字符串
（string2）两端／开
头／结尾最长的一个
字符串（string1）

OVERLAY(string1	PLACING
string2	FROM	integer	[	FOR
integer2	])

SUBSTRING(string	FROM
integer)

SUBSTRING(string	FROM
integer1	FOR	integer2)

INITCAP(string)

REPLACE(string,	search,
replacement)

从字符串（string1）
第	integer	位开始将
字符替换为字符串
（string2）

从第	integer	位开
始，取字符串
（string）的部分字
符串

从第	integer1	位开
始，取字符串
（string）中的
integer2	个字符

将字符串（string）
的第一个字母的大写
字母,并将其余的字
母转换成小写，最终
以字符串返回。

将字符串（string）
中的字符串
（search）	替换为字
符串
（replacement）。目
前不支持使用正则表
达式进行字符串匹配

基
本
查
询

✔

✔

✔

✔

✔

✔

✔

✔

✔

✔

	CHAR_LENGTH('Kyligence')		=	9

	CHARACTER_LENGTH('Kyligence')		=	9

	UPPER('Kyligence')		=	KYLIGENCE

	LOWER('Kyligence')		=	kyligence

	POSITION('Kyli'	IN	'Kyligence')		=	1

示例	1： 	TRIM(BOTH	'6'	FROM
'666Kyligence66')
=	Kyligence

示例	2： 	TRIM(LEADING	'6'	FROM
'666Kyligence66')
=	Kyligence66

示例	3： 	TRIM(TRAILING	'6'	FROM
'666Kyligence66')
=	666Kyligence

	OVERLAY('666'	placing	'KYLIGENCE'	FROM	2
for	2)
=	6KYLIGENCE

	SUBSTRING('Kyligence'	FROM	5)
=	gence

	SUBSTRING('Kyligence'	from	5	for	2)
=	ge

	INITCAP('kyligence')
=	Kyligence

	REPLACE('Kyligence','Kyli','Kyliiiiiii')
=	Kyliiiiiiigence

✔

472

查询分析

达式进行字符串匹配
的用法。

BASE64(bin)

将二进制参数转换为
base64	字符串

	BASE64('Spark	SQL')
=	U3BhcmsgU1FM

✔

DECODE(bin,	charset)

ENCODE(string,	charset)

FIND_IN_SET(str,	str_array)

将第一个参数	 	bin
以指定的字符集
	charset		解码。如
果任何一个参数为

null，返回	null。可
选字符集为：
'US_ASCII',	'ISO-
8859-1',	'UTF-8',
'UTF-16BE',	'UTF-
16LE',	'UTF-16'

将第一个参数
	string		以指定的字
符集	 	charset		编
码。如果任一参数为
null，返回	null。可
选字符集为：
'US_ASCII',	'ISO-
8859-1',	'UTF-8',
'UTF-16BE',	'UTF-
16LE',	'UTF-16'

返回	 	str		在
	str_array		中第一
次出现的位
置。 	str_array		为
用逗号分隔的字符
串，如果	 	str	包含
逗号或者在
	str_array		没有发
现	 	str	，则返回
0。若任何参数为
null，返回	null。

	DECODE(ENCODE('abc',	'utf-8'),	'utf-8')
=	abc

✔

	ENCODE('abc',	'utf-8')
=	abc

	FIND_IN_SET('ab','abc,b,ab,c,def')
=	3

LCASE(string)

返回字符串	 	string
的小写形式

	LCASE('SparkSql')
=	sparksql

LEVENSHTEIN(str,	str)

返回两个字符串的编
辑距离

	LEVENSHTEIN('kitten',	'sitting')
=	3

LOCATE(substr,	str[,	pos])

LPAD(str,	len,	pad)

RPAD(str,	len,	pad)

RTRIM(trimStr,	str)

	LOCATE('bar',	'foobarbar')
=	4
	LOCATE('bar',	'foobarbar',	5)
=7

	LPAD('hi',	5,	'??')
=	???hi
	LPAD('hi',	5)
=				hi

	RPAD('hi',	5,	'??')
=	hi???
	RPAD('hi',	5)
=	hi

	RTRIM('KR',	'SPARK')
=	SPA

返回字符串	 	substr
在字符串	 	str		的位
置	 	pos		后第一次出
现的位置

将	 	str		左侧用字符
串	 	pad		填充，直到
长度为	 	len	，如果
	str	长度超过
	len	，会缩短到
	len		个字符

在	 	str		的右侧使用
	pad		填充至长
度 	len	，如果
	str	长度超过
	len	，会缩短到
	len		个字符

从 	str	中右侧去
掉 	trimStr	包含的字
符

将自然语言文本处理
为句子和单词。以数

✔

✔

✔

✔

✔

✔

✔

✔

473

✔

✔

✔

✔

✔

✔

✔

✔

✔

✔

✔

查询分析

SENTENCES(str)

SUBSTRING_INDEX(str,

delim,	count)

UCASE(str)

UNBASE64(str)

ASCII(str)

CHR(str)

SPACE(len)

SPLIT_PART(str,	separator,
index)

为句子和单词。以数
组的形式返回每个句
子中的单词组成的数
组。

使用	 	delim		分割
	str	，返回	 	count
个分割的子串组成的
字符串。如果

	count		为正，返回
左侧的字符串，如果
	count		为负，返回
右侧的字符串

	SENTENCES('Hi	there!	Good	morning.')
=	[["Hi","there"],["Good","morning"]]

	SUBSTRING_INDEX('www.apache.org',	'.',
1)

=	www

返回字符串	 	str		的
大写形式

	UCASE('SparkSql')
=	SPARKSQL

将	base64	的字符串
转换为二进制

	UNBASE64('U3BhcmsgU1FM')
=	Spark	SQL

将字符转换为	ascii
code

将	ascii	code	转换为
对应字符

生成 	len	个连续空
格

将 	str	按 	separator
分割开，然后取
第 	index	个分割后的
部分,	 	index	从	1	开
始，可以为负数，负
数代表从后往前数

	ASCII('a')		=	97

	CHR(97)		=	a

space(2)	=

	split_part('a-b-c',	'-',	1)		=	a,
	split_part('a-b-c',	'-',	-1)		=	c,

concat(any,	[any]*)

将任意类型的多个数
据连接为一个字符串

	concat('Kyli',	'gence',	111)	=
Kyligence111

repeat(str,n)

left(str,n)

REGEXP_EXTRACT(str,
pattern,	index)

将 	str	重复 	n	次返
回。模型查询
时， 	str		支持传入
常量、列和表达
式， 	n	只支持传入
常量

将 	str	从左边开始
的 	n	个字符返回。
模型查询时， 	str
支持传入常量、
列， 	n		只支持传入
常量，当

将字符串	 	str		按照
正则表达式
	pattern		的规则拆
分，返回	 	index		指
定的字符串。
	str		为要匹配的字
符串表达式；
	pattern		必须是一
个	Java	正则表达
式，可以包含多个
组。
	index		指要提取哪
个正则表达式组。为
大于或等于	0	的整
数，默认值为	1。
	index		为	0	则表示

	repeat('kylin',2)		=	'kylinkylin'

	left('kylin',2)		=	'ky'

	regexp_extract('foothebar',	'foo(.*?)
(bar)',	2)		=	'bar'

✔

474

查询分析

	index		为	0	则表示
匹配整个正则表达
式。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

475

查询分析

日期函数

语法

描述

示例

CURRENT_DATE

CURRENT_TIMESTAMP

EXTRACT(timeUnit	FROM	datetime)

返回当前时区的日期。
返回类型为	DATE	格式

返回当前时区的时间戳。
返回类型为	TIMESTAMP	格式

提取返回日期中的指定项。
	timeunit		可以为：
	year	、 	month	、 	day	、
	hour	、 	minute	、 	second

FLOOR(datetime	TO	timeUnit)

CEIL(datetime	TO	timeUnit)

YEAR(date)

QUARTER(date)

以	 	timeUnit		为单位对	 	datetime		向下取
整。
	timeunit		可以为：
	year	、 	quarter	、 	month	、 	week	、 	day	、
	hour	、 	minute	、 	second

以	 	timeUnit		为单位对	 	datetime		向上取
整。
	timeunit		可以为：
	year	、
	quarter	、 	month	、 	week	、 	day	、
	hour	、 	minute	、 	second

返回日期中的年份，
等同于 	EXTRACT(YEAR	FROM	date)	。

	YEAR(date	'2019-01-02')
=	2019

返回日期中的季度，

等同于 	EXTRACT(QUARTER	FROM	date)	。返回值
为	1	到	4	的整数

NOW(date)

返回发送查询的当前时间戳

MONTH(date)

WEEK(date)

DAYOFYEAR(date)

DAYOFMONTH(date)

返回日期中的月份，
等同于	 	EXTRACT(MONTH	FROM	date)	。
返回值为	1	到	12	的整数

返回日期中对应的星期，
等同于	 	EXTRACT(WEEK	FROM	date)	。
返回值为	1	到	53	的整数

返回日期对应年的天数，
等同于	 	EXTRACT(DOY	FROM	date)	。
返回值为	1	到	366	的整数

返回日期对应月的天数，
等同于 	EXTRACT(DAY	FROM	date)	。
返回值为	1	到	31

返回日期对应的星期几，

	CURRENT_DATE
=	2018-10-10

	CURRENT_TIMESTAMP
=	2022-07-19	10:24:44.708

	EXTRACT(minute	FROM	timestamp'2018-
10-10	11:47:16')
=	47

示例	1：
	FLOOR(timestamp'2018-10-10
11:47:16'	TO	year)
=	2018-01-01	00:00:00
示例	2：
	FLOOR(timestamp'2018-10-10
11:47:16'	TO	minute)
=	2018-10-10	11:47:00

示例	1：
	CEIL(timestamp'2018-10-10	11:47:16'
TO	year)
=	2019-01-01	00:00:00
示例	2：
	CEIL(timestamp'2018-10-10	11:47:16'
TO	minute)
=	2018-10-10	11:48:00

	QUARTER(date	'2019-01-02')
=	1

	NOW()
=	2019-09-24	17:19:09.932

	MONTH(date	'2019-01-02')
=	1

	WEEK(date	'2019-01-02')
=	1

	DAYOFYEAR(date	'2019-10-03')
=	276

	DAYOFMONTH(date	'2019-10-03')
=	3

476

查询分析

DAYOFWEEK(date)

HOUR(date)

MINUTE(date)

SECOND(date)

TIMESTAMPADD(timeUnit,	integer,
datetime)

返回日期对应的星期几，
等同于	 	EXTRACT(DOW	FROM	date)	。
返回值为	1	到	7	的整数

	DAYOFWEEK(date	'2019-10-03')
=	5

返回日期中的小时数，
等同于	 	EXTRACT(HOUR	FROM	date)	。返回值为
0	到	23	的整数

	HOUR(timestamp	'2019-01-02
14:01:50')
=	14

返回日期中的分钟数，
等同于	 	EXTRACT(MINUTE	FROM	date)	。

	MINUTE(timestamp	'2019-01-02
14:01:50')

返回结果为	0	到	59	的整数

=	1

返回日期中的秒数，
等同于	 	EXTRACT(SECOND	FROM	date)	。
返回结果为	0	到	59	的整数

返回添加了	 	timeUnit		为单位的时间
	integer		后的日期	 	datetime	，
等同于	 	datetime	+	INTERVAL	'integer'
timeUnit		。
返回类型为	 	datetime
入参	 	datetime	为日期或字符串类型

	SECOND(timestamp	'2019-01-02
14:01:50')
=	50

示例	1：获取一个月后的日期时
间 	TIMESTAMPADD(month,	1,
CURRENT_DATE)
=	2018-11-10

示例	2：获取本月最后一天
	TIMESTAMPADD(day,	-(extract(day
from	CURRENT_DATE)),
timestampadd(month,1,CURRENT_DATE))
=	2018-10-31

	TIMESTAMPDIFF(day,	date'2018-01-
01',	date	'2018-10-10')
=	282

	TRUNC(date	'2009-02-12',	'MM')
=	2009-02-01

	ADD_MONTHS(date	'2016-08-31',	1)
=	2016-09-30

	DATE_ADD(date	'2016-07-30',	1)
=	2016-07-31

	DATE_SUB(date	'2016-07-30',	1)
=	2016-07-29

	FROM_UNIXTIME(0,	'yyyy-MM-dd
HH:mm:ss')
=	1970-01-01	00:00:00

	FROM_UTC_TIMESTAMP(TIMESTAMP'2015-
03-02	06:05:00',	'America/Toronto')
=	2015-03-02	01:05:00.0

TIMESTAMPDIFF(timeUnit,	datetime,
datetime2)

TRUNC(date,	fmt)

以	 	timeUnit		为单位返回	 	datetime		和
	datetime2		的时间差，
等同于	 	(datetime2	-	datetime)/timeUnit
入参	 	datetime		和	 	datetime2		为日期或字符
串类型

返回将	 	date		截断到	 	fmt		指定的单位后的
日期， 	fmt		可以取集合	["year",	"yyyy",	"yy",
"mon",	"month",	"mm"]	中的值

ADD_MONTHS(start_date,	num_months)

返回	 	start_date		后	 	num_months	个月的日期

DATE_ADD(start_date,	num_days)

返回	 	start_date		后	 	num_days	天的日期

DATE_SUB(start_date,	num_days)

返回	 	start_date		前	 	num_days	天的日期

FROM_UNIXTIME(unix_time,	format)

将	 	unix_time		时间转换为	 	format	格式

FROM_UTC_TIMESTAMP(timestamp,
timezone)

假设给定时间戳	 	timestamp		为	UTC	时间，
将其转换为给定时区	 	timezone		的时间戳

MONTHS_BETWEEN(timestamp1,
timestamp2)

返回	 	timestamp1		和	 	timestamp2	月份差，如
果	 	timestamp1		晚于	 	timestamp2	，则结果为
正。以	31	天为基数进行计算。如果两个时间
都是月份中的同一天，或者都是月份中的最
后一天，则返回整数

	MONTHS_BETWEEN('1997-02-28
10:30:00',	'1996-10-30')
=	3.94959677

TO_UTC_TIMESTAMP(timestamp,
timezone)

假设给定时间戳 	timestamp	为给定时
区 	timezone	的时间，将其转换为	UTC	时间
戳

	TO_UTC_TIMESTAMP('2016-08-31',
'Asia/Seoul')
=	2016-08-30	15:00:00

UNIX_TIMESTAMP(datetime,	format)

返回	 	1970-01-01	08:00:00		到	 	datetime		的
秒数，指定	 	datetime		为	 	format		格式

	UNIX_TIMESTAMP('2016-04-08
09:00:00',	'yyyy-MM-dd	HH:mm:ss')
=	1460106000

DATEDIFF(endDate,	startDate)

返回	 	endDate		和	 	startDate		之间的日期差
值，参数为日期或字符串类型

DATEDIFF(date	'2022-02-03',	date
'2022-02-01')
=	2
DATEDIFF('2022-02-03',	'2022-02-01')
=	2

477

查询分析

DATE_TRUNC(unit,	timestamp)

返回将时间戳	 	timestamp		截断到	 	unit		指定
的单位后的日期， 	unit		可以取集合	["year",
"yyyy",	"yy",	"quarter",	"mon",	"month",	"mm",
"week",	"day",	"dd",	"hour",	"minute",	"second",
"millisecond",	"microsecond"]	中的值
入参	 	timestamp	为时间戳或字符串类型

将时间戳转换为 	fmt	格式的字符串。 	expr

SELECT	DATE_TRUNC('second',
TIMESTAMP	'2020-04-30
04:05:06.789')
=	2020-04-30	04:05:06

	date_format('2016-04-08',	'y')

DATE_FORMAT(expr,	fmt)

为	 	DATE	、 	TIMESTAMP		或有效日期时间格式
的字符串， 	fmt		为所需格式的字符串表达式

=2016

_YMDINT_BETWEEN(date_expression1,
date_expression2)

注意：

参数中的日期格式为	 	yyyy-MM-dd	，传回一个
数字，代表	 	date_expression1		和
	date_expression2		之间的差距。
回复值的格式为 	YYYYMMDD	，其中 	YYYY	代表
年数， 	MM	代表月数， 	DD	代表天数。
回复值月数和日数各固定占2位，年数为实际
差值，不向前补位

	_ymdint_between(1990-04-30,	2003-
02-05)
=	120906，表示12年9个月又6天

从	4.6.23.0	版本开始，SQL	中使用	 	CURRENT_DATE	、 	CURRENT_TIMESTAMP	，不加引号时视作函数，加引号时视作列/字
段。在	4.6.23.0	版本之前，加不加引号都视作函数。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

478

查询分析

条件函数

语法

说明

示例

CASE	value
WHEN	value1
THEN	result1
WHEN	valueN
THEN	resultN
ELSE	resultZ	END

CASE	WHEN
condition1	THEN
result1WHEN
conditionN	THEN
resultN	ELSE
resultZ	END

简单	CASE	语句

搜索	CASE	语句

	CASE	OPS_REGION	WHEN
'Beijing'	THEN	'BJ'	WHEN
'Shanghai'	THEN	'SH'WHEN
'Hongkong'	THEN	'HK'	END	FROM
KYLIN_SALES
=	HK	SH	BJ

	CASE	WHEN
OPS_REGION='Beijing'THEN	'BJ'
WHEN	OPS_REGION='Shanghai'
THEN	'SH'	WHEN
OPS_REGION='Hongkong'	THEN
'HK'	END	FROM	KYLIN_SALES
=	HK	SH	BJ

NULLIF(value,
value)

如果两个值相同返回	NULL，否
则返回第一个值

	NULLIF(5,5)
=	null

COALESCE(value,
value	[,	value	]*)

返回第一个不为	NULL	的值

	COALESCE(NULL,NULL,5)
=	5

基
本
查
询

查
询
下
压

可
定
义
为
可
计
算
列

✔

✔

✔

✔

✔

✔

✔

✔

✔

✔

✔

✔

IFNULL(value1,
value2)

如果	value1	为	NULL，返回
value2;	否则返回	value1

	IFNULL('kyligence','apache')
=	'kyligence'

✔

✔

✔

ISNULL(value)

如果	value	为	NULL，返回	true;
否则返回	false

	ISNULL('kyligence')
=	false

✔

✔

✔

NVL(value1,
value2)

如果	value1	为	NULL，返回
value2;	否则返回	value1。value1,
value2	的数据类型必须相同。在
Kyligence	Enterprise	4.2.3	版本之
前，要使用该函数需要在
kylin.properties	中加入配
置： 	kylin.query.calcite.extras-
props.FUN=standard,oracle	。

	NVL('kyligence','apache')
=	'kyligence'

✔

✔

✔

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

479

查询分析

类型转换函数

基
本
查
询

查
询
下
压

可
定
义
为
可
计
算
列

可
推
荐
为
可
计
算
列

可
用
于
模
型
数
据
筛
选

✔

✔

✔

✔

✔

✔

✔

✔

语法

说明

示例

将	 	value		强制
转换成 	type	的
类型，现在支持
的类型

将字符串转换为
日期类型，
等同于
CAST(string	AS
date)

将字符串转换为
日期时间类型，
等同于
CAST(string	AS
timestamp)

示例	1：
将时间类型强制转换成字
符串类型
	CAST(CURRENT_DATE	as
varchar)
=	2018-10-10

示例	1：
	DATE'2018-10-10'
=	2018-10-10

示例	2：返回字符串对应
的日期的月份（与日期函
数	MONTH()	配合使用）
	MONTH(DATE'2018-10-10')
=	10

示例	1：
	TIMESTAMP'2018-10-10
15:57:07
=	2018-10-10	15:57:07

示例	2：返回字符串对应
的日期时间的秒（与日期
函数	SECOND()	配合使
用）
	SECOND(TIMESTAMP'2018-
10-10	15:57:07')
=	7

CAST(value	AS	type)

DATE<String>

TIMESTAMP<String>

注意：

1.	 现仅支持如下类型的转换： 	char	, 	varchar	,	 	boolean	,	 	int	,	 	integer	,	 	tinyint	,	 	smallint	,	 	bigint	,

	float	,	 	double	,	 	decimal	,	 	numeric	,	 	date	,	 	time	,	 	timestamp

2.	 但是现在不支持从	 	bigint		转换到	 	timestamp		类型
3.	 若从	 	char		转换到	 	int		类型， 	char		类型中非数值，则会返回空值
4.	 当其他数据类型转换为	 	char(n)	/ 	varchar(n)		时，长度	n	不会生效

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

480

查询分析

窗口函数

用户可以使用窗口函数来完成更多复杂的查询、简化查询过程并且获得更好的统计结果。

注意：窗口函数目前无法被定义及自动推荐为可计算列。

函数的语法结构

function(value)	OVER	window
window	的组成

partition	by：分组子句，表示窗口函数的计算范围。
order	by:	排序子句，表示分组后，组内数据的排序方式。
rows	/	range：窗口子句，表示分组后，在组内确定一个滑动的数据窗口，窗口函数将根据该窗口包含的数据范
围进行运算。常写为	(rows	|	range)	between	(unbounded	|	[num])	preceding	and	([num]	preceding	|	current	row	|

(unbounded	|	[num])	following)

rows	是物理窗口，即根据	order	by	子句排序后的结果，选取当前行序号的固定前后记录。该子句的结果与
当前行的值无关，只与排序后的行号有关。

例如	sum(column	A)	rows	between	1	preceding	and	2	following	，如当前行的	column	A	排序后序号是3，
那么这个子句的定义就会选择分区中	column	A	序号落在2至5区间的记录。

range	是逻辑窗口，即以当前行对应值为基准，选取当前行对应值的固定前后记录。该子句的结果与排序
后的行号无关，与行的值有关。

例如	sum(column	A)	range	between	1	preceding	and	2	following	，如当前行的	column	A	字段值是3，那么
这个子句的定义就会选择分区中	column	A	字段值落在2至5区间的记录。

如果指定了	order	by	子句，没有指定窗口子句，则默认窗口子句等同于	range	between	unbounded	preceding
and	current	row，代表窗口选取的记录为第一行至当前行。

窗口函数示例

接下来我们以样例数据集中的表	P_LINEORDER	为例，介绍每个函数的使用方法。表中字段及其意义可参考样例数据
集。

ROW_NUMBER

函数说明：ROW_NUMBER()	OVER	window，返回当前行在其分区中的位置，序号不重复。

RANK

函数说明：RANK()	OVER	window，返回当前行在其分区中的位置，可能会有序号空隙。

DENSE_RANK

函数说明：DENSE_RANK()	OVER	window，返回当前行在其分区中的位置，无序号空隙。

查询示例	使用	RANK()	和	DENSE_RANK()	与	ROW_NUMBER()	在同一条查询语句中，查询每个买家购买商品数最
少的前五个订单，进行对比，查询如下：

SELECT	*

FROM	(

SELECT

				ROW_NUMBER()	OVER	w	AS	ROW_NUM,

				RANK()	OVER	w	AS	_RANK,

				DENSE_RANK()	OVER	w	AS	D_RANK,

				LO_ORDERKEY,

				LO_CUSTKEY,

				LO_QUANTITY,

				LO_PARTKEY

481

查询分析

				FROM	SSB.P_LINEORDER

				WINDOW	w	AS	(PARTITION	BY	LO_CUSTKEY	ORDER	BY	LO_QUANTITY)

				)	T

WHERE	ROW_NUM	<=	5;

返回示例

返回结果说明	​	对于买家	'1'	，购买商品个数为1的订单有四条，使用三种排名函数对比如下：

使用	row_number	函数，购买商品个数为1的订单序号为1，2，3，4，购买商品个数为2的订单序号为5。
使用	rank	函数，购买商品个数为1的订单序号为1，1，1，1，购买商品个数为2的订单序号为5（此处存在序号
空隙）。

使用	dense_rank	函数，购买商品个数为1的订单序号为1，1，1，1，购买商品个数为2的订单序号为2（此处不
存在序号空隙）。

NTILE

函数说明：NTILE(value)	OVER	window，将分区内的有序数据尽量按	value	等分，返回组号。

查询示例

将每个买家的订单按照购买商品个数等分为3组，为了完整展示搜索结果，选取商品个数大于等于48的订单进行分
组。

SELECT

				NTILE(3)	OVER	w	AS	N_3,

				LO_ORDERKEY,

				LO_CUSTKEY,

				LO_QUANTITY,

				LO_PARTKEY

FROM	SSB.P_LINEORDER

WHERE	LO_QUANTITY	>=	48

WINDOW	w	AS	(PARTITION	BY	LO_CUSTKEY	ORDER	BY	LO_QUANTITY);

482

查询分析

返回示例

FIRST_VALUE

函数说明：FIRST_VALUE(value)	OVER	window，返回窗口框架中计算行中第一行的值。

LAST_VALUE

函数说明：LAST_VALUE(value)	OVER	window，返回窗口框架中计算行中最后一行的值	。

查询示例

查询按照日期排序的总价格最高的第一个订单和最后一个订单。

SELECT

				FIRST_VALUE(TOTAL1)	OVER	W	AS	FIRST_VALUE_A,

				LAST_VALUE(TOTAL1)	OVER	W	AS	LAST_VALUE_A,

				TOTAL1,

				LO_ORDERDATE

FROM	(

				SELECT

								SUM(LO_ORDTOTALPRICE)	AS	TOTAL1,

								LO_ORDERDATE

				FROM	SSB.P_LINEORDER

				GROUP	BY	LO_ORDERDATE

				)	T	WINDOW	W	AS	(

								ORDER	BY	LO_ORDERDATE	ROWS	BETWEEN	UNBOUNDED	PRECEDING	AND	UNBOUNDED	FOLLOWING

								)

ORDER	BY	LO_ORDERDATE	DESC

483

查询分析

返回示例

LEAD()

函数说明：LEAD(value,	offset,	default)	OVER	window，返回分区内当前行向后的偏移行。其中	value	表示作为
当前值的字段，offset	代表需要基于当前值往后查找	offset	行的数据，default	代表当没有符合条件的值时默认
返回的值，不填写默认返回	null。

LAG()

函数说明：LAG(value,	offset,	default)	OVER	window，返回分区内当前行向前的偏移行。其中	value	表示作为当
前值的字段，offset	代表需要基于当前值往前查找	offset	行的数据，default	代表当没有符合条件的值时默认返
回的值，不填写默认返回	null。

查询示例	查询当前订单和上一个订单、下一个订单的时间。

SELECT

		LO_ORDERKEY,

		LO_CUSTKEY,

		LO_QUANTITY,

		LO_ORDERDATE,

		LEAD(LO_ORDERDATE,	1)	OVER	W	AS	NEXT_DT,

		LAG(LO_ORDERDATE,	1)	OVER	W	AS	LAST_DT

FROM	SSB.P_LINEORDER

WINDOW	W	AS	(PARTITION	BY	LO_CUSTKEY	ORDER	BY	LO_ORDERDATE)

484

查询分析

返回示例

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

485

查询分析

分组函数

在查询语句中经常要使用各种分组汇总，ROLLUP，	CUBE，	GROUPING	SETS	函数就是常用的分组汇总方式。

注意：分组函数暂时无法被定义及推荐为可计算列。

GROUPING	SETS(expression)

在一个结果集中，您有时候需要对列	A，列	B	分别做聚合，同时也要对这两列一起做聚合，实现方法往往是使用多个
UNION	ALL	语句连接起不同的聚合结果。	GROUPING	SETS	子句对聚合查询同时采用不同的分组设置，它可以代替多
个	UNION	ALL	语句，使	SQL	语句更为便捷高效。

函数说明

GROUPING	SETS	子句用于	GROUP	BY	子句后，expression	内填写需要进行分组的维度的组合，例如
GROUPING	SETS((	A	,	B	),	(C)	,	())，意为同时展示对列	A	和列	B	做分组聚合，对列	C	做分组聚合和无分组聚
合三种分组设置的结果。

查询示例

SELECT

				LO_CUSTKEY,

				LO_ORDERKEY,

				SUM(LO_ORDTOTALPRICE)	AS	PRICE

FROM	SSB.P_LINEORDER

GROUP	BY

				GROUPING	SETS((LO_CUSTKEY,LO_ORDERKEY),(LO_ORDERKEY),());

返回示例

GROUPING	SETS	函数

486

查询分析

CUBE(expression)	和	ROLLUP(expression)

CUBE	和	ROLLUP	可以认为是	GROUPING	SETS	的特殊情况。

函数说明

CUBE	会对所有的列进行分组统计，最后给出合计。expression	内使用的列会被解析为所有可能的组合形式。
例如	GROUP	BY	CUBE(a,	b,	c)	等价于	GOUPING	SETS((a,b,c),(a,b),(a,c),(b,c),(a),(b),(c),())

ROLLUP	会先对第一个列进行分组统计，最后给出合计。	expression	内使用的列会被解析为包含层级的组合形
式。例如	GROUP	BY	ROLLUP(a,	b,	c)	等价于	GROUPING	SETS((a,b,c),(a,b),(a),	())

查询示例（此处以	ROLLUP	为例）

SELECT

		LO_CUSTKEY,

		LO_ORDERKEY,

		SUM(LO_ORDTOTALPRICE)	AS	PRICE

FROM	SSB.P_LINEORDER

GROUP	BY

		ROLLUP(LO_CUSTKEY,	LO_ORDERKEY);

返回示例

ROLLUP	函数

GROUPING(expression)

在使用常用的分组函数	ROLLUP，	CUBE，	GROUPING	SETS	创建的结果列表中，会使用	NULL	作为占位符，所以您
在查看结果时，无法区分	NULL	是占位符还是实际的原始数据中的	NULL。

通过	GROUPING	函数可将占位符	NULL	与原始数据中的	NULL	区分开来。

487

查询分析

函数说明

分组函数中涉及的分组列均可用于	GROUPING	函数的	expression	中。如果该函数的返回值为0，意味着	对应行
中分组列下显示的	NULL	来自实际的原始数据，如果返回1，则意味着对应行中分组列下显示的	NULL	是分组
函数产生的的占位符。

查询示例

SELECT

				LO_CUSTKEY,

				LO_ORDERKEY,

				SUM(LO_ORDTOTALPRICE)	AS	PRICE,

				GROUPING(LO_CUSTKEY)	AS	GC,

				GROUPING(LO_ORDERKEY)	AS	GM

FROM	SSB.P_LINEORDER

GROUP	BY

				GROUPING	SETS((LO_CUSTKEY,LO_ORDERKEY),(LO_ORDERKEY),());

返回示例：

可以看到第一行中两列	GROUPING	函数产生的结果都为1，说明该行	LO_CUSTKEY	和	LO_ORDERKEY	两列中的
NULL	都是由于	GROUPING	SETS	函数产生的占位符。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

488

查询分析

交集函数

用户可以使用交集函数计算两个数据集的交集的值。通常情况下，它们具有一些相同的维度（城市，类别等）和一个变

化的维度（日期等），可以用来计算留存率和转化率。

Kyligence	Enterprise	支持如下交集函数。

INTERSECT_COUNT

说明

返回不同条件下多个结果集交集的去重计数

语法

参数

	intersect_count(column_to_count,	column_to_filter,	filter_value_list)

	column_to_count		指向用于统计去重计数的列，这个列必须已经被添加为精确去重的度量
	column_to_filter		指向可变的维度
	filter_value_list		数组形式，指向可变维度中的值；当	 	column_to_filter		为	varchar	类型时，数组中单个元
素可以映射多个值，默认使用'|'分割，可以使用	 	kylin.query.intersect.separator		配置分隔符，可以取值	 	|
或者	 	,	，默认为	 	|	，仅支持在	 	kylin.properties		文件中配置（目前该参数不支持使用子查询的结果作为参
数使用）。

注意：	当可变维度的数据类型不是	varchar	或	integer	时， 	filter_value_list	中的值需要做显式的类型转换，例
如：	 	select	intersect_count(column_to_count,	column_to_filter,	array[cast(3.53	as	double),	cast(5.79	as
double)])	from	TEST_TABLE		或	 	select	intersect_count(column_to_count,	column_to_filter,	array[TIMESTAMP'2012-
01-02	11:23:45',	TIMESTAMP'2012-01-01	11:23:45'])	from	TEST_TABLE;

查询示例	1

以	Kyligence	Enterprise	的样例数据集为例，事实表	 	KYLIN_SALES		模拟了在线交易数据的记录表。	以下查询语句可
以获得有多少比例的卖家能在新年假期阶段（2012.01.01-2012.01.03）进行持续的在线交易。

select	LSTG_FORMAT_NAME,

intersect_count(SELLER_ID,	PART_DT,	array[date'2012-01-01'])	as	first_day,

intersect_count(SELLER_ID,	PART_DT,	array[date'2012-01-02'])	as	second_day,

intersect_count(SELLER_ID,	PART_DT,	array[date'2012-01-03'])	as	third_day,

intersect_count(SELLER_ID,	PART_DT,	array[date'2012-01-01',date'2012-01-02'])	as	retention_oneday,

intersect_count(SELLER_ID,	PART_DT,	array[date'2012-01-01',date'2012-01-02',date'2012-01-03'])	as	retention

_twoday

from	KYLIN_SALES

where	PART_DT	in	(date'2012-01-01',date'2012-01-02',date'2012-01-03')

group	by	LSTG_FORMAT_NAME

返回示例	1

489

查询分析

结果表示没有卖家在新年阶段进行持续的在线交易。

查询示例	2（column	to	filter	为	varchar	类型时，单元素映射多个值）

		select

		intersect_count(SELLER_ID,	LSTG_FORMAT_NAME,	array['FP-GTC|FP-non	GTC|Others',	'Others'])	as	test_column

		from	kylin_sales

返回示例	2

INTERSECT_VALUE

说明

返回不同条件下多个结果集交集的去重结果。若返回结果较大，可能会导致分析页面浏览器崩溃。

语法

490

查询分析

参数

	intersect_value(column_to_count,	column_to_filter,	filter_value_list)

	column_to_count		指向用于统计去重数据的列，这个列必须已经被添加为精确去重的度量。	仅当类型为
tinyint、smallint或integer且模型重写设置 	kylin.query.skip-encode-integer-enabled=true	时，返回结果为该列
真实值，否则为该列编码后的值。

	column_to_filter		指向可变的维度
	filter_value_list		数组形式，指向可变维度中的值；当	 	column_to_filter		为	varchar	类型时，数组中单个元
素可以映射多个值，默认使用'|'分割，可以使用	 	kylin.query.intersect.separator		配置分隔符，可以取值	 	|
或者	 	,	，默认为	 	|	，仅支持在	 	kylin.properties		文件中配置（目前该参数不支持使用子查询的结果作为参
数使用）。

注意：	当可变维度的数据类型不是	varchar	或	integer	时， 	filter_value_list	中的值需要做显式的类型转换，例
如：	 	select	intersect_value(column_to_count,	column_to_filter,	array[cast(3.53	as	double),	cast(5.79	as
double)])	from	TEST_TABLE		或	 	select	intersect_value(column_to_count,	column_to_filter,	array[TIMESTAMP'2012-
01-02	11:23:45',	TIMESTAMP'2012-01-01	11:23:45'])	from	TEST_TABLE;

查询示例	1

事实表	 	KYLIN_SALES_TEST		模拟了在线交易数据的记录表，其中	SELLER_ID	字段的类型为	integer。
以下查询语句可以获得哪些卖家能在新年假期阶段（2012.01.01-2012.01.03）进行持续的在线交易。

select	LSTG_FORMAT_NAME,

intersect_value(SELLER_ID,	PART_DT,	array[date'2012-01-01'])	as	first_day,

intersect_value(SELLER_ID,	PART_DT,	array[date'2012-01-02'])	as	second_day,

intersect_value(SELLER_ID,	PART_DT,	array[date'2012-01-03'])	as	third_day,

intersect_value(SELLER_ID,	PART_DT,	array[date'2012-01-01',date'2012-01-02'])	as	retention_oneday,

intersect_value(SELLER_ID,	PART_DT,	array[date'2012-01-01',date'2012-01-02',date'2012-01-03'])	as	retention

_twoday

from	KYLIN_SALES

where	PART_DT	in	(date'2012-01-01',date'2012-01-02',date'2012-01-03')

group	by	LSTG_FORMAT_NAME

返回示例	1

结果表示在新年阶段进行持续的在线交易的卖家	id	的集合，以数组的形式展示。

查询示例	2（column	to	filter	为	varchar	类型时，单元素映射多个值）

491

查询分析

select

intersect_value(SELLER_ID,	LSTG_FORMAT_NAME,	array['FP-GTC|FP-non	GTC|Others',	'Others'])	as	test_column

from	kylin_sales

返回示例	2

INTERSECT_COUNT_V2

说明

语法

参数

返回不同条件下多个结果集交集的去重计数，条件支持正则表达式匹配。

	intersect_count_v2(column_to_count,	column_to_filter,	filter_value_list,	filter_type)

	column_to_count		指向用于统计去重计数的列，这个列必须已经被添加为精确去重的度量
	column_to_filter		指向可变的维度
	filter_value_list		数组形式，指向可变维度中的值
	filter_type		类型为	String，标识	filter	的方式，目前有两个可选值	“RAWSTRING”	和	"REGEXP"，当参数值
为	"RAWSTRING"	时的过滤方式为精确过滤，当	 	column_to_filter		为	varchar	类型时，数组中单个元素可以
映射多个值，默认使用'|'分割，可以使用	 	kylin.query.intersect.separator		配置分隔符，可以取值	 	|		或者
	,	，默认为	 	|	，仅支持在	 	kylin.properties		文件中配置（目前该参数不支持使用子查询的结果作为参数使
用）。当参数值为	"REGEXP"	时，过滤方式为正则匹配，只会过滤	column_to_filter	中能够匹配	filter_value_list
中的正则表达式的值。

注意：	当	filter_type	为	"RAWSTRING"	，并且可变维度的数据类型不是	varchar	或	integer
时， 	filter_value_list	中的值需要做显式的类型转换，例如：	 	select	intersect_count_v2(column_to_count,
column_to_filter,	array[cast(3.53	as	double),	cast(5.79	as	double)],	'RAWSTRING')	from	TEST_TABLE		或
	select	intersect_count_v2(column_to_count,	column_to_filter,	array[TIMESTAMP'2012-01-02	11:23:45',

TIMESTAMP'2012-01-01	11:23:45'],	'RAWSTRING')	from	TEST_TABLE;

查询示例	1

	select	intersect_count_v2(

						LSTG_SITE_ID,	LSTG_FORMAT_NAME,

						array['FP.*GTC',	'Other.*'],	'REGEXP')

			from	kylin_sales

492

查询分析

返回示例	1

INTERSECT_VALUE_V2

说明

返回不同条件下多个结果集交集的去重结果。若返回结果较大，可能会导致分析页面浏览器崩溃。条件支持正

则表达式匹配。

语法

参数

	intersect_value_v2(column_to_count,	column_to_filter,	filter_value_list,	filter_type)

	column_to_count		指向用于统计去重计数的列，这个列必须已经被添加为精确去重的度量。	仅当类型为
tinyint、smallint或integer且模型重写设置 	kylin.query.skip-encode-integer-enabled=true	时，返回结果为该列
真实值，否则为该列编码后的值。

	column_to_filter		指向可变的维度
	filter_value_list		数组形式，指向可变维度中的值
	filter_type		类型为	String，标识	filter	的方式，目前有两个可选值	“RAWSTRING”	和	"REGEXP"，当参数值
为	"RAWSTRING"	时的过滤方式为精确过滤，当	 	column_to_filter		为	varchar	类型时，数组中单个元素可以
映射多个值，默认使用'|'分割，可以使用	 	kylin.query.intersect.separator		配置分隔符，可以取值	 	|		或者
	,	，默认为	 	|	，仅支持在	 	kylin.properties		文件中配置（目前该参数不支持使用子查询的结果作为参数使
用）。当参数值为	"REGEXP"	时，过滤方式为正则匹配，只会过滤	column_to_filter	中能够匹配	filter_value_list
中的正则表达式的值。

注意：	当	filter_type	为	"RAWSTRING"	，并且可变维度的数据类型不是	varchar	或	integer
时， 	filter_value_list	中的值需要做显式的类型转换，例如：	 	select	intersect_value_v2(column_to_count,
column_to_filter,	array[cast(3.53	as	double),	cast(5.79	as	double)],	'RAWSTRING')	from	TEST_TABLE		或
	select	intersect_value_v2(column_to_count,	column_to_filter,	array[TIMESTAMP'2012-01-02	11:23:45',

TIMESTAMP'2012-01-01	11:23:45'],	'RAWSTRING')	from	TEST_TABLE;

查询示例	1

	select	intersect_value_v2(

						LSTG_SITE_ID,	LSTG_FORMAT_NAME,

						array['FP.*GTC',	'Other.*'],	'REGEXP')

			from	kylin_sales

493

查询分析

返回示例	1

已知限制

上述函数均不支持查询下压

上述函数均不支持明细索引回答(即使开启开关	kylin.query.use-tableindex-answer-non-raw-query	=	true)

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

494

查询分析

聚合函数

可定义
为可计
算列

可推荐
为可计
算列

语法

说明

示例

AVG(numeric)

返回所有输入值中类型为
numeric	的算术平均值

SUM(numeric)

返回所有输入值中类型为
numeric	的总计值

MAX(value)

返回所有输入值中	value
的最大值

MIN(value)

返回所有输入值中	value
的最小值

	SELECT	AVG(PRICE)	FROM
KYLIN_SALES
=	49.23855638491023

	SELECT	SUM(PRICE)	FROM
KYLIN_SALES
=	244075.5240

	SELECT	MAX(PRICE)	FROM
KYLIN_SALES
=	99.9865

	SELECT	MIN(PRICE)	FROM
KYLIN_SALES
=	0.0008

COUNT(value)

返回所有输入值中	value
不为	NULL	的输入行的
数量

	SELECT	count(PRICE)
FROM	KYLIN_SALES
=	4957

COUNT(*)

返回输入的行数

CORR(value1,
value2)

返回输入的两列的相关性

	SELECT	COUNT(*)	FROM
KYLIN_COUNTRY
=	244

	SELECT
CORR(ITEM_COUNT,	PRICE)
FROM	KYLIN_SALES
=	0.1278

基
本
查
询

查
询
下
压

✔

✔

✔

✔

✔

✔

✔

✔

✔

✔

✔

✔

✔

✔

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

495

查询分析

Bitmap	函数

用户可以使用	Bitmap	函数，从多个模型中分别计算出去重后的	bitmap	结果，再对子查询的	bitmap	做交集操作。

Kyligence	Enterprise	支持如下	Bitmap	函数。

前提条件

您的	Kyligence	Enterprise	版本高于或等于	4.1.6。

BITMAP_UUID

说明

返回一个String，指向一个	bitmap	序列化后的二进制数据。该	bitmap	包含去重后的结果集，可供其他函数进行
二次计算。

语法

参数

	bitmap_uuid(column_to_count)

	column_to_count		指向用于统计去重数据的列，这个列必须已经被添加为精确去重的度量。

查询示例	1

	select	bitmap_uuid(SELLER_ID)	from	KYLIN_SALES	where	PART_DT=date'2012-01-01'

返回示例	1

结果返回一个	String	，指向一个用户不可见的	bitmap	序列化后的二进制数据，表示元旦在线交易的卖家	id	的集
合，供其他函数进行二次计算。

INTERSECT_BITMAP_UUID

说明

返回一个String，指向一个	bitmap	序列化后的二进制数据。该	bitmap	包含多个去重结果集的交集，供其他函数
进行二次计算。

496

查询分析

语法

参数

	intersect_bitmap_uuid(column_to_count,	column_to_filter,	filter_value_list)

	column_to_count		指向用于统计去重数据的列，这个列必须已经被添加为精确去重的度量。
	column_to_filter		指向可变的维度
	filter_value_list		数组形式，指向可变维度中的值；当	 	column_to_filter		为	varchar	类型时，数组中单个元
素可以映射多个值，默认使用'|'分割，可以使用	 	kylin.query.intersect.separator		配置分隔符，可以取值	 	|
或者	 	,	，默认为	 	|	，仅支持在	 	kylin.properties		文件中配置（目前该参数不支持使用子查询的结果作为参
数使用）。

注意：	当可变维度的数据类型不是	varchar	或	integer	时， 	filter_value_list	中的值需要做显式的类型转换，例
如：	 	select	intersect_bitmap_uuid(column_to_count,	column_to_filter,	array[cast(3.53	as	double),	cast(5.79
as	double)])	from	TEST_TABLE		或	 	select	intersect_bitmap_uuid(column_to_count,	column_to_filter,
array[TIMESTAMP'2012-01-02	11:23:45',	TIMESTAMP'2012-01-01	11:23:45'])	from	TEST_TABLE;

查询示例	1

LSTG_FORMAT_NAME	字段类型为	VARCHAR(4096)，作为可变维度列。

select	intersect_bitmap_uuid(

								SELLER_ID,	LSTG_FORMAT_NAME,

								array['FP-GTC|FP-non	GTC',	'Others'])

				from	KYLIN_SALES

返回示例	1

结果返回一个	String	，指向一个用户不可见的	bitmap	序列化后的二进制数据，表示同时进行过类型为	'FP-GTC'	和
'Others'，或	'FP-non	GTC'	和	'Others'	两种交易的用户的去重合集。该去重合集可供其他函数进行二次计算。

INTERSECT_BITMAP_UUID_V2

说明

返回一个String，指向一个	bitmap	序列化后的二进制数据。该	bitmap	包含多个去重结果集的交集，供其他函数
进行二次计算。

语法

497

查询分析

参数

	intersect_bitmap_uuid_v2(column_to_count,	column_to_filter,	filter_value_list,	filter_type)

	column_to_count		指向用于统计去重数据的列，这个列必须已经被添加为精确去重的度量。
	column_to_filter		指向可变的维度
	filter_value_list		数组形式，指向可变维度中的值
	filter_type		类型为	String，标识	filter	的方式，目前有两个可选值	“RAWSTRING”	和	"REGEXP"，当参数值
为	"RAWSTRING"	时的过滤方式为精确过滤，当	 	column_to_filter		为	varchar	类型时，数组中单个元素可以
映射多个值，默认使用'|'分割，可以使用	 	kylin.query.intersect.separator		配置分隔符，可以取值	 	|		或者
	,	，默认为	 	|	，仅支持在	 	kylin.properties		文件中配置（目前该参数不支持使用子查询的结果作为参数使
用）。当参数值为	"REGEXP"	时，过滤方式为正则匹配，只会过滤	column_to_filter	中能够匹配	filter_value_list
中的正则表达式的值。

注意：	当	filter_type	为	"RAWSTRING"	，并且可变维度的数据类型不是	varchar	或	integer
时， 	filter_value_list	中的值需要做显式的类型转换，例如：	 	select
intersect_bitmap_uuid_v2(column_to_count,	column_to_filter,	array[cast(3.53	as	double),	cast(5.79	as	double)],
'RAWSTRING')	from	TEST_TABLE		或	 	select	intersect_bitmap_uuid_v2(column_to_count,	column_to_filter,
array[TIMESTAMP'2012-01-02	11:23:45',	TIMESTAMP'2012-01-01	11:23:45'],	'RAWSTRING')	from	TEST_TABLE;

查询示例	1

LSTG_FORMAT_NAME	字段类型为	VARCHAR(4096)，作为可变维度列。

select	intersect_bitmap_uuid_v2(

								SELLER_ID,	LSTG_FORMAT_NAME,

								array['FP.*GTC',	'Other.*'],	'REGEXP')

				from	KYLIN_SALES

返回示例	1

结果返回一个	String	，指向一个用户不可见的	bitmap	序列化后的二进制数据，正则表达式能匹配到	'FP-GTC',	'FP-
non	GTC'	和	'Others'，表示进行过类型为	'FP-GTC'	和	'Others'，或	'FP-non	GTC'	和	'Others'	两种交易的用户的去重合
集。该去重合集可供其他函数进行二次计算。

INTERSECT_COUNT_BY_COL

说明

498

查询分析

语法

参数

对	bitmap	序列化后的二进制数据进行反序列化，	然后再进行交集操作，返回去重计数。

	intersect_count_by_col(Array[t1.c1,t2.c2	...])

	t1.c1,	t2.c2	...		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。能返回该类型的函数
有，bitmap_uuid	和	intersect_bitmap_uuid	和	intersect_bitmap_uuid_v2。

查询示例	1

select	intersect_count_by_col(Array[t1.a1,t2.a2])	from

				(select	bitmap_uuid(SELLER_ID)	as	a1

								from	KYLIN_SALES)	t1,

				(select	intersect_bitmap_uuid(

								SELLER_ID,	LSTG_FORMAT_NAME,

								array['FP-GTC|FP-non	GTC',	'Others'])	as	a2

from	KYLIN_SALES)	t2

返回示例	1

子查询中的两个bitmap	，分别由	bitmap_uuid	和	intersect_bitmap_uuid	提供。intersect_count_by_col	函数对这两个
bitmap	进行交集操作，并返回去重计数。

INTERSECT_BITMAP_UUID_COUNT

说明

语法

参数

通过	uuid	，对	bitmap	序列化后的二进制数据进行反序列化，然后再进行交集操作，返回去重计数。

	intersect_bitmap_uuid_count(uuid)

	uuid		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。

查询示例	1

select	intersect_bitmap_uuid_count(uuid)

from	(

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['1-URGENT'])	as	uuid

from	SSB.LINEORDER

499

查询分析

union

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['2-HIGH'])	as	uuid

from	SSB.LINEORDER

)

返回示例	1

子查询中的两个bitmap	，分别由两个	intersect_bitmap_uuid	提供。intersect_bitmap_uuid_count	函数对这两个	bitmap
进行交集操作，并返回去重计数。

INTERSECT_BITMAP_UUID_VALUE_ALL

说明

通过	uuid	，对	bitmap	序列化后的二进制数据进行反序列化，然后再进行交集操作，返回去重结果。

语法

参数

	intersect_bitmap_uuid_value_all(uuid)

	uuid		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。

查询示例	1

select	intersect_bitmap_uuid_value_all(uuid)

from	(

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['1-URGENT'])	as	uuid

from	SSB.LINEORDER

union

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['2-HIGH'])	as	uuid

from	SSB.LINEORDER

)

返回示例	1

子查询中的两个bitmap	，分别由两个	intersect_bitmap_uuid	提供。intersect_bitmap_uuid_value_all	函数对这两个
bitmap	进行交集操作，并返回去重结果。

500

查询分析

INTERSECT_BITMAP_UUID_VALUE

说明

通过	uuid	，对	bitmap	序列化后的二进制数据进行反序列化，然后再进行交集操作，根据	limit	、offset	返回去
重结果。

语法

参数

	intersect_bitmap_uuid_value(uuid,limit,offset)

	uuid		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。
	limit		返回结果集大小限制。
	offset		返回结果集的偏移量。

查询示例	1

select	intersect_bitmap_uuid_value(uuid,10,10)

from	(

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['1-URGENT'])	as	uuid

from	SSB.LINEORDER

union

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['2-HIGH'])	as	uuid

from	SSB.LINEORDER

)

返回示例	1

子查询中的两个bitmap	，分别由两个	intersect_bitmap_uuid	提供。intersect_bitmap_uuid_value	函数对这两个	bitmap
进行交集操作，并返回去重结果。

INTERSECT_BITMAP_UUID_DISTINCT

说明

通过	uuid	，对	bitmap	序列化后的二进制数据进行反序列化，然后再进行交集操作，返回一个String，指向一个
bitmap	序列化后的二进制数据。

语法

参数

	intersect_bitmap_uuid_distinct(uuid)

	uuid		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。

查询示例	1

select	intersect_bitmap_uuid_distinct(uuid)

from	(

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['1-URGENT'])	as	uuid

from	SSB.LINEORDER

501

查询分析

union

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['2-HIGH'])	as	uuid

from	SSB.LINEORDER

)

返回示例	1

子查询中的两个bitmap	，分别由两个	intersect_bitmap_uuid	提供。intersect_bitmap_uuid_distinct	函数对这两个	bitmap
进行交集操作，并返回一个String，指向一个	bitmap	序列化后的二进制数据。

UNION_BITMAP_UUID_COUNT

说明

语法

参数

通过	uuid	，对	bitmap	序列化后的二进制数据进行反序列化，然后再进行并集操作，返回去重计数。

	union_bitmap_uuid_count(uuid)

	uuid		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。

查询示例	1

select	union_bitmap_uuid_count(uuid)

from	(

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['1-URGENT'])	as	uuid

from	SSB.LINEORDER

union

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['2-HIGH'])	as	uuid

from	SSB.LINEORDER

)

返回示例	1

子查询中的两个bitmap	，分别由两个	intersect_bitmap_uuid	提供。union_bitmap_uuid_count	函数对这两个	bitmap	进
行并集操作，并返回去重计数。

502

查询分析

UNION_BITMAP_UUID_VALUE_ALL

说明

语法

参数

通过	uuid	，对	bitmap	序列化后的二进制数据进行反序列化，然后再进行并集操作，返回去重结果。

	union_bitmap_uuid_value_all(uuid)

	uuid		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。

查询示例	1

select	union_bitmap_uuid_value_all(uuid)

from	(

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['1-URGENT'])	as	uuid

from	SSB.LINEORDER

union

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['2-HIGH'])	as	uuid

from	SSB.LINEORDER

)

返回示例	1

子查询中的两个bitmap	，分别由两个	intersect_bitmap_uuid	提供。union_bitmap_uuid_value_all	函数对这两个	bitmap
进行并集操作，并返回去重结果。

UNION_BITMAP_UUID_VALUE

说明

语法

参数

通过	uuid	，对	bitmap	序列化后的二进制数据进行反序列化，然后再进行并集操作，根据	limit	、offset	返回去
重结果。

	union_bitmap_uuid_value(uuid,limit,offset)

	uuid		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。
	limit		返回结果集大小限制。
	offset		返回结果集的偏移量。

查询示例	1

select	union_bitmap_uuid_value(uuid,10,10)

from	(

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['1-URGENT'])	as	uuid

from	SSB.LINEORDER

union

503

查询分析

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['2-HIGH'])	as	uuid

from	SSB.LINEORDER

)

返回示例	1

子查询中的两个bitmap	，分别由两个	intersect_bitmap_uuid	提供。union_bitmap_uuid_value	函数对这两个	bitmap	进
行并集操作，并返回去重结果。

UNION_BITMAP_UUID_DISTINCT

说明

通过	uuid	，对	bitmap	序列化后的二进制数据进行反序列化，然后再进行并集操作，返回一个String，指向一个
bitmap	序列化后的二进制数据。

语法

参数

	union_bitmap_uuid_distinct(uuid)

	uuid		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。

查询示例	1

select	union_bitmap_uuid_distinct(uuid)

from	(

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['1-URGENT'])	as	uuid

from	SSB.LINEORDER

union

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['2-HIGH'])	as	uuid

from	SSB.LINEORDER

)

返回示例	1

子查询中的两个bitmap	，分别由两个	intersect_bitmap_uuid	提供。union_bitmap_uuid_distinct	函数对这两个	bitmap
进行并集操作，并返回一个String，指向一个	bitmap	序列化后的二进制数据。

504

查询分析

BITMAP_UUID_TO_ARRAY

说明

通过	uuid	，对	bitmap	序列化后的二进制数据进行反序列化，返回数组。

语法

参数

	bitmap_uuid_to_array(uuid)

	uuid		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。

查询示例	1

select	bitmap_uuid_to_array(uuid)

from	(

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['1-URGENT'])	as	uuid

from	SSB.LINEORDER

union

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['2-HIGH'])	as	uuid

from	SSB.LINEORDER

)

返回示例	1

子查询中的两个bitmap	，分别由两个	intersect_bitmap_uuid	提供。union_bitmap_uuid_distinct	函数对这两个	bitmap
进行反序列化操作，并返回数组。

SUBTRACT_BITMAP_UUID_COUNT

说明

通过	uuid	，对	bitmap	序列化后的二进制数据进行反序列化，然后再进行差集操作，返回去重计数。

语法

参数

	subtract_bitmap_uuid_count(uuid1,uuid2)

	uuid1		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。
	uuid2		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。

查询示例	1

select	subtract_bitmap_uuid_count(uuid1,uuid2)

from	(

select

intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['1-URGENT'])	as	uuid1,

intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['2-HIGH'])	as	uuid2

from	SSB.LINEORDER

505

查询分析

)

返回示例	1

子查询中的两个bitmap	，分别由两个	intersect_bitmap_uuid	提供。subtract_bitmap_uuid_count	函数对这两个	bitmap
进行差集操作，并返回去重计数。

SUBTRACT_BITMAP_UUID_VALUE_ALL

说明

通过	uuid	，对	bitmap	序列化后的二进制数据进行反序列化，然后再进行差集操作，返回去重结果。

语法

参数

	subtract_bitmap_uuid_value_all(uuid1,uuid2)

	uuid1		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。
	uuid2		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。

查询示例	1

select	subtract_bitmap_uuid_value_all(uuid1,uuid2)

from	(

select

intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['1-URGENT'])	as	uuid1,

intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['2-HIGH'])	as	uuid2

from	SSB.LINEORDER

)

返回示例	1

子查询中的两个bitmap	，分别由两个	intersect_bitmap_uuid	提供。subtract_bitmap_uuid_value_all	函数对这两个
bitmap	进行差集操作，并返回去重结果。

SUBTRACT_BITMAP_UUID_VALUE

506

查询分析

说明

通过	uuid	，对	bitmap	序列化后的二进制数据进行反序列化，然后再进行差集操作，根据	limit	、offset	返回去
重结果。

语法

参数

	subtract_bitmap_uuid_value(uuid1,uuid2,limit,offset)

	uuid1		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。
	uuid2		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。
	limit		返回结果集大小限制。
	offset		返回结果集的偏移量。

查询示例	1

select	subtract_bitmap_uuid_value(uuid1,uuid2,10,10)

from	(

select

intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['1-URGENT'])	as	uuid1,

intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['2-HIGH'])	as	uuid2

from	SSB.LINEORDER

)

返回示例	1

子查询中的两个bitmap	，分别由两个	intersect_bitmap_uuid	提供。subtract_bitmap_uuid_value	函数对这两个	bitmap
进行差集操作，并返回去重结果。

SUBTRACT_BITMAP_UUID_DISTINCT

说明

通过	uuid	，对	bitmap	序列化后的二进制数据进行反序列化，然后再进行差集操作，返回一个String，指向一个
bitmap	序列化后的二进制数据。

语法

参数

	subtract_bitmap_uuid_distinct(uuid1,uuid2)

	uuid1		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。
	uuid2		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。

查询示例	1

select	subtract_bitmap_uuid_distinct(uuid1,uuid2)

from	(

select

intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['1-URGENT'])	as	uuid1,

intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['2-HIGH'])	as	uuid2

507

查询分析

from	SSB.LINEORDER

)

返回示例	1

子查询中的两个bitmap	，分别由两个	intersect_bitmap_uuid	提供。subtract_bitmap_uuid_distinct	函数对这两个	bitmap
进行差集操作，并返回一个String，指向一个	bitmap	序列化后的二进制数据。

已知限制

上述函数均不支持查询下压

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

508

查询分析

其他函数

UUID()

MONOTONICALLY_INCREASING_ID()

EXPLODE(array)

SIZE(expr)

语法

描述

示例

可
定
义
为
可
计
算
列

基
本
查
询

查
询
下
压

✔

返回通用唯
一识别码
（UUID）。
该值以规范
的	36	个字
符的字符串
形式返回

返回单调递
增的最大	64
位的整数。
生成的	ID
单调递增且
唯一，但不
连续。

返回array展
开后的多行
数据。array
中的每一个
元素都会对
应一行

expr	必须为
array	或者
map	类型，
返回	array
或	map	中包
含的元素个
数。

	UUID()
=	46707d92-02f4-4817-8116-
a4c3b23e6266

	MONOTONICALLY_INCREASING_ID()
=	1111111

✔

✔

	EXPLODE(array[1,	2,	3])
=
1
2
3

✔

	SIZE(array(1,	2,	3))
=
3

✔

✔

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

509

查询分析

为查询指定模型优先级

当一个项目中有多个就绪的模型时，系统会自动为每个查询选择最合适的模型。但有时，用户希望直接指定查询要击中

的模型，而不是由系统自动判断。这时就可以使用在	SQL	中添加相关	hint。

Model	Priorities	Hint

语法

SELECT	/*+	MODEL_PRIORITY(model1,	model2)	*/	col1,	col2	from	....

Hint	由	 	/*+		开始	 	*/		结束，必须放在	 	SELECT		的后面， 	SELECT		和	 	/*+	..	*/		中间不能有其他的内容。

该语法从	Kyligence	Enterprise	4.2.4	开始支持。Model	Priorities	Hint	使用	 	/*+	MODEL_PRIORITY(model1,	model2)	*/		指定，
MODEL_PRIORITY	接受任意个数的模型名作为参数，模型的优先级从左到右递减，没有出现在	MODEL_PRIORITY	中
的模型优先级最低。	当前	model	priority	hint	会对整个查询生效，如果	SQL	中出现多个	model	priority	hint	以第一个为
准。

在模型匹配过程中，如果同时有多个模型可以回答该查询，则会使用	MODEL_PRIORITY	中定义的模型优先级，优先选
取优先级高的模型作为查询对象。

从	4.6.22.0	版本，如果需要仅通过指定特定模型回答查询，可添加配置项	 	kylin.query.use-only-in-priorities=true		并
使用	 	MODEL_PRIORITY(...)		指定模型，其优先级从左到右递减，当	 	MODEL_PRIORITY(...)		中包含的模型无法回答查询
时，查询将下压。该参数可以在项目级生效，默认值为	 	false	。

例子

SELECT	/*+	MODEL_PRIORITY(model1,	model2)	*/	col1,	col2	from	table;

若该查询可以同时被	model1	和	model2	回答，根据	SQL	中的	MODEL_PRIORITY	,	Kyligence	Enterprise	会选择	model1	回
答该查询。

兼容	Kyligence	Enterprise	3	的语法

Kyligence	Enterprise	4	对于	Kyligence	Enterprise	3	在SQL中指定模型优先级的语法做了兼容，语法如下

--	CubePriority(model1,model2)

select	....	from	...

注释中关键字	CubePriority	后的括弧内包含一串由	,	分割的	Model	名字，它们的优先级从高到低排列。以上例，假如
Model1	和	Model2	都能满足查询，那么系统将优先使用	Model1。

注意

1.	 CubePriority	关键字大小写敏感，且其后的括号前后内不能有多余的空格。不准确的拼写将导致系统无法识别该注

释选项。

2.	 如果	SQL	中包含多条	CubePriority	注释选项，则只有第一条会生效，其他的会被忽略。
3.	 如果同时存在	 	MODEL_PRIORITY		和	 	CubePriority	，则只有	 	MODEL_PRIORITY		会生效

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

510

查询历史

查询历史

您在	Kyligence	Enterprise	中执行的所有查询分析都会保存在查询历史中，您可以通过导航栏查询	->	查询历史查看相关
信息。此界面保存了查询的基本信息，如查询时间、SQL	语句、查询用户等，可以帮助您记录查询行为，以及更好地管
理或优化模型。本节我们为您介绍查询历史界面的内容。

准备工作

1.	 在介绍查询历史界面之前，我们建议您先执行几条查询语句，这样更有助于您阅读下文的介绍。

2.	 下文我们以快速开始章节中建立的模型为例，介绍查询历史界面。在快速指南章节完成后且监控	->	任务界面的任

务也完全执行完毕后，我们可以在查询	->	分析界面执行以下查询语句。

查询	1：查询收入总额。

select	SUM(LO_REVENUE)	as	TOTAL_REVENUE	from	SSB.P_LINEORDER

提示：存在对列	LO_REVENUE	的度量	SUM。

查询	2：查询订单总额。

select	SUM(LO_ORDTOTALPRICE)	from	SSB.P_LINEORDER

提示：不存在对列	LO_ORDTOTALPRICE	的度量	SUM。

查询	3：查询商品名称。

select	P_NAME	from	SSB.P_LINEORDER

提示：这是一个错误查询，因为表	P_LINEORDER	中不存在字段	P_NAME。

查询历史界面

请您进入导航栏查询	->	查询历史界面，在执行过上述	SQL	查询语句之后，您会看到如下内容。

查询历史

图片中的每一行为您的一次历史查询，列的含义如下：

开始时间：提交查询的时间。

用时：执行完成查询所用的时间。如果查询失败，则显示为空。

查询	ID：每条查询对应的唯一	ID	号，这是自动生成的序号。

511

查询历史

SQL：查询的	SQL	语句。

对象：查询击中的查询对象，	有以下类型：	模型名称，HIVE，RDBMS、CONSTANTS，您可在顶部筛选查询对
象：

Hive：表示查询下压至	Hive
RDBMS：表示查询下压至	RDBMS	数据源
CONSTANTS：表示查询常量
模型名称：表示查询击中的模型名称，您可以勾选”全选“表示查看所有击中模型的查询，结果包含只是击中快
照的查询。筛选框中的模型来自模型列表，根据被击中的次数降序排列后仅展示前	100	个模型，您可以在筛选
下拉框首部搜索希望筛选的模型

状态：两种查询状态。击中模型和查询下压的查询显示为成功，语法错误、语法不支持和超时的查询显示为失败。

节点：提交查询的节点的主机名:端口

提交人：提交查询的	Kyligence	Enterprise	用户

操作：下载查询诊断包

当您点击某一条查询左侧的图标，将展示该条查询的执行详情，如下图所示：

查询执行详情

左侧为	SQL	语句，您可以复制粘贴再查询。SQL	语句默认按照输入时的格式展示，如果需要系统自动规范格式，您可
点击重排格式按钮，该功能需要浏览器版本为谷歌	Chrome	74	及以上，Internet	Explorer	浏览器不支持该功能。

右侧的字段含义如下：

查询	ID：每条查询对应的唯一	ID	号，这是自动生成的序号。
用时：执行完成查询所用的时间。如果查询失败，则显示为空。当您在进行慢查询优化时，需要了解查询的具体执

行步骤，定位耗时原因。可将鼠标悬停在响应时间上，以查看当前查询的详细执行步骤及耗时，辅助分析。

对象：查询击中模型将显示模型名称，HIVE	表示查询下压至	Hive，RDBMS	表示查询下压至	RDBMS	数据
源，CONSTANTS	表示查询常量。
击中快照：查询击中快照将显示快照名称

索引	ID：查询击中的索引的	ID。
扫描行数：查询总共扫描行数。

扫描字节：查询总共扫描字节数。

结果行数：查询结果行数。

击中缓存：查询是否击中缓存。

缓存类型：查询击中缓存时，显示击中的缓存类型。 	EHCACHE		代表	EHCACHE	缓存， 	REDIS		代表	REDIS	分布式
缓存。

当您点击某一条查询失败右侧的错误详情，将展示该条查询的异常详情，如下图所示：

512

查询历史

查询异常信息

注意：SQL	未换行时，查询执行详情中仅能看到前	100	行	SQL,	SQL	换行时，详情显示前	2000	个字符.您可以点
击	SQL	语句框内右上角的复制按钮复制完整的	SQL	语句。

Kyligence	Enterprise	使用内置的	RDBMS	数据库保存查询的相关信息，您可以在附录查询历史字段表中查阅所有和查询
历史相关的字段及含义。

查询历史留存

为了保证查询历史的读写性能和数据库稳定性，Kyligence	Enterprise	为查询历史设有默认留存上限：

默认总留存	1000	万条数据，可通过在	 	kylin.properties		中配置	 	kylin.query.queryhistory.max-size		进行调整

其中单个项目最多默认留存	100	万条数据，可通过在	 	kylin.properties		中配置
	kylin.query.queryhistory.project-max-size		进行调整

总留存时间为	30	天，可通过在	 	kylin.properties		中配置	 	kylin.query.queryhistory.survival-time-threshold		进行
调整

导出查询历史

查询历史支持导出为	csv	文件，如下图所示，导出结果为筛选过滤后的数据

导出查询历史

513

查询历史

也可单独将查询历史中的	SQL	导出为	text	文件，如下图所示，导出结果同样为筛选过滤后的数据

导出SQL

查询历史支持配置导出上限，默认值为	10	万条	 	kylin.query.query-history-download-max-size=100000

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

514

查询优化

查询优化

本章将介绍在	Kyligence	Enterprise	中的一些查询优化方法。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

515

查询优化

使用	Left	Join	模型回答等价语义的	Inner	Join	查询

Kyligence	Enterprise	在默认情况下，查询	SQL	中表的关联关系必需与模型中定义事实表和维表的关联关系一致，即
	Left	Join		的模型不能回答	 	Inner	Join		的查询。

但在某些情况下，部分	 	Left	Join		查询在语义上可以等价转化为	 	Inner	Join		查询，因此我们提供了配置参数，可以
允许用户使用	 	Left	Join		的模型回答等价语义的	 	Inner	Join		查询。

配置参数开始生效版本为	Kyligence	Enterprise	4.2.4，此配置为全局配置，默认关闭。

场景一

	[Table	A]	Left	Join	[Table	B]	Inner	Join	[Table	C]		语义等价于	 	[Table	A]	Inner	Join	[Table	B]	Inner	Join	[Table
C]	。

原因是，当	 	Left	Join		之后再做	 	Inner	Join		，与最后一个右表不匹配的行都会被筛除，所以上述两个表达式在语义
上是等价的。

使用	 	kylin.query.join-match-optimization-enabled=true		配置，Kyligence	Enterprise	可以支持	 	Left	Join		的模型回答上
述等价语义的	 	Inner	Join		查询。

举例	1

模型定义为	 	KYLIN_SALES	Left	Join	KYLIN_ACCOUNT	Inner	Join	KYLIN_COUNTRY

有	SQL	如下：

select	kylin_country.name

from	kylin_sales	inner	join	kylin_account	on	kylin_sales.buyer_id	=	kylin_account.account_id

inner	join	kylin_country	on	kylin_account.account_country	=	kylin_country.country

上述模型	可以回答此	SQL。

举例	2

模型定义为	 	[Table	A]	Left	Join	[Table	B]	Left	Join	[Table	C]	Inner	Join	[Table	D]	Left	Join	[Table	E]

有	SQL	如下：	 	[Table	A]	Inner	Join	[Table	B]	Inner	Join	[Table	C]	Inner	Join	[Table	D]	Left	Join	[Table	E]

上述模型	可以回答此	SQL。

场景二

有	SQL	具有如下特征：	 	[Table	A]	Left	Join	[Table	B]		且过滤条件中	 	[Table	B]	的任意列具有非空约束，则该	SQL
语义等价于	 	[Table	A]	Inner	Join	[Table	B]	。

使用	 	kylin.query.join-match-optimization-enabled=true		配置，Kyligence	Enterprise	可以支持	 	Left	Join		的模型回答上
述等价语义的	 	Inner	Join		查询。

其中列具有非空约束需要满足条件：存在	 	isNotNull		类过滤条件， 	isNotNull		对应常见比较运算
符： 	=	， 	<>	， 	>	， 	<	， 	<=	， 	>=	， 	like	， 	in	， 	not	like	， 	not	in	等。

而	 	isNULL		过滤条件则不具备非空约束，例如	 	IS	NULL	。

同时，目前暂不支持	 	IS	DISTINCT	FROM	， 	CASE	WHEN		过滤条件的等价转换，该过滤条件会被自动忽略，见已知限制1。

516

查询优化

举例	1

模型定义为： 	TEST_ACCOUNT	left	join	TEST_ORDER	left	join	TEST_ACCOUNT

有	SQL	如下，可以击中上述模型，因为存在非空约束的过滤条件。

select	SUM(a.ITEM_COUNT)	as	SUM_ITEM_COUNT

from	TEST_KYLIN_FACT	a

left	join	TEST_ORDER	b	on	a.ORDER_ID	=	b.ORDER_ID

inner	join	TEST_ACCOUNT	c	on	b.BUYER_ID	=	c.ACCOUNT_ID

where	c.ACCOUNT_COUNTRY	=	'CN'	and	(c.ACCOUNT_COUNTRY	like	'%US'	or	c.ACCOUNT_COUNTRY	is	null)

举例	2

模型定义为：	 	[Table	A]	inner	join	[Table	B]

有	SQL	如下，可以击中此模型：

A	left	join	B	where	B.nonfk	=	'123'	and	B.col1	in	('ab',	'ac')

A	left	join	B	where	A.col	is	null	and	B.col1	like	'xxx'

A	left	join	B	where	B.col	between	100	and	100000

A	left	join	B	where	A.fk	is	null	and	B.col1	=	'something'

A	left	join	B	where	b.col	=	'something'	and	(b.col	=	'xxx'	or	b.col	is	null)

A	left	join	B	where	abs(b.col)	=	123

A	left	join	B	where	floor(b.col)	=	123

如下SQL无法击中此的模型：

A	left	join	B	where	B.col1	=	'xx'	or	A.col2	=	'yy'

A	left	join	B	where	B.col1	=	'xx'	or	B.col2	is	null

场景三

现在有模型 	[Table	A]	Left	Join	[Table	B]	left	join	[Table	C]	。

如下SQL如下，可以击中此模型：

A	inner	join	B	inner	join	C	where	C.col	=	'abc'

原因是表	C	中的列存在非空约束，因此查询可以等价为：

A	LEFT_OR_INNER	join	B	LEFT_OR_INNER	join	C	where	C.col	=	'abc'

场景三是场景一和场景二的混合。

已知限制

1.	 对于场景二，在非空约束的判断中，暂不支持	 	IS	DISTINCT	FROM	， 	CASE	WHEN		表达式。
2.	 同样对于场景二，在非空约束的判断中，暂不支持聚合函数的非空判断，例如	 	HAVING	SUM(PRICE)	>	0	。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

517

查询优化

查询	Segment	剪枝

从	Kyligence	Enterprise	4.3.2	版本开始，我们支持在构建	Segment	时计算所有维度的维度值范围（最大值和最小值），因
此查询时可以进行	Segment	剪枝，减少	Segment	扫描范围，以优化部分查询性能。

配置

该功能默认为开启状态。正常情况下，用户无需过多关注此功能，极端情况下支持系统级或项目级关闭。

系统级关闭，在	 	$KYLIN_HOME/conf/kylin.properties		中配置参数。项目级关闭，在设置-高级设置-自定义项目配置中添
加配置。

	kylin.storage.columnar.dimension-range-filter-enabled=false

支持衍生维度查询	Segment	剪枝

为了提升剪枝的效果，从	Kyligence	Enterprise	4.6.0	版本开始，当存在匹配到的索引与衍生维度进行join的查询时，我们
支持使用衍生维度的查询过滤条件，结合构建时得到的维度值范围，进一步减少	Segment	扫描范围，并在查询的文件扫
描阶段过滤掉更多的数据。

该功能默认为关闭状态，需要通过添加参数启用该功能，支持系统级配置。

	kylin.storage.columnar.spark-conf.spark.sql.optimizer.runtime.bloomFilter.enabled=true

同时该功能生效有2个额外的条件，衍生维表的大小需要小于阈值，这个阈值默认为 	10M	，这个参数可以配置：

	kylin.storage.columnar.spark-conf.spark.sql.optimizer.runtime.bloomFilter.creationSideThreshold

查询时匹配到索引表的大小需要大于阈值，这个阈值的默认值为 	10G	，这个参数可以配置：

	kylin.storage.columnar.spark-conf.spark.sql.optimizer.runtime.bloomFilter.applicationSideScanSizeThreshold

默认	broadcast	join	时不适用，将这个参数设为 	true	，则	broadcast	join	也可以应用	runtime	filter:

	kylin.storage.columnar.spark-conf.spark.sql.optimizer.runtime.bloomFilter.broadcastJoinCondition.ignored

已知限制

1.	 查询过滤条件中目前只支持	 	=、in、>、>=、<、<=、and、or		的	Segment	剪枝，暂不支持	 	not、is	null	。

2.	 此功能会略微加长构建时间，但相比总构建时长，基本可忽略不计。

3.	 已完成构建的历史数据不会使用到此优化，如果希望历史数据也可以应用此优化，需要刷新	Segment。

4.	 暂不支持多级分区模型。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

518

查询下压

查询下压

本产品内嵌了一个智能查询下压引擎（Smart	Pushdown	Engine），支持	SQL	on	Hadoop	技术--	Spark	SQL。

Kyligence	Enterprise	在必要时可以将模型无法回答的查询语句，路由到查询下压引擎中，由	Spark	SQL	执行。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

519

查询下压

下压至原生	SparkSQL

Kyligence	Enterprise	使用预计算的数据来代替在线计算以实现大数据场景下的亚秒级查询响应。一般来说，	加载过数据
的模型已经可以服务大多数常用查询，但是当您需要执行一些模型无法满足的查询时，Kyligence	Enterprise	会将其路由
到智能查询下压引擎执行，默认的查询下压引擎为	Spark	SQL。

注意：为了保障数据一致性，查询下压不会击中缓存。

查询下压开关

Kyligence	Enterprise	4.x	起默认启用了	Spark	SQL，您在添加过数据源后，即可使用查询下压功能。	Kyligence	Enterprise
5.x	起，如果项目级开启了内表功能，则不再下压至数据源，而由内表回答。

查询下压功能默认为开启状态，如果您需要关闭查询下压，有如下两种方法：

项目级别关闭：如下图所示，点击左侧导航栏设置标签，在基础设置标签下的查询下压设置中可以关闭查询下压引擎。

如果这项配置从未在项目级别做过更改，将会与全局配置保持一致。

项目级别关闭查询下压

实例级别关闭：在配置文件	 	kylin.properties		中修改查询下压的对应配置项	 	kylin.query.pushdown-enabled=true	，将
其修改为	 	kylin.query.pushdown-enabled=false	，并删除这一配置项前的注释符号使其生效。

注意：修改配置文件后需要重启产品使配置生效。

验证查询下压

如果开启了查询下压，则在添加完数据源后，无需构建相应的模型即可使用查询功能。此时您在提交查询时，查询下压

将发挥作用。如果数据源类型为	HIVE，则查询结果会显示为： 	查询对象：HIVE	。

提示：如果查询击中模型，查询执行历史会显示为： 	查询对象：{对应的模型名称}	。

浮点数注意事项

下压查询中，如果有涉及数据源表中	 	float		类型列的过滤条件时，需注意过滤条件中字面量的类型和精度问题:

类型问题：手工指定字面量的数据类型，达成和列类型一致，写成类似	 	'123.4f'		的格式，如

SELECT	*	FROM	table1	WHERE	col1	>	'123.4f'

精度问题：字面量数据勿超过	 	float	/	double		的精度范围

举例来说，数据源表	 	table1		中有列	 	col1		为	 	float		类型，表中数据为：

|-------|

|	col1		|

|-------|

|	1.2			|

|	5.67		|

520

查询下压

|	123.4	|

|	130.1	|

|-------|

与此同时下压查询的	SQL	语句为：

SELECT	*	FROM	table1	WHERE	col1	>	123.4

则对应查询结果会是：

|-------|

|	col1		|

|-------|

|	123.4	|

|	130.1	|

|-------|

可以看到虽然在	 	WHERE		过滤条件中使用了大于号（ 	>	），但	 	123.4		这行也被查询出来了。

造成该结果的原因是由于该过滤条件两侧数据类型不同，命中了	Spark	优化器规则导致：

其中	 	col1		为	 	float		类型，字面量	 	123.4		默认为	 	double		类型；

而	Spark	优化器规则会将该过滤条件进行如下转换（注意转换后的	 	>=		号）：

cast(col1	to	double)	>	123.4		===>		col1	>=	cast(123.4	to	float)

从而导致	 	123.4		被查询出来。

因此，需要手工指定字面量的数据类型，正确的下压查询语句应为：

SELECT	*	FROM	table1	WHERE	col1	>	'123.4f'

查询出的结果也就正常了：

|-------|

|	col1		|

|-------|

|	130.1	|

|-------|

此外，关于字面量的精度问题，同样以上述情况为例，下压查询语句：

SELECT	*	FROM	table1	WHERE	col1	>	'123.3999f'

可以获得正确的查询结果：

|-------|

|	col1		|

|-------|

|	123.4	|

|	130.1	|

|-------|

而当精度超过相应数据类型范围时，结果是不可预料的：

521

查询下压

SELECT	*	FROM	table1	WHERE	col1	>	'123.39999999999f'

结果如下：

|-------|

|	col1		|

|-------|

|	130.1	|

|-------|

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

522

实时功能

实时功能（Beta）

实时功能是	Kyligence	提供的高级功能，支持查询实时的流数据，可显著地缩短数据从加载到查询的延迟时间。

功能背景

功能架构

随着企业对用户体验、服务质量及决策时效性的要求不断提高，实时分析已广泛的应用在众多场景（如个性化服务、指

标分析等）。然而，引入额外的流式实时数据平台后，虽然一定程度满足了业务需求，但是往往带来成本高昂、运维困

难、数据一致性低等问题。

借助	Kyligence	Enterprise，企业仅需建设一套数据平台即可同时满足离线和实时数据的处理和分析需求，降低技术门槛
并统一数据口径，帮助企业在复杂的商业活动中更快速、更精准地做出商业决策。

功能特性

低延迟、高并发

满足低延时、高并发的	OLAP	数据分析需求。

从	T+1	加速至	T+0

实现了从	T+1	到	T+0	的拓展和延伸，在分钟级数据延时的情况下依然可以保持亚秒级查询响应，同时显著降低部
署实时分析应用的开发和运维成本。

降本增效的解决方案

为企业快速获取批流一体的	OLAP	分析能力以及多样实时分析场景提供了一套低成本、高效率的解决方案。

相关文档

软硬件环境要求

使用实时功能

523

实时功能

已知限制

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

524

软硬件环境要求

软硬件环境要求

实时功能是	Kyligence	提供的高级功能，支持查询实时的流数据，可显著地缩短数据从加载到查询的延迟时间。

本文介绍实时功能的软硬件要求。

需具备	Kyligence	Enterprise	高级版证书才能使用本功能，详细信息请联系	Kyligence	客户经理。

网络要求

Kyligence	Enterprise	和	Kafka	集群之间网络可连通。

[!NOTE]

如果您的内网环境中没有统一的	DNS	服务，您需要将	Kafka	各节点的	IP	地址和	Hostname	信息，手动配置到
Kyligence	Enterprise	所属服务器的	 	/etc/hosts		文件中。

版本要求

类别

说明

Kyligence	Enterprise

4.5.0	及以上版本

Kafka

其他要求

0.11.0.X	及以上版本，需自行部署。

Kyligence	Enterprise	和	Kafka	集群所属服务器的时区与时间需保持一致。如需修改	Kyligence	Enterprise	的时区，见
基本配置参数。

如果	Hadoop	或	Kafka	集群启用了安全认证，您还需要在进行额外配置：

Hadoop	和	Kafka	均启用	Kerberos	认证时

[!NOTE]

本场景中，需确保	Kerberos	票据在索引构建任务运行期间处于有效期范围，否则可能导致无法消费	Kafka	数
据。

1.	 在	kylin.properties	文件中，增加下述	Kafka	相关配置。

kylin.kafka-jaas.enabled=true

kylin.streaming.kafka-conf.security.protocol=SASL_PLAINTEXT

kylin.streaming.kafka-conf.sasl.mechanism=GSSAPI

kylin.streaming.kafka-conf.sasl.kerberos.service.name=kafka

2.	 新建	Kafka	认证文件（路径为	$KYLIN_HOME/conf/kafka_jaas.conf），配置参考如下。

本配置已在	CDH（6.3）环境中验证。

KafkaClient	{

					com.sun.security.auth.module.Krb5LoginModule	required

					useKeyTab=false

					useTicketCache=true

					serviceName="{serviceName}";

};

{serviceName}：服务名，通常设置为	kafka。

525

软硬件环境要求

Hadoop	启用	Kerberos	认证且	Kafka	启用	SASL/PLAIN	认证时

1.	 在	kylin.properties	文件中，增加下述	Kafka	相关配置。

kylin.kafka-jaas.enabled=true

kylin.streaming.kafka-conf.security.protocol=SASL_PLAINTEXT

kylin.streaming.kafka-conf.sasl.mechanism={mechanism}

{mechanism}	表示加密算法，例如	PLAIN	或	SCRAM-SHA-256。

2.	 新建	Kafka	认证文件（路径为	$KYLIN_HOME/conf/kafka_jaas.conf），配置参考如下。

本配置已在	CDH（6.3）和	FI	环境中验证。

KafkaClient	{

			{LoginModule}	required

			username="{username}"

			password="{password}";

};

{LoginModule}：登录模块的类名，如： 	org.apache.kafka.common.security.scram.ScramLoginModule

{username}：	Kafka	用户名

{password}：Kafka	密码

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

526

使用实时功能

使用实时功能

实时功能是	Kyligence	提供的高级功能，支持查询实时的流数据，可显著地缩短数据从加载到查询的延迟时间。

本文将介绍如何使用该功能，包括如何加载流数据源（即	Kafka	数据源）以及如何在模型、索引中使用该功能。

前提条件

满足软硬件环境要求

完成	Kafka	数据准备

功能限制

目前实时功能对某些高级功能和	Kafka	数据存在一些使用限制，更多信息，见已知限制。

操作步骤

1.	 登录	Kyligence	Enterprise	平台。

2.	 （可选）加载维度表（适用于需同时分析批数据和流数据的场景），具体操作，见导入	Hive	数据源。

3.	 加载事实表。

i.	 在左侧导航栏，单击数据资产	>	数据源。

ii.	 单击

	图标。

iii.	 在弹出的对话框中，选择	Kafka	并单击下一步。

iv.	 填写	Kafka	集群的连接信息，格式为	 	{IP	地址}:{端口号}	（例如	10.1.0.8:9092），单击获取集群信息。

v.	 选择目标	Kafka	Topic，右侧将显示该	Topic	中的样例数据，单击下一步。

527

使用实时功能

加载源表	1

vi.	 根据下述说明设置源表信息，然后单击加载。

528

使用实时功能

加载源表	2

[!NOTE]

请注意	timestamp	列类型不支持格式如1668009600000这样的数据类型，对于这样的值，请使用string或
int。	支持的timestamp的格式为yyyy-MM-dd，yyyy/MM/dd，yyyyMMdd，yyyy-MM-dd	HH:mm:ss及yyyy-
MM-dd	HH:mm:ss.SSSS。

填写数据库和表名：自定义数据库和表的名称。

关联	Hive	表：根据要分析的数据类型选择是否打开该开关。

如需同时分析批数据和流数据：保持默认打开状态，然后选择要关联的	Hive	表，系统会自动转换
Kafka	Topic	中各字段的类型，保持与	Hive	表一致。

[!NOTE]

该	Hive	表的分区列的数据类型须为	timestamp	，且表中列的数量、名称必须与	Kafka	Topic	中的信息完
全一致。

如仅分析流数据：关闭该开关，然后指定分区列的数据类型为	timestamp。
4.	 创建模型，具体操作，见模型设计。创建模型时，可以将刚刚加载的	Kafka	数据源作为事实表。

5.	 创建索引，具体操作，见聚合索引和明细索引。

如果在加载事实表时设置了关联	Hive	表，您可以在创建索引时选择数据范围：

529

使用实时功能

索引数据范围

批数据：通过	Hive	表构建索引。
流数据：通过	Kafka	Topic	构建索引。
融合：分别生成相同内容的流数据和批数据索引。

6.	 查询数据。

索引构建完成后，在查询时指定时间范围，即可由流数据索引响应查询请求，如下图所示。

查询数据

常见问题

问：使用实时功能时，事实表必须同时具备批数据和流数据才可以使用吗？

答：不是，事实表的数据可以在	Kafka	中，也可以在	Hive	表中。

问：Kafka	是否支持维度数据？

答：不支持，目前维度数据只能存储在	Hive	表中。

问：如何查看流数据的任务状态？

530

使用实时功能

答：在左侧导航栏，单击监控	>	流数据任务，即可查看任务状态信息。您可以单击对应任务的
务参数。相关参数介绍，见基本参数配置。

	图标自定义任

问：如果数据在	Kafka	和	Hive	表中都能查到，会出现数据重复的情况吗？

答：不会。Kyligence	Enterprise	采用下述数据一致性逻辑来避免数据重复：

查询同时命中批数据索引和流数据索引：优先使用批数据索引返回数据，不在批数据索引范围内的数据，则使

用流数据索引返回数据。

查询只命中批数据索引或流数据索引：由命中的索引返回数据。

查询没有命中批数据索引和流数据索引：不返回数据。

问：维表信息发生变更后，支持自动更新至相关模型中吗？

答：支持。您需要设置维表刷新频率，具体操作为：

1.	 在左侧导航栏，单击设置。

2.	 单击高级设置页签，找到自定义项目配置，然后单击	+	配置。

3.	 在弹出的对话框中设置配置项和参数值，然后单击确定。

配置项：填写	kylin.streaming.table-refresh-interval。

参数值：设置时间频率，例如设置每小时刷新	1	次，则填入	1h，支持的时间单位为	d（天）、h（小时）和
m（分钟）。

自定义项目配置

问：模型中出现重叠时间范围的	Segments	如何处理？

答：对于包含重叠时间范围的	Segments	的模型，会被在模型列表中标记为	broken，为保证数据准确性，该模型无
法被修复，您需要重新创建模型并刷新数据。checkpoint	文件丢失可能导致该问题（checkpoint	文件用于记录
Segment	的构建进度），您可以通过配置参数	 	kylin.engine.streaming-checkpoint-location=
{hdfsWorkingDir}/_streaming		避免	checkpoint	文件被异常删除。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

531

自定义解析器

自定义解析器

实时功能接入Kafka支持自定义解析器，以便处理多层嵌套Json、Csv结构等数据，自定义增删字段。

使用自定义解析器

解析器的使用详情请参考	实时自定义解析器	SDK

解析器在系统中的使用

管理解析器Jar文包功能请参考	自定义解析器Jar包管理	API

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

532

已知限制

已知限制

目前实时功能的数据源仅支持	Kafka，同时对某些高级功能和	Kafka	数据存在一些使用限制，具体如下：

类别

数据源（Kafka）

模型与索引

运维

其他

限制

●	不支持数据抽样
●	不支持重载数据源

●	不支持更换事实表
●	不支持与智能分层存储功能联动使用
●	不支持与多级分区功能联动使用
●	不支持刷新历史	Segment	数据
●	不支持可计算列
●	不支持融合模型下	SQL	建模
●	不支持生成模型优化建议
●	不支持导出	TDS

●	不支持	FusionInsight	环境下的	Kerberos	权限集成
●	不支持容量计费
●	不支持表行列级访问权限控制
●	不支持垃圾清理
●	不支持导入导出模型元数据

●	不支持异步查询

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

533

快照管理

快照管理

本章将介绍	Kyligence	Enterprise	的快照管理功能。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

534

快照管理与操作

快照管理与操作

快照（Snapshot）是原始表的只读静态视图，其可服务于以下情况：

支持单独对维度表的查询，该种查询下将优先使用快照进行回答

维度表上的维度可在不生成索引的情况下，通过将关联键加入聚合组，使其也能够服务于查询，从而避免聚合组维

度爆炸问题

快照默认会在加载数据、构建索引、刷新/合并	Segment	时由系统自动生成，用来储存模型中维表的数据。而在
Kyligence	Enterprise	4.2.2	及之后的版本，提供了独立管理快照的功能。开启快照管理功能后，系统将不再自动进行快照
的管理，快照的构建、刷新、删除均需通过手动管理的方式进行。

快照管理开关

您可以在项目级高级设置中打开快照管理开关。默认为关闭。

1.	 点击进入导航栏	设置	->	高级设置	->	快照管理，将	支持管理快照	开关设置为开启。

快照管理开关

快照管理开启

535

快照管理与操作

快照管理关闭

注意：

在快照管理开启时，系统将不再自动进行快照的管理，具体如下：

如果某张表已经在系统中生成了快照，则其将显示在快照列表中，当该表数据发生了变化时，您需要手动触发

快照刷新任务才能够刷新对应的快照数据

如果某张表在系统中未生成快照，	则不会显示在快照列表中，且您需要手动进行构建才可生成对应的快照

如果一张表未被模型引用，则其快照无法服务于相关查询

从	4.6.6.0	版本后，模型构建时默认从快照中取数进行维度表的构建，因此当	Hive	源表数据有变更，需要在
Kyligence	Enterprise	中及时刷新快照，否则会导致从快照取数构建后的结果和	Hive	中不一致。如希望从	Hive	源表
取数构建维度表，可以设置	 	kylin.engine.persist-flat-use-snapshot-enabled=false	，模型级生效。

自动刷新快照开关

当开启快照管理开关时,	您可以在项目级高级设置中自动刷新快照开关。默认为关闭。

1.	 点击进入导航栏	设置	->	高级设置	->	快照管理，将	自动刷新	开关设置为开启。

自动刷新开启

2.	 开启自动刷新快照开关时,	您可以调整定时检测的频率。默认为每天	0	时	0	点	0	分刷新

536

快照管理与操作

自动刷新频率-天

自动刷新频率-时

自动刷新频率-分

注意:

自动刷新快照不支持	JDBC	数据源

定时检测的频率

天，取值范围:	1	~	31	，例如设置为	5	时,	每月	1	号、	6	号、	11	号、	16	号、	21	号、	26	号、	31	号触发检测
小时，取值范围:	1	~	23	，例如设置为	5	时,	每天	0	点、	5	点、	10	点、	15	点、	20	点触发检测
分，取值范围:	1	~	59	，例如设置为	20	时,	每小时	0	分种、	20	分钟、	40	分钟触发检测

537

快照管理与操作

多级分区检测最下级分区的分区数量和分区内文件信息

事务表自动合并数据文件时，会触发构建快照任务

配置项

配置项

描述

kylin.snapshot.auto-refresh-
fetch-files-count

检测时，fetch	file	的数量。默认值	1	表示表	location	的文件数量未发生
变化时，判断最新更新的一个文件的文件信息

kylin.snapshot.auto-refresh-
fetch-partitions-count

检测时，fetch	partition	的数量。默认值	1	表示表分区数量未发生变化
时，判断最新创建的一个分区的中文件

kylin.snapshot.auto-refresh-
max-concurrent-jobs

检测时，检测表是否更新的执行并行度。默认值	20	表示并行度为	20
。

kylin.snapshot.first-auto-
refresh-enabled

第一次检测时，是否刷新快照。默认值	false	表示第一次检测时，不刷
新快照。

kylin.snapshot.null-location-
auto-refresh-enabled

表	location	或	partition	location	为	null	时，是否刷新快照。默认值	false
表示	location	为	null	时,	不刷新快照。

默认
值

1

1

20

false

false

kylin.snapshot.auto-refresh-
task-timeout

判断	Hive	表数据是否变化的超时时间。默认值	30min	表示超时时间为
30	分钟。

30min

kylin.env.write-hdfs-
working-dir

Kyligence	读写分离部署时，读集群的	hdfs-working-dir	，必要参数。默
认值为空，表示未配置

-

快照列表

1.	 在	支持管理快照	开关开启之后，您将会在	数据资产	找到	快照。

2.	 点击进入导航栏	数据资产	->	快照	界面，主页面将以列表形式显示已有的快照。下图所示为快照列表页面：

快照列表的字段介绍：

表名称：表的名称。

数据库：数据库的名称。

分区列：构建时采用的分区列。

使用次数：查询击中快照的次数。间隔	30	分钟更新一次。
状态：四种快照状态。

LOADING	快照构建中，构建完成后可服务于查询。

ONLINE	快照上线，可用于查询。

REFRESHING	快照上线，并且有快照刷新任务执行中，已有的快照可服务于查询。

BROKEN	快照损坏，当源表发生结构变更并被重载后，对应的快照会变为该状态，且此时不可服务于查
询。

存储大小：快照的存储大小（	以	Snappy	方式压缩的	Parquet	文件格式大小	）。

维度表模型数量：快照所属表被用作维度表的模型数量。

事实表模型数量：快照所属表被用作事实表的模型数量。

538

快照管理与操作

最后更新时间：快照最近一次构建/刷新成功的时间。

快照操作

快照列表的上方是对指定快照的操作选项，以下介绍对快照的操作：

添加快照：从已加载了源数据的表中选择需要构建快照的表或库，点击下一步进入分区设置。

接下来为快照分区设置步骤。设置快照分区可以在一定程度上通过并行构建分区提升构建速度，默认情况下，系统

会按照无分区的方式进行构建，用户也可设置或是探测分区列，同时可以指定分区值。

注意：

快照分区列仅支持设置为	Hive	分区列，若采用错误的分区列进行构建，构建任务将出错；
分区构建仅能增加构建的速度，构建的结果依然为全量的数据。

刷新快照：刷新已经构建过了的快照。

全量刷新：此时刷新操作即构建最新且全量的快照。

539

快照管理与操作

增量刷新：对于设置了源表分区的快照，将仅刷新新增的分区值数据（已构建的历史数据不刷新），建议历史

数据无更新时选择。

自定义分区值刷新：指定单个或多个分区值进行数据刷新。

刷新快照

删除快照：删除已有快照，并且终止该快照的所有相关任务。

修复快照：当源表发生结构变更并被重载后，对应的快照会变为	BROKEN	状态，此时可修复该快照，即重新构
建。

540

快照管理与操作

修复快照

对于快照发起的构建任务，可在	 	kylin.properties		中（全局生效）和项目设置页面（项目级生效）配置	spark	的相关配
置，此处进行的配置将覆盖全局/项目级别的索引构建任务配置。

配置以	 	kylin.engine.snapshot.spark-conf		开头，如下所示：

kylin.engine.snapshot.spark-conf.spark.executor.instances=5

kylin.engine.snapshot.spark-conf.spark.executor.cores=2

kylin.engine.snapshot.spark-conf.spark.executor.memory=12288m

kylin.engine.snapshot.spark-conf.spark.executor.memoryOverhead=3072m

kylin.engine.snapshot.spark-conf.spark.sql.shuffle.partitions=200

kylin.engine.snapshot.spark-conf.spark.driver.memory=4096m

kylin.engine.snapshot.spark-conf.spark.driver.memoryOverhead=3072m

kylin.engine.snapshot.spark-conf.spark.driver.cores=2

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

541

内表使用指南

使用内表

本章将介绍	Kyligence	Enterprise	的全新功能：内表的作用、创建与使用方法、配置项以及注意事项。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

542

内表功能概述

内表功能概述

灵活分析，跳跃的思维火花

Kyligence	的预计算技术可以通过定义模型和索引，帮助您实现大数据量、高并发场景下的亚秒级查询体验	。然而并非
所有的查询分析场景都可以预先定义，而从构建和存储成本角度考虑，也不适合预计算所有维度组合的索引。

在业务分析模式固定之前，分析师往往需要通过灵活探查来挖掘数据价值和规律，亦或是为制作固定报表做准备。	由于
分析维度、度量的多变，数量有限的预计算索引无法完全覆盖所有查询场景，而此时基于内表的现算能力就可以发挥作

用。

什么是内表？

内表（Internal	Table）是指由Kyligence	Enterprise直接管理数据和元数据的表。	相较于原先的数据源表仅导入表元数据
用于建模，内表既保存元数据，又能直接管理用户数据。与传统RDBMS和大多数数仓软件一样，您只需将数据导入内
表，即可进行查询分析。

如何创建内表？

您无需自己编写DDL建表语句，仅需在导入的数据源表页面点击"创建内表"按钮，并完成相关表属性设置后，即可完成
内表创建。	详情请参考管理内表页面。

如何区分数据源表和内表？

查询时无需区分数据源表还是内表，您可以认为它们在Kyligence中是一张表，它只有一个数据库名和表名。区别在于未
开启内表功能或者未创建内表时，该表不直接管理数据，仅用于建模。

如何在项目级开启使用内表功能？

您仅需在项目设置页面，点击"内表设置"标签页，打开内表功能开关即可。

543

内表功能概述

打开内表开关后，您可以在侧边导航栏中看到“内表”页签，点击可以进入内表管理页面。

关于快照功能

在Kyligence	Enterprise	4.x版本及以前，系统支持创建快照表，从Kyligence	Enterprise	5.x开始，当开启内表功能后，快照
功能将不再支持。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

544

管理内表

管理内表

1.	创建内表

Kyligence	Enterprise暂不支持通过SQL	DDL语句创建内表。

当前您可以通过两种方式创建内表：

1.	 在导入数据源表时，勾选“同时加载为内表”，该方式适合在初次导入数据源表的同时批量创建内表。

注意：批量创建内表时，系统默认不会设置分区列等信息，如您需要设置分区列、排序列等信息，请稍后在内表管理页

面进行更新。

1.	 在已导入的数据源表页面点击"创建内表"按钮，并完成相关表属性设置后，即可完成内表创建。

2.	设置内表属性

设置分区列

545

管理内表

内表支持通过设置分区列来提升某些场景下的查询性能。您可以将表中的一个列设置为分区列，该列可以是日期列，也

可以非日期列。但请注意，当且仅当分区列为日期列时，内表可以进行增量加载。	内表不含分区列或分区列为非日期列
时，仅支持全量加载。	我们强烈建议您避免将高基列设置为分区列，生成过多的数据分区可能对查询性能造成负面影
响。

设置主键列（PrimaryKey）和排序列（OrderByKey）

设置主键列和排序列可以提升某些场景下的查询性能。与传统的RDBMS不同，这里的主键列（PrimaryKey）并不是唯
一键约束，仅用于该列在where过滤条件下的查询加速。	需要注意的是，主键列必须是排序列的前缀列。

546

管理内表

您可以点击“	>>	”后进行主键列和排序列的设置

3.	更新内表属性

您可以在内表管理页面进行表属性的更新。

注意：由于内表属性会影响表数据的存储分布方式，在导入数据后您无法再更改分区列等表属性信息。	需要先清空所有
内表数据后再进行修改。

4.	表重载

如果您重载数据源表，内表也将被重载。但是当内表包含数据时无法进行表重载，您需要先清空表数据后再进行表重

载。

5.	清空表数据

您可以在内表管理页面清空内表数据。执行清空表数据操作会同时终止该表所有运行中的数据导入任务。

6.	删除内表

您可以在内表管理页面删除内表，执行删除内表操作将同时清空内表数据并停止运行中的数据导入任务。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

547

内表数据导入

导入内表数据

全量导入

所有内表，无论其是否分区表，都支持全量数据导入。	全量导入适用于数据量大小适中的表，如果表数据量特别大，且

设置了时间分区列，建议使用增量导入的方式。	鼠标移动至需要导入数据的表，点击加载按钮

load-table

全量导入无需选择时间范围，系统会将数据源表中的所有数据导入内表。

增量导入

仅设置了时间分区列的表，支持增量导入。增量导入时可以设置导入的起始时间和结束时间，系统会从数据源拉取该时

间范围内的数据导入内表。

548

内表数据导入

请注意：内表并没有唯一键约束与重复数据检查，如果您导入的数据时间范围存在重叠，将可能出现重复数据。如果您

希望更新某些分区数据，可以在删除该分区数据后重新导入。

数据导入任务

提交数据导入任务请求后，您可以在“监控”	->	“批数据任务”中看到运行中的数据导入任务及其运行进度、状态以及日志
等信息。

预加载内表缓存

预加载内表缓存到查询集群	executor	本地磁盘，可以减少查询时对内表文件的访问，从而提高查询性能。

使用参数	 	kylin.internal-table.preloaded-cache.enabled		控制是否开启预加载。参数默认值为	true	，表示开启预加载。

549

内表数据导入

load-gluten-cache

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

550

查询内表

查询内表

1.	准备工作

内表查询与模型查询在查询界面上没有区别，详情参考SQL查询

您无需做任何SQL改写，但需要确保所查询的表均已创建了内表并导入数据。

2.	查询内表

在Kyligence	Enterprise的查询界面上，您可以通过勾选“直查内表”来跳过模型匹配阶段。在确定您的查询为灵活查询，
无法通过模型预计算索引回答时，勾选“直查内表”可以节省模型匹配时间，从而提高查询响应速度。

默认不勾选“直查内表”，此时查询引擎将优先进行模型匹配模型预计算索引，当无法通过模型预计算索引回答时，会转
为直查内表。	如果复杂查询的部分子查询能通过模型索引回答，部分不能，系统会尝试通过模型索引和内表联查回答。

3.	下压查询

开启内表功能后，无论查询中的表是否已创建内表，或是否导入数据，查询都不再下压至数据源。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

551

数据分析师指南

数据分析师指南

本章将从数据分析的角度出发，介绍如何分析数据、进行	SQL	查询以及对接第三方	BI。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:01

552

SQL	查询

SQL	查询

本章将介绍如何在	Kyligence	Enterprise	中执行	SQL	查询语句，以及	Kyligence	Enterprise	支持的	SQL	语法和使用规范。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

553

数据类型

数据类型

Kyligence	已支持的数据类型列表如下：

字段类型

说明

取值范围

tinyint

小整数值

(-128，127)

smallint

大整数值

(-32,768，32,767)

int/integer

大整数值

(-2,147,483,648，2,147,483,647)

bigint

极大整数值

(-9,223,372,036,854,775,808，9,223,372,036,854,775,807)

float

double

单精度浮点
数值

双精度浮点
数值

decimal

小数值

timestamp

时间戳，纳
秒级精度

date

日期值

varchar

变长字符串

char

定长字符串

boolean

布尔类型

(-3.402823466E+38，-1.175494351E-38)，0，(1.175494351E-38，
3.402823466351E+38)

(-1.7976931348623157E+308，-2.2250738585072014E-308)，0，
(2.2250738585072014E-308，1.797693134	8623157E+308)

---

---

---

---

---

---

注意：double	类型计算存在精度不准确问题。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

554

查询分析

查询分析

Kyligence	Enterprise	是企业级智能多维数据库平台，您可以通过构建索引来完成预计算和数据加载，实现海量数据下的
亚秒级查询响应。

与普通查询的执行过程不同，Kyligence	Enterprise	在执行	SQL	时会用预计算结果代替在线计算，极大地减少在线计算
量，并提升查询性能。

预计算查询执行过程

与普通查询的执行过程不同，Kyligence	Enterprise	在执行	SQL	时会用预计算结果代替在线计算，极大地减少在线计算
量，并提升查询性能。为了便于理解，执行过程简化后可以描述为：

1.	 解析	SQL	语句，提取查询中所有的	 	FROM		子句。

2.	 为每个	 	FROM		子句寻找与之匹配的且代价最小的模型。	与之匹配需满足以下几点：

	FROM		子句中出现的表和它们间的关联必需与模型中定义事实表和维表的关联一致。留意	 	LEFT	JOIN		与
	INNER	JOIN		是不匹配的。
对于聚合查询， 	GROUP	BY		子句中的聚合列必需是模型中定义的维度，同时	 	SELECT		子句中的聚合函数必需是
模型中定义的度量。

对于非聚合查询（即不带聚合函数），模型中必需定义有表明细索引，否则匹配失败。同时查询中所有的列都

必需包含在表明细索引中。

代价最小指当有多个可能的匹配（模型/索引）时，Kyligence	Enterprise	会根据执行代价最低的原则，自动挑选一个
最优的匹配。比如，表明细索引其实也可以匹配聚合查询，但由于需要作在线聚合运算，执行代价很高。因此，用

表明细索引匹配聚合查询是最后的选择，只会发生在所有模型的聚合索引都无法匹配的时候。

3.	 若所有	 	FROM		子句均匹配成功，那么	Kyligence	Enterprise	将使用模型下的索引执行查询。

查询中所有的	 	FROM		子句将被替换成预计算结果，然后执行并获得查询结果。如果您在	Web	UI	执行查询，查询成
功后，可以在屏幕下方的查询对象条目中找到命中模型的名字。详见在用户界面执行	SQL	查询。

4.	 若有个别	 	FROM		子句无法找到匹配的模型或索引组，那么	Kyligence	Enterprise	无法用模型或索引组执行查询。

查询将报错，出错信息为	 	no	model	found		或	 	no	realization	found	。

作为特例，如果查询下压被启用，那么	Kyligence	Enterprise	将不会报错，而是转发这种无法匹配的查询到下压查询
引擎执行。更多请见查询下压的详细介绍。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

555

查询分析

在用户界面执行	SQL	查询

打开	Kyligence	Enterprise	的	Web	UI，进入导航栏	查询	->	分析	界面。如下图所示左边为您添加的数据源表，即所有可
以查询的表。右边为查询分析面板，在上方的查询编辑器中输入	SQL	语句并点击查询，将在下方显示结果。下面详述
不同标识对应的解释。

执行	SQL	查询

在输入框中输入	SQL	语句，点击查询按钮即可进行查询。在右下角提交按钮旁有一个	Limit	输入框，如果	SQL	语句中
不含	Limit	子句，则该	SQL	语句会拼接一个默认	Limit	值。如果	SQL	语句中有	Limit	子句则以	SQL	语句为准。假如用
户想去掉	Limit	限制，可以反选	Limit	前的选择框。

select	LO_ORDERDATE,	count(*)

from	SSB.P_LINEORDER

group	by	LO_ORDERDATE

查询结果成功返回并在下方显示查询信息。您可以看出该查询执行时间为	0.13	秒，并且查询对象中显示该查询击中了模
型。

同时，点击查询	ID	后箭头图标，可以直接打开	Spark	UI	中关于该查询的页面。在该页面，用户可以方便的看到该	SQL
在	Spark	中的执行流程。

当您在进行慢查询优化时，需要了解查询的具体执行步骤，定位耗时原因。可点击展开响应时间，以查看当前查询的详

细执行步骤及耗时，辅助分析。

注意：

1.	 仅支持	SELECT	查询语句。
2.	 若开启了查询下压，当查询无法击中模型（索引组）时，将会重定向到下压查询引擎执行。这时可能耗时稍

长。此时查询对象可能显示为	Hive，即查询下压至	Hive。

3.	 若查询不需要	Spark	计算，例如击中查询缓存，常量查询等，则不会有箭头打开	Spark	UI。
4.	 当查询使用分层存储时，查询扫描记录数需要手动获取。

停止查询

556

查询分析

点击查询按钮后，点击相同位置的停止按钮，即可停止此次查询。

查询被停止后，展示此次查询的查询	ID	和报错文案。

此外，点击该查询的关闭按钮也会停止此次查询。

保存查询

与用户账号关联，用户将能够从不同的浏览器甚至机器上获取已保存的查询。在查询编辑器下方点击保存查询按钮，将

会在弹窗中提示输入名称和描述来保存当前查询。

557

查询分析

已保存的查询

在查询编辑器的右上方点击已保存的查询按钮查看所有保存的查询。弹窗中将显示已保存的查询列表，您可以勾选查询

前方的选择框，然后点击查询按钮来重新执行查询。

查询结果展现

558

查询分析

默认情况下，Kyligence	Enterprise	会以表格形式展示数据。您可以在查询结果右上方的筛选框中搜索查询内容，该搜索
方式为模糊搜索。如输入	 	1992	，则查询结果中的每一行都将包含	 	1992	，如图所示为	1992	年每天的订单量。也可以
点击导出按钮将查询结果导出到	CSV	文件。

查询可视化

除了表格，Kyligence	Enterprise	还支持可视化展示查询结果，实现快速洞察。

目前支持：折线图，柱状图，饼图。

其他执行	SQL	查询的方式

与BI工具集成

注意事项

如果查询既可以用索引回答也可以用快照回答，将会优先由快照回答。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

559

查询分析

查询样例

我们以	Kyligence	Enterprise	的样例数据集为例介绍	SQL	的查询方式。首先请您通过AI	增强模式指引完整创建一个	AI	增
强模式的项目，构建索引并当所有任务成功执行完毕后，请您进入	查询	->	分析	页面。请您在查询编辑器中输入	SQL
语句，然后单击提交按钮。

下面我们将介绍	SQL	查询的例子和相应的结果。

提示：你可以在样例数据集章节查看样例数据集的介绍，你也可以在	Kyligence	Enterprise	的模型编辑界面查看模
型。

单表行数统计

SELECT	COUNT(*)	FROM	P_LINEORDER

这条	SQL	用于查询	P_LINEORDER	表中总行数，您可以同时在	Hive	中执行同样的查询进行性能对比。在我们的对比
中，Hive	查询耗时	29.711	秒，Kyligence	Enterprise	查询耗时	2.18	秒。

多表连接

select

P_LINEORDER.LO_SUPPKEY

,	P_LINEORDER.LO_PARTKEY

,	PART.P_NAME

,	SUPPLIER.S_CITY

,	sum(LO_QUANTITY)

from	P_LINEORDER

left	join	PART	on	P_LINEORDER.LO_PARTKEY	=	PART.P_PARTKEY

left	join	SUPPLIER	on	P_LINEORDER.LO_SUPPKEY	=	SUPPLIER.S_SUPPKEY

group	by

P_LINEORDER.LO_SUPPKEY

,	P_LINEORDER.LO_PARTKEY

,	PART.P_NAME

,	SUPPLIER.S_CITY

这条	SQL	将事实表	P_LINEORDER	和两张维度表	PART	和	SUPPLIER	根据外键进行了左连接。在笔者的对比试验中，
Hive	查询耗时	28.164	秒，Kyligence	Enterprise	查询耗时	2.06	秒。

全表查询

SELECT	*	FROM	P_LINEORDER

假如没有创建表明细索引，Kyligence	Enterprise	默认并不对原始数据的明细进行保存，因此该查询将不会击中模型。但
是	Kyligence	Enterprise	默认开启查询下压引擎，该条查询将通过查询下压至	Spark	SQL	返回结果。您可以查看下压至原
生	SparkSQL	章节了解更多。

如果您希望	Kyligence	Enterprise	支持原始数据的保存和查询，可以创建相关列的表明细索引并加载数据。您可以查看表
明细索引章节了解更多。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

560

查询分析

SQL	规范参考

Kyligence	Enterprise	支持	ANSI	SQL	2003，以下列举了支持的基本	SQL	语句。

支持语法

statement:

|		query

query:

						values

		|		WITH	withItem	[	,	withItem	]*	query

		|			{

										select

						|		selectWithoutFrom

						|		query	UNION	[	ALL	|	DISTINCT	]	query

						|		query	INTERSECT	[	ALL	|	DISTINCT	]	query

						}

						[	ORDER	BY	orderItem	[,	orderItem	]*	]

						[	LIMIT	{	count	|	ALL	}	]

						[	OFFSET	start	{	ROW	|	ROWS	}	]

						[	FETCH	{	FIRST	|	NEXT	}	[	count	]	{	ROW|	ROWS	}	]

withItem:

						name

						['('	column	[,	column	]*	')'	]

						AS	'('	query	')'

orderItem:
						expression	[	ASC	|	DESC	]［	NULLS	FIRST	|NULLS	LAST	］

select:

						SELECT	[	ALL	|	DISTINCT]

										{	*	|	projectItem	[,	projectItem	]*	}

						FROM	tableExpression

						[	WHERE	booleanExpression	]

						[	GROUP	BY	{	groupItem	[,	groupItem	]*	}]

						[	HAVING	booleanExpression	]

						[	WINDOW	windowName	AS	windowSpec	[,windowName	AS	windowSpec	]*	]

selectWithoutFrom:

						SELECT	[	ALL	|	DISTINCT	]

										{	*	|	projectItem	[,	projectItem	]*	}

projectItem:

						expression	[	[	AS	]	columnAlias	]

		|		tableAlias	.	*

tableExpression:

						tableReference	[,	tableReference	]*
		|		tableExpression	[	NATURAL	]［(	LEFT	|	RIGHT	|	FULL	)	[	OUTER	]	］	JOINtableExpression	[	joinCondition	]

joinCondition:

						ON	booleanExpression

		|		USING	'('	column	[,	column	]*	')'

tableReference:

						tablePrimary

						[	matchRecognize	]

						[	[	AS	]	alias	[	'('	columnAlias	[,columnAlias	]*	')'	]	]

tablePrimary:

						[	[	catalogName	.	]	schemaName	.	]tableName

						'('	TABLE	[	[	catalogName	.	]	schemaName.	]	tableName	')'

561

查询分析

		|			[LATERAL	]	'('	query	')'

		|		UNNEST	'('	expression	')'	[	WITH	ORDINALITY	]

		|			[LATERAL	]	TABLE	'('	[	SPECIFIC	]	functionName	'('	expression	[,	expression	]*')'	')'

values:

						VALUES	expression	[,	expression	]*

groupItem:

						expression

		|			'('')'

		|			'('expression	[,	expression	]*	')'

		|		GROUPING	SETS	'('	groupItem	[,	groupItem	]*	')'

windowRef:

						windowName

		|		windowSpec

windowSpec:

						[windowName	]

						'('

						[	ORDER	BYorderItem	[,	orderItem	]*	]

						[	PARTITION	BY	expression	[,	expression]*	]

						[

										RANGE	numericOrIntervalExpression	{PRECEDING	|	FOLLOWING	}

						|		ROWS	numericExpression	{	PRECEDING	|	FOLLOWING	}

						]

				')'

注意：不同版本实现反馈可能会有不同，如有问题请咨询技术服务团队。

SQL	关键字

以下为	Kyligence	Enterprise	中	SQL的关键字，请尽可能避免使用关键字做为标识符。

A,	ABS,	ABSOLUTE,	ACTION,	ADA,	ADD,	ADMIN,	AFTER,	ALL,ALLOCATE,	ALLOW,	ALTER,	ALWAYS,	AND,	ANY,

APPLY,	ARE,	ARRAY,ARRAY_MAX_CARDINALITY,	AS,	ASC,	ASENSITIVE,	ASSERTION,	ASSIGNMENT,

ASYMMETRIC,	AT,	ATOMIC,	ATTRIBUTE,	ATTRIBUTES,AUTHORIZATION,	AVG,	BEFORE,	BEGIN,

BEGIN_FRAME,BEGIN_PARTITION,	BERNOULLI,	BETWEEN,	BIGINT,	BINARY,	BIT,BLOB,	BOOLEAN,	BOTH,

BREADTH,	BY,	C,	CALL,	CALLED,CARDINALITY,	CASCADE,	CASCADED,	CASE,	CAST,	CATALOG,

CATALOG_NAME,	CEIL,	CEILING,	CENTURY,	CHAIN,	CHAR,CHARACTER,	CHARACTERISTICS,

CHARACTERS,CHARACTER_LENGTH,	CHARACTER_SET_CATALOG,	CHARACTER_SET_NAME,

CHARACTER_SET_SCHEMA,CHAR_LENGTH,	CHECK,	CLASSIFIER,	CLASS_ORIGIN,	CLOB,	CLOSE,COALESCE,

COBOL,	COLLATE,	COLLATION,	COLLATION_CATALOG,	COLLATION_NAME,	COLLATION_SCHEMA,	COLLECT,

COLUMN,	COLUMN_NAME,	COMMAND_FUNCTION,	COMMAND_FUNCTION_CODE,	COMMIT,

COMMITTED,CONDITION,	CONDITION_NUMBER,	CONNECT,	CONNECTION,	CONNECTION_NAME,

CONSTRAINT,	CONSTRAINTS,	CONSTRAINT_CATALOG,	CONSTRAINT_NAME,	CONSTRAINT_SCHEMA,

CONSTRUCTOR,	CONTAINS,	CONTINUE,CONVERT,	CORR,	CORRESPONDING,	COUNT,

COVAR_POP,COVAR_SAMP,	CREATE,	CROSS,	CUBE,	CUME_DIST,	CURRENT,CURRENT_CATALOG,

CURRENT_DATE,CURRENT_DEFAULT_TRANSFORM_GROUP,	CURRENT_PATH,CURRENT_ROLE,

CURRENT_ROW,	CURRENT_SCHEMA,CURRENT_TIME,

CURRENT_TIMESTAMP,CURRENT_TRANSFORM_GROUP_FOR_TYPE,	CURRENT_USER,CURSOR,

CURSOR_NAME,	CYCLE,	DATA,	DATABASE,	DATE,	DATETIME_INTERVAL_CODE,

DATETIME_INTERVAL_PRECISION,DAY,	DEALLOCATE,	DEC,	DECADE,	DECIMAL,	DECLARE,	DEFAULT,

DEFAULTS,	DEFERRABLE,	DEFERRED,	DEFINE,	DEFINED,	DEFINER,	DEGREE,	DELETE,	DENSE_RANK,	DEPTH,

DEREF,	DERIVED,	DESC,DESCRIBE,	DESCRIPTION,	DESCRIPTOR,	DETERMINISTIC,	DIAGNOSTICS,	DISALLOW,

DISCONNECT,	DISPATCH,	DISTINCT,	DOMAIN,	DOUBLE,	DOW,	DOY,	DROP,	DYNAMIC,	DYNAMIC_FUNCTION,

DYNAMIC_FUNCTION_CODE,	EACH,ELEMENT,	ELSE,	EMPTY,	END,	END-EXEC,	END_FRAME,END_PARTITION,

EPOCH,	EQUALS,	ESCAPE,	EVERY,	EXCEPT,	EXCEPTION,	EXCLUDE,	EXCLUDING,	EXEC,	EXECUTE,	EXISTS,

562

查询分析

EXP,EXPLAIN,	EXTEND,	EXTERNAL,	EXTRACT,	FALSE,	FETCH,	FILTER,	FINAL,	FIRST,	FIRST_VALUE,	FLOAT,

FLOOR,	FOLLOWING,	FOR,FOREIGN,	FORTRAN,	FOUND,	FRAC_SECOND,	FRAME_ROW,	FREE,FROM,	FULL,

FUNCTION,	FUSION,	G,	GENERAL,	GENERATED,	GET,GLOBAL,	GO,	GOTO,	GRANT,	GRANTED,	GROUP,

GROUPING,GROUPS,	HAVING,	HIERARCHY,	HOLD,	HOUR,	IDENTITY,	IMMEDIATE,	IMMEDIATELY,

IMPLEMENTATION,	IMPORT,	IN,	INCLUDING,	INCREMENT,	INDICATOR,	INITIAL,	INITIALLY,	INNER,INOUT,

INPUT,	INSENSITIVE,	INSERT,	INSTANCE,	INSTANTIABLE,	INT,INTEGER,	INTERSECT,	INTERSECTION,

INTERVAL,	INTO,	INVOKER,	IS,	ISOLATION,	JAVA,	JOIN,	JSON,	K,	KEY,	KEY_MEMBER,	KEY_TYPE,	LABEL,	LAG,

LANGUAGE,	LARGE,	LAST,	LAST_VALUE,	LATERAL,	LEAD,LEADING,	LEFT,	LENGTH,	LEVEL,	LIBRARY,	LIKE,

LIKE_REGEX,	LIMIT,LN,	LOCAL,	LOCALTIME,	LOCALTIMESTAMP,	LOCATOR,	LOWER,	M,	MAP,	MATCH,

MATCHED,	MATCHES,	MATCH_NUMBER,MATCH_RECOGNIZE,	MAX,	MAXVALUE,	MEASURES,

MEMBER,MERGE,	MESSAGE_LENGTH,	MESSAGE_OCTET_LENGTH,	MESSAGE_TEXT,	METHOD,	MICROSECOND,

MILLENNIUM,	MIN,MINUS,	MINUTE,	MINVALUE,	MOD,	MODIFIES,	MODULE,	MONTH,	MORE,	MULTISET,

MUMPS,	NAME,	NAMES,	NATIONAL,	NATURAL,NCHAR,	NCLOB,	NESTING,	NEW,	NEXT,	NO,	NONE,	NORMALIZE,

NORMALIZED,	NOT,	NTH_VALUE,	NTILE,	NULL,	NULLABLE,	NULLIF,	NULLS,	NUMBER,	NUMERIC,	OBJECT,

OCCURRENCES_REGEX,	OCTETS,	OCTET_LENGTH,	OF,	OFFSET,	OLD,	OMIT,	ON,	ONE,	ONLY,OPEN,	OPTION,

OPTIONS,	OR,	ORDER,	ORDERING,	ORDINALITY,	OTHERS,	OUT,	OUTER,	OUTPUT,	OVER,	OVERLAPS,	OVERLAY,

OVERRIDING,	PAD,	PARAMETER,	PARAMETER_MODE,	PARAMETER_NAME,	PARAMETER_ORDINAL_POSITION,

PARAMETER_SPECIFIC_CATALOG,	PARAMETER_SPECIFIC_NAME,	PARAMETER_SPECIFIC_SCHEMA,	PARTIAL,

PARTITION,	PASCAL,	PASSTHROUGH,	PAST,	PATH,	PATTERN,	PER,	PERCENT,PERCENTILE_CONT,

PERCENTILE_DISC,	PERCENT_RANK,	PERIOD,PERMUTE,	PLACING,	PLAN,	PLI,	PORTION,

POSITION,POSITION_REGEX,	POWER,	PRECEDES,	PRECEDING,	PRECISION,PREPARE,	PRESERVE,	PREV,

PRIMARY,	PRIOR,	PRIVILEGES,PROCEDURE,	PUBLIC,	QUARTER,	RANGE,	RANK,	READ,	READS,

REAL,RECURSIVE,	REF,	REFERENCES,	REFERENCING,	REGR_AVGX,REGR_AVGY,	REGR_COUNT,

REGR_INTERCEPT,	REGR_R2,REGR_SLOPE,	REGR_SXX,	REGR_SXY,	REGR_SYY,	RELATIVE,	RELEASE,

REPEATABLE,	REPLACE,	RESET,	RESTART,	RESTRICT,	RESULT,RETURN,	RETURNED_CARDINALITY,

RETURNED_LENGTH,	RETURNED_OCTET_LENGTH,	RETURNED_SQLSTATE,	RETURNS,REVOKE,	RIGHT,	ROLE,

ROLLBACK,	ROLLUP,	ROUTINE,	ROUTINE_CATALOG,	ROUTINE_NAME,	ROUTINE_SCHEMA,	ROW,ROWS,

ROW_COUNT,	ROW_NUMBER,	RUNNING,	SAVEPOINT,	SCALE,	SCHEMA,	SCHEMA_NAME,	SCOPE,

SCOPE_CATALOGS,	SCOPE_NAME,	SCOPE_SCHEMA,	SCROLL,	SEARCH,	SECOND,	SECTION,	SECURITY,	SEEK,

SELECT,	SELF,	SENSITIVE,	SEQUENCE,	SERIALIZABLE,	SERVER,	SERVER_NAME,	SESSION,	SESSION_USER,SET,

SETS,	SHOW,	SIMILAR,	SIMPLE,	SIZE,	SKIP,	SMALLINT,	SOME,	SOURCE,	SPACE,	SPECIFIC,	SPECIFICTYPE,

SPECIFIC_NAME,	SQL,SQLEXCEPTION,	SQLSTATE,	SQLWARNING,	SQL_BIGINT,	SQL_BINARY,	SQL_BIT,

SQL_BLOB,	SQL_BOOLEAN,	SQL_CHAR,	SQL_CLOB,	SQL_DATE,	SQL_DECIMAL,	SQL_DOUBLE,	SQL_FLOAT,

SQL_INTEGER,	SQL_INTERVAL_DAY,	SQL_INTERVAL_DAY_TO_HOUR,	SQL_INTERVAL_DAY_TO_MINUTE,

SQL_INTERVAL_DAY_TO_SECOND,	SQL_INTERVAL_HOUR,	SQL_INTERVAL_HOUR_TO_MINUTE,

SQL_INTERVAL_HOUR_TO_SECOND,	SQL_INTERVAL_MINUTE,	SQL_INTERVAL_MINUTE_TO_SECOND,

SQL_INTERVAL_MONTH,	SQL_INTERVAL_SECOND,	SQL_INTERVAL_YEAR,

SQL_INTERVAL_YEAR_TO_MONTH,	SQL_LONGVARBINARY,	SQL_LONGVARCHAR,	SQL_LONGVARNCHAR,

SQL_NCHAR,	SQL_NCLOB,	SQL_NUMERIC,	SQL_NVARCHAR,	SQL_REAL,	SQL_SMALLINT,	SQL_TIME,

SQL_TIMESTAMP,	SQL_TINYINT,	SQL_TSI_DAY,	SQL_TSI_FRAC_SECOND,	SQL_TSI_HOUR,

SQL_TSI_MICROSECOND,	SQL_TSI_MINUTE,	SQL_TSI_MONTH,	SQL_TSI_QUARTER,	SQL_TSI_SECOND,

SQL_TSI_WEEK,	SQL_TSI_YEAR,	SQL_VARBINARY,	SQL_VARCHAR,	SQRT,	START,	STATE,	STATEMENT,STATIC,

STDDEV_POP,	STDDEV_SAMP,	STREAM,	STRUCTURE,	STYLE,	SUBCLASS_ORIGIN,	SUBMULTISET,	SUBSET,

SUBSTITUTE,SUBSTRING,	SUBSTRING_REGEX,	SUCCEEDS,	SUM,	SYMMETRIC,SYSTEM,	SYSTEM_TIME,

SYSTEM_USER,	TABLE,	TABLESAMPLE,	TABLE_NAME,	TEMPORARY,	THEN,	TIES,	TIME,	TIMESTAMP,

TIMESTAMPADD,	TIMESTAMPDIFF,	TIMEZONE_HOUR,TIMEZONE_MINUTE,	TINYINT,	TO,	TOP_LEVEL_COUNT,

TRAILING,	TRANSACTION,	TRANSACTIONS_ACTIVE,	TRANSACTIONS_COMMITTED,

TRANSACTIONS_ROLLED_BACK,	TRANSFORM,	TRANSFORMS,	TRANSLATE,

TRANSLATE_REGEX,TRANSLATION,	TREAT,	TRIGGER,	TRIGGER_CATALOG,	TRIGGER_NAME,

TRIGGER_SCHEMA,	TRIM,	TRIM_ARRAY,	TRUE,TRUNCATE,	TYPE,	UESCAPE,	UNBOUNDED,	UNCOMMITTED,

UNDER,	UNION,	UNIQUE,	UNKNOWN,	UNNAMED,	UNNEST,UPDATE,	UPPER,	UPSERT,	USAGE,	USER,

563

查询分析

USER_DEFINED_TYPE_CATALOG,	USER_DEFINED_TYPE_CODE,	USER_DEFINED_TYPE_NAME,

USER_DEFINED_TYPE_SCHEMA,USING,	VALUE,	VALUES,	VALUE_OF,	VARBINARY,	VARCHAR,VARYING,

VAR_POP,	VAR_SAMP,	VERSION,	VERSIONING,	VIEW,	WEEK,	WHEN,	WHENEVER,	WHERE,	WIDTH_BUCKET,

WINDOW,WITH,	WITHIN,	WITHOUT,	WORK,	WRAPPER,	WRITE,	XML,	YEAR,	ZONE.

标识符

标识符为	SQL	查询中使用的表名、列名以及其他元数据。没有使用引号的标识符，如	emp	，需要以字母开头并且只能
包含字母、数字及下划线。没有使用引号的标识符在查询时会隐式地被转换成全大写。

带引号的标识符，如	"Employee	Name"，以双引号开头及结尾。这种标识符基本可以包含任何字符，包括空格或其他标
点符号。如果您希望在标识符中包含双引号，使用另一个双引号来将其转义，例如：An	employee	called	""Fred""."

标识符和引用的对象进行匹配是大小写敏感的。没有使用引号的标识符会隐式地被转换成全大写，如果查询对象在创建

时也没有使用引号，它的名字也会被转换成全大写，因此标识符和查询对象可以进行匹配。

转义关键字

如果您的列名或表名是关键字，您需要使用双引号对其进行转义。

例如表	DATES	包含列	YEAR。这列的列名和	Kyligence	Enterprise	的关键字	YEAR	重复。如下图所示，如果用户直接对
YEAR	进行查询，查询会返回报错，因为	Kyligence	Enterprise	查询引擎无法分辨该列是关键字还是列名。

如上文所述，这时候您只要在列名两端加上双引号就可以正常查询了。

564

查询分析

转义引号

如果您查询的值中包含单引号，您可以用另一个单引号对查询进行转义。

但是查询的值中的双引号是不需要转义的。

565

查询分析

日期查询

如果您进行查询的关键字中包含日期类型的列，您可以参照以下两种日期查询语法范例：

第一种：

select	LO_LINENUMBER,	LO_ORDERDATE,	LO_ORDTOTALPRICE

from	SSB.P_LINEORDER

where	LO_ORDERDATE	=	date	'1992-06-03'

第二种：

566

查询分析

select	LO_LINENUMBER,	LO_ORDERDATE,	LO_ORDTOTALPRICE

from	SSB.P_LINEORDER

where	LO_ORDERDATE	=	cast	(	'1992-06-03'	as	date)

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

567

查询分析

异步查询

异步查询支持用户异步地执行	SQL	查询，并提供更高效的数据导出方式。比如如果一条	SQL	查询的结果集	过大（百万
条结果）或	SQL	执行时间过长，通过异步查询，可以高效地把查询结果集导出，实现自助取数	等各种应用场景。

目前异步查询仅支持调用	REST	API	方式，关于如何使用异步查询	API，请阅读	-	异步查询	API	。

为异步查询结果，配置留存时间

异步查询支持在	 	kylin.properties		进行以下配置：

	kylin.query.async.result-retain-days=7d		：异步查询结果在HDFS上的留存时间，默认为	7	天，即超过	7	天的异步
查询结果及相关文件将被清理

为异步查询，配置单独的集群队列

一般情况下，异步查询和普通查询使用相同的集群队列即可。在一些高级场景下，如果希望避免异步查询影响普通查

询，可以针对异步查询部署单独的队列。具体的配置方式如下：

1.	 开启异步查询部署单独的集群队列设置。将 	kylin.query.unique-async-query-yarn-queue-enabled		设为 	true	，支持
项目级配置和系统级配置，项目级配置的优先级高于系统级配置。	若均未配置，则异步查询与普通查询使用相同的
集群队列。

2.	 指定异步查询使用的队列。支持三个级别进行指定，优先级从高到低依次为:

查询级别，通过	API	请求参数	 	spark_queue		进行指定
项目级别，项目设置	 	kylin.query.async-query.spark-conf.spark.yarn.queue		进行指定
系统级别，配置文件	 	/conf/kylin.properties		中设置	 	kylin.query.async-query.spark-conf.spark.yarn.queue
进行指定

提示：若三种均未配置，默认队列为	 	default

3.	 设置配置:	 	kylin.query.async-query.submit-hadoop-conf-dir=$KYLIN_HOME/async_query_hadoop_conf

4.	 将异步查询集群的	hadoop	配置放到	 	$KYLIN_HOME/async_query_hadoop_conf		目录下，同时把构建集群的	 	hive-

site.xml		分别放到此目录中。

如果开启了	Kerberos	认证，需要将	 	krb5.conf		文件拷贝到	 	$KYLIN_HOME/async_query_hadoop_conf		目录。

5.	 如果异步查询集群、查询集群和构建集群之间开启了	Kerberos	认证，还需要进行以下额外配置：

		kylin.storage.columnar.spark-conf.spark.yarn.access.hadoopFileSystems=hdfs://readcluster,hdfs://asyncquer

ycluster,hdfs://writecluster

		kylin.query.async-query.spark-conf.spark.yarn.access.hadoopFileSystems=hdfs://readcluster,hdfs://asyncque

rycluster,hdfs://writecluster

		kylin.engine.spark-conf.spark.yarn.access.hadoopFileSystems=hdfs://readcluster,hdfs://asyncquerycluster,h

dfs://writecluster

6.	 一般情况下，上述配置即可满足要求。在一些更高级的场景中，可通过	Kyligence	专家指导，在	 	kylin.properties

中配置	spark	的相关配置，以实现更精细的控制。

配置以 	kylin.query.async-query.spark-conf		开头，如下所示：

kylin.query.async-query.spark-conf.spark.yarn.queue=default

kylin.query.async-query.spark-conf.spark.executor.extraJavaOptions=-Dhdp.version=current	-Dlog4j.configuration=

spark-executor-log4j.properties	-Dlog4j.debug	-Dkylin.hdfs.working.dir=${kylin.env.hdfs-working-dir}	-Dkap.meta

data.identifier=${kylin.metadata.url.identifier}	-Dkap.spark.category=sparder	-Dkap.spark.project=${job.project

568

查询分析

}	-Dkap.spark.mountDir=${kylin.tool.mount-spark-log-dir}	-XX:MaxDirectMemorySize=896M

kylin.query.async-query.spark-conf.spark.yarn.am.extraJavaOptions=-Dhdp.version=current

kylin.query.async-query.spark-conf.spark.driver.extraJavaOptions=-Dhdp.version=current

kylin.query.async-query.spark-conf.spark.port.maxRetries=128

kylin.query.async-query.spark-conf.spark.driver.memory=4096m

kylin.query.async-query.spark-conf.spark.sql.driver.maxCollectSize=3600m

kylin.query.async-query.spark-conf.spark.executor.memory=12288m

kylin.query.async-query.spark-conf.spark.executor.memoryOverhead=3072m

kylin.query.async-query.spark-conf.spark.yarn.am.memory=1024m

kylin.query.async-query.spark-conf.spark.executor.cores=5

kylin.query.async-query.spark-conf.spark.executor.instances=4

kylin.query.async-query.spark-conf.spark.task.maxFailures=1

kylin.query.async-query.spark-conf.spark.ui.port=4041

kylin.query.async-query.spark-conf.spark.locality.wait=0s

kylin.query.async-query.spark-conf.spark.sql.dialect=hiveql

kylin.query.async-query.spark-conf.spark.sql.constraintPropagation.enabled=false

kylin.query.async-query.spark-conf.spark.ui.retainedStages=300

kylin.query.async-query.spark-conf.spark.hadoop.yarn.timeline-service.enabled=false

kylin.query.async-query.spark-conf.spark.hadoop.hive.exec.scratchdir=${kylin.env.hdfs-working-dir}/hive-scratch

kylin.query.async-query.spark-conf.hive.execution.engine=MR

kylin.query.async-query.spark-conf.spark.sql.crossJoin.enabled=true

kylin.query.async-query.spark-conf.spark.broadcast.autoClean.enabled=true

kylin.query.async-query.spark-conf.spark.sql.objectHashAggregate.sortBased.fallbackThreshold=1

kylin.query.async-query.spark-conf.spark.sql.hive.caseSensitiveInferenceMode=NEVER_INFER

kylin.query.async-query.spark-conf.spark.sql.sources.bucketing.enabled=false

kylin.query.async-query.spark-conf.spark.yarn.stagingDir=${kylin.env.hdfs-working-dir}

kylin.query.async-query.spark-conf.spark.eventLog.enabled=true

kylin.query.async-query.spark-conf.spark.history.fs.logDirectory=${kylin.env.hdfs-working-dir}/sparder-history

kylin.query.async-query.spark-conf.spark.eventLog.dir=${kylin.env.hdfs-working-dir}/sparder-history

kylin.query.async-query.spark-conf.spark.eventLog.rolling.enabled=true

kylin.query.async-query.spark-conf.spark.eventLog.rolling.maxFileSize=100m

kylin.query.async-query.spark-conf.spark.sql.cartesianPartitionNumThreshold=-1

kylin.query.async-query.spark-conf.parquet.filter.columnindex.enabled=false

kylin.query.async-query.spark-conf.spark.master=yarn

kylin.query.async-query.spark-conf.spark.submit.deployMode=client

已知限制

异步查询不支持查询缓存。

当	SQL	的	select	列中包含	 	,;{}()=		时，在结果文件中会将这些字符转化为	 	_	。
异步查询不支持查询下压至	JDBC	数据源。

行为变更

自	4.6.4	版本后，为了解决返回大量结果的性能问题，产品进行了变更， 	include_header	参数被移至提交异步查询
的API，下载查询结果API中的 	include_header	参数将不起作用。请参考异步查询	API以了解更多细节。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

569

查询分析

通过模型视图简化查询

从	4.5.2	版本开始，引入了模型视图，支持将模型中的表根据关联关系打平后对外暴露，用户可直接通过模型名称查询
数据，而无需写全源表的关联关系，从而简化	SQL	语句或在	BI	工具及应用程序中二次建模的过程。

如何使用

提供系统级和项目级参数以开启模型视图功能，默认为关闭，若需使用模型视图，您可以根据需求在系统级或项目级配

置以下参数：

kylin.query.auto-model-view-enabled=true

模型视图包含模型中的所有维度和度量列，数据已经根据关联关系和筛选条件完成整合。当您查询某个模型时，在

	from		子句中可以直接写	 	项目名称.模型名称		来表示模型视图。

如图模型的关联关系如下：

查询语句如下：

select	C_NAME,	sum(LO_QUANTITY)	as	total_quantity

from	kyligence.model

group	by	C_NAME

570

查询分析

注意事项：

模型视图不支持行列级访问权限设置，若需要设置行列级权限，请不要使用模型视图，具体影响如下：

对模型视图包含的列设置权限，会导致所有用模型视图的查询失败；

对行设置访问权限无效，仍然可以查询到无权限的行数据。

如果数据源中存在与	 	项目名称.模型名称		同名的表，将使用数据源的表回答查询；
模型视图不支持查询下压，如果查询无法击中模型，将失败；

修改模型名称，相当于更改了模型视图的名称，此时，之前包含旧模型视图名称的查询将不可用；

在	BI	工具中连接模型视图

您可以在	BI	工具中连接模型视图，以减少在	BI	工具中的二次建模工作。首先需要在系统级或项目级配置参数
	kylin.query.auto-model-view-enabled=true	，然后就可以在	BI	工具连接	Kyligence	Enterprise	时，选择连接项目下的模
型视图，最后通过模型视图进行分析。

注意事项：

不建议在	Tableau	中连接模型视图，您可以在	Kyligence	Enterprise	中导出模型的	TDS	文件，该方式可以避免重复建
模，且成熟度较高，可查看与	Tableau	Desktop	集成	章节了解更多；
在	BI	工具中连接模型视图时尚存在一些兼容性问题，使用前请联系	Kyligence	评估方案可行性，目前已知问题如
下：

在	Power	BI	中连接模型视图，可能存在读取中文字段乱码的问题；

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

571

查询分析

函数及运算符

本节介绍适用于查询的函数和运算符。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

572

查询分析

运算符

Kyligence	Enterprise	支持如下运算符：

比较运算符

逻辑运算符

算术运算符

字符串运算符

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

573

查询分析

比较运算符

运算符

描述

语法

示例

<

<=

>

>=

<>

小于

小于或等于

大于

大于或等于

不等于

A<B

A<=B

A>=B

A>=B

A<>B

Profit	<	Cost

Profit	<=Cost

Profit	>Cost

Profit	>=Cost

Profit1<>Profit2

IS	NULL

判断值是否为	NULL

value	IS	NULL

profit	IS	NULL

IS	NOT
NULL

IS
DISTINCT
FROM

IS	NOT
DISTINCT
FROM

BETWEEN

判断值是否不为	NULL

判断两个值是否不相等，其中
有值为	NULL	时当作相等。

判断两个值是否相等，其中有
值为	NULL	时当作相等。

value	IS	NOT
NULL

value1	IS
DISTINCT	FROM
value2

value1	IS	NOT
DISTINCT	FROM
value2

profit	IS	NOT	NULL

profit1	IS	DISTINCT	FROM	profit2

profit1	IS	NOT	DISTINCT	FROM
profit2

如果具体的值大于等于	value1
且小于等于	value2，返回结果为
真

A	BETWEEN
value1	AND
value2

profit	BETWEEN	1	AND	1000	Date
BETWEEN	'2016-01-01'	AND	'2016-12-
30'

NOT
BETWEEN

如果具体的值大于等于	value1
且小于等于	value2，返回结果为
假

value1	NOT
BETWEEN	value2
AND	value3

profit	NOT	BETWEEN	1	AND	1000
Date	NOT	BETWEEN	'2016-01-01'
AND	'2016-12-30'

string1	是否和	string2	的样式匹
配，其中	string1	和	string2	为字
符串类型

string1	LIKE
string2

name	LIKE	'%frank%'

string1	是否和	string2	的样式不
匹配，其中	string1	和	string2	为
字符串类型

string1	NOT	LIKE
string2	[	ESCAPE
string3	]

name	NOT	LIKE	'%frank%'

string1	是否和	string2	按正则表
达式匹配

string1	SIMILAR
TO	string2

name	SIMILAR	TO	'frank'

string1	是否和	string2	按正则表
达式不匹配

string1	NOT
SIMILAR	TO
string2

name	NOT	SIMILAR	TO	'frank'

LIKE

NOT	LIKE

SIMILAR
TO

NOT
SIMILAR
TO

已知限制

目前	SIMILAR	TO	ESCAPE	语法，仅限于支持在	SQL	语句中添加并且击中模型的场景，其他场景如添加可计算
列、推荐等暂不支持。

字符串文字如果包含特殊符号需要转义后再进行对比，转义符号为	 	\		，例如匹配	 	\kylin		时实际需要写作
	\\kylin		。对于	 	SIMILAR	TO		以及	 	NOT	SIMILAR	TO		函数使用的是正则匹配，因此会额外进行一次转义处理。例
如，对于	 	\\\\kylin		来说，使用	 	SIMILAR	TO		函数对比	 	\kylin		以及	 	\\kylin		的结果均是	 	true		。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

574

查询分析

逻辑运算符

本节介绍	Kyligence	Enterprise	支持的逻辑运算符。逻辑命题的值有	TRUE、FALSE	和	UNKNOWN，	以下以	 	boolean
指代一个逻辑命题。

运算符

描述

语法

示例

AND

是否条件1	boolean1	和	条件2	boolean2	都为真

是否条件1	boolean1	或	条件2	boolean2	为真

boolean1	AND
boolean2

Name	='frank'	AND
gender='M'

boolean1	OR
boolean2

Name='frank'	OR
Name='Hentry'

是否	boolean	不为真;	如果	boolean	为	UNKNOWN
则返回	UNKNOWN

NOT	boolean

NOT	(NAME	='frank')

OR

NOT

IS	FALSE

是否	boolean	为假;	如果	boolean	为	UNKNOWN	则
返回假

boolean	IS
FALSE

Name	='frank'	IS
FALSE

IS	NOT
FALSE

IS	TRUE

IS	NOT
TRUE

是否	boolean	不为假;	如果	boolean	为	UNKNOWN
则返回真

boolean	IS	NOT
FALSE

Name	='frank'	IS	NOT
FALSE

是否	boolean	为真;	如果	boolean	为	UNKNOWN	则
返回假

boolean	IS
TRUE

Name	='frank'	IS
TRUE

是否	boolean	不为真;	如果	boolean	为	UNKNOWN
则返回真

boolean	IS	NOT
TRUE

Name	='frank'	IS	NOT
TRUE

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

575

查询分析

算术运算符

运算符

描述

语法

示例

+

-

*

/

加号

减号

乘号

除号

A+B

A-B

A*B

A/B

Cost+Profit

Revenue-Cost

Unit_Price*Quantity

Total_Sale/Quantity

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

576

查询分析

字符串运算符

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

577

查询分析

函数

Kyligence	Enterprise	支持如下函数：

算术函数

字符串函数

日期函数

条件函数

类型转换函数

窗口函数

分组函数

交集函数

聚合函数

其他函数

Bitmap	函数

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

578

查询分析

算术函数

语法

说明

示例

基
本
查
询

查
询
下
压

可
定
义
为
可
计
算
列

可
推
荐
为
可
计
算
列

可
用
于
模
型
数
据
筛
选

ABS(numeric)

CEIL(numeric)

FLOOR(numeric)

MOD(numeric1,
numeric2)

SQRT(numeric)

CBRT(numeric)

返回数字（numeric）
的绝对值

返回大于或者等于数字
（numeric）的最小整
数

返回小于或者等于数字
（numeric）的最大整
数

返回被除数
（numeric1）与除数
（numeric2）相除的余
数，	结果的符号与被
除数相同

返回数字（numeric）
的平方根

返回数字（numeric）
的立方根

	ABS(-2)		=	2

✔

✔

✔

✔

✔

	CEIL(-2.2)		=	-2

✔

✔

✔

✔

✔

	FLOOR(-2.2)		=	-3

✔

✔

✔

✔

✔

	MOD(-3,	2)		=	-1

✔

✔

	SQRT(16)		=	4.0

✔

✔

✔

✔

✔

	CBRT(27.0)		=	3.0

✔

✔

✔

✔

✔

HYPOT(numeric1,
numeric2)

返回

	HYPOT(3,	4)		=	5.0

✔

✔

✔

✔

✔

LN(numeric)

返回数字（numeric）
的自然对数

	LN(2)		=
0.6931471805599453

✔

✔

✔

✔

✔

LOG(base,	numeric)

LOG10(numeric)

LOG1P(numeric)

LOG2(numeric)

返回数字（numeric）
以（base）为底的对数

返回数字（numeric）
以	10	为底的对数

返回数字（numeric	+
1）的自然对数

返回数字（numeric）
以	2	为底的对数

	LOG(10,	100)		=	2.0

✔

✔

✔

✔

✔

	LOG10(100)		=	2.0

✔

✔

✔

✔

✔

	LOG1P(0)		=	0.0

✔

✔

✔

✔

✔

	LOG2(2)		=	1.0

✔

✔

✔

✔

✔

EXP(numeric)

返回	e	的	numeric	次幂

	EXP(1)		=
2.718281828459045

✔

✔

✔

✔

✔

EXPM1(numeric)

POWER(numeric1,
numeric2)

RAND([seed])

返回	e	的	numeric	次幂
减	1

返回数字（numeric1）
乘幂（numeric2）的结
果

生成一个大于等于	0	且
小于	1	的随机实数
-	 	seed	： 	可选		用于初
始化随机数生成器

	EXPM1(0)		=	0.0

✔

✔

✔

✔

✔

	POWER(5,2)		=	25.0

✔

✔

✔

✔

✔

	RAND(15)		=
0.45951471073476047

✔

✔

579

查询分析

COS(numeric)

SIN(numeric)

TAN(numeric)

COT(numeric)

ACOS(numeric)

ASIN(numeric)

ATAN(numeric)

始化随机数生成器

返回数字（numeric）
的余弦

	COS(5)		=
0.28366218546322625

✔

✔

✔

✔

✔

返回数字（numeric）
的正弦

	SIN(5)		=
-0.9589242746631385

✔

✔

✔

✔

✔

返回数字（numeric）
的正切

	TAN(5)		=
-3.380515006246586

✔

✔

✔

✔

✔

返回数字（numeric）
的余切

	COT(5)		=
-0.2958129155327455

✔

✔

✔

✔

✔

返回数字（numeric）
的反余弦

	ACOS(0.8)		=
0.6435011087932843

✔

✔

✔

✔

✔

返回数字（numeric）
的反正弦

	ASIN(0.8)		=
0.9272952180016123

✔

✔

✔

✔

✔

返回数字（numeric）
的反正切

	ATAN(0.8)		=
0.6747409422235527

✔

✔

✔

✔

✔

ATAN2(numeric1,
numeric2)

返回坐标	(numeric1,
numeric2)	的反正切

	ATAN2(0.2,	0.8)		=
0.24497866312686414

✔

✔

✔

✔

✔

COSH(numeric)

SINH(numeric)

TANH(numeric)

返回数字（numeric）
的双曲余弦值

返回数字（numeric）
的双曲正弦值

返回数字（numeric）
的双曲正切值

	COSH(0)		=	1.0

✔

✔

✔

✔

✔

	SINH(0)		=	0.0

✔

✔

✔

✔

✔

	TANH(0)		=	0.0

✔

✔

✔

✔

✔

DEGREES(numeric)

将弧度（numeric）转
成角度

	DEGREES(5)		=
286.4788975654116

✔

✔

✔

✔

✔

PI

返回无限接近	π	的数字

	PI		=
3.141592653589793

✔

✔

RADIANS(numeric)

将角度（numeric）转
成弧度

	RADIANS(90)		=
1.5707963267948966

✔

✔

✔

✔

✔

BROUND(numeric1,
numeric2)

将数字（numeric1）取
数字（numeric2）位小
数，向下取整

	BROUND(8.23,	1)		=
8.2
	BROUND(2.5)		=	2.0

ROUND(numeric1,
numeric2)

将数字（numeric1）取
数字（numeric2）位小
数，四舍五入

	ROUND(2.53,	1)		=
2.5
	ROUND(2.5)		=	3

✔

✔

✔

✔

✔

✔

✔

✔

✔

✔

RINT(numeric)

SIGN(numeric)

CONV(numeric,
from_base,	to_base)

CONV(string,
from_base,	to_base)

TRUNCATE(numeric1,
numeric2)

返回值最接近数字
（numeric）的整数，
double	类型。

返回数字（numeric）
的符号

返回数字（numeric）
从基数（from_base）
转换到基数
（to_base）的结果

返回字符串类型的数字
（string）从基数
（from_base）转换到
基数（to_base）的结
果

将数字（numeric1）截
断到数字（numeric2，

	RINT(12.3456)		=
12.0

✔

✔

✔

✔

✔

	SIGN(-5)		=	-1.0

✔

✔

✔

✔

✔

	CONV(-10,	16,	-10)
=	-16

✔

✔

✔

✔

✔

	CONV('100',	2,	10)
=	4

✔

✔

✔

✔

✔

	TRUNCATE(5.55555,2)
=	5.55

✔

✔

✔

✔

✔

580

查询分析

numeric2)

断到数字（numeric2，
默认为	0）

=	5.55

✔

✔

✔

✔

✔

FACTORIAL(numeric)

返回数字（numeric）
的阶乘，如果数字
（numeric）大于	20，
则返回	null

注意：

	FACTORIAL(5)		=	120

✔

✔

✔

✔

✔

	POWER		函数中的参数如果是类似于	 	CAST(2	AS	DOUBLE)		这种常量转换，可能会导致可计算列推荐失败。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

581

查询分析

字符串函数

语法

说明

示例

CHAR_LENGTH(string)

CHARACTER_LENGTH(string)

UPPER(string)

LOWER(string)

POSITION(string1	IN	string2)

返回字符串
（string）长度

返回字符串
（string）长度

返回字符串
（string）为全大写

返回字符串
（string）为全小写

返回字符串
（string1）在字符串
（string2）中的位置

TRIM(	{	BOTH	\	LEADING\
TRAILING	}	string1	FROM
string2)

去掉字符串
（string2）两端／开
头／结尾最长的一个
字符串（string1）

OVERLAY(string1	PLACING
string2	FROM	integer	[	FOR
integer2	])

SUBSTRING(string	FROM
integer)

SUBSTRING(string	FROM
integer1	FOR	integer2)

INITCAP(string)

REPLACE(string,	search,
replacement)

从字符串（string1）
第	integer	位开始将
字符替换为字符串
（string2）

从第	integer	位开
始，取字符串
（string）的部分字
符串

从第	integer1	位开
始，取字符串
（string）中的
integer2	个字符

将字符串（string）
的第一个字母的大写
字母,并将其余的字
母转换成小写，最终
以字符串返回。

将字符串（string）
中的字符串
（search）	替换为字
符串
（replacement）。目
前不支持使用正则表
达式进行字符串匹配

基
本
查
询

✔

✔

✔

✔

✔

✔

✔

✔

✔

✔

	CHAR_LENGTH('Kyligence')		=	9

	CHARACTER_LENGTH('Kyligence')		=	9

	UPPER('Kyligence')		=	KYLIGENCE

	LOWER('Kyligence')		=	kyligence

	POSITION('Kyli'	IN	'Kyligence')		=	1

示例	1： 	TRIM(BOTH	'6'	FROM
'666Kyligence66')
=	Kyligence

示例	2： 	TRIM(LEADING	'6'	FROM
'666Kyligence66')
=	Kyligence66

示例	3： 	TRIM(TRAILING	'6'	FROM
'666Kyligence66')
=	666Kyligence

	OVERLAY('666'	placing	'KYLIGENCE'	FROM	2
for	2)
=	6KYLIGENCE

	SUBSTRING('Kyligence'	FROM	5)
=	gence

	SUBSTRING('Kyligence'	from	5	for	2)
=	ge

	INITCAP('kyligence')
=	Kyligence

	REPLACE('Kyligence','Kyli','Kyliiiiiii')
=	Kyliiiiiiigence

✔

582

查询分析

达式进行字符串匹配
的用法。

BASE64(bin)

将二进制参数转换为
base64	字符串

	BASE64('Spark	SQL')
=	U3BhcmsgU1FM

✔

DECODE(bin,	charset)

ENCODE(string,	charset)

FIND_IN_SET(str,	str_array)

将第一个参数	 	bin
以指定的字符集
	charset		解码。如
果任何一个参数为

null，返回	null。可
选字符集为：
'US_ASCII',	'ISO-
8859-1',	'UTF-8',
'UTF-16BE',	'UTF-
16LE',	'UTF-16'

将第一个参数
	string		以指定的字
符集	 	charset		编
码。如果任一参数为
null，返回	null。可
选字符集为：
'US_ASCII',	'ISO-
8859-1',	'UTF-8',
'UTF-16BE',	'UTF-
16LE',	'UTF-16'

返回	 	str		在
	str_array		中第一
次出现的位
置。 	str_array		为
用逗号分隔的字符
串，如果	 	str	包含
逗号或者在
	str_array		没有发
现	 	str	，则返回
0。若任何参数为
null，返回	null。

	DECODE(ENCODE('abc',	'utf-8'),	'utf-8')
=	abc

✔

	ENCODE('abc',	'utf-8')
=	abc

	FIND_IN_SET('ab','abc,b,ab,c,def')
=	3

LCASE(string)

返回字符串	 	string
的小写形式

	LCASE('SparkSql')
=	sparksql

LEVENSHTEIN(str,	str)

返回两个字符串的编
辑距离

	LEVENSHTEIN('kitten',	'sitting')
=	3

LOCATE(substr,	str[,	pos])

LPAD(str,	len,	pad)

RPAD(str,	len,	pad)

RTRIM(trimStr,	str)

	LOCATE('bar',	'foobarbar')
=	4
	LOCATE('bar',	'foobarbar',	5)
=7

	LPAD('hi',	5,	'??')
=	???hi
	LPAD('hi',	5)
=				hi

	RPAD('hi',	5,	'??')
=	hi???
	RPAD('hi',	5)
=	hi

	RTRIM('KR',	'SPARK')
=	SPA

返回字符串	 	substr
在字符串	 	str		的位
置	 	pos		后第一次出
现的位置

将	 	str		左侧用字符
串	 	pad		填充，直到
长度为	 	len	，如果
	str	长度超过
	len	，会缩短到
	len		个字符

在	 	str		的右侧使用
	pad		填充至长
度 	len	，如果
	str	长度超过
	len	，会缩短到
	len		个字符

从 	str	中右侧去
掉 	trimStr	包含的字
符

将自然语言文本处理
为句子和单词。以数

✔

✔

✔

✔

✔

✔

✔

✔

583

✔

✔

✔

✔

✔

✔

✔

✔

✔

✔

✔

查询分析

SENTENCES(str)

SUBSTRING_INDEX(str,

delim,	count)

UCASE(str)

UNBASE64(str)

ASCII(str)

CHR(str)

SPACE(len)

SPLIT_PART(str,	separator,
index)

为句子和单词。以数
组的形式返回每个句
子中的单词组成的数
组。

使用	 	delim		分割
	str	，返回	 	count
个分割的子串组成的
字符串。如果

	count		为正，返回
左侧的字符串，如果
	count		为负，返回
右侧的字符串

	SENTENCES('Hi	there!	Good	morning.')
=	[["Hi","there"],["Good","morning"]]

	SUBSTRING_INDEX('www.apache.org',	'.',
1)

=	www

返回字符串	 	str		的
大写形式

	UCASE('SparkSql')
=	SPARKSQL

将	base64	的字符串
转换为二进制

	UNBASE64('U3BhcmsgU1FM')
=	Spark	SQL

将字符转换为	ascii
code

将	ascii	code	转换为
对应字符

生成 	len	个连续空
格

将 	str	按 	separator
分割开，然后取
第 	index	个分割后的
部分,	 	index	从	1	开
始，可以为负数，负
数代表从后往前数

	ASCII('a')		=	97

	CHR(97)		=	a

space(2)	=

	split_part('a-b-c',	'-',	1)		=	a,
	split_part('a-b-c',	'-',	-1)		=	c,

concat(any,	[any]*)

将任意类型的多个数
据连接为一个字符串

	concat('Kyli',	'gence',	111)	=
Kyligence111

repeat(str,n)

left(str,n)

REGEXP_EXTRACT(str,
pattern,	index)

将 	str	重复 	n	次返
回。模型查询
时， 	str		支持传入
常量、列和表达
式， 	n	只支持传入
常量

将 	str	从左边开始
的 	n	个字符返回。
模型查询时， 	str
支持传入常量、
列， 	n		只支持传入
常量，当

将字符串	 	str		按照
正则表达式
	pattern		的规则拆
分，返回	 	index		指
定的字符串。
	str		为要匹配的字
符串表达式；
	pattern		必须是一
个	Java	正则表达
式，可以包含多个
组。
	index		指要提取哪
个正则表达式组。为
大于或等于	0	的整
数，默认值为	1。
	index		为	0	则表示

	repeat('kylin',2)		=	'kylinkylin'

	left('kylin',2)		=	'ky'

	regexp_extract('foothebar',	'foo(.*?)
(bar)',	2)		=	'bar'

✔

584

查询分析

	index		为	0	则表示
匹配整个正则表达
式。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

585

查询分析

日期函数

语法

描述

示例

CURRENT_DATE

CURRENT_TIMESTAMP

EXTRACT(timeUnit	FROM	datetime)

返回当前时区的日期。
返回类型为	DATE	格式

返回当前时区的时间戳。
返回类型为	TIMESTAMP	格式

提取返回日期中的指定项。
	timeunit		可以为：
	year	、 	month	、 	day	、
	hour	、 	minute	、 	second

FLOOR(datetime	TO	timeUnit)

CEIL(datetime	TO	timeUnit)

YEAR(date)

QUARTER(date)

以	 	timeUnit		为单位对	 	datetime		向下取
整。
	timeunit		可以为：
	year	、 	quarter	、 	month	、 	week	、 	day	、
	hour	、 	minute	、 	second

以	 	timeUnit		为单位对	 	datetime		向上取
整。
	timeunit		可以为：
	year	、
	quarter	、 	month	、 	week	、 	day	、
	hour	、 	minute	、 	second

返回日期中的年份，
等同于 	EXTRACT(YEAR	FROM	date)	。

	YEAR(date	'2019-01-02')
=	2019

返回日期中的季度，

等同于 	EXTRACT(QUARTER	FROM	date)	。返回值
为	1	到	4	的整数

NOW(date)

返回发送查询的当前时间戳

MONTH(date)

WEEK(date)

DAYOFYEAR(date)

DAYOFMONTH(date)

返回日期中的月份，
等同于	 	EXTRACT(MONTH	FROM	date)	。
返回值为	1	到	12	的整数

返回日期中对应的星期，
等同于	 	EXTRACT(WEEK	FROM	date)	。
返回值为	1	到	53	的整数

返回日期对应年的天数，
等同于	 	EXTRACT(DOY	FROM	date)	。
返回值为	1	到	366	的整数

返回日期对应月的天数，
等同于 	EXTRACT(DAY	FROM	date)	。
返回值为	1	到	31

返回日期对应的星期几，

	CURRENT_DATE
=	2018-10-10

	CURRENT_TIMESTAMP
=	2022-07-19	10:24:44.708

	EXTRACT(minute	FROM	timestamp'2018-
10-10	11:47:16')
=	47

示例	1：
	FLOOR(timestamp'2018-10-10
11:47:16'	TO	year)
=	2018-01-01	00:00:00
示例	2：
	FLOOR(timestamp'2018-10-10
11:47:16'	TO	minute)
=	2018-10-10	11:47:00

示例	1：
	CEIL(timestamp'2018-10-10	11:47:16'
TO	year)
=	2019-01-01	00:00:00
示例	2：
	CEIL(timestamp'2018-10-10	11:47:16'
TO	minute)
=	2018-10-10	11:48:00

	QUARTER(date	'2019-01-02')
=	1

	NOW()
=	2019-09-24	17:19:09.932

	MONTH(date	'2019-01-02')
=	1

	WEEK(date	'2019-01-02')
=	1

	DAYOFYEAR(date	'2019-10-03')
=	276

	DAYOFMONTH(date	'2019-10-03')
=	3

586

查询分析

DAYOFWEEK(date)

HOUR(date)

MINUTE(date)

SECOND(date)

TIMESTAMPADD(timeUnit,	integer,
datetime)

返回日期对应的星期几，
等同于	 	EXTRACT(DOW	FROM	date)	。
返回值为	1	到	7	的整数

	DAYOFWEEK(date	'2019-10-03')
=	5

返回日期中的小时数，
等同于	 	EXTRACT(HOUR	FROM	date)	。返回值为
0	到	23	的整数

	HOUR(timestamp	'2019-01-02
14:01:50')
=	14

返回日期中的分钟数，
等同于	 	EXTRACT(MINUTE	FROM	date)	。

	MINUTE(timestamp	'2019-01-02
14:01:50')

返回结果为	0	到	59	的整数

=	1

返回日期中的秒数，
等同于	 	EXTRACT(SECOND	FROM	date)	。
返回结果为	0	到	59	的整数

返回添加了	 	timeUnit		为单位的时间
	integer		后的日期	 	datetime	，
等同于	 	datetime	+	INTERVAL	'integer'
timeUnit		。
返回类型为	 	datetime
入参	 	datetime	为日期或字符串类型

	SECOND(timestamp	'2019-01-02
14:01:50')
=	50

示例	1：获取一个月后的日期时
间 	TIMESTAMPADD(month,	1,
CURRENT_DATE)
=	2018-11-10

示例	2：获取本月最后一天
	TIMESTAMPADD(day,	-(extract(day
from	CURRENT_DATE)),
timestampadd(month,1,CURRENT_DATE))
=	2018-10-31

	TIMESTAMPDIFF(day,	date'2018-01-
01',	date	'2018-10-10')
=	282

	TRUNC(date	'2009-02-12',	'MM')
=	2009-02-01

	ADD_MONTHS(date	'2016-08-31',	1)
=	2016-09-30

	DATE_ADD(date	'2016-07-30',	1)
=	2016-07-31

	DATE_SUB(date	'2016-07-30',	1)
=	2016-07-29

	FROM_UNIXTIME(0,	'yyyy-MM-dd
HH:mm:ss')
=	1970-01-01	00:00:00

	FROM_UTC_TIMESTAMP(TIMESTAMP'2015-
03-02	06:05:00',	'America/Toronto')
=	2015-03-02	01:05:00.0

TIMESTAMPDIFF(timeUnit,	datetime,
datetime2)

TRUNC(date,	fmt)

以	 	timeUnit		为单位返回	 	datetime		和
	datetime2		的时间差，
等同于	 	(datetime2	-	datetime)/timeUnit
入参	 	datetime		和	 	datetime2		为日期或字符
串类型

返回将	 	date		截断到	 	fmt		指定的单位后的
日期， 	fmt		可以取集合	["year",	"yyyy",	"yy",
"mon",	"month",	"mm"]	中的值

ADD_MONTHS(start_date,	num_months)

返回	 	start_date		后	 	num_months	个月的日期

DATE_ADD(start_date,	num_days)

返回	 	start_date		后	 	num_days	天的日期

DATE_SUB(start_date,	num_days)

返回	 	start_date		前	 	num_days	天的日期

FROM_UNIXTIME(unix_time,	format)

将	 	unix_time		时间转换为	 	format	格式

FROM_UTC_TIMESTAMP(timestamp,
timezone)

假设给定时间戳	 	timestamp		为	UTC	时间，
将其转换为给定时区	 	timezone		的时间戳

MONTHS_BETWEEN(timestamp1,
timestamp2)

返回	 	timestamp1		和	 	timestamp2	月份差，如
果	 	timestamp1		晚于	 	timestamp2	，则结果为
正。以	31	天为基数进行计算。如果两个时间
都是月份中的同一天，或者都是月份中的最
后一天，则返回整数

	MONTHS_BETWEEN('1997-02-28
10:30:00',	'1996-10-30')
=	3.94959677

TO_UTC_TIMESTAMP(timestamp,
timezone)

假设给定时间戳 	timestamp	为给定时
区 	timezone	的时间，将其转换为	UTC	时间
戳

	TO_UTC_TIMESTAMP('2016-08-31',
'Asia/Seoul')
=	2016-08-30	15:00:00

UNIX_TIMESTAMP(datetime,	format)

返回	 	1970-01-01	08:00:00		到	 	datetime		的
秒数，指定	 	datetime		为	 	format		格式

	UNIX_TIMESTAMP('2016-04-08
09:00:00',	'yyyy-MM-dd	HH:mm:ss')
=	1460106000

DATEDIFF(endDate,	startDate)

返回	 	endDate		和	 	startDate		之间的日期差
值，参数为日期或字符串类型

DATEDIFF(date	'2022-02-03',	date
'2022-02-01')
=	2
DATEDIFF('2022-02-03',	'2022-02-01')
=	2

587

查询分析

DATE_TRUNC(unit,	timestamp)

返回将时间戳	 	timestamp		截断到	 	unit		指定
的单位后的日期， 	unit		可以取集合	["year",
"yyyy",	"yy",	"quarter",	"mon",	"month",	"mm",
"week",	"day",	"dd",	"hour",	"minute",	"second",
"millisecond",	"microsecond"]	中的值
入参	 	timestamp	为时间戳或字符串类型

将时间戳转换为 	fmt	格式的字符串。 	expr

SELECT	DATE_TRUNC('second',
TIMESTAMP	'2020-04-30
04:05:06.789')
=	2020-04-30	04:05:06

	date_format('2016-04-08',	'y')

DATE_FORMAT(expr,	fmt)

为	 	DATE	、 	TIMESTAMP		或有效日期时间格式
的字符串， 	fmt		为所需格式的字符串表达式

=2016

_YMDINT_BETWEEN(date_expression1,
date_expression2)

注意：

参数中的日期格式为	 	yyyy-MM-dd	，传回一个
数字，代表	 	date_expression1		和
	date_expression2		之间的差距。
回复值的格式为 	YYYYMMDD	，其中 	YYYY	代表
年数， 	MM	代表月数， 	DD	代表天数。
回复值月数和日数各固定占2位，年数为实际
差值，不向前补位

	_ymdint_between(1990-04-30,	2003-
02-05)
=	120906，表示12年9个月又6天

从	4.6.23.0	版本开始，SQL	中使用	 	CURRENT_DATE	、 	CURRENT_TIMESTAMP	，不加引号时视作函数，加引号时视作列/字
段。在	4.6.23.0	版本之前，加不加引号都视作函数。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

588

查询分析

条件函数

语法

说明

示例

CASE	value
WHEN	value1
THEN	result1
WHEN	valueN
THEN	resultN
ELSE	resultZ	END

CASE	WHEN
condition1	THEN
result1WHEN
conditionN	THEN
resultN	ELSE
resultZ	END

简单	CASE	语句

搜索	CASE	语句

	CASE	OPS_REGION	WHEN
'Beijing'	THEN	'BJ'	WHEN
'Shanghai'	THEN	'SH'WHEN
'Hongkong'	THEN	'HK'	END	FROM
KYLIN_SALES
=	HK	SH	BJ

	CASE	WHEN
OPS_REGION='Beijing'THEN	'BJ'
WHEN	OPS_REGION='Shanghai'
THEN	'SH'	WHEN
OPS_REGION='Hongkong'	THEN
'HK'	END	FROM	KYLIN_SALES
=	HK	SH	BJ

NULLIF(value,
value)

如果两个值相同返回	NULL，否
则返回第一个值

	NULLIF(5,5)
=	null

COALESCE(value,
value	[,	value	]*)

返回第一个不为	NULL	的值

	COALESCE(NULL,NULL,5)
=	5

基
本
查
询

查
询
下
压

可
定
义
为
可
计
算
列

✔

✔

✔

✔

✔

✔

✔

✔

✔

✔

✔

✔

IFNULL(value1,
value2)

如果	value1	为	NULL，返回
value2;	否则返回	value1

	IFNULL('kyligence','apache')
=	'kyligence'

✔

✔

✔

ISNULL(value)

如果	value	为	NULL，返回	true;
否则返回	false

	ISNULL('kyligence')
=	false

✔

✔

✔

NVL(value1,
value2)

如果	value1	为	NULL，返回
value2;	否则返回	value1。value1,
value2	的数据类型必须相同。在
Kyligence	Enterprise	4.2.3	版本之
前，要使用该函数需要在
kylin.properties	中加入配
置： 	kylin.query.calcite.extras-
props.FUN=standard,oracle	。

	NVL('kyligence','apache')
=	'kyligence'

✔

✔

✔

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

589

查询分析

类型转换函数

基
本
查
询

查
询
下
压

可
定
义
为
可
计
算
列

可
推
荐
为
可
计
算
列

可
用
于
模
型
数
据
筛
选

✔

✔

✔

✔

✔

✔

✔

✔

语法

说明

示例

将	 	value		强制
转换成 	type	的
类型，现在支持
的类型

将字符串转换为
日期类型，
等同于
CAST(string	AS
date)

将字符串转换为
日期时间类型，
等同于
CAST(string	AS
timestamp)

示例	1：
将时间类型强制转换成字
符串类型
	CAST(CURRENT_DATE	as
varchar)
=	2018-10-10

示例	1：
	DATE'2018-10-10'
=	2018-10-10

示例	2：返回字符串对应
的日期的月份（与日期函
数	MONTH()	配合使用）
	MONTH(DATE'2018-10-10')
=	10

示例	1：
	TIMESTAMP'2018-10-10
15:57:07
=	2018-10-10	15:57:07

示例	2：返回字符串对应
的日期时间的秒（与日期
函数	SECOND()	配合使
用）
	SECOND(TIMESTAMP'2018-
10-10	15:57:07')
=	7

CAST(value	AS	type)

DATE<String>

TIMESTAMP<String>

注意：

1.	 现仅支持如下类型的转换： 	char	, 	varchar	,	 	boolean	,	 	int	,	 	integer	,	 	tinyint	,	 	smallint	,	 	bigint	,

	float	,	 	double	,	 	decimal	,	 	numeric	,	 	date	,	 	time	,	 	timestamp

2.	 但是现在不支持从	 	bigint		转换到	 	timestamp		类型
3.	 若从	 	char		转换到	 	int		类型， 	char		类型中非数值，则会返回空值
4.	 当其他数据类型转换为	 	char(n)	/ 	varchar(n)		时，长度	n	不会生效

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

590

查询分析

窗口函数

用户可以使用窗口函数来完成更多复杂的查询、简化查询过程并且获得更好的统计结果。

注意：窗口函数目前无法被定义及自动推荐为可计算列。

函数的语法结构

function(value)	OVER	window
window	的组成

partition	by：分组子句，表示窗口函数的计算范围。
order	by:	排序子句，表示分组后，组内数据的排序方式。
rows	/	range：窗口子句，表示分组后，在组内确定一个滑动的数据窗口，窗口函数将根据该窗口包含的数据范
围进行运算。常写为	(rows	|	range)	between	(unbounded	|	[num])	preceding	and	([num]	preceding	|	current	row	|

(unbounded	|	[num])	following)

rows	是物理窗口，即根据	order	by	子句排序后的结果，选取当前行序号的固定前后记录。该子句的结果与
当前行的值无关，只与排序后的行号有关。

例如	sum(column	A)	rows	between	1	preceding	and	2	following	，如当前行的	column	A	排序后序号是3，
那么这个子句的定义就会选择分区中	column	A	序号落在2至5区间的记录。

range	是逻辑窗口，即以当前行对应值为基准，选取当前行对应值的固定前后记录。该子句的结果与排序
后的行号无关，与行的值有关。

例如	sum(column	A)	range	between	1	preceding	and	2	following	，如当前行的	column	A	字段值是3，那么
这个子句的定义就会选择分区中	column	A	字段值落在2至5区间的记录。

如果指定了	order	by	子句，没有指定窗口子句，则默认窗口子句等同于	range	between	unbounded	preceding
and	current	row，代表窗口选取的记录为第一行至当前行。

窗口函数示例

接下来我们以样例数据集中的表	P_LINEORDER	为例，介绍每个函数的使用方法。表中字段及其意义可参考样例数据
集。

ROW_NUMBER

函数说明：ROW_NUMBER()	OVER	window，返回当前行在其分区中的位置，序号不重复。

RANK

函数说明：RANK()	OVER	window，返回当前行在其分区中的位置，可能会有序号空隙。

DENSE_RANK

函数说明：DENSE_RANK()	OVER	window，返回当前行在其分区中的位置，无序号空隙。

查询示例	使用	RANK()	和	DENSE_RANK()	与	ROW_NUMBER()	在同一条查询语句中，查询每个买家购买商品数最
少的前五个订单，进行对比，查询如下：

SELECT	*

FROM	(

SELECT

				ROW_NUMBER()	OVER	w	AS	ROW_NUM,

				RANK()	OVER	w	AS	_RANK,

				DENSE_RANK()	OVER	w	AS	D_RANK,

				LO_ORDERKEY,

				LO_CUSTKEY,

				LO_QUANTITY,

				LO_PARTKEY

591

查询分析

				FROM	SSB.P_LINEORDER

				WINDOW	w	AS	(PARTITION	BY	LO_CUSTKEY	ORDER	BY	LO_QUANTITY)

				)	T

WHERE	ROW_NUM	<=	5;

返回示例

返回结果说明	​	对于买家	'1'	，购买商品个数为1的订单有四条，使用三种排名函数对比如下：

使用	row_number	函数，购买商品个数为1的订单序号为1，2，3，4，购买商品个数为2的订单序号为5。
使用	rank	函数，购买商品个数为1的订单序号为1，1，1，1，购买商品个数为2的订单序号为5（此处存在序号
空隙）。

使用	dense_rank	函数，购买商品个数为1的订单序号为1，1，1，1，购买商品个数为2的订单序号为2（此处不
存在序号空隙）。

NTILE

函数说明：NTILE(value)	OVER	window，将分区内的有序数据尽量按	value	等分，返回组号。

查询示例

将每个买家的订单按照购买商品个数等分为3组，为了完整展示搜索结果，选取商品个数大于等于48的订单进行分
组。

SELECT

				NTILE(3)	OVER	w	AS	N_3,

				LO_ORDERKEY,

				LO_CUSTKEY,

				LO_QUANTITY,

				LO_PARTKEY

FROM	SSB.P_LINEORDER

WHERE	LO_QUANTITY	>=	48

WINDOW	w	AS	(PARTITION	BY	LO_CUSTKEY	ORDER	BY	LO_QUANTITY);

592

查询分析

返回示例

FIRST_VALUE

函数说明：FIRST_VALUE(value)	OVER	window，返回窗口框架中计算行中第一行的值。

LAST_VALUE

函数说明：LAST_VALUE(value)	OVER	window，返回窗口框架中计算行中最后一行的值	。

查询示例

查询按照日期排序的总价格最高的第一个订单和最后一个订单。

SELECT

				FIRST_VALUE(TOTAL1)	OVER	W	AS	FIRST_VALUE_A,

				LAST_VALUE(TOTAL1)	OVER	W	AS	LAST_VALUE_A,

				TOTAL1,

				LO_ORDERDATE

FROM	(

				SELECT

								SUM(LO_ORDTOTALPRICE)	AS	TOTAL1,

								LO_ORDERDATE

				FROM	SSB.P_LINEORDER

				GROUP	BY	LO_ORDERDATE

				)	T	WINDOW	W	AS	(

								ORDER	BY	LO_ORDERDATE	ROWS	BETWEEN	UNBOUNDED	PRECEDING	AND	UNBOUNDED	FOLLOWING

								)

ORDER	BY	LO_ORDERDATE	DESC

593

查询分析

返回示例

LEAD()

函数说明：LEAD(value,	offset,	default)	OVER	window，返回分区内当前行向后的偏移行。其中	value	表示作为
当前值的字段，offset	代表需要基于当前值往后查找	offset	行的数据，default	代表当没有符合条件的值时默认
返回的值，不填写默认返回	null。

LAG()

函数说明：LAG(value,	offset,	default)	OVER	window，返回分区内当前行向前的偏移行。其中	value	表示作为当
前值的字段，offset	代表需要基于当前值往前查找	offset	行的数据，default	代表当没有符合条件的值时默认返
回的值，不填写默认返回	null。

查询示例	查询当前订单和上一个订单、下一个订单的时间。

SELECT

		LO_ORDERKEY,

		LO_CUSTKEY,

		LO_QUANTITY,

		LO_ORDERDATE,

		LEAD(LO_ORDERDATE,	1)	OVER	W	AS	NEXT_DT,

		LAG(LO_ORDERDATE,	1)	OVER	W	AS	LAST_DT

FROM	SSB.P_LINEORDER

WINDOW	W	AS	(PARTITION	BY	LO_CUSTKEY	ORDER	BY	LO_ORDERDATE)

594

查询分析

返回示例

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

595

查询分析

分组函数

在查询语句中经常要使用各种分组汇总，ROLLUP，	CUBE，	GROUPING	SETS	函数就是常用的分组汇总方式。

注意：分组函数暂时无法被定义及推荐为可计算列。

GROUPING	SETS(expression)

在一个结果集中，您有时候需要对列	A，列	B	分别做聚合，同时也要对这两列一起做聚合，实现方法往往是使用多个
UNION	ALL	语句连接起不同的聚合结果。	GROUPING	SETS	子句对聚合查询同时采用不同的分组设置，它可以代替多
个	UNION	ALL	语句，使	SQL	语句更为便捷高效。

函数说明

GROUPING	SETS	子句用于	GROUP	BY	子句后，expression	内填写需要进行分组的维度的组合，例如
GROUPING	SETS((	A	,	B	),	(C)	,	())，意为同时展示对列	A	和列	B	做分组聚合，对列	C	做分组聚合和无分组聚
合三种分组设置的结果。

查询示例

SELECT

				LO_CUSTKEY,

				LO_ORDERKEY,

				SUM(LO_ORDTOTALPRICE)	AS	PRICE

FROM	SSB.P_LINEORDER

GROUP	BY

				GROUPING	SETS((LO_CUSTKEY,LO_ORDERKEY),(LO_ORDERKEY),());

返回示例

CUBE(expression)	和	ROLLUP(expression)

CUBE	和	ROLLUP	可以认为是	GROUPING	SETS	的特殊情况。

596

查询分析

函数说明

CUBE	会对所有的列进行分组统计，最后给出合计。expression	内使用的列会被解析为所有可能的组合形式。
例如	GROUP	BY	CUBE(a,	b,	c)	等价于	GOUPING	SETS((a,b,c),(a,b),(a,c),(b,c),(a),(b),(c),())

ROLLUP	会先对第一个列进行分组统计，最后给出合计。	expression	内使用的列会被解析为包含层级的组合形
式。例如	GROUP	BY	ROLLUP(a,	b,	c)	等价于	GROUPING	SETS((a,b,c),(a,b),(a),	())

查询示例（此处以	ROLLUP	为例）

SELECT

		LO_CUSTKEY,

		LO_ORDERKEY,

		SUM(LO_ORDTOTALPRICE)	AS	PRICE

FROM	SSB.P_LINEORDER

GROUP	BY

		ROLLUP(LO_CUSTKEY,	LO_ORDERKEY);

返回示例

GROUPING(expression)

在使用常用的分组函数	ROLLUP，	CUBE，	GROUPING	SETS	创建的结果列表中，会使用	NULL	作为占位符，所以您
在查看结果时，无法区分	NULL	是占位符还是实际的原始数据中的	NULL。

通过	GROUPING	函数可将占位符	NULL	与原始数据中的	NULL	区分开来。

函数说明

分组函数中涉及的分组列均可用于	GROUPING	函数的	expression	中。如果该函数的返回值为0，意味着	对应行
中分组列下显示的	NULL	来自实际的原始数据，如果返回1，则意味着对应行中分组列下显示的	NULL	是分组
函数产生的的占位符。

查询示例

SELECT

597

查询分析

				LO_CUSTKEY,

				LO_ORDERKEY,

				SUM(LO_ORDTOTALPRICE)	AS	PRICE,

				GROUPING(LO_CUSTKEY)	AS	GC,

				GROUPING(LO_ORDERKEY)	AS	GM

FROM	SSB.P_LINEORDER

GROUP	BY

				GROUPING	SETS((LO_CUSTKEY,LO_ORDERKEY),(LO_ORDERKEY),());

返回示例：

可以看到第一行中两列	GROUPING	函数产生的结果都为1，说明该行	LO_CUSTKEY	和	LO_ORDERKEY	两列中的
NULL	都是由于	GROUPING	SETS	函数产生的占位符。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

598

查询分析

交集函数

用户可以使用交集函数计算两个数据集的交集的值。通常情况下，它们具有一些相同的维度（城市，类别等）和一个变

化的维度（日期等），可以用来计算留存率和转化率。

Kyligence	Enterprise	支持如下交集函数。

INTERSECT_COUNT

说明

返回不同条件下多个结果集交集的去重计数

语法

参数

	intersect_count(column_to_count,	column_to_filter,	filter_value_list)

	column_to_count		指向用于统计去重计数的列，这个列必须已经被添加为精确去重的度量
	column_to_filter		指向可变的维度
	filter_value_list		数组形式，指向可变维度中的值；当	 	column_to_filter		为	varchar	类型时，数组中单个元
素可以映射多个值，默认使用'|'分割，可以使用	 	kylin.query.intersect.separator		配置分隔符，可以取值	 	|
或者	 	,	，默认为	 	|	，仅支持在	 	kylin.properties		文件中配置（目前该参数不支持使用子查询的结果作为参
数使用）。

注意：	当可变维度的数据类型不是	varchar	或	integer	时， 	filter_value_list	中的值需要做显式的类型转换，例
如：	 	select	intersect_count(column_to_count,	column_to_filter,	array[cast(3.53	as	double),	cast(5.79	as
double)])	from	TEST_TABLE		或	 	select	intersect_count(column_to_count,	column_to_filter,	array[TIMESTAMP'2012-
01-02	11:23:45',	TIMESTAMP'2012-01-01	11:23:45'])	from	TEST_TABLE;

查询示例	1

以	Kyligence	Enterprise	的样例数据集为例，事实表	 	KYLIN_SALES		模拟了在线交易数据的记录表。	以下查询语句可
以获得有多少比例的卖家能在新年假期阶段（2012.01.01-2012.01.03）进行持续的在线交易。

select	LSTG_FORMAT_NAME,

intersect_count(SELLER_ID,	PART_DT,	array[date'2012-01-01'])	as	first_day,

intersect_count(SELLER_ID,	PART_DT,	array[date'2012-01-02'])	as	second_day,

intersect_count(SELLER_ID,	PART_DT,	array[date'2012-01-03'])	as	third_day,

intersect_count(SELLER_ID,	PART_DT,	array[date'2012-01-01',date'2012-01-02'])	as	retention_oneday,

intersect_count(SELLER_ID,	PART_DT,	array[date'2012-01-01',date'2012-01-02',date'2012-01-03'])	as	retention

_twoday

from	KYLIN_SALES

where	PART_DT	in	(date'2012-01-01',date'2012-01-02',date'2012-01-03')

group	by	LSTG_FORMAT_NAME

返回示例	1

599

查询分析

结果表示没有卖家在新年阶段进行持续的在线交易。

查询示例	2（column	to	filter	为	varchar	类型时，单元素映射多个值）

		select

		intersect_count(SELLER_ID,	LSTG_FORMAT_NAME,	array['FP-GTC|FP-non	GTC|Others',	'Others'])	as	test_column

		from	kylin_sales

返回示例	2

INTERSECT_VALUE

说明

返回不同条件下多个结果集交集的去重结果。若返回结果较大，可能会导致分析页面浏览器崩溃。

语法

600

查询分析

参数

	intersect_value(column_to_count,	column_to_filter,	filter_value_list)

	column_to_count		指向用于统计去重数据的列，这个列必须已经被添加为精确去重的度量。	仅当类型为
tinyint、smallint或integer且模型重写设置 	kylin.query.skip-encode-integer-enabled=true	时，返回结果为该列
真实值，否则为该列编码后的值。

	column_to_filter		指向可变的维度
	filter_value_list		数组形式，指向可变维度中的值；当	 	column_to_filter		为	varchar	类型时，数组中单个元
素可以映射多个值，默认使用'|'分割，可以使用	 	kylin.query.intersect.separator		配置分隔符，可以取值	 	|
或者	 	,	，默认为	 	|	，仅支持在	 	kylin.properties		文件中配置（目前该参数不支持使用子查询的结果作为参
数使用）。

注意：	当可变维度的数据类型不是	varchar	或	integer	时， 	filter_value_list	中的值需要做显式的类型转换，例
如：	 	select	intersect_value(column_to_count,	column_to_filter,	array[cast(3.53	as	double),	cast(5.79	as
double)])	from	TEST_TABLE		或	 	select	intersect_value(column_to_count,	column_to_filter,	array[TIMESTAMP'2012-
01-02	11:23:45',	TIMESTAMP'2012-01-01	11:23:45'])	from	TEST_TABLE;

查询示例	1

事实表	 	KYLIN_SALES_TEST		模拟了在线交易数据的记录表，其中	SELLER_ID	字段的类型为	integer。
以下查询语句可以获得哪些卖家能在新年假期阶段（2012.01.01-2012.01.03）进行持续的在线交易。

select	LSTG_FORMAT_NAME,

intersect_value(SELLER_ID,	PART_DT,	array[date'2012-01-01'])	as	first_day,

intersect_value(SELLER_ID,	PART_DT,	array[date'2012-01-02'])	as	second_day,

intersect_value(SELLER_ID,	PART_DT,	array[date'2012-01-03'])	as	third_day,

intersect_value(SELLER_ID,	PART_DT,	array[date'2012-01-01',date'2012-01-02'])	as	retention_oneday,

intersect_value(SELLER_ID,	PART_DT,	array[date'2012-01-01',date'2012-01-02',date'2012-01-03'])	as	retention

_twoday

from	KYLIN_SALES

where	PART_DT	in	(date'2012-01-01',date'2012-01-02',date'2012-01-03')

group	by	LSTG_FORMAT_NAME

返回示例	1

结果表示在新年阶段进行持续的在线交易的卖家	id	的集合，以数组的形式展示。

查询示例	2（column	to	filter	为	varchar	类型时，单元素映射多个值）

601

查询分析

select

intersect_value(SELLER_ID,	LSTG_FORMAT_NAME,	array['FP-GTC|FP-non	GTC|Others',	'Others'])	as	test_column

from	kylin_sales

返回示例	2

INTERSECT_COUNT_V2

说明

语法

参数

返回不同条件下多个结果集交集的去重计数，条件支持正则表达式匹配。

	intersect_count_v2(column_to_count,	column_to_filter,	filter_value_list,	filter_type)

	column_to_count		指向用于统计去重计数的列，这个列必须已经被添加为精确去重的度量
	column_to_filter		指向可变的维度
	filter_value_list		数组形式，指向可变维度中的值
	filter_type		类型为	String，标识	filter	的方式，目前有两个可选值	“RAWSTRING”	和	"REGEXP"，当参数值
为	"RAWSTRING"	时的过滤方式为精确过滤，当	 	column_to_filter		为	varchar	类型时，数组中单个元素可以
映射多个值，默认使用'|'分割，可以使用	 	kylin.query.intersect.separator		配置分隔符，可以取值	 	|		或者
	,	，默认为	 	|	，仅支持在	 	kylin.properties		文件中配置（目前该参数不支持使用子查询的结果作为参数使
用）。当参数值为	"REGEXP"	时，过滤方式为正则匹配，只会过滤	column_to_filter	中能够匹配	filter_value_list
中的正则表达式的值。

注意：	当	filter_type	为	"RAWSTRING"	，并且可变维度的数据类型不是	varchar	或	integer
时， 	filter_value_list	中的值需要做显式的类型转换，例如：	 	select	intersect_count_v2(column_to_count,
column_to_filter,	array[cast(3.53	as	double),	cast(5.79	as	double)],	'RAWSTRING')	from	TEST_TABLE		或
	select	intersect_count_v2(column_to_count,	column_to_filter,	array[TIMESTAMP'2012-01-02	11:23:45',

TIMESTAMP'2012-01-01	11:23:45'],	'RAWSTRING')	from	TEST_TABLE;

查询示例	1

	select	intersect_count_v2(

						LSTG_SITE_ID,	LSTG_FORMAT_NAME,

						array['FP.*GTC',	'Other.*'],	'REGEXP')

			from	kylin_sales

602

查询分析

返回示例	1

INTERSECT_VALUE_V2

说明

返回不同条件下多个结果集交集的去重结果。若返回结果较大，可能会导致分析页面浏览器崩溃。条件支持正

则表达式匹配。

语法

参数

	intersect_value_v2(column_to_count,	column_to_filter,	filter_value_list,	filter_type)

	column_to_count		指向用于统计去重计数的列，这个列必须已经被添加为精确去重的度量。	仅当类型为
tinyint、smallint或integer且模型重写设置 	kylin.query.skip-encode-integer-enabled=true	时，返回结果为该列
真实值，否则为该列编码后的值。

	column_to_filter		指向可变的维度
	filter_value_list		数组形式，指向可变维度中的值
	filter_type		类型为	String，标识	filter	的方式，目前有两个可选值	“RAWSTRING”	和	"REGEXP"，当参数值
为	"RAWSTRING"	时的过滤方式为精确过滤，当	 	column_to_filter		为	varchar	类型时，数组中单个元素可以
映射多个值，默认使用'|'分割，可以使用	 	kylin.query.intersect.separator		配置分隔符，可以取值	 	|		或者
	,	，默认为	 	|	，仅支持在	 	kylin.properties		文件中配置（目前该参数不支持使用子查询的结果作为参数使
用）。当参数值为	"REGEXP"	时，过滤方式为正则匹配，只会过滤	column_to_filter	中能够匹配	filter_value_list
中的正则表达式的值。

注意：	当	filter_type	为	"RAWSTRING"	，并且可变维度的数据类型不是	varchar	或	integer
时， 	filter_value_list	中的值需要做显式的类型转换，例如：	 	select	intersect_value_v2(column_to_count,
column_to_filter,	array[cast(3.53	as	double),	cast(5.79	as	double)],	'RAWSTRING')	from	TEST_TABLE		或
	select	intersect_value_v2(column_to_count,	column_to_filter,	array[TIMESTAMP'2012-01-02	11:23:45',

TIMESTAMP'2012-01-01	11:23:45'],	'RAWSTRING')	from	TEST_TABLE;

查询示例	1

	select	intersect_value_v2(

						LSTG_SITE_ID,	LSTG_FORMAT_NAME,

						array['FP.*GTC',	'Other.*'],	'REGEXP')

			from	kylin_sales

603

查询分析

返回示例	1

已知限制

上述函数均不支持查询下压

上述函数均不支持明细索引回答(即使开启开关	kylin.query.use-tableindex-answer-non-raw-query	=	true)

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

604

查询分析

聚合函数

可定义
为可计
算列

可推荐
为可计
算列

语法

说明

示例

AVG(numeric)

返回所有输入值中类型为
numeric	的算术平均值

SUM(numeric)

返回所有输入值中类型为
numeric	的总计值

MAX(value)

返回所有输入值中	value
的最大值

MIN(value)

返回所有输入值中	value
的最小值

	SELECT	AVG(PRICE)	FROM
KYLIN_SALES
=	49.23855638491023

	SELECT	SUM(PRICE)	FROM
KYLIN_SALES
=	244075.5240

	SELECT	MAX(PRICE)	FROM
KYLIN_SALES
=	99.9865

	SELECT	MIN(PRICE)	FROM
KYLIN_SALES
=	0.0008

COUNT(value)

返回所有输入值中	value
不为	NULL	的输入行的
数量

	SELECT	count(PRICE)
FROM	KYLIN_SALES
=	4957

COUNT(*)

返回输入的行数

CORR(value1,
value2)

返回输入的两列的相关性

	SELECT	COUNT(*)	FROM
KYLIN_COUNTRY
=	244

	SELECT
CORR(ITEM_COUNT,	PRICE)
FROM	KYLIN_SALES
=	0.1278

基
本
查
询

查
询
下
压

✔

✔

✔

✔

✔

✔

✔

✔

✔

✔

✔

✔

✔

✔

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

605

查询分析

Bitmap	函数

用户可以使用	Bitmap	函数，从多个模型中分别计算出去重后的	bitmap	结果，再对子查询的	bitmap	做交集操作。

Kyligence	Enterprise	支持如下	Bitmap	函数。

前提条件

您的	Kyligence	Enterprise	版本高于或等于	4.1.6。

BITMAP_UUID

说明

返回一个String，指向一个	bitmap	序列化后的二进制数据。该	bitmap	包含去重后的结果集，可供其他函数进行
二次计算。

语法

参数

	bitmap_uuid(column_to_count)

	column_to_count		指向用于统计去重数据的列，这个列必须已经被添加为精确去重的度量。

查询示例	1

	select	bitmap_uuid(SELLER_ID)	from	KYLIN_SALES	where	PART_DT=date'2012-01-01'

返回示例	1

结果返回一个	String	，指向一个用户不可见的	bitmap	序列化后的二进制数据，表示元旦在线交易的卖家	id	的集
合，供其他函数进行二次计算。

INTERSECT_BITMAP_UUID

说明

返回一个String，指向一个	bitmap	序列化后的二进制数据。该	bitmap	包含多个去重结果集的交集，供其他函数
进行二次计算。

606

查询分析

语法

参数

	intersect_bitmap_uuid(column_to_count,	column_to_filter,	filter_value_list)

	column_to_count		指向用于统计去重数据的列，这个列必须已经被添加为精确去重的度量。
	column_to_filter		指向可变的维度
	filter_value_list		数组形式，指向可变维度中的值；当	 	column_to_filter		为	varchar	类型时，数组中单个元
素可以映射多个值，默认使用'|'分割，可以使用	 	kylin.query.intersect.separator		配置分隔符，可以取值	 	|
或者	 	,	，默认为	 	|	，仅支持在	 	kylin.properties		文件中配置（目前该参数不支持使用子查询的结果作为参
数使用）。

注意：	当可变维度的数据类型不是	varchar	或	integer	时， 	filter_value_list	中的值需要做显式的类型转换，例
如：	 	select	intersect_bitmap_uuid(column_to_count,	column_to_filter,	array[cast(3.53	as	double),	cast(5.79
as	double)])	from	TEST_TABLE		或	 	select	intersect_bitmap_uuid(column_to_count,	column_to_filter,
array[TIMESTAMP'2012-01-02	11:23:45',	TIMESTAMP'2012-01-01	11:23:45'])	from	TEST_TABLE;

查询示例	1

LSTG_FORMAT_NAME	字段类型为	VARCHAR(4096)，作为可变维度列。

select	intersect_bitmap_uuid(

								SELLER_ID,	LSTG_FORMAT_NAME,

								array['FP-GTC|FP-non	GTC',	'Others'])

				from	KYLIN_SALES

返回示例	1

结果返回一个	String	，指向一个用户不可见的	bitmap	序列化后的二进制数据，表示同时进行过类型为	'FP-GTC'	和
'Others'，或	'FP-non	GTC'	和	'Others'	两种交易的用户的去重合集。该去重合集可供其他函数进行二次计算。

INTERSECT_BITMAP_UUID_V2

说明

返回一个String，指向一个	bitmap	序列化后的二进制数据。该	bitmap	包含多个去重结果集的交集，供其他函数
进行二次计算。

语法

607

查询分析

参数

	intersect_bitmap_uuid_v2(column_to_count,	column_to_filter,	filter_value_list,	filter_type)

	column_to_count		指向用于统计去重数据的列，这个列必须已经被添加为精确去重的度量。
	column_to_filter		指向可变的维度
	filter_value_list		数组形式，指向可变维度中的值
	filter_type		类型为	String，标识	filter	的方式，目前有两个可选值	“RAWSTRING”	和	"REGEXP"，当参数值
为	"RAWSTRING"	时的过滤方式为精确过滤，当	 	column_to_filter		为	varchar	类型时，数组中单个元素可以
映射多个值，默认使用'|'分割，可以使用	 	kylin.query.intersect.separator		配置分隔符，可以取值	 	|		或者
	,	，默认为	 	|	，仅支持在	 	kylin.properties		文件中配置（目前该参数不支持使用子查询的结果作为参数使
用）。当参数值为	"REGEXP"	时，过滤方式为正则匹配，只会过滤	column_to_filter	中能够匹配	filter_value_list
中的正则表达式的值。

注意：	当	filter_type	为	"RAWSTRING"	，并且可变维度的数据类型不是	varchar	或	integer
时， 	filter_value_list	中的值需要做显式的类型转换，例如：	 	select
intersect_bitmap_uuid_v2(column_to_count,	column_to_filter,	array[cast(3.53	as	double),	cast(5.79	as	double)],
'RAWSTRING')	from	TEST_TABLE		或	 	select	intersect_bitmap_uuid_v2(column_to_count,	column_to_filter,
array[TIMESTAMP'2012-01-02	11:23:45',	TIMESTAMP'2012-01-01	11:23:45'],	'RAWSTRING')	from	TEST_TABLE;

查询示例	1

LSTG_FORMAT_NAME	字段类型为	VARCHAR(4096)，作为可变维度列。

select	intersect_bitmap_uuid_v2(

								SELLER_ID,	LSTG_FORMAT_NAME,

								array['FP.*GTC',	'Other.*'],	'REGEXP')

				from	KYLIN_SALES

返回示例	1

结果返回一个	String	，指向一个用户不可见的	bitmap	序列化后的二进制数据，正则表达式能匹配到	'FP-GTC',	'FP-
non	GTC'	和	'Others'，表示进行过类型为	'FP-GTC'	和	'Others'，或	'FP-non	GTC'	和	'Others'	两种交易的用户的去重合
集。该去重合集可供其他函数进行二次计算。

INTERSECT_COUNT_BY_COL

说明

608

查询分析

语法

参数

对	bitmap	序列化后的二进制数据进行反序列化，	然后再进行交集操作，返回去重计数。

	intersect_count_by_col(Array[t1.c1,t2.c2	...])

	t1.c1,	t2.c2	...		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。能返回该类型的函数
有，bitmap_uuid	和	intersect_bitmap_uuid	和	intersect_bitmap_uuid_v2。

查询示例	1

select	intersect_count_by_col(Array[t1.a1,t2.a2])	from

				(select	bitmap_uuid(SELLER_ID)	as	a1

								from	KYLIN_SALES)	t1,

				(select	intersect_bitmap_uuid(

								SELLER_ID,	LSTG_FORMAT_NAME,

								array['FP-GTC|FP-non	GTC',	'Others'])	as	a2

from	KYLIN_SALES)	t2

返回示例	1

子查询中的两个bitmap	，分别由	bitmap_uuid	和	intersect_bitmap_uuid	提供。intersect_count_by_col	函数对这两个
bitmap	进行交集操作，并返回去重计数。

INTERSECT_BITMAP_UUID_COUNT

说明

语法

参数

通过	uuid	，对	bitmap	序列化后的二进制数据进行反序列化，然后再进行交集操作，返回去重计数。

	intersect_bitmap_uuid_count(uuid)

	uuid		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。

查询示例	1

select	intersect_bitmap_uuid_count(uuid)

from	(

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['1-URGENT'])	as	uuid

from	SSB.LINEORDER

609

查询分析

union

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['2-HIGH'])	as	uuid

from	SSB.LINEORDER

)

返回示例	1

子查询中的两个bitmap	，分别由两个	intersect_bitmap_uuid	提供。intersect_bitmap_uuid_count	函数对这两个	bitmap
进行交集操作，并返回去重计数。

INTERSECT_BITMAP_UUID_VALUE_ALL

说明

通过	uuid	，对	bitmap	序列化后的二进制数据进行反序列化，然后再进行交集操作，返回去重结果。

语法

参数

	intersect_bitmap_uuid_value_all(uuid)

	uuid		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。

查询示例	1

select	intersect_bitmap_uuid_value_all(uuid)

from	(

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['1-URGENT'])	as	uuid

from	SSB.LINEORDER

union

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['2-HIGH'])	as	uuid

from	SSB.LINEORDER

)

返回示例	1

子查询中的两个bitmap	，分别由两个	intersect_bitmap_uuid	提供。intersect_bitmap_uuid_value_all	函数对这两个
bitmap	进行交集操作，并返回去重结果。

INTERSECT_BITMAP_UUID_VALUE

说明

通过	uuid	，对	bitmap	序列化后的二进制数据进行反序列化，然后再进行交集操作，根据	limit	、offset	返回去
重结果。

语法

参数

	intersect_bitmap_uuid_value(uuid,limit,offset)

	uuid		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。
	limit		返回结果集大小限制。
	offset		返回结果集的偏移量。

查询示例	1

select	intersect_bitmap_uuid_value(uuid,10,10)

from	(

610

查询分析

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['1-URGENT'])	as	uuid

from	SSB.LINEORDER

union

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['2-HIGH'])	as	uuid

from	SSB.LINEORDER

)

返回示例	1

子查询中的两个bitmap	，分别由两个	intersect_bitmap_uuid	提供。intersect_bitmap_uuid_value	函数对这两个	bitmap
进行交集操作，并返回去重结果。

INTERSECT_BITMAP_UUID_DISTINCT

说明

通过	uuid	，对	bitmap	序列化后的二进制数据进行反序列化，然后再进行交集操作，返回一个String，指向一个
bitmap	序列化后的二进制数据。

语法

参数

	intersect_bitmap_uuid_distinct(uuid)

	uuid		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。

查询示例	1

select	intersect_bitmap_uuid_distinct(uuid)

from	(

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['1-URGENT'])	as	uuid

from	SSB.LINEORDER

union

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['2-HIGH'])	as	uuid

from	SSB.LINEORDER

)

返回示例	1

子查询中的两个bitmap	，分别由两个	intersect_bitmap_uuid	提供。intersect_bitmap_uuid_distinct	函数对这两个	bitmap
进行交集操作，并返回一个String，指向一个	bitmap	序列化后的二进制数据。

UNION_BITMAP_UUID_COUNT

说明

通过	uuid	，对	bitmap	序列化后的二进制数据进行反序列化，然后再进行并集操作，返回去重计数。

语法

参数

	union_bitmap_uuid_count(uuid)

	uuid		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。

查询示例	1

select	union_bitmap_uuid_count(uuid)

from	(

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['1-URGENT'])	as	uuid

611

查询分析

from	SSB.LINEORDER

union

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['2-HIGH'])	as	uuid

from	SSB.LINEORDER

)

返回示例	1

子查询中的两个bitmap	，分别由两个	intersect_bitmap_uuid	提供。union_bitmap_uuid_count	函数对这两个	bitmap	进
行并集操作，并返回去重计数。

UNION_BITMAP_UUID_VALUE_ALL

说明

语法

参数

通过	uuid	，对	bitmap	序列化后的二进制数据进行反序列化，然后再进行并集操作，返回去重结果。

	union_bitmap_uuid_value_all(uuid)

	uuid		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。

查询示例	1

select	union_bitmap_uuid_value_all(uuid)

from	(

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['1-URGENT'])	as	uuid

from	SSB.LINEORDER

union

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['2-HIGH'])	as	uuid

from	SSB.LINEORDER

)

返回示例	1

子查询中的两个bitmap	，分别由两个	intersect_bitmap_uuid	提供。union_bitmap_uuid_value_all	函数对这两个	bitmap
进行并集操作，并返回去重结果。

UNION_BITMAP_UUID_VALUE

说明

通过	uuid	，对	bitmap	序列化后的二进制数据进行反序列化，然后再进行并集操作，根据	limit	、offset	返回去
重结果。

语法

参数

	union_bitmap_uuid_value(uuid,limit,offset)

	uuid		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。
	limit		返回结果集大小限制。
	offset		返回结果集的偏移量。

查询示例	1

select	union_bitmap_uuid_value(uuid,10,10)

612

查询分析

from	(

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['1-URGENT'])	as	uuid

from	SSB.LINEORDER

union

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['2-HIGH'])	as	uuid

from	SSB.LINEORDER

)

返回示例	1

子查询中的两个bitmap	，分别由两个	intersect_bitmap_uuid	提供。union_bitmap_uuid_value	函数对这两个	bitmap	进
行并集操作，并返回去重结果。

UNION_BITMAP_UUID_DISTINCT

说明

语法

参数

通过	uuid	，对	bitmap	序列化后的二进制数据进行反序列化，然后再进行并集操作，返回一个String，指向一个
bitmap	序列化后的二进制数据。

	union_bitmap_uuid_distinct(uuid)

	uuid		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。

查询示例	1

select	union_bitmap_uuid_distinct(uuid)

from	(

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['1-URGENT'])	as	uuid

from	SSB.LINEORDER

union

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['2-HIGH'])	as	uuid

from	SSB.LINEORDER

)

返回示例	1

子查询中的两个bitmap	，分别由两个	intersect_bitmap_uuid	提供。union_bitmap_uuid_distinct	函数对这两个	bitmap
进行并集操作，并返回一个String，指向一个	bitmap	序列化后的二进制数据。

BITMAP_UUID_TO_ARRAY

说明

语法

参数

通过	uuid	，对	bitmap	序列化后的二进制数据进行反序列化，返回数组。

	bitmap_uuid_to_array(uuid)

	uuid		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。

查询示例	1

select	bitmap_uuid_to_array(uuid)

from	(

613

查询分析

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['1-URGENT'])	as	uuid

from	SSB.LINEORDER

union

select	intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['2-HIGH'])	as	uuid

from	SSB.LINEORDER

)

返回示例	1

子查询中的两个bitmap	，分别由两个	intersect_bitmap_uuid	提供。union_bitmap_uuid_distinct	函数对这两个	bitmap
进行反序列化操作，并返回数组。

SUBTRACT_BITMAP_UUID_COUNT

说明

通过	uuid	，对	bitmap	序列化后的二进制数据进行反序列化，然后再进行差集操作，返回去重计数。

语法

参数

	subtract_bitmap_uuid_count(uuid1,uuid2)

	uuid1		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。
	uuid2		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。

查询示例	1

select	subtract_bitmap_uuid_count(uuid1,uuid2)

from	(

select

intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['1-URGENT'])	as	uuid1,

intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['2-HIGH'])	as	uuid2

from	SSB.LINEORDER

)

返回示例	1

子查询中的两个bitmap	，分别由两个	intersect_bitmap_uuid	提供。subtract_bitmap_uuid_count	函数对这两个	bitmap
进行差集操作，并返回去重计数。

SUBTRACT_BITMAP_UUID_VALUE_ALL

说明

通过	uuid	，对	bitmap	序列化后的二进制数据进行反序列化，然后再进行差集操作，返回去重结果。

语法

参数

	subtract_bitmap_uuid_value_all(uuid1,uuid2)

	uuid1		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。
	uuid2		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。

查询示例	1

select	subtract_bitmap_uuid_value_all(uuid1,uuid2)

from	(

614

查询分析

select

intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['1-URGENT'])	as	uuid1,

intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['2-HIGH'])	as	uuid2

from	SSB.LINEORDER

)

返回示例	1

子查询中的两个bitmap	，分别由两个	intersect_bitmap_uuid	提供。subtract_bitmap_uuid_value_all	函数对这两个
bitmap	进行差集操作，并返回去重结果。

SUBTRACT_BITMAP_UUID_VALUE

说明

通过	uuid	，对	bitmap	序列化后的二进制数据进行反序列化，然后再进行差集操作，根据	limit	、offset	返回去
重结果。

语法

参数

	subtract_bitmap_uuid_value(uuid1,uuid2,limit,offset)

	uuid1		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。
	uuid2		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。
	limit		返回结果集大小限制。
	offset		返回结果集的偏移量。

查询示例	1

select	subtract_bitmap_uuid_value(uuid1,uuid2,10,10)

from	(

select

intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['1-URGENT'])	as	uuid1,

intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['2-HIGH'])	as	uuid2

from	SSB.LINEORDER

)

返回示例	1

子查询中的两个bitmap	，分别由两个	intersect_bitmap_uuid	提供。subtract_bitmap_uuid_value	函数对这两个	bitmap
进行差集操作，并返回去重结果。

SUBTRACT_BITMAP_UUID_DISTINCT

说明

通过	uuid	，对	bitmap	序列化后的二进制数据进行反序列化，然后再进行差集操作，返回一个String，指向一个
bitmap	序列化后的二进制数据。

语法

参数

	subtract_bitmap_uuid_distinct(uuid1,uuid2)

	uuid1		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。
	uuid2		子查询的	bitmap	列，每一个列都指向一个对用户不可见的	bitmap	。

615

查询分析

查询示例	1

select	subtract_bitmap_uuid_distinct(uuid1,uuid2)

from	(

select

intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['1-URGENT'])	as	uuid1,

intersect_bitmap_uuid(	LO_CUSTKEY,	LO_ORDERPRIOTITY,		array['2-HIGH'])	as	uuid2

from	SSB.LINEORDER

)

返回示例	1

子查询中的两个bitmap	，分别由两个	intersect_bitmap_uuid	提供。subtract_bitmap_uuid_distinct	函数对这两个	bitmap
进行差集操作，并返回一个String，指向一个	bitmap	序列化后的二进制数据。

已知限制

上述函数均不支持查询下压

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

616

查询分析

其他函数

UUID()

MONOTONICALLY_INCREASING_ID()

EXPLODE(array)

SIZE(expr)

语法

描述

示例

可
定
义
为
可
计
算
列

基
本
查
询

查
询
下
压

✔

返回通用唯
一识别码
（UUID）。
该值以规范
的	36	个字
符的字符串
形式返回

返回单调递
增的最大	64
位的整数。
生成的	ID
单调递增且
唯一，但不
连续。

返回array展
开后的多行
数据。array
中的每一个
元素都会对
应一行

expr	必须为
array	或者
map	类型，
返回	array
或	map	中包
含的元素个
数。

	UUID()
=	46707d92-02f4-4817-8116-
a4c3b23e6266

	MONOTONICALLY_INCREASING_ID()
=	1111111

✔

✔

	EXPLODE(array[1,	2,	3])
=
1
2
3

✔

	SIZE(array(1,	2,	3))
=
3

✔

✔

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

617

查询分析

为查询指定模型优先级

当一个项目中有多个就绪的模型时，系统会自动为每个查询选择最合适的模型。但有时，用户希望直接指定查询要击中

的模型，而不是由系统自动判断。这时就可以使用在	SQL	中添加相关	hint。

Model	Priorities	Hint

语法

SELECT	/*+	MODEL_PRIORITY(model1,	model2)	*/	col1,	col2	from	....

Hint	由	 	/*+		开始	 	*/		结束，必须放在	 	SELECT		的后面， 	SELECT		和	 	/*+	..	*/		中间不能有其他的内容。

该语法从	Kyligence	Enterprise	4.2.4	开始支持。Model	Priorities	Hint	使用	 	/*+	MODEL_PRIORITY(model1,	model2)	*/		指定，
MODEL_PRIORITY	接受任意个数的模型名作为参数，模型的优先级从左到右递减，没有出现在	MODEL_PRIORITY	中
的模型优先级最低。	当前	model	priority	hint	会对整个查询生效，如果	SQL	中出现多个	model	priority	hint	以第一个为
准。

在模型匹配过程中，如果同时有多个模型可以回答该查询，则会使用	MODEL_PRIORITY	中定义的模型优先级，优先选
取优先级高的模型作为查询对象。

从	4.6.22.0	版本，如果需要仅通过指定特定模型回答查询，可添加配置项	 	kylin.query.use-only-in-priorities=true		并
使用	 	MODEL_PRIORITY(...)		指定模型，其优先级从左到右递减，当	 	MODEL_PRIORITY(...)		中包含的模型无法回答查询
时，查询将下压。该参数可以在项目级生效，默认值为	 	false	。

例子

SELECT	/*+	MODEL_PRIORITY(model1,	model2)	*/	col1,	col2	from	table;

若该查询可以同时被	model1	和	model2	回答，根据	SQL	中的	MODEL_PRIORITY	,	Kyligence	Enterprise	会选择	model1	回
答该查询。

兼容	Kyligence	Enterprise	3	的语法

Kyligence	Enterprise	4	对于	Kyligence	Enterprise	3	在SQL中指定模型优先级的语法做了兼容，语法如下

--	CubePriority(model1,model2)

select	....	from	...

注释中关键字	CubePriority	后的括弧内包含一串由	,	分割的	Model	名字，它们的优先级从高到低排列。以上例，假如
Model1	和	Model2	都能满足查询，那么系统将优先使用	Model1。

注意

1.	 CubePriority	关键字大小写敏感，且其后的括号前后内不能有多余的空格。不准确的拼写将导致系统无法识别该注

释选项。

2.	 如果	SQL	中包含多条	CubePriority	注释选项，则只有第一条会生效，其他的会被忽略。
3.	 如果同时存在	 	MODEL_PRIORITY		和	 	CubePriority	，则只有	 	MODEL_PRIORITY		会生效

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

618

查询历史

查询历史

您在	Kyligence	Enterprise	中执行的所有查询分析都会保存在查询历史中，您可以通过导航栏查询	->	查询历史查看相关
信息。此界面保存了查询的基本信息，如查询时间、SQL	语句、查询用户等，可以帮助您记录查询行为，以及更好地管
理或优化模型。本节我们为您介绍查询历史界面的内容。

准备工作

1.	 在介绍查询历史界面之前，我们建议您先执行几条查询语句，这样更有助于您阅读下文的介绍。

2.	 下文我们以快速开始章节中建立的模型为例，介绍查询历史界面。在快速指南章节完成后且监控	->	任务界面的任

务也完全执行完毕后，我们可以在查询	->	分析界面执行以下查询语句。

查询	1：查询收入总额。

select	SUM(LO_REVENUE)	as	TOTAL_REVENUE	from	SSB.P_LINEORDER

提示：存在对列	LO_REVENUE	的度量	SUM。

查询	2：查询订单总额。

select	SUM(LO_ORDTOTALPRICE)	from	SSB.P_LINEORDER

提示：不存在对列	LO_ORDTOTALPRICE	的度量	SUM。

查询	3：查询商品名称。

select	P_NAME	from	SSB.P_LINEORDER

提示：这是一个错误查询，因为表	P_LINEORDER	中不存在字段	P_NAME。

查询历史界面

请您进入导航栏查询	->	查询历史界面，在执行过上述	SQL	查询语句之后，您会看到如下内容。

图片中的每一行为您的一次历史查询，列的含义如下：

开始时间：提交查询的时间。

用时：执行完成查询所用的时间。如果查询失败，则显示为空。

查询	ID：每条查询对应的唯一	ID	号，这是自动生成的序号。

SQL：查询的	SQL	语句。

对象：查询击中的查询对象，	有以下类型：	模型名称，HIVE，RDBMS、CONSTANTS，您可在顶部筛选查询对
象：

619

查询历史

Hive：表示查询下压至	Hive
RDBMS：表示查询下压至	RDBMS	数据源
CONSTANTS：表示查询常量
模型名称：表示查询击中的模型名称，您可以勾选”全选“表示查看所有击中模型的查询，结果包含只是击中快
照的查询。筛选框中的模型来自模型列表，根据被击中的次数降序排列后仅展示前	100	个模型，您可以在筛选
下拉框首部搜索希望筛选的模型

状态：两种查询状态。击中模型和查询下压的查询显示为成功，语法错误、语法不支持和超时的查询显示为失败。

节点：提交查询的节点的主机名:端口

提交人：提交查询的	Kyligence	Enterprise	用户

操作：下载查询诊断包

当您点击某一条查询左侧的图标，将展示该条查询的执行详情，如下图所示：

左侧为	SQL	语句，您可以复制粘贴再查询。SQL	语句默认按照输入时的格式展示，如果需要系统自动规范格式，您可
点击重排格式按钮，该功能需要浏览器版本为谷歌	Chrome	74	及以上，Internet	Explorer	浏览器不支持该功能。

右侧的字段含义如下：

查询	ID：每条查询对应的唯一	ID	号，这是自动生成的序号。
用时：执行完成查询所用的时间。如果查询失败，则显示为空。当您在进行慢查询优化时，需要了解查询的具体执

行步骤，定位耗时原因。可将鼠标悬停在响应时间上，以查看当前查询的详细执行步骤及耗时，辅助分析。

对象：查询击中模型将显示模型名称，HIVE	表示查询下压至	Hive，RDBMS	表示查询下压至	RDBMS	数据
源，CONSTANTS	表示查询常量。
击中快照：查询击中快照将显示快照名称

索引	ID：查询击中的索引的	ID。
扫描行数：查询总共扫描行数。

扫描字节：查询总共扫描字节数。

结果行数：查询结果行数。

击中缓存：查询是否击中缓存。

缓存类型：查询击中缓存时，显示击中的缓存类型。 	EHCACHE		代表	EHCACHE	缓存， 	REDIS		代表	REDIS	分布式
缓存。

当您点击某一条查询失败右侧的错误详情，将展示该条查询的异常详情，如下图所示：

620

查询历史

注意：SQL	未换行时，查询执行详情中仅能看到前	100	行	SQL,	SQL	换行时，详情显示前	2000	个字符.您可以点
击	SQL	语句框内右上角的复制按钮复制完整的	SQL	语句。

Kyligence	Enterprise	使用内置的	RDBMS	数据库保存查询的相关信息，您可以在附录查询历史字段表中查阅所有和查询
历史相关的字段及含义。

查询历史留存

为了保证查询历史的读写性能和数据库稳定性，Kyligence	Enterprise	为查询历史设有默认留存上限：

默认总留存	1000	万条数据，可通过在	 	kylin.properties		中配置	 	kylin.query.queryhistory.max-size		进行调整

其中单个项目最多默认留存	100	万条数据，可通过在	 	kylin.properties		中配置
	kylin.query.queryhistory.project-max-size		进行调整

总留存时间为	30	天，可通过在	 	kylin.properties		中配置	 	kylin.query.queryhistory.survival-time-threshold		进行
调整

导出查询历史

查询历史支持导出为	csv	文件，如下图所示，导出结果为筛选过滤后的数据

也可单独将查询历史中的	SQL	导出为	text	文件，如下图所示，导出结果同样为筛选过滤后的数据

查询历史支持配置导出上限，默认值为	10	万条	 	kylin.query.query-history-download-max-size=100000

621

查询历史

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

622

查询优化

查询优化

本章将介绍在	Kyligence	Enterprise	中的一些查询优化方法。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

623

查询优化

使用	Left	Join	模型回答等价语义的	Inner	Join	查询

Kyligence	Enterprise	在默认情况下，查询	SQL	中表的关联关系必需与模型中定义事实表和维表的关联关系一致，即
	Left	Join		的模型不能回答	 	Inner	Join		的查询。

但在某些情况下，部分	 	Left	Join		查询在语义上可以等价转化为	 	Inner	Join		查询，因此我们提供了配置参数，可以
允许用户使用	 	Left	Join		的模型回答等价语义的	 	Inner	Join		查询。

配置参数开始生效版本为	Kyligence	Enterprise	4.2.4，此配置为全局配置，默认关闭。

场景一

	[Table	A]	Left	Join	[Table	B]	Inner	Join	[Table	C]		语义等价于	 	[Table	A]	Inner	Join	[Table	B]	Inner	Join	[Table
C]	。

原因是，当	 	Left	Join		之后再做	 	Inner	Join		，与最后一个右表不匹配的行都会被筛除，所以上述两个表达式在语义
上是等价的。

使用	 	kylin.query.join-match-optimization-enabled=true		配置，Kyligence	Enterprise	可以支持	 	Left	Join		的模型回答上
述等价语义的	 	Inner	Join		查询。

举例	1

模型定义为	 	KYLIN_SALES	Left	Join	KYLIN_ACCOUNT	Inner	Join	KYLIN_COUNTRY

有	SQL	如下：

select	kylin_country.name

from	kylin_sales	inner	join	kylin_account	on	kylin_sales.buyer_id	=	kylin_account.account_id

inner	join	kylin_country	on	kylin_account.account_country	=	kylin_country.country

上述模型	可以回答此	SQL。

举例	2

模型定义为	 	[Table	A]	Left	Join	[Table	B]	Left	Join	[Table	C]	Inner	Join	[Table	D]	Left	Join	[Table	E]

有	SQL	如下：	 	[Table	A]	Inner	Join	[Table	B]	Inner	Join	[Table	C]	Inner	Join	[Table	D]	Left	Join	[Table	E]

上述模型	可以回答此	SQL。

场景二

有	SQL	具有如下特征：	 	[Table	A]	Left	Join	[Table	B]		且过滤条件中	 	[Table	B]	的任意列具有非空约束，则该	SQL
语义等价于	 	[Table	A]	Inner	Join	[Table	B]	。

使用	 	kylin.query.join-match-optimization-enabled=true		配置，Kyligence	Enterprise	可以支持	 	Left	Join		的模型回答上
述等价语义的	 	Inner	Join		查询。

其中列具有非空约束需要满足条件：存在	 	isNotNull		类过滤条件， 	isNotNull		对应常见比较运算
符： 	=	， 	<>	， 	>	， 	<	， 	<=	， 	>=	， 	like	， 	in	， 	not	like	， 	not	in	等。

而	 	isNULL		过滤条件则不具备非空约束，例如	 	IS	NULL	。

同时，目前暂不支持	 	IS	DISTINCT	FROM	， 	CASE	WHEN		过滤条件的等价转换，该过滤条件会被自动忽略，见已知限制1。

624

查询优化

举例	1

模型定义为： 	TEST_ACCOUNT	left	join	TEST_ORDER	left	join	TEST_ACCOUNT

有	SQL	如下，可以击中上述模型，因为存在非空约束的过滤条件。

select	SUM(a.ITEM_COUNT)	as	SUM_ITEM_COUNT

from	TEST_KYLIN_FACT	a

left	join	TEST_ORDER	b	on	a.ORDER_ID	=	b.ORDER_ID

inner	join	TEST_ACCOUNT	c	on	b.BUYER_ID	=	c.ACCOUNT_ID

where	c.ACCOUNT_COUNTRY	=	'CN'	and	(c.ACCOUNT_COUNTRY	like	'%US'	or	c.ACCOUNT_COUNTRY	is	null)

举例	2

模型定义为：	 	[Table	A]	inner	join	[Table	B]

有	SQL	如下，可以击中此模型：

A	left	join	B	where	B.nonfk	=	'123'	and	B.col1	in	('ab',	'ac')

A	left	join	B	where	A.col	is	null	and	B.col1	like	'xxx'

A	left	join	B	where	B.col	between	100	and	100000

A	left	join	B	where	A.fk	is	null	and	B.col1	=	'something'

A	left	join	B	where	b.col	=	'something'	and	(b.col	=	'xxx'	or	b.col	is	null)

A	left	join	B	where	abs(b.col)	=	123

A	left	join	B	where	floor(b.col)	=	123

如下SQL无法击中此的模型：

A	left	join	B	where	B.col1	=	'xx'	or	A.col2	=	'yy'

A	left	join	B	where	B.col1	=	'xx'	or	B.col2	is	null

场景三

现在有模型 	[Table	A]	Left	Join	[Table	B]	left	join	[Table	C]	。

如下SQL如下，可以击中此模型：

A	inner	join	B	inner	join	C	where	C.col	=	'abc'

原因是表	C	中的列存在非空约束，因此查询可以等价为：

A	LEFT_OR_INNER	join	B	LEFT_OR_INNER	join	C	where	C.col	=	'abc'

场景三是场景一和场景二的混合。

已知限制

1.	 对于场景二，在非空约束的判断中，暂不支持	 	IS	DISTINCT	FROM	， 	CASE	WHEN		表达式。
2.	 同样对于场景二，在非空约束的判断中，暂不支持聚合函数的非空判断，例如	 	HAVING	SUM(PRICE)	>	0	。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

625

查询优化

查询	Segment	剪枝

从	Kyligence	Enterprise	4.3.2	版本开始，我们支持在构建	Segment	时计算所有维度的维度值范围（最大值和最小值），因
此查询时可以进行	Segment	剪枝，减少	Segment	扫描范围，以优化部分查询性能。

配置

该功能默认为开启状态。正常情况下，用户无需过多关注此功能，极端情况下支持系统级或项目级关闭。

系统级关闭，在	 	$KYLIN_HOME/conf/kylin.properties		中配置参数。项目级关闭，在设置-高级设置-自定义项目配置中添
加配置。

	kylin.storage.columnar.dimension-range-filter-enabled=false

支持衍生维度查询	Segment	剪枝

为了提升剪枝的效果，从	Kyligence	Enterprise	4.6.0	版本开始，当存在匹配到的索引与衍生维度进行join的查询时，我们
支持使用衍生维度的查询过滤条件，结合构建时得到的维度值范围，进一步减少	Segment	扫描范围，并在查询的文件扫
描阶段过滤掉更多的数据。

该功能默认为关闭状态，需要通过添加参数启用该功能，支持系统级配置。

	kylin.storage.columnar.spark-conf.spark.sql.optimizer.runtime.bloomFilter.enabled=true

同时该功能生效有2个额外的条件，衍生维表的大小需要小于阈值，这个阈值默认为 	10M	，这个参数可以配置：

	kylin.storage.columnar.spark-conf.spark.sql.optimizer.runtime.bloomFilter.creationSideThreshold

查询时匹配到索引表的大小需要大于阈值，这个阈值的默认值为 	10G	，这个参数可以配置：

	kylin.storage.columnar.spark-conf.spark.sql.optimizer.runtime.bloomFilter.applicationSideScanSizeThreshold

默认	broadcast	join	时不适用，将这个参数设为 	true	，则	broadcast	join	也可以应用	runtime	filter:

	kylin.storage.columnar.spark-conf.spark.sql.optimizer.runtime.bloomFilter.broadcastJoinCondition.ignored

已知限制

1.	 查询过滤条件中目前只支持	 	=、in、>、>=、<、<=、and、or		的	Segment	剪枝，暂不支持	 	not、is	null	。

2.	 此功能会略微加长构建时间，但相比总构建时长，基本可忽略不计。

3.	 已完成构建的历史数据不会使用到此优化，如果希望历史数据也可以应用此优化，需要刷新	Segment。

4.	 暂不支持多级分区模型。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

626

查询下压

查询下压

本产品内嵌了一个智能查询下压引擎（Smart	Pushdown	Engine），支持	SQL	on	Hadoop	技术--	Spark	SQL。

Kyligence	Enterprise	在必要时可以将模型无法回答的查询语句，路由到查询下压引擎中，由	Spark	SQL	执行。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

627

查询下压

下压至原生	SparkSQL

Kyligence	Enterprise	使用预计算的数据来代替在线计算以实现大数据场景下的亚秒级查询响应。一般来说，	加载过数据
的模型已经可以服务大多数常用查询，但是当您需要执行一些模型无法满足的查询时，Kyligence	Enterprise	会将其路由
到智能查询下压引擎执行，默认的查询下压引擎为	Spark	SQL。

注意：为了保障数据一致性，查询下压不会击中缓存。

查询下压开关

Kyligence	Enterprise	4.x	起默认启用了	Spark	SQL，您在添加过数据源后，即可使用查询下压功能。	Kyligence	Enterprise
5.x	起，如果项目级开启了内表功能，则不再下压至数据源，而由内表回答。

查询下压功能默认为开启状态，如果您需要关闭查询下压，有如下两种方法：

项目级别关闭：如下图所示，点击左侧导航栏设置标签，在基础设置标签下的查询下压设置中可以关闭查询下压引擎。

如果这项配置从未在项目级别做过更改，将会与全局配置保持一致。

实例级别关闭：在配置文件	 	kylin.properties		中修改查询下压的对应配置项	 	kylin.query.pushdown-enabled=true	，将
其修改为	 	kylin.query.pushdown-enabled=false	，并删除这一配置项前的注释符号使其生效。

注意：修改配置文件后需要重启产品使配置生效。

验证查询下压

如果开启了查询下压，则在添加完数据源后，无需构建相应的模型即可使用查询功能。此时您在提交查询时，查询下压

将发挥作用。如果数据源类型为	HIVE，则查询结果会显示为： 	查询对象：HIVE	。

提示：如果查询击中模型，查询执行历史会显示为： 	查询对象：{对应的模型名称}	。

浮点数注意事项

下压查询中，如果有涉及数据源表中	 	float		类型列的过滤条件时，需注意过滤条件中字面量的类型和精度问题:

类型问题：手工指定字面量的数据类型，达成和列类型一致，写成类似	 	'123.4f'		的格式，如

SELECT	*	FROM	table1	WHERE	col1	>	'123.4f'

精度问题：字面量数据勿超过	 	float	/	double		的精度范围

举例来说，数据源表	 	table1		中有列	 	col1		为	 	float		类型，表中数据为：

|-------|

|	col1		|

|-------|

|	1.2			|

|	5.67		|

|	123.4	|

|	130.1	|

|-------|

与此同时下压查询的	SQL	语句为：

628

查询下压

SELECT	*	FROM	table1	WHERE	col1	>	123.4

则对应查询结果会是：

|-------|

|	col1		|

|-------|

|	123.4	|

|	130.1	|

|-------|

可以看到虽然在	 	WHERE		过滤条件中使用了大于号（ 	>	），但	 	123.4		这行也被查询出来了。

造成该结果的原因是由于该过滤条件两侧数据类型不同，命中了	Spark	优化器规则导致：

其中	 	col1		为	 	float		类型，字面量	 	123.4		默认为	 	double		类型；

而	Spark	优化器规则会将该过滤条件进行如下转换（注意转换后的	 	>=		号）：

cast(col1	to	double)	>	123.4		===>		col1	>=	cast(123.4	to	float)

从而导致	 	123.4		被查询出来。

因此，需要手工指定字面量的数据类型，正确的下压查询语句应为：

SELECT	*	FROM	table1	WHERE	col1	>	'123.4f'

查询出的结果也就正常了：

|-------|

|	col1		|

|-------|

|	130.1	|

|-------|

此外，关于字面量的精度问题，同样以上述情况为例，下压查询语句：

SELECT	*	FROM	table1	WHERE	col1	>	'123.3999f'

可以获得正确的查询结果：

|-------|

|	col1		|

|-------|

|	123.4	|

|	130.1	|

|-------|

而当精度超过相应数据类型范围时，结果是不可预料的：

SELECT	*	FROM	table1	WHERE	col1	>	'123.39999999999f'

结果如下：

|-------|

629

查询下压

|	col1		|

|-------|

|	130.1	|

|-------|

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

630

与	BI	工具集成

与	BI	工具集成

本章将介绍如何使用第三方	BI	工具连接	Kyligence	Enterprise。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:01

631

驱动程序

驱动程序

本章介绍了几种本产品目前支持的数据驱动。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:01

632

驱动程序

Kyligence	JDBC	驱动

本产品支持	JDBC	接口，并提供了	JDBC	驱动程序。该驱动允许如第三方BI应用，SQL	查询工具或其他支持	JDBC	接口
的应用访问本产品实例。

如何获取	JDBC	驱动程序

在	Kyligence	下载页面	下载	Kyligence	JDBC	驱动程序，并放置在	BI	或其它第三方应用指定路径。

注意：

1.	 支持连接到	Kyligence	Enterprise	3.2.x，3.3.x，3.4.x，4.0.x，4.1.x	及之后的高版本
2.	 较早期的	Kyligence	Enterprise版本，可以在产品安装目录的	 	./lib	子目录下，获取	JDBC	JAR	包文件进行连

接,	文件名为：kylin-jdbc-kap-\.jar

3.	 不支持连接到	Apache	Kylin

如何配置	JDBC	连接

本产品的	JDBC	驱动程序遵循了	JDBC	标准接口，用户可通过	URL	指定	JDBC	方式连接到	Kyligence	服务。

URL	格式为：

jdbc:kylin://<hostname>:<port>/<project_name>

URL	参数说明如下：

<hostname>:	主机名

<port>：端口号，如果本产品部署启用了SSL安全认证服务，则应该使用相关HTTPS端口号

<project_name>:	必须指定具体项目名称，并且确认该项目在服务中存在

其他配置参数如下：

<user>:	登陆服务实例的用户名

<password>:	登陆服务实例的密码

<ssl>:	是否开启SSL，值为String类型的"true"或"false"，	默认为"false"。如果是"true"，所有Kyligence的访问都将基
于HTTPS

<timeout>:	向	Kyligence	Enterprise	发请求的过期时间，单位为毫秒，默认为0，代表没有过期时间

JAVA	配置连接样例：

Driver	driver	=	(Driver)	Class.forName("org.apache.kylin.jdbc.Driver").newInstance();

Properties	info	=	new	Properties();

info.put("user",	"ADMIN");

info.put("password",	"KYLIN");

//info.put("ssl","true");

Connection	conn	=	driver.connect("jdbc:kylin://localhost:7070/kylin_project_name",	info);

下面章节介绍两种	JAVA	程序调用	JDBC	的连接方式

方法一：基于	Statement	的查询

具体直接基于	Statement	进行查询的代码样例如下：

633

驱动程序

Driver	driver	=	(Driver)	Class.forName("org.apache.kylin.jdbc.Driver").newInstance();

Properties	info	=	new	Properties();

info.put("user",	"ADMIN");

info.put("password",	"KYLIN");

//info.put("ssl","true");

Connection	conn	=	driver.connect("jdbc:kylin://localhost:7070/kylin_project_name",	info);

Statement	state	=	conn.createStatement();

ResultSet	resultSet	=	state.executeQuery("select	*	from	test_table");

while	(resultSet.next())	{

				System.out.println(resultSet.getString(1));

				System.out.println(resultSet.getString(2));

				System.out.println(resultSet.getString(3));

}

方法二：基于	PreparedStatement	的查询

该方法支持在	SQL	语句中传入参数，	目前支持如下方法进行参数设置：

setString

setInt

setShort

setLong

setDouble

setBoolean

setByte

setDate

setTimestamp

具体基于	Prepared	Statement	进行查询的代码样例如下：

Driver	driver	=	(Driver)	Class.forName("org.apache.kylin.jdbc.Driver").newInstance();

Properties	info	=	new	Properties();

info.put("user",	"ADMIN");

info.put("password",	"KYLIN");

//info.put("ssl","true");

Connection	conn	=	driver.connect("jdbc:kylin://localhost:7070/kylin_project_name",	info);

PreparedStatement	state	=	conn.prepareStatement("select	*	from	test_table	where	id=?");

state.setInt(1,	10);

ResultSet	resultSet	=	state.executeQuery();

while	(resultSet.next())	{

				System.out.println(resultSet.getString(1));

				System.out.println(resultSet.getString(2));

				System.out.println(resultSet.getString(3));

}

Prepared	Statement	已知限制

不支持查询下压

动态参数不支持与"-"放在一起，如 	SUM(price	-	?)
动态参数不支持出现在	case	when	中，如 	case	when	xxx	then	?	else	?	end

我们推荐您仅让动态参数出现在查询的过滤条件中，如	 	where	id	=	?

此外，我们也提供了动态参数绑定功能，需要配置相应的参数开启该功能，配置方法为： 	kylin.query.replace-dynamic-
params-enabled=true

上述配置开启之后，动态参数的限制收敛为：

动态参数的类型仅支持手册中提及到的类型，所以不支持列名和时间单位。

类型转换函数包括有	 	data	,	 	timestamp		和	 	cast	,	其中	 	date		和	 	timestamp		不支持动态参数。

634

驱动程序

部分函数如	 	subtract_count		支持传	 	array['FP-GTC,FP-non	GTC',	'Others']		类型的参数，array中的参数也支持使
用动态参数，如	 	array['FP-GTC|FP-non	GTC',	?]	，但单引号内不支持动态参数，即不能使用	`array['?|?',	?]

JDBC	用户委任

从	Kyligence	Enterprise	4.1.6	开始，通过在	JDBC	配置	Execute	as	user	为当前登陆用户账号，您可以使用一个认证的用户
委任查询请求给另一个用户。JDBC	发送给	Kyligence	Enterprise	的查询会以委任的	Execute	as	user	来执行。

下面章节介绍两种	JDBC	的配置	Execute	as	user	的方法

方法一：通过	JAVA	代码配置

Driver	driver	=	(Driver)	Class.forName("org.apache.kylin.jdbc.Driver").newInstance();

Properties	info	=	new	Properties();

info.put("user",	"ADMIN");

info.put("password",	"KYLIN");

info.put("EXECUTE_AS_USER_ID","EXECUTE_AS_NON_ADMIN");

Connection	conn	=	driver.connect("jdbc:kylin://localhost:7070/kylin_project_name",	info);

方法二：通过	connect	string	传参

在	connect	string	中增加配置	 	jdbc:kylin:EXECUTE_AS_USER_ID=EXECUTE_AS_NON_ADMIN;//localhost:7070/kylin_project_name

用以上任意一种方式设置成功以后，可以在	JDBC	日志里观察到	INFO	级别的日志："Found	the	parameter
EXECUTE_AS_USER_ID	in	the	connection	string.	The	query	will	be	executed	as	the	user	defined	in	this	connection	string."	查
询的用户将变更为	EXECUTE_AS_NON_ADMIN	。

JDBC	驱动日志

您可以启用驱动程序中的日志记录来跟踪活动和故障排除问题。

重要:	启动详细的的日志记录用来捕获问题，但日志记录会降低性能并消耗大量磁盘空间。

1.	 在文本编辑器中打开	JDBC	驱动程序日志配置文件。

例如，您可打开	{JDBC安装路径}/kyligence-jdbc.properties	文件

注意：kyligence-jdbc.properties	默认配置文件，需要与	JDBC	jar	包放在同一路径。

2.	 设置日志级别。下面列出了所有日志级别的信息，TRACE	在大多数情况下是最佳的。

OFF	禁用所有日志记录。
FATAL	记录非常严重的错误事件，可能导致驱动程序中止。
ERROR	记录错误事件，可能仍然允许驱动程序继续运行。
WARN	记录潜在的有害情况。
INFO	记录描述驱动程序进程的一般信息。
DEBUG	记录对调试驱动程序有用的详细信息。
TRACE	记录比日志DEBUG更详细的信息。

例如:	LogLevel=TRACE

3.	 设置日志文件路径和名称。将	LogPath	属性设置为要保存日志文件的文件夹完整路径。这个路径确保存在，并且是

可写的，包括如果使用驱动程序的应用程序作为特定用户运行，其他用户也可以写。

例如:	LogPath=/usr/local/KyligenceJDBC.log

4.	 配置	MaxBackupIndex	属性以保留最大数量的日志文件。

635

驱动程序

例如:	MaxBackupIndex=10

注意:	在达到日志文件的最大数量之后，每次创建一个额外的文件，驱动程序都会删除最旧的文件。

5.	 配置	MaxFileSize	属性设置为每个日志文件的最大大小	(以字节为单位)。

例如:	MaxFileSize=268435456

注意:	在达到最大文件大小之后，驱动程序创建一个新文件并继续日志记录。

6.	 保存驱动程序配置文件。

示例如下：

#	设置日志级别

LogLevel=TRACE

#	设置日志路径

LogPath=/usr/local/KyligenceJDBC.log

#	设置保留最大数量的日志文件

MaxBackupIndex=10

#	设置每个日志文件的最大大小

MaxFileSize=268435456

7.	 重新启动使用驱动程序的应用程序。在重新加载驱动程序之前，应用程序不会应用配置更改。

FAQ

Q:	如何升级	JDBC	驱动?

将	BI	或其它第三方应用的	Kyligence	JDBC	驱动包移除，替换至新的	JDBC	驱动包即可。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:01

636

驱动程序

Kyligence	ODBC	驱动

本产品支持ODBC接口，并提供了Kyligence	ODBC驱动程序。

它不仅支持与	Kyligence	Enterprise连接，并支持	Apache	Kylin	ODBC	驱动程序的全部功能。

支持	ODBC	接口的应用可以通过该驱动程序访问本产品进行数据查询。

Kyligence	ODBC	驱动程序包含在Kyligence	Enterprise	发行版。驱动程序有效使用期限与发行版一致。

目前有如下版本：

Windows	64位/32位
Linux	64位/32位

Mac	OS

在接下来的章节中，我们将介绍如何安装、配置和使用Kyligence	ODBC驱动。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:01

637

驱动程序

Kyligence	ODBC	驱动（Windows	版本）

在本文中，我们以	Windows	7	为例，介绍	Kyligence	ODBC	驱动程序（Windows版本）的安装和使用步骤。

前提条件

1.	 Microsoft	Visual	C++	2015	Redistributable

在安装	Kyligence	ODBC	驱动程序的过程中，系统会首先自行安装	Microsoft	Visual	C++	2015	Redistributable。如果
操作系统中已经安装了	Microsoft	Visual	C++	2015	Redistributable，安装步骤会跳过此步。

2.	 一个运行的Kyligence	Enterprise服务器（仅在配置DSN时）

Kyligence	ODBC	驱动程序安装成功后，在配置DSN时会连接	Kyligence	Enterprise	服务器，请务必先确保	Kyligence
Enterprise	服务已正常运行。

安装

1.	 如果机器上已经安装过	Kyligence	ODBC	驱动程序，首先卸载已有	Kyligence	ODBC	驱动程序。
2.	 在	Kyligence	下载页面	申请下载	Kyligence	ODBC	驱动程序，并运行安装。

32	位应用程序：请安装使用	Kyligence.ODBC.{version}.x86.exe

64	位应用程序：请安装使用	Kyligence.ODBC.{version}.x64.exe

配置	DSN

1.	 打开	ODBC	数据源管理器：

32	位	ODBC	驱动：单击开始	->	运行，并打开	C:\Windows\SysWOW64\odbcad32.exe

64	位	ODBC	驱动：单击控制面板	->管理工具，找到并打开数据源(ODBC)

2.	 切换至系统	DSN	选项卡，单击添加，在弹出的驱动程序选择框中选择	KyligenceODBCDriver，然后单击完成按

钮。

注意：用户	DSN只有特定的用户可以调用，而系统	DSN	对该系统的所有登录用户可用。如果用户需要在
Web	BI	Server	通过	ODBC	访问	Kyligence	Enterprise，应使用系统	DSN。

638

驱动程序

ODBC	数据源管理器

3.	 在弹出的对话框中输入	Kyligence	Enterprise	服务器信息，如图所示：

639

驱动程序

DSN	设置

其中，各项参数介绍如下：

Data	Source	Name：数据源名称
Description：数据源描述
Host：本产品	服务器地址
Port：本产品	服务器端口号
Username：本产品	服务登录用户名，不区分大小写
Password：本产品	服务登录密码
Project：查询所使用的	本产品	项目名称，不区分大小写
Disable	catalog：是否关闭catalog层，默认为开启状态，如果勾选Disable	catalog则为关闭状态

4.	 单击	Test	按钮，连接成功后，将显示如下对话框。

640

驱动程序

连接成功

是否需要开启catalog层

需要关闭catalog层的BI工具有：Cognos

需要开启catalog层的BI工具有：OBIEE

连接字符串

有一些BI工具支持不使用DSN而直接配置ODBC连接字符串的形式访问数据源。在这种场景下，用户可以使用下面的字
符串格式进行配置：

DRIVER={KyligenceODBCDriver};SERVER=locahost;PORT=7070;PROJECT=learn_kylin

提示：请将SERVER，PORT及PROJECT中的信息替换成您所使用的本产品的信息。

Windows	ODBC	驱动日志	-	使用日志记录对话框

您可以启用驱动程序中的日志记录来跟踪活动和故障排除问题。

641

驱动程序

重要:	启动详细的的日志记录用来捕获问题，但日志记录会降低性能并消耗大量磁盘空间。

1.	 单击控制面板	->管理工具，找到并打开ODBC	数据源管理程序
2.	 选择要记录连接活动的DSN，然后单击配置

642

驱动程序

3.	 在DSN安装对话框中，单击Logging	Options

4.	 下面列出了所有日志级别的信息。在大多数情况下，LOG_TRACE是最佳的。

LOG_FATAL	记录可能导致驱动程序中止的非常严重的错误事件。
LOG_ERROR	记录可能仍然允许驱动程序继续运行的错误事件。
LOG_WARNING	记录潜在的预警情况。
LOG_INFO	记录描述驱动程序进程的一般信息。
LOG_DEBUG	记录对调试驱动程序有用的详细信息。
LOG_TRACE	记录比LOG_DEBUG级别更详细的信息。

643

驱动程序

5.	 在Log	Path字段中，键入要保存日志文件的文件夹完整路径。

6.	 在Max	Number	Files字段中，键入要保留的最大日志文件数。

注意:	到达日志文件的最大数量后，每次创建一个额外的文件，驱动程序都会删除最旧的文件。

7.	 在Max	File	Size字段中，键入每个日志文件的最大大小(以MB为单位)。

注意:	达到最大文件大小后，驱动程序创建一个新文件并继续日志记录。

8.	 单击OK关闭日志记录选项对话框。

9.	 单击OK保存设置并关闭DSN配置对话框。

注意:	在DSN配置对话框中单击OK后，驱动程序才会保存配置更改。单击Cancel按钮将放弃更改。

10.	 重新启动使用驱动程序的应用程序。在重新加载驱动程序之前，应用程序不会应用配置更改。

特别提醒

如果用户希望在其他应用程序中使用	Kyligence	ODBC	驱动程序连接本产品，可访问本手册	与BI	工具连接	章节，了解
相关信息。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:01

644

驱动程序

Kyligence	ODBC	驱动（Linux	版本）

在本文中，我们将向您介绍如何在	Linux	系统下安装和配置	Kyligence	ODBC	驱动（Linux	版本)

安装库的依赖

我们建议您使用	unixODBC(http://www.unixodbc.org/)	作为驱动管理器来管理	ODBC	连接信息。

注意：	由于64位	unixODBC	将会覆盖32位	unixODBC	的一些依赖库，这将会导致在使用32位	unixODBC	驱动时会
出现依赖库的冲突，可能无法正常使用32位	Kyligence	ODBC	驱动。因此，若您要使用	Linux	32	位版本的
Kyligence	ODBC	驱动，需要卸载环境中的64位	unixODBC。

对于不同的	Linux	系统：

1.	 Redhat	和	CentOS	环境,	请参考如下操作安装

若您需要使用64位	Kyligence	ODBC	驱动，您可以直接使用以下命令进行64位	unixODBC	的安装

	sudo	yum	install	unixODBC-devel	-y

若您需要使用32位	Kyligence	ODBC	驱动，建议您依次使用以下命令进行32位	unixODBC	的安装

	sudo	yum	install	unixODBC.i686	-y

	sudo	yum	install	unixODBC-devel.i686	-y

2.	 Ubuntu	环境，请参考如下操作安装

若您需要使用64位	Kyligence	ODBC	驱动，您可以直接使用以下命令进行64位unixODBC的安装

	sudo	apt-get	install	unixODBC-devel

若您需要使用32位	Kyligence	ODBC	驱动，建议您依次使用以下命令进行32位unixODBC的安装	 	sudo	apt-get
install	unixODBC.i686

	sudo	apt-get	install	unixODBC-devel.i686

下载	ODBC	驱动程序

您可以在	Kyligence	下载页面	申请下载	Kyligence	ODBC	Driver	(Linux版本）安装包。

安装	ODBC	驱动程序

1.	 解压下载的压缩包

	tar	-zxvf	Kyligence.ODBC.{version}.tar.gz

注意：	请不要将	ODBC	安装文件放在	root	目录下，否则会因为读写权限问题可能导致	BI	Server	访问失败。

2.	 检查库的依赖

	cd	ODBCDriver/

	ldd	libKyligenceODBC64.so

提示：	使用32位的	Kyligence	ODBC	驱动请使用 	ldd	libKyligenceODBC32.so	命令检查库的依赖。

如果检查成功，您将会看到如下输出：

linux-vdso.so.1	=>		(0x00007fffca9eb000)

librt.so.1	=>	/lib64/librt.so.1	(0x00007fe826b3f000)

libdl.so.2	=>	/lib64/libdl.so.2	(0x00007fe82693b000)

libm.so.6	=>	/lib64/libm.so.6	(0x00007fe8266b6000)

645

驱动程序

libpthread.so.0	=>	/lib64/libpthread.so.0	(0x00007fe826499000)

libc.so.6	=>	/lib64/libc.so.6	(0x00007fe826105000)

lib64/ld-linux-x86-64.so.2	(0x00007fe829aac000)

如果检查失败，依赖库不存在，您将看到如下输出：

linux-vdso.so.1	=>		not	found

librt.so.1	=>	/lib64/librt.so.1	(0x00007fe826b3f000)

libdl.so.2	=>	/lib64/libdl.so.2	(0x00007fe82693b000)

libm.so.6	=>	/lib64/libm.so.6	(0x00007fe8266b6000)

libpthread.so.0	=>	/lib64/libpthread.so.0	(0x00007fe826499000)

libc.so.6	=>	/lib64/libc.so.6	(0x00007fe826105000)

lib64/ld-linux-x86-64.so.2	(0x00007fe829aac000)

设置ODBC	DSN

1.	 将	Kyligence	ODBC	添加入配置文件

提示：	一些	BI	工具需要	ODBC	配置文件放置在自己的安装目录下，如样例说明中的	MicroStrategy。因此
请您根据所使用的	BI	工具进行配置。

ODBC驱动配置文件	–	/etc/odbcinst.ini

[{DriverName}]

APILevel=1

ConnectFunctions=YYY

Description={Description}

Driver={DriverPath}

Setup={DriverPath}

DriverODBCVer=03.80

SQLLevel=1

Locale=en-US

DSN配置文件	–	/etc/odbc.ini

[{DSName}]

Driver	=	{DriverName}

PORT	=	{KE_Port}

PROJECT	=	{KE_Project}

SERVER	=	{KE_Url}

样例配置：

/etc/odbcinst.ini

[KyligenceODBCDriver]

APILevel=1

ConnectFunctions=YYY

Description=Sample	64-bit	Kyligence	ODBC	Driver

Driver=/home/kylin/KyligenceODBC/ODBC_DRIVER/libKyligenceODBC64.so

Setup=/home/kylin/KyligenceODBC/ODBC_DRIVER/libKyligenceODBC64.so

DriverODBCVer=03.80

SQLLevel=1

Locale=en-US

/etc/odbc.ini

[KyligenceDataSource]

Driver	=	KyligenceODBCDriver

PORT	=	80

646

驱动程序

PROJECT	=	learn_kylin

SERVER	=	http://kapdemo.chinaeast.cloudapp.chinacloudapi.cn

注意：	请确认	 	odbc.ini		文件中的	DSN	名称和	BI	桌面环境下配置的	DSN	名称完全一致，保证	BI	应用由桌
面客户端发布至服务器端时连接正常

2.	 使用命令行工具 	isql	DSN	[UID	'[PWD]']	测试连接

	isql	KyligenceDataSource	ADMIN	'KYLIN'

3.	 发送查询测试

	SQL>	select	count(*)	from	kylin_sales;		如果连接成功，则会返回如下结果

+---------------------+

|	EXPR$0														|

+---------------------+

|	4957																|

+---------------------+

SQLRowCount	returns	1

1	rows	fetched

样例说明

这里我们以	MicroStrategy	Linux	Intelligence	Server	为例，介绍如何创建	DSN。

1.	 在	Linux	shell	下，浏览至	MicroStrategy	的安装目录。

2.	 打开文件 	ODBC.ini	，按如下格式添加	DSN	配置信息。

[DSN_Name]

ConnectionType=Direct

Driver=<ODBC_HOME>/libKyligenceODBC64.so

PORT=<PORT_NUMBER>

PROJECT=<PROJECT_NAME>

SERVER=<SERVER_NAME>

3.	 添加如下配置信息，映射	DSN	至	ODBC。

[ODBC	Data	Sources]

<DSN_Name>=KyligenceODBC

以下就是一个名为	EAT1_WH	的	DSN	配置样例：

[ODBC	Data	Sources]

KyligenceDataSource=KyligenceODBC

[EAT_WH1]

ConnectionType=Direct

Driver=/home/kylin/ODBCDriver/libKyligenceODBC64.so

PORT=57070

PROJECT=mstr

SERVER=http://106.75.137.52

4.	 完成	DSN	配置后，我们建议您重启	MicroStrategy	Intelligence	Server，确保刚创建的	DSN	已经生效。

5.	 现在您就可以在	MicroStrategy	Linux	I-Server	上使用该	DSN	创建新的数据库连接了。

Linux	ODBC	驱动日志

647

驱动程序

您可以启用驱动程序中的日志记录来跟踪活动和故障排除问题。

重要:	启动详细的的日志记录用来捕获问题，但日志记录会降低性能并消耗大量磁盘空间。

1.	 在文本编辑器中打开ODBC驱动程序配置文件。

例如，您可打开{[ODBC安装路径]}/kyligence.odbc.ini文件

2.	 下面列出了所有日志级别的信息。6	在大多数情况下是最佳的。

0	禁用所有日志记录。
1	记录非常严重的错误事件，可能导致驱动程序中止。
2	记录错误事件，可能仍然允许驱动程序继续运行。
3	记录潜在的有害情况。
4	记录描述驱动程序进程的一般信息。
5	记录对调试驱动程序有用的详细信息。
6	(TRACE)	记录比日志级别5更详细的信息。

例如:	LogLevel=6

3.	 将LogPath属性设置为要保存日志文件的文件夹完整路径。这个路径确保存在，并且是可写的，包括如果使用驱动

程序的应用程序作为特定用户运行，其他用户也可以写。

例如:	LogPath=/localhome/username/Documents

4.	 配置LogFileCount属性以保留最大数量的日志文件。

例如:	LogFileCount=5

注意:	在达到日志文件的最大数量之后，每次创建一个额外的文件，驱动程序都会删除最旧的文件。

5.	 配置LogFileSize属性设置为每个日志文件的最大大小(以Bytes为单位)。

例如:	LogFileSize=20971520

注意:	在达到最大文件大小之后，驱动程序创建一个新文件并继续日志记录。

6.	 保存驱动程序配置文件。

7.	 重新启动使用驱动程序的应用程序。在重新加载驱动程序之前，应用程序不会应用配置更改。

FAQ

Q:	isql	测试连接失败

请使用 	isql	-v	DSN	[UID	'[PWD]']	获取更多报错信息，然后根据报错检查	ODBC	配置文件和	DSN	配置文件是否正确。

以下为一个 	SERVER		配置项错误写为 	SEVER	后，系统无法正确识别 	SERVER	配置项的样例：

输入命令 	isql	-v	KyligenceDataSource	ADMIN	'KYLIN'

您可以看到报错：

[08001][unixODBC][Simba][ODBC](10380)	Unable	to	establish	connection	with	data	source.	Missing	settings:	{[SERV

ER]}

648

驱动程序

[ISQL]ERROR:	Could	not	SQLConnect

Q:isql测试连接报错	"Can't	open	lib	'/usr/local/ODBCDriver/libKyligenceODBC32.so'	:	file	not	found"，但是文件实际在
对应目录下存在

这通常是因为环境中有64位	unixODBC	导致依赖库冲突，需要彻底卸载64位	unixODBC。您可以通过运行 	odbcinst	-
j	命令查看	unixODBC	的相关安装信息。

若安装了32位	unixODBC，您可以看到如下结果：

unixODBC	2.2.14

DRIVERS............:	/etc/odbcinst.ini

SYSTEM	DATA	SOURCES:	/etc/odbc.ini

FILE	DATA	SOURCES..:	/etc/ODBCDataSources

USER	DATA	SOURCES..:	/root/.odbc.ini

SQLULEN	Size.......:	4

SQLLEN	Size........:	4

SQLSETPOSIROW	Size.:	2

若安装了64位	unixODBC，您可以看到如下结果：

unixODBC	2.2.14

DRIVERS............:	/etc/odbcinst.ini

SYSTEM	DATA	SOURCES:	/etc/odbc.ini

FILE	DATA	SOURCES..:	/etc/ODBCDataSources

USER	DATA	SOURCES..:	/root/.odbc.ini

SQLULEN	Size.......:	8

SQLLEN	Size........:	8

SQLSETPOSIROW	Size.:	8

Q:	如何卸载	unixODBC

首先您需要使用命令 	yum	list	installed	|	grep	unixODBC	查看您安装的	unixODBC	包名；其次，您需要使用 	sudo	yum
remove	{package	name}	命令进行卸载。

这里以卸载64位	unixODBC	为例：

输入命令 	yum	list	installed	|	grep	unixODBC	，您可以看到以下信息：

unixODBC.x86_64											2.2.14-14.el6											@base

unixODBC-devel.x86_64					2.2.14-14.el6											@base

接下来依次使用以下命令，完成64位	unixODBC	的卸载：

sudo	yum	remove	unixODBC-devel.x86_64

sudo	yum	remove	unixODBC.x86_64

Q:	报错提示：(11560)	Unable	to	locate	SQLGetPrivateProfileString	function.

请您运行以下命令：

	export	LD_PRELOAD=/usr/lib/libodbcinst.so

Q:	如何升级	ODBC	驱动?

将	BI	或其它第三方应用的	Kyligence	ODBC	驱动包移除，替换至新的	ODBC	驱动包即可。

Q:	如何修改	ODBC	默认数据库类型.

649

驱动程序

ODBC	默认数据库类型是	MYSQL。若您需要修改，则要在	/etc/odbc.ini	文件内，在	DSN	配置添加

SQLDBMSName=Oracle

[KyligenceDataSource]

Driver	=	<ODBC_HOME>/libKyligenceODBC64.so

PORT	=	80

PROJECT	=	learn_kylin

SERVER	=	http://kapdemo.chinaeast.cloudapp.chinacloudapi.cn

SQLDBMSName	=	Oracle

注意：仅在	Cognos	自助式分析场景下，建议将默认数据库类型修改为	Oracle，且必须配合	Kyligence	SQL
Adapter	一起使用，其它情况下不推荐修改。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:01

650

驱动程序

Kyligence	ODBC	驱动（Mac	版本）

在本文中，我们将向您介绍如何在Mac	系统下通过ODBC	Manager或unixODBC安装和配置	Kyligence	ODBC	驱动（Mac
版本)。

您可以使用	ODBC	Manager	通过界面创建DSN或者也可以直接编辑 	odbc.ini		文件

使用ODBC	Manger安装

安装	Kyligence	ODBC	Driver

您可以在	Kyligence	下载页面	申请下载	Kyligence	ODBC	Driver	安装包，并运行安装。

64	位应用程序：请安装使用	Kyligence.ODBC.{version}.x64.pkg

注意：	请不要将	ODBC	安装文件放在	root	目录下，否则会因为读写权限问题可能导致	BI	Server	访问失败。

安装ODBC	Manger

您可以在	ODBC	Manager	页面下载ODBC	Manager安装包，并运行安装。

注意：若安装后，/Library/下没有ODBC文件夹，请手动创建，并配置odbcinst.ini、odbc.ini

mkdir	ODBC

cd	ODBC

touch	odbcinst.ini

touch	odbc.ini

ODBC驱动配置文件	–	/Library/ODBC/odbcinst.ini

[ODBC	Drivers]

[{DriverName}]	=	Installed

[{DriverName}]

Driver={DriverPath}

DSN配置文件	–	/Library/ODBC/odbc.ini

[ODBC	Data	Sources]

{DSNName}	=	{DriverName}

[{DSNName}]

Driver	=	{DriverPath}

Host	=	{KE_Url}

Port	=	{KE_Port}

Project	=	{KE_Project}

样例配置：

/Library/ODBC/odbcinst.ini

[ODBC	Drivers]

KyligenceODBCDriver		=	Installed

[KyligenceODBCDriver]

Driver	=	/Library/KyligenceODBCLib/libKyligenceODBC64.dylib

651

驱动程序

/Library/ODBC/odbc.ini

[ODBC	Data	Sources]

KyligenceDataSource	=	KyligenceODBCDriver

[KyligenceDataSource]

Driver	=	/Library/KyligenceODBCLib/libKyligenceODBC64.dylib

Host	=	http://kapdemo.chinaeast.cloudapp.chinacloudapi.cn

Port	=	7070

Project	=	learn_kylin

配置好后，您就可以直接在BI工具中使用了，可跳过下面的界面配置Driver、DSN操作。

配置KyligenceODBCDriver

打开ODBC	Manger，进入“Drivers”	页面​	，确认已成功添加	KyligenceODBCDriver

注意：请务必保证	Driver	Name	为	“KyligenceODBCDriver”

Drivers

652

驱动程序

配置DSN

进入“System	DSN”或“User	DSN”页面，点击“Add”新建

注意：用户	DSN	只有特定的用户可以调用，系统	DSN	对该系统的所有登录用户可用。如果用户需要在Web
BI	Server	通过	ODBC	访问	Kyligence	Enterprise，应使用系统	DSN。

System	DSN

653

驱动程序

选择“KyligenceODBCDriver”

Select	Driver

确认后，输入Host、Port、Project等信息，点击“OK”即可

Host：本产品服务器地址
Port：本产品服务器端口号
Username：本产品服务登录用户名，不区分大小写
Password：本产品服务登录密码
Project：查询所使用的本产品项目名称，不区分大小写

654

驱动程序

DSN	Setting

DSN配置好后您就可以直接在BI工具中使用了。

使用UnixODBC	安装

如您已经通过ODBC	Manager	完成了ODBC的安装及	DSN的配置，可跳过本章节。

安装	unixODBC

我们建议您使用	unixODBC(http://www.unixodbc.org/)	作为驱动管理器来管理	ODBC	连接信息​

brew	install	unixODBC

安装完成后，执行下述命令，确认结果是否为	/usr/local/bin/isql

which	isql

执行下述命令，确认DRIVERS路径是否是	/usr/local/etc/odbcinst.ini，	确认SYSTEM	DATA	SOURCES路径是否是

/usr/local/etc/odbc.ini

odbcinst	-j

配置KyligenceODBCDriver

将	Kyligence	ODBC	添加入配置文件

ODBC驱动配置文件	–	/usr/local/etc/odbcinst.ini

655

驱动程序

[{DriverName}]

APILevel=1

ConnectFunctions=YYY

Description={Description}

Driver={DriverPath}

Setup={DriverPath}

DriverODBCVer=03.80

SQLLevel=1

Locale=en-US

配置DSN

DSN配置文件	–	/usr/local/etc/odbc.ini

[{DSName}]

Driver	=	{DriverName}

SERVER	=	{KE_Url}

PORT	=	{KE_Port}

PROJECT	=	{KE_Project}

样例配置：

/etc/odbcinst.ini

[KyligenceODBCDriver]

APILevel=1

ConnectFunctions=YYY

Description=Sample	64-bit	Kyligence	ODBC	Driver

Driver=/Library/KyligenceODBCLib/libKyligenceODBC64.dylib

Setup=/Library/KyligenceODBCLib/libKyligenceODBC64.dylib

DriverODBCVer=03.80

SQLLevel=1

Locale=en-US

/etc/odbc.ini

[KyligenceDataSource]

Driver	=	KyligenceODBCDriver

SERVER	=	http://kapdemo.chinaeast.cloudapp.chinacloudapi.cn

PORT	=	7070

PROJECT	=	learn_kylin

查询验证

使用命令行工具 	isql	DSN	[UID	'[PWD]']	测试连接

isql	KyligenceDataSource	ADMIN	'KYLIN'

发送查询测试

SQL>	select	count(*)	from	kylin_sales;

如果连接成功，则会返回如下结果

+---------------------+

|	EXPR$0														|

+---------------------+

656

驱动程序

|	10000															|

+---------------------+

SQLRowCount	returns	1

1	rows	fetched

拷贝ini文件至/Library/ODBC下

sudo	cp	/usr/local/etc/odbcinst.ini	/Library/ODBC/

sudo	cp	/usr/local/etc/odbcinst.ini	/Library/ODBC/

sudo	chown	-R	{UserName}	odbc.ini

sudo	chown	-R	{UserName}	odbcinst.ini

注意：若您本机环境没有/Library/ODBC文件夹，需要手动创建

cd	/Library

sudo	mkdir	/ODBC

Mac	ODBC	驱动日志

您可以启用驱动程序中的日志记录来跟踪活动和故障排除问题。

重要:	启动详细的的日志记录用来捕获问题，但日志记录会降低性能并消耗大量磁盘空间。

1.	 在文本编辑器中打开ODBC驱动程序配置文件。

例如，您可打开{[ODBC安装路径]}/kyligence.odbc.ini文件

2.	 下面列出了所有日志级别的信息。6	在大多数情况下是最佳的。

0	禁用所有日志记录。
1	记录非常严重的错误事件，可能导致驱动程序中止。
2	记录错误事件，可能仍然允许驱动程序继续运行。
3	记录潜在的有害情况。
4	记录描述驱动程序进程的一般信息。
5	记录对调试驱动程序有用的详细信息。
6	(TRACE)	记录比日志级别5更详细的信息。

例如:	LogLevel=6

3.	 将LogPath属性设置为要保存日志文件的文件夹完整路径。这个路径确保存在，并且是可写的，包括如果使用驱动

程序的应用程序作为特定用户运行，其他用户也可以写。

例如:	LogPath=/localhome/username/Documents

4.	 配置LogFileCount属性以保留最大数量的日志文件。	例如:	LogFileCount=5

注意:	在达到日志文件的最大数量之后，每次创建一个额外的文件，驱动程序都会删除最旧的文件。

5.	 配置LogFileSize属性设置为每个日志文件的最大大小(以Bytes为单位)。	例如:	LogFileSize=20971520

注意:	在达到最大文件大小之后，驱动程序创建一个新文件并继续日志记录。

657

驱动程序

6.	 保存驱动程序配置文件。

7.	 重新启动使用驱动程序的应用程序。在重新加载驱动程序之前，应用程序不会应用配置更改。

FAQ

Q:	如何卸载	unixODBC

输入命令 	brew	uninstall	unixodbc	，您可以看到以下信息：

Uninstalling	/usr/local/Cellar/unixodbc/2.3.7...	(46	files,	1.8MB)

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:01

658

与	BI	工具连接

与	BI	工具连接

本章节主要介绍如何使用第三方	BI	工具与	Kyligence	Enterprise	连接。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:01

659

与	BI	工具连接

与	Tableau	集成

本章节介绍	Kyligence	Enterprise	如何与	Tableau	集成。

包含如下内容：

与	Tableau	Desktop	集成
与	Tableau	Server	集成
启用	Tableau	Server	用户委任

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:01

660

与	BI	工具连接

与	Tableau	Desktop	集成

Tableau	是	Windows	平台上最流行的商业智能工具之一，它操作简洁，功能强大，通过简单地拖拽就可以将大量数据体
现在可视化图表中。Kyligence	Enterprise	提供与	Tableau	Desktop	不同的集成方式。

Kyligence	Enterprise	支持与	2020.4	及以上版本集成，本小节以	Tableau	2020.4	为例，将分步介绍	Kyligence	Enterprise	与
Tableau	Desktop	集成操作。

前置条件

安装	Kyligence	ODBC	驱动程序。有关安装信息，请参考页面	Kyligence	ODBC	驱动程序介绍。
安装	Tableau	Desktop。有关	Tableau	的安装说明，请访问	Tableau	Desktop	下载页面。

配置与	Kyligence	数据源连接

1.	 在	Kyligence下载中心	下载	Kyligence	Connector	文件	(.taco)	文件

2.	 将	.taco	文件拷贝至	Tableau	Desktop	安装目录，Tableau	安装目录为

Windows:	My	Documents/My	Tableau	Repository/Connectors

macOS:	~/Documents/My	Tableau	Repository/Connectors

注意：中文路径名可能会导致	Kyligence	连接器不生效，可通过自定义英文路径，并通过	TSM	配置
native_api.connect_plugins_path	解决。

3.	 (可选)	Desktop	启动新增	-DConnectPluginsPath	参数

右键	Tableau	Desktop	快捷方式，选择	属性	->	快捷方式	->目标，添加	-DConnectPluginsPath	参数

"C:\Program	Files\Tableau\Tableau	2020.2\bin\tableau.exe"	-DConnectPluginsPath="自定义路径"
示例："C:\Program	Files\Tableau\Tableau	2020.2\bin\tableau.exe"	-DConnectPluginsPath="C:\tableau-connector-p

lugin"

注意：快捷方式添加参数后，需要先通过快捷方式打开	Tableau，然后在	Tableau	内通过	文件->打开	打开
TDS	文件。双击打开	TDS	文件将无法应用自定义路径参数。

4.	 配置	Tableau	Datasource	Customization	(TDC)	文件。

注意:	Tableau	支持配置	TDC	文件，以达到自定义和调整	ODBC	连接。针对该特性，Kyligence	提供满足
Kyligence	Enterprise	特殊的查询规范的	TDC	文件，以帮助	Tableau	更好的连接	Kyligence	数据。

配置步骤如下：

i.	 在	Kyligence下载中心	下载	Tableau	Datasource	Customization	(TDC)	文件
ii.	 将	TDC	文件拷贝至	Tableau	Desktop	相关安装目录下即可，默认目录为	Documents\My	Tableau

Repository\Datasources

5.	 重启	Tableau	Desktop

连接	Kyligence

Kyligence	Enterprise	与	Tableau	Desktop	支持2种集成方式，下文将分别介绍具体集成步骤。

Kyligence	Enterprise	快捷导入导出同步模型方式
Kyligence	Enterprise	手动映射模型方式

661

与	BI	工具连接

方式一：Kyligence	Enterprise	快捷导入导出同步模型方式

您在Kyligence	Enterprise	完成建模后，可以直接导出	Tableau	对应的数据源文件(.TDS)，

并在	Tableau	中一键导入该文件，快速完成模型同步。

注意：	仅	Kyligence	Enterprise	4.2.1	以上版本支持该方式

Kyligence	Enterprise	导出	Tableau	Data	Source	(.TDS)	文件

该方式主要步骤如下：

进入模型页面

在需要导出的模型更多操作中选择导出TDS

在导出选项中可以选择

1.	 导出范围：

只包含聚合索引中的维度列和度量列（默认）

包含聚合索引和明细索引中的维度列和度量列

包含模型中所有的维度列和度量列，即使这些列没有加入任何聚合索引或明细索引

2.	 数据源连接方式：

其他	ODBC	数据源（默认）
Tableau	Kyligence	Connector，如您在前一步配置了	Tableau	Connector，则该步骤可以选择此选项。

662

与	BI	工具连接

将导出的.TDS文件导入至	Tableau

在已部署的	Tableau	环境中，双击导出的TDS文件
在弹出的认证窗口中，输入连接认证信息

点击OK

663

与	BI	工具连接

在	Tableau	中，检查导入的模型内容,	如维度，度量

创建可视化图表

现在您可以进一步使用Tableau进行可视化分析，拖拽维度、度量字段，就可以生成自己的图表了。

664

与	BI	工具连接

方式二：Kyligence	Enterprise	手动映射模型方式

使用数据源连接器连接	Kyligence	Enterprise

如配置了	Kyligence	数据源连接器，请单击左侧面板中的	Kyligence	Connector	by	Kyligence，在弹出窗口中输入连接认证
信息，包括服务器地址、端口、项目、模型名（可选）、用户名、密码。点击登陆，认证通过后，即可获取该账户下所

有有权限访问的表和数据。

注意：

如果您在	Tableau	Desktop	使用了	Kyligence	数据源连接器，将工作薄发布至	Tableau	Server	时，	Tableau
Server	也需要同样配置	Kyligence	数据源连接器以保证连接正常。
使用	Tableau	Connector	方式连接时，请注意模型名称为大小写敏感，即输入模型名称时，需保证与
Kyligence	Enterprise	中的模型名称大小写一致。

665

与	BI	工具连接

连接	Kyligence	Enterprise

使用其他数据源方式连接	Kyligence	Enterprise

打开	Tableau	Desktop，单击左侧面板中的其它数据源	(ODBC)，可选择驱动程序或者	DSN	方式连接。选择驱动程序方
式，需要在弹出窗口中输入连接认证信息（服务器地址、端口、项目、用户名、密码）,	选择	DSN	方式，直接下拉选择
本地已创建好的	DSN	。点击连接，认证通过后，即可获取该账户下所有有权限访问的表和数据。

注意：当您在	Tableau	Desktop	使用	DSN	方式连接到	Kyligence	Enterprise，并需要将工作薄发布至	Tableau	Server
时，应在	Tableau	Server	创建与本地同名的	DSN，DSN	类型必须是系统	DSN。若您使用驱动程序方式连接时，不
需要在	Tableau	Server	创建	DSN。

666

与	BI	工具连接

创建数据模型

连接	Kyligence	Enterprise

在	Tableau	Desktop	左边面板中，选择	default	作为数据库，在搜索框中点击	Search	图标，将会列出所有的表，可通过拖
拽的方式把表拖到右边面板中，创建表与表的连接关系	。

创建数据模型

设置实时连接

Tableau	中提供两种数据源连接类型，大数据场景下，建议您选择实时（Live）连接。

667

与	BI	工具连接

自定义	SQL

设置实时连接

如果用户想通过自定义SQL进行交互，可以点击模型界面左下角的新建自定义	SQL（New	Custom	SQL），在弹出的框
中输入	SQL	即可实现。

自定义	SQL	交互

可视化

现在您可以进一步使用	Tableau	进行可视化分析，拖拽维度、度量字段，就可以生成自己的图表了。

668

与	BI	工具连接

已知限制

可视化分析

暂不支持度量	TopN、PERCENTILE_APRROX、COLLECT_SET	在	Tableau	中显示。
Kyligence	Enterprise	4.5.19.0	及以上版本导出的	TDS，需要使用新版本	Tableau	Connector	1.0.2	及以上
（tableau_connector_for_kyligence_1.0.2.taco	及以上）打开，老版本	Tableau	Connector	1.0.0	无法打开。建议	Tableau
Connector	1.0.2	及以上	和	Kyligence	Enterprise	4.5.19.0	及以上版本共同升级。
Kyligence	Enterprise	4.2.1.3041	及以上版本导出的	TDS，均可以使用新版本	Tableau	Connector	1.0.2	及以上
（tableau_connector_for_kyligence_1.0.2.taco	及以上）打开。
由于	Tableau	2020.3	及之前版本在官网已无法下载（存在	Log4j	漏洞），Tableau	connector	1.0.2	及以上对	Tableau
2020.3	及之前版本不再兼容。
实时模型和融合模型导出	TDS	后，导入	Tableau	不可用。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:01

669

与	BI	工具连接

与	Tableau	Server	集成

前置条件

安装	Kyligence	ODBC	驱动程序。有关安装信息，参考页面	Kyligence	ODBC驱动程序介绍
安装	Tableau	Server。有关	Tableau	Server	的安装说明，请访问	Tableau	Server下载页面

配置与	Kyligence	数据源连接

如	Tableau	版本为	2020.4	及以上，请按照下述步骤配置	Kyligence	数据源连接器。

1.	 登录	Kyligence下载中心，下载	Tableau	Connector	for	Kyligence	文件（格式为	.taco）。

2.	 将	.taco	文件复制到	Tableau	Server	的安装目录，通常为：

Windows：My	Documents/My	Tableau	Repository/Connectors
Linux：{自定义路径}/tableau_connectors

[!NOTE]

当出现下述情况时，您需要执行步骤	3：

未找到	Tableau	Server	安装目录。

3.	 （可选）为	Kyligence	数据源连接器设置新的路径，路径不可包含中文和空格。

tsm	configuration	set	-k	native_api.connect_plugins_path	-v	{自定义路径}

[!NOTE]

如果提示配置错误，请尝试在命令末尾添加	 	--force-keys	。

4.	 应用未完成的配置更改，此操作将会重启服务器。

tsm	pending-changes	apply

登录	Tableau	Server

670

与	BI	工具连接

在	Tableau	Desktop	界面上方，点击	服务器->登录，在弹出的窗口输入	Tableau	Server	地址，以及账号密码进行登陆。

发布工作簿至	Tableau	Server

登录成功后，点击发布工作簿

发布时，Tableau	支持两种数据源身份认证类型：嵌入式密码、提示用户、通过嵌入密码进行模拟。选择嵌入式密码
时，Tableau	会有效地嵌入其发布者的连接权限，并允许可以查看工作簿的任何人查看工作簿连接到的数据。当选择提
示用户时，将提示经允许可以对数据源使用连接能力的	Viewer（查看者）输入其凭据，详细介绍可参考Tableau	权限参
考。

如实现	Tableau	Server	与	Kyligence	Enterprise	的用户委任，可选择通过嵌入密码进行模拟，请参考启用	Tableau	Server	用
户委任章节。

671

与	BI	工具连接

身份认证类型

在	Tableau	Server	中查看工作簿

发布成功后，浏览器进入	Tableau	Server，登录	Tableau	账号密码，进入发布工作簿所在路径，查看视图。首次查看时，
需要输入	Kyligence	Enterprise	的账号密码，认证后即可查看有权访问的数据。

1.	 进入发布路径

2.	 输入	Kyligence	Enterprise	账号密码

672

与	BI	工具连接

3.	 查看报告

有编辑权限的	Tableau	用户可在	Server	端编辑报告。

注意事项

如当前版本的	Tableau	Server	不支持用户委任，可在	Desktop	以提示用户模式发布工作簿，并在	Tableau	Server	输入
Kyligence	Enterprise	账号密码，实现权限集成。Tableau	Server	支持保存	Kyligence	Enterprise	账号密码，通过	设置->
常规->保存的凭据	勾选对应设置。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:01

673

与	BI	工具连接

启用	Tableau	Server	用户委任

本文将引导您配置	Tableau	Server	和	Kyligence	Enterprise	的用户委任。

从	Kyligence	Enterprise	4.1.6	开始，通过在	Tableau	Server	启用透传	Execute	as	user	为当前登陆用户账号，您可以使用一
个认证的用户委任查询请求给另一个用户。Tableau	Server	发送给	Kyligence	Enterprise	的查询会以委任的	Execute	as	user
来执行。

用户委任

这样就实现了	Tableau	Server	与	Kyligence	Enterprise	用户账户的单点登录，用户在	Tableau	Server	中查询	Kyligence
Enterprise	数据时，无需进行二次登陆。且通过用户委任，您也可以让	Tableau	Server	和	Kyligence	Enterprise	实现统一的
数据权限配置，用户在	Tableau	Server	上查看报表时，直接复用在	Kyligence	Enterprise	中设置的行级、列级、表级权
限。

前置条件

使用	Tableau	Desktop	和	Server	2020.4	版本及以上

使用	Kyligence	Enterprise	4.1.6	版本及以上

使用	Kyligence	ODBC	Driver	3.1.9	及以上

在安装	Tableau	Desktop	及	Tableau	Server	的机器上配置了	Kyligence	数据源连接器

请确保您要使用的	Tableau	Server	用户名在	Kyligence	Enterprise	中有同名的认证用户。我们称之为	Execute	as	user。
您可以通过手动设置、LDAP	服务或者其他第三方用户认证系统来配置	Tableau	Server	和	Kyligence	Enterprise	用户
在	Kyligence	Enterprise	的配置文件	/conf/kylin.properties	中将	kylin.query.query-with-execute-as	配置成	true，并重启
Kyligence	Enterprise	服务使参数生效
作为嵌入式账号的	Kyligence	Enterprise	用户具有项目中所有的表级、列级、行级权限，强烈建议使用项目管理员或
系统管理员。因为项目管理员或系统管理员不受配置项	 	kylin.acl.project-internal-default-permission-granted		的
限制，默认拥有所有的表级、列级、行级权限。其他用户角色，如果	 	kylin.acl.project-internal-default-
permission-granted		设为	false，默认不具有任何表级、列级、行级权限。

配置用户委任

674

与	BI	工具连接

用户委任仅在	Tableau	Server	上生效。当您使用	Tableau	Desktop	发布工作簿到	Tableau	Server	时，请确保使用了
Kylgience	Connector	作为数据源连接，并在发布工作簿时，配置身份认证方式为“通过嵌入式密码进行模拟”。

通过嵌入式密码进行模拟

验证用户委任是否生效

如果用户委任生效，当用户登陆	Tableau	Server	查看报表时，你可以在	ODBC	的日志中查看到	Execute	as	user	ID	的参
数。了解如何启用	Kyligence	ODBC	日志。

675

与	BI	工具连接

问题排查

验证用户委任是否生效

下面是在使用用户委任过程中一些常见的报错信息以及具体的问题解释和解决方案。如果您遇到更多问题无法解决请联

系	Kyligence	技术支持。

报错

解释

解决方案

EXECUTE_AS_USER_ID	cannot	be	empty,
please	check	its	value	in	the	Kyligence	ODBC
connection	string.

Tableau	没有将委任的用户账
号正确的传给	Kyligence
ODBC

请确认您是否在安装
Tableau	Server	的机器正确
配置	Kyligence	connector	。

value	of	EXECUTE_AS_USER_ID	cannot
exceed	1024	characters.

Execute	user	id	参数的长度超
过最大长度	1024	个字符时

请使用更加简短的用户ID。

KE-10024001(Access	Denied):	Access	is	denied"

当前的	Tableau	没有
Kyligence	数据源的访问权限

请为用户授权	Kyligence	访
问权限

User	[xxx]	does	not	have	permissions	for	all
tables,	rows,	and	columns	in	the	project	[xxx]	and
cannot	use	the	executeAs	parameter

上传	Tableau	工作簿的嵌入式
账号在	Kyligence	Enterprise	中
没有足够的访问权限

使用在	Kyligence	中没有限
制行级、列级、表级权限的
用户作为嵌入式账号

User	[xxx]	in	the	executeAs	field	does	not	exist

当前登录的	Tableau	用户在
Kyligence	Enterprise	中不存在

请为用户授权	Kyligence	访
问权限

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:01

676

与	BI	工具连接

与	Power	BI	集成

本章节介绍	Kyligence	Enterprise	如何与	Power	BI	集成。

包含如下内容：

与Power	BI	Dekstop	集成
与	Power	BI	Service集成

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:01

677

与	BI	工具连接

与	Power	BI	Desktop	集成

Kyligence	Enterprise	是微软	Power	BI	Desktop	内置的数据源之一，本章节将介绍	Kyligence	Enterprise	与	Power	BI	Desktop
的集成。

安装	Kyligence	ODBC	驱动程序

有关安装信息，参考页面	Kyligence	ODBC	驱动程序教程。

使用	Power	BI	Desktop	连接	Kyligence	Enterprise

先决条件：

如果您的	Power	BI	Desktop	版本	>=	2018年10月版本	(v2.63)，则您使用	Power	BI	Desktop	内置的	Kyligence
Enterprise	Data	Connector	for	PowerBI	连接	Kyligence	Enterprise，因为自该版本起	Kyligence	成为其内置的认证数据
源。

如果您的	Power	BI	Desktop	版本	<	2018年10月版本	(v2.63)，请先按照本文末的步骤	安装	Kyligence	Enterprise	Data
Connector	for	PowerBI	插件。之后，再继续下面步骤。

连接	Kyligence	Enterprise	的具体方法：

1.	 启动已经安装的	Power	BI	Desktop，单击	Get	data	->	more，在	Database	类别下选中	Kyligence	Enterprise。

注意：为了更好地与	PowerBI	集成，请开启	Kyligence	Enterprise	查询下压，操作请参考	查询下压页面。

678

与	BI	工具连接

选中	Kyligence	Enterprise

2.	 在连接字符串文本框中输入所需的数据库信息。请选择	DirectQuery	作为数据连接方式。

注意：	当您的	Kyligence	Enterprise	部署在	Azure	时，需要在	Server	处填入	https://	，同时填写443端口。

679

与	BI	工具连接

数据连接方式：DirectQuery

3.	 输入账号密码进行身份验证。

680

与	BI	工具连接

4.	 这样	Power	BI	会列出项目中所有的表，可以根据需要选择要连接的表。

5.	 现在可以进一步使用	Power	BI	进行可视化分析，首先对需要连接的表进行建模。

注意：	编辑关系时，如果表的关联关系为	INNER	JOIN，请选中假设引用完整性，更多介绍，见应用假设引
用完整性。

681

与	BI	工具连接

对需要连接的表建模

6.	 现在可以回到报表页面开始可视化分析。

安装	Kyligence	Enterprise	Data	Connector	for	PowerBI	插件

如果您的	Power	BI	Desktop	版本	<	2018年10月版本	(v2.63)，您可以按照以下步骤安装	Kyligence	Enterprise	Data
Connector	for	PowerBI	插件：

1.	 在	Kyligence	Account	页面下载	Kyligence	Enterprise	Data	Connector	for	PowerBI	插件。

2.	 将	DirectQuery	插件文件（.mez	文件）复制到	Power	BI	安装目录	 	[Documents]\Microsoft	Power	BI	Desktop\Custom

Connectors		文件夹中。如果没有	Custom	Connectors	这个文件夹，请手动创建。

682

与	BI	工具连接

3.	 打开	Power	BI	Desktop	中	Options	and	settings	下的	Options。	在	Preview	Features	中勾选	Custom	data

connectors：

提示：	Power	BI	2.61版本无法显示	Kyligence	connector，须修改扩展插件安全设置。您可以依次选择文件->
选项和设置->选项->安全，在数据扩展插件下，从两个安全级别中进行选择	（不推荐）允许加载任何插件而
不发出警告。

4.	 重启	Power	BI	Desktop。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:01

683

与	BI	工具连接

与	Power	BI	Service	集成

Microsoft	Power	BI	Service	也被称为	Power	BI	online，是一个具有强大的分析能力及协作管理能力的在线	SaaS	服务。可
以轻松与	Power	BI	Desktop	或	Power	BI	Mobile	进行协作，搭建企业级	BI	平台。

Power	BI	Desktop，Microsoft	Power	BI	Service，Microsoft	Power	BI	Mobile	关系

本文将分步介绍如何使用	Power	BI	Service	连接	Kyligence	Enterprise。

Power	BI	Desktop	集成

Power	BI	Service	通过	Power	BI	Desktop	发布报表，需要已经安装	Power	BI	Desktop	并集成	Kyligence。关于如何使用
Power	BI	Desktop	连接	Kyligence	Enterprise	的信息请参考页面	Power	BI	Desktop	集成。

注意：Power	BI	service	和	Power	BI	Desktop	通过	Power	BI	账号进行关联，所以在将报表发布到	Power	BI	service
时，Power	BI	Desktop	需处于正确的登录状态。

安装	Gateway

Power	BI	service	通过	Gateway	和本地服务器进行通信，您可以参考	Microsoft	的	Gateway	安装页面完成	Gateway	安装。

注意：

1.	 Gateway	不需要和	Power	BI	Desktop	安装在同一机器上。
2.	 运行	Gateway	的机器网络通畅且能访问	Kyligence	Enterprise	Data	Connector	for	PowerBI	配置的数据源
3.	 运行	Gateway	的机器需要安装64位的	Kyligence	ODBC	驱动程序
4.	 有关如何下载和配置	Kyligence	ODBC	驱动程序的详细信息，请参阅	Kyligence	Enterprise	用户手册中

Kyligence	ODBC	驱动程序教程。

配置	Gateway

684

与	BI	工具连接

1.	 完成	Gateway	安装后，在运行网关的计算机上，启动管理员命令提示符，运行	 	net	start	PBIEgwService		命令启动

Gateway	服务。

2.	 启动	Gateway	服务后，您可以通过双击	On-premises	data	gateway	程序图标进行	Gateway	的配置。详细的本地数据

网关配置，请参考	Microsoft	的教程	本地数据网关。

3.	 您也可以通过在运行网关的计算机上，启动管理员命令提示符，运行	 	net	stop	PBIEgwService		命令停止	Gateway

服务。

向	Power	BI	Service	添加数据源

1.	 登录	Power	BI	service	后，在右上角，选择齿轮图标>管理网关。

管理网关

2.	 选择一个网关	>“添加数据源”	，或转到“网关”>“添加数据源”	。

685

与	BI	工具连接

新增	Data	Source

3.	 选择"选择数据类型"，为	Kyligence	Enterprise。

选择数据源类型

4.	 输入数据源的信息，数据源的配置信息需与在	Power	BI	Desktop	上的	Kyligence	Enterprise	的连接信息保持一致。

686

与	BI	工具连接

配置数据源

5.	 您可以在	Data	Source	Settings	的右侧，点击	Users	选项，为	DATA	SOURCE	增加用户，被增加的用户将拥有发布
报表的权限。若要了解更多的	Power	BI	Service	的配置功能，可以参考	Microsoft	的官方教程	管理	Power	BI	本地网
关。

通过	Power	BI	Desktop	发布报表到	Power	BI	Service

Gateway	配置全部完成后，在已登录的	Power	BI	Desktop	上编辑并保存报表后，点击	Publish	按钮、选择对应的工作区
域，即可发布报表到	Power	BI	service。	这样，就可以在Power	BI	service对应的工作区域查看及修改上传的报表。

687

与	BI	工具连接

报表发布

查看报表

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:01

688

与	BI	工具连接

与	MicroStrategy	集成

本章节介绍	Kyligence	Enterprise	如何与	MicroStrategy	集成。

包含如下内容：

与	MicroStrategy	Workstation/Desktop	集成
与	MicroStrategy	Secure	Enterprise	集成

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:01

689

与	BI	工具连接

与	MicroStrategy	Secure	Enterprise	集成

支持的平台:

Kyligence	目前支持	MicroStrategy	Secure	Enterprise	10.8及更高版本。

前提条件:

已经安装	MicroStrategy	Secure	Enterprise	10.8或更高版本。
已经安装	Kyligence	Enterprise	。
已经在安装	MicroStrategy	Intelligence	Server	的机器上安装了	JDK	1.8或更高版本。
已经在安装	MicroStrategy	Intelligence	Server	的机器上安装了64位的	Kyligence	ODBC	驱动程序。	有关如何下载和配
置	Kyligence	ODBC	驱动程序的详细信息，请参阅	Kyligence	Enterprise用户手册中	Kyligence	ODBC	驱动程序教程章
节。

判断	MicroStrategy	版本

如果您使用的	MicroStrategy	Enterprise	的版本为	11或以上，您只需要在安装	MicroStrategy	时选择	MicroStrategy
Community	数据连接器，就完成了	Kyligence	的数据连接器的配置，可跳过下方在	MicroStrategy	Intelligence	Server	和
MicroStrategy	Web	中的配置。

如果您使用的	MicroStrategy	Enterprise	早于	11，请参见下方文档手动配置	Kyligence	连接器。

为MicroStrategy	Intelligence	Server	安装Kyligence	连接器

690

与	BI	工具连接

更新数据库对象

1.	 在安装	MicroStrategy	Intelligence	Server	的计算机上下载并拷贝连接器文件。	连接器文件可以点击以下链接下载。

2.	 在	MicroStrategy	的安装目录之外的其他目录解压zip文件

3.	 启动	MicroStrategy	Developer	并登录到2-tier项目源。	转到数据库实例管理器，并编辑您已连接到Kyligence数据源的

实例。点击位于	“	数据库连接类型”	旁边的	“	升级”	按钮，如下所示：

4.	 出现以下窗口。浏览文件，使得数据库类型脚本文件指向在步骤1中获得的	”Database_KAP.PDS“	文件。单击	“加

载”	按钮，如下图所示：

691

与	BI	工具连接

5.	 现在左侧窗格中的可用数据库类型中出现了	Kyligence。	使用箭头按钮将	"Kyligence"	对象从左侧窗格移动到右侧，

如下图所示：

该步骤会帮助您将包含了	Kylignece	的数据库文件	”Database_KAP.PDS“	文件更新到现有的	Intelligence	Server
的	Database.PDS	中。

6.	 单击确定。“Kyligence	2.x”现在显示为可用的数据库连接类型。

692

与	BI	工具连接

在数据库实例管理器中选择	“Kyligence	2.x”。

注意：尽管数据库连接类型为Kyligence	2.x，其连通性已在Kyligence	Enterprise	4.x	上验证可以正常使用。

7.	 点击确定并保存数据库实例。

8.	 重新加载项目，以使新设置生效。

将	MicroStrategy	登陆用户设置成	Kyligence	查询用户

如果您想要使用	MicroStrategy	账号作为	Kyligence	的	 	查询用户	，请完成以下配置，否则请跳过这个步骤。

以下设置需要依赖如下版本	:

1.	 Kyligence	Enterprise	4.1.6	及之后版本
2.	 Kyligence	ODBC	Driver	3.1.9	及之后版本

1.	 确保您要使用的	MicroStrategy	用户名在	Kyligence	Enterprise	中有同名的认证用户。我们称之为	 	查询用户	。您可以

通过手动设置、LDAP	服务或者其他第三方用户认证系统来配置	MicroStrategy	用户并将其设置	 	查询用户		到
Kyligence	Enterprise	。

2.	 确保您在	MicroStrategy	数据库实例的数据库连接中先配置好一个数据库登陆账户作为	 	服务账号	。该 	服务账号		应拥

有待访问的	Kyligence	Enterprise	项目下所有的表/列/行权限。

693

与	BI	工具连接

3.	 在Kyligence	Enterprise	的配置文件	/conf/kylin.properties	中将	 	kylin.query.query-with-execute-as		配置成	 	true	，并

重启	Kyligence	Enterprise	服务。

4.	 修改	MicroStrategy	Developer	的数据库实例管理器中的数据库连接配置，在	 	additional	connection	string

parameters		一项末尾添加	 	EXECUTE_AS_USER_ID=?delegated_mstr_uid	，如下图所示。

通配符	 	?delegated_mstr_uid		将会在	MicroStrategy	运行时被替换成当前登陆的	MicroStrategy	用户名，同时也会被
当作	Kyligence	Enterprise	的	 	查询用户		来执行	sql	查询。

694

与	BI	工具连接

5.	 点击确定，保存数据库实例并重启项目。现在您可以通过	MicroStrategy	连接	Kyligence	Enterprise	，并以

MicroStrategy	 	查询用户		的身份执行	sql	查询，Kyligence	Enterprise	在接受查询后会使用	 	?delegated_mstr_uid		参数
中提供的用户名来进行访问鉴权，数据查询。

更新Intelligence	Server上的数据类型映射

1.	 将	DTMAPPING	和	AddConnector.jar	复制到需要安装连接器的机器。

2.	 查找安装Intelligence	Server的机器上的DTMAPPING.pds文件的位置

提示：在	Windows	上，默认位置是	 	C：\Program	Files（x86）\Common	Files	\MicroStrategy	，也指向环境变量

$	MSTR_CLASSPATH

3.	 用	DTMAPPING.pds	所在的文件夹替换	并运行以下命令，这些命令将帮助您将包含有	Kyligence	的数据类型文件补

充到	MicroStrategy	Web	默认自带的	DTMAPPING.pds	中。

	java	-jar	AddConnector.jar	--target	<location>\DTMAPPING.pds	--file	DTMAPPING

提示：运行该命令需要具有复制和修改现有	DTMAPPING.pds文件的权限。该命令将在	中创建原始
DTMAPPING.pds文件的备份。

4.	 重启	Intelligence	Server.

5.	 重启完成后，用户可以在Intelligence	Server	正常使用Kyligence数据源。

在	MicroStrategy	Web	中安装	Kyligence	连接器

为了在MicroStrategy	Web使用Kyligence数据源，接下来需要在	MicroStrategy	集群中所有的	MicroStrategy	Web	计算机中
完成如下的配置：

1.	 将	DBproperties	文件和	AddConnector.jar	文件复制到运行MicroStrategy	Web的机器。	并将文件的所在路径记为。

2.	 找到MicroStrategy	Web	默认提供的DBProperties.xml文件的所在路径，并将此路径记为。

DBProperties.xml文件的路径默认为

Microsoft	IIS:	 	C:\Program	Files	(x86)\MicroStrategy\Web	ASPx\WEB-INF\xml\DBproperties.xml

Tomcat	(on	Windows):	 	C:\Program	Files	(x86)\Common	Files\MicroStrategy\Tomcat\apache-tomcat-

8.0.30\webapps\MicroStrategy\WEB-INF\xml\DBProperties.xml

Tomcat	(on	Linux):	 	/opt/apache/tomcat/apache-tomcat-8.0.43/webapps/MicroStrategy/WEB-

INF/xml/DBproperties.xml

3.	 替换和，并执行如下命令，这些命令会帮助您将包含有	Kylignece	数据源信息的DBProperties	文件补充到

MicroStrategy	Web	默认的	DBProperties	文件中。

java	-jar	<location1>\AddConnector.jar	--target	<location2>\DBProperties.xml	--file	<location2>\DBpropertie

s

提示：

运行该命令需要具有复制和修改现有DBproperties.xml文件的权限。

在Windows上，需要以反斜杠	“	\	”	字符结束，在Linux上需要以正斜杠	“	/	”	字符结束。

该命令将在中创建原始DBProperties	文件的备份。

4.	 运行上述命令后，请重新启动您的应用程序服务器。

5.	 设置连接器图标:

默认情况下，数据导入主页中的图标是如下所示数据库的常规图标：

695

与	BI	工具连接

要自定义图标，请将KyligenceConnectorFiles.zip中的图标文件放到 	<MSTR_WEB_SERVER>\javascript\
mojo\css\images\DI\connectors\		路径中。

然后在数据源处搜索	Kyligence	来连接	Kyligence，或者可以在	Hadoop	连接类别下找到	Kyligence。

使用	MicroStrategy	连接	Kyligence	Enterprise	的最佳实践

以下是经笔者测试的	MicroStrategy	连接	Kyligence	Enterprise	的最佳实践，建议按照下面操作配置你的	MicroStrategy	环
境以优化和	Kyligence	Enterprise	的连接。

1.	 建议在	MicroStrategy	环境中修改	VLDB	配置，设置	report	intermediate	table类型为	derived	来避免	MicroStrategy	生
成临时表，以提高查询效率。修改方法为在	MicroStrategy	的	report	中菜单选择	Data->	VLDB	property->	Tables->
Intermediate	Table	Type设置为Derived即可。

2.	 避免使用以下	MicroStrategy功能，因为下面的功能可能会生成多段SQL语句，这些多段的SQL语句无法通过VLDB

配置规避。

使用	Datamarts
使用	partitioned	tables
使用	custom	groups

696

与	BI	工具连接

3.	 如果	Kyligence	数据模型中有事实表向维度表的左连接，MicroStrategy	生成的	SQL	也需要产生相同的左连接来击中
Model，默认情况下	MicroStrategy	仅会生成内连接，	可以参照以下	MicroStrategy	技术文档来修改	MicroStrategy	的
VLDB	配置实现左连接：https://community.microstrategy.com/s/article/...

4.	 默认情况下	MicroStrategy	生成的	SQL	语句在对日期进行过滤时日期的格式为	'mm/dd/yyyy'。这个格式可能会和

Kyligence	Enterprise	中的日期格式不一致，导致查询报错。	可以参考以下文章来修改	MicroStrategy	的配置，使其生
成与	Kyligence	Enterprise	的日期格式一致的日期过滤查询：https://kyligence.zendesk.com/...

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:01

697

与	BI	工具连接

与	MicroStrategy	Workstation/Desktop	集成

前提条件:

1.	 已经安装	MicroStrategy	Workstation	/	Desktop	10.10	或更高版本。
2.	 已经安装	Kyligence	Enterprise	。
3.	 已经在安装	MicroStrategy	Workstation	/	Desktop的机器上安装了	JDK	1.8或更高版本。
4.	 已经在安装	MicroStrategy	Workstation	/	Desktop的机器上安装了64位的Kyligence	ODBC	驱动程序。	有关如何下载和
配置	Kyligence	ODBC驱动程序的详细信息，请参阅	Kyligence	Enterprise	用户手册中	Kyligence	ODBC	驱动程序教程
章节。

5.	 已经完成在	MicroStrategy	Inteligence	Server	和	MicroStrategy	Web	中	Kylignece	数据源的配置。

在	MicroStrategy	Workstation/Desktop上安装连接器:

1.	 按照手册中MicroStrategy	Web	中安装	Kyligence连接器的步骤更新	DBProperties.xml	文件，并使用生成的

DBProperties.xml	文件完成以下步骤。

您必须拥有一个MicroStrategy	Web	环境才能完成以上操作。

2.	 更新	DBProperties.json	文件

解压下载的	KyligenceConnectorFiles.zip	中的	utils.zip

在	Windows	中以管理员权限运行	run.bat	脚本

运行脚本后，该工具会自动将原始DBProperties.xml转换为两个新文件	DBProperties.json32	和
DBProperties.json64，将	DBProperties.json64	重命名为	DBProperties.json	，并使用此新文件替换	MicroStrategy
Workstation	/	Desktop	中的旧文件。

旧文件默认路径：[MSTR_WINDOWS_WORKSTATION/DESKTOP安装目录]\code\config	for	Windows

Platform

3.	 要自定义图标，请将KyligenceConnectorFiles.zip中的图标文件放到[MSTR_WINDOWS_WORKSTATION/DESKTOP

安装目录]\code\javascript\mojo\css\images\DI\connectors\	路径中

4.	 使用在配置	MicroStrategy	Intelligence	Server	中生成的DATABASE.PDS	文件和	DTMapping.PDS	文件替换Workstation

/	Desktop	中原有的DATABASE.PDS	and	DTMapping.PDS	文件

Workstation	默认位置:	C:\Program	Files\MicroStrategy\Desktop

Desktop	默认位置:	C:\Program	Files\MicroStrategy\Desktop

该步骤要求您拥有	MicroStrategy	Intelligence	Server	环境，并已经可以通过MicroStrategy	Inteligence	Server	连
接	Kyligence数据源。

5.	 重启	Workstation	/	Desktop。

请注意，Kyligence	在	Mac	版	Workstation	/	Desktop	中尚不支持。

使用	MicroStrategy	Desktop	连接Kyligence:

1.	 打开	MicroStrategy	Desktop并选择	New	Data，选择	Kyligence	作为数据源

698

与	BI	工具连接

2.	 然后，选择	Select	Table	方式

699

与	BI	工具连接

3.	 接着，您可以任意选择	DSN	数据源或	DSN-less	数据源。如果使用	DSN	数据源的话则首先需要在	ODBC	Manager

中先配置DSN。选择数据类型为	Kyligence。

700

与	BI	工具连接

4.	 成功创建数据源后即可选择表、表连接关系及定义维度和度量，以匹配	Kyligence中的数据模型。

701

与	BI	工具连接

5.	 为了完全发挥经过预计算的	Model	的能力，请选用	Connect	Live	方式进行连接，而无需将数据导入内存。

6.	 连接数据之后就可以自由地在	MicroStrategy	Desktop中使用	Kyligence中的数据源了。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:01

702

与	BI	工具连接

与	Cognos	集成

安装	Kyligence	ODBC	驱动程序

Kyligence	Enterprise	支持通过	Kyligence	ODBC	驱动程序与	Cognos	集成，目前支持Window	及	Linux	版本的Cognos，已
测试支持版本包含Cognos	10.x	及	11.x的。

有关Kyligence	ODBC安装信息，请参考页面	Kyligence	ODBC	驱动程序教程。

前置条件

Cognos	Framework	manager	的版本与	Cognos	server	的版本需要一致。

Framework	manager	和	Cognos	server	需要使用相同版本的	32位	ODBC	Driver。

Framework	manager	和	Cognos	server	安装的机器都需要安装	Kyligence	ODBC	驱动且DSN	的名字在	Framework
manager	和	Cognos	server	需要一致。

配置	CALCITE	相关适配参数，支持系统级和项目级设置

##	使用模型回答查询

kylin.query.transformers=io.kyligence.kap.query.util.ReplaceStringWithVarchar,org.apache.kylin.query.util.P

owerBIConverter,org.apache.kylin.query.util.DefaultQueryTransformer,io.kyligence.kap.query.util.EscapeTrans

former,io.kyligence.kap.query.util.CognosParenthesesEscapeTransformer,io.kyligence.kap.query.util.ConvertTo

ComputedColumn,org.apache.kylin.query.util.KeywordDefaultDirtyHack,io.kyligence.kap.query.security.RowFilte

r

##	使用下压引擎回答查询

kylin.query.pushdown.converter-class-names=org.apache.kylin.source.adhocquery.DoubleQuotePushDownConverter,

org.apache.kylin.query.util.PowerBIConverter,org.apache.kylin.query.util.KeywordDefaultDirtyHack,io.kyligen

ce.kap.query.util.CognosParenthesesEscapeTransformer,io.kyligence.kap.query.util.RestoreFromComputedColumn,

io.kyligence.kap.query.security.RowFilter,io.kyligence.kap.query.security.HackSelectStarWithColumnACL,io.ky

ligence.kap.query.util.SparkSQLFunctionConverter

##	智能推荐相关

kylin.query.table-detect-transformers=org.apache.kylin.query.util.PowerBIConverter,org.apache.kylin.query.u

til.DefaultQueryTransformer,io.kyligence.kap.query.util.EscapeTransformer,io.kyligence.kap.query.util.Cogno

sParenthesesEscapeTransformer

创建一个Cognos数据源

在安装完	Kyligence	ODBC	Driver	并配置好	DSN	后，打开一个已有	Cognos	项目或者创建一个新项目。在本例中我们将
创建一个新项目。

703

与	BI	工具连接

1.	 创建新项目

左下角的	 	Use	Dynamic	query	Mode	不要打勾。

2.	 使用 	元数据向导	创建新 	数据源	。

3.	 选择	New	新建一个数据连接，如果已经存在的连接可用，请直接选择。

704

与	BI	工具连接

705

与	BI	工具连接

4.	 在 	新建数据源向导	第一步中输入数据源名称。

706

与	BI	工具连接

5.	 选择 	ODBC	作为连接类型。在 	隔离级别	中，选择 	使用默认对象Gateway	。

707

与	BI	工具连接

6.	 在	ODBC	数据源中填入上一步创建的	DSN	的名称。勾选 	Unicode	ODBC	。在 	登陆	项中勾选 	无身份认证		或者选择 	登

陆	此处需要输入登录Kyligence	Enterprise的账号。随后点击 	测试连接	。

708

与	BI	工具连接

7.	 如果一切配置正确的话，测试连接会顺利通过。

709

与	BI	工具连接

这样数据源就创建成功了。

8.	 点击 	下一步	你可以继续在 	元数据向导	中测试表的连接。

测试连接

1.	 下面我们对已创建的数据源连接进行测试。首先选择需要导入项目中的表。

710

与	BI	工具连接

2.	 下一步的所有参数可以保留默认配置。

711

与	BI	工具连接

3.	 现在新数据源已经被导入到项目中了。右键一个表测试表的连接。

712

与	BI	工具连接

4.	 在测试的弹窗中，点击 	测试示样	来测试与表的连接。如果连接配置正确，测试结果会返回在弹窗中。

713

与	BI	工具连接

5.	 Cognos	对	Kyligence	Enterprise	的字段属性不识别，因此需要修改对应字段的属性.调整字段的	Usage	类型。每个字
段在	Cognos	里面有	4	个类型，Fact，Identifier，	Attribute	和	unknown。日期和做	ID	的字段可以选为	Identifier，	数
字类型可累加的	选	fact，字符型选	Attribute。

714

与	BI	工具连接

6.	 右键表名，为表设置relationship

7.	 为表设置	relationship。在选择	Cardinality	和	Operator	的时候，会显示相应解释

715

与	BI	工具连接

8.	 或者您也可以双击数据源名称，在	Diagram	页面，通过	ctrl+点选两个字段后，右键选择Create	->	Relationship	可建

立表之间的关联。

自定义SQL

如果遇到需要对现有表结构，列进行调整，如转换某列对格式，您也可以选择使用自定义SQL。

1.	 选择右键数据源选择新建Query	Subject

716

与	BI	工具连接

2.	 第二步选择创建 	Data	Source	类型。

3.	 选择数据源，请注意不要勾选“run	databases	query	subject	wizard”

717

与	BI	工具连接

4.	 输入SQL语句，点击Validate，确认没有报错后，点击OK。

718

与	BI	工具连接

select

				KYLIN_CAL_DT.CAL_DT,

				KYLIN_SALES.PART_DT,

				KYLIN_SALES.BUYER_ID,

				KYLIN_SALES.ITEM_COUNT

From

[sandbox-dong].KYLIN_SALES	as	KYLIN_SALES

join

[sandbox-dong].KYLIN_CAL_DT	as	KYLIN_CAL_DT

on	KYLIN_SALES.PART_DT	=	KYLIN_CAL_DT.CAL_DT

创建命名空间

建立好模型后可右键数据源，选择Create	->	Namespace。然后可以将导航栏中的表拖拽到同一个命名空间中。

719

与	BI	工具连接

发布数据包

在项目查看器中，右键 	数据包	-> 	新建	-> 	数据包	将需要使用的表进行发布。

720

与	BI	工具连接

首先创建数据包，在创建流程中第一步先为数据包命名。

721

与	BI	工具连接

第二步选择数据包中需要包含的表。

722

与	BI	工具连接

第三步选择包中支持的 	函数集	，这里可以保留默认的设置。

723

与	BI	工具连接

这样数据包就创建成功了，接下来进入 	发布数据包向导	。

下面的步骤可以保留默认配置。

724

与	BI	工具连接

725

与	BI	工具连接

这样数据包就发布成功了。

发布成功后，在IBM	Cognos	Connection	网页端中可查看到已发布的数据包。

726

与	BI	工具连接

创建一个简单的图表

下面我们可以使用发布好的数据包来制作一个简单的图表。

在	IBM	Cognos	Conenction	网页端启动 	Report	Studio	。

选择之前创建好的数据包。

727

与	BI	工具连接

在 	Report	Studio	中选择 	新建	。

使用新创建的数据包，选择 	图表	。

728

与	BI	工具连接

选择一个图表类型。

729

与	BI	工具连接

将维度和度量拉拽到报表上。

730

与	BI	工具连接

点击菜单中的 	运行	键运行报表。

这样你就成功的使用	Kyligence	Enterprise	作为数据源创建了一个图表。

731

与	BI	工具连接

Cognos	与	Kyligence	Enterprise	权限集成

为了支持输入不同的用户名和密码，需要进行	Cognos	与	Kyligence	Enterprise	权限集成。本小节在默认已经配置	Cognos
认证程序的基础上进行	Kyligence	Enterprise	与	Cognos	的	ODBC	用户集成，以自定义的	Java	为样例来进行介绍。有关详
细信息，请参考	Cognos	SDK	对应的	AuthenticationProvider	文档。下图是以	Java	程序为例子的典型	Cognos	外部认证空
间：

在	Cognos	权限认证对应的数据库中，添加	Kyligence	Enterprise	的用户名和密码：

创建一个	Cognos	数据源，第一步至第四步与上面相同，在第五步中，选择 	外部名称空间	：

732

与	BI	工具连接

点击测试连接后，可以看到测试成功的提示，这说明	Cognos	通过	Kyligence	Enterprise	的	ODBC	已成功连接	Kyligence
Enterprise	的	server。

已知局限

1.	 Kyligence	Enterprise	在建模时不支持	fact	table	right	join	lookup	的形式。

解决方案:	可以建立视图为

create	view	vw_1	as

sleect	*

from	fact	table

right	join	lookup	table

然后以该视图作为建模的事实表，则可以实现	right	join，缺点是需要单独对视图建模。

2.	 Kyligence	Enterprise	暂不支持多事实表建模

解决方案：	在	Cognos	的	Framework	Manager	中建立查询时	sql	写成子查询	join	的形式，每个子查询针对一个事实
表，类似下面这样(在	learn_kylin	的	project	下可以测试):

select	a.part_dt,sum_price,sum_item

from

(select	part_dt,sum(price)	as	sum_price

	from	KYLIN_SALES

733

与	BI	工具连接

	group	by	PART_DT	havingsum(price)>1000)	a

join	(

		select	part_dt,sum(ITEM_COUNT)	as	sum_item

		from	KYLIN_SALES

		where	LSTG_FORMAT_NAME='Others'

		group	by	part_dt)	b

on	a.part_dt=b.part_dt

FAQ

Q:	在使用	Cognos	网页版运行	data	module	report	进行查询时，语句中会默认带有	defaultCataog，导致查询失败。	解
决方案：在	kylin.properties	中把	 	kylin.query.escape-default-keyword		设置为	true，删除	defaultCatalog。

Q:	下压查询不支持	OFFSET	FETCH	的	SQL	语法。	解决方案：在	kylin.properties	中在
	kylin.query.pushdown.converter-class-names		里加上	org.apache.kylin.query.util.DialectConverter	(此Converter需要放在该
配置的最前面)。

示例：

kylin.query.pushdown.converter-class-names=org.apache.kylin.query.util.DialectConverter,org.apache.kylin.source

.adhocquery.DoubleQuotePushDownConverter,org.apache.kylin.query.util.PowerBIConverter,io.kyligence.kap.query.ut

il.RestoreFromComputedColumn,io.kyligence.kap.query.security.RowFilter,io.kyligence.kap.query.security.HackSele

ctStarWithColumnACL,io.kyligence.kap.query.util.SparkSQLFunctionConverter

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:01

734

与	BI	工具连接

与	Oracle	Business	Intelligence/OBIEE	集成

本章节介绍	Kyligence	Enterprise	如何与	OBIEE	集成。

包含如下内容：

与	OBIEE	11g	集成
与	OBIEE	12c	集成
与	Oracle	BI	Publisher	集成
OBIEE	设置行级安全性

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:01

735

与	BI	工具连接

与OBIEE	11g	集成

OBIEE是Oracle旗下的BI产品，可提供完整的	BI	功能，包括交互式信息板、完全即席的主动式智能和警报、企业和财务
报表、实时预测智能以及离线分析等。本文将分步介绍使用OBIEE	11g连接Kyligence	Enterprise的方法。

前置条件：

Kyligence	Enterprise	版本	3.0	或以上
Kyligence	ODBC	版本	2.2	或以上

配置ODBC及DSN

1.	 配置	Client

需要先安装	BI	Administrator	tool	，安装后在	ODBC	管理器中增加对	BIEE	server的连接DSN	。

ODBC管理器增加连接

736

与	BI	工具连接

连接后在	BI	Administrator	tool	中点击打开-联机打开即可管理	BIEE	server	中的数据模型。

管理数据模型

2.	 设置DSN

在	client	端和	server	端都需要安装	Kyligence	ODBC	并配置	DSN，且两端的	DSN	名称应保持一致。

有关	Windows	下	Kyligence	ODBC	的配置，请参考Windows下安装与配置Kyligence	ODBC驱动。

有关	Linux	下配置	Kyligence	ODBC	的配置，请参考Linux下安装与配置Kyligence	ODBC驱动中的Configuring
Database	Connections	Using	Native	ODBC	Drivers部分。

在 	obdc.ini	文件中增加的	Kyligence	数据源格式为：

[KyligenceDataSource]

Driver	=	KyligenceODBC64

PORT	=	7070

PROJECT	=	learn_kylin

SERVER	=	http://kapdemo.chinaeast.cloudapp.chinacloudapi.cn			#(Optional)

UID	=	KYLIN			#(Optional)

PWD	=	ADMIN

创建数据模型

1.	 在	BI	Administrator	tool	中点击导入元数据来增加数据源。

737

与	BI	工具连接

增加数据源

2.	 选择	ODBC3.5，将	Kyligence	Enterprise	中的表导入。

导入	Kyligence	Enterprise	中的表

738

与	BI	工具连接

3.	 导入成功后，在物理模型里面找到之前创建的数据源，右键选择属性->通用->数据源定义，将数据库类型修改

为Apache	Hadoop。

4.	 在物理模型里找到	Kyligence	Enterprise	数据源，复选需要建模的表右键，选择物理图表进行建模。

进行建模

5.	 点击新建联接定义表关联关系，然后保存物理模型。

739

与	BI	工具连接

新建连接关系

6.	 保存模型后，您需要手动检索并更改数据类型为字符串的物理列，展开表后，右键点击各列，点击属性，即可进入

编辑页面

编辑物理列

740

与	BI	工具连接

7.	 您在手动检索并更改数据类型为字符串的物理列，如果长度显示为	0，则需要更改为	Kyligence	Enterprise	中字段的

实际长度。

更改数据类型

8.	 保存物理模型后，您需要在业务模型和映射区域，右键点击空白区域，出现菜单，以新建业务模型

741

与	BI	工具连接

新建业务模型

9.	 然后将刚才增加的物理模型拖动到业务模型，并保存到业务模型。

更新业务模型

10.	 然后将刚才增加的逻辑模型拖动到表示层，并保存到表示层。

742

与	BI	工具连接

更新表示层

11.	 点击	BI	Administrator	tool	中左上角的文件-保存，保存整个模型。

保存模型

743

与	BI	工具连接

12.	 登陆BIEE服务器，使用以下代码，重启	BIEE	server。

$	service	obiee	stop
-	停止服务器

$	service	obiee	start
-	启动服务器

创建分析

有两种方式可以使用刚才创建的模型中的数据进行分析。

方法一

1.	 在	BIEE	主页点击新建-分析，使用在client端创建的主题区域即可使用	Kyligence	Enterprise	进行分析。这种方式

使用拖拽查询方式方式。

新建分析

2.	 拖动所需字段到所选列即可，度量需要点击字段右下角的编辑公式编辑聚合方式。

编辑公式

其他需要再加工的字段都可以在编辑公式里进行再定义。

744

与	BI	工具连接

其他编辑公式

3.	 点击结果即可看到查询结果，然后编辑所需图表类型及相关样式即可。

查看结果

745

与	BI	工具连接

方法二

1.	 在	BIEE	主页点击新建-分析-创建直接数据库查询，使用自定义	SQL	进行查询。

创建直接数据库查询

2.	 选择在	client	端创建的数据源的连接池名进行连接，输入查询	SQL	进行分析。

连接池名称格式： 	"dsn_name"."connect_pool_name"

连接数据库

3.	 点击结果即可得到查询结果，点击结果左下角的新建视图可以更改图表类型。

746

与	BI	工具连接

查看查询结果

更改查询图表类型

注意事项

1.	 根据	BIEE	的开发规范，在	client	端创建的模型最少需要有两张表，否则上载模型会导致	BIEE	无法启动服务。
2.	 由于	BIEE	产生的查询	SQL	不带	schema	，拖拽查询则需要一个项目里只含有一个	database	的表。在连接池查询时

使用自定义SQL查询可以避免此问题	。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:01

747

与	BI	工具连接

与	OBIEE	12c	集成

Oracle	Business	Intelligence	Enterprise	Edition	(OBIEE)	是	Oracle	旗下的	BI	产品，可提供完整的	BI	功能，包括交互式信息
板、完全即席的主动式智能和警报、企业和财务报表、实时预测智能以及离线分析等。本文将分步介绍使用	OBIEE	连
接	Kyligence	Enterprise	的方法。

前提条件

Kyligence	Enterprise	版本高于	3.0
Kyligence	ODBC	驱动版本高于	2.2

配置	ODBC	及	DSN

1.	 配置	OBIEE	Client

需要先安装	BI	Administrator	tool	，安装后在	ODBC	管理器中增加对	BIEE	server	的连接	DSN。

配置ODBC

连接后在	BI	Administrator	tool	中点击菜单打开	->	联机，即可管理	BIEE	server	中的数据模型。

748

与	BI	工具连接

连接OBIEE

2.	 设置	DSN

在	client	端和	server	端都需要安装	Kylignece	ODBC	并配置	DSN，且两端的	DSN	名称应保持一致。

有关	Windows	下	Kyligence	ODBC	的配置，请参考	Windows下安装与配置Kyligence	ODBC驱动。

有关	Linux	下	Kyligence	ODBC	的配置，请参考	Linux	下安装与配置	Kyligence	ODBC	驱动中的Configuring	Database
Connections	Using	Native	ODBC	Drivers	部分。

在 	odbc.ini	文件中增加的	Kyligence	数据源格式为：

[KyligenceDataSource]

Driver	=	KyligenceODBC64

PORT	=	7070

PROJECT	=	learn_kylin

SERVER	=	http://kapdemo.chinaeast.cloudapp.chinacloudapi.cn

UID	=	KYLIN

PWD	=	ADMIN

创建数据模型

1.	 在	BI	Administrator	tool	中点击导入元数据来增加数据源。

749

与	BI	工具连接

2.	 选择	ODBC	3.5，将	Kyligence	Enterprise	中的表导入。

750

与	BI	工具连接

3.	 导入成功后，在物理模型里面找到之前创建的数据源，右键选择属性->通用->数据源定义，将数据库类型修改

为Apache	Spark	SQL。

选择数据源

4.	 下一步您可定义数据模型，复选需要建模的表右键，选择物理图表进行建模。

751

与	BI	工具连接

物理表建模

5.	 点击新建联接定义表关联关系，然后保存物理模型。

752

与	BI	工具连接

建立连接

6.	 保存模型后，您需要手动检索并更改数据类型为字符串的物理列，展开表后，右键点击各列，点击属性，即可进入

编辑页面

编辑物理列

7.	 您在手动检索并更改数据类型为字符串的物理列，如果长度显示为	0，则需要更改为	Kyligence	Enterprise	中字段的

实际长度。

753

与	BI	工具连接

8.	 保存物理模型后，您需要在业务模型和映射区域，右键点击空白区域，出现菜单，以新建业务模型

754

与	BI	工具连接

新建业务模型

9.	 保存物理模型后新建业务模型，然后将刚才增加的物理模型拖动到业务模型。

更新业务模型

10.	 如需	left	outer	join	可以选择编辑业务模型,	在此处设置为左外部连接，	并保存到业务模型。

755

与	BI	工具连接

756

与	BI	工具连接

11.	 然后将刚才增加的逻辑模型拖动到表示层，并保存到表示层。

757

与	BI	工具连接

更新表示层

12.	 点击	BI	Administrator	tool	中左上角的文件->保存，保存整个模型。

13.	 登陆BIEE服务器，使用以下代码，重启	BIEE	server。

$	service	obiee	stop
-	停止服务器

758

与	BI	工具连接

$	service	obiee	start
-	启动服务器

创建分析

有两种方式可以使用刚才创建的模型中的数据进行分析。

方法一

1.	 在BIEE主页点击新建-分析，使用在	client	端创建的主题区域即可使用	Kyligence	Enterprise	进行分析。这种方式

使用拖拽查询方式方式。

2.	 拖动所需字段到所选列即可，度量需要点击字段右下角的编辑公式编辑聚合方式。

其他需要再加工的字段都可以在编辑公式里进行再定义。

759

与	BI	工具连接

3.	 点击结果即可看到查询结果，然后编辑所需图表类型及相关样式即可。

方法二

1.	 在	BIEE	主页点击新建-分析-创建直接数据库查询，使用自定义	SQL	进行查询。

2.	 选择在	client	端创建的数据源的连接池名进行连接，输入查询	SQL	进行分析。

连接池名称格式： 	"dsn_name"."connect_pool_name"

760

与	BI	工具连接

3.	 点击结果即可得到查询结果，点击结果左下角的新建视图可以更改图表类型。

注意事项

1.	 根据	BIEE	的开发规范，在	client	端创建的模型最少需要有两张表，否则上载模型会导致	BIEE	无法启动服务。
2.	 由于	BIEE	产生的查询	SQL	不带	schema	，拖拽查询则需要一个项目里只包含同一个	schema	的表。在连接池查询时

761

与	BI	工具连接

使用自定义	SQL	查询可以避免此问题	。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:01

762

与	BI	工具连接

OBIEE	设置行级安全性

本文将引导您在	OBIEE	设置行级安全性，与	Kyligence	进行用户集成，实现数据权限控制。

您可以选择在	OBIEE	存储库或数据库（即	Kyligence）中设置行级安全性。在存储库中实现行级安全性的好处在于：

所有用户共享同一个数据库连接池，可提高性能

所有用户共享缓存，可提高性能

您可以定义和维护适用于许多联合数据源的安全规则

相比之下，在	Kyligence	中实现行级安全性，适用于多个应用程序共享同一个	Kyligence	环境，Kyligence	作为统一的查
询入口。请注意，即使在数据库中设计和实现行级安全性时，仍应在存储库中定义和应用对象权限。

注意：尽管可以在存储库和数据库中都设置行级安全性，但是除非有特殊需要，否则通常不要在两个地方都强制

执行行级安全性。

本节包含以下主题：

在存储库中设置行级安全性（数据过滤器）

在数据库中设置行级安全性

在存储库中设置行级安全性（数据过滤器）

数据过滤器是一项安全功能，它提供了一种在存储库中强制执行行级安全规则的方法。数据过滤器需要使用管理工具在

存储库中设置，并应用于特定的应用程序角色。如果您已在数据库中实现行级安全性，则通常不需要再设置数据过滤

器。

支持在业务模型和映射层、表示层中为对象设置数据过滤器。在逻辑对象上应用筛选器，会影响使用该对象的所有展示

层对象。如果在展示层对象上设置过滤器，则除了可能在基础逻辑对象上设置的所有过滤器之外，还会应用该过滤器。

下图显示了如何在	Oracle	BI	Server	中实施数据过滤器规则。安全规则适用于所有传入的客户端，即使修改了	Logical
SQL	查询，也不会被违反。

在此示例中，已将过滤器应用于应用程序角色。当属于该角色的成员	Anne	Green	发送请求时，将基于过滤器限制返回
结果。由于未将任何过滤器应用于管理员用户的应用程序角色，因此将返回所有结果。	Oracle	BI	Server	生成的	SQL	考
虑了已定义的所有数据过滤器。

763

与	BI	工具连接

存储库行级安全性

您应该始终为特定的应用程序角色而不是单个用户设置数据过滤器。

在存储库中设置行级安全性（数据过滤器），配置步骤如下：

1.	 在管理工具中打开您的存储库

2.	 选择管理，然后选择身份

3.	 在身份管理对话框的树形窗格中，选择	BI	资料档案库

4.	 在右窗格中，选择应用程序角色选项卡，然后双击要为其设置数据过滤器的应用程序角色

注意：如果您处于脱机模式，除非您首先在联机模式下对其进行了修改，否则列表中不会显示任何应用程序角

色。有关更多信息，请参见关于在脱机模式下应用数据访问安全性。

1.	 在应用程序角色对话框中，单击权限

2.	 在应用程序角色	->	权限对话框中，单击数据过滤器选项卡	要创建过滤器，首先要选择需要应用过滤器的对象。然

后，您提供各个对象的过滤器表达式信息

3.	 要添加要对其应用过滤器的对象，请执行以下步骤之一：

单击添加按钮。然后，浏览找到所需的对象，将其选中，然后单击选择

单击名称字段为空的行。然后，浏览找到所需的对象，将其选中，然后单击选择

4.	 要输入单个对象的过滤器表达式，请执行以下步骤之一：

选择数据过滤器，然后单击表达式生成器按钮。在表达式生成器中创建过滤器表达式，然后单击确定

单击数据过滤器字段，以获取合适的过滤，然后键入过滤器表达式

例如，您可能想定义一个过滤器，例如 	"Sample	Sales"."D2	Market"."M00	Mkt	Key"	>	5	，以基于表中另一列的值范围来

限制结果。您还可以在过滤器定义中使用存储库和会话变量。使用表达式生成器包含这些变量以确保语法正确。

1.	 （可选）从状态列表中为每个过滤器选择一个状态。您可以选择以下选项之一：

启用：过滤器将应用于访问对象的任何查询

禁用：不使用过滤器，并且不使用其他更高级别的优先级（例如通过应用程序角色）应用于对象的过滤器

764

与	BI	工具连接

忽略：过滤器未使用，但使用了其他任何过滤器，例如通过其他应用程序角色应用于对象的其他过滤器。如果

没有启用其他过滤器，则不会进行过滤

2.	 除了定义新的过滤器外，您还可以在数据过滤器选项卡中执行其他操作，详细可参考	OBIEE	文档
3.	 单击确定，然后再次单击确定以返回到身份管理

在数据库中设置行级安全性

在数据库中实现行级安全性，首先需要在	Kyligence	创建与	Oracle	BI	Server	中相同的用户，密码也需要一致。接下来在
Kyligence	中为不同用户，设置不同的表、行、列级权限。最后，您需要配置	OBIEE	连接池，以便	Oracle	BI	Server	将每
个用户的凭据传递到	Kyligence	。然后，Kyligence	依据凭据将其自己的	ACL	规则应用于用户查询。

下图显示了如何在数据库中为	Oracle	Business	Intelligence	查询强制实施行级安全性。安全规则适用于所有传入的客户
端，即使修改了	Logical	SQL	查询，也不会被违反。在此示例中，即使	Oracle	BI	Server	生成的	SQL	查询相同，返回的
结果取决于哪个用户生成了查询，基于	Kyligence	数据库中创建的	ACL	规则进行数据过滤。

数据库行级安全性

在数据库中设置行级安全性，配置步骤如下：

1.	 使用管理工具，打开你的资料库

2.	 双击与要为其设置数据库级安全性的数据库

3.	 双击连接池，勾选共享登录，在用户名和口令输入框，分析输入变量	:USER	和	:PASSWORD

4.	 连接池对话框中，单击确定

5.	 再次双击要为其设置数据库级安全性的数据库对象

6.	 在数据库对话框中，选择虚拟专用数据库。选择此选项可确保	Oracle	BI	Server	保护每个用户的缓存条目

7.	 在数据库对话框中单击确定

在数据库中设置行级安全性之后，必须在存储库中为展示层或其他对象设置对象权限。您还可以设置查询限制（管理

者）。有关更多信息，请参见设置对象权限和设置查询限制。

765

与	BI	工具连接

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:01

766

与	BI	工具连接

与	Oracle	BI	Publisher	集成

Oracle	BI	Publisher	是一种报告解决方案，可以比传统报告工具更轻松、更快速地制作、管理和交付所有报告和文档。
使用您的	Web	浏览器或熟悉的桌面工具，针对几乎所有数据源创建所需的报告，从面向客户的完美文档到交互式管理
报告。

本文以	OBIEE	12c	为例，介绍如何与	Oracle	BI	Publisher	集成。

前提条件

在	Oracle	BI	Server	安装	Kyligence	JDBC	驱动程序

1.	 获取	Kyligence	JDBC	驱动程序。有关信息，请参考	Kyligence	JDBC	驱动程序教程。

2.	 将	Kyligence	JDBC	驱动放置	Oracle	BI	Server	安装目录下，如:

${WL_HOME}	/wlserver/server/lib

如

/app/oracle/biee/wlserver/server/lib

3.	 修改配置文件	${WL_HOME}	/oracle_common/common/bin/commExtEnv.sh	中的变量$WEBLOGIC_CLASSPATH，添

加驱动包路径信息，如：

${CLASSPATHSEP}${WL_HOME}/server/lib/kyligence-jdbc-{version}.jar

注意：请不要在路径下同时放置kylin	和	Kyligence	的	JDBC	Jar	包，否则两个	Jar	包会产生冲突。

4.	 重启	Oracle	BI	Server，如

su	oracle

	/app/oracle/biee/user_projects/domains/bi/bitools/bin/stop.sh

	/app/oracle/biee/user_projects/domains/bi/bitools/bin/start.sh

配置	JDBC	连接

1.	 打开BIEE	分析界面，进入”管理>管理	BI	Publisher>JDBC连接“，新建Kyligence	JDBC连接

767

与	BI	工具连接

管理	BI	Publisher

选择	JDBC	连接

1.	 添加配置JDBC链接串

Kyligence的	JDBC	驱动程序遵循了	JDBC	标准接口，用户可通过	URL	指定	JDBC	方式连接到	Kyligence	服务。

URL	格式为：

jdbc:kylin://<hostname>:<port>/<project_name>

URL	参数说明如下：

<hostname>:	主机名

<port>：端口号，如果本产品部署启用了SSL安全认证服务，则应该使用相关HTTPS端口号

768

与	BI	工具连接

<project_name>:	必须指定具体项目名称，并且确认该项目在服务中存在

其他配置参数如下：

<user>:	登陆服务实例的用户名

<password>:	登陆服务实例的密码

<ssl>:	是否开启SSL，值为String类型的"true"或"false"，	默认为"false"。如果是"true"，所有Kyligence的访问都将基于HTTPS

在新建JDBC	连接时驱动程序请选择	Other

数据库驱动程序类为	org.apache.kylin.jdbc.Driver

连接字符串请按照上面的	URL	来输入	，如，

jdbc:kylin//10.1.2.43:7070/learn_kylin

并输入连接	Kyligence	Enterprise	所使用的用户名和口令

点击测试连接，如连接成功会显示已成功建立连接。

新建	Kyligence	JDBC	连接

创建数据模型

新建->数据模型，使用建立好的JDBC连接，查询Kyligence	Enterprise数据

新建数据模型

769

与	BI	工具连接

新建数据模型

选择新建	SQL	查询

新建	SQL	查询

在数据源选项中选择上一步创建的	JDBC	的数据源，SQL	的类型选择标准	SQL。

770

与	BI	工具连接

输入	SQL

选择使用查询构建器来进行数据建模，从而生成和	Kyligence	Enterprise	中数据模型或	Cube	相匹配的模型。

请横向对比	Kyligence	Enterprise	中定义的数据模型和	Cube	上的维度和度量，在查询构建器中定义相同的维度和度量。

创建模型

771

与	BI	工具连接

在条件选项卡将	Kyligence	Enterprise	中	Cube上的维度勾选上分组方式，将Cube上的度量按照相同的聚合函数进行聚
合，比如如您在	Kyligence	Enterprise	的	模型或Cube	中的将列 	KYLIN_CATEGORY_GROUPINGS.META_CATEG_NAME	定义为了维
度，那么在	BIP	中需要将 	KYLIN_CATEGORY_GROUPINGS.META_CATEG_NAME	勾选为分组方式。

在	Kyligence	Enterprise	的型或Cube	中的将列 	PRICE	定义为了度量	 	GMV_SUM	，聚合方式为	SUM，则需要在	BIP	中勾选
	PRICE		函数为	SUM。

查询构建器

或者您也可以手动撰写这段SQL，SQL	生成后建议您将SQL	拷贝到	Kyligence	Enterprise	的分析页面执行，确认生成的
SQL	后击中	Kyligence	Enterprise	中定义的	Cube	或聚合索引。

SQL查询

772

与	BI	工具连接

查询分析

点击数据->查看可预览数据

预览数据

注意：在创建图表时预览的数据是由实例数据生成的，因此在创建图表之前您需要在数据模型页面的数据页面选

择另存为示例数据。

至此数据模型已创建完成，您可以点击创建报表来继续基于该数据模型的报表定义。

773

与	BI	工具连接

查看报表

根据创建报表的引导完成布局，报表类型的选择等，完成报表创建。

774

与	BI	工具连接

创建图表

使用参数

创建参数

首先您需要创建一个参数，点击新建->数据模型->属性->参数，点击号创建新的参数，在本例中我们创建一个
对 	OPS_REGION	字段进行筛选的参数，方便用户在界面输入字段值来进行筛选，根据 	OPS_REGION	字段的情况，我们创建

名称为 	p_region	的参数，类型根据待筛选的 	OPS_REGION	选择字符串类型，参数类型选择文本。

775

与	BI	工具连接

创建参数

创建参数后在创建数据集时可插入参数名使用，如在新建数据集	SQL	查询时输入一个包含参数的	where	条件，如

where	"OPS_REGION"=	:p_region

776

与	BI	工具连接

创建参数

完整	SQL	请参见：

SELECT	"KYLIN_CATEGORY_GROUPINGS"."CATEG_LVL2_NAME"	AS	"CATEG_LVL2_NAME",

	"KYLIN_CATEGORY_GROUPINGS"."CATEG_LVL3_NAME"	AS	"CATEG_LVL3_NAME",

	"KYLIN_CATEGORY_GROUPINGS"."META_CATEG_NAME"	AS	"META_CATEG_NAME",

	"SELLER_COUNTRY"."NAME"	AS	"NAME__SELLER_COUNTRY_",

	"KYLIN_CAL_DT"."YEAR_BEG_DT"	AS	"YEAR_BEG_DT",

	SUM("KYLIN_SALES"."PRICE")	AS	"usr_GMV_SUM_ok",

	COUNT(DISTINCT	"KYLIN_SALES"."SELLER_ID")	AS	"usr_SELLER_CNT_HLL_ok",

	SUM({fn	CONVERT(1,	SQL_BIGINT)})	AS	"usr_TRANS_CNT_ok"

FROM	"DEFAULT"."KYLIN_SALES"	"KYLIN_SALES"

	INNER	JOIN	"DEFAULT"."KYLIN_CAL_DT"	"KYLIN_CAL_DT"	ON	("KYLIN_SALES"."PART_DT"	=	"KYLIN_CAL_DT"."CAL_DT")

	INNER	JOIN	"DEFAULT"."KYLIN_CATEGORY_GROUPINGS"	"KYLIN_CATEGORY_GROUPINGS"	ON	(("KYLIN_SALES"."LEAF_CATEG_ID"

=	"KYLIN_CATEGORY_GROUPINGS"."LEAF_CATEG_ID")	AND	("KYLIN_SALES"."LSTG_SITE_ID"	=	"KYLIN_CATEGORY_GROUPINGS"."S

ITE_ID"))

	INNER	JOIN	"DEFAULT"."KYLIN_ACCOUNT"	"SELLER_ACCOUNT"	ON	("KYLIN_SALES"."SELLER_ID"	=	"SELLER_ACCOUNT"."ACCOUN

T_ID")

	INNER	JOIN	"DEFAULT"."KYLIN_ACCOUNT"	"BUYER_ACCOUNT"	ON	("KYLIN_SALES"."BUYER_ID"	=	"BUYER_ACCOUNT"."ACCOUNT_I

D")

777

与	BI	工具连接

	INNER	JOIN	"DEFAULT"."KYLIN_COUNTRY"	"SELLER_COUNTRY"	ON	("SELLER_ACCOUNT"."ACCOUNT_COUNTRY"	=	"SELLER_COUNTRY

"."COUNTRY")

	INNER	JOIN	"DEFAULT"."KYLIN_COUNTRY"	"BUYER_COUNTRY"	ON	("BUYER_ACCOUNT"."ACCOUNT_COUNTRY"	=	"BUYER_COUNTRY"."

COUNTRY")

where	"OPS_REGION"=	:p_region

GROUP	BY	"KYLIN_CATEGORY_GROUPINGS"."CATEG_LVL2_NAME",

	"KYLIN_CATEGORY_GROUPINGS"."CATEG_LVL3_NAME",

	"KYLIN_CATEGORY_GROUPINGS"."META_CATEG_NAME",

	"SELLER_COUNTRY"."NAME",

	"KYLIN_CAL_DT"."YEAR_BEG_DT"

在查看数据时，用户需要输入参数值，如本例中我们输入	 	Shanghai	，在准备数据模型时可以输入参数值来测试参数的
使用情况

创建参数

本例中，Kyligence	Enterprise	会收到查询，其中的	？代表接受到的参数值

SELECT	"KYLIN_CATEGORY_GROUPINGS"."CATEG_LVL2_NAME"	AS	"CATEG_LVL2_NAME",

	"KYLIN_CATEGORY_GROUPINGS"."CATEG_LVL3_NAME"	AS	"CATEG_LVL3_NAME",

	"KYLIN_CATEGORY_GROUPINGS"."META_CATEG_NAME"	AS	"META_CATEG_NAME",

	"SELLER_COUNTRY"."NAME"	AS	"NAME__SELLER_COUNTRY_",

	"KYLIN_CAL_DT"."YEAR_BEG_DT"	AS	"YEAR_BEG_DT",

	SUM("KYLIN_SALES"."PRICE")	AS	"usr_GMV_SUM_ok",

	COUNT(DISTINCT	"KYLIN_SALES"."SELLER_ID")	AS	"usr_SELLER_CNT_HLL_ok",

	SUM({fn	CONVERT(1,	SQL_BIGINT)})	AS	"usr_TRANS_CNT_ok"

778

与	BI	工具连接

FROM	"DEFAULT"."KYLIN_SALES"	"KYLIN_SALES"

	INNER	JOIN	"DEFAULT"."KYLIN_CAL_DT"	"KYLIN_CAL_DT"	ON	("KYLIN_SALES"."PART_DT"	=	"KYLIN_CAL_DT"."CAL_DT")

	INNER	JOIN	"DEFAULT"."KYLIN_CATEGORY_GROUPINGS"	"KYLIN_CATEGORY_GROUPINGS"	ON	(("KYLIN_SALES"."LEAF_CATEG_ID"

=	"KYLIN_CATEGORY_GROUPINGS"."LEAF_CATEG_ID")	AND	("KYLIN_SALES"."LSTG_SITE_ID"	=	"KYLIN_CATEGORY_GROUPINGS"."S

ITE_ID"))

	INNER	JOIN	"DEFAULT"."KYLIN_ACCOUNT"	"SELLER_ACCOUNT"	ON	("KYLIN_SALES"."SELLER_ID"	=	"SELLER_ACCOUNT"."ACCOUN

T_ID")

	INNER	JOIN	"DEFAULT"."KYLIN_ACCOUNT"	"BUYER_ACCOUNT"	ON	("KYLIN_SALES"."BUYER_ID"	=	"BUYER_ACCOUNT"."ACCOUNT_I

D")

	INNER	JOIN	"DEFAULT"."KYLIN_COUNTRY"	"SELLER_COUNTRY"	ON	("SELLER_ACCOUNT"."ACCOUNT_COUNTRY"	=	"SELLER_COUNTRY

"."COUNTRY")

	INNER	JOIN	"DEFAULT"."KYLIN_COUNTRY"	"BUYER_COUNTRY"	ON	("BUYER_ACCOUNT"."ACCOUNT_COUNTRY"	=	"BUYER_COUNTRY"."

COUNTRY")

where	"OPS_REGION"=	?

GROUP	BY	"KYLIN_CATEGORY_GROUPINGS"."CATEG_LVL2_NAME",

	"KYLIN_CATEGORY_GROUPINGS"."CATEG_LVL3_NAME",

	"KYLIN_CATEGORY_GROUPINGS"."META_CATEG_NAME",

	"SELLER_COUNTRY"."NAME",

	"KYLIN_CAL_DT"."YEAR_BEG_DT"

请查看	JDBC	章节详细了解	Kyligence	Enterprise	动态传参所支持的查询场景。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:01

779

与	BI	工具连接

与	SAP	BusinessObjects/BO	集成

本章节介绍	Kyligence	Enterprise	如何与	SAP	BusinessObjects/BO	集成。

包含如下内容：

与	SAP	BusinessOjects	Client	集成
与	SAP	BusinessOjects	Server	集成

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:01

780

与	BI	工具连接

与	SAP	BusinessOjects	Client	集成

SAP	BusinessObjects（SAP	BO）是	SAP	公司旗下的商务智能产品，自	Kyligence	Enterprise	3.0	版本开始，支持与	SAP
BO	进行集成。	本文将分步介绍	SAP	BO	Web	Intelligence	4.1	与	Kyligence	Enterprise	连接的方法。

配置	ODBC	及	DSN

有关	Kyligence	ODBC	的配置，请参考	Windows	下安装与配置	Kyligence	ODBC驱动。

使用	Universe	设计工具进行建模

1.	管理数据连接

1.1	点击	connections，管理数据连接。

connections

点击新增连接，增加连接。

781

与	BI	工具连接

新增连接

选择下一步

1.2	选择	Generic	ODBC	数据源。

782

与	BI	工具连接

选择数据源

1.3	输入用户名、密码和	DSN	名称即可。

783

与	BI	工具连接

输入用户名等

1.4	选择连接池类型为始终保持连接，然后保存该连接即可。

784

与	BI	工具连接

选择连接池

2.	创建数据模型

2.1	打开	Universe	设计工具，使用刚才新建的数据连接创建模型。

785

与	BI	工具连接

打开设计工具

2.2	将需要使用的表增加到右侧。

786

与	BI	工具连接

增加表

2.3	将度量按照聚合形式增加到右侧，点击完成保存即可。

787

与	BI	工具连接

增加度量

2.4	导入表后会进入建模，首先会根据列名自动匹配连接关系，如果没有被连接的表可以点击增加连接进行连接。

建立连接

2.5	点击连接线即可修改连接关系编辑全部关系后，点击保存即可。

788

与	BI	工具连接

修改连接

3.	发布至服务器

另存为，发布到	CMC	Server	模型路径下。

在胖客户端中创建报表

选择	Server上的	Universe	为数据源	(本地也可以)，并使用新建的	Universe，把需要分析的字段拖动到右侧，点击运行查
询。

789

与	BI	工具连接

运行查询

得到查询结果，如图所示

运行查询

保存，即发布至	BO	Server。

替换数据源的方法

790

与	BI	工具连接

方法一	在报表内修改

首先创建	Kyligence	Enterprise	的	universe，然后在报表设计页面点击数据访问-更改源

选择其他	universe

设置字段映射，完毕后点击完成

791

与	BI	工具连接

792

与	BI	工具连接

在查询界面点击运行查询即可还原报表

方法二	在	universe	上修改

在	universe	里编辑	Connection

793

与	BI	工具连接

修改	DSN	为需要的	DSN，然后保存即可。

FAQ

Q:	BO	发出的查询都会带上	schema,包括	default	database，而	default	在	Kyligence	Enterprise	查询中是一个关键字不能
使用	default.table	的形式的查询语句。	解决方法：在kylin.properties中把	 	kylin.query.escape-default-keyword	设为
true，Kyligence	Enterprise	会自动为	default	转为"DEFAULT"。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:01

794

与	BI	工具连接

与	SAP	BusinessOjects	Server	集成

本章节以	Suse	12	SAP	BO	Server	4.2	为例，介绍如何与	SAP	BO	Server	集成。

Server	配置操作

安装	Unix	ODBC	Manager

sudo	-i	yast

转至	Software	Management。在搜索框，输入	unixodbc，Enter	确认。

安装	Unix	ODBC	Manager

选择	64-bit	位	安装包，按	Tab+Enter	打开操作菜单，选择	Install	+，Enter	确认。

安装完成后，按	F10	完成退出，然后按	F9	退出以退出	YaST。

使用命令	 	odbcinst		验证	Unix	ODBC	Manager	安装是否成功。如出现如下信息，证明安装成功。

795

与	BI	工具连接

安装成功信息

使用命令	 	odbcinst	-j		确认	Unix	ODBC	Manager	版本。

Unix	ODBC	Manager	版本

注意：不同版本的	unix	odbc	manager，BO	Server	odbc.sbo	配置不同

安装	Kyligence	ODBC	Driver

Download	下载安装包，拷贝至	BO	Server	指定目录，解压

tar	-zxvf	Kyligence.ODBC.{version}.tar.gz

如，拷贝至	{BO	安装目录}/sap_bobj/enterprise_xi40/linux_x64/odbc/KyligenceODBC

确认	libodbc	路径，设置	libodbc.so.1	软链

796

与	BI	工具连接

libodbc	是	Suse	环境	BO	Server	安装的前置条件，无须再次安装

cd	/usr/lib64

ll	libodbc*

确认	libodbc.so	存在，设置	libodbc.so.1	软链。

ln	-s	/usr/lib64/libodbc.so	libodbc.so.1

使用命令	 	ll	libodbc*		确认软链是否正确。

验证软链接

配置环境变量

1）修改	/etc/profile

vi	/etc/profile

新增变量	ODBCINI	指向	DSN	路径	，LD_LIBRARY_PATH	指向	libodbc	和	Kyligence	ODBC	lib

export	ODBCINI=/home/boadmin/BOServer/install_dir/sap_bobj/enterprise_xi40/odbc.ini

export	LD_LIBRARY_PATH=/usr/lib64:/home/boadmin/BOServer/install_dir/sap_bobj/enterprise_xi40/linux_x64/odbc/Ky

ligenceODBC

source	/etc/profile

2）修改	env.sh

vi	{BO	安装目录}/sap_bobj/setup/env.sh

找到	LIBRARYPATH，新增	libodbc	和	Kyligence	ODBC	lib	路径

:/usr/lib64:${BOBJEDIR}enterprise_xi40/linux_x64/odbc/KyligenceODBC

新建	DSN

编辑	ODBCINI	路径的	odbc.ini	文件，新增	Kyligence	Enterprise	DSN

cd	{BO	安装目录}/sap_bobj/enterprise_xi40

vi	odbc.ini

797

与	BI	工具连接

新增	DSN	KyligenceDataSource

注意	：DSN	名称必须与客户端自建的	DSN	一致。

[KyligenceDataSource]

SERVER=10.1.2.43

PORT	=	7070

PROJECT	=	learn_kylin

Driver=/home/boadmin/BOServer/install_dir/sap_bobj/enterprise_xi40/linux_x64/odbc/KyligenceODBC/libKyligenceODB

C64.so

ISQL	验证	DSN

isql	KyligenceDataSource	ADMIN	'KYLIN'

select	*	from	KYLIN_SALES	limit	1;

SQL	结果正常返回，即验证	DSN	有效。

配置	BO	Server	odbc.sbo

进入	odbc.sbo	所在路径，odbc.sbo	相关介绍，请参考	SAP	手册。

cd	{BO	安装目录}/sap_bobj/enterprise_xi40/dataAccess/connectionServer/odbc

vi	odbc.sbo

参考	odbc.sbo	备注信息，基于安装的	ODBC	Manager	版本，修改	odbc.sbo	文件，保存。

比如，当	Unix	ODBC	Manager	版本为	2.3.6，需要修改	odbc.sbo	中的	参数值，并注释掉	Table	parameter。

重启	BO	Server

cd	{BO	安装目录}/sap_bobj

./stopservers

./startservers

创建并发布报表

使用	Universe	+	Web	Intelligence	胖客户端创建，并发布报表，可参考手册	与	SAP	BusinessOjects	Web	Intelligence	集成。

Server	查看报表

浏览器进入	CMC	Server	http://ip:port/BOE/CMC，进入报表发布目录，选择报表，右键**查看**。

798

与	BI	工具连接

查看报表

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:01

799

与	BI	工具连接

与	SmartBI	Insight	集成

SmartBI	Insight	是企业级的商业智能分析平台，定位于前端数据分析，对接各种数据库、数据仓库和大数据平台，构建
交互式仪表盘，满足多样性的数据分析应用需求，如大数据分析、企业报表平台、自主探索分析等。本文将分步介绍

SmartBI	Insight	与	Kyligence	Enterprise	的连接。

安装	SmartBI	Insight

有关	SmartBI	Insight	的安装说明，请访问	SmartBI	Insight	下载页面。

支持的	SmartBI	版本

SmartBI	8.5	及以上版本，验证过的版本为	8.5，9.3	和	10.5。您可以查看：

与	SmartBI	8.5	集成
与	SmartBI	10.5	集成

与	SmartBI	8.5	集成

安装	Kyligence	JDBC	驱动程序

SmartBI	Insight	通过	JDBC	连接	Kyligence	Enterprise，所以首先需要在	SmartBI	Insight	上安装	Kyligence	JDBC	驱动程
序，获取	Kyligence	JDBC	驱动程序：请参考	Kyligence	JDBC	驱动程序说明。

向	SmartBI	Insight	增加	JDBC	驱动程序：

删除	SmartBI	自带的	Apache	Kylin	JDBC	驱动程序，通常放置在以下路径：

[SmartBI_Insight安装路径]\Tomcat\webapps\smartbi\WEB-INF\lib

确认	SmartBI	的动态目录

进入	SmartBI	的配置界面，URL	为	 	http://server:port/smartbi/vision/config.jsp	（根据实际情况修改server和port），
将界面滚动到底部，找到动态驱动存放路径一项

找到	SmartBI	的动态驱动路径

800

与	BI	工具连接

下载	Kyligence	的	JDBC	驱动程序并放到	SmartBI	的动态驱动路径下,	默认安装路径为：

[SmartBI_Insight	安装路径]\Tomcat\bin\dynamicLibraryPath\KYLIN

直接将文件添加到上述步骤中配置的存放路径即可，无需重启服务。系统每隔10秒会自动监听该目录里	jar	文件
的变化。

建立	Kyligence	Enterprise	数据源连接

1.	新建数据源

在	定制管理->数据管理->数据源	节点下右键选择新建关系数据源，或是在定制管理快捷按钮选择	数据源连接，则打开
数据源连接窗口。

名称：输入任意名称

别名：输入任意别名

驱动程序类型：Kylin

驱动程序类： 	org.apache.kylin.jdbc.Driver

连接字符串： 	jdbc:kylin://<servername>:<port>/<projectName>

验证类型:	根据需要选择静态或动态，如直接输入单一验证账户，则选择静态。

用户名:	输入连接的	Kyligence	环境的用户名

密码:	输入连接的	Kyligence	环境的密码

数据库源字符集:	留空

数据库目标字符集:	留空

最大连接数:不修改，默认值	100

引用标识符:查询中的转义符号，请使用英文的双引号

801

与	BI	工具连接

创建数据源

点击测试连接，显示连接通过，然后点击保存数据源。

2.	管理数据源

点击保存后，您将在	定制管理->数据管理->数据源下看到您此前建立的	Kyligence	数据源。

右键点击数据源名称，点击管理数据库，即可进入管理页面

数据库管理

802

与	BI	工具连接

对数据源进行管理，将表结构信息（表名、字段名、字段类型等）添加到	SmartBI	Insight	中。

导入数据源表

对于需要在模型上重复使用的表需要复制表，并修改表的别名。

点击您创建的数据源，右键点击需要重复使用的表，点击复制表。

管理数据源1

803

与	BI	工具连接

右键点击需要表名，点击属性，修改表的别名。在本例中，我们将需要重复使用的表	KYLIN_ACCOUNT分别修改别名
为BUYER_ACCOUNT和SELLER_ACCOUNT

修改表别名

右键点击您创建的数据源下的表关系视图，点击其中的新建->表关系视图，即可进入关系图页面

804

与	BI	工具连接

表关系视图

输入名称、别名、描述。

拖拽左侧的表到画布中，进行建模，对于星型模型的多表关联，会按照按外键、列名等方式自动创建表之间的关联关

系，也可以手动拖拽建立关联关系。

数据建模

注：在	SmartBI	中定义的模型需要与	Kyligence	Enterprise	中定义的模型的关联关系相匹配

805

与	BI	工具连接

对于需要多列关联的表，可点击关联模型的线，修改关联表达式

数据建模

创建业务视图

右键点击数据库->数据库名->业务视图->可视化查询，即可进入新增业务视图的界面。

新建业务视图

806

与	BI	工具连接

将字段拖入后，创建业务视图。

创建业务视图

注意：对于在	Kyligence	的模型上定义了聚合的度量请双击字段，并定义字段的聚合方式。

如	Kylin_sales_cube	上度量	GMV	定义为	sum(price)，则在业务视图中需要将	PRICE	字段的聚合方式定义为合计。

定义业务视图

807

与	BI	工具连接

透视分析

点击定制管理->透视分析，即可进入透视分析页面。

创建透视分析

在选择业务查询页面，选择数据源中的表选项卡，并找到之前创建的业务视图。

808

与	BI	工具连接

选择业务视图

拖拽字段到行列区和过滤区，点击刷新，进行自助式探索分析。

809

与	BI	工具连接

创建透视分析

根据分析需要，生成各种分析图表。

创建图表分析

810

与	BI	工具连接

注意：若想使用多维模式连接	Kyligence	产品，需要使用	Kyligence	MDX	。更多信息请看	Kyligence	MDX	对接
SmartBI	操作手册。

自助仪表盘

1.	创建业务主题

使用自助仪表盘功能需要先创建业务主题，在菜单中选择定置管理>业务主题。

创建业务主题

在数据源中选择创建好的	Kyligence	数据源，如果您好没有创建	Kyligence	数据源	请参考	建立	Kyligence	Enterprise	数据
源连接	部分文档创建数据源。

811

与	BI	工具连接

创建业务主题

使用数据源中的需要使用的表拖拽到左侧栏位，并在表关系视图定义表之间的关联。

812

与	BI	工具连接

创建业务主题

如果您需要对数据进行过滤，您可以右键过滤器，选择新建过滤器

创建业务主题

在过滤器中定义过滤器的表达式。

813

与	BI	工具连接

创建业务主题

2.	创建自助仪表盘

选择定置管理>自主仪表盘

814

与	BI	工具连接

创建业务主题

在左侧数据栏位下拉选择刚才创建的业务主题

815

与	BI	工具连接

创建业务主题

816

与	BI	工具连接

即可进行拖拽可视化分析。

创建业务主题

与	SmartBI	10.5	集成

创建数据源连接

步骤一：添加数据源驱动

向	SmartBI	Insight	增加	JDBC	驱动程序，具体步骤如下：

1.	 确认	SmartBI	的动态目录

进入	SmartBI	的配置界面，URL为	http://server:port/smartbi/vision/config.jsp（根据实际情况修改	 	server		和
	port	），将界面滚动到底部，找到“业务库驱动类存放路径”一项。

817

与	BI	工具连接

业务库驱动泪存放路径

默认情况下，这个路径应该是：

{SmartBI_HOME}\Tomcat\bin\dynamicLibraryPath\

2.	 添加数据源驱动

在	SmartBI	的动态驱动目录下，创建	Kylin	目录，并放入	Kyligence	JDBC	驱动。放置完成后，无需重启服务。系统
每隔	10	秒会自动监听该目录里	jar	文件的变化，之后您可以在新建数据源里的	驱动程序存放目录-自定义	中能看到
创建的驱动目录，即说明驱动已被扫到。

查看驱动程序

818

与	BI	工具连接

3.	 添加数据源驱动到	OLAP

如果要使用	Kyligence	数据源创建多维模型，还需要将	Kyligence	JDBC	驱动放置在
	{SmartBI_HOME}\smartbiOLAP\dynamicLibraryPath\Kylin		路径下。

步骤二：新建数据源连接

进入主界面，点击”数据连接“，选择”Apache	KYLIN“，修改连接字符串	jdbc:kylin://:/，替换为	Kyligence	Enterprise	的
IP、端口和项目名称，然后点击测试连接，显示连接通过，然后点击保存数据源。

新建数据源

步骤三：添加数据库资源

选择已保存的数据连接，进入数据库管理：

数据库管理

819

与	BI	工具连接

对数据源进行管理，将需要分析的表，添加到	SmartBI	中，点击保存：

添加数据源表

提示：从	4.6.18.0	版本之后，SmartBI	同步	Kyligence	数据源时，支持添加表时使用以下注释作为别名：

同步原始表至	SmartBI：

数据源表中列的注释，会作为列的别名，如下图中的列别名"页面ID"、"页面名称"、"页面URL"。
数据源表中表的注释，会作为表的别名，如下图的中的表别名	"页面浏览表"。

同步模型视图至	SmartBI：

模型视图的描述信息，会作为表的别名，如下图中名为	 	model_view		的模型，其描述信息"这是个描
述"，已经作为表别名同步至	SmartBI。

820

与	BI	工具连接

模型视图的维度和度量相对应的源表中的列的注释，会作为列的别名，如下图中名为	 	model_view		的模
型，有两个维度	 	AGE	和	 	ID	，这两个维度对应的列来自	Hive	源表	 	TEST_VIEW	，可以看到源表中列的注
释"员工id"和"nianlin"已经作为维度列的别名同步至	SmartBI。如果添加可计算列为维度，暂不支持同步
可计算列的注释。

数据准备

在同步数据库资源后，已经可以基于同步到的表进行简单的分析，但多数的分析场景中都需要结合多表数据进行。

SmartBI	中提供了较为丰富的数据视图/模型能力，结合	Kyligence	Enterprise	的产品特性，可总结为以下数据准备方式：

方式1：表关系视图+可视化数据集

定义全局性的表关联关系，这种关联关系在选择当前数据源构建可视化数据集、或是业务主题时会被自动引用。

1.	 创建表关系视图

展开数据连接，点击表关系视图	，点击新建	>	表关系视图	，即可进入关系图页面

821

与	BI	工具连接

新建表关系视图

输入名称、别名、描述后，进入表关系设置页面。拖拽左侧的表到画布中，进行建模，对于需要多列关联的表，可

点击关联模型的线，修改关联表达式

设置表关系视图

最后定义好数据模型，并点击保存。

注意：

在	SmartBI	中定义的模型需要与	Kyligence	Enterprise	中定义的模型的关联关系相匹配；

822

与	BI	工具连接

对于需要在模型上重复使用的表需要复制表，并修改表的别名。您可以在数据连接中点击需要重复使用

的表右侧，然后点击复制表，然后再点击复制的表的右侧，点击属性，修改表的别名。

2.	 创建可视化数据集

您可通过以下方式创建可视化数据集，或查看可视化数据集了解更多

在系统导航栏中选择	数据准备	，在数据集的更多中选择	新建	>	可视化数据集	。
在数据准备中选择一个业务主题，在业务主题右键更多中选择	新建	>	可视化数据集	。

将字段拖入后，创建业务视图，对于在	Kyligence	Enterprise	中定义为度量的字段请双击字段，并定义字段的聚合方
式。如	Kylin_sales_cube	上度量	GMV	定义为	sum(price)，则在业务视图中需要将	PRICE	字段的聚合方式定义为合
计。设置完毕后点击保存。

创建可视化数据集

方式2：Kyligence	模型视图

1.	 在	Kyligence	Enterprise	中开启模型视图功能，可以查看	通过模型视图简化查询。

2.	 在	SmartBI	的数据库资源添加页面，选择项目名相同的	Schema，即可看到	V	标志的模型视图

提示：对于在	Kyligence	Enterprise	中被定义为维度的列，连接模型视图后展示的列名会是维度名称，而度量
名称不会同步至	SmartBI。

823

与	BI	工具连接

连接模型视图

3.	 基于模型视图进行可视化与分析。

通过模型视图分析

方式3：数据模型

这是	SmartBI	v10	版本新增的方式，本质上是基于	Mondrian	实现了一套多维语义层，类似于	Kyligence	Enterprise	+
Kyligence	MDX，您可以查看数据模型了解更多，使用方式如下：

1.	 进入数据准备	-	数据集	-	新建	-	数据模型

824

与	BI	工具连接

新建数据模型

2.	 点击左上角	+	，选择数据源表并添加。右上角可选择数据源类型为“直连”或“抽取”，对于	Kyligence	数据源，推荐

数据源类型为直连。

选择数据源表

3.	 连线定义表关系，注意要从事实表向维表连线

825

与	BI	工具连接

定义表关系

4.	 接下来您可以根据需求对维度重命名，可以创建层次结构，可以创建计算度量，您可以查看	SmartBI	手册了解详细

的使用方式。

重命名维度

重命名维度

创建层次结构，创建后可将相应字段拖入层次结构中

826

与	BI	工具连接

提示：SmartBI	交互式仪表盘中支持下钻操作，默认情况支持的下钻方式包括时间层次下钻、地理层次下
钻、自定义层次维下钻。而基于数据模型的自助仪表盘中的图表，可按数据模型中定义的层次结构展现下钻

效果。

创建层次结构

创建层次结构

创建计算度量

827

与	BI	工具连接

创建计算度量

5.	 完成设置后保存数据模型

保存数据模型

方式4：SQL	数据集

SQL	数据集是通过在文本区中输入	SQL	语句，来定义数据集条件和内容的一种数据集。这种方式对于熟悉	SQL	语句的
技术人员来说较为快捷创建，也是多数	BI	工具支持、多数	BI	用户重度使用的方式。SQL	数据集中除了写	SQL，还可
以使用“参数”、“用户属性”、“系统函数”等系统资源。相关使用方式及示例，可参考SQL数据集。

828

与	BI	工具连接

进行可视化与分析

SmartBI	提供了多种分析类型，其中常用是交互式仪表盘（自助仪表盘）和透视分析。使用	SmartBI	10.5	进行可视化分
析的入口与之前版本稍有不同，但方式是一样的，您可以查看上文与	SmartBI	8.5	集成部分了解具体方法或查看	SmartBI
手册了解更多。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:01

829

与	BI	工具连接

与	FineBI	集成

帆软是国内最大、实力最强的	Web	报表工具、商业智能等数据类产品研发的公司。旗下产品	FineBI	是新型商业智能软
件优秀代表。帆软产品被成功实施于上万个信息化应用项目，客户遍及各行各业，每天有超过50万人通过帆软的产品来
查阅、填报、分析数据。Kyligence	Enterprise	支持与	FineBI	4.1，5.1	产品集成，本文将分步介绍集成操作。

安装	FineBI

有关	FineBI	的安装说明，请访问	FineBI	下载页面,	推荐使用	Fine	BI	5.1.10	及以上的直连版本。

注意：现仅支持	Windows，Linux	版	FineBI

安装	Kyligence	JDBC	驱动程序

FineBI	通过JDBC连接	Kyligence	Enterprise，所以首先需要在FineBI	上安装	Kyligence	JDBC	驱动程序。

1.	 获取	Kyligence	JDBC	驱动程序

请参考	Kyligence	JDBC	驱动程序说明。

2.	 向	FineBI	增加	JDBC	驱动程序

​	Windows	版：拷贝	JDBC	驱动程序到	安装路径\webapps\webroot\WEB-INF\lib

​	Linux	版：拷贝	JDBC	驱动程序到	安装路径\webapps\webroot\WEB-INF\lib

建立	Kyligence	Enterprise	数据源连接

1.	 新建数据源

在主页面选择管理系统->数据连接。

新建数据连接

点击新建数据连接，选择	APACHE	KYLIN。

830

与	BI	工具连接

新建数据源

2.	 保存数据源

将服务器	IP	地址等信息填写到连接字符串，字符串格式为：

jdbc:kylin://<hostname>:<port>/<project_name>

然后填写用户名和密码。

编辑连接信息

注意：由于	FineBI	若开启获取连接前校验的选项会不使用数据库名发送侦测查询，且该配置从5.1开始默认开启，
所以在测试连接前请确认关闭了该选项。

831

与	BI	工具连接

关闭获取连接前校验

然后点击测试连接，测试成功后点击确定保存数据源连接。

保存数据源

新建业务包

1.	 在主页面选择数据准备->添加业务包，新建一个业务包。

832

与	BI	工具连接

新建业务包

2.	 点击新增的业务包，进入业务包编辑页面。

进入业务包

3.	 点击添加表->数据库表。

833

与	BI	工具连接

业务包添加表

4.	 点击需要加入数据库的表，点击确定，将需要的表添加到业务包中。

选择表

5.	 为了将查询推送到	Kyligence	Enterprise	中，选择实时数据

834

与	BI	工具连接

选择实时数据

6.	 点击管理视图，可以定义表间关联。

定义关联视图

添加自助数据集

1.	 点击创建->添加自助数据集，并且选择位置为您刚才新建的业务包

添加自助数据集

2.	 从各张表中选择需要的列，点击保存

835

与	BI	工具连接

保存自助数据集

在仪表盘中使用数据

1.	 在主页面选择创建->新建仪表板，新建一个仪表板。

新建仪表板

2.	 点击添加组件->选择创建的业务包->选择数据集或者表，即可开始分析。

836

与	BI	工具连接

新建仪表板

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:01

837

与	BI	工具连接

与帆软集成

帆软是国内最大、实力最强的	Web	报表工具、商业智能等数据类产品研发的公司。旗下产品	FineReport	是中国报表软
件著名品牌。帆软产品被成功实施于上万个信息化应用项目，客户遍及各行各业，每天有超过50万人通过帆软的产品来
查阅、填报、分析数据。近日，Kyligence	已认证帆软旗下FineReport（9.0版本）产品。本文将分别介绍Kyligence
Enterprise与	FineReport	的集成。

安装	FineReport

有关	FineReport	的安装说明，请访问	FineReport	下载页面。

安装	Kyligence	JDBC	驱动程序

FineReport	通过JDBC连接	Kyligence	Enterprise，所以首先需要在FineReport	上安装	Kyligence	JDBC	驱动程序。

1.	 获取	Kyligence	JDBC	驱动程序

请参考	Kyligence	JDBC	驱动程序说明。

2.	 向	FineReport	增加	JDBC	驱动程序

拷贝JDBC驱动程序到安装路径\webapps\webroot\WEB-INF\lib路径下,然后重启设计器。

建立	Kyligence	Enterprise	数据源连接

1.	 在主页面选择服务器->定义数据连接，

新建数据连接

2.	 选择新建	JDBC	数据源

838

与	BI	工具连接

新建数据源

3.	 选择数据库类型为	Others	,驱动器填写：org.apache.kylin.jdbc.Driver，URL填写： 	jdbc:kylin://<hostname>:

<port>/<project_name>	，填写用户名、密码，然后点击测试连接，连接成功后点击确定保存。

839

与	BI	工具连接

新建数据源

建立	Kyligence	Enterprise	数据集

1.	 在主页面选择服务器->服务器数据集

新建数据源

2.	 选择新建数据库查询

840

与	BI	工具连接

新建数据源

3.	 数据源选择Kyligence	Enterprise的数据源

选择数据源

841

与	BI	工具连接

4.	 然后将编辑查询语句，由于	FineReport	在发送查询时并不会自动补全数据库名，所以您的查询中必须包含数据库

名。如下图所示。

合格的查询

5.	 若您出现如下报错，就是因为没有书写数据库名所致

报错

制作报表

1.	 在主页面选择文件->新建聚合报表

842

与	BI	工具连接

新建数据源

2.	 从服务器数据集中，选择Kyligence	Enterprise的数据集，编辑报表，自由使用Kyligence	Enterprise中的数据。

新建数据源

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:01

843

与	BI	工具连接

与永洪	Yonghong	BI	集成

Yonghong	BI	为用户提供了一站式的大数据分析平台。本文将分步介绍如何使用	Kyligence	Enterprise	与	Yonghong	BI	集
成。

前置条件

安装	Yonghong	BI	Z-Suite。有关安装信息，请参考	Yonghong	帮助中心。

安装	Kyligence	JDBC	驱动程序

1.	 获取	Kyligence	JDBC	驱动程序。有关信息，请参考	Kyligence	JDBC	驱动程序教程。

2.	 向	Yonghong	BI	添加	JDBC	驱动程序。拷贝	JDBC	驱动程序至安装路径，如	 	{Yonghong	安装目录}/jdbcDriver/

。

提示：由于	Yonghong	BI	内置了	Apache	Kylin	的	JDBC	驱动，防止驱动冲突，建议将其移除后再添加
Kyligence	Enterprise	JDBC	驱动。

新建	Kyligence	Enterprise	数据源

在首页选择添加数据源，点击进入	-	选择	Kylin：

844

与	BI	工具连接

输入连接属性等连接信息后，点击测试连接，成功后请点击保存：

845

与	BI	工具连接

新建数据集

在首页选择创建数据集模块，点击进入-选择	SQL	数据集：

846

与	BI	工具连接

选择已经创建好的Kyligence	Enterprise数据源，输入自定义SQL语句，点击刷新元数据后进行保存；

提示：当使用	 	select	*	from	table	、 	select	*	from	facttable	inner	join	dimtable		这种	SQL	语句刷新元数据
的时候，Kyligence	Enterprise	有可能使用查询下压来回答，当数据源中数据量特别大时，返回查询结果和更新元
数据的速度可能较慢。	此时建议在	 	$KYLIN_HOME/conf/kylin.properties		中开启配置项	 	kylin.query.return-empty-
result-on-select-star=true	，该配置项可以针对此	 	select	*		的	SQL	直接返回查询结果为空的表元数据，从而
加快更新刷新元数据的速度。

847

与	BI	工具连接

848

与	BI	工具连接

制作报告

在首页选择制作报告，点击进入，选择主题，新建报告：

849

与	BI	工具连接

数据集处选择保存好的查询，拖拽字段即可设计报告：

报告创建完成后，请点击预览报告。至此，你将可以在	Yonghong	BI	中查看	Kyligence	Enterprise	数据。

850

与	BI	工具连接

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:01

851

与	Excel	集成

与	Excel	集成

如需使用	Excel	分析	Kyligence	Enterprise	中的数据，需要安装	Kyligence	MDX	。Kyligence	MDX	提供了强大的语义层功
能和	MDX	查询接口，可以对接	Excel	数据透视表功能。您还可以基于	Kyligence	MDX	支持多事实表模型，定义层级结
构，定义计算度量和多对多关系等场景。详见	Kyligence	MDX	手册。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:01

852

与	Python	集成

与	Python	集成

您可以使用	kylinpy	组件实现本产品与	Python	集成。Kylinpy	提供了	SQLAlchemy	Dialect	实现，可以帮助您通过	pandas
访问	Kyligence	Enterprise	中的数据，满足数据统计、机器学习等分析需求。

前置条件

1.	 Python	2.7+	或者	Python	3.5+
2.	 已经安装	pip	包管理软件
3.	 已经通过	pip	安装	SQLAlchemy
4.	 已经通过	pip	安装	Pandas	(可选)

如何获取	kylinpy

pip	install	--upgrade	kylinpy

如果需要离线安装	kylinpy	,	可以通过如下网址下载压缩包后安装	https://pypi.org/project/kylinpy/#files

pip	install	kylinpy-<version>.tar.gz

配置连接字符串和连接选项

配置连接字符串

kylinpy	实现了	SQLAlchemy	接口，您可以通过如下	SQLAlchemy	URI	模板创建连接字符串：

kylin://<username>:<password>@<hostname>:<port>/<project>

配置项说明如下：

配置项

配置说明

默认值

备注

username

Kyligence	Enterprise	帐名

不区分大小写

password

Kyligence	Enterprise	密码

hostname

Kyligence	Enterprise	主机名或者	IP	地址

无需附加	 	http		或者	 	https		协议前缀

port

Kyligence	Enterprise	主机端口

	7070

project

Kyligence	Enterprise	项目名称

不区分大小写

配置连接选项

SQLAlchemy	的	create_engine	方法还可以接收一个	connect_args	参数作为连接选项。

配置项说明如下：

配置项

配置说明

默认值

可选值

备注

is_ssl

是否通过	ssl	连接

	0

	0	或 	1

连接	Kyligence	Enterprise
的 	https	端口时，需要设置
为 	1

prefix

api	前缀

	kylin/api

访问	Kyligence	Enterprise	实例

853

与	Python	集成

timeout

访问	Kyligence	Enterprise	实例
超时时间，单位:	秒

version

使用	api	版本

is_pushdown

Kyligence	Enterprise	实例是否
开启	pushdown	选项

is_debug

是否启用	debug	模式

	30

	v1

	0

	0

连接示例

	v1	、 	v2
和	 	v3

请设置为	 	v4

如果设为	 	1		可以查询到未经
构建的原表

	0	或 	1

	0	或 	1

假设您已经建立了名称为	 	learn_kylin		的项目，且已经导入了样例数据集	SSB	中的所有源表，则如下为通过
SQLAlchemy	访问	Kyligence	Enterprise	中的数据：

$	python

>>>	import	sqlalchemy	as	sa

>>>	kylin_engine	=	sa.create_engine('kylin://ADMIN:KYLIN@sandbox/learn_kylin?timeout=60&is_debug=1&version=v4')

>>>	results	=	kylin_engine.execute('SELECT	count(*)	FROM	KYLIN_SALES')

>>>	[e	for	e	in	results]

[(4953,)]

>>>	kylin_engine.table_names()

[u'KYLIN_ACCOUNT',

	u'KYLIN_CAL_DT',

	u'KYLIN_CATEGORY_GROUPINGS',

	u'KYLIN_COUNTRY',

	u'KYLIN_SALES',

	u'KYLIN_STREAMING_TABLE']

通过	Pandas	访问

$	python

	>>>	import	sqlalchemy	as	sa

	>>>	import	pandas	as	pd

	>>>	kylin_engine	=	sa.create_engine('kylin://ADMIN:KYLIN@sandbox/learn_kylin?timeout=60&is_debug=1&version=v4'

)

	>>>	sql	=	'select	*	from	kylin_sales	limit	10'

	>>>	pd.read_sql(sql,	kylin_engine)

通过	Apache	Superset	访问

现在，您可以在	Apache	Superset	中配置	DSN	以建立与	Kyligence	Enterprise	的连接。

例如，您可以在	Apache	Superset	环境中安装	kylinpy，并在	Apache	Superset	中配置与	Kyligence	Enterprise	的连接。

854

与	Python	集成

配置	DSN

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

855

开发者指南

开发者文档

Kyligence	为您提供了所需的各种开发文档，帮助您更好地使用与集成	Kyligence	Enterprise	产品功能。开发者文档将为
您提供开发教程，样例代码以及	Rest	API	等。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

856

REST	API	v4

REST	API	v4

Kyligence	Enterprise	REST	API	v4	主要用于	Kyligence	Enterprise	4。目前提供了SQL查询、触发构建任务等全面的	REST
API。基于这些	API，可以更好地帮助	Kyligence	Enterprise	与您的日常使用紧密集成。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

857

访问与安全认证	API

访问与安全认证	API

访问

Kyligence	Enterprise	API	的访问前缀为	 	/kylin/api/	，不管对哪个模块的	API	访问都需要加上该前缀，比如访问所有模
型的	API	为	 	/kylin/api/models	，对应的完整路径为	 	http://host:port/kylin/api/models	。

认证

Kyligence	Enterprise	所有的	API	都是基于	Basic	Authentication	认证机制。Basic	Authentication	是一种简单的访问控制机
制，将帐号密码基于	Base64	编码后作为请求头添加到	HTTP	请求头中，后端会读取请求头中的帐号密码信息进行认
证。以账号密码	 	ADMIN:KYLIN		为例，对应帐号密码编码后结果为	 	'Basic	QURNSU46S1lMSU4='	，那么	HTTP	对应的头信
息为	 	'Authorization:	Basic	QURNSU46S1lMSU4='	。

认证要点

在	HTTP	头添加	 	Authorization		信息

或者可以通过	 	POST	http://host:port/kylin/api/user/authentication		进行认证，一旦认证通过，接下来对	API
请求基于	cookies	在	HTTP	头中免去	 	Authorization	信息

HTTP	Header

	Authorization:Basic	QURNSU46S1lMSU4=

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	POST	\

		'http://host:port/kylin/api/user/authentication'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

		{

						"code":"000",

						"data":{

										"username":"ADMIN",

										"authorities":[{"authority":	"ROLE_ADMIN"},	{"authority":	"ALL_USERS"}],

										"disabled":false,

										"locked":false,

										"uuid":"0205dac6-215a-4454-84ae-3dcc85b9675c",

										"last_modified":1574756819619,

										"create_time":1563346648008,

										"version":"4.0.0.0",

										"mvcc":24,

										"locked_time":0,

										"wrong_time":2,

										"first_login_failed_time":1574756817981

						},

						"msg":""

		}

858

访问与安全认证	API

JavaScript	认证请求示例

提示：您可以通过如下路径下载	"jquery.base64.js"	https://github.com/yckart/jquery.base64.js

var	authorizationCode	=	$.base64('encode',	'NT_USERNAME'	+	":"	+	'NT_PASSWORD');

$.ajaxSetup({

			headers:	{

				'Authorization':	"Basic	"	+	authorizationCode,

				'Content-Type':	'application/json;charset=utf-8',

				'Accept':	'application/vnd.apache.kylin-v4-public+json'

			}

});

$.ajaxSetup({

						headers:	{

								'Authorization':	'Basic	eWFu**********X***ZA==',

								'Content-Type':	'application/json;charset=utf-8',

								'Accept':	'application/vnd.apache.kylin-v4-public+json'

						}	//	use	your	own	authorization	code	here

				});

				var	request	=	$.ajax({

							url:	"http://host:port/kylin/api/query",

							type:	"POST",

							data:	'{"sql":"select	count(*)	from	SUMMARY;","offset":0,"limit":50000,"acceptPartial":true,"project":"t

est"}',

							dataType:	"json"

				});

				request.done(function(	msg	)	{

							alert(msg);

				});

				request.fail(function(	jqXHR,	textStatus	)	{

							alert(	"Request	failed:	"	+	textStatus	);

		});

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

859

项目设置	API

项目设置	API

提示：

1.	 请确保已阅读前面的访问及安全认证章节，了解如何在	REST	API	语句中添加认证信息。

2.	 在	Curl	命令行上，如果您访问的	URL	中含有	 	&		符号，请注意转义，比如在	URL	两端加上引号。

创建项目

	POST	http://host:port/kylin/api/projects

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

HTTP	Body:	JSON	Object

	name		-	 	必选		 	string	，项目名称。
	description		-	 	可选		 	string	，项目描述。
	maintain_model_type		-	 	必选		 	string	， 	MANUAL_MAINTAIN	表示	AI	增强模式。

Curl	请求示例

curl	-X	POST	\

'http://host:port/kylin/api/projects'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	cn'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'	\

-d	'{

		"name":	"a",

		"description":	"",

		"maintain_model_type":	"MANUAL_MAINTAIN"

}'

响应示例

{

				"code":"000",

				"data":{

								"uuid":"c7713bea-7df5-49d5-9713-f0094addbafe",

								"last_modified":1574389912687,

								"create_time":1574389912687,

								"version":"4.0.0.0",

								"mvcc":0,

								"name":"a",

								"owner":"ADMIN",

								"status":"ENABLED",

								"create_time_utc":1574389912687,

								"default_database":"DEFAULT",

								"description":"",

								"ext_filters":[

								],

								"maintain_model_type":"AUTO_MAINTAIN",

								"override_kylin_properties":{

								},

860

项目设置	API

								"segment_config":{

												"auto_merge_enabled":true,

												"auto_merge_time_ranges":[

																"WEEK",

																"MONTH",

																"QUARTER",

																"YEAR"

												],

												"volatile_range":{

																"volatile_range_number":0,

																"volatile_range_enabled":false,

																"volatile_range_type":"DAY"

												},

												"retention_range":{

																"retention_range_number":1,

																"retention_range_enabled":false,

																"retention_range_type":"MONTH"

												}

								}

				},

				"msg":""

}

删除项目

	DELETE	http://host:port/kylin/api/projects/{project}

URL	Parameters

	project		-	 	必选		 	string	，项目名称。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	DELETE	\

'http://host:port/kylin/api/projects/b'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	cn'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":"000",

				"data":null,

				"msg":""

}

通用设置

	PUT	http://host:port/kylin/api/projects/{project}/project_general_info

URL	Parameters

	project		-	 	必选		 	string	，项目名称。

HTTP	Header

861

项目设置	API

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

HTTP	Body:	JSON	Object

	description		-	 	可选		 	string	，项目描述。
	semi_automatic_mode		-	 	可选		 	boolean	，是否开启智能推荐模式， 	true		表示开启， 	false		表示关闭，默认
为	 	false	。

Curl	请求示例

curl	-X	PUT	\

'http://host:port/kylin/api/projects/b/project_general_info'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	cn'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'	\

-d	'{

				"description":"description",

				"semi_automatic_mode":true

}'

响应示例

{

				"code":"000",

				"data":null,

				"msg":""

}

存储配额

	PUT	http://host:port/kylin/api/projects/{project}/storage_quota

URL	Parameters

	project		-	 	必选		 	string	，项目名称。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

HTTP	Body:	JSON	Object

	storage_quota_size		-	 	必选		 	long	，项目存储配额，单位是 	byte	，可选值：正数且大于等于	 	1099511627776
，即大于等于	1	TB。

Curl	请求示例

curl	-X	PUT	\

'http://host:port/kylin/api/projects/b/storage_quota'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	cn'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'	\

-d	'{

				"storage_quota_size":	1099511627776

}'

响应示例

862

项目设置	API

{

				"code":"000",

				"data":true,

				"msg":""

}

低效存储

	PUT	http://host:port/kylin/api/projects/{project}/garbage_cleanup_config

URL	Parameters

	project		-	 	必选		 	string	，项目名称。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

HTTP	Body:	JSON	Object

	frequency_time_window		-	 	必选		 	string	，低效存储计算周期，可选值： 	MONTH	,	 	WEEK	,	 	DAY	。
	low_frequency_threshold		-	 	必选		 	int	，低效存储使用次数，可选值：正整数和	 	0	，如可以设置当每月使用
频率低于	10	次的加速查询和对应的存储即为低效存储。

Curl	请求示例

curl	-X	PUT	\

'http://host:port/kylin/api/projects/b/garbage_cleanup_config'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	cn'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'	\

-d	'{

				"frequency_time_window":	"WEEK",

				"low_frequency_threshold":	7

}'

响应示例

{

				"code":"000",

				"data":true,

				"msg":""

}

查询下压

	PUT	http://host:port/kylin/api/projects/{project}/push_down_config

URL	Parameters

	project		-	 	必选		 	string	，项目名称。

HTTP	Header

	Content-Type:	application/json;charset=utf-8

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

HTTP	Body:	JSON	Object

863

项目设置	API

	push_down_enabled		-	 	必选		 	boolean	，是否开启查询下压， 	true		开启， 	false		关闭。

Curl	请求示例

curl	-X	PUT	\

'http://host:port/kylin/api/projects/b/push_down_config'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	cn'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'	\

-d	'{

	"push_down_enabled":true

}'

响应示例

{

				"code":"000",

				"data":null,

				"msg":""

}

查询下压配置

	PUT	http://host:port/kylin/api/projects/{project}/push_down_project_config

URL	Parameters

	project		-	 	必选		 	string	，项目名称。

HTTP	Header

	Content-Type:	application/json;charset=utf-8

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

HTTP	Body:	JSON	Object

	runner_class_name		-	 	必选		 	string	，配置项目级别	 	kylin.query.pushdown.runner-class-name		的值。用于指定
查询下压时将查询发送到何种查询引擎。默认值为

	io.kyligence.kap.query.pushdown.PushDownRunnerSparkImpl	，即下压至原生	Spark。
	converter_class_names		-	 	必选		 	string	，配置项目级别	SQL	转换参数	 	kylin.query.pushdown.converter-class-
names		的值。

Curl	请求示例

curl	-X	PUT	\

'http://host:port/kylin/api/projects/b/push_down_project_config'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	cn'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'	\

-d	'{

	"runner_class_name":"io.kyligence.kap.query.pushdown.PushDownRunnerSparkImpl",

	"converter_class_names":"io.kyligence.kap.query.security.HackSelectStarWithColumnACL,io.kyligence.kap.quer

y.util.SparkSQLFunctionConverter"

}'

响应示例

{

				"code":"000",

				"data":null,

864

项目设置	API

				"msg":""

}

Segment	设置

	PUT	http://host:port/kylin/api/projects/{project}/segment_config

URL	Parameters

	project		-	 	必选		 	string	，项目名称。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

HTTP	Body:	JSON	Object

	auto_merge_enabled		-	 	必选		 	boolean	，是否开启	Segment	自动合并， 	true		开启， 	false		关闭。
	auto_merge_time_ranges		-	 	必选		 	array	，	Segment	自动合并的周期，也是留存阀值的单位，可选
值： 	DAY	， 	WEEK	， 	MONTH	， 	QUARTER	， 	YEAR	。如可以设置自动合并	1	周的	segments。
	volatile_range		-	 	可选		 	json	，自动合并的变动范围，表示"自动合并"将不会合并[变动范围]内的	segments。
如可以设置	10	天，表示不会自动合并	10	天内的	segments。

	volatile_range_number		-	 	可选		 	int	，变动范围的时间，默认值为	 	0	，可选值：正整数和	 	0	。
	volatile_range_type		-	 	可选		 	string	，变动范围的时间单位，默认值为	 	DAY	，可选
值： 	DAY	， 	WEEK	， 	MONTH	。

	retention_range		-	 	可选		 	json	，留存阈值，表示保留留存阈值内的	segments。如可以设置	1	年，表示超出	1
年的	segments	会被系统自动移除。

	retention_range_enabled		-	 	可选		 	boolean	，是否开启留存阀值， 	true		开启， 	false		关闭，默认值为
	false	。

	retention_range_number		-	 	可选		 	int	，留存阀值的时间，默认值为	 	1	，可选值：正整数和	 	0	。

	create_empty_segment_enabled		-	 	可选		 	boolean	，是否允许新增空的	Segment。 	true		开启， 	false		关闭，默
认值为	 	false	。

Curl	请求示例

curl	-X	PUT	\

'http://host:port/kylin/api/projects/b/segment_config'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	cn'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'	\

-d	'{

								"auto_merge_time_ranges":[

												"WEEK",

												"MONTH",

												"QUARTER",

												"DAY",

												"YEAR"

								],

								"auto_merge_enabled":true,

								"volatile_range":{

												"volatile_range_number":0,

												"volatile_range_type":"DAY"

								},

								"retention_range":{

												"retention_range_number":1,

												"retention_range_enabled":false

								}

				}'

865

项目设置	API

提示：

	auto_merge_time_ranges		数组内至少包含一个值。
	retention_range		的时间单位等于 	auto_merge_time_ranges		数组内的最大时间单位。如果
	"auto_merge_time_ranges":["DAY",MONTH"]	，那么	 	retention_range		的时间单位是	 	MONTH	。如果
	"auto_merge_time_ranges":["YEAR",WEEK"]	，那么	 	retention_range		的时间单位是	 	YEAR	。

响应示例

		{

						"code":"000",

						"data":null,

						"msg":""

		}

默认数据库

	PUT	http://host:port/kylin/api/projects/{project}/default_database

URL	Parameters

	project		-	 	必选		 	string	，项目名称。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

HTTP	Body:	JSON	Object

	default_database		-	 	必选		 	string	，默认数据库名称。

Curl	请求示例

curl	-X	PUT	\

'http://host:port/kylin/api/projects/b/default_database'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	cn'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'	\

-d	'{

								"default_database":"EDW"

				}'

响应示例

		{

						"code":"000",

						"data":"",

						"msg":""

		}

任务提醒

	PUT	http://host:port/kylin/api/projects/{project}/job_notification_config

注意：自	4.6.11.0	版本起，新增参数	 	job_states_notification	，老参数	 	job_error_notification_enabled		仍
然生效，但同时配置新老参数，将按照新参数生效。如配置	 	job_states_notification		不包含
	error	， 	job_error_notification_enabled		为	 	true		时，不会收到失败任务提醒。

URL	Parameters

866

项目设置	API

	project		-	 	必选		 	string	，项目名称。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

HTTP	Body:	JSON	Object

	data_load_empty_notification_enabled		-	 	必选		 	boolean	，是否开启空数据提醒， 	true		代表开启。
	job_error_notification_enabled		-	 	可选		 	boolean	，是否开启失败任务提醒， 	true		代表开启。
	job_states_notification		-	 	可选		 	array	，指定状态任务提醒，可选 	error	、 	finished	、 	discarded	。
	job_notification_emails		-	 	必选		 	array	，任务提醒的邮箱地址，邮箱格式： 	xx@xx.xx	。

Curl	请求示例

curl	-X	PUT	\

'http://host:port/kylin/api/projects/b/job_notification_config'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	cn'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'	\

-d	'{

								"data_load_empty_notification_enabled":true,

								"job_states_notification":["error","finished","discarded"],

								"job_notification_emails":[

												"nnnn@kyligence.io","tttt@kyligence.io"

								]

				}'

响应示例

		{

						"code":"000",

						"data":null,

						"msg":""

		}

YARN	资源队列

	PUT	http://host:port/kylin/api/projects/{project}/yarn_queue

URL	Parameters

	project		-	 	必选		 	string	，项目名称。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

HTTP	Body:	JSON	Object

	queue_name		-	 	必选		 	string	，YARN	资源队列名称。

Curl	请求示例

curl	-X	PUT	\

'http://host:port/kylin/api/projects/b/yarn_queue'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	cn'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'	\

867

项目设置	API

-d	'{

								"queue_name":"yarnqueue"

				}'

响应示例

{

				"code":	"000",

				"data":	null,

				"msg":	""

}

更新项目与任务节点的绑定关系

注意：

该	API	仅在	4.6.18.0	版本之前生效，4.6.18.0	版本之后项目与任务节点无绑定关系
该	Rest	API	需要配合任务引擎多活使用，更多详情请参考	Kyligence	Enterprise	任务引擎多活

	POST	http://host:port/kylin/api/epoch

HTTP	Body:	JSON	Object

	projects		-	 	必填		 	array[string]	，项目名称，如果数组为空，则默认更新所有项目的绑定关系。
	force		-	 	必填		 	boolean	，是否强制更新项目对应的任务节点信息。如果为	 	false		时，会先进行检查更新，
如果对应的信息已经过期，则进行更新。如果为	 	true		时，则直接进行更新。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	POST	\

		'http://host:port/kylin/api/epoch'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{"projects":["Project_A"],"force":true}'

响应示例

{

				"code":	"000",

				"data":	"",

				"msg":	""

}

项目设置重置

低效存储、Segment	设置、任务提醒以及存储配额五个设置项可以重置为默认值。每次只能重置一个设置。

	PUT	http://host:port/kylin/api/projects/{project}/project_config

URL	Parameters

	project		-	 	必选		 	string	，项目名称

868

项目设置	API

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

HTTP	Body:	JSON	Object

	reset_item		-	 	必选		 	string	，重置的项目设置项，可选
值： 	job_notification_config	， 	query_accelerate_threshold	， 	garbage_cleanup_config	， 	segment_config	,
	storage_quota_config	。

Curl	请求示例

curl	-X	PUT	\

'http://host:port/kylin/api/projects/a/project_config'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	cn'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'	\

-d	'{

								"reset_item":"job_notification_config"

				}'

响应示例

	{

					"code":"000",

					"data":{

									"project":"a",

									"description":"",

									"maintain_model_type":"MANUAL_MAINTAIN",

									"default_database":"EDW",

									"semi_automatic_mode":false,

									"storage_quota_size":10995116277760,

									"push_down_enabled":true,

									"auto_merge_enabled":true,

									"auto_merge_time_ranges":[

													"WEEK",

													"MONTH",

													"QUARTER",

													"YEAR"

									],

									"volatile_range":{

													"volatile_range_number":0,

													"volatile_range_enabled":true,

													"volatile_range_type":"DAY"

									},

									"retention_range":{

													"retention_range_number":1,

													"retention_range_enabled":false,

													"retention_range_type":"YEAR"

									},

									"job_error_notification_enabled":false,

									"job_states_notification":[],

									"data_load_empty_notification_enabled":false,

									"job_notification_emails":[

									],

									"threshold":20,

									"tips_enabled":true,

									"frequency_time_window":"MONTH",

									"low_frequency_threshold":5

					},

					"msg":""

	}

869

项目设置	API

低效存储的默认设置：

	"frequency_time_window":"MONTH"

	"low_frequency_threshold":0

Segment	设置的默认设置：

	"auto_merge_enabled":true

	"auto_merge_time_ranges":["DAY",	"MONTH",	"QUARTER",	"YEAR"]

	"volatile_range"

	"volatile_range_number":0

	"volatile_range_type":"DAY"

	retention_range

	"retention_range_enabled":false

	"retention_range_number":1

	"create_empty_segment_enabled":false

任务提醒的默认设置：

	"data_load_empty_notification_enabled":false

	"job_error_notification_enabled":false

	"job_notification_emails"		为空

存储配额默认设置:

	"kylin.storage.quota-in-giga-bytes":	10240

添加或修改项目级配置参数

	PUT	http://host:port/kylin/api/projects/{project}/config

URL	Parameters

	project		-	 	必选		 	string	，项目名称

HTTP	Body:	JSON	Object

	config_name		-	 	必选		 	string	，要添加或修改的项目级配置的参数名称
	config_value		-	 	必选		 	string	，要添加或修改的项目级配置的参数值

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	PUT	\

		'http://host:port/kylin/api/projects/kylin_learn/config'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	en'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{

								"config_name_1":"config_value_1",

								"config_name_2":"config_value_2",

								......

								"config_name_n":"config_value_n"

				}'

响应示例

{

870

项目设置	API

				"code":	"000",

				"data":	"",

				"msg":	""

}

删除项目级配置参数

	DELETE	http://host:port/kylin/api/projects/{project}/config?config_name={config_name}

URL	Parameters

	project		-	 	必选		 	string	，项目名称
	config_name		-	 	必选		 	string	，需要删除的项目级配置的参数名称

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	DELETE	\

'http://host:port/kylin/api/projects/kylin_learn/config?config_name=config_name'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	en'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":"000",

				"data":"",

				"msg":""

}

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

871

数据源管理	API

数据源管理	API

提示：

1.	 请确保已阅读前面的访问及安全认证章节，了解如何在	REST	API	语句中添加认证信息。

2.	 在	Curl	命令行上，如果您访问的	URL	中含有	 	&		符号，请注意转义，比如在	URL	两端加上引号。

3.	 本模块所有接口参数字段 	[table、database]	（可能存在别名）在未指明情况下均不区分大小写

加载	Hive	表

将	Hive	表的元数据加载到	Kyligence	Enterprise	中。用户新增一张	Hive	表之后，默认这张	Hive	表的表信息不会加
载到	Kyligence	Enterprise	中。通过调用这个	API，将	Hive	表的元数据加载到	Kyligence	Enterprise	中。

	POST	http://host:port/kylin/api/tables

HTTP	Body:	JSON	Object

	project		-	 	必选		 	string	，项目名称

	need_sampling		-	 	必选		 	boolean	，是否开启表采样

	sampling_rows		-	 	可选		 	integer	，指定采样行数的最大限制，取值范围	[10,000	-	20,000,000]

注意：当开启了表采样时，该参数为必选项。

	databases		-	 	可选		 	[string]	，加载该数据库下所有表

	tables		-	 	可选		 	[string]	，指定想要加载的表，格式如：DB.TABLE

注意：

一次最多可加载	1000	张表。如果按照数据库加载表，则所提交的数据库下的表总和应小于等于	1000；若
单次提交多个数据库，且库下的表较多，您可以分次加载避免超过限制；若单个数据库下的表超过	1000
张，则无法按库加载，您需要输入表进行加载

当表已加载，则不会重复加载，提交后将跳过已加载的表

以上两个参数	 	databases		和	 	tables		不能同时为空，即必须选择任意一个加载对象

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	POST	\

		'http://host:port/kylin/api/tables'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{"project":"ssb","tables":["SSB.LINEORDER"],"need_sampling":false}'

响应字段

	loaded	，加载成功的表

872

数据源管理	API

	failed	，加载失败的表

响应示例

{

				"code":	"000",

				"data":	{

																		"loaded":["SSB.LINEORDER"],

																		"failed":[]

												},

				"msg":	""

}

预重载	Hive	表

比较	Kyligence	Enterprise	中的	Hive	表元数据与数据源的	Hive	表的元数据的差别。Hive	表的元数据已经加载到
Kyligence	Enterprise	中，并且	Kyligence	Enterprise	已经使用这张	Hive	进行创建模型和构建索引。这时某个模型中
用到的字段在	Hive	表中被删除了，读取	Hive	表的这个字段的数据会失败。通过调用这个	API，能够比较
Kyligence	Enterprise	中的	Hive	表元数据与数据源的	Hive	表的元数据的差别，从而评估是否需要通过重载	Hive	表
来更新	Kyligence	Enterprise	中元数据。

	GET	http://host:port/kylin/api/tables/pre_reload

开始生效版本：4.1.9

URL	Parameters

	project		-	 	必选		 	string	，项目名称

	table		-	 	必选		 	string	，指定想要重载的表，格式如：DB.TABLE

	need_details		-	 	可选		 	boolean	，是否输出明细数据， 	true		代表返回明细数据， 	false		代表返回空数组[]，
默认值是	 	false	。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://host:port/kylin/api/tables/pre_reload?project=ssb&table=SSB.LINEORDER'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应字段

	has_datasource_changed	，源表结构是否发生变化

	has_effected_jobs	，是否有未运行完成的该表相关任务

	has_duplicated_columns	，是否有重复的列名

	add_column_count	，新增列的数量

	remove_column_count	，减少列的数量

	data_type_change_column_count	，列类型发生变化的数量

	broken_model_count	，	重载后可能发生损坏的模型数量
	remove_measures_count	，影响的度量数量

	remove_dimensions_count	，	影响的维度数量

873

数据源管理	API

	remove_layouts_count	，删除的索引数量

	add_layouts_count	，增加的索引数量

	refresh_layouts_count	，刷新的索引数量

	snapshot_deleted	，快照是否被删除

	duplicated_columns	，	重复的列，格式为	database.table.column
	effected_jobs	，受影响的任务	ID
	details	，明细数据

	added_columns	，新增的列名

	removed_columns	，减少的列名

	data_type_changed_columns	，数据类型发生变化的列名

	broken_models	，重载后可能损坏的模型

	removed_measures	，影响的度量名

	removed_dimensions	，影响的维度名

	removed_layouts	，删除的索引ID
	added_layouts	，增加的索引ID
	refreshed_layouts	，刷新的索引ID

响应示例

{

				"code":	"000",

				"data":	{

						"has_datasource_changed":	false,

						"has_effected_jobs":	true,

						"has_duplicated_columns":	true,

						"add_column_count":	0,

						"remove_column_count":	0,

						"data_type_change_column_count":	0,

						"broken_model_count":	0,

						"remove_measures_count":	0,

						"remove_dimensions_count":	0,

						"remove_layouts_count":	0,

						"add_layouts_count":	0,

						"refresh_layouts_count":	0,

						"snapshot_deleted":	true,

						"dumplicated_columns":	["SSB.LINEORDER.PROFIT",	"SSB.LINEORDER.LO_DISCOUNT"],

						"effected_jobs":	["266c9086-7ffe-44a1-9d5e-f9f9941b891d",	"f42e5dd3-78e6-43f8-9bcb-edcb2c09312d"],

						"details":	{

												"added_columns":	[],

												"removed_columns":	[],

												"data_type_changed_columns":	[],

												"broken_models":	[],

												"removed_measures":	[],

												"removed_dimensions":	[],

												"removed_layouts":	{},

												"added_layouts":	{},

												"refreshed_layouts":	{}

								}

				},

				"msg":	""

}

重载	Hive	表

	POST	http://host:port/kylin/api/tables/reload

请求权限：MANAGEMENT	及以上权限

开始生效版本：4.2.0

HTTP	Body:	JSON	Object

874

数据源管理	API

	project		-	 	必选		 	string	，项目名称。
	table		-	 	必选		 	string	，指定想要加载的表，格式如：DB.TABLE。
	need_sampling		-	必选	 	boolean	，是否开启表采样。
	sampling_rows		-	可选	 	integer	，指定采样行数的最大限制，取值范围	[10,000	-	20,000,000]。

注意：当开启了表采样时，该参数为必选项。

	need_building		-	可选	 	boolean	，当有索引新增时，是否要构建新增的这部分索引， 	true		表示构建， 	false
表示不构建，默认为	 	false	。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	POST	\

		'http://host:port/kylin/api/tables/reload'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	en'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{"project":"ssb","table":"SSB.LINEORDER","need_sampling":false,"need_building":false}'

响应字段

	sampling_id	，触发的表采样任务	id。
	job_ids	，触发的构建任务	id。

响应示例

{

				"code":	"000",

				"data":	{

								"sampling_id":"",

								"job_ids":["1234","1234"]

				},

				"msg":	""

}

预删除表

评估从	Kyligence	Enterprise	中卸载	Hive	表元数据的风险。Kyligence	Enterprise	加载某张	Hive	表的元数据一段时
间了。在某些情况下，需要在	Kyligence	Enterprise	中下线这张	Hive	表。在正式下线之前，需要评估写在卸载这张
Hive	表元数据对	Kyligence	Enterprise	模型、任务的影响。

	GET	http://host:port/kylin/api/tables/{database}/{table}/prepare_unload

URL	Parameters

	database		-	 	必选		 	string	，待删除表数据库名

	table		-	 	必选		 	string	，待删除表名

	project		-	 	必选		 	string	，项目名称

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

875

数据源管理	API

Curl	请求示例

curl	-X	GET	\

		'http://host:port/kylin/api/tables/SSB/LINEORDER/prepare_unload?project=ssb'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应字段

	has_job	，当前表是否存在正在运行的表采样、构建快照任务

	has_model	，当前表是否被模型使用

	has_snapshot	，当前表是否存在快照

	storage_size	，当前表快照的存储大小	(Byte)
	models	，模型列表

响应示例

{

				"code":	"000",

				"data":	{

								"has_job":	false,

								"has_model":	true,

								"has_snapshot":	true,

								"storage_size":	16616,

								"models":	[

												"model"

								]

				},

				"msg":	""

}

删除表

从	Kyligence	Enterprise	中卸载	Hive	表的元数据。

	DELETE	http://host:port/kylin/api/tables/{database}/{table}

URL	Parameters

	databases		-	 	必选		 	string	，待删除表数据库名

	table		-	 	必选		 	string	，待删除表名

	project		-	 	必选		 	string	，项目名称

	cascade		-	 	可选		 	boolean	，是否全部删除。默认为	 	false

true:	删除源表、快照、关联的	Kafka/Hive	表、相关模型，并停止/删除相关任务
false:	删除源表、快照，并停止相关任务。但保留相应模型（将变为	Broken	状态，可通过重新添加该表进
行修复）

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	DELETE	\

		'http://host:port/kylin/api/tables/SSB/LINEORDER?project=ssb'	\

876

数据源管理	API

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应字段

	data	，已被删除的表名。

响应示例

{

				"code":	"000",

				"data":	"SSB.LINEORDER",

				"msg":	""

}

表采样

通过采样	Hive	表的数据，了解	Hive	表的数据特征。

	POST	http://host:port/kylin/api/tables/sampling_jobs

请求权限：MANAGEMENT	及以上权限

开始生效版本：4.2.0

HTTP	Body:	JSON	Object

	project		-	 	必选		 	string	，项目名称。
	qualified_table_name		-	 	必选		 	string	，指定想要采样的表，格式如：DB.TABLE。
	rows		-	 	必选		 	integer	，指定采样行数的最大限制，取值范围	[10,000	-	20,000,000]。
	priority		-	 	可选		 	integer	，设置任务优先级，范围为	 	0-4	，	默认为 	3	。
	yarn_queue		-	 	选填		 	string	，指定该任务使用的	YARN	队列，在系统级别或项目级别设置参数后使用：
kylin.engine-yarn.queue.in.task.enabled（是否允许为任务指定	YARN	队列，默认	false	不开启，true	代表开
启）、kylin.engine-yarn.queue.in.task.available（可供设置的	YARN	队列，多个队列时用英文逗号分隔）。
	tag		-	 	选填		 	object	，任务标记，如果填入此值，在调用	返回任务列表	接口，返回该任务时会将此字段原样
返回，可用于系统集成时，对任务进行标记并进行相应处理。字段值最大限制	默认	1024	KB，由配置
kylin.job.tag-max-size=1024	指定。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	POST	\

		'http://host:port/kylin/api/tables/sampling_jobs'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{"project":"ssb","qualified_table_name":"SSB.LINEORDER","rows":20000,"priority":0}'

响应字段

	data	，表采样任务的	id。

响应示例

877

数据源管理	API

{

				"code":"000",

				"data":"3ccf61f6-0b0a-2cd5-156a-5cd52d2b413d",

				"msg":""

}

获取表中某列的分区格式

当某列在	Kyligence	Enterprise	中在某模型中被使用为分区列时，获取该列的分区格式

	GET	http://host:port/kylin/api/tables/column_format

请求权限：Operation	及以上操作权限。

开始生效版本：4.2.0

Request	Parameters

	project		-	 	必填		 	string	，项目名称。
	table		-	 	必填		 	string	，表名（不支持视图），格式：database.table。
	column_name		-	 	必填		 	string	，列名称。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://host:port/kylin/api/tables/column_format?project=test&table=DEFAULT.KYLIN_SALES&column_name=PART_

DT'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应字段

	column_name		列名称
	column_format		列的分区格式

响应示例

{

				"code":	"000",

				"data":	{

										"partition_column":	"PART_DT",

														"format":	"yyyy-MM-dd"

				},

				"msg":	""

}

获取表信息

获取指定	Hive	表的元数据。

	GET	http://host:port/kylin/api/tables

请求权限：READ	及以上权限。

878

数据源管理	API

开始生效版本：4.2.0

Request	Parameters

	project		-	 	必填		 	string	，项目名称。
	database		-	 	可选		 	string	，数据库名称。
	table		-	 	可选		 	string	，表名。
	is_fuzzy		-	 	可选		 	boolean	，表名称是否启用模糊匹配， 	true		表示开启， 	false	表示关闭，默认为
	false	。

	ext		-	 	可选		 	boolean	，是否需要包含表的扩展信息， 	true		表示开启， 	false	表示关闭，默认为	 	true	。
	page_offset		-	 	可选		 	int	，分页页面，默认为	 	0	。
	page_size		-	 	可选		 	int	，分页大小，默认为	 	10	。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://localhost:7070/kylin/api/tables?project=test&database=SSB&table=KYLIN_SALES'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":	"000",

				"data":	{

								"value":	[

												{

																"uuid":	"6e638305-1a44-42dc-a161-5e06338dcb14",

																"last_modified":	1600335525521,

																"create_time":	1600335525522,

																"version":	"4.0.0.0",

																"mvcc":	0,

																"name":	"KYLIN_SALES",

																"table_comment":	null,

																"columns":	[

																				{

																								"id":	"1",

																								"name":	"TRANS_ID",

																								"datatype":	"bigint",

																								"cardinality":	null,

																								"min_value":	null,

																								"max_value":	null,

																								"null_count":	null

																				}

																],

																"source_type":	9,

																"kafka_bootstrap_servers":	null,

																"subscribe":	null,

																"starting_offsets":	null,

																"table_type":	"MANAGED",

																"top":	false,

																"increment_loading":	false,

																"last_snapshot_path":	null,

																"database":	"DEFAULT",

																"exd":	{

																				"owner":	"root",

																				"create_time":	"1524213799000",

879

数据源管理	API

																				"total_file_size":	"0",

																				"hive_inputFormat":	"org.apache.hadoop.mapred.TextInputFormat",

																				"hive_outputFormat":	"org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat",

																				"location":	"hdfs://sandbox.hortonworks.com:8020/apps/hive/warehouse/kylin_sales",

																				"partition_column":	"",

																				"total_file_number":	"0",

																				"last_access_time":	"0"

																},

																"root_fact":	false,

																"lookup":	false,

																"primary_key":	[],

																"foreign_key":	[],

																"partitioned_column":	null,

																"partitioned_column_format":	null,

																"segment_range":	null,

																"storage_size":	-1,

																"total_records":	0,

																"sampling_rows":	[],

																"last_build_job_id":	null

												}

								],

								"offset":	0,

								"limit":	10,

								"total_size":	3

				},

				"msg":	""

}

注意：返回字段 	sampling_rows		为空时，可能原因是用户无数据权限，或表没有数据。

注意：返回字段	 	table_comment		的开始生效版本为	4.6.9，表示表注释。对于在此版本之前已经加载过的
表，且表注释不为空，想要通过此	API	获取表注释，那么需要先重载此表（重载表有风险，可能会因为源表
结构发生变化而导致重载后删除与该表有关的索引数据，谨慎操作！），然后才能获取到该表的注释信息。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

880

模型	API

模型	API

Kyligence	Enterprise	提供了可以用来查看模型信息、进行模型构建和管理的	REST	API。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

881

模型	API

模型管理	API

请确保已阅读前面的访问及安全认证章节，了解如何在	REST	API	语句中添加认证信息。
在	Curl	命令行上，如果您访问的	URL	中含有	 	&		符号，请注意转义，比如在	URL	两端加上引号。
在	Curl	命令行上，如果您访问的	URL	中含有	 	%		符号，请注意转义，转为	 	%25	。

创建模型

	POST	http://host:port/kylin/api/models

请求权限：MANAGEMENT	及以上权限

开始生效版本：4.5.11

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

HTTP	Body:	JSON	Object

	project		-	 	必填		 	string	，项目名称

	fact_table		-	 	必填		 	string	，事实表名

	uuid		-	 	可选		 	string	，唯一识别码，默认随机生成

	alias		-	 	必填		 	string	，模型别名

	management_type		-	 	必填		 	string	，创建模型请填：	MODEL_BASED

	simplified_measures		-	 	必填		 	JSON	Object[]	，度量信息

	name		-	 	必填		 	string	，度量名称
	expression		-	 	必填		 	string	，函数
（SUM,MIN,MAX,TOP_N,COUNT,COUNT_DISTINCT,CORR,PERCENTILE_APPROX,COLLECT_SET）
	parameter_value		-	 	必填		 	JSON	Object[]	，度量参数

	type		-	 	必填		 	string	，参数类型（constant,column）无默认值
	value		-	 	必填		 	int|string	，参数值（expression为COUNT且type为constant时，此处请填1；其他情
况为：表名.列名）无默认值

	return_type		-	 	必填		 	string	，函数参数，例如	topn(10)、topn(100)、percentile(100)等等，若无需参数填
空字符串：""

expression与return_type对应关系如下：

TOP_N:

		*	Top	10:	topn(10)

		*	Top	100:	topn(100)

		*	Top	1000:	topn(1000)

COUNT_DISTINCT:

		*	Error	Rate	<	9.75%:	hllc(10)

		*	Error	Rate	<	4.88%:	hllc(12)

		*	Error	Rate	<	2.44%:	hllc(14)

		*	Error	Rate	<	1.72%:	hllc(15)

		*	Error	Rate	<	1.22%:	hllc(16)

		*	Precisely:	bitmap

PERCENTILE_APPROX:

882

模型	API

		*	percentile(100)

		*	percentile(1000)

		*	percentile(10000)

	comment		-	 	可选		 	string	，注释

	simplified_dimensions		-	 	必填		 	JSON	Object[]	，维度信息

	column		-	 	必填		 	string	，格式：表名.列名
	name		-	 	必填		 	string	，列别名，可与列名保持一致
	status		-	 	必填		 	string	，列状态，固定填	DIMENSION

	computed_columns		-	 	可选		 	JSON	Object[]	，可计算列描述信息

	columnName		-	 	必填		 	string	，可计算列列名
	expression		-	 	必填		 	string	，表达式
	datatype		-	 	必填		 	string	，数据类型（VARCHAR,INT,BIGINT	...standard	sql	types）
	tableIdentity		-	 	必填		 	string	，格式：Schema名称.表名
	tableAlias		-	 	必填		 	string	，表别名

	join_tables		-	 	必填		 	JSON	Object[]	，维表相关信息

	table		-	 	必填		 	string	，表名

	join		-	 	必填		 	JSON	Object	，连接信息

	type		-	 	必填		 	string	，连接类型（INNER,LEFT）无默认值

	foreign_key		-	 	必填		 	string[]	，其它表上关联该表的列

	primary_key		-	 	必填		 	string[]	，该表上关联其它表的列

	simplified_non_equi_join_conditions		-	 	可选		 	JSON	Object	，非等值关联条件

（注意1：使用该参数需提前开启“支持拉链表”设置，详见缓慢变化维度）

（注意2：关联关系	>=	和	<	必须成对出现，且位于中间的列必须一致）

	foreign_key		-	 	string	，其它表上关联该表的列
	primary_key		-	 	string	，该表上关联其它表的列
	op		-	 	string	，非等值关联关系（LESS_THAN,GREATER_THAN_OR_EQUAL）

	kind		-	 	可选		 	string	，表类型（FACT,LOOKUP）默认为：LOOKUP

	alias		-	 	可选		 	string	，别名

	flattenable		-	 	必填		 	string	，预计算关联关系（预计算：flatten，不预计算：normalized）无默认值，通
常使用	flatten

	join_relation_type		-	 	可选		 	string	，连接类型（MANY_TO_ONE,MANY_TO_MANY）默认为：

MANY_TO_ONE

	partition_desc		-	 	可选		 	JSON	Object	，分区列信息

	partition_date_column		-	 	必填		 	string	，时间分区列，格式：表名.列名
	partition_date_format		-	 	必填		 	string	，时间分区列格式（yyyy-MM-dd，yyyyMMdd等，支持的时间格
式请参考用户手册“基本模型设计”章节）
	partition_type		-	 	可选		 	string	，分区类型（APPEND）默认为：APPEND

	owner		-	 	可选		 	string	，模型拥有者，默认为当前用户

	description		-	 	可选		 	string	，模型额外描述

	capacity		-	 	可选		 	string	，模型容量（SMALL,MEDIUM,LARGE）默认为：MEDIUM

883

模型	API

	filter_condition		-	 	可选		 	string	，数据筛选条件，通过数据筛选在保存模型时过滤掉空值数据或是符合特定
条件的数据

	with_base_index		-	 	可选		 	boolean	，是否添加基础索引，包含基础聚合索引和基础明细索引，基础索引包含模
型全部维度和度量，随着模型变化自动更新，默认值：false;	4.6.6	版本后推荐使用	 	base_index_type	，配置
	base_index_type		后	 	with_base_index		不生效

	base_index_type		-	 	可选		 	Array[String]	，选择要添加的基础索引类型，可选
值 	BASE_AGG_INDEX	, 	BASE_TABLE_INDEX	，开始生效版本：4.6.6

	[BASE_AGG_INDEX,	BASE_TABLE_INDEX]		基础聚合索引和基础明细索引都添加
	[BASE_AGG_INDEX]		只添加基础聚合索引
	[BASE_TABLE_INDEX]		只添加基础明细索引
	[]		不添加基础索引

	computed_column_name_auto_adjust		-	 	可选		 	boolean	，与项目内可计算列表达式相同，名称不同时，是否自动
调整名称为已存在的可计算列名。默认值：false

（注意：嵌套可计算列中，被嵌套的可计算列调整名称后，会导致创建模型失败。请确保嵌套可计算列不

会发生冲突）

Curl	请求示例

curl	-X	POST	\

		'http://localhost:7070/kylin/api/models'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\
		#	该示例为了展示直观，将	JSON	Object	String	展开，使用时需要进行压缩并转义

		-d	'{

				"project":	"pj01",

				"fact_table":	"SSB.P_LINEORDER",

				"alias":	"test_model_01",

				"management_type":	"MODEL_BASED",

				"simplified_measures":	[

								{

												"name":	"COUNT_ALL",

												"expression":	"COUNT",

												"parameter_value":	[

																{

																				"type":	"constant",

																				"value":	1

																}

												],

												"return_type":	""

								}

				],

				"simplified_dimensions":	[

								{

												"column":	"P_LINEORDER.LO_ORDERKEY",

												"name":	"LO_ORDERKEY",

												"status":	"DIMENSION"

								},

								{

												"column":	"P_LINEORDER.LO_CUSTKEY",

												"name":	"LO_CUSTKEY",

												"status":	"DIMENSION"

								},

								{

												"column":	"P_LINEORDER.LO_ORDERDATE",

												"name":	"LO_ORDERDATE",

												"status":	"DIMENSION"

								},

								{

												"column":	"P_LINEORDER.LO_ORDERPRIOTITY",

884

模型	API

												"name":	"LO_ORDERPRIOTITY",

												"status":	"DIMENSION"

								},

								{

												"column":	"P_LINEORDER.V_REVENUE",

												"name":	"V_REVENUE",

												"status":	"DIMENSION"

								},

								{

												"column":	"DATES.D_YEAR",

												"name":	"D_YEAR",

												"status":	"DIMENSION"

								},

								{

												"column":	"CUSTOMER.C_NAME",

												"name":	"C_NAME",

												"status":	"DIMENSION"

								},

								{

												"column":	"CUSTOMER.C_PHONE",

												"name":	"C_PHONE",

												"status":	"DIMENSION"

								}

				],

				"join_tables":	[

								{

												"table":	"SSB.DATES",

												"join":	{

																"type":	"LEFT",

																"foreign_key":	[

																				"P_LINEORDER.LO_ORDERDATE"

																],

																"primary_key":	[

																				"DATES.D_DATE"

																]

												},

												"alias":	"DATES",

												"flattenable":	"flatten",

												"join_relation_type":	"MANY_TO_ONE"

								},

								{

												"table":	"SSB.CUSTOMER",

												"join":	{

																"type":	"LEFT",

																"foreign_key":	[

																				"P_LINEORDER.LO_CUSTKEY"

																],

																"primary_key":	[

																				"CUSTOMER.C_CUSTKEY"

																]

												},

												"alias":	"CUSTOMER",

												"flattenable":	"flatten",

												"join_relation_type":	"MANY_TO_ONE"

								}

				],

				"base_index_type":	["BASE_AGG_INDEX",	"BASE_TABLE_INDEX"],

				"computed_columns":	[

								{

												"tableIdentity":	"SSB.LINEORDER",

												"tableAlias":	"LINEORDER",

												"columnName":	"CC_3",

												"expression":	"1+2",

												"datatype":	"BIGINT"

								}

				],

				"computed_column_name_auto_adjust":	true

		}'

885

模型	API

响应字段

	code		-	 	string	，响应码，返回值： 	000		（请求处理成功），	 	999	（请求处理失败）
	msg		-	 	string	，响应消息
	data		-	 	JSON	Object	，返回内容

	base_table_index		-	 	JSON	Object	，基础明细索引信息

	dimension_count		-	 	int	，维度数量
	measure_count		-	 	int	，度量数量
	layout_id		-	 	long	，索引ID号
	operate_type		-	 	string	，	操作类型（UPDATE,CREATE）

	base_agg_index		-	 	JSON	Object	，基础聚合索引信息，结构同	 	base_table_index
	warn_code		-	 	string	，告警信息
	computed_column_conflict		-	 	JSON	Object	，可计算列名自动调整后返回的调整信息

响应示例

{

		"code":	"000",

		"msg":	"",

		"data":	{

				"base_table_index":	{

								"dimension_count":	8,

								"measure_count":	0,

								"layout_id":	20000000001,

								"operate_type":	"CREATE"

				},

				"base_agg_index":	{

								"dimension_count":	8,

								"measure_count":	1,

								"layout_id":	1,

								"operate_type":	"CREATE"

				},

				"warn_code":	null,

				"computed_column_conflict":	{

						"detail":	[

								{

										"detail_code":	"KE-010010204",
										"detail_msg":	"名为	“CC_3”	表达式为	“1+2”	的可计算列，与项目中名为	“CC_1”	表达式为	“1+2”	的可计算列表达式存
在冲突，将当前可计算列重命名为	“CC_1”	。"

								}

						]

				}

		}

}

失败响应示例一

{

		"code":	"999",

		"data":	null,
		"msg":	"KE-010001002(项目名为空)：没有项目信息，请指定一个项目。",

		"stacktrace":	"KE-010001002(Empty	Project	Name)	\norg.apache.kylin.common.exception.KylinException:	KE-01
0001002(项目名为空)：没有项目信息，请指定一个项目。	...",
		"exception":	"KE-010001002(项目名为空)：没有项目信息，请指定一个项目。",

		"url":	"http://localhost:7070/kylin/api/models"

}

失败响应示例二

{

		"code":	"999",

		"data":	{

886

模型	API

						"detail":	[

										{

														"detail_code":	"KE-010010203",
														"detail_msg":	"重复的可计算列表达式，名为	“CC_2”	表达式为	“concat(PART.P_NAME,	LINEORDER.LO_QUANTIT
Y)”	的可计算列，与模型	“M1”	中的可计算列表达式存在冲突。"

										},

										{

														"detail_code":	"KE-010010202",
														"detail_msg":	"重复的可计算列名，名为	“CC_1”	表达式为	“LINEORDER.LO_ORDERKEY	+	PART.P_SIZE”	的可计
算列，与模型	“M1”	中的可计算列名存在冲突。"

										}

						]

		},
		"msg":	"KE-010010201:	当前模型中定义的可计算列的名称和表达式与其它模型存在冲突。",
		"stacktrace":	"KE-010010201:	当前模型中定义的可计算列的名称和表达式与其它模型存在冲突。........",
		"exception":	"KE-010010201:	当前模型中定义的可计算列的名称和表达式与其它模型存在冲突。",

		"url":	"http://localhost:7070/kylin/api/models",

		"suggestion":	"",

		"error_code":	"KE-010010201"

}

错误码（具体错误信息请以接口返回内容为准）

	KE-010001001	:	项目不存在
	KE-010001002	:	项目名为空
	KE-010006002	:	非法的分区列
	KE-010000003	:	非法参数
	KE-010000002	:	非法的范围
	KE-010000004	:	非法命名
	KE-010006005	:	时间戳列不存在
	KE-010002010	:	添加模型失败
	KE-010011001	:	重复的可计算列名
	KE-010007001	:	表不存在

返回模型列表

返回项目下指定条件的模型列表。

	GET	http://host:port/kylin/api/models

URL	Parameters

	project		-	 	必填		 	string	，项目名称。
	page_offset		-	 	可选		 	int	，分页页面，默认为	 	0	。
	page_size		-	 	可选		 	int	，分页大小，默认为	 	10	。
	status		-	 	可选		 	string	，模型状态。
	model_name		-	 	可选		 	string	，模型名称。
	exact		-	 	可选		 	boolean	，是否和模型名称完全匹配。默认为	 	true	。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://localhost:7070/kylin/api/models?project=doc_expert'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

887

模型	API

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应字段

	code	： 	String	，响应码，返回值： 	000		（请求处理成功），	 	999	（请求处理失败）。
	data	： 	JSON	，返回数据。

	value	：返回值的详细信息，各字段解释如下：

	name	： 	String	，模型名称。

	lookups	： 	JSON	，维度表信息列表。

	size_kb	： 	Long	，模型中所有	Segment	大小的总和。
	input_records_count	： 	Long	，所有	Segment	的平表条数总和。
	input_records_size	： 	Long	，所有	Segment的平表总大小。
	project	： 	String	，项目名称。

	uuid	： 	String	，模型ID。
	last_modified	： 	Long	，模型最后修改时间。

	create_time	： 	Long	，模型创建时间。

	mvcc	： 	Long	，元数据修改版本号。

	alias	： 	String	，模型别名。

	owner	： 	String	，模型所属的用户。

	config_last_modifier	： 	String	，最后修改的用户。

	fact_table	： 	String	，事实表，一个模型中仅包含一个事实表。

	fact_table_alias	： 	String	，事实表别名。

	join_tables	： 	JSON	，关联表。

	partition_desc	： 	JSON	，模型分区列。

	all_measures	： 	JSON	，模型中所有度量。

	multi_partition_desc	： 	JSON	，多级分区列。

	computed_columns	： 	JSON	，可计算列。

	canvas	： 	JSON	，模型画布的位置信息。

	status	： 	String	，模型状态，返回值： 	online	（上线）、 	offline	（下线）、 	broken	（不可

用）、 	warning	（警告）。

	last_build_end	： 	String	，最后一个	Segment	的结束时间。
	storage	： 	Long	，模型总存储大小，单位为字节。

	source	： 	Long	，模型中所有	Segment	的sourceBytes之和。
	expansion_rate	： 	String	，模型膨胀率，单位为百分比。

	usage	： 	Long	，模型被查询次数。

	model_broken	： 	Boolean	，模型是否不可用。

	root_fact_table_deleted	： 	Boolean	，事实表是否为空。

	segments	： 	JSON	，Segment	列表。
	recommendations_count	： 	Integer	，优化建议条数。

	simplified_measures	： 	JSON	，模型度量列表。

	simplified_dimensions	： 	JSON	，模型维度列表。

	simplified_tables	： 	JSON	，模型包含的表。

	offset	：页码。

	limit	：每页显示模型数。

	total_size	：总模型数。

响应示例

[!NOTE]

模型中部分参数包含较多的	JSON	信息（例如 	join_tables	），本文未一一列举。您也可以通过	Kyligence
Enterprise	控制台查看更多信息。具体操作，见模型详情。

888

模型	API

		{

						"code":"000",

						"data":{

										"value":	[

														{

																		"name":"Model_03",

																		"lookups":Array[1],

																		"is_streaming":false,

																		"size_kb":0,

																		"input_records_count":0,

																		"input_records_size":0,

																		"project":null,

																		"uuid":"0464241b-fd7d-49a9-a3c9-b4f7e32cf489",

																		"last_modified":1574750372949,

																		"create_time":1574761225505,

																		"version":"4.0.0.0",

																		"mvcc":4,

																		"alias":"Model_03",

																		"owner":"ADMIN",

																		"config_last_modifier":null,

																		"config_last_modified":0,

																		"description":"",

																		"fact_table":"SSB.LINEORDER",

																		"fact_table_alias":null,

																		"management_type":"MODEL_BASED",

																		"join_tables":Array[1],

																		"filter_condition":"",

																		"partition_desc":Object{...},

																		"capacity":"MEDIUM",

																		"segment_config":Object{...},

																		"data_check_desc":null,

																		"semantic_version":0,

																		"all_named_columns":Array[26],

																		"all_measures":Array[2],

																		"column_correlations":Array[0],

																		"multilevel_partition_cols":Array[0],

																		"computed_columns":Array[0],

																		"canvas":Object{...},

																		"status":"ONLINE",

																		"last_build_end":"902016000000",

																		"storage":24694,

																		"source":5585164,

																		"expansion_rate":"0.44",

																		"usage":0,

																		"model_broken":false,

																		"root_fact_table_deleted":false,

																		"segments":null,

																		"recommendations_count":0,

																		"simplified_measures":Array[2],

																		"simplified_dimensions":Array[9],

																		"simplified_tables":Array[2],

																		"multi_partitiomulti_partition_desc":	n_desc":	{

																						"columns":	["KYLIN_SALES.LSTG_SITE_ID"],

																						"partitions":	[

																										{

																														"id":	0,

																														"values":	[

																																		"1"

																														]

																										},

																										{

																														"id":	1,

																														"values":	[

																																		"2"

																														]

																										}

																						],

																						"max_partition_id":	1

																				}

889

模型	API

														},

														Object{...},

														Object{...}

										],

										"offset":0,

										"limit":10,

										"total_size":3

						},

						"msg":""

		}

返回模型描述信息

返回单个模型的描述信息，如维度、度量、事实表、表关联关系等。

	GET	http://host:port/kylin/api/models/{project}/{model_name}/model_desc

该	API	的返回中不会包含系统推荐出的维度和索引。

URL	Parameters

	project		-	 	必填		 	string	，项目名称。
	model_name		-	 	必填		 	string	，模型名称。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://host:port/kylin/api/models/kyligence/AUTO_MODEL/model_desc'\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应字段

	code	： 	String	，响应码，返回值： 	000		（请求处理成功），	 	999	（请求处理失败）。
	data	： 	JSON	，返回数据。

	uuid	： 	String	，模型ID。
	last_modified	： 	Long	，模型最后修改时间。

	create_time	： 	Long	，模型最后修改时间。

	version	： 	String	，模型版本。

	name	： 	String	，模型名称。

	project	： 	String	，项目名称。

	description	： 	String	，模型描述。

	dimensions	： 	Array	，维度信息。

	id	： 	Integer	，维度	ID。
	name	： 	String	，维度名称。

	column	： 	String	，列名。

	status	： 	String	，状态。

	depend_lookup_table	： 	Boolean	，是否依赖查询表。

	cardinality	： 	Long	，基数。

	min_value	： 	String	，最小值。

	max_value	： 	String	，最大值。

890

模型	API

	max_length_value	： 	String	，最大长度。

	min_length_value	： 	String	，最小长度。

	null_count	： 	Long	，空统计。

	comment	： 	String	，维度注释或备注。

	type	： 	String	，维度类型。

	simple	： 	Array[String]	，简单类型。

	derived		： 	Boolean	，该列是否为衍生维度。

	measures	： 	Array	，度量信息。

	name	： 	String	，度量名称。

	function	： 	JSON	，函数。

	expression	： 	String	，表达式。

	parameters	： 	Array	，参数。

	type	： 	String	，参数类型。

	value	： 	String	，参数值。

	returntype	： 	String	，返回类型。

	column	： 	String	，度量字段。

	comment	： 	String	，度量注释或备注。

	id	： 	Integer	，度量	ID。
	type	： 	String	，度量类型。

	internal_ids	： 	Array[Integer]	，内部ID数组。

	aggregation_groups	： 	Array	，聚合组。

	includes	： 	Array[String]	，聚合组包含的列。

	select_rule		： 	JSON	，聚合组类型。

	hierarchy_dims	： 	Array[][]	，层级维度。

	mandatory_dims	： 	Array[String]	，必须维度。

	joint_dims	： 	Array[][]	，联合维度。

	computed_columns	： 	Array	，可计算列。

	tableIdentity	： 	String	，表名。

	tableAlias	： 	String	，表别名。

	columnName	： 	String	，列名。

	expression	： 	String	，可计算列的表达式。

	innerExpression	： 	String	，

	datatype	： 	String	，列类型。

	comment	： 	String	，列的注释或备注。

	rec_uuid	： 	String	，字段ID。

	fact_table	： 	String	，事实表。

	join_tables	： 	Array	，关联表。

	table	： 	String	，表名称。

	kind	： 	String	，表类型，返回值： 	FACT	（事实表）、 	LOOKUP	（维表）。

	alias	： 	String	，表别名。

	join	： 	JSON	，关联条件信息。

	type	： 	String	，连接类型，返回值： 	INNER	（内连接）、 	LEFT	（左连接）、 	RIGHT	（右连

接）、 	OUTER	（外连接）。

	primary_key	： 	Array[String]	，该表上关联其它表的列。

	foreign_key	： 	Array[String]	，其它表上关联该表的列。

	non_equi_join_condition	： 	String	，非等值关联条件	(对象）。
	primary_table	： 	String	，当前表。

	foreign_table	： 	String	，当前表对应的关联表。

	flattenable	： 	String	，维表是否参与到打平表。

	join_relation_type	： 	String	，关联关系，返回值： 	MANY_TO_ONE	（多对一）、 	ONE_TO_ONE	（一对

一）、 	ONE_TO_MANY	（一对多）	、 	MANY_TO_MANY	（多对多）。

891

模型	API

	msg	： 	String	，响应信息。

响应示例

{

				"code":"000",

				"data":{

								"uuid":"24dc8eae-e613-40ce-b601-26f065f24070",

								"last_modified":1577436020423,

								"create_time":	1577436020115,

								"version":"4.0.0.0",

								"name":"kyligence",

								"project":"test_gy",

								"description":"",

								"dimensions":[

												{

																"id":8,

																"name":"P_LINEORDER_LO_CUSTKEY",

																"column":"P_LINEORDER.LO_CUSTKEY",

																"status":"DIMENSION",

																"depend_lookup_table":	false,

																"cardinality":	null,

																"min_value":	null,

																"max_value":	null,

																"max_length_value":	null,

																"min_length_value":	null,

																"null_count":	null,

																"comment":	null,

																"type":	"integer",

																"simple":	null,

																"derived":false

												}

								],

								"measures":[

												{

																"name":"COUNT_ALL",

																"function":{

																				"expression":"COUNT",

																				"parameters":[

																								{

																												"type":"constant",

																												"value":"1"

																								}

																				],

																				"returntype":"bigint"

																},

																"column":	null,

																"comment":	null,

																"id":100000,

																"type":	"NORMAL",

																"internal_ids":	[]

												},

												{

																"name":"TEST",

																"function":{

																				"expression":"SUM",

																				"parameters":[

																								{

																												"type":"column",

																												"value":"P_LINEORDER.LO_QUANTITY"

																								}

																				],

																				"returntype":"bigint"

																},

																"column":	null,

																"comment":	null,

																"id":100001,

																"type":	"NORMAL",

																"internal_ids":	[]

892

模型	API

												}

								],

								"aggregation_groups":[

												{

																"includes":[

																				"P_LINEORDER.LO_CUSTKEY"

																],

																"select_rule":{

																				"hierarchy_dims":[

																				],

																				"mandatory_dims":[

																				],

																				"joint_dims":[

																				]

																}

												}

								],

								"computed_columns":	[{

										"tableIdentity":	"SSB.P_LINEORDER",

										"tableAlias":	"P_LINEORDER",

										"columnName":	"CASTCOL",

										"expression":	"CAST(P_LINEORDER.LO_PARTKEY	as	bigint)",

										"innerExpression":	"CAST(`P_LINEORDER`.`LO_PARTKEY`	as	bigint)",

										"datatype":	"BIGINT",

										"comment":	null,

										"rec_uuid":	null

								},{...}],

								"fact_table":	"SSB.P_LINEORDER",

								"join_tables":	[{

										"table":	"SSB.CUSTOMER",

										"kind":	"LOOKUP",

										"alias":	"CUSTOMER",

										"join":	{

														"type":	"INNER",

														"primary_key":	[

																		"CUSTOMER.C_CUSTKEY"

														],

														"foreign_key":	[

																		"P_LINEORDER.LO_CUSTKEY"

														],

														"non_equi_join_condition":	null,

														"primary_table":	null,

														"foreign_table":	null

										},

										"flattenable":	"flatten",

										"join_relation_type":	"MANY_TO_ONE"

								},{...}]

				},

				"msg":""

}

设置分区列

为指定项目下的指定模型设置分区字段。用户想要为模型设置成增量构建，此时，需要指定模型的分区字段。

Kylin	会根据模型的分区字段，增量加载	Hive	表中的数据，实现增量构建的目的。

	PUT	http://host:port/kylin/api/models/{model_name}/partition

URL	Parameters

	model_name		-	 	必填		 	string	，模型名称。

HTTP	Body:	JSON	Object

893

模型	API

	project		-	 	必填		 	string	，项目名称。

	partition_desc		-	 	选填	，分区列信息。

	partition_date_column		-	 	选填		 	string	，分区列名。
	partition_date_format		-	 	选填		 	string	，分区列格式。

	multi_partition_desc		-	 	选填	，多级分区子分区列信息，多级分区模型该值需要。

	columns		-	 	array[string]	，多级分区的子分区列

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	PUT	\

		http://host:port/kylin/api/models/multi_partition_model/partition	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json'	\

		-d	'{

				"project":	"multi_partition",

				"partition_desc":	{

								"partition_date_column":	"KYLIN_SALES.PART_DT",

								"partition_date_format":	"yyyy-MM-dd"

				},

				"multi_partition_desc":	{

								"columns":	[

												"KYLIN_SALES.LSTG_SITE_ID"

								]

				}

}'

响应示例

{

				"code":"000",

				"data":"",

				"msg":""

}

设置分区列（废弃）

	PUT	http://host:port/kylin/api/models/{project}/{model_name}/partition_desc

URL	Parameters

	model_name		-	 	必填		 	string	，模型名称。
	project		-	 	必填		 	string	，项目名称。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

HTTP	Body:	JSON	Object

	partition_desc		-	 	可选		 	string	，定义分区列的列名及数据类型。

894

模型	API

	start		-	 	可选		 	string	，Segment	开始时间（存在时间分区列），默认为	 	1	，时间戳类型，毫秒。

	end		-	 	可选		 	string	，Segment	结束时间（存在时间分区列），默认为	 	9223372036854775806	，时间戳类型，
毫秒。

如您需要设置模型分区列时，上述参数均需要进行填写。反之，如您希望模型定义为无分区列时，上述

参数均不填写即可。

Curl	请求示例

curl	-X	PUT	\

		'http://localhost:7070/kylin/api/models/ssb/test/partition_desc'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	en'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{

				"partition_desc":{

								"partition_date_column":"LINEORDER.LO_ORDERDATE",

								"partition_date_format":"yyyy-MM-dd"},

				"start":"0",

				"end":"1111"

				}'

响应示例

{

				"code":"000",

				"data":"",

				"msg":""

}

模型校验

	POST	http://host:port/kylin/api/models/model_validation

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

HTTP	Body:	JSON	Object

	project		-	 	必填		 	string	，项目名称。
	sqls		-	 	必填		 	array	，用于校验的查询。

Curl	请求示例

curl	-X	POST	\

		'http://localhost:7070/kylin/api/models/model_validation'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{"project":"ssb",	"sqls":["select	LO_CUSTKEY,	count(1)	from	SSB.P_LINEORDER	GROUP	BY	LO_CUSTKEY1",	"S

ELECT	LO_SHIPPRIOTITY,count(1)	FROM	SSB.LINEORDER	GROUP	BY	LO_SHIPPRIOTITY"]}'

响应字段

	valid_sqls	，通过语法校验的	SQL，以及对应的可回答模型。如果无可回答模型，则	SQL	对应列表为空
	error_sqls	，无法通过语法校验的	SQL

895

模型	API

	error_sqls_detail	，无法通过语法校验	SQL	的详细信息

响应示例

{

				"code":	"000",

				"data":	{

								"valid_sqls":	{

												"SELECT	LO_SHIPPRIOTITY,count(1)	FROM	SSB.LINEORDER	GROUP	BY	LO_SHIPPRIOTITY":	[]

								},

								"error_sqls":	[

												"select	LO_CUSTKEY,	count(1)	from	SSB.P_LINEORDER	GROUP	BY	LO_CUSTKEY1"

								],

								"error_sqls_detail":	[

												{

																"sql":	"select	LO_CUSTKEY,	count(1)	from	SSB.P_LINEORDER	GROUP	BY	LO_CUSTKEY1",

																"sql_advices":	[

																				{

																								"suggestion":	"Can’t	find	column	\"LO_CUSTKEY1\".	Please	check	if	it	exists	in	the

source	table.	If	exists,	please	try	reloading	the	table;	if	not	exist,	please	contact	admin	to	add	it.",

																								"incapable_reason":	"Can’t	find	column	\"LO_CUSTKEY1\".	Please	check	if	it	exists	i

n	the	source	table.	If	exists,	please	try	reloading	the	table;	if	not	exist,	please	contact	admin	to	add	it

."

																				}

																]

												}

								]

				},

				"msg":	""

}

返回索引列表

根据给定的模型获取索引列表。

	GET	http://host:port/kylin/api/models/{model_name}/indexes

URL	Parameters

	project		-	 	必填		 	string	，项目名称
	model_name		-	 	必填		 	string	，模型名称
	status		-	 	可选		 	string	，索引状态，支持	 	NO_BUILD	,	 	BUILDING	,	 	LOCKED	,	 	ONLINE	，默认为空
	page_offset		-	 	可选		 	int	，分页页面，默认为	 	0	。
	page_size		-	 	可选		 	int	，分页大小，默认为	 	10	。
	sources		-	 	可选		 	string	，索引的类型，支持	 	RECOMMENDED_AGG_INDEX	,	 	RECOMMENDED_TABLE_INDEX	,
	CUSTOM_AGG_INDEX	,	 	CUSTOM_TABLE_INDEX	，默认值为空
	sort_by		-	 	可选		 	string	，排序字段，支持	 	last_modified,	usage	,	 	data_size	，默认值为	 	last_modified
	reverse		-	 	可选		 	boolean	，是否倒序排序，默认值为	 	true
	batch_index_ids		-	 	可选		 	array[long]	，指定索引Id，默认值为	 	空

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	'http://localhost:7070/kylin/api/models/m1/indexes?project=ssb&batch_index_ids=1,10001,20001'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

896

模型	API

响应字段

	absent_batch_index_ids	,	无法匹配的索引Id
	indexes	,	索引列表

	related_tables	,	该索引使用到的表

响应示例

{

				"code":	"000",

				"data":	{

								"project":	"ssb",

								"uuid":	"383cd655-89f4-4986-85cf-1d299e287e84",

								"model_name":	"m1",

								"total_size":	2,

								"offset":	0,

								"limit":	10,

								"owner":	"ADMIN",

								"absent_batch_index_ids":	[20001],

								"indexes":	[

												{

																"id":	1,

																"status":	"NO_BUILD",

																"source":	"CUSTOM_AGG_INDEX",

																"col_order":	[

																				{

																								"key":	"LINEORDER.LO_ORDERKEY",

																								"value":	"column",

																								"cardinality":	null

																				},

																				{

																								"key":	"LINEORDER.LO_LINENUMBER",

																								"value":	"column",

																								"cardinality":	null

																				},

																				{

																								"key":	"COUNT_ALL",

																								"value":	"measure",

																								"cardinality":	null

																				}

																],

																"shard_by_columns":	[],

																"sort_by_columns":	[],

																"data_size":	0,

																"usage":	0,

																"last_modified":	1610462519405,

																"related_tables":	["SSB.LINEORDER"],

																"storage_type":	20

												},

												{

																"id":	10001,

																"status":	"NO_BUILD",

																"source":	"CUSTOM_AGG_INDEX",

																"col_order":	[

																				{

																								"key":	"LINEORDER.LO_ORDERKEY",

																								"value":	"column",

																								"cardinality":	null

																				},

																				{

																								"key":	"COUNT_ALL",

																								"value":	"measure",

																								"cardinality":	null

																				}

																],

																"shard_by_columns":	[],

																"sort_by_columns":	[],

																"data_size":	0,

897

模型	API

																"usage":	0,

																"last_modified":	1610462519405,

																"related_tables":	["SSB.LINEORDER"],

																"storage_type":	20

												}

								]

				},

				"msg":	""

}

SQL	推荐模型

	POST	http://host:port/kylin/api/models/model_suggestion

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

HTTP	Body:	JSON	Object

	project		-	 	必填		 	string	，项目名称。
	sqls		-	 	必填		 	array	，用于推荐模型的查询。
	with_segment		-	 	optional		 	bool	，模型是否产生空的segment，默认是	true
	with_model_online		-	 	optional		 	bool	,	模型是否默认上线，默认是	false

Curl	请求示例

curl	-X	POST	\

		'http://localhost:7070/kylin/api/models/model_suggestion'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{"project":"ssb",	"sqls":["select	count(*)	from	ssb.P_LINEORDER",	"SELECT	1"]}'

响应字段

	models	,	推荐出的模型信息
	uuid	,	模型的	UUID
	alias	,	模型名称
	version	,	模型的版本
	rec_items	,	新创建的模型。请注意这里会将模型的相关信息，如维度度量等以建议的形态展示，并不会
真正地产生这样一条建议。

	sqls	,	建立该模型对应的	SQL	查询
	index_id	,	重用的索引	ID，-1	表示是新建模型没有重用索引
	dimensions	,	模型的维度， 	new		代表是否是新创建或者被重用
	measues	,	模型的度量， 	new		代表是否是新创建或者被重用
	computed_columns	,	模型的可计算列， 	new		代表是否是新创建或者被重用

	error_sqls	,	无法被推荐的	SQL	列表

响应示例

{

		"code":	"000",

		"data":	{

						"models":	[

										{

														"uuid":	"364e4485-433c-4fe2-be57-02c59170b5d4",

														"alias":	"AUTO_MODEL_P_LINEORDER_1",

														"version":	"4.0.0.0",

898

模型	API

														"rec_items":	[

																		{

																						"sqls":	[

																										"select	count(*)	from	ssb.P_LINEORDER"

																						],

																						"index_id":	-1,

																						"dimensions":	[],

																						"measures":	[

																										{

																														"measure":	{

																																		"name":	"COUNT_ALL",

																																		"function":	{

																																						"expression":	"COUNT",

																																						"parameters":	[

																																										{

																																														"type":	"constant",

																																														"value":	"1"

																																										}

																																						],

																																						"returntype":	"bigint"

																																		},

																																		"id":	100000

																														},

																														"new":	true

																										}

																						],

																						"computed_columns":	[]

																		}

														]

										}

						],

						"error_sqls":	[

										"SELECT	1"

						]

		},

		"msg":	""

}

模型优化

	POST	http://host:port/kylin/api/models/model_optimization

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

HTTP	Body:	JSON	Object

	project		-	 	必填		 	string	，项目名称。
	sqls		-	 	必填		 	array	，用于优化模型的查询
	accept_recommendation		-	 	可选		 	boolean	，默认值为	false，生成的建议会写入到建议列表。如果为	true，通过
API	调用生成的优化建议，会直接接受并生成索引
	discard_table_index		-	 	可选		 	boolean	,	是否不生成系统推荐明细索引或其优化建议，默认是	 	false	，表示生
成，当修改为	 	true		时，则不生成系统推荐明细索引或其优化建议

Curl	请求示例

curl	-X	POST	\

		'http://localhost:7070/kylin/api/models/model_optimization'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{"project":"ssb",	"sqls":["select	LO_CUSTKEY,	count(1)	from	SSB.P_LINEORDER	GROUP	BY	LO_CUSTKEY",	"se

899

模型	API

lect	LINEORDER.LO_ORDERKEY,LINEORDER.LO_CUSTKEY,COUNT(*)	FROM	SSB.LINEORDER	group	by	LINEORDER.LO_ORDERKEY,

LINEORDER.LO_CUSTKEY",	"SELECT	SELECT"]}'

响应字段

	models		,	被优化的模型信息

	alias	,	模型名称
	rec_items	,	优化建议的详细信息

	sqls	,	生成这条建议对应的	SQL	查询
	index_id	,	推荐出来的临时索引	ID
	dimensions	,	一条建议使用的所有维度信息
	measures	,	一条建议使用的所有度量
	computed_column	,	一条建议使用的所有可计算列
	discarded	,	这条建议是否不被生成， 	false		表示生成

	optimal_models	,	通过最优模型响应的信息

	uuid	,	模型的	UUID

	alias	,	模型名称

	version	,	模型的版本

	rec_items	,	查询响应的详细信息

	sqls	,	响应的	SQL	查询
	index_id	,	响应的索引	ID
	dimensions	,	响应查询的索引的所有维度信息
	measures	,	响应查询的索引的所有度量
	computed_columns	,	响应查询的所有可计算列

	error_sqls	,	无法被推荐的	SQL	列表

响应示例

{

						"code":	"000",

						"data":	{

										"models":	[

														{

																		"uuid":	"364e4485-433c-4fe2-be57-02c59170b5d4",

																		"alias":	"AUTO_MODEL_P_LINEORDER_1",

																		"version":	"4.0.0.0",

																		"rec_items":	[

																						{

																										"sqls":	[

																														"select	LO_CUSTKEY,	count(1)	from	SSB.P_LINEORDER	GROUP	BY	LO_CUSTKEY"

																										],

																										"index_id":	10001,

																										"dimensions":	[

																														{

																																		"dimension":	{

																																						"id":	1,

																																						"name":	"P_LINEORDER_0_DOT_0_LO_CUSTKEY",

																																						"column":	"P_LINEORDER.LO_CUSTKEY",

																																						"status":	"DIMENSION"

																																		},

																																		"dataType":	"integer",

																																		"new":	true

																														}

																										],

																										"measures":	[

																														{

900

模型	API

																																		"measure":	{

																																						"name":	"COUNT_ALL",

																																						"function":	{

																																										"expression":	"COUNT",

																																										"parameters":	[

																																														{

																																																		"type":	"constant",

																																																		"value":	"1"

																																														}

																																										],

																																										"returntype":	"bigint"

																																						},

																																						"id":	100000

																																		},

																																		"new":	false

																														}

																										],

																										"computed_columns":	[],

																										"discarded":	false

																						}

																		]

														}

										],

										"optimal_models":	[

										{

														"uuid":	"cbc54073-7bda-a613-4fe5-256c68a89973",

														"alias":	"test1",

														"version":	"4.0.0.0",

														"rec_items":	[

																		{

																						"sqls":	[

																										"select	LINEORDER.LO_ORDERKEY,LINEORDER.LO_CUSTKEY,COUNT(*)	FROM	SSB.LINEORDER	gr

oup	by	LINEORDER.LO_ORDERKEY,LINEORDER.LO_CUSTKEY"

																						],

																						"index_id":	20002,

																						"dimensions":	[

																										{

																														"dimension":	{

																																		"id":	16,

																																		"name":	"LO_CUSTKEY",

																																		"column":	"LINEORDER.LO_CUSTKEY",

																																		"status":	"DIMENSION"

																														},

																														"dataType":	"integer",

																														"new":	false

																										},

																										{

																														"dimension":	{

																																		"id":	0,

																																		"name":	"LO_ORDERKEY",

																																		"column":	"LINEORDER.LO_ORDERKEY",

																																		"status":	"DIMENSION"

																														},

																														"dataType":	"bigint",

																														"new":	false

																										}

																						],

																						"measures":	[

																										{

																														"measure":	{

																																		"name":	"COUNT_ALL",

																																		"function":	{

																																						"expression":	"COUNT",

																																						"parameters":	[

																																										{

																																														"type":	"constant",

																																														"value":	"1"

																																										}

																																						],

901

模型	API

																																						"returntype":	"bigint"

																																		},

																																		"column":	null,

																																		"comment":	null,

																																		"id":	100000,

																																		"type":	"NORMAL",

																																		"internal_ids":	[]

																														},

																														"new":	false

																										}

																						],

																						"computed_columns":	[]

																			}

																]

													}

										],

										"error_sqls":	[

														"SELECT	SELECT"

										]

						},

						"msg":	""

		}

SQL	加速

	POST	http://host:port/kylin/api/models/sql_acceleration

[!NOTE]

从	Kyligence	Enterprise	4.5.9.2	版本开始，API	请求路径中的	 	accelerate_sqls		变更为	 	sql_acceleration	。原
请求路径目前仍可兼容，但请及时更新到新路径，原请求路径以后可能随时废弃。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

HTTP	Body:	JSON	Object

	project		-	 	必填		 	string	，项目名称。
	sqls		-	 	必填		 	array	，用于优化模型的查询
	accept_recommendation		-	 	可选		 	boolean	，对于优化模型，	生成的建议是否会写入到建议列表。如果为	true，
通过	API	调用生成的优化建议，会直接接受并生成索引
	with_segment		-	 	可选		 	boolean	，对于创建的模型，是否产生空的segment，默认是	true
	with_model_online		-	 	可选		 	boolean	,	对于创建的模型，是否默认上线，默认是	false
	discard_table_index		-	 	可选		 	boolean	,	是否不生成系统推荐明细索引或其优化建议，默认是	 	false	，表示生
成，当修改为	 	true		时，则不生成系统推荐明细索引或其优化建议

Curl	请求示例

curl	-X	POST	\

		'http://localhost:7070/kylin/api/models/sql_acceleration'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{"project":"ssb",	"sqls":["select	count(*)	from	SSB.LINEORDER",	"select	LO_CUSTKEY,	count(1)	from	SSB

.P_LINEORDER	GROUP	BY	LO_CUSTKEY",	"SELECT	1"]}'

响应字段

	optimized_models		,	被优化的模型信息

902

模型	API

	alias	,	模型名称
	rec_items	,	优化建议的详细信息

	sqls	,	生成这条建议对应的	SQL	查询
	index_id	,	推荐出来的临时索引	ID
	dimensions	,	一条建议使用的所有维度信息
	measures	,	一条建议使用的所有度量
	computed_columns	,	一条建议使用的所有可计算列
	discarded	,	这条建议是否不被生成， 	false		表示生成

	created_models	,	推荐出的模型信息

	uuid	,	模型的	UUID
	alias	,	模型名称
	version	,	模型的版本
	rec_items	,	新创建的模型。请注意这里会将模型的相关信息，如维度度量等以建议的形态展示，并不会
真正地产生这样一条建议。

	sqls	,	建立该模型对应的	SQL	查询
	index_id	,	重用的索引	ID，-1	表示是新建模型没有重用索引
	dimensions	,	模型的维度， 	new		代表是否是新创建或者被重用
	measures	,	模型的度量， 	new		代表是否是新创建或者被重用
	computed_columns	,	模型的可计算列， 	new		代表是否是新创建或者被重用

	optimal_models	,	通过最优模型响应的信息

	uuid	,	模型的	UUID

	alias	,	模型名称

	version	,	模型的版本

	rec_items	,	查询响应的详细信息

	sqls	,	响应的	SQL	查询
	index_id	,	响应的索引	ID
	dimensions	,	响应查询的索引的所有维度信息
	measures	,	响应查询的索引的所有度量
	computed_columns	,	响应查询的所有可计算列

	error_sqls	,	无法被推荐的	SQL	列表

响应示例

{

						"code":	"000",

						"data":	{

										"optimized_models":	[

														{

																		"uuid":	"364e4485-433c-4fe2-be57-02c59170b5d4",

																		"alias":	"AUTO_MODEL_P_LINEORDER_1",

																		"version":	"4.0.0.0",

																		"rec_items":	[

																						{

																										"sqls":	[

																														"select	LO_CUSTKEY,	count(1)	from	SSB.P_LINEORDER	GROUP	BY	LO_CUSTKEY"

																										],

																										"index_id":	10001,

																										"dimensions":	[

																														{

																																		"dimension":	{

																																						"id":	1,

																																						"name":	"P_LINEORDER_0_DOT_0_LO_CUSTKEY",

																																						"column":	"P_LINEORDER.LO_CUSTKEY",

																																						"status":	"DIMENSION"

903

模型	API

																																		},

																																		"dataType":	"integer",

																																		"new":	true

																														}

																										],

																										"measures":	[

																														{

																																		"measure":	{

																																						"name":	"COUNT_ALL",

																																						"function":	{

																																										"expression":	"COUNT",

																																										"parameters":	[

																																														{

																																																		"type":	"constant",

																																																		"value":	"1"

																																														}

																																										],

																																										"returntype":	"bigint"

																																						},

																																						"id":	100000

																																		},

																																		"new":	false

																														}

																										],

																										"computed_columns":	[],

																										"discarded":	false

																						}

																		]

														}

										],

					"created_models":	[

												{

																"uuid":	"364e4485-433c-4fe2-be57-02c59170b5d4",

																"alias":	"AUTO_MODEL_LINEORDER_1",

																"version":	"4.0.0.0",

																"rec_items":	[

																				{

																								"sqls":	[

																												"select	count(*)	from	SSB.LINEORDER"

																								],

																								"index_id":	-1,

																								"dimensions":	[],

																								"measures":	[

																												{

																																"measure":	{

																																				"name":	"COUNT_ALL",

																																				"function":	{

																																								"expression":	"COUNT",

																																								"parameters":	[

																																												{

																																																"type":	"constant",

																																																"value":	"1"

																																												}

																																								],

																																								"returntype":	"bigint"

																																				},

																																				"id":	100000

																																},

																																"new":	true

																												}

																								],

																								"computed_columns":	[],

																								"discarded":	false

																				}

																]

												}

								],

									"optimal_models":[

												{

904

模型	API

																"uuid":"6731928e-0f6c-6a79-f430-9e2c938689de",

																"alias":"CONSTANT",

																"version":"4.0.0.0",

																"rec_items":[

																				{

																								"sqls":[

																												"select	1"

																								],

																								"index_id":-1,

																								"dimensions":[

																								],

																								"measures":[

																								],

																								"computed_columns":[

																								],

																								"discarded":	false

																				}

																]

												}

								],

										"error_sqls":	[

														"SELECT	SELECT"

										]

						},

						"msg":	""

		}

获取模型推荐建议

根据指定的模型名称，获取该模型的推荐建议。用户通过	SQL	查询一段时间之后，发现有部分	SQL	不是通过模
型应答，而是通过下压查询应答。Kylin	会根据这些下压查询的历史信息，推荐出对应的多条模型优化建议。通
过调用该	API，能够获取指定模型的优化建议。

	GET	http://host:port/kylin/api/models/{model_name}/recommendations

URL	Parameters

	model_name		-	 	必填		 	string	，模型名称。
	project		-	 	必填		 	string	，项目名称。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://host:port/kylin/api/models/ssb_test/recommendations?project=ssb'\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应字段

	layouts	,	所有的索引建议

	add	,	建议用来增加索引或者删除索引
	agg	,	推荐出来的建议是聚合索引还是明细索引
	item_id	,	建议的	ID

905

模型	API

	is_agg	,	与	agg	属性相同
	is_add	,	与	add	属性相同
	type	,	建议类型，包括	ADD_AGG_INDEX,	REMOVE_AGG_INDEX,	ADD_TABLE_INDEX,

REMOVE_TABLE_INDEX
	create_time	,	建议创建时间
	last_modified	,	建议的最后更新时间
	hit_count	,	推荐的建议在被使用的次数
	index_id	,	与建议相关的索引的	ID，如果	add	为真，则没有意义
	data_size	,	建议相关的索引的大小，如果	add	为真，则设置	-1，没有意义
	memo_info	,	建议的生成的备注信息，删除建议的原因存储在这个字段中

	size	,	所有索引建议的数量
	model_id	,	模型的	UUID
	project	,	项目名称

响应示例

	{

				"code":	"000",

				"data":	{

								"layouts":	[{

												"add":	true,

												"agg":	true,

												"item_id":	34,

												"is_agg":	true,

												"is_add":	true,

												"type":	"ADD_AGG_INDEX",

												"create_time":	1601027171262,

												"last_modified":	1601028480033,

												"hit_count":	20,

												"index_id":	0,

												"data_size":	-1,

												"memo_info":	{}

								},	{

												"add":	false,

												"agg":	true,

												"item_id":	35,

												"is_agg":	true,

												"is_add":	false,

												"type":	"REMOVE_AGG_INDEX",

												"create_time":	1601028374011,

												"last_modified":	1601028491121,

												"hit_count":	2,

												"index_id":	1,

												"data_size":	155219,

												"memo_info":	{

																"index_opt_reason":	"INCLUDED"

												}

								}],

								"size":	2,

								"model_id":	"931c95ba-a6c1-4d7e-8f30-b4599dae16ed",

								"project":	"ssb"

				},

				"msg":	""

}

批量通过模型推荐建议

批量接受指定模型的优化建议。接受优化建议的粒度时模型粒度，一个模型下的优化建议，要么全部接受，要不

全部不接受。

	PUT	http://host:port/kylin/api/models/recommendations/batch

HTTP	Body:	JSON	Object

906

模型	API

	project		-	 	必填		 	string	，项目名称。
	filter_by_models		-	 	必填		 	boolean		，是否以模型为单位批量通过建议，默认为	 	true		，仅通过	 	model_names
指定的模型下的优化建议；否则通过项目下所有模型建议。

	model_names		-	 	可选		 	array	，模型名称列表。
	discard_table_index		-	 	可选		 	boolean	,	是否不通过新增明细索引的优化建议,	默认是	 	false	，表示通过，当
修改为	 	true		时，则不通过新增明细索引的优化建议，这些建议仍然保留在建议列表。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	PUT	\

		'http://localhost:7070/kylin/api/models/recommendations/batch'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{

								"project":	"ssb",

								"filter_by_models":	true,

								"model_names":	["ssb_test"]

								}'

响应字段

project，项目名称
models，所涉及的模型列表及信息

uuid,	模型的	UUID
alias,	模型名称
added_indexes：通过的优化建议中被添加的索引的	ID
removed_indexes：通过的优化建议中被删除的索引的	ID

响应示例

{

	"code":	"000",

	"data":	{

			"project":	"ssb",

			"models":	[

				{

									"uuid":	"364e4485-433c-4fe2-be57-02c59170b5d4",

									"alias":	"ssb_test",

									"added_indexes":	[20001,30001],

									"removed_indexes":	[]

				}]

	},

	"msg":	""

}

删除模型

	DELETE	http://host:port/kylin/api/models/{model_name}

请求权限：MANAGEMENT	及以上权限

开始生效版本：4.2.0

URL	Parameters

907

模型	API

	model_name		-	 	必选		 	string	，模型名称

Request	Parameters

	project		-	 	必选		 	string	，项目名称

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	DELETE	\

'http://host:port/kylin/api/models/{model_name}?project=test'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	cn'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":"000",

				"data":"",

				"msg":""

}

导出TDS

GET	http://host:port/kylin/api/models/{model_name}/export

URL	Parameters

	model_name		-	 	必选		 	string	,	模型名
	project		-	 	必选		 	string	,	项目名
	export_as		-	 	必选		 	string	,	导出格式

	TABLEAU_ODBC_TDS		导出为	Tableau	TDS	并以	Kyligence	ODBC	作为数据源
	TABLEAU_CONNECTOR_TDS		导出为	Tableau	TDS	并以	Kyligence	Tableau	Connector	作为数据源

	element		-	 	string		 	可选		导出的模型元素

	AGG_INDEX_COL		(default)	只导出聚合组中的维度和度量
	AGG_INDEX_AND_TABLE_INDEX_COL		只导出聚合组和表索引中的维度和度量
	ALL_COLS		导出所有模型定义的维度和度量

	server_host		-	 	可选		 	string	,	导出的	Kyligence	数据源的	host，默认为当前请求的	host
	server_port		-	 	可选		 	string		,	导出的	Kyligence	数据源的	port，默认为当前请求的	port

HTTP	Header

Accept:application/vnd.apache.kylin-v4-public+json

Accept-Language:	cn

Content-Type:	application/json;charset=utf-8

Curl	Request	Example

curl	-X	GET	\

'http://localhost:7070/kylin/api/models/a3/export?project=test_project&export_as=TABLEAU_ODBC_TDS&element=A

GG_INDEX_COL&server_host=host&server_port=7080'	\

-H	'accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'authorization:	Basic	QURNSU46S1lMSU4='	\

908

模型	API

模型重命名

	PUT	http://host:port/kylin/api/models/{model_name}/name

开始生效版本：4.5.4

URL	Parameters

	model_name		-	 	必填		 	string	，模型名称。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

HTTP	Body:	JSON	Object

	project		-	 	必填		 	string	，项目名称。
	new_model_name		-	 	必填		 	string	，模型新名称。
	description		-	 	可选		 	string	，模型描述。

Curl	请求示例

curl	-X	PUT	\

'http://localhost:7070/kylin/api/models/sytest/name'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	cn'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'

-d	'{"project":"ssb",	"new_model_name":"testNewName"}'

响应示例

{

				"code":	"000",

				"data":	"",

				"msg":	""

}

模型上/下线

	PUT	http://host:port/kylin/api/models/{model_name}/status

请求权限：MANAGEMENT	及以上权限

开始生效版本：4.5.11

URL	Parameters

	model_name		-	 	必填		 	string	，模型名称

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

HTTP	Body:	JSON	Object

project	-	 	必填		 	string	，项目名称
status	-	 	必填		 	string	，上/下线字段（上线：ONLINE，下线：OFFLINE）

Curl	请求示例

909

模型	API

curl	-X	PUT	\

'http://localhost:7070/kylin/api/models/model_test1/status'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	cn'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'

-d	'{"project":	"pj01",	"status":	"OFFLINE"}'

响应示例

{

				"code":	"000",

				"data":	"",

				"msg":	""

}

失败响应示例

{

		"code":	"999",

		"data":	null,
		"msg":	"KE-010001002(项目名为空)：没有项目信息，请指定一个项目。",

		"stacktrace":	"KE-010001002(Empty	Project	Name)	\norg.apache.kylin.common.exception.KylinException:	KE-01
0001002(项目名为空)：没有项目信息，请指定一个项目。	...",
		"exception":	"KE-010001002(项目名为空)：没有项目信息，请指定一个项目。",

		"url":	"http://localhost:7070/kylin/api/models"

}

错误码（具体错误信息请以接口返回内容为准）

	KE-010001001	:	项目不存在
	KE-010001002	:	项目名为空
	KE-010000003	:	非法参数

根据用户权限导出TDS

	GET	http://host:port/kylin/api/models/bi_export

URL	Parameters

	model_name		-	 	必选		 	string	,	模型名

	project		-	 	必选		 	string	,	项目名

	export_as		-	 	必选		 	string	,	导出格式

	TABLEAU_ODBC_TDS		导出为	Tableau	TDS	并以	Kyligence	ODBC	作为数据源
	TABLEAU_CONNECTOR_TDS		导出为	Tableau	TDS	并以	Kyligence	Tableau	Connector	作为数据源

	element		-	 	string		 	可选		导出的模型元素

	AGG_INDEX_COL		(default)	导出用户有权限访问的聚合组中的维度和度量
	AGG_INDEX_AND_TABLE_INDEX_COL		导出用户有权限访问的聚合组和表索引中的维度和度量
	ALL_COLS		导出用户有权限访问的模型定义的维度和度量中
	CUSTOM_COLS		导出用户有权限访问的模型定义的维度和度量,	当使用该方式时，必须传入	 	dimensions	,
	measures		参数

	server_host		-	 	可选		 	string	,	导出的	Kyligence	数据源的	host，默认为当前请求的	host

	server_port		-	 	可选		 	string		,	导出的	Kyligence	数据源的	port，默认为当前请求的	port

910

模型	API

	dimensions		-	 	可选		 	string	,	导出的维度列表,	 	element=CUSTOM_COLS		参数才会生效,	集合格式为
	${table_alias}.${columnName1},${table_alias}.${columnName2}

	measures		-	 	可选		 	string	,	导出的度量列表,	 	element=CUSTOM_COLS		参数才会生效,	集合格式为
	${measureName1},${measureName2}

HTTP	Header

	Accept:application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	Request	Example

curl	-X	GET	\

		'http://{host}:{port}/kylin/api/models/bi_export?model_name={modelName}&project={project}&export_as=TABLEAU_O

DBC_TDS&server_host=localhost&server_port=8080&dimensions=CUSTOMER.C_NAME,CUSTOMER.CC_6,CUSTOMER.CC_7,CUSTOMER.

CC_9,LINEORDER_1.LO_CUSTKEY&measures=m_aa&element=CUSTOM_COLS'	\

		-H	'accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'authorization:	Basic	QURNSU46S1lMSU4='	\

失败响应示例(当模型所有列都无权限或者表关联列没有权限时)

{

				"code":	"999",

				"data":	null,

				"msg":	"KE-010002022(The	table	not	contains	unauthenticated	columns):Please	add	permissions	to	columns	in	t

he	table!",

				"stacktrace":	"KE-010002022(The	table	not	contains	unauthenticated	columns)	\norg.apache.kylin.common.excep

tion.KylinException:	KE-010002022(The	table	not	contains	unauthenticated	columns):Please	add	permissions	to	col
umns	in	the	table!8)...。",

				"exception":	"KE-010002022(The	table	not	contains	unauthenticated	columns):Please	add	permissions	to	column

s	in	the	table!",

				"url":	"http://159.27.81.165:7032/kylin/api/models/bi_export"

}

错误码（具体错误信息请以接口返回内容为准）

	KE-010002022	:	请向表中的列添加权限

成功响应示例	(导出为	tds	文件内容)

<?xml	version='1.0'	encoding='UTF-8'?>

<datasource	formatted-name="federated.0e6gjbn18cj0a41an9pi309itkyi"	inline="true"	source-platform="win"	version

="10.0">

				<connection	class="federated">

								<named-connections>

												<named-connection	caption="localhost"	name="genericodbc.11du78x0szfyb51b703es1ocv315">

																<connection	class="genericodbc"	dbname=""	odbc-connect-string-extras="PROJECT=KE_36166;CUBE=tes

t_model_3_cc"	odbc-dbms-name="MySQL"	odbc-driver="KyligenceODBCDriver"	odbc-dsn=""	odbc-suppress-connection-poo

ling=""	odbc-use-connection-pooling=""	port="8080"	schema="DEFAULT"	server="localhost"	username="ADMIN"/>

												</named-connection>

								</named-connections>

								<relation	join="inner"	type="join">

												<clause	type="join">

																<expression	op="=">

																				<expression	op="[CUSTOMER].[C_CUSTKEY]"/>

																				<expression	op="[CUSTOMER_1].[C_CUSTKEY]"/></expression>

												</clause>

												<relation	join="inner"	type="join">

																<clause	type="join">

																				<expression	op="=">

																								<expression	op="[CUSTOMER].[C_CUSTKEY]"/>

																								<expression	op="[LINEORDER_1].[LO_CUSTKEY]"/></expression>

																</clause>

																<relation	type="table"	connection="genericodbc.11du78x0szfyb51b703es1ocv315"	name="CUSTOMER"	ta

911

模型	API

ble="[SSB].[CUSTOMER]"/>

																<relation	type="table"	connection="genericodbc.11du78x0szfyb51b703es1ocv315"	name="LINEORDER_1"

	table="[SSB].[LINEORDER]"/></relation>

												<relation	type="table"	connection="genericodbc.11du78x0szfyb51b703es1ocv315"	name="CUSTOMER_1"	tabl

e="[SSB1].[CUSTOMER]"/></relation>

								<cols>

												<map	key="[LO_ORDERPRIOTITY]"	value="[LINEORDER_1].[LO_ORDERPRIOTITY]"/>

												<map	key="[C_ADDRESS	(CUSTOMER_1)]"	value="[CUSTOMER_1].[C_ADDRESS]"/>

												<map	key="[C_NAME	(CUSTOMER_1)]"	value="[CUSTOMER_1].[C_NAME]"/>

												<map	key="[C_REGION	(CUSTOMER_1)]"	value="[CUSTOMER_1].[C_REGION]"/>

												<map	key="[C_NATION	(CUSTOMER)]"	value="[CUSTOMER].[C_NATION]"/>

												<map	key="[C_CUSTKEY	(CUSTOMER)]"	value="[CUSTOMER].[C_CUSTKEY]"/>

												<map	key="[C_MKTSEGMENT	(CUSTOMER)]"	value="[CUSTOMER].[C_MKTSEGMENT]"/>

												<map	key="[LO_PARTKEY]"	value="[LINEORDER_1].[LO_PARTKEY]"/>

												<map	key="[C_CITY	(CUSTOMER)]"	value="[CUSTOMER].[C_CITY]"/>

												<map	key="[LO_LINENUMBER]"	value="[LINEORDER_1].[LO_LINENUMBER]"/>

												<map	key="[C_REGION	(CUSTOMER)]"	value="[CUSTOMER].[C_REGION]"/>

												<map	key="[LO_ORDERKEY]"	value="[LINEORDER_1].[LO_ORDERKEY]"/>

												<map	key="[C_PHONE	(CUSTOMER)]"	value="[CUSTOMER].[C_PHONE]"/>

												<map	key="[CC_10]"	value="[CUSTOMER].[CC_10]"/>

												<map	key="[C_ADDRESS	(CUSTOMER)]"	value="[CUSTOMER].[C_ADDRESS]"/>

												<map	key="[CC_4]"	value="[CUSTOMER].[CC_4]"/>

												<map	key="[LO_SHIPMODE]"	value="[LINEORDER_1].[LO_SHIPMODE]"/>

												<map	key="[C_CITY	(CUSTOMER_1)]"	value="[CUSTOMER_1].[C_CITY]"/>

												<map	key="[CC_6]"	value="[CUSTOMER].[CC_6]"/>

												<map	key="[C_NATION	(CUSTOMER_1)]"	value="[CUSTOMER_1].[C_NATION]"/>

												<map	key="[CC_5]"	value="[CUSTOMER].[CC_5]"/>

												<map	key="[C_PHONE	(CUSTOMER_1)]"	value="[CUSTOMER_1].[C_PHONE]"/>

												<map	key="[CC_7]"	value="[CUSTOMER].[CC_7]"/>

												<map	key="[CC_9]"	value="[CUSTOMER].[CC_9]"/>

												<map	key="[LO_QUANTITY]"	value="[LINEORDER_1].[LO_QUANTITY]"/>

												<map	key="[LO_SUPPLYCOST]"	value="[LINEORDER_1].[LO_SUPPLYCOST]"/>

												<map	key="[C_CUSTKEY	(CUSTOMER_1)]"	value="[CUSTOMER_1].[C_CUSTKEY]"/>

												<map	key="[LO_CUSTKEY]"	value="[LINEORDER_1].[LO_CUSTKEY]"/>

												<map	key="[LO_ORDTOTALPRICE]"	value="[LINEORDER_1].[LO_ORDTOTALPRICE]"/>

												<map	key="[C_NAME	(CUSTOMER)]"	value="[CUSTOMER].[C_NAME]"/>

												<map	key="[LO_COMMITDATE]"	value="[LINEORDER_1].[LO_COMMITDATE]"/>

												<map	key="[LO_EXTENDEDPRICE]"	value="[LINEORDER_1].[LO_EXTENDEDPRICE]"/>

												<map	key="[LO_REVENUE]"	value="[LINEORDER_1].[LO_REVENUE]"/>

												<map	key="[LO_DISCOUNT]"	value="[LINEORDER_1].[LO_DISCOUNT]"/>

												<map	key="[LO_SHIPPRIOTITY]"	value="[LINEORDER_1].[LO_SHIPPRIOTITY]"/>

												<map	key="[LO_SUPPKEY]"	value="[LINEORDER_1].[LO_SUPPKEY]"/>

												<map	key="[LO_TAX]"	value="[LINEORDER_1].[LO_TAX]"/>

												<map	key="[LO_ORDERDATE]"	value="[LINEORDER_1].[LO_ORDERDATE]"/>

												<map	key="[C_MKTSEGMENT	(CUSTOMER_1)]"	value="[CUSTOMER_1].[C_MKTSEGMENT]"/>

								</cols>

				</connection>

				<aliases	enabled="yes"/>

				<column	caption="LO_ORDERPRIOTITY"	datatype="string"	name="[LO_ORDERPRIOTITY]"	role="dimension"	type="nomin

al"	hidden="true"/>

				<column	caption="C_ADDRESS_CUSTOMER_1"	datatype="string"	name="[C_ADDRESS	(CUSTOMER_1)]"	role="dimension"	t

ype="nominal"	hidden="true"/>

				<column	caption="C_NAME_CUSTOMER_1"	datatype="string"	name="[C_NAME	(CUSTOMER_1)]"	role="dimension"	type="n

ominal"	hidden="true"/>

				<column	caption="C_REGION_CUSTOMER_1"	datatype="string"	name="[C_REGION	(CUSTOMER_1)]"	role="dimension"	typ

e="nominal"	hidden="true"/>

				<column	caption="C_NATION"	datatype="string"	name="[C_NATION	(CUSTOMER)]"	role="dimension"	type="nominal"	h

idden="true"/>

				<column	caption="C_CUSTKEY"	datatype="integer"	name="[C_CUSTKEY	(CUSTOMER)]"	role="dimension"	type="ordinal

"	hidden="true"/>

				<column	caption="C_MKTSEGMENT"	datatype="string"	name="[C_MKTSEGMENT	(CUSTOMER)]"	role="dimension"	type="no

minal"	hidden="true"/>

				<column	caption="LO_PARTKEY"	datatype="integer"	name="[LO_PARTKEY]"	role="dimension"	type="ordinal"	hidden=

"true"/>

				<column	caption="C_CITY"	datatype="string"	name="[C_CITY	(CUSTOMER)]"	role="dimension"	type="nominal"	hidde

n="true"/>

				<column	caption="LO_LINENUMBER"	datatype="integer"	name="[LO_LINENUMBER]"	role="dimension"	type="ordinal"	h

idden="true"/>

				<column	caption="C_REGION"	datatype="string"	name="[C_REGION	(CUSTOMER)]"	role="dimension"	type="nominal"	h

912

模型	API

idden="true"/>

				<column	caption="LO_ORDERKEY"	datatype="integer"	name="[LO_ORDERKEY]"	role="dimension"	type="ordinal"	hidde

n="true"/>

				<column	caption="C_PHONE"	datatype="string"	name="[C_PHONE	(CUSTOMER)]"	role="dimension"	type="nominal"	hid

den="true"/>

				<column	caption="CC_10"	datatype="integer"	name="[CC_10]"	role="dimension"	type="ordinal"	hidden="true"/>

				<column	caption="C_ADDRESS"	datatype="string"	name="[C_ADDRESS	(CUSTOMER)]"	role="dimension"	type="nominal"

	hidden="true"/>

				<column	caption="CC_4"	datatype="integer"	name="[CC_4]"	role="dimension"	type="ordinal"	hidden="true"/>

				<column	caption="LO_SHIPMODE"	datatype="string"	name="[LO_SHIPMODE]"	role="dimension"	type="nominal"	hidden

="true"/>

				<column	caption="C_CITY_CUSTOMER_1"	datatype="string"	name="[C_CITY	(CUSTOMER_1)]"	role="dimension"	type="n

ominal"	hidden="true"/>

				<column	caption="CC_6"	datatype="integer"	name="[CC_6]"	role="dimension"	type="ordinal"/>

				<column	caption="C_NATION_CUSTOMER_1"	datatype="string"	name="[C_NATION	(CUSTOMER_1)]"	role="dimension"	typ

e="nominal"	hidden="true"/>

				<column	caption="CC_5"	datatype="integer"	name="[CC_5]"	role="dimension"	type="ordinal"	hidden="true"/>

				<column	caption="C_PHONE_CUSTOMER_1"	datatype="string"	name="[C_PHONE	(CUSTOMER_1)]"	role="dimension"	type=

"nominal"	hidden="true"/>

				<column	caption="CC_7"	datatype="integer"	name="[CC_7]"	role="dimension"	type="ordinal"/>

				<column	caption="CC_9"	datatype="integer"	name="[CC_9]"	role="dimension"	type="ordinal"/>

				<column	caption="LO_QUANTITY"	datatype="integer"	name="[LO_QUANTITY]"	role="dimension"	type="ordinal"	hidde

n="true"/>

				<column	caption="LO_SUPPLYCOST"	datatype="integer"	name="[LO_SUPPLYCOST]"	role="dimension"	type="ordinal"	h

idden="true"/>

				<column	caption="C_CUSTKEY_CUSTOMER_1"	datatype="integer"	name="[C_CUSTKEY	(CUSTOMER_1)]"	role="dimension"

type="ordinal"	hidden="true"/>

				<column	caption="LO_CUSTKEY"	datatype="integer"	name="[LO_CUSTKEY]"	role="dimension"	type="ordinal"/>

				<column	caption="LO_ORDTOTALPRICE"	datatype="integer"	name="[LO_ORDTOTALPRICE]"	role="dimension"	type="ordi

nal"	hidden="true"/>

				<column	caption="C_NAME_1"	datatype="string"	name="[C_NAME	(CUSTOMER)]"	role="dimension"	type="nominal"/>

				<column	caption="LO_COMMITDATE"	datatype="date"	name="[LO_COMMITDATE]"	role="dimension"	type="ordinal"	hidd

en="true"/>

				<column	caption="LO_EXTENDEDPRICE"	datatype="integer"	name="[LO_EXTENDEDPRICE]"	role="dimension"	type="ordi

nal"	hidden="true"/>

				<column	caption="LO_REVENUE"	datatype="integer"	name="[LO_REVENUE]"	role="dimension"	type="ordinal"	hidden=

"true"/>

				<column	caption="LO_DISCOUNT"	datatype="integer"	name="[LO_DISCOUNT]"	role="dimension"	type="ordinal"	hidde

n="true"/>

				<column	caption="LO_SHIPPRIOTITY"	datatype="integer"	name="[LO_SHIPPRIOTITY]"	role="dimension"	type="ordina

l"	hidden="true"/>

				<column	caption="LO_SUPPKEY"	datatype="integer"	name="[LO_SUPPKEY]"	role="dimension"	type="ordinal"	hidden=

"true"/>

				<column	caption="LO_TAX"	datatype="integer"	name="[LO_TAX]"	role="dimension"	type="ordinal"	hidden="true"/>

				<column	caption="LO_ORDERDATE"	datatype="date"	name="[LO_ORDERDATE]"	role="dimension"	type="ordinal"	hidden

="true"/>

				<column	caption="C_MKTSEGMENT_CUSTOMER_1"	datatype="string"	name="[C_MKTSEGMENT	(CUSTOMER_1)]"	role="dimens

ion"	type="nominal"	hidden="true"/>

				<column	caption="COUNT_ALL"	datatype="integer"	name="[COUNT_ALL]"	role="measure"	type="quantitative"	hidden

="true">

								<calculation	class="tableau"	formula="COUNT(1)"/>

				</column>

				<column	caption=""	datatype="integer"	name="[m_aa]"	role="measure"	type="quantitative">

								<calculation	class="tableau"	formula="SUM([CC_4])"/>

				</column>

				<column	caption=""	datatype="integer"	name="[m_bb]"	role="measure"	type="quantitative"	hidden="true">

								<calculation	class="tableau"	formula="SUM([CC_5])"/>

				</column>

				<column	caption=""	datatype="integer"	name="[m_cc]"	role="measure"	type="quantitative"	hidden="true">

								<calculation	class="tableau"	formula="SUM([C_CUSTKEY	(CUSTOMER)])"/>

				</column>

				<column	caption=""	datatype="integer"	name="[m_dd]"	role="measure"	type="quantitative"	hidden="true">

								<calculation	class="tableau"	formula="SUM([CC_10])"/>

				</column>

				<drill-paths>

								<drill-path	name="[C_ADDRESS	(CUSTOMER)],	[C_NATION	(CUSTOMER)],	[CC_7]">

												<field>[C_ADDRESS	(CUSTOMER)]</field>

												<field>[C_NATION	(CUSTOMER)]</field>

												<field>[CC_7]</field>

913

模型	API

								</drill-path>

				</drill-paths>

				<semantic-values>
								<semantic-value	key="[Country].[Name]"	value="&quot;美国&quot;"/>

				</semantic-values>

</datasource>

添加聚合组

	PUT	http://host:port/kylin/api/index_plans/agg_groups

开始生效版本：4.6.8

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

HTTP	Body:	JSON	Object

	project		-	 	必填		 	string	，项目名称
	model		-	 	必填		 	string	，模型名称
	aggregation_groups		-	 	必填		 	JSON	Object[]	，聚合组数组信息，可添加多个聚合组

	dimensions		-	 	必填		 	array[string]	，维度数组，必须是	database.table	格式，添加的维度必须已经在模型
中添加为维度

	measures		-	 	可选		 	array[string]	，度量数组，添加的度量名称是在模型中定义的度量名称，大小写敏感
	mandatory_dims		-	 	可选		 	array[string]	，必需维度数组，聚合组生成的索引中必须包含的维度
	hierarchy_dims		-	 	可选		 	array[array[string]]	，层级维度数组，聚合组生成的索引中，能够按照层级关
系优化的维度，一组层级维度在一个数组中

	joint_dims		-	 	可选		 	array[array[string]]	，联合维度数组，聚合组生成的索引中必须同时包含的维度，
一组联合维度在一个数组中

注意：	 	mandatory_dims		、 	hierarchy_dims		、 	joint_dims		三者必须在	 	dimensions		中，且三者在
单个聚合组内同一维度仅能被设置一次。

	dim_cap		-	 	可选		 	int	，该聚合组的最大维度组合数，正整数

	global_dim_cap		-	 	可选		 	int	，当前请求的全局最大维度组合数，正整数，优先级	global_dim_cap	<	dim_cap
	restore_deleted_index		-	 	可选		 	boolean	，当聚合组生成的索引已经被删除，添加聚合组时是否要再次生成这
些索引，默认	 	false	，表示不生成

Curl	请求示例

curl	-X	PUT	\

'http://localhost:7070/kylin/api/index_plans/agg_groups'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	cn'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'

-d	'{"project":"ssb",

					"model":"testNewName",

					"aggregation_groups":[

								{

										"dimensions":[

														"CUSTOMER_DETAILS.IMei",

														"CUSTOMER_DETAILS.REGION",

														"CUSTOMER_DETAILS.BALANCE"

										],

										"measures":[

														"ME2"

										],

										"mandatory_dims":[

														"CUSTOMER_DETAILS.reGION"

914

模型	API

										],

										"hierarchy_dims":[

														[

																		"CUSTOMER_DETAILS.Imei"

														]

										],

											"joint_dims":[

														[

																		"CUSTOMER_DETAILS.BALANCE"

														]

										],

										"dim_cap":	4

								}

					],

					"global_dim_cap":3,

					"restore_deleted_index":false

}'

响应字段

code	-	string，响应码，返回值：000	（请求处理成功），	999（请求处理失败）
removed_layouts_size	-	删除的索引个数
added_layouts_size	-	添加的索引个数
recovered_layouts_size	-	生成的索引中已被删除的索引个数，当	restore_deleted_index	=	true，才会添加这些索引

响应示例

{

				"code":	"000",

				"data":	{

								"removed_layouts_size":	0,

								"added_layouts_size":	3,

								"recovered_layouts_size":	0

				},

				"msg":	""

}

批量删除索引

	DELETE	http://host:port/kylin/api/index_plans/index

开始生效版本：4.6.9

Request	Parameters

	project		-	 	必选		 	string	，项目名称
	model_name		-	 	必选		 	string	，模型名称
	index_ids		-	 	必选		 	long	，索引id，支持传多个，如：1,10001
	index_range		-	 	可选		 	string	，索引范畴，该参数仅在融合模型删除索引场景下生效，可传： 	BATCH	,
	STREAMING	,	 	HYBRID	，默认值为 	BATCH	， 	BATCH	：仅删除批模型索引， 	STREAMING	：仅删除流模型索
引， 	HYBRID	：删除批模型以及流模型索引

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	DELETE	\

'http://host:port/kylin/api/index_plans/index?project=test&model_name=test_model&index_ids=1,10001'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

915

模型	API

-H	'Accept-Language:	cn'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":"000",

				"data":"",

				"msg":""

}

克隆模型

	POST	http://host:port/kylin/api/models/{model_name}/clone

开始生效版本：4.6.20

URL	Parameters

	model_name		-	 	必填		 	string	，原模型名称

HTTP	Body:	JSON	Object

	project		-	 	必填		 	string	，项目名称
	new_model_name		-	 	必填		 	string	，新模型名称

Curl	请求示例

```sh	curl	-X	POST	\	'http://host:port/kylin/api/models/model_test_1/clone'	\	-H	'Accept:	application/vnd.apache.kylin-v4-

public+json'	\	-H	'Accept-Language:	cn'	\	-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\	-H	'Content-Type:

application/json;charset=utf-8'	\	-d	'{"project":"ssb",

	"new_model_name":"testNewName"

}'

响应示例

{

				"code":"000",

				"data":"",

				"msg":""

}

新增模型级自定义参数

	POST	http://host:port/kylin/api/models/config

开始生效版本：4.6.20.0

HTTP	Body:	JSON	Object

	project		-	 	必选		 	string	，项目名称
	model		-	 	必选		 	string	，模型名称
	custom_settings		-	 	必选		 	JSON{map<String:String>}	，模型级自定义参数，用户可以以键值对的形式输入需要
新增的自定义参数

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

916

模型	API

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	POST	\

'http://host:port/kylin/api/models/config'	\

	-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	cn'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'	\

-d	'{"project":"test",	"model":"test","custom_settings":{"kylin.engine.spark-conf.spark.executor.cores":1}}

响应示例

{

				"code":"000",

				"data":{

						"model":"a0377e64-61fd-16ac-5278-cc2ca3b51917",

						"alias":"test",

						"auto_merge_enabled":null,

						"auto_merge_time_ranges":null,

						"volatile_range":null,

						"retention_range":null,

						"config_last_modifier":"ADMIN",

						"config_last_modified":1704185123266,

						"override_props":{

										"kylin.engine.spark-conf.spark.executor.cores":"1"

						}},

				"msg":""

}

修改模型级自定义参数

	PUT	http://host:port/kylin/api/models/config

开始生效版本：4.6.20.0

HTTP	Body:	JSON	Object

	project		-	 	必选		 	string	，项目名称
	model		-	 	必选		 	string	，模型名称
	custom_settings		-	 	必选		 	JSON{map<String:String>}	，模型级自定义参数，用户可以以键值对的形式输入需要
修改的自定义参数

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	PUT	\

'http://host:port/kylin/api/models/config'	\

	-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	cn'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'	\

-d	'{"project":"test",	"model":"test","custom_settings":{"kylin.engine.spark-conf.spark.executor.cores":2}}

响应示例

917

模型	API

{

				"code":"000",

				"data":{

						"model":"a0377e64-61fd-16ac-5278-cc2ca3b51917",

						"alias":"test",

						"auto_merge_enabled":null,

						"auto_merge_time_ranges":null,

						"volatile_range":null,

						"retention_range":null,

						"config_last_modifier":"ADMIN",

						"config_last_modified":1704185123266,

						"override_props":{

										"kylin.engine.spark-conf.spark.executor.cores":"2"

						}},

				"msg":""

}

删除模型级自定义参数

	DELETE	http://host:port/kylin/api/models/config

开始生效版本：4.6.20.0

HTTP	Body:	JSON	Object

	project		-	 	必选		 	string	，项目名称
	model		-	 	必选		 	string	，模型名称
	delete_custom_settings		-	 	必选		 	Array<String>	，需要删除的参数名称

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	DELETE	\

'http://host:port/kylin/api/models/config'	\

	-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	cn'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'	\

-d	'{"project":"test",	"model":"test","delete_custom_settings":["kylin.engine.spark-conf.spark.executor.cor

es"]}

响应示例

{

				"code":"000",

				"data":{

						"model":"a0377e64-61fd-16ac-5278-cc2ca3b51917",

						"alias":"test",

						"auto_merge_enabled":null,

						"auto_merge_time_ranges":null,

						"volatile_range":null,

						"retention_range":null,

						"config_last_modifier":"ADMIN",

						"config_last_modified":1704185123266,

						"override_props":{

						}},

				"msg":""

}

918

模型	API

返回模型级自定义参数列表

	GET	http://host:port/kylin/api/models/config

开始生效版本：4.6.20.0

Request	Parameters

	project		-	 	必选		 	string	，项目名称
	model		-	 	必选		 	string	，模型名称

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

'http://host:port/kylin/api/models/config?project=test&model=test'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	cn'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

		"code":	"000",

		"data":	{

						"model":	"529c89ee-f8ee-3b9c-674d-f647ccce0073",

						"alias":	"test",

						"auto_merge_enabled":	true,

						"auto_merge_time_ranges":	[

										"WEEK"

						],

						"volatile_range":	{

										"volatile_range_number":	1,

										"volatile_range_enabled":	true,

										"volatile_range_type":	"HOUR"

						},

						"retention_range":	{

										"retention_range_number":	1,

										"retention_range_enabled":	true,

										"retention_range_type":	"DAY"

						},

						"config_last_modifier":	"ADMIN",

						"config_last_modified":	1703245885741,

						"override_props":	{

										"kylin.engine.spark-conf.spark.executor.cores":	"1"

						}

		},

		"msg":	""

}

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

919

模型	API

模型构建	API

提示：

1.	 请确保已阅读前面的访问及安全认证章节，了解如何在	REST	API	语句中添加认证信息。

2.	 在	Curl	命令行上，如果您访问的	URL	中含有	 	&		符号，请注意转义，比如在	URL	两端加上引号。

加载数据

	POST	http://host:port/kylin/api/models/{model_name}/segments

URL	Parameters

	model_name		-	 	必填		 	string	，模型名称。

HTTP	Body:	JSON	Object

	project		-	 	必填		 	string	，项目名称。
	start		-	 	选填		 	string	，模型全量构建时，无需填写，模型增量构建时必填。Segment	开始时间（存在时间分
区列），时间戳类型，毫秒，值必须大于0，例如	 	694195200000		代表	 	1992-01-01	00:00:00	。
	end		-	 	选填		 	string	，模型全量构建时，无需填写，模型增量构建时必填。Segment	结束时间（存在时间分区
列），时间戳类型，毫秒，值必须大于0，例如	 	883584000000		代表	 	1998-01-01	00:00:00	。
	build_all_indexes		-	 	选填		 	boolean	，是否在对应	Segment	区间中构建所有索引，默认为	 	true
	sub_partition_values		-	 	选填		 	Array		，子分区值，用于多级分区模型，默认为空。对多级分区模型，当
	build_all_indexes		为 	true	时（需要构建所有索引），该值必填，当	 	build_all_indexes	为 	false	时（创建
空	Segment），该值需为空。
	priority		-	 	选填		 	int	，设置任务优先级，范围为	 	0-4	，优先级依次从高到低，默认为 	3
	build_all_sub_partitions		-	 	选填		 	boolean	，对于多级分区模型，是否构建所有分区值，默认为 	false
	yarn_queue		-	 	选填		 	string	，指定该任务使用的	YARN	队列，在系统级别或项目级别设置参数后使用：
kylin.engine-yarn.queue.in.task.enabled（是否允许为任务指定	YARN	队列，默认	false	不开启，true	代表开
启）、kylin.engine-yarn.queue.in.task.available（可供设置的	YARN	队列，多个队列时用英文逗号分隔）。
	tag		-	 	选填		 	object	，任务标记，如果填入此值，在调用	返回任务列表	接口，返回该任务时会将此字段原样
返回，可用于系统集成时，对任务进行标记并进行相应处理。字段值最大限制	默认	1024	KB，由配置
kylin.job.tag-max-size=1024	指定。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	POST	\

		'http://localhost:7070/kylin/api/models/SSB_LINEORDER/segments'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{"project":"doc_expert",	"start":	"694195200000",	"end":	"883584000000","build_all_indexes":true,"sub

_partition_values":[["1"],["2"]],"build_all_sub_partitions":false}'

响应示例

		{

						"code":	"000",

						"data":	{

920

模型	API

										"jobs":	[

														{

																		"job_name":	"INC_BUILD",

																		"job_id":	"61f4d697-e648-4ace-8e52-155829417b2a"

														},

														{

																		"job_name":	"INDEX_BUILD",

																		"job_id":	"0217b970-4525-468b-ba25-58bbb168d612"

														}

										]

						},

						"msg":	""

		}

加载索引文件	Gluten	缓存

	POST	http://host:port/kylin/api/index/gluten_cache

HTTP	Body:	JSON	Object

	project		-	 	必填		 	string	，项目名称。
	model		-	 	必填		 	string	，模型名称。
	indexes		-	 	选填		 	array[string]	，需要缓存的索引文件列表。只对储存类型是	 	V3		的模型有效。如果未制
定，则缓存所有索引文件。

	start		-	 	选填		 	string	，开始时间。只对储存类型是	 	V1		的模型有效。Segment	开始时间（存在时间分区
列），时间戳类型，毫秒，值必须大于0，例如	 	694195200000		代表	 	1992-01-01	00:00:00	。
	end		-	 	选填		 	string	，结束时间。只对储存类型是	 	V1		的模型有效。Segment	结束时间（存在时间分区
列），时间戳类型，毫秒，值必须大于0，例如	 	883584000000		代表	 	1998-01-01	00:00:00	。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

Curl	Request	Example

```sh	curl	-X	POST	'http://localhost:7070/kylin/api/index/gluten_cache'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	en'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-d	'{"project":	"test",	"model":	"test",	"indexes":	[],	"start":"694368000000",	"end":"694468000000"	}`

Response	Example

{

	"code":	"000",

	"data":	"",

	"msg":	""

}

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

921

模型	API

模型导入导出	API

提示：

1.	 请确保已阅读前面的访问及安全认证章节，了解如何在	REST	API	语句中添加认证信息。

2.	 在	Curl	命令行上，如果您访问的	URL	中含有	 	&		符号，请注意转义，比如在	URL	两端加上引号。

获取批量可导出的模型

	GET	http://host:port/kylin/api/metastore/previews/models?project=test&model_names=model1,model2

URL	Parameters

	project		-	 	required		 	string	，项目名称。
	model_names		-	 	optional		 	array[string]	,	模型名称,	使用逗号分割。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	--location	--request	GET	'http://localhost:7070/kylin/api/metastore/previews/models?project=target_pro

ject&model_names=model_index'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	cn'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'

响应示例

Field	description
	code		-	 	string	,	 	000		代表请求正常处理,	 	999		请求不合法。

	data		-	 	json	,	return	data

	uuid		-	 	string		uuid;
	name		-	 	string	模型名;
	status		-	 	string	模型的状态;
	has_recommendations		-	 	boolean		模型是否有优化建议;
	has_override_props		-	 	boolean		模型是否有参数重写设置;
	has_multiple_partition_values		-	 	boolean		模型是否存在多级分区;

		{

						"code":	"000",

						"data":	[

										{

														"uuid":	"10d5eb7c-d854-4f72-9e4b-9b1f3c65bcda",

														"name":	"model_index",

														"status":	"ONLINE",

														"has_recommendations":	true,

														"has_override_props":	true,

														"has_multiple_partition_values":	true,

														"tables":	[

																		{

																						"name":	"SSB.P_LINEORDER",

																						"kind":	"FACT"

																		},

922

模型	API

																		{

																						"name":	"SSB.CUSTOMER",

																						"kind":	"LOOKUP"

																		}

														]

										}

						],

						"msg":	""

		}

注意：只有可导出的模型，可以通过此	API	返回，broken	的模型不会被返回，即使请求参数中指定此模型。

模型元数据导出

	POST	http://host:port/kylin/api/metastore/backup/models?project=test

URL	Parameters

	project		-	 	required		 	string	，项目名称。

HTTP	Body:	JSON	Object

	names		-	 	必填		 	array[string]	，模型名称列表。
	export_recommendations		-	 	选填		 	boolean	，true/false，默认	false，是否导出模型的优化建议。
	export_over_props		-	 	选填		 	boolean	，true/false，默认	false，是否导出模型的重写配置。
	export_multiple_partition_values		-	 	选填		 	boolean	，true/false，默认	false，是否导出模型的多级分区值。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	--remote-name	--remote-header-name	--location	--request	POST	'http://localhost:7070/kylin/api/metastor

e/backup/models?project=original_project'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	cn'	\

-H	'Content-Type:	application/json;charset=utf-8'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

--data	'{

				"names":	[

								"ssb_model"

				],

				"export_recommendations":	true,

				"export_over_props":	true,

				"export_multiple_partition_values":	true

}'

响应示例

成功时返回	zip	文件

注意：remote-header-name	参数在	curl	7.20.0	及以上版本可用。

模型元数据导入校验

	POST	http://host:port/kylin/api/metastore/validation/models?project=test

URL	Parameters

	project		-	 	required		 	string	，项目名称。

923

模型	API

HTTP	Body:	form-data

	file		-	 	必填		 	MultipartFile	，模型元数据文件包。

[!NOTE]

如果对模型的元数据文件包执行了修改或重命名操作，可能导致校验失败。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

Curl	请求示例

curl	--location	--request	POST	'http://localhost:7070/kylin/api/metastore/validation/models?project=origina

l_project'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	cn'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

--form	'file=@metadata.zip'

响应示例

{

				"code":	"000",

				"data":	{

								"models":	{

												"ssb_model":	{

																"differences":	3,

																"missing_items":	[],

																"new_items":	[],

																"update_items":	[],

																"reduce_items":	[

																				{

																								"reason":	null,

																								"attributes":	{

																												"name":	"LO_SUPPLYCOST",

																												"alias_dot_column":	"P_LINEORDER.LO_SUPPLYCOST"

																								},

																								"detail":	"LO_SUPPLYCOST",

																								"type":	"MODEL_DIMENSION",

																								"model_alias":	"ssb_model",

																								"importable":	true,

																								"creatable":	true,

																								"overwritable":	true

																				},

																				{

																								"reason":	null,

																								"attributes":	{

																												"col_orders":	[

																																"P_LINEORDER.LO_CUSTKEY",

																																"P_LINEORDER.LO_DISCOUNT",

																																"P_LINEORDER.LO_LINENUMBER",

																																"P_LINEORDER.LO_ORDERDATE",

																																"P_LINEORDER.LO_ORDERKEY",

																																"P_LINEORDER.LO_PARTKEY",

																																"P_LINEORDER.LO_QUANTITY",

																																"P_LINEORDER.LO_SUPPKEY",

																																"P_LINEORDER.LO_SUPPLYCOST"

																												]

																								},

																								"detail":	"20000050001",

																								"type":	"WHITE_LIST_INDEX",

																								"model_alias":	"ssb_model",

																								"importable":	true,

																								"creatable":	true,

924

模型	API

																								"overwritable":	true

																				},

																				{

																								"reason":	null,

																								"attributes":	{

																												"col_orders":	[

																																"P_LINEORDER.LO_CUSTKEY",

																																"P_LINEORDER.LO_QUANTITY",

																																"P_LINEORDER.LO_SUPPKEY",

																																"LO_SUPPKEY_SUM",

																																"COUNT_ALL"

																												]

																								},

																								"detail":	"180001",

																								"type":	"WHITE_LIST_INDEX",

																								"model_alias":	"ssb_model",

																								"importable":	true,

																								"creatable":	true,

																								"overwritable":	true

																				}

																],

																"importable":	true,

																"overwritable":	true,

																"creatable":	true

												}

								}

				},

				"msg":	""

}

返回值描述：

	code		-	 	string	， 	000		代表请求正常处理,	 	999		请求不合法。

	data		-	 	json

	models		-	 	array[object]	,	模型列表，包含每个模型检测的结果

	key		-	 	string	,	模型名

	differences		-	 	int	,	当前zip文件中的模型和目标项目的元数据差异总数
	missing_items		-	 	array[object]	,	导入的模型需要的表或列，但是目标项目不存在
	new_items		-	 	array[object]	,	相较于目标项目新增的元数据
	reduce_items		-	 	array[object]	,	相较于目标项目减少的元数据
	update_items		-	 	array[object]	,	相较于目标项目更新的元数据
	has_same_name		-	 	boolean	,	是否有同名模型
	importable		-	 	boolean	,	是否允许导入
	overwritable		-	 	boolean	,	是否允许覆盖现有模型
	creatable		-	 	boolean	,	是否能够新建模型

模型元数据导入

	POST	http://host:port/kylin/api/metastore/import/models?project=test

URL	Parameters

	project		-	 	required		 	string	，项目名称。

HTTP	Body:	form-data

	file		-	 	必填		 	MultipartFile	，模型元数据文件包。

	request		-	 	必填		 	MultipartFile	，json文件。request的文件内容如下

{

				"models":[

925

模型	API

								{

												"original_name":"ssb_model",

												"target_name":"ssb_model",

												"import_type":"OVERWRITE"

								}

				]

}

	original_name		- 	string		模型名称
	target_name		- 	string		模型名称，新建后的模型名称，只在	import_type	为	NEW	时起作用
	import_type		- 	string		可选值为NEW、OVERWRITE、UN_IMPORT，分别表示新建模型，覆盖现有模
型，和不导入

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

Curl	请求示例

curl	--location	--request	POST	'http://localhost:7070/kylin/api/metastore/import/models?project=original_pr

oject'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	cn'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

--form	'file=@metadata.zip;type=application/octet-stream'	\

--form	'request=@request.json;type=application/json'

响应示例

{

						"code":"000",

						"data":"",

						"msg":""

}

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

926

模型	API

多级分区模型	API

提示：

1.	 请确保已阅读前面的访问及安全认证章节，了解如何在	REST	API	语句中添加认证信息。

2.	 在	Curl	命令行上，如果您访问的	URL	中含有	 	&		符号，请注意转义，比如在	URL	两端加上引号。

前提条件

开启多级分区

设置分区列

多级分区模型设置分区列请直接参考	设置分区列。

添加子分区值

可以	加载数据	时通过直接指定	 	sub_partition_values		添加或者使用以下API

	POST	http://host:port/kylin/api/models/{model_name}/segments/multi_partition/sub_partition_values

URL	Parameters

	model_name		-	 	必填		 	string	，模型名称。

HTTP	Body:	JSON	Object

	project		-	 	必填		 	string	，项目名称。

	sub_partition_values		-	 	必填		 	array	，构建子分区的值。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	POST	\

		http://host:port/kylin/api/models/multi_level_partition/segments/multi_partition/sub_partition_values	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{

				"project":"multi_level_partition",

				"sub_partition_values":[["5"]]

}'

响应示例

		{

			"code":	"000",

			"data":	"",

			"msg":	""

		}

927

模型	API

加载数据

多级分区模型构建请直接参考	加载数据	API。

构建子分区

	POST	http://host:port/kylin/api/models/{model_name}/segments/multi_partition

URL	Parameters

	model_name		-	 	必填		 	string	，模型名称。

HTTP	Body:	JSON	Object

	project		-	 	必填		 	string	，项目名称。

	segment_id		-	 	必填		 	string	，Segment	id。

	sub_partition_values		-	 	必填		 	array	，构建子分区的值。

	parallel_build_by_segment		-	 	选填		 	boolean	，	是否并发构建，默认为	 	false	。

	build_all_sub_partitions		-	 	选填		 	boolean	，	是否构建所有已存在子分区值，默认为	 	false	。

	yarn_queue		-	 	选填		 	string	，指定该任务使用的	YARN	队列，在系统级别或项目级别设置参数后使用：
kylin.engine-yarn.queue.in.task.enabled（是否允许为任务指定	YARN	队列，默认	false	不开启，true	代表开
启）、kylin.engine-yarn.queue.in.task.available（可供设置的	YARN	队列，多个队列时用英文逗号分隔）。

	tag		-	 	选填		 	object	，任务标记，如果填入此值，在调用	返回任务列表	接口，返回该任务时会将此字段原样
返回，可用于系统集成时，对任务进行标记并进行相应处理。字段值最大限制	默认	1024	KB，由配置
kylin.job.tag-max-size=1024	指定。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	POST	\

		http://host:port/kylin/api/models/multi_partition_model/segments/multi_partition	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json'	\

		-d	'{

				"project":	"multi_partition_project",

				"segment_id":	"983904fa-d573-4944-acb8-558c59598a48",

				"sub_partition_values":	[

								[

												"5"

								]

				],

				"parallel_build_by_segment":	false,

				"build_all_sub_partitions":	false

}'

响应示例

{

				"code":	"000",

				"data":	{

								"jobs":	[

928

模型	API

												{

																"job_name":	"SUB_PARTITION_BUILD",

																"job_id":	"0282e2c9-63e3-46b0-85f6-6e74ca5bf984"

												}

								]

				},

				"msg":	""

}

删除子分区值对应的构建数据

	DELETE	http://host:port/kylin/api/models/segments/multi_partition

URL	Parameters

	project		-	 	必填		 	string	，项目名称。

	model		-	 	必填		 	string	，模型名称。

	segment_id		-	 	必填		 	string	,	Segement	Id.

	sub_partition_values		-	 	必填		 	string	,	子分区值.

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	DELETE	\

		'http://host:port/kylin/api/models/segments/multi_partition?project=multi_partition_project&model=multi_p

artition_model&segment_id=ff839b0b-2c23-4420-b332-0df70e36c343&sub_partition_values=0,1'	\

		-H	'accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

响应示例

{

				"code":	"000",

				"data":	"",

				"msg":	""

}

刷新子分区值对应的构建数据

	PUT	http://host:port/kylin/api/models/{model_name}/segments/multi_partition

URL	Parameters

	model_name		-	 	必填		 	string	，模型名称。

HTTP	Body:	JSON	Object

	project		-	 	必填		 	string	，项目名称。

	segment_id		-	 	必填		 	string	，Segment	id。

	sub_partition_values		-	 	必填		 	array	，子分区值数组。

929

模型	API

	yarn_queue		-	 	选填		 	string	，指定该任务使用的	YARN	队列，在系统级别或项目级别设置参数后使用：
kylin.engine-yarn.queue.in.task.enabled（是否允许为任务指定	YARN	队列，默认	false	不开启，true	代表开
启）、kylin.engine-yarn.queue.in.task.available（可供设置的	YARN	队列，多个队列时用英文逗号分隔）。

	tag		-	 	选填		 	object	，任务标记，如果填入此值，在调用	返回任务列表	接口，返回该任务时会将此字段原样
返回，可用于系统集成时，对任务进行标记并进行相应处理。字段值最大限制	默认	1024	KB，由配置
kylin.job.tag-max-size=1024	指定。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	PUT	\

		http://host:port/kylin/api/models/SSB_LINEORDER/segments/multi_partition	\

		-H	'accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{"project":"default","segment_id":"60615c5e-2ae1-4ee9-b88d-f00f1f101a8a","sub_partition_values":[["1"

],	["2"]]}'

响应示例

{

				"code":	"000",

				"data":	{

								"jobs":	[

												{

																"job_name":	"SUB_PARTITION_REFRESH",

																"job_id":	"4fa1a0a1-6a97-4be9-bdf6-8957c5f80114"

												}

								]

				},

				"msg":	""

}

获取	Segment	列表

多级分区模型获取	Segment	请直接参考	获取	Segment	列表。

获取	Segment	分区详情

	GET	http://host:port/kylin/api/models/{model_name}/segments/multi_partition

URL	Parameters

	project		-	 	必填		 	string	，项目名称。

	segment_id		-	 	必填		 	string	，需要查看的	Segment	Id。

	page_offset		-	 	选填		 	int	，分页页面，默认为	0。

	page_size		-	 	选填		 	int	，分页大小，默认为	10。

	model_name		-	 	必选	，模型名称。

HTTP	Header

930

模型	API

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

	'http://host:port/kylin/api/models/multi_partition_model/segments/multi_partition?project=multi_partition_

project&segment_id=ffdfc037-7c63-4499-986d-9b680276161e'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	cn'	\

-H	'Authorization:	Basic	QURNSU46a3lsaW5AMjAxOQ=='	\

-H	'Content-Type:	application/json;charset=utf-8'	\

响应示例

{

				"code":	"000",

				"data":	{

								"value":	[

												{

																"id":	2,

																"values":	[

																				"3"

																],

																"status":	"ONLINE",

																"last_modified_time":	1609213843048,

																"source_count":	0,

																"bytes_size":	3747

												},

												{

																"id":	3,

																"values":	[

																				"4"

																],

																"status":	"ONLINE",

																"last_modified_time":	1609213843048,

																"source_count":	0,

																"bytes_size":	3747

												}

								],

								"offset":	0,

								"limit":	10,

								"total_size":	2

				},

				"msg":	""

}

查询映射设置

	PUT	http://host:port/kylin/api/models/{model_name}/multi_partition/mapping

URL	Parameters

	model_name		-	 	必选	，模型名称

HTTP	Body:	JSON	Object

	project		-	 	必填		 	string	，项目名称。

	alias_columns		-	 	必选	， 	array<string>	,	多级分区列需要mapping到的对应列名

	multi_partition_columns		-	 	必选	， 	array<string>	，多级分区列名

	value_mapping		-	 	必选	， 	array<object>	，分区值映射

931

模型	API

	origin		-	 	必选	， 	array<string>	，子分区列值

	target		-	 	必选	,	 	array<string>	，子分区列值映射值

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	PUT	\

		http://host:port/kylin/api/models/test_multi/multi_partition/mapping	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46a3lsaW5AMjAxOQ=='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{

				"project":	"multi_partition_project",

				"alias_columns":	["KYLIN_SALES.LEAF_CATEG_ID"],

				"multi_partition_columns":	["KYLIN_SALES.LSTG_SITE_ID"],

				"value_mapping":	[

						{

								"origin":	["Beijing"],

								"target":["North"]

						},

						{

								"origin":["Shanghai"],

								"target":["South"]

						}

				]

}'

响应示例

{

				"code":	"000",

				"data":	"",

				"msg":	""

}

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

932

模型	API

逻辑视图（Logical	View）	API

提示：

1.	 请确保已阅读前面的访问及安全认证章节，了解如何在	REST	API	语句中添加认证信息。

2.	 在	Curl	命令行上，如果您访问的	URL	中含有	 	&		符号，请注意转义，比如在	URL	两端加上引号。

逻辑视图	DDL

	POST	http://host:port/kylin/api/logical_view/ddl

HTTP	Body:	JSON	Object

	project		-	 	必填		 	string	，项目名称。
	restrict		-	 	可选		 	string	，创建/删除逻辑视图使用： 	logic		，修改逻辑视图使用： 	replaceLogicalView	，默
认值为	 	logic	。
	sql		-	 	必填		 	string	，逻辑视图	DDL	SQL。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	POST	'http://localhost:7070/kylin/api/logical_view/ddl'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{"project":	"demo",	"restrict":	"logic",	"sql":	"create	logical	view	logical_view_name	as	select	*	fr

om	SSB.PART"}'

响应示例

		{

						"code":	"000",

						"data":	"",

						"msg":	""

		}

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

933

Segment	管理	API

Segment	管理	API

提示：

1.	 请确保已阅读前面的访问及安全认证章节，了解如何在	REST	API	语句中添加认证信息。

2.	 在	Curl	命令行上，如果您访问的	URL	中含有	 	&		符号，请注意转义，比如在	URL	两端加上引号。

获取	Segment	列表

获取指定模型的	Segment	列表。调用“	指定	Segment	补全索引	”API	之后，通过监控指定模型的	Segment	列表，来
判断	Segment	是否已经构建完成。

	GET	http://host:port/kylin/api/models/{model_name}/segments

URL	Parameters

	model_name		-	 	必填		 	string	，模型名称。
	project		-	 	必填		 	string	，项目名称。
	page_offset		-	 	选填		 	int	，分页页面，默认为	 	0	。
	page_size		-	 	选填		 	int	，分页大小，默认为	 	10	。
	start		-	 	选填		 	string	，Segments	开始时间，默认为	 	1	,	时间戳类型，毫秒，值必须大于0。
	end		-	 	选填		 	string	，Segments	结束时间，默认为 	9223372036854775806	，时间戳类型，毫秒，值必须大于
0。
	statuses		-	 	选填		 	string	，Segments	状态，可选值为
	ONLINE	， 	LOCKED	， 	REFRESHING	， 	MERGING	， 	LOADING	， 	WARNING	，多个值之间用逗号分隔。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://localhost:7070/kylin/api/models/SSB_LINEORDER/segments?project=doc_expert'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":	"000",

				"data":	{

								"value":	[

												{

																"id":	"99c547b7-1bc1-4b57-b62a-127c080e1fd2",

																"name":	"20120101000000_20130101000000",

																"create_time_utc":	1609209524110,

																"status":	"READY",

																"segRange":	{

																				"@class":	"org.apache.kylin.metadata.model.SegmentRange$TimePartitionedSegmentRange",

																				"date_range_start":	1325347200000,

																				"date_range_end":	1356969600000

																},

																"timeRange":	null,

934

Segment	管理	API

																"parameters":	null,

																"dictionaries":	null,

																"snapshots":	null,

																"last_build_time":	1609209642839,

																"source_count":	2,

																"source_bytes_size":	798009,

																"column_source_bytes":	{},

																"ori_snapshot_size":	{},

																"additionalInfo":	{

																				"segment_path":	"hdfs://nameservice1/kylin/jrc_kylin/multi_partition/parquet/d5b94380-f

84f-481f-b4bb-ffa3f6b3b391/99c547b7-1bc1-4b57-b62a-127c080e1fd2",

																				"file_count":	"14"

																},

																"is_encoding_data_skew":	false,

																"is_snapshot_ready":	false,

																"is_dict_ready":	false,

																"is_flat_table_ready":	false,

																"is_fact_view_ready":	false,

																"multi_partitions":	[],

																"max_bucket_id":	13,

																"bytes_size":	12520,

																"hit_count":	0,

																"status_to_display":	"ONLINE",

																"index_count":	7,

																"index_count_total":	7,

																"multi_partition_count":	2,

																"multi_partition_count_total":	2,

																"row_count":	13,

																"second_storage_nodes":[

																				{

																								"name":"sandbox.hortonworks.com",

																								"ip":"10.1.2.55",

																								"port":9500

																				}

																],

																"second_storage_size":12989,

																"has_base_table_index":true,

																"has_base_agg_index":true,

																"has_base_table_index_data":true,

																"last_modified_time":	1609209642839

												}

								],

								"offset":	0,

								"limit":	10,

								"total_size":	1

				},

				"msg":	""

}

刷新/合并	Segment

刷新或者合并多个连续的	Segment。当索引发生变更时，可以刷新	Segment，来更新索引数据；当存在多个连续
的小	Segment	时，通过合并成一个大	Segment，能够减少小文件，提升查询性能。

	PUT	http://host:port/kylin/api/models/{model_name}/segments

URL	Parameters

	model_name		-	 	必填		 	string	，模型名称。

HTTP	Body:	JSON	Object

	project		-	 	必填		 	string	，项目名称。
	type		-	 	选填		 	string	，	刷新	Segments	或合并多个连续的	Segments，可选值为	 	REFRESH	， 	MERGE	，默认值为
	REFRESH		。
	ids		-	 	选填		 	array[string]	，Segment	id	列表。

935

Segment	管理	API

	names		-	 	选填		 	array[string]	，Segment	name	列表。

注意：	 	ids		和	 	names		必须设置一个，不能两者都设置或两者都为空。

	priority		-	 	选填		 	integer	，设置任务优先级，范围为	 	0-4	，优先级依次从高到低，默认为 	3
	yarn_queue		-	 	选填		 	string	，指定该任务使用的	YARN	队列，在系统级别或项目级别设置参数后使用：
kylin.engine-yarn.queue.in.task.enabled（是否允许为任务指定	YARN	队列，默认	false	不开启，true	代表开
启）、kylin.engine-yarn.queue.in.task.available（可供设置的	YARN	队列，多个队列时用英文逗号分隔）。
	tag		-	 	选填		 	object	，任务标记，如果填入此值，在调用	返回任务列表	接口，返回该任务时会将此字段原样
返回，可用于系统集成时，对任务进行标记并进行相应处理。字段值最大限制	默认	1024	KB，由配置
kylin.job.tag-max-size=1024	指定。
	refresh_all_indexes		-	 	选填		 	boolean	，是否刷新全部索引，默认值为	"false"。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	PUT	\

		'http://localhost:7070/kylin/api/models/SSB_LINEORDER/segments'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{"project":"doc_expert",	"ids":["8f3b4040-aa75-4e74-9730-6bf1cae61745"],	"type":"REFRESH"}'

响应示例

		{

		"code":"000",

		"data":{

						"jobs":[

										{

														"job_name":"INDEX_REFRESH",

														"job_id":"38e2e1cc-97fa-7913-fb99-428191133fca-9ed2ef3a-178a-25fc-61f8-cae13bbf3f08"

										}

						]},

		"msg":""

		}

删除	Segment

	DELETE	http://host:port/kylin/api/models/{model_name}/segments

URL	Parameters

	model_name		-	 	必填		 	string	，模型名称。
	project		-	 	必填		 	string	，项目名称。
	purge		-	 	必填		 	boolean	，是否清空	Segments。
	ids		-	 	选填		 	array[string]	，Segment	id	列表。
	names		-	 	选填		 	array[string]	，Segment	name	列表。
	force		-	 	选填		 	boolean	，是否强制删除，默认值为	"false"。

注意：

1.当	 	purge		为	 	false		时， 	ids		和	 	names		必须设置一个，不能两者都设置或两者都为空。

2.因为	http	协议对请求头大小有限制，故推荐	 	ids		或	 	names		的个数小于100个。

936

Segment	管理	API

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	DELETE	\

		'http://localhost:7070/kylin/api/models/SSB_LINEORDER/segments?project=doc_expert&ids=291b9926-eaba-42d1-

9d70-0a587992bea7&purge=false'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

		{

						"code":"000",

						"data":"",

						"msg":""

		}

检测	Segment

校验传参区间内模型是否有重叠的	Segment	区间

	POST	http://host:port/kylin/api/models/{model_name}/segments/check

请求权限：Operation	及以上操作权限

生效版本：4.1.1	及以上版本

URL	Parameters

	model_name		-	 	required		 	string	，模型名称。

HTTP	Body:	JSON	Object

	project		-	 	required		 	string	，项目名称。
	start		-	 	required		 	string	，开始时间，时间戳类型，单位为毫秒，值必须大于0。
	end		-	 	required		 	string	，结束时间，时间戳类型，单位为毫秒，值必须大于0。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	POST	\

		'http://localhost:7070/kylin/api/models/ssb_model/segments/check'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{

										"project":"ssb",

										"start":"775785600000",

										"end":"775789200000"

						}'

937

Segment	管理	API

响应示例

{

				"code":	"000",

				"data":	{

								"segments_overlap":	[

												{

																"segment_id":	"17df7def-f06b-4b67-81d8-4c8368e714dc",

																"segment_name":	"19920101000000_19980802000000"

												},

												{

																"segment_id":	"1a9c070b-3847-48c6-b938-7109379eef9b",

																"segment_name":	"19980802000000_19980803000000"

												},

												{

																"segment_id":	"5cece637-daef-47f5-88e9-85b6a247d357",

																"segment_name":	"19980803000000_19980804000000"

												}

								]

				},

				"msg":	""

}

补全所有	Segment	索引

说明：指定模型，对该模型所有的	Segment，构建补全所有缺失的索引

	POST	http://host:port/kylin/api/models/{model_name}/indexes

URL	Parameters

	model_name		-	 	必填		 	string	，模型名称。

HTTP	Body:	JSON	Object

	project		-	 	必填		 	string	，项目名称。
	priority		-	 	选填		 	int	，设置任务优先级，范围为	 	0-4	，优先级依次从高到低，	默认为 	3
	yarn_queue		-	 	选填		 	string	，指定该任务使用的	YARN	队列，在系统级别或项目级别设置参数后使用：
kylin.engine-yarn.queue.in.task.enabled（是否允许为任务指定	YARN	队列，默认	false	不开启，true	代表开
启）、kylin.engine-yarn.queue.in.task.available（可供设置的	YARN	队列，多个队列时用英文逗号分隔）。
	tag		-	 	选填		 	object	，任务标记，如果填入此值，在调用	返回任务列表	接口，返回该任务时会将此字段原样
返回，可用于系统集成时，对任务进行标记并进行相应处理。字段值最大限制	默认	1024	KB，由配置
kylin.job.tag-max-size=1024	指定。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	POST	\

		'http://localhost:7070/kylin/api/models/ssb_test/indexes'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{"project":"ssb"}'

响应字段

	type	，	任务对应的类型

938

Segment	管理	API

NORM_BUILD，正常构建
NO_LAYOUT，所有待补齐的索引，状态都为非在线状态
NO_SEGMENT，所有待补齐的	Segment，状态都为非在线状态

	job_id	，正常构建时会返回对应的任务	id，无索引或者无数据时对应值为空

响应示例

{

				"code":"000",

				"data":{

								"type":"NORM_BUILD",

								"job_id":"e3aa809b-5e73-42a5-a1e1-649d53b16e2c"

				},

				"msg":""

}

指定	Segment	补全索引

	POST	http://host:port/kylin/api/models/{model_name}/segments/completion

URL	Parameters

	model_name		-	 	required		 	string	，模型名称
	project		-	 	required		 	string	，项目名称。
	parallel		-	 	optional		 	boolean	，	补全	segment	是否支持并行，默认值为	false
	ids		-	 	optional		 	array[string]	，Segment	id	列表。
	names		-	 	optional		 	array[string]	，Segment	name	列表。

注意：	 	ids		和	 	names		必须设置一个，不能两者都设置或两者都为空。

	yarn_queue		-	 	选填		 	string	，指定该任务使用的	YARN	队列，在系统级别或项目级别设置参数后使用：
kylin.engine-yarn.queue.in.task.enabled（是否允许为任务指定	YARN	队列，默认	false	不开启，true	代表开
启）、kylin.engine-yarn.queue.in.task.available（可供设置的	YARN	队列，多个队列时用英文逗号分隔）。
	tag		-	 	选填		 	object	，任务标记，如果填入此值，在调用	返回任务列表	接口，返回该任务时会将此字段原样
返回，可用于系统集成时，对任务进行标记并进行相应处理。字段值最大限制	默认	1024	KB，由配置
kylin.job.tag-max-size=1024	指定。
	batch_index_ids		-	 	optional		 	array<long>	，索引	id	列表
	index_status		-	 	optional		 	array<string>	，索引状态列表，可选值	NO	BUILD，ONLINE，BUILDING，大小
写不区分。

注意：	 	batch_index_ids		和	 	index_status		不能两者都设置，两者都为空默认补全指定	segment	全部索
引。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	POST	\

'http://localhost:7070/kylin/api/models/m1/segments/completion?project=ssb&names=19900101000000_19950101000

000,19950101000000_19970101000000'	\

-H	'Accept:		application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:		cn'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:		application/json;charset=utf-8'

响应示例

		{

939

Segment	管理	API

						"code":	"000",

						"data":	{

										"jobs":	[

														{

																		"job_name":	"INDEX_BUILD",

																		"job_id":	"74e28420-e317-42a9-a221-a7b381b5aeea"

														}

										],

										"failed_segments":	[]

						},

						"msg":	""

		}

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

940

快照管理	API

快照管理	API

提示：

1.	 请确保已阅读前面的访问及安全认证章节，了解如何在	REST	API	语句中添加认证信息。

2.	 在	Curl	命令行上，如果您访问的	URL	中含有	 	&		符号，请注意转义，比如在	URL	两端加上引号。

快照管理开关

注意：打开快照管理后，系统将不再自动进行快照构建和刷新，请根据快照列表手动进行快照管理

	PUT	http://host:port/kylin/api/projects/{project}/snapshot_config

请求权限：ADMIN	及以上权限
开始生效版本：4.2.2

URL	Parameters

	project		-	 	必填		 	string	，项目名称

HTTP	Body:	JSON	Object

	snapshot_manual_management_enabled		-	 	选填		 	boolean	，是否开启快照手动管理模式，默认为	false

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	PUT	\

'http://localhost:7070/kylin/api/projects/gc_test/snapshot_config'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	cn'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'	\

-d	'{	"snapshot_manual_management_enabled":	true	}'

响应示例

{

		"code":	"000",

		"data":	"",

		"msg":	""

}

新建快照

	POST	http://host:port/kylin/api/snapshots

请求权限：OPERATION	及以上权限
开始生效版本：4.2.2（分区构建生效版本：4.2.6）

HTTP	Body:	JSON	Object

	project		-	 	必填		 	string	，项目名称
	tables		-	 	选填		 	array[string]	，指定想要加载的表，格式如：DB.TABLE
	databases		-	 	选填		 	array[string]	，加载该数据库下所有表

注意：以上两个参数	 	databases		和	 	tables		不能同时为空，即必须选择任意一个加载对象

	priority		-	 	选填		 	integer	，设置任务优先级，范围为	 	0-4	，	优先级依次从高到低，默认为 	3

	options		-	 	选填		 	map[string:args]	，表名（格式如：DB.TABLE）到参数集合的映射， 	args		如下：

941

快照管理	API

	partition_col		-	 	必填		 	string	对应表的分区列，默认为	null，即没有设置分区，如果已经设置分区，此
处需要输入对应分区列

	partitions_to_build	- 	选填		 	string	，选择指定的分区来构建

	yarn_queue		-	 	选填		 	string	，指定该任务使用的	YARN	队列，在系统级别或项目级别设置参数后使用：
kylin.engine-yarn.queue.in.task.enabled（是否允许为任务指定	YARN	队列，默认	false	不开启，true	代表开
启）、kylin.engine-yarn.queue.in.task.available（可供设置的	YARN	队列，多个队列时用英文逗号分隔）。
	tag		-	 	选填		 	object	，任务标记，如果填入此值，在调用	返回任务列表	接口，返回该任务时会将此字段原样
返回，可用于系统集成时，对任务进行标记并进行相应处理。字段值最大限制	1	KB。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	POST	\

'http://localhost:7070/kylin/api/snapshots'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	cn'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'	\

-d	'{"project":"gc_test",	"tables":	["SSB.P_LINEORDER",	"DEFAULT.TEST_KYLIN_FACT"],	"options":{"DEFAULT.TES

T_KYLIN_FACT":{"partition_col":"CAL_DT"}}}'

Curl	响应示例

{

		"code":	"000",

		"data":	{

						"jobs":	[{

										"job_name":	"SNAPSHOT_BUILD",

										"job_id":	"65b3b0a4-d4d2-4a5b-af29-b190ca420543"

						},	{

										"job_name":	"SNAPSHOT_BUILD",

										"job_id":	"24aafb93-1cde-43d1-a627-8cd592f51cfe"

						}]

		},

		"msg":	""

}

配置分区列

	POST	http://host:port/kylin/api/snapshots/config

请求权限：OPERATION	及以上权限
开始生效版本：4.2.6

HTTP	Body:	JSON	Object

	project		-	 	必填		 	string	，项目名称
	table_partition_col		-	 	必填		 	map[string:string]		表（格式如：DB.TABLE）与分区列的映射关系

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	POST	\

'http://localhost:7070/kylin/api/snapshots/config'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

942

快照管理	API

-H	'Accept-Language:	cn'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'	\

-d	'{"project":"gc_test","table_partition_col":{"DEFAULT.TEST_KYLIN_FACT":"CAL_DT"}}'

Curl	响应示例

{

		"code":	"000",

		"data":	"",

		"msg":	""

}

刷新快照

	PUT	http://host:port/kylin/api/snapshots

请求权限：OPERATION	及以上权限

开始生效版本：4.2.2（分区构建生效版本：4.2.6）

HTTP	Body:	JSON	Object

	project		-	 	必填		 	string	，项目名称
	tables		-	 	选填		 	array[string]	，指定想要加载的表，格式如：DB.TABLE
	databases		-	 	选填		 	array[string]	，加载该数据库下所有表

注意：以上两个参数	 	databases		和	 	tables		不能同时为空，即必须选择任意一个加载对象

	priority		-	 	选填		 	integer	，设置任务优先级，范围为	 	0-4	，	优先级依次从高到低，默认为 	3

	options		-	 	必填		 	map[string:args]	，表名（格式如：DB.TABLE）到参数集合的映射， 	args		如下：

	partition_col		-	 	必填		 	string	对应表的分区列，默认为	null，即没有设置分区，如果已经设置分区，此
处需要输入对应分区列

	incremental_build		-	 	选填		 	boolean		是否保留之前构建的分区，默认	false。
	partitions_to_build	- 	选填		 	array[string]	，选择指定的分区来刷新

	yarn_queue		-	 	选填		 	string	，指定该任务使用的	YARN	队列，在系统级别或项目级别设置参数后使用：
kylin.engine-yarn.queue.in.task.enabled（是否允许为任务指定	YARN	队列，默认	false	不开启，true	代表开
启）、kylin.engine-yarn.queue.in.task.available（可供设置的	YARN	队列，多个队列时用英文逗号分隔）。
	tag		-	 	选填		 	object	，任务标记，如果填入此值，在调用	返回任务列表	接口，返回该任务时会将此字段原样
返回，可用于系统集成时，对任务进行标记并进行相应处理。字段值最大限制	默认	1024	KB，由配置
kylin.job.tag-max-size=1024	指定。

如果已经加载过某张表的快照，再进行加载时，会刷新该表快照。

参数	 	options		中的	 	partition_col		暂时为必填项，如果之前已经调用过设置分区列的接口，也必须在此处
填入正确的参数值。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	PUT	\

'http://localhost:7070/kylin/api/snapshots'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	cn'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

943

快照管理	API

-H	'Content-Type:	application/json;charset=utf-8'	\

-d	'{"project":"gc_test",		"tables":	["SSB.P_LINEORDER",		"DEFAULT.TEST_KYLIN_FACT"],"options":{"DEFAULT.TE

ST_KYLIN_FACT":{"partition_col":"CAL_DT","incremental_build":true,"partitions_to_build":["2012-03-01","2012

-03-04"]}}}'

Curl	响应示例

{

		"code":	"000",

		"data":	{

						"jobs":	[{

										"job_name":	"SNAPSHOT_REFRESH",

										"job_id":	"65b3b0a4-d4d2-4a5b-af29-b190ca420543"

						},	{

										"job_name":	"SNAPSHOT_REFRESH",

										"job_id":	"24aafb93-1cde-43d1-a627-8cd592f51cfe"

						}]

		},

		"msg":	""

}

删除快照

	DELETE	http://host:port/kylin/api/snapshots

请求权限：OPERATION	及以上权限
开始生效版本：4.2.2

URL	Parameters

	project		-	 	必填		 	string	，项目名称
	tables		-	 	必填		 	array[string]	，需要删除快照的表名列表，格式如：DB.TABLE，多张表之间用逗号分隔。
因为	http	协议对请求头大小有限制，故推荐长度小于100。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	DELETE	\

'http://localhost:7070/kylin/api/snapshots?project=gc_test&tables=SSB.P_LINEORDER%2CDEFAULT.TEST_KYLIN_FACT

'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	cn'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

		"code":"000",

		"data":	{

						"affected_jobs":[

										{

														"database":	"DEFAULT",

														"table":	"KYLIN_CAL",

														"job_id":	"e3aa809b-5e73-42a5-a1e1-649d53b16e2c"

										},

										{

														"database":	"DEFAULT",

														"table":	"P_LINEORDER",

														"job_id":	"e3aa809b-5e73-42a5-a1e1-649d53b16e2b"

										}

						]

		},

944

快照管理	API

		"msg":""

}

返回快照列表

	GET	http://host:port/kylin/api/snapshots

请求权限：QUERY	及以上权限
开始生效版本：4.2.2

URL	Parameters

	project		-	 	必填		 	string	，项目名称。
	table		-	 	选填		 	string	，表的搜索关键字，默认空，展示项目下所有快照。
	page_offset		- 	选填		 	int	，分页页面，默认为	0。
	page_size		- 	选填		 	int	，分页大小，默认为	10。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

'http://localhost:7070/kylin/api/snapshots?project=gc_test'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	cn'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

		"code":"000",

		"data":{

						"value":[

										{

														"table":"P_LINEORDER",

														"database":"SSB",

														"usage":	5,

														"storage":	8555,

														"fact_table_count":	2

														"lookup_table_count":	2,

														"last_modified_time":	1602315332279,

														"status":	"REFRESHING"

										},

										Object{...},

										Object{...},

										Object{...}

						],

						"offset":0,

						"limit":10,

						"total_size":4

		},

		"msg":""

}

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

945

内表管理	API

内表管理	API

提示：

1.	 请确保已阅读前面的访问及安全认证章节，了解如何在	REST	API	语句中添加认证信息。

2.	 在	Curl	命令行上，如果您访问的	URL	中含有	 	&		符号，请注意转义，比如在	URL	两端加上引号。

创建内表

	POST	http://host:port/kylin/api/internal_tables/{database}/{table}

URL	Parameters

	project		-	 	必填		 	string	，项目名称。

HTTP	Body:	JSON	Object

	partition_cols		-	 	选填		 	array[string]	，分区列（currently,	only	one	partition	column	is	supported）。
	date_partition_format		-	 	选填		 	string	，时间分区列格式。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	POST	http://localhost:7070/kylin/api/internal_tables/SSB/LINE_ORDER?project=test	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=UTF-8'	\

		-d	'{

						"partition_cols":	["date"],

						"date_partition_format":	"yyyy-MM-dd"

		}'

响应示例

{

				"code":"000",

				"data":"",

				"msg":""

}

返回内表列表

	GET	http://host:port/kylin/api/internal_tables

URL	Parameters

	project		-	 	必填		 	string	，项目名称。
	page_offset		-	 	选填		 	int	，分页页面，默认为	 	0	。
	page_size		-	 	选填		 	int	，分页大小，默认为	 	10	。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

946

内表管理	API

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	http://localhost:3000/kylin/api/internal_tables?project=test	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=UTF-8'

响应示例

{

"code":	"000",

"data":	{

		"value":	[

				{

						"uuid":	"4436afc6-aa96-896b-77e9-14d4c1cb4e7c",

						"table_name":	"KYLIN_CAL_DT",

						"database_name":	"DEFAULT",

						"time_partition_col":	"CAL_DT",

						"date_partition_format":	"yyyy-MM-dd",

						"hit_count":	0,

						"row_count":	0,

						"storage_size":	0,

						"update_time":	1724229338221,

						"tbl_properties":	{}

				},

				{

						"uuid":	"86091cd3-3364-24a2-3417-4678b275573d",

						"table_name":	"KYLIN_SALES",

						"database_name":	"DEFAULT",

						"time_partition_col":	"PART_DT",

						"date_partition_format":	"yyyy-MM-dd",

						"hit_count":	0,

						"row_count":	459,

						"storage_size":	164373,

						"update_time":	1724062924308,

						"tbl_properties":	{

										"bucketNum":	"1"

						}

				}

		],

		"offset":	0,

		"limit":	10,

		"total_size":	2

		},

		"msg":	""

}

更新内表属性

	PUT	http://host:port/kylin/api/internal_tables/{database}/{table}

URL	Parameters

	project		-	 	必填		 	string	，项目名称。

HTTP	Body:	JSON	Object

	partition_cols		-	 	选填		 	array[string]	，分区列（当前只支持一个分区列）。
	date_partition_format		-	 	选填		 	string	，时间分区列格式。

HTTP	Header

947

内表管理	API

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	PUT	http://localhost:7070/kylin/api/internal_tables/SSB/LINE_ORDER?project=test	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=UTF-8'	\

		-d	'{

						"partition_cols":	["date"],

						"date_partition_format":	"yyyy-MM-dd"

		}'

响应示例

{

				"code":"000",

				"data":"",

				"msg":""

}

获取内表分区详情

	GET	http://host:port/kylin/api/internal_tables/{database}/{table}

URL	Parameters

	project		-	 	必填		 	string	，项目名称。
	page_offset		-	 	选填		 	int	，分页页面，默认为	 	0	。
	page_size		-	 	选填		 	int	，分页大小，默认为	 	10	。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	http://localhost:3000/kylin/api/internal_tables/{database}/{table}?project=test	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=UTF-8'

响应示例

{

		"code":	"000",

		"data":	{

		"value":	[

				{

						"uuid":	"b052703c-a63d-b132-7104-e82917e92b2f",

						"last_modified":	0,

						"create_time":	1724062886440,

						"version":	"4.0.0.0",

						"mvcc":	-1,

						"storage_path":	"hdfs://sandbox.hortonworks.com:8020/kylin/test5_0812/test/Internal/DEFAULT/KYLIN_SAL

ES/part_dt=2012-01-01",

948

内表管理	API

						"size_in_bytes":	4147,

						"file_count":	1,

						"partition_value":	"2012-01-01"

				},

				{

						"uuid":	"b7c06ed2-a127-45b8-64c5-9fbb280a4a5e",

						"last_modified":	0,

						"create_time":	1724062886439,

						"version":	"4.0.0.0",

						"mvcc":	-1,

						"storage_path":	"hdfs://sandbox.hortonworks.com:8020/kylin/test5_0812/test/Internal/DEFAULT/KYLIN_SAL

ES/part_dt=2012-01-02",

						"size_in_bytes":	4327,

						"file_count":	1,

						"partition_value":	"2012-01-02"

				}

		],

		"offset":	0,

		"limit":	10,

		"total_size":	2

		},

		"msg":	""

}

加载内表数据

	POST	http://host:port/kylin/api/internal_tables/{project}/{database}/{table}

HTTP	Body:	JSON	Object

	incremental		-	 	必填		 	boolean	，是否增量加载。
	refresh		-	 	必填		 	boolean	，false	表示加载数据，true表示刷新数据。
	start_date		-	 	选填		 	string	，毫秒时间戳，增量加载时的开始时间，增量加载时必填。
	end_date		-	 	选填		 	string	，毫秒时间戳，增量加载时的结束区间，增量加载时必填。
	yarn_queue		-	 	选填		 	string	，加载任务使用的队列。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

		curl	-X	POST	http://localhost:3000/kylin/api/internal_tables/test_inner_table_2/DEFAULT/KYLIN_CAL_DT	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=UTF-8'	\

		-d	'{"incremental":true,"refresh":false,"start_date":1328112000000,"end_date":1328198400000,"yarn_queue":

"default"}'

响应示例

{

		"code":	"000",

		"data":	{

				"internal_table_loading_jobs":	[

						{

								"job_name":	"INTERNAL_TABLE_BUILD",

								"job_id":	"881287d7-3835-52cc-dfdd-c378cd6f57fc"

						}

				]

		},

949

内表管理	API

		"msg":	""

}

清空内表数据

	DELETE	http://host:port/kylin/api/internal_tables/truncate_internal_table

URL	Parameters

	project		-	 	必填		 	string	，项目名称。
	database		-	 	必填		 	string	，数据库名称。
	table		-	 	必填		 	string	，表名。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl		-X	DELETE	'http://localhost:3000/kylin/api/internal_tables/truncate_internal_table?project=test&datab

ase=SSB&table=LINEORDER'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='

响应示例

{

		"code":	"000",

		"data":	null,

		"msg":	""

}

删除表分区

	DELETE	http://host:port/kylin/api/internal_tables/partitions

URL	Parameters

	project		-	 	必填		 	string	，项目名称。
	database		-	 	必填		 	string	，数据库名称。
	table		-	 	必填		 	string	，表名。
	partitions		-	 	必填		 	array[string]		分区字段值数组。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl		-X	DELETE	'http://localhost:3000/kylin/api/internal_tables/partitions?project=test&database=SSB&table

=LINEORDER&partitions=2012-01-30,2012-01-31'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='

响应示例

950

内表管理	API

{

		"code":	"000",

		"data":	null,

		"msg":	""

}

删除内表

	DELETE	http://host:port/kylin/api/internal_tables/{database}/{table}

URL	Parameters

	project		-	 	必填		 	string	，项目名称。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

	curl	-X	DELETE	http://localhost:3000/kylin/api/internal_tables/DEFAULT/KYLIN_CAL_DT?project=test	\

				-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

				-H	'Accept-Language:	cn'	\

				-H	'Authorization:	Basic	QURNSU46S1lMSU4='

响应示例

{

	"code":	"000",

	"data":	"",

	"msg":	""

}

加载内表	Gluten	缓存

	POST	http://host:port/kylin/api/internal_table/gluten_cache

HTTP	Body:	JSON	Object

	project		-	 	必填		 	string	，项目名称。
	database		-	 	必填		 	string	，数据库名称。
	table		-	 	必填		 	string	，表名。
	columns		-	 	选填		 	array[string]	,	需要加载缓存的列名数组。如果未指定，将加载所有列。
	start		-	 	选填		 	string	,	开始时间。仅对分区表有效，如果指定 	start	，将会缓存 	start	之后的分区数据。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

	curl	-X	POST	'http://localhost:3000/kylin/api/internal_table/gluten_cache'	\

				-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

				-H	'Accept-Language:	cn'	\

				-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

				-d	'{"start":694368000000,	"columns":[],	"table":	"lineorder",	"database":	"ssb",	"project":	"test"}'

951

内表管理	API

响应示例

{

	"code":	"000",

	"data":	"",

	"msg":	""

}

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

952

查询	API

查询	API

提示：

1.	 请确保已阅读前面的访问及安全认证章节，了解如何在	REST	API	语句中添加认证信息。

2.	 在	Curl	命令行上，如果您访问的	URL	中含有	 	&		符号，请注意转义，比如在	URL	两端加上引号。

查询模型数据

	POST	http://host:port/kylin/api/query

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

HTTP	Body:	JSON	Object

	sql		-	 	必选		 	string	，查询的	SQL	语句
	project		-	 	必选		 	string	，项目名称
	offset		-	 	可选		 	int	，	设置查询从哪一行开始往后返回数据。使用时必须与	 	limit		配合使用。
	limit		-	 	可选		 	int	，设置从	 	offset		开始返回的行数，不足	 	limit		以实际行数为准
	forcedToPushDown		-	 	可选		 	boolean	，查询是否强制下压，默认为	 	false	，同时需要打开查询下压开关才可强
制下压。

	partialMatchIndex		-	 	可选		 	boolean	,	默认为	 	false	，异构segment中存在不能回答查询的segment的时候，是
否只查询具有合适index的segment中的数据
	forced_to_index		-	 	可选		 	boolean	,	查询是否强制击中索引，默认为	 	false	，开启后，查询如果能击中索引则
正常返回，如果不能则直接报错，不再下压。

	forcedToTieredStorage		-	 	optional		 	int	，查询是否强制使用分层存储，默认值为	 	0	，表示当分层存储无法
回答时，通过	HDFS	上的基础明细索引回答，配置为	 	1		表示当分层存储无法回答时，查询下压，配置为	 	2
表示当分层存储无法回答查询时，查询失败。当	 	forcedToPushDown		为	 	true		时，该参数不生效，当
	forced_to_index		为	 	true		时，该参数配置为	 	1		不生效。

注意：参数	 	forcedToPushDown		和	 	forced_to_index		不能同时为	 	true	，会报错。

Curl	请求示例

curl	-X	POST	\

		'http://host:port/kylin/api/query'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{	"sql":"select	count(*)	from	SSB.P_LINEORDER",	"project":"ssb",	"partialMatchIndex":"true"}'

响应示例

{

				"code":"000",

				"data":{

								"columnMetas":[

												{

																"isNullable":0,

																"displaySize":19,

																"label":"EXPR$0",

																"name":"EXPR$0",

																"schemaName":null,

953

查询	API

																"catelogName":null,

																"tableName":null,

																"precision":19,

																"scale":0,

																"columnType":-5,

																"columnTypeName":"BIGINT	NOT	NULL",

																"caseSensitive":false,

																"autoIncrement":false,

																"currency":false,

																"definitelyWritable":false,

																"signed":true,

																"writable":false,

																"searchable":false,

																"readOnly":false

												}

								],

								"results":[

												[

																"60175"

												]

								],

								"affectedRowCount":0,

								"exceptionMessage":null,

								"duration":129,

								"scanRows":[

												2519

								],

								"totalScanRows":2519,

								"scanBytes":[

												6118

								],

								"totalScanBytes":6118,

								"resultRowCount":1,

								"shufflePartitions":1,

								"hitExceptionCache":false,

								"storageCacheUsed":false,

								"queryStatistics":null,

								"cpu_time":35753933,

								"explain":false,

								"is_explain":false,

								"query_plan":{

										"spark_plan":"",

										"calcite_plan":""

								},

								"traceUrl":null,

								"queryId":"738fad53-57a9-43fc-a186-b25d0993dfcb",

								"server":"client134.kcluster:7470",

								"suite":null,

								"signature":"1593670148521;1592230756490_1595228217256_1595228217256_1595228217256_1595228217257",

								"engineType":"NATIVE",

								"exception":false,

								"prepare":false,

								"timeout":false,

								"partial":false,

								"isException":false,

								"appMasterURL":"/kylin/sparder/SQL/execution/?id=27391",

								"pushDown":false,

								"is_prepare":false,

								"is_timeout":false,

								"realizations":[

												{

																"modelId":"c7a7a1d0-71c6-4d42-bbc3-76167e5d2d10",

																"modelAlias":"ssb_cube",

																"layoutId":80001,

																"type":"Agg	Index",

																"valid":true,

																"partialMatchModel":false,

																"storageType":0,

																"lookupTables":[]

954

查询	API

												}

								],

								"traces"	:	[

								{

											"name":	"GET_ACL_INFO",

											"group":	"PREPARATION",

											"duration":	10

								},

								{

											"name"	:	"SQL_TRANSFORMATION",

											"group"	:	"PREPARATION",

											"duration"	:	3

								},

								{

											"name"	:	"SQL_PARSE_AND_OPTIMIZE",

											"group"	:	"PREPARATION",

											"duration"	:	9

								},

								{

											"name"	:	"MODEL_MATCHING",

											"group"	:	"PREPARATION",

											"duration"	:	2

								},

								{

											"name"	:	"PREPARE_AND_SUBMIT_JOB",

											"group"	:	null,

											"duration"	:	64

								},

								{

											"name"	:	"WAIT_FOR_EXECUTION",

											"group"	:	null,

											"duration"	:	2

								},

								{

											"name"	:	"EXECUTION",

											"group"	:	null,

											"duration"	:	26

								},

								{

											"name"	:	"FETCH_RESULT",

											"group"	:	null,

											"duration"	:	7

								}]

				},

				"msg":""

}

响应信息

	columnMetas		-	每个列的元数据信息
	results		-	返回的结果集
	resultRowCount		-	返回结果行数
	engineType		-	使用的查询引擎
	isException		-	这个查询返回是否是异常
	exceptionMessage		-	返回异常对应的内容
	cpu_time		-	CPU	耗时(纳秒)
	is_explain		-	是否为执行计划查询
	query_plan		-	执行计划

	calcite_plan		calcite	执行计划
	spark_plan		spark	执行计划
	realizations		-	查询命中的模型信息

	modelId		-	模型	ID
	modelAlias		-	模型名称

955

查询	API

	layoutId		-	索引	ID
	type		-	索引类型
	lookupTables		-	查询扫描的快照列表
	storageType		-	模型存储类型，0，1-DEFAULT，3-DELTA，4-ICEBERG
	valid		-	模型是否有效
	partialMatchModel		-	是否模型部分匹配

	queryId		-	查询	ID
	duration		-	查询耗时
	totalScanRows		-	总扫描行数
	totalScanBytes		-	总扫描字节数
	hitExceptionCache		-	是否来自执行失败的结果缓存
	storageCacheUsed		-	是否来自执行成功的结果缓存
	server		-	在启用了负载平衡的环境中，执行查询的服务器
	timeout		-	查询是否超时
	pushDown		-	查询是否下压到其他引擎
	traces		-	查询每一步的耗时信息
	name		-	查询步骤的名字
	duration		-	耗时(毫秒)
	group		-	查询步骤所属的类别

判断查询是否为大查询

API	说明：

生效版本：从	4.6.18.0	版本开始生效；
使用场景：大查询往往消耗更多查询资源，查询响应也更慢，可能影响小查询的响应性能。您可通过此	API
判断查询是否为大查询，然后根据返回值分流大查询至特定的查询队列，从而保证小查询的性能。该	API	的
入参与查询模型数据	API	一致。如需了解具体实现方案，请联系	Kyligence	技术支持团队获取帮助。
前置条件：开启查询限流，设置为大查询拒绝策略，设置方法和大查询的判断标准可查看查询限流，保护查

询稳定章节。

	POST	http://host:port/kylin/api/query/if_big_query

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

HTTP	Body:	JSON	Object

	sql		-	 	必选		 	string	，查询的	SQL	语句
	project		-	 	必选		 	string	，项目名称
	offset		-	 	可选		 	int	，	设置查询从哪一行开始往后返回数据。使用时必须与	 	limit		配合使用。
	limit		-	 	可选		 	int	，设置从	 	offset		开始返回的行数，不足	 	limit		以实际行数为准
	forcedToPushDown		-	 	可选		 	boolean	，查询是否强制下压，默认为	 	false	，同时需要打开查询下压开关才可强
制下压。

	partialMatchIndex		-	 	可选		 	boolean	,	默认为	 	false	，异构segment中存在不能回答查询的segment的时候，是
否只查询具有合适index的segment中的数据
	forced_to_index		-	 	可选		 	boolean	,	查询是否强制击中索引，默认为	 	false	，开启后，查询如果能击中索引则
正常返回，如果不能则直接报错，不再下压。

	forcedToTieredStorage		-	 	optional		 	int	，查询是否强制使用分层存储，默认值为	 	0	，表示当分层存储无法
回答时，通过	HDFS	上的基础明细索引回答，配置为	 	1		表示当分层存储无法回答时，查询下压，配置为	 	2
表示当分层存储无法回答查询时，查询失败。当	 	forcedToPushDown		为	 	true		时，该参数不生效，当

956

查询	API

	forced_to_index		为	 	true		时，该参数配置为	 	1		不生效。

注意：参数	 	forcedToPushDown		和	 	forced_to_index		不能同时为	 	true	，会报错。

Curl	请求示例

curl	-X	POST	\

		'http://host:port/kylin/api/query/if_big_query'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{	"sql":"select	count(*)	from	SSB.P_LINEORDER",	"project":"ssb",	"partialMatchIndex":"true"}'

响应示例

{

								"code":"000",

								"data":{

																"if_big_query":	"bigquery",

																"scan_rows":	10000,

																"isException":	false,

																"exceptionMessage":	null,

																						"isCache":	false

								},

								"msg":""

}

响应信息

	code		-	 	string	，响应码，返回值： 	000		（请求处理成功），	 	999	（请求处理失败）
	msg		-	 	string	，响应消息
	data		-	 	JSON	Object	，返回内容

	ifbigquery		-	 	string	，是否大查询， 	bigquery		为大查询， 	nonbigquery		不是大查询， 	others		表示未
判定是否大查询，查询报错、查询下压时无法判断是否大查询；

	scanrows		-	 	string	，查询扫描行数
	isException		-	 	boolean	，查询是否异常，为	true	表示没有异常，为	false	表示有异常
	exceptionMessage		-	 	string	，查询异常信息
	iscache		-	 	boolean	，查询是否击中缓存

判断查询是否命中索引

API	说明：

生效版本：从	4.6.16.0	版本开始生效；

	POST	http://host:port/kylin/api/query/detection

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

HTTP	Body:	JSON	Object

	sql		-	 	必选		 	string	，查询的	SQL	语句
	project		-	 	必选		 	string	，项目名称
	offset		-	 	可选		 	int	，	设置查询从哪一行开始往后返回数据。使用时必须与	 	limit		配合使用，默认是	0
	limit		-	 	可选		 	int	，设置从	 	offset		开始返回的行数，不足	 	limit		以实际行数为准，默认是	500

Curl	请求示例

957

查询	API

curl	-X	POST	\

		'http://host:port/kylin/api/query/detection'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{	"sql":"SELECT	LO_PARTKEY	FROM	SSB.P_LINEORDER",	"project":"ssb"}'

响应示例

{

				"code":	"000",

				"data":	{

								"is_exception":	false,

								"exception_message":	null,

								"query_id":	"73643bdf-a37d-528b-3e90-6ff5e2b98947",

								"is_push_down":	false,

								"is_post_aggregation":	false,

								"is_table_index":	true,

								"is_base_index":	false,

								"is_cache":	false,

								"is_constants":	false,

								"realizations":	[

												{

																"model_id":	"aa7d0eab-6f72-3b02-019f-9f2fc84a0ecb",

																"model_alias":	"AUTO_MODEL_P_LINEORDER_1",

																"layout_id":	20000020001,

																"index_type":	"Table	Index",

																"partial_match_model":	false,

																"valid":	true,

																"is_table_index":	true,

																"is_base_index":	false

												}

								]

				},

				"msg":	""

}

响应信息

	is_exception		-	查询是否异常
	exception_message		-	查询异常时，返回的异常信息
	query_id		-	查询	ID
	is_push_down		-	查询是否下压到其他引擎
	is_post_aggregation		-	是否需要后聚合，即没有精确命中索引（任意一个被击中的索引需要后聚合，则为
true）
	is_table_index		-	是否命中明细索引（被击中的索引包含明细索引，则为	true）
	is_base_index		-	是否命中基础聚合/明细索引（被击中的索引包含基础索引，则为	true）
	is_cache		-	是否命中缓存（若要命中缓存，请保证	query	和	/query/detection	API	的请求参数一致）
	is_constants		-	是否是常量查询
	realizations		-	查询命中的模型和索引信息的集合

	model_id		-	模型ID
	model_alias		-	模型名称
	layout_id		-	索引ID
	index_type		-	索引类型
	partial_match_model		-	是否模型部分匹配
	valid		-	模型是否有效
	is_table_index		-	是否命中明细索引
	is_base_index		-	是否命中基础聚合/明细索引

958

查询	API

清理查询缓存

	DELETE	http://host:port/kylin/api/query/cache

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

URL	Parameters

	project		-	 	可选		 	string	，项目名称

Curl	请求示例

curl	-X	DELETE	'http://host:port/kylin/api/query/cache?project=kylin'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	cn'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":	"000",

				"data":"",

				"msg":""

}

刷新缓存数据

调用本	API	可对所有查询节点的	Spark	SQL	Context	表缓存进行刷新，适用于数据源表更新后，查询下压失败的场景。

	PUT	http://host:port/kylin/api/tables/catalog_cache

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

HTTP	Body:	JSON	Object

	tables		-	 	必选		 	string	，指定想要加载的表，格式如：DB.TABLE，多张表之间用逗号分隔

Curl	请求示例

curl	-X	PUT	\

		'http://host:port/kylin/api/tables/catalog_cache'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{"tables":["SSB.LINEORDER","SSB.SUPPLIER"]}'

响应示例

{

				"code":	"000",

				"data":	{

								"nodes":	[

												{

959

查询	API

																"server":	"slave104.tnt:18001",

																"refreshed":	[

																				"SSB.LINEORDER",

																				"SSB.SUPPLIER"

																],

																"failed":	[]

												},

												{

																"server":	"slave104.tnt:18003",

																"refreshed":	[

																				"SSB.LINEORDER",

																				"SSB.SUPPLIER"

																],

																"failed":	[]

												}

								]

				},

				"msg":	""

}

响应信息

	nodes		-	不同节点的刷新结果
	server		-	节点信息
	refreshed		-	刷新成功的表
	failed		-	刷新失败的表
	msg		-	刷新失败的原因

获取查询历史

	GET	http://host:port/kylin/api/query/query_histories

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

URL	Parameters

	project		-	 	必选		 	string	，项目名称
	page_offset		-	 	可选		 	int	，分页页面，默认为	 	0
	page_size		-	 	可选		 	int	，分页大小，默认为	 	10
	start_time_from		-	 	可选		 	string	，查询历史开始时间	timestamp，单位	ms，和	start_time_to	不能单独使用
	start_time_to		-	 	可选		 	string	，查询历史结束时间	timestamp，单位	ms，和	start_time_from	不能单独使用
	sql		-	 	可选		 	string	，用于模糊匹配	SQL	查询关键字	或	查询	ID

Curl	请求示例

curl	-X	GET	\

		'http://host:port/kylin/api/query/query_histories?project=kylin_demo&page_offset=5&page_size=1&start_time

_from=1656864000000&start_time_to=1656950400000&sql=SELECT'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":	"000",

				"data":	{

960

查询	API

								"size":	79,

								"query_histories":	[

												{

																"queryRealizations":	null,

																"query_id":	"4bfbc8f1-ffcb-ae86-c5f1-2b78c73cb802",

																"query_history_info":	{

																				"exactly_match":	true,

																				"scan_segment_num":	1,

																				"state":	"FAILED",

																				"execution_error":	false,

																				"error_msg":	null,

																				"query_snapshots":	[],

																				"realization_metrics":	[

																								{

																												"queryId":	"4bfbc8f1-ffcb-ae86-c5f1-2b78c73cb802",

																												"duration":	568,

																												"layoutId":	"1",

																												"indexType":	"Agg	Index",

																												"modelId":	"118ae12b-5198-ade2-ecd9-b7e5f64318a2",

																												"queryTime":	1656914360898,

																												"projectName":	"kylin_demo",

																												"snapshots":	[],

																												"secondStorage":	false,

																												"streamingLayout":	false

																								},

																								{

																												"queryId":	"4bfbc8f1-ffcb-ae86-c5f1-2b78c73cb802",

																												"duration":	568,

																												"layoutId":	"1",

																												"indexType":	"Agg	Index",

																												"modelId":	"6cf4a660-e217-add5-87f4-04493c8df21e",

																												"queryTime":	1656914360898,

																												"projectName":	"kylin_demo",

																												"snapshots":	[],

																												"secondStorage":	false,

																												"streamingLayout":	false

																								}

																				],

																				"traces":	[

																								{

																												"name":	"HTTP_RECEPTION",

																												"group":	null,

																												"duration":	29

																								},

																								{

																												"name":	"CONNECTION_CREATING_TIME",

																												"group":	null,

																												"duration":	378

																								},

																								{

																												"name":	"STATEMENT_TO_REQUEST_TIME",

																												"group":	null,

																												"duration":	1

																								},

																								{

																												"name":	"GET_ACL_INFO",

																												"group":	"PREPARATION",

																												"duration":	1

																								},

																								{

																												"name":	"SQL_TRANSFORMATION",

																												"group":	"PREPARATION",

																												"duration":	12

																								},

																								{

																												"name":	"SQL_PARSE_AND_OPTIMIZE",

																												"group":	"PREPARATION",

																												"duration":	125

																								},

961

查询	API

																								{

																												"name":	"MODEL_MATCHING",

																												"group":	"PREPARATION",

																												"duration":	10

																								},

																								{

																												"name":	"PREPARE_AND_SUBMIT_JOB",

																												"group":	"JOB_EXECUTION",

																												"duration":	277

																								},

																								{

																												"name":	"WAIT_FOR_EXECUTION",

																												"group":	"JOB_EXECUTION",

																												"duration":	13

																								},

																								{

																												"name":	"EXECUTION",

																												"group":	"JOB_EXECUTION",

																												"duration":	90

																								},

																								{

																												"name":	"FETCH_RESULT",

																												"group":	"JOB_EXECUTION",

																												"duration":	11

																								},

																								{

																												"name":	"QUERY_RESPONSE_TIME",

																												"group":	null,

																												"duration":	8

																								}

																				],

																				"cache_type":	null,

																				"query_msg":	null

																},

																"sql_text":	"SELECT	*\nFROM\n		(SELECT	PICKUP_DATE,\n										TAXI_ORDER_NUMBER,\n										PE

OPLE_POSITIVE_NEW_CASES_COUNT,\n										round(TAXI_ORDER_NUMBER	/	PEOPLE_POSITIVE_NEW_CASES_COUNT,	2)	AS	COVI

D_IMPACT_INDEX\n			FROM\n					(SELECT	PICKUP_DATE,\n													MONTH_START,\n													ZONE,\n

	TAXI_ORDER_NUMBER\n						FROM\n								(SELECT	PICKUP_DATE,\n																MONTH_START,\n																ZON

E,\n																sum(TOTAL_AMOUNT)	AS	TAXI_PRICE_AMOUNT	,\n																count(TOTAL_AMOUNT)	AS	TAXI_ORDER

_NUMBER\n									FROM\n											(SELECT	PICKUP_DATE,\n																			MONTH_START,\n																			ZO

NE,\n																			TOTAL_AMOUNT,\n																			trip_distance\n												FROM	KYLIN_DEMO.TAXI_TRIP_

RECORDS_VIEW	t_f\n												LEFT	JOIN	KYLIN_DEMO.NEWYORK_ZONE	t_z	ON	t_f.PULOCATIONID	=	t_z.LOCATIONID\n

							LEFT	JOIN	KYLIN_DEMO.LOOKUP_CALENDAR	t_c	ON	t_f.PICKUP_DATE	=	t_c.DAY_START)	t_merge\n									GROUP	BY

PICKUP_DATE,\n																		MONTH_START,\n																		ZONE)\n						WHERE	ZONE	=	'East	New	York')	t_l\

n			LEFT	JOIN\n					(SELECT	REPORT_DATE,\n													MONTH_START,\n													PROVINCE_STATE_NAME,\n

						PEOPLE_POSITIVE_NEW_CASES_COUNT\n						FROM\n								(SELECT	REPORT_DATE,\n																MONTH_START,\n

																PROVINCE_STATE_NAME,\n																sum(PEOPLE_POSITIVE_NEW_CASES_COUNT)	AS	PEOPLE_POSITIVE_N

EW_CASES_COUNT\n									FROM	KYLIN_DEMO.COVID_19_ACTIVITY	t_f\n									LEFT	JOIN	KYLIN_DEMO.LOOKUP_CALENDAR	t

_c	ON	t_f.REPORT_DATE	=	t_c.DAY_START\n									GROUP	BY	REPORT_DATE,\n																		MONTH_START,\n

										PROVINCE_STATE_NAME)\n						WHERE	PROVINCE_STATE_NAME	=	'New	York')	t_r	ON	t_l.PICKUP_DATE=t_r.REPORT

_DATE)	tt\nWHERE	PICKUP_DATE	>=	'2020-01-01'\n		AND	PICKUP_DATE	<=	'2020-12-31'\nLIMIT	50000",

																"query_time":	1656914360898,

																"duration":	568,

																"server":	"snoopy-gw07.kylin.com:7095",

																"submitter":	"ADMIN",

																"index_hit":	true,

																"query_status":	"SUCCEEDED",

																"result_row_count":	366,

																"id":	296,

																"engine_type":	"NATIVE",

																"total_scan_count":	122839,

																"project_name":	"kylin_demo",

																"realizations":	[

																				{

																								"modelId":	"118ae12b-5198-ade2-ecd9-b7e5f64318a2",

																								"modelAlias":	"AUTO_MODEL_TAXI_TRIP_RECORDS_VIEW_1",

																								"layoutId":	1,

																								"indexType":	"Agg	Index",

																								"snapshots":	[],

962

查询	API

																								"valid":	true,

																								"partialMatchModel":	false

																				},

																				{

																								"modelId":	"6cf4a660-e217-add5-87f4-04493c8df21e",

																								"modelAlias":	"AUTO_MODEL_COVID_19_ACTIVITY_1",

																								"layoutId":	1,

																								"indexType":	"Agg	Index",

																								"snapshots":	[],

																								"valid":	true,

																								"partialMatchModel":	false

																				}

																],

																"total_scan_bytes":	849962,

																"error_type":	null,

																"cache_hit":	false

												}

								]

				},

				"msg":	""

}

响应信息

	query_id		-	查询	ID
	query_history_info		-	查询历史的信息
	exactly_match		-	是否精确匹配
	scan_segment_num		-	扫描的	Segment	数
	state		-	是否满足查询历史推荐的标识
	execution_error		-	是否查询失败
	error_msg		-	查询失败的错误信息
	query_snapshots		-	查询扫描的快照列表

	realization_metrics

	queryId		-	查询	ID
	duration		-	耗时(毫秒)
	layoutId		-	索引	ID
	indexType		-	索引类型
	modelId		-	模型	ID
	queryTime		-	查询发生的时间戳
	projectName		-	项目名称
	snapshots		-	查询扫描的快照列表
	secondStorage		-	是否使用分层存储
	streamingLayout		-	是否命中流数据索引

	traces

	name		-	查询步骤的名字
	duration		-	耗时(毫秒)
	group		-	查询步骤所属的类别

	cache_type		-	缓存类型
	query_msg		-	待补充
	sql_text		-	查询使用的	SQL
	query_time		-	查询发生的时间戳
	duration		-	耗时(毫秒)
	server		-	节点信息
	submitter		-	用户名
	index_hit		-	是否命中索引
	query_status		-	查询的状态
	result_row_count		-	查询结果的行数

963

查询	API

	engine_type		-	引擎类型
	total_scan_count		-	查询扫描的行数
	project_name		-	项目名称

	realizations

	modelId		-	模型	ID
	modelAlias		-	模型名称
	layoutId		-	索引	ID
	indexType		-	索引类型
	snapshots		-	查询扫描的快照列表
	valid		-	模型是否有效
	partialMatchModel		-	是否模型部分匹配
	total_scan_bytes		-	总扫描字节数
	error_type		-	错误类型
	cache_hit		-	是否命中缓存

下载查询历史

	GET	http://host:port/kylin/api/query/download_query_histories

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

URL	Parameters

	project		-	 	必选		 	string	，项目名称。
	timezone_offset_hour		-	 	必选		 	int	，查询历史的时区偏移，与格林尼治时间（GMT）相差的小时数，例如东
八区则传入	8，注意只能取	[-18,18]	之间的整数。
	start_time_from		-	 	可选		 	string	，查询历史开始时间	timestamp，单位	ms，和	start_time_to	一起使用才有
效。例如	1617206400000，若输入的不是数字，将返回空。
	start_time_to		-	 	可选		 	string	，查询历史结束时间	timestamp，单位	ms，和	start_time_from	一起使用才有
效。	例如	1620662400000，若输入的不是数字，将返回空。
	latency_from		-	 	可选		 	string	，查询延迟大于latency_from，单位s，和	latency_to	一起使用才有效。例如	10，
若输入的不是数字，将返回空。

	latency_to		-	 	可选		 	string	，查询延迟小于latency_to，单位s，和	latency_from	一起使用才有效。例如20，若
输入的不是数字，将返回空。

	query_status		-	 	可选		 	List<String>		，	查询状态，例如	SUCCEEDED、FAILED，若输入这两个以外的值，将
返回空。

	sql		-	 	可选		 	string		，用于模糊匹配用户sql	或	query	ID。
	realization		-	 	可选		 	List<String>		，查询对象。
	server		-	 	可选		 	string	，查询节点的主机名和端口号，如：myhost:7072。
	submitter		-	 	可选		 	List<String>	，查询用户。

Curl	请求示例

curl	-X	GET	\

		'http://host:port/kylin/api/query/download_query_histories?timezone_offset_hour=8&realization=&query_stat

us=&submitter=&project=default&start_time_from=&start_time_to=&latency_from=&latency_to=&sql='	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-o	query_history.csv

964

查询	API

下载查询历史SQL

	GET	http://host:port/kylin/api/query/download_query_histories_sql

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

URL	Parameters

	project		-	 	必选		 	string	，项目名称
	start_time_from		-	 	可选		 	string	，查询历史开始时间	timestamp，单位	ms，和	start_time_to	一起使用才有
效，例如	1617206400000，若输入的不是数字，将返回空。
	start_time_to		-	 	可选		 	string	，查询历史结束时间	timestamp，单位	ms，和	start_time_from	一起使用才有
效，例如	1620662400000，若输入的不是数字，将返回空。
	latency_from		-	 	可选		 	string	，查询延迟大于latency_from，单位s，和	latency_to	一起使用才有效。例如	10，
若输入的不是数字，将返回空。

	latency_to		-	 	可选		 	string	，查询延迟小于latency_to，单位s，和	latency_from	一起使用才有效。例如20，若
输入的不是数字，将返回空。

	query_status		-	 	可选		 	List<String>		,	查询状态，例如	SUCCEEDED、FAILED，若输入这两个以外的值，将
返回空。

	sql		-	 	可选		 	string		，用于模糊匹配用户sql	或	query	ID	。
	realization		-	 	可选		 	List<String>		，查询对象。
	server		-	 	可选		 	string	，查询节点。
	submitter		-	 	可选		 	List<String>	，查询用户。

Curl	请求示例

curl	-X	GET	\

		'http://host:port/kylin/api/query/download_query_histories_sql?timezone_offset_hour=8&realization=&query_

status=&submitter=&project=default&start_time_from=&start_time_to=&latency_from=&latency_to=&sql='	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-o	query_history.sql

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

965

异步查询	API

异步查询	API

提示：

1.	 请确保已阅读前面的访问及安全认证章节，了解如何在	REST	API	语句中添加认证信息。
2.	 在	Curl	命令行上，如果您访问的	URL	中含有	 	&		符号，请注意转义，比如在	URL	两端加上引号。
3.	 本章节的所有的	get	请求及	delete	by	id	请求均做了向前兼容，即：若在	URL	上没有传	project	参数，在请求

体中传	project	参数也可请求成功。

4.	 由于parquet格式的要求，列的命名不能包含"	,;{}()\n\t="等字符，因此需要在SQL查询中显示定义别名，并且

别名不包含这些特殊字符。

5.	 较早版本的hive不支持读取parquet	date类型字段，因此可以更换原表数据类型为timestamp,或者升级hive到1.2

之后版本。

6.	 自	4.6.4	版本起，为了解决返回大量结果的性能问题，产品进行了变更， 	include_header		参数被移至提交异

步查询的	API，下载结果中的	 	include_header		参数将不起作用。

提交查询

	POST	http://host:port/kylin/api/async_query

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

HTTP	Body:	JSON	Object

	sql		-	 	必选		 	string	，查询语句
	separator		-	 	可选		 	string	，导出结果的分隔符，默认为	 	,		，其它分隔符，如： 	#	,	 	$	,	 	@	,	 	|		也支持。
	offset		-	 	可选		 	int	，查询结果的偏移量
	limit		-	 	可选		 	int	，从偏移量开始返回对应的行数，不足	limit	以实际行数为准
	project		-	 	必选		 	string	，项目名
	format		-	 	可选		 	string	，文件格式，默认为	"csv",	其他可选值为	"json"、"xlsx"	、"parquet"

注意：文件格式为	"xlsx","json"	时，不支持指定分隔符	separator；文件格式为	"parquet"	时，当前不支持
通过	下载查询结果	API下载结果文件，只能直接从	HDFS	上获取。文件格式为	"xlsx"	可能影响性能，不
推荐使用	"xlsx"。

	file_name		-	 	可选		 	string	，文件名（暂不支持中文），默认为	"result"
	spark_queue		-	 	可选		 	string	，指定集群队列，默认值	"default"。开启	 	kylin.query.unique-async-query-yarn-
queue-enabled		后方可生效
	include_header		-	 	可选		 	boolean	，查询结果是否包含表头，默认为	false

Curl	请求示例

curl	-X	POST	\

		'http://host:port/kylin/api/async_query'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{	"sql":"select	*	from	KYLIN_SALES	limit	100",	"project":"learn_kylin",	"format":"csv","encode":"utf-

8",	"file_name":"test"	}'

响应示例

966

异步查询	API

{

				"code":	"000",

				"data":	{

								"query_id":	"eb3e837f-d826-4670-aac7-2b92fcd0c8fe",

								"status":	"RUNNING",

								"info":	"query	still	running"

				},

				"msg":	""

}

响应信息

	query_id		-	异步查询的	Query	ID
	status		-	提交的状态，分为："SUCCESSFUL"	（成功），"RUNNING"（仍在运行中）和	"FAILED"	(失败)	。
	info		-	提交状态的详细信息

返回查询状态

	GET	http://host:port/kylin/api/async_query/{query_id}/status?project=learn_kylin

URL	Parameters

	query_id		-	 	必选		 	string	，异步查询的	Query	ID
	project		-	 	必选		 	string		项目名称

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://host:port/kylin/api/async_query/{query_id}/status?project=learn_kylin'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":	"000",

				"data":	{

								"query_id":	"eb3e837f-d826-4670-aac7-2b92fcd0c8fe",

								"status":	"SUCCESSFUL",

								"info":	"await	fetching	results"

				},

				"msg":	""

}

响应信息

	query_id		-	异步查询的	Query	ID
	status		-	查询状态，分为："SUCCESSFUL"	（成功），"RUNNING"（仍在运行中），"FAILED"	(失败)	和
"MISSING"	(查询不到此查询)	。
	info		-	查询状态的详细信息

返回查询的元数据信息

967

异步查询	API

	GET	http://host:port/kylin/api/async_query/{query_id}/metadata?project=learn_kylin

URL	Parameters

	query_id		-	 	必选		 	string	，异步查询的	Query	ID
	project		-	 	必选		 	string		项目名称

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://host:port/kylin/api/async_query/{query_id}/metadata?project=learn_kylin'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":	"000",

				"data":	[

								[

												"TRANS_ID",

												"PART_DT"

								],

								[

												"BIGINT",

												"DATE"

								]

				],

				"msg":	""

}

响应信息

	data		-	data	中包含两个	list，其中第一个	list	为列名，第二个	list	为列对应的数据类型

返回查询结果文件大小

	GET	http://host:port/kylin/api/async_query/{query_id}/file_status?project=learn_kylin

URL	Parameters

	query_id		-	 	必选		 	string	，异步查询的	Query	ID
	project		-	 	必选		 	string		项目名称

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

请求示例

curl	-X	GET	\

		'http://host:port/kylin/api/async_query/{query_id}/file_status?project=learn_kylin'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

968

异步查询	API

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":	"000",

				"data":	7611,

				"msg":	""

}

响应信息

	data		-	保存结果的总大小

下载查询结果

提示：请确认查询状态为	SUCCESSFUL	之后再调用此接口

	GET	http://host:port/kylin/api/async_query/{query_id}/result_download?include_header=true&project=learn_kylin

注意：自	4.6.4	版本起， 	include_header		参数被移至提交异步查询的	API，下载结果中的	 	include_header
参数将不起作用。

URL	Parameters

	query_id		-	 	必选		 	string	，异步查询的	Query	ID
	project		-	 	必选		 	string	，项目名称

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

		curl	-X	GET	\

				'http://host:port/kylin/api/async_query/{query_id}/result_download?include_header=true&project=learn_kylin'

	\

				-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

				-H	'Accept-Language:	cn'	\

				-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

				-H	'Content-Type:	application/json;charset=utf-8'	\

				-o	result.csv

响应示例

返回一个名为	 	result.csv		的文件

返回查询的	HDFS	路径

	GET	http://host:port/kylin/api/async_query/{query_id}/result_path?project=learn_kylin

URL	Parameters

	query_id		-	 	必选		 	string	，异步查询的	Query	ID
	project		-	 	必选		 	string		项目名称

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

969

异步查询	API

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://host:port/kylin/api/async_query/{query_id}/result_path?project=learn_kylin'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":	"000",

				"data":	"hdfs://host:8020/{kylin_working_dir}/{kylin_metadata_url}/{project}/async_query_result/{query_

id}",

				"msg":	""

}

响应信息

	data		-	该查询的	HDFS	保存路径

删除所有查询结果文件

提示：该接口可能会删除还没有获取到结果的查询。

	DELETE	http://host:port/kylin/api/async_query

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	DELETE	\

		'http://host:port/kylin/api/async_query'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":	"000",

				"data":	true,

				"msg":	""

}

响应信息

	data		-	成功删除所有查询结果文件返回	true，否则返回	false

根据时间删除旧的查询结果文件

提示：该接口可能会删除还没有获取到结果的查询。

970

异步查询	API

	DELETE	http://host:port/kylin/api/async_query?project={project}&older_than={time}

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

URL	Parameters

	project	- 	必选		 	string	，需要删除哪个项目的查询结果文件
	older_than	- 	必选		 	string	，最早保留时间，last_modify	早于此	time	的异步查询结果文件会被删除，时间格
式	 	yyyy-MM-dd	HH:mm:ss	，不需要带上引号。注意：使用	Curl	请求时，需要进行	url	转义，将空格替换为	 	%20
。

Curl	请求示例

curl	-X	DELETE	\

		'http://host:port/kylin/api/async_query?project=learn_kylin&older_than=2021-04-26%2010:00:00'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":	"000",

				"data":	true,

				"msg":	""

}

响应信息

	data		-	成功删除所有旧的查询结果文件返回	true，否则返回	false

根据	query_id	删除查询结果文件

	DELETE	http://host:port/kylin/api/async_query/{query_id}?project=learn_kylin

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

URL	Parameters

	query_id	- 	必选		 	string	，异步查询的	Query	ID
	project		-	 	必选		 	string		项目名称

Curl	请求示例

curl	-X	DELETE	\

		'http://host:port/kylin/api/async_query/{query_id}?project=learn_kylin'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

971

异步查询	API

{

				"code":	"000",

				"data":	true,

				"msg":	""

}

响应信息

	data		-	成功删除 	query_id	对应的的查询结果文件返回	true，否则返回	false

根据	query_id	停止正在运行的异步查询

	DELETE	http://host:port/kylin/api/async_query/stop/{query_id}?project={project}

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

URL	Parameters

	query_id	- 	必选		 	string	，异步查询的	Query	ID
	project		-	 	必选		 	string		项目名称

Curl	请求示例

curl	-X	DELETE	\

		'http://host:port/kylin/api/async_query/stop/642b24ce-3e59-47b1-a87a-6589946c21a6?project=learn_kylin'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":	"000",

				"data":	"",
				"msg":	"ID为642b24ce-3e59-47b1-a87a-6589946c21a6的异步查询正被执行取消。"

}

响应信息

	code		-	成功停止 	query_id	对应的的查询则返回	"000"

已知限制

列名中包含英文逗号	 	,		时，如果指定分隔符	 	separator	，则下载结果表头列名中的英文逗号	 	,		将被替换为分隔
符。

列名中包含分隔符时，可能导致文件格式解析错乱。

发起取消异步查询，到实际完成（hdfs上状态变更）是需要一定时间的，因此并发取消同一个异步查询的时候会有
多个请求都是成功的响应（但不影响最后的结果）。

如果为异步查询配置了独立队列，取消该查询后，该查询不会被记录到查询历史中。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

972

任务	API

任务	API

提示：

1.	 请确保已阅读前面的访问及安全认证章节，了解如何在	REST	API	语句中添加认证信息。

2.	 在	Curl	命令行上，如果您访问的	URL	中含有	 	&		符号，请注意转义，比如在	URL	两端加上引号。

返回任务列表

	GET	http://host:port/kylin/api/jobs

开始生效版本：4.0.12

URL	Parameters

	time_filter		-	 	必选		 	int	，时间范围。对应关系如下：

	project		-	 	可选		 	string	，项目名称

	statuses		-	 	可选		 	string	，任务状态，可选
值： 	PENDING	， 	RUNNING	， 	FINISHED	， 	ERROR	， 	DISCARDED	， 	STOPPED	，多个值之间用逗号分隔

	page_offset		-	 	可选		 	int	，每页返回的任务的偏移量，默认值为	"0"

	page_size		-	 	可选		 	int	，每页返回的任务数量，默认值为	"10"

	sort_by		-	 	可选		 	string	，排序字段，默认为	 	last_modified	，可选	 	project	、
	id	、 	job_name	、 	target_subject	、 	create_time	、 	total_duration	。

	reverse		-	 	可选		 	boolean	，是否倒序，默认为	"true"

	key		-	 	可选		 	string	，筛选字段，目前支持筛选任务	ID	及任务对象名称

	exact		-	 	可选		 	string	，是否和任务对象名称完全匹配.	默认为	false

	type		-	 	可选		 	string	，任务类型，可选值见下表，多个值之间用逗号分隔

|	可选值	|	任务类型	|	|-------|-------|	|INDEX_REFRESH|刷新数据|	|INDEX_MERGE|合并数据|	|INDEX_BUILD|构建
索引|	|INC_BUILD|加载数据|	|TABLE_SAMPLING|抽样表数据|	|SNAPSHOT_BUILD|构建快照|
|SNAPSHOT_REFRESH|刷新快照|	|SUB_PARTITION_BUILD|加载子分区数据|	|SUB_PARTITION_REFRESH|刷
新子分区数据|	|EXPORT_TO_SECOND_STORAGE|加载数据至分层存储|	|SECOND_STORAGE_NODE_CLEAN|
删除分层存储（项目）|	|SECOND_STORAGE_MODEL_CLEAN|删除分层存储（模型）|
|SECOND_STORAGE_SEGMENT_CLEAN|删除分层存储（Segment）|	|SECOND_STORAGE_INDEX_CLEAN|
删除分层存储（索引）|	|SECOND_STORAGE_REFRESH_SECONDARY_INDEXES|刷新	Skipping	索引|

HTTP	Header

973

任务	API

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://host:port/kylin/api/jobs?time_filter=0&page_size=1'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":"000",

				"data":{

								"value":[

												{

																"id":"232bf69f-6cdf-4dcc-a3aa-b6ca7651e98c",

																"last_modified":0,

																"duration":91020,

																"exec_start_time":1577764731199,

																"steps":null,

																"job_status":"FINISHED",

																"job_name":"INDEX_BUILD",

																"data_range_start":0,

																"data_range_end":9223372036854775807,

																"target_model":"5b54898a-dd75-4146-abbe-de77c0cf77fb",

																"target_segments":[

																				"3344c9bb-83fa-4128-803b-e18f27b0ccf8"

																],

																"step_ratio":1,

																"create_time":1577764730069,

																"wait_time":1130,

																"target_subject":"AUTO_MODEL_KYLIN_ACCOUNT_1",

																"target_subject_error":false,

																"project":"test",

																"submitter":"ADMIN",

																"exec_end_time":1577764822219,

																"tag":"mark"

												}

								],

								"offset":0,

								"limit":1,

								"total_size":1364

				},

				"msg":""

}

操作任务

	PUT	http://host:port/kylin/api/jobs/status

URL	Parameters

	action		-	 	必选		 	string	，对任务的操作类型，可选值如下:

	RESUME	，恢复暂停或错误的任务

	DISCARD	，	终止任务
	PAUSE	，	暂停任务
	RESTART	，	重启任务

974

任务	API

	project		-	 	可选		 	string	，	项目名称。如果仅填写项目，表示操作该项目下所有任务。注意： 	project		和
	job_ids		不能同时为空。

	job_ids		-	 	可选		 	array<string>	，	任务	ID。如果仅填写	 	job_ids	，表示操作所有符合对应	ID	的任务。注
意： 	project		和	 	job_ids		不能同时为空。

	statuses		-	 	可选		 	array<string>	，	根据	 	project		和	 	job_ids		的过滤结果筛选某些任务状态，可选值为：

	PENDING	，等待任务

	RUNNING	，运行中的任务

	FINISHED	，已完成的任务

	ERROR	，错误任务

	DISCARDED	，终止任务

	STOPPED	，暂停任务

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	PUT	\

		'http://host:port/kylin/api/jobs/status'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{

									"action"	:	"PAUSE",

									"job_ids"	:	[

												"d7e4a098-10b6-4961-85b4-9eebfe29eb25",

												"80f4d168-1074-4218-875c-4c70a4334029"

									],

									"project"	:	"ssb"

						}'

响应示例

{

				"code":"000",

				"data":"",

				"msg":""

}

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

975

许可证容量	API

许可证容量	API

提示：

1.	 请确保已阅读前面的访问及安全认证章节，了解如何在	REST	API	语句中添加认证信息。

2.	 在	Curl	命令行上，如果您访问的	URL	中含有	 	&		符号，请注意转义，比如在	URL	两端加上引号。

获取项目数据量信息

	GET	http://host:port/kylin/api/system/capacities

开始生效版本：4.2.0

URL	Parameters

	project_names		-	 	可选		 	string	，项目名称列表，用逗号分隔。
	page_offset		-	 	可选		 	int	，分页页面，默认为	 	0	。
	page_size		-	 	可选		 	int	，分页大小，默认为	 	10	。
	sort_by		-	 	可选		 	string	，排序字段，默认为	"capacity"，此外，还支持	name,	capacity_ratio	和	status
	reverse		-	 	可选		 	boolean	，是否倒序，默认为	"true"

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://localhost:7070/kylin/api/system/capacities?project_names=test_project1,test_project2'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

		{

						"code":	"000",

						"data":	{

										"size":	2,

										"capacity_detail":	[

														{

																"name":	"test_project1",

																"capacity":	123123,

																"capacity_ratio":	0.1,

																"status":	"OK"

														}

														,

														{

																		"name":	"test_project2",

																		"capacity":	2223,

																		"capacity_ratio":	0.5,

																		"status":	"ERROR"

													}

										]

						},

						"msg":	""

		}

976

许可证容量	API

获取系统数据量信息

	GET	http://host:port/kylin/api/system/license/capacity

开始生效版本：4.2.0

URL	Parameters:	无

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://localhost:7070/kylin/api/system/license/capacity'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

		{

						"code":	"000",

						"data":

								{

								"current_capacity":	123213,

								"capacity":	2410420101,

								"capacity_status":	"OK",

								"check_time":	1590720522075,

								"first_error_time":	0,

								"error_over_thirty_days":	false,

								"error":	false,

								"evaluation":	false

							}

						,

						"msg":	""

		}

注意：如果返回结果中	capacity	的值为	-1，指的是许可证未对数据量做限制。

获取节点信息

	GET	http://host:port/kylin/api/system/license/nodes

开始生效版本：4.2.0

URL	Parameters:	无

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://localhost:7070/kylin/api/system/license/nodes'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

977

许可证容量	API

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

		{

				"code":	"000",

				"data":

						{

								"current_node":	2,

								"node":	5,

								"node_status":	"OK",

								"error":	false

							},

					"msg":	""

			}

注意：如果返回结果中	 	node		的值为	-1，指的是许可证未对节点数做限制。

刷新系统数据量

	PUT	http://host:port/kylin/api/system/capacity/refresh_all

开始生效版本：4.2.0

URL	Parameters:	无

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	PUT	\

		'http://localhost:7070/kylin/api/system/capacity/refresh_all'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

		{

						"code":	"000",

						"data":

								{

								"current_capacity":	123213,

								"capacity":	2410420101,

								"capacity_status":	"OK",

								"check_time":	1590720522075,

								"first_error_time":	0,

								"error_over_thirty_days":	false,

								"error":	false,

								"evaluation":	false

							}

						,

						"msg":	""

		}

978

许可证容量	API

注意：如果返回结果中	capacity	的值为	-1，指的是许可证未对数据量做限制。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

979

访问控制权限	API

访问控制权限	API

Kyligence	Enterprise	提供了可以用来控制用户对于项目、表、用户和用户组等的访问控制权限的	REST	API，基于这些
API，用户可以严格地管理相关的访问控制权限列表。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

980

访问控制权限	API

用户管理	API

提示：

1.	 请确保已阅读前面的访问及安全认证章节，了解如何在	REST	API	语句中添加认证信息。

2.	 在	Curl	命令行上，如果您访问的	URL	中含有	 	&		符号，请注意转义，比如在	URL	两端加上引号。

返回用户列表

	GET	http://host:port/kylin/api/user

开始生效版本：4.1.4

Request	Parameters

	name		-	 	可选		 	string	，用户名称。
	is_case_sensitive		-	 	可选		 	boolean	，对用户名称的模糊匹配是否区分大小写，默认不区分。
	page_offset		-	 	可选		 	int	，分页页面，默认为	 	0。
	page_size		-	 	可选		 	int	，分页大小，默认为	 	10	。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://localhost:7070/kylin/api/user'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":	"000",

				"data":	{

								"value":	[

												{

																"username":	"test",

																"authorities":	[

																				{

																								"authority":	"ALL_USERS"

																				}

																						...

																],

																"disabled":	false,

																"default_password":	false,

																"locked":	false,

																"uuid":	"af11440a-8e9d-4801-8508-5d0ce0e04a2f",

																"last_modified":	1592296833935,

																"create_time":	1592296833844,

																"locked_time":	0,

																"wrong_time":	0,

																"first_login_failed_time":	0

												}

														...

								],

981

访问控制权限	API

								"offset":	0,

								"limit":	10,

								"total_size":	3

				},

				"msg":	""

}

创建用户

	POST	http://host:port/kylin/api/user

开始生效版本：4.1.4

HTTP	Body:	JSON	Object

	username		-	 	必填		 	string	，用户名。
	password		-	 	必填		 	string	，用户密码。
	disabled		-	 	必填		 	boolean	，是否禁用，可填内容	 	true	（代表该用户处于禁用状态）， 	false	（代表该用户
处于启用状态）。

	authorities		-	 	必填		 	array[string]	，用户所属用户组列表。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	POST	\

		'http://localhost:7070/kylin/api/user'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{

				"username":	"test",

				"password":	"Password@123",

				"disabled":	false,

				"authorities":["ALL_USERS"]

				}'

响应示例

{

				"code":	"000",

				"data":	"",

				"msg":	""

}

修改用户所在用户组或用户状态

注意：修改用户将覆盖更新该用户原有的所属用户组列表。

	PUT	http://host:port/kylin/api/user

开始生效版本：4.1.4

HTTP	Body:	JSON	Object

	username		-	 	必填		 	string	，用户名。

982

访问控制权限	API

	authorities		-	 	选填		 	array[string]	，用户所属用户组列表，不填表示不做任何更改。
	disabled		-	 	选填		 	boolean	，是否禁用，可填内容	 	true	（代表该用户处于禁用状态）， 	false	（代表该用户
处于启用状态），不填表示不做任何更改。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	PUT	\

		'http://localhost:7070/kylin/api/user'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{

				"username":	"createuser",

				"authorities":["ALL_USERS"]

				}'

响应示例

{

				"code":	"000",

				"data":	"",

				"msg":	""

}

修改密码

	PUT	http://host:port/kylin/api/user/password

开始生效版本：4.1.4

HTTP	Body:	JSON	Object

	username		-	 	必填		 	string	，用户名。
	password		-	 	必填		 	string	，用户旧密码。
	new_password		-	 	必填		 	string	，用户新密码。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	PUT	\

		'http://localhost:7070/kylin/api/user/password'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{

				"username":	"test",

				"password":	"Password@123",

				"new_password":	"Password@1234"

				}'

983

访问控制权限	API

响应示例

{

				"code":	"000",

				"data":	"",

				"msg":	""

}

删除用户

	DELETE	http://host:port/kylin/api/user

开始生效版本：4.2.1

HTTP	Body:	JSON	Object

	username		-	 	必填		 	string	，用户名。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	DELETE	\

		'http://localhost:7070/kylin/api/user'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	en'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

		-d	'{

				"username":	"testuser"

				}'

响应示例

{

				"code":	"000",

				"data":	"",

				"msg":	""

}

获取一个用户或用户组的权限

	GET	http://host:port/kylin/api/access/acls

开始生效版本：4.1.4

Request	Parameters

	type		-	 	必填		 	string	，表示用户或用户组，可选值为	 	user		或	 	group	。
	name		-	 	必填		 	string	，用户或用户组名称。
	project		-	 	可选		 	string	，项目名称，填写该值将获取一个用户或用户组在该项目中的所有权限。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

984

访问控制权限	API

Curl	请求示例

curl	-X	GET	\

		'http://localhost:7070/kylin/api/access/acls?type=user&name=ADMIN'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	en'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":	"000",

				"data":	[

								{

												"project_name":	"test",

												"project_permission":	"ADMIN",

												"acl_info":	[

																{

																				"tables":	[

																								{

																												"authorized":	true,

																												"columns":	[

																																{

																																				"authorized":	true,

																																				"column_name":	"C_ADDRESS"

																																}

																																		...

																												],

																												"rows":	[],

																												"table_name":	"CUSTOMER",

																												"authorized_column_num":	8,

																												"total_column_num":	8

																								}

																										...

																				],

																				"authorized_table_num":	6,

																				"total_table_num":	6,

																				"database_name":	"SSB"

																}

																		...

												]

								}

										...

				],

				"msg":	""

}

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

985

访问控制权限	API

用户组管理	API

提示：

1.	 请确保已阅读前面的访问及安全认证章节，了解如何在	REST	API	语句中添加认证信息。

2.	 在	Curl	命令行上，如果您访问的	URL	中含有	 	&		符号，请注意转义，比如在	URL	两端加上引号。

返回用户组列表

	GET	http://host:port/kylin/api/user_group/groups

开始生效版本：4.1.4

请求参数

	group_name		-	 	可选		 	string	，用户组名称。
	is_case_sensitive		-	 	可选		 	boolean	，对用户组名称的模糊匹配是否区分大小写，默认为	 	false		不区分。
	page_offset		-	 	可选		 	int	，分页页面，默认为	 	0	。
	page_size		-	 	可选		 	int	，分页大小，默认为	 	10	。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://localhost:7070/kylin/api/user_group/groups`'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":	"000",

				"data":	{

								"value":	[

												"ALL_USERS",

												"ROLE_ADMIN",

												"ROLE_ANALYST",

												"ROLE_MODELER"

														...

								],

								"offset":	0,

								"limit":	10,

								"total_size":	7

				},

				"msg":	""

}

返回指定用户组的用户列表

	GET	http://host:port/kylin/api/user_group/group_members/{group_name}

开始生效版本：4.1.4

986

访问控制权限	API

URL	参数

	group_name		-	 	必填		 	string	，用户组名称。

请求参数

	username		-	 	可选		 	string	，用户名。
	page_offset		-	 	可选		 	int	，分页页面，默认为	 	0。
	page_size		-	 	可选		 	int	，分页大小，默认为	 	10	。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://localhost:7070/kylin/api/user_group/group_members/test'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":	"000",

				"data":	{

								"value":	[

												{

																"username":	"ADMIN",

																"authorities":	[

																				{

																								"authority":	"ROLE_ADMIN"

																				},

																				{

																								"authority":	"ALL_USERS"

																				}

																],

																"disabled":	false,

																"default_password":	false,

																"locked":	false,

																"uuid":	"aaf02c5d-1605-42fa-abf9-9b0bb5715a6a",

																"last_modified":	1592555313558,

																"create_time":	1586744927779,

																"locked_time":	0,

																"wrong_time":	0,

																"first_login_failed_time":	0

												}

														...

								],

								"offset":	0,

								"limit":	10,

								"total_size":	10

				},

				"msg":	""

}

增加用户组

	POST	http://host:port/kylin/api/user_group

开始生效版本：4.2.1

987

访问控制权限	API

HTTP	Body:	JSON	Object

	group_name		-	 	必填		 	string	，用户组名称。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	POST	\

		'http://localhost:7070/kylin/api/user_group'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{

				"group_name":	"test_group"

				}'

响应示例

{

				"code":	"000",

				"data":	"",

				"msg":	"add	user	group"

}

更新用户组

注意：更新用户组将覆盖原有的用户列表。

	PUT	http://host:port/kylin/api/user_group/users

开始生效版本：4.1.4

HTTP	Body:	JSON	Object

	group_name		-	 	必填		 	string	，用户组名称。
	users		-	 	必填		 	array[string]	，用户组中的用户列表。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	PUT	\

		'http://localhost:7070/kylin/api/user_group/users'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{

				"group_name":	"test",

				"users":["ANALYST",	"MODELER"]

				}'

响应示例

988

访问控制权限	API

{

				"code":	"000",

				"data":	"",

				"msg":	"modify	users	in	user	group"

}

删除用户组

	DELETE	http://host:port/kylin/api/user_group

开始生效版本：4.2.1

HTTP	Body:	JSON	Object

	group_name		-	 	必填		 	string	，用户组名称。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	DELETE	\

		'http://localhost:7070/kylin/api/user_group'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

		-d	'{

				"group_name":	"test_group"

				}'

响应示例

{

				"code":	"000",

				"data":	"",

				"msg":	"del	user	group"

}

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

989

访问控制权限	API

项目级权限管理	API

提示：

1.	 请确保已阅读前面的访问及安全认证章节，了解如何在	REST	API	语句中添加认证信息。

2.	 在	Curl	命令行上，如果您访问的	URL	中含有	 	&		符号，请注意转义，比如在	URL	两端加上引号。

获取项目级访问权限

	GET	http://host:port/kylin/api/access/project

开始生效版本：4.1.4

请求参数

	project		-	 	必填		 	string	，项目名称。
	name		-	 	可选		 	string	，用户/用户组名称。
	page_offset		-	 	可选		 	int	，分页页面，默认为	 	0。
	page_size		-	 	可选		 	int	，分页大小，默认为	 	10	。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://localhost:7070/kylin/api/access/project?project=kyligence'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":	"000",

				"data":	{

								"value":	[

												{

																"type":	"user",

																"name":	"ADMIN",

																"permission":	"ADMIN",

																"ext_permissions":	[

																		"DATA_QUERY"

																]

												},

												{

																"type":	"group",

																"name":	"TEST_GROUP",

																"permission":	"QUERY"

												}

								],

								"offset":	0,

								"limit":	10,

								"total_size":	2

				},

				"msg":	""

990

访问控制权限	API

}

授予项目级访问权限

	POST	http://host:port/kylin/api/access/project

开始生效版本：4.1.4

HTTP	Body:	JSON	Object

	project		-	 	必填		 	string	，项目名称。
	type		-	 	必填		 	string	，表示用户或用户组，可选值为	 	user		或	 	group	。
	permission		-	 	必填		 	string	，表示用户或用户组权限，可选值为	 	QUERY	、 	OPERATION	、
	MANAGEMENT	、 	ADMIN	。

	names		-	 	必填		 	array[string]	，用户或用户组名称列表。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	POST	\

		'http://localhost:7070/kylin/api/access/project'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{

		"project":	"kyligence",

				"type":	"user",

				"permission":	"QUERY",

				"names":["test"]

				}'

响应示例

{

				"code":	"000",

				"data":	"",

				"msg":	""

}

更新项目级访问权限（覆盖更新）

	PUT	http://host:port/kylin/api/access/project

开始生效版本：4.1.4

HTTP	Body:	JSON	Object

	project		-	 	必填		 	string	，项目名称。
	type		-	 	必填		 	string	，表示用户或用户组，可选值为	 	user		或	 	group	。
	permission		-	 	必填		 	string	，表示用户或用户组权限，可选值为	 	QUERY	、 	OPERATION	、
	MANAGEMENT	、 	ADMIN	。

	name		-	 	必填		 	string	，用户或用户组名称。

HTTP	Header

991

访问控制权限	API

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	PUT	\

		'http://localhost:7070/kylin/api/access/project'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{

		"project":	"kyligence",

				"type":	"user",

				"permission":	"ADMIN",

				"name":	"test"

				}'

响应示例

{

				"code":	"000",

				"data":	"",

				"msg":	""

}

删除项目级访问权限

	DELETE	http://host:port/kylin/api/access/project

开始生效版本：4.1.4

请求参数

	project		-	 	必填		 	string	，项目名称。
	type		-	 	必填		 	string	，表示用户或用户组，可选值为	 	user		或	 	group	。
	name		-	 	必填		 	string	，用户或用户组名称。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	DELETE	\

		'http://localhost:7070/kylin/api/access/project?project=kyligence&type=user&name=test'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":	"000",

				"data":	"",

				"msg":	""

}

992

访问控制权限	API

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

993

访问控制权限	API

表行列级权限管理	API

提示：

1.	 请确保已阅读前面的访问及安全认证章节，了解如何在	REST	API	语句中添加认证信息。

2.	 在	Curl	命令行上，如果您访问的	URL	中含有	 	&		符号，请注意转义，比如在	URL	两端加上引号。

获取表行列级权限

	GET	http://localhost:port/kylin/api/acl/{type}/{name}?authorized_only=true&project=m

URL	Parameters

	type		-	 	必选		 	string	，用户类型，可选值：user，group，大小写不敏感。
	name		-	 	必选		 	string	，用户或用户组名称。
	project		-	 	必选		 	string	，项目名称。
	authorized_only		-	 	可选		 	boolean	，是否只返回有权限的表行列，默认值 	false	。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://localhost:7070/kylin/api/acl/User/bb?authorized_only=true&project=m'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":	"000",

				"data":	[

								{

												"tables":	[

																{

																				"authorized":	true,

																				"columns":	[

																								{

																												"authorized":	true,

																												"column_name":	"C_ADDRESS",

																												"data_mask_type":	"AS_NULL",

																												"dependent_columns":	null,

																												"datatype":	"varchar(4096)"

																								},

																								{

																												"authorized":	true,

																												"column_name":	"C_CITY",

																												"data_mask_type":	"DEFAULT",

																												"dependent_columns":	null,

																												"datatype":	"varchar(4096)"

																								},

																								{

																												"authorized":	false,

																												"column_name":	"C_CUSTKEY",

																												"data_mask_type":	null,

994

访问控制权限	API

																												"dependent_columns":	null,

																												"datatype":	"integer"

																								},

																								{

																												"authorized":	true,

																												"column_name":	"C_MKTSEGMENT",

																												"data_mask_type":	null,

																												"dependent_columns":	null,

																												"datatype":	"varchar(4096)"

																								},

																								{

																												"authorized":	true,

																												"column_name":	"C_NAME",

																												"data_mask_type":	null,

																												"dependent_columns":	null,

																												"datatype":	"varchar(4096)"

																								},

																								{

																												"authorized":	true,

																												"column_name":	"C_NATION",

																												"data_mask_type":	null,

																												"dependent_columns":	null,

																												"datatype":	"varchar(4096)"

																								},

																								{

																												"authorized":	true,

																												"column_name":	"C_PHONE",

																												"data_mask_type":	null,

																												"dependent_columns":	null,

																												"datatype":	"varchar(4096)"

																								},

																								{

																												"authorized":	true,

																												"column_name":	"C_REGION",

																												"data_mask_type":	null,

																												"dependent_columns":	null,

																												"datatype":	"varchar(4096)"

																								}

																				],

																				"row_filter":	{

																								"type":	"AND",

																								"filter_groups":	[]

																				},

																				"table_name":"ANALYSIS_PACKAGE_TABLE",

																				"authorized_column_num":10,

																				"total_column_num":10

																},

																{

																				"authorized":	true,

																				"columns":	[

																								{

																												"authorized":	true,

																												"column_name":	"LO_COMMITDATE",

																												"data_mask_type":	null,

																												"dependent_columns":	null,

																												"datatype":	"date"

																								},

																								{

																												"authorized":	true,

																												"column_name":	"LO_CUSTKEY",

																												"data_mask_type":	null,

																												"dependent_columns":	null,

																												"datatype":	"integer"

																								},

																								{

																												"authorized":	true,

																												"column_name":	"LO_DISCOUNT",

																												"data_mask_type":	null,

																												"dependent_columns":	null,

995

访问控制权限	API

																												"datatype":	"bigint"

																								},

																								{

																												"authorized":	true,

																												"column_name":	"LO_EXTENDEDPRICE",

																												"data_mask_type":	null,

																												"dependent_columns":	null,

																												"datatype":	"bigint"

																								},

																								{

																												"authorized":	true,

																												"column_name":	"LO_LINENUMBER",

																												"data_mask_type":	null,

																												"dependent_columns":	null,

																												"datatype":	"bigint"

																								},

																								{

																												"authorized":	true,

																												"column_name":	"LO_ORDERDATE",

																												"data_mask_type":	null,

																												"dependent_columns":	null,

																												"datatype":	"date"

																								},

																								{

																												"authorized":	true,

																												"column_name":	"LO_ORDERKEY",

																												"data_mask_type":	null,

																												"dependent_columns":	null,

																												"datatype":	"bigint"

																								},

																								{

																												"authorized":	true,

																												"column_name":	"LO_ORDERPRIOTITY",

																												"data_mask_type":	null,

																												"dependent_columns":	null,

																												"datatype":	"varchar(4096)"

																								},

																								{

																												"authorized":	true,

																												"column_name":	"LO_ORDTOTALPRICE",

																												"data_mask_type":	null,

																												"dependent_columns":	null,

																												"datatype":	"bigint"

																								},

																								{

																												"authorized":	true,

																												"column_name":	"LO_PARTKEY",

																												"data_mask_type":	null,

																												"dependent_columns":	null,

																												"datatype":	"integer"

																								},

																								{

																												"authorized":	true,

																												"column_name":	"LO_QUANTITY",

																												"data_mask_type":	null,

																												"dependent_columns":	null,

																												"datatype":	"bigint"

																								},

																								{

																												"authorized":	true,

																												"column_name":	"LO_REVENUE",

																												"data_mask_type":	null,

																												"dependent_columns":	null,

																												"datatype":	"bigint"

																								},

																								{

																												"authorized":	true,

																												"column_name":	"LO_SHIPMODE",

																												"data_mask_type":	null,

996

访问控制权限	API

																												"dependent_columns":	null,

																												"datatype":	"varchar(4096)"

																								},

																								{

																												"authorized":	true,

																												"column_name":	"LO_SHIPPRIOTITY",

																												"data_mask_type":	null,

																												"dependent_columns":	null,

																												"datatype":	"integer"

																								},

																								{

																												"authorized":	true,

																												"column_name":	"LO_SUPPKEY",

																												"data_mask_type":	null,

																												"dependent_columns":	null,

																												"datatype":	"integer"

																								},

																								{

																												"authorized":	true,

																												"column_name":	"LO_SUPPLYCOST",

																												"data_mask_type":	null,

																												"dependent_columns":	null,

																												"datatype":	"bigint"

																								},

																								{

																												"authorized":	true,

																												"column_name":	"LO_TAX",

																												"data_mask_type":	null,

																												"dependent_columns":	null,

																												"datatype":	"bigint"

																								},

																								{

																												"authorized":	true,

																												"column_name":	"V_REVENUE",

																												"data_mask_type":	null,

																												"dependent_columns":	null,

																												"datatype":	"bigint"

																								}

																				],

																				"row_filter":	{

																								"type":	"AND",

																								"filter_groups":	[]

																				},

																				"table_name":"QUERY_FACT_TABLE",

																				"authorized_column_num":11,

																				"total_column_num":11

																}

												],

												"authorized_table_num":	2,

												"total_table_num":	2,

												"database_name":	"SSB"

								}

				],

				"msg":	""

}

更新表行列级权限

	PUT	http://localhost:port/kylin/api/acl/{type}/{name}?project=m

URL	Parameters

	type		-	 	必选		 	string	，用户类型，可选值：user，group，大小写不敏感。
	name		-	 	必选		 	string	，用户或用户组名称。
	project		-	 	必选		 	string	，项目名称。

HTTP	Body

997

访问控制权限	API

注意：支持对表、行、列权限的单独更新。

	database_name		-	 	必选		 	string	，数据库名称，大小写不敏感。
	tables		-	 	必选		 	array[string]		表的信息。

	table_name		-	 	必选		 	string		表的名称，大小写不敏感。
	authorized		-	 	可选		 	boolean		是否授权该表权限， 	true		代表授权， 	false		代表不授权，默认值是
	false	。

	columns		-	 	可选		 	array[string]		列级权限，需要授予或者取消列级权限时设置，不修改可不设值。

	column_name		-	 	必选		 	string		列的名称，大小写不敏感。
	authorized		-	 	可选		 	boolean		是否授权该列权限， 	true		代表授权， 	false		代表不授权，默认值是
	false	。

	data_mask_type		-	 	可选		 	string	,	脱敏参数，可选值:	DEFAULT,	AS_NULL.	如下

{

		"authorized":true,

		"columns":[

						{

										"authorized":true,

										"column_name":"STORE_AND_FWD_FLAG",

										"data_mask_type":null,

										"dependent_columns":null

						},

						{

										"authorized":true,

										"column_name":"TOTAL_AMOUNT",

										"data_mask_type":"DEFAULT",

										"dependent_columns":null

						},

						{

										"authorized":true,

										"column_name":"TRIP_DISTANCE",

										"data_mask_type":"AS_NULL",

										"dependent_columns":null

						}

		]

}

DEFAULT:	使用该列类型的默认值作为脱敏值，例如	int的默认值为0,	varchar的默认值为**
AS_NULL:	使用null作为脱敏值

	dependent_columns		-	 	可选		 	array		关联行值的列级权限控制参数.	如下

{

		"authorized":true,

		"column_name":"PASSENGER_COUNT",

		"data_mask_type":null,

		"dependent_columns":[

						{

										"column_identity":"DEFAULT.GREEN_TRIP_DATA.DO_LOCATION_ID",

										"values":[

														"1",

														"2"

										]

						}

		]

}

PASSENGER_COUNT	列的值依赖于列	DEFAULT.GREEN_TRIP_DATA.DO_LOCATION_ID	设置的
值

	row_filter		-	 	可选		需要修改行级权限时设置，不修改可不设置。

998

访问控制权限	API

	type		-	 	可选		 	string		设置过滤组之间由 	AND	还是 	OR	作为逻辑操作符，默认值为 	AND	。
	filter_groups		-	 	可选		 	array[string]		设置过滤组或过滤器，默认为空。

	type		-	 	可选		 	string		设置过滤器之间由 	AND	还是 	OR	作为逻辑操作符，默认值为 	AND	。
	is_group		-	 	必选		 	boolean		设置添加的是过滤器还是过滤组。
	filters		-	 	可选		 	array[string]		设置过滤器，默认为空。

	column_name		-	 	必选		 	string		设置行级权限所作用于的列名。
	in_items		-	 	可选		 	array[string]		in	操作过滤条件的值，默认为空。
	like_items		-	 	可选		 	array[string]		like	操作匹配模式的值，默认为空。

举例，以下的请求会设置一个拥有两个过滤器的过滤组，和一个单独的过滤器。过滤组与过

滤器中由 	OR	作为逻辑操作符。第一个过滤组中，两个过滤器由 	AND	作为逻辑操作符。

{

		"row_filter":	{

						"type":	"OR",

						"filter_groups":	[{

										"type":	"AND",

										"filters":	[

														{

																		"column_name":	"LSTG_FORMAT_NAME",

																		"in_items":	["ABIN",	"Others"],

																		"like_items":	["B%"]

														},

														{

																		"column_name":	"TRANS_ID",

																		"in_items":	["0",	"1"],

																		"like_items":	[]

														}

										],

										"is_group":	true

						},	{

										"type":	"AND",

										"filters":	[

														{

																		"column_name":	"TRANS_ID",

																		"in_items":	["0"],

																		"like_items":	[]

														}

										],

										"is_group":	false

						}]

		}

}

赋权成功后，只能查看到符合以下	sql	筛选条件的行：

(

		(LSTG_FORMAT_NAME	in	('ABIN',	'Others')	OR	LSTG_FORMAT_NAME	like	'B%')

		AND

		(TRANS_ID	in	(0,	1))

)	OR	(

		(TRANS_ID	in	(0))

)

如您需要设置行级权限，那么	 	column_name	， 	in_items		和	 	like_items		参数都需要填写。
此字段采用全量覆盖的更新方法。如果您想要清空行级权限，只需要传递一个空的

	filter_groups		即可，如下：

{

		"row_filter":

999

访问控制权限	API

						{

										"type":	"AND",

										"filter_groups":	[]

						}

}

注意：	如果您还在使用	Kyligence	Enterprise	4.3.3	版本之前的行级权限管理	API	来进行更新与查询，会遇
到更新失败的情况。建议统一使用最新的	API	来进行行级权限的管理。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

授权/取消授权表下所有列的权限，表下所有的列都会被取消授权，行级权限也会被取消。只会更新指定的
表，不更新其他表。

		curl	-X	PUT	'http://localhost:8080/kylin/api/acl/User/user_1?project=project_1'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46a3lsaW5AMjAyMA=='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		--data	'[

						{

										"tables":	[

														{

																		"authorized":	false,

																		"table_name":	"CUSTOMER"

														}

										],

										"database_name":	"SSB"

						}

		]'

授权/取消授权列级权限。只会更新指定的列，不更新其他列。

		curl	-X	PUT	'http://localhost:8080/kylin/api/acl/User/user_1?project=project_1'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46a3lsaW5AMjAyMA=='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		--data	'[

						{

										"tables":	[

														{

																		"columns":	[

																						{

																										"authorized":	false,

																										"column_name":	"C_CITY"

																						}

																		],

																		"authorized":	true,

																		"table_name":	"CUSTOMER"

														},

														{

																		"columns":	[

																						{

																										"authorized":	true,

																										"column_name":	"LO_REVENUE",

																										"data_mask_type":	"AS_NULL"

																						},

																						{

1000

访问控制权限	API

																										"authorized":	true,

																										"column_name":	"LO_TAX",

																										"data_mask_type":	"DEFAULT"

																						},

																						{

																										"authorized":	true,

																										"column_name":	"LO_QUANTITY",

																										"data_mask_type":	null,

																										"dependent_columns":	[

																														{

																																		"column_identity":	"SSB.CUSTOMER.C_CUSTKEY",

																																		"values":	[

																																						"1",

																																						"2"

																																		]

																														}

																										]

																						}

																		],

																		"authorized":	true,

																		"table_name":	"P_LINEORDER"

														}

										],

										"database_name":	"SSB"

						}

		]'

授权/取消授权行级权限。全量更新指定表的行级权限，不更新其他表的行级权限。

curl	-X	PUT	'http://localhost:8080/kylin/api/acl/User/user_1?project=project_1'	\

-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

-H	'Accept-Language:	cn'	\

-H	'Authorization:	Basic	QURNSU46a3lsaW5AMjAyMA=='	\

-H	'Content-Type:	application/json;charset=utf-8'	\

--data	'[

		{

						"tables":	[

										{

														"authorized":	true,

														"row_filter":

														{

																		"type":	"AND",

																		"filter_groups":	[

																						{

																										"type":	"AND",

																										"filters":	[

																														{

																																		"column_name":	"C_NATION",

																																		"in_items":	["CHINA",	"UNITED	KINGDOM"],

																																		"like_items":	[]

																														}

																										],

																										"is_group":	false

																						},

																						{

																										"type":	"AND",

																										"filters":	[

																														{

																																		"column_name":	"C_CUSTKEY",

																																		"in_items":	["15",	"16",	"19"],

																																		"like_items":	[]

																														}

																										],

																										"is_group":	false

																						}

																		]

														},

1001

访问控制权限	API

														"table_name":	"CUSTOMER"

										},

										{

														"row_filter":

														{

																		"type":	"AND",

																		"filter_groups":	[

																						{

																										"type":	"AND",

																										"filters":	[

																														{

																																		"column_name":	"LO_CUSTKEY",

																																		"in_items":	["15",	"16",	"20"],

																																		"like_items":	[]

																														}

																										],

																										"is_group":	false

																						},

																						{

																										"type":	"AND",

																										"filters":	[

																														{

																																		"column_name":	"LO_QUANTITY",

																																		"in_items":	["31",	"33",	"23"],

																																		"like_items":	[]

																														}

																										],

																										"is_group":	false

																						},

																						{

																										"type":	"AND",

																										"filters":	[

																														{

																																		"column_name":	"LO_ORDERDATE",

																																		"in_items":	["1995-02-01",	"1996-01-26",	"1992-11-21"],

																																		"like_items":	[]

																														}

																										],

																										"is_group":	false

																						}

																		]

														},

														"authorized":	true,

														"table_name":	"P_LINEORDER"

										}

						],

						"database_name":	"SSB"

		}

]'

响应示例

		{

						"code":	"000",

						"data":	"",

						"msg":	""

		}

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

1002

实时功能	API

实时任务	API

提示：

1.	 请确保已阅读前面的访问及安全认证章节，了解如何在	REST	API	语句中添加认证信息。

2.	 在	Curl	命令行上，如果您访问的	URL	中含有	 	&		符号，请注意转义，比如在	URL	两端加上引号。

返回任务列表

	GET	http://host:port/kylin/api/streaming_jobs

开始生效版本：4.5.8.2

使用场景

获取实时任务的详细信息，可根据任务的状态等信息提供运维决策。

URL	Parameters

	model_name		-	 	可选		 	string	，模糊匹配model	name

	model_names		-	 	可选		 	array<string>	，精确匹配model	name列表

	job_types		-	 	可选		 	array<string>	，job类型，可选值： 	STREAMING_MERGE	， 	STREAMING_BUILD

	statuses		-	 	可选		 	array<string>	，job状态，可选值： 	STARTING	， 	RUNNING	， 	STOPPING	， 	ERROR
， 	STOPPED

	project		-	 	可选		 	string	，项目名称

	page_offset		-	 	可选		 	int	，每页返回的任务的偏移量，默认值为	"0"

	page_size		-	 	可选		 	int	，每页返回的任务数量，默认值为	"10"

	sort_by		-	 	可选		 	string	，排序字段，默认为	 	last_modified	，可选
值： 	model_alias	、 	data_latency	、 	last_status_duration	、 	last_modified

	reverse		-	 	可选		 	boolean	，是否倒序，默认为	"true"

	job_ids		-	 	可选		 	array<string>	，任务id列表，当 	job_ids	不为空时，要求 	project	也不能为空

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://host:port/kylin/api/streaming_jobs'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应字段

	code	： 	String	，响应码，返回值： 	000		（请求处理成功），	 	999	（请求处理失败）。
	data	： 	JSON	，返回数据。

1003

实时功能	API

	value	：返回值的详细信息，各字段解释如下：

	uuid	： 	String	，任务Id。
	last_modified	： 	Long	，模型最后修改时间。

	version	： 	String	，系统元数据版本号。

	mvcc	： 	Long	，元数据修改版本号。

	model_alias	： 	String	，model别名。
	owner	： 	String	，任务的所有者。

	model_id	： 	String	，模型ID。
	last_start_time	： 	Long	，任务上一次的开始时间。

	last_end_time	： 	Long	，任务上一次的结束时间。

	last_update_time	： 	Long	，任务上一次的更新时间。

	last_batch_count	： 	Long	，上一次消费的消息数。

	subscribe	： 	String	，topic名称。
	fact_table	： 	String	，事实表。

	job_status	： 	String	，任务状态，可能

值： 	STARTING	， 	RUNNING	， 	STOPPING	， 	ERROR	， 	STOPPED	。

	job_type	： 	String	，任务类型，可能值： 	STREAMING_MERGE	， 	STREAMING_BUILD	。

	process_id	： 	String	，任务的进程ID。
	node_info	： 	String	，运行任务的节点信息。

	job_execution_id	： 	String	，任务的执行ID。
	yarn_app_id	： 	String	，任务在yarn上运行的ApplicationId。
	yarn_app_url	： 	String	，任务在yarn上运行的Application地址。
	project	： 	String	，项目名称。

	skip_listener	： 	Boolean	，是否不使用监听器。

	action	： 	String	，任务当前所处的动作。

	model_broken	： 	Boolean	，模型是否不可用。

	data_latency	： 	Long	，数据的最小延迟时间（ms）。
	last_status_duration	： 	Long	，最近状态的持续时间（ms）。
	model_indexes	： 	Int	，索引的总个数。

	launching_error	： 	Boolean	，是否启动失败。

	params	： 	JSON	，构建参数。

	partition_desc	： 	JSON	，分区列设置。

	offset	：页码。

	limit	：每页显示任务数。

	total_size	：总任务数。

	msg	： 	String	，报错信息。

响应示例

		{

		"code":	"000",

		"data":	{

				"value":	[

						{

								"uuid":	"7bccf62d-535c-70b8-8271-eaef3985aa96_merge",

								"last_modified":	1645186414513,

								"create_time":	1644823384864,

								"version":	"4.0.0.0",

								"mvcc":	-1,

								"model_alias":	"hy_model",

								"owner":	"ADMIN",

								"model_id":	"7bccf62d-535c-70b8-8271-eaef3985aa96",

								"last_start_time":	null,

								"last_end_time":	null,

								"last_update_time":	"2022-02-18	19:21:27",

								"last_batch_count":	null,

1004

实时功能	API

								"subscribe":	null,

								"fact_table":	"BASE.HY_LINEORDER",

								"job_status":	"ERROR",

								"job_type":	"STREAMING_MERGE",

								"process_id":	null,

								"node_info":	null,

								"job_execution_id":	null,

								"yarn_app_id":	"",

								"yarn_app_url":	"",

								"params":	{

										"spark.executor.memory":	"1g",

										"kylin.streaming.segment-max-size":	"32m",

										"spark.master":	"yarn",

										"spark.driver.memory":	"512m",

										"spark.executor.cores":	"2",

										"kylin.streaming.job-retry-enabled":	"false",

										"spark.executor.instances":	"2",

										"kylin.streaming.segment-merge-threshold":	"3",

										"spark.sql.shuffle.partitions":	"8"

								},

								"project":	"p1",

								"skip_listener":	false,

								"action":	null,

								"model_broken":	false,

								"data_latency":	null,

								"last_status_duration":	240562073,

								"model_indexes":	3,

								"launching_error":	false,

								"partition_desc":	{

										"partition_date_column":	"HY_LINEORDER.LO_PARTITIONCOLUMN",

										"partition_date_start":	0,

										"partition_date_format":	"yyyy-MM-dd	HH:mm:ss",

										"partition_type":	"APPEND",

										"partition_condition_builder":	"org.apache.kylin.metadata.model.PartitionDesc$DefaultPartitionCon

ditionBuilder"

								}

						},

						{

								"uuid":	"7bccf62d-535c-70b8-8271-eaef3985aa96_build",

								"last_modified":	1645186414089,

								"create_time":	1644823384857,

								"version":	"4.0.0.0",

								"mvcc":	-1,

								"model_alias":	"hy_model",

								"owner":	"ADMIN",

								"model_id":	"7bccf62d-535c-70b8-8271-eaef3985aa96",

								"last_start_time":	null,

								"last_end_time":	null,

								"last_update_time":	"2022-02-18	17:43:27",

								"last_batch_count":	null,

								"subscribe":	null,

								"fact_table":	"BASE.HY_LINEORDER",

								"job_status":	"ERROR",

								"job_type":	"STREAMING_BUILD",

								"process_id":	null,

								"node_info":	null,

								"job_execution_id":	null,

								"yarn_app_id":	"application_1643095564973_0592",

								"yarn_app_url":	"http://10.1.2.210:8088/proxy/application_1643095564973_0592/",

								"params":	{

										"spark.executor.memory":	"1g",

										"spark.master":	"yarn",

										"spark.driver.memory":	"512m",

										"kylin.streaming.kafka-conf.maxOffsetsPerTrigger":	"0",

										"kylin.streaming.duration":	"30",

										"spark.executor.cores":	"2",

										"kylin.streaming.job-retry-enabled":	"false",

										"spark.executor.instances":	"2",

										"spark.sql.shuffle.partitions":	"8"

1005

实时功能	API

								},

								"project":	"p1",

								"skip_listener":	false,

								"action":	null,

								"model_broken":	false,

								"data_latency":	0,

								"last_status_duration":	246442660,

								"model_indexes":	3,

								"launching_error":	false,

								"partition_desc":	{

										"partition_date_column":	"HY_LINEORDER.LO_PARTITIONCOLUMN",

										"partition_date_start":	0,

										"partition_date_format":	"yyyy-MM-dd	HH:mm:ss",

										"partition_type":	"APPEND",

										"partition_condition_builder":	"org.apache.kylin.metadata.model.PartitionDesc$DefaultPartitionCon

ditionBuilder"

								}

						}

				],

				"offset":	0,

				"limit":	10,

				"total_size":	2

		},

		"msg":	""

}

操作任务

	PUT	http://host:port/kylin/api/streaming_jobs/status

开始生效版本：4.5.8.2

使用场景

修改任务的状态，如在发现任务异常后可重启该任务。

URL	Parameters

	action		-	 	必选		 	string	，对任务的操作类型，可选值如下:

	START	，启动

	STOP	，	停止
	FORCE_STOP	，	立即停止
	RESTART	，	重启

	project		-	 	可选		 	string	，	项目名称。

	job_ids		-	 	必选		 	array<string>	，	任务	ID。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	--location	--request	PUT	'http://host:port/kylin/api/streaming_jobs/status'	\

	-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

	-H	'Accept-Language:	cn'	\

	-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

	-H	'Content-Type:	application/json;charset=utf-8'	\

	-d	'{

			"project":	"p1",

			"action":	"RESTART",

			"job_ids":	[

1006

实时功能	API

			"7bccf62d-535c-70b8-8271-eaef3985aa96_merge"

			]

	}'

响应字段

	code	： 	String	，响应码，返回值： 	000		（请求处理成功），	 	999	（请求处理失败）。
	data	： 	String	，返回的数据，此处总为空。

	msg	： 	String	，报错信息。

响应示例

{

				"code":"000",

				"data":"",

				"msg":""

}

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

1007

实时功能	API

自定义解析器	Jar	包管理	API

提示：

1.	 请确保已阅读前面的访问及安全认证章节，了解如何在	REST	API	语句中添加认证信息。

2.	 在	Curl	命令行上，如果您访问的	URL	中含有	 	&		符号，请注意转义，比如在	URL	两端加上引号。

加载Jar
删除Jar
获取解析器列表

删除解析器

加载Jar

	POST	http://host:port/kylin/api/custom/jar

HTTP	Body:	form-data

	project		-	 	必选		 	string	，项目名称

	file		-	 	必选		 	File	，需加载的Jar文件

	jar_type		-	 	必选		 	string	,	Jar文件使用类别

注意：用于解析器的jar_type只有"STREAMING_CUSTOM_PARSER"。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	multipart/form-data

Curl	请求示例

		curl	-X	POST	\

				'http://host:port/kylin/api/custom/jar'	\

				-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

				-H	'Accept-Language:	cn'	\

				-H	'Content-Type:	multipart/form-data'	\

				-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

				-F	'file=@"/**/**/custom_parser.jar"'	\

				-F	'project="TestProject"'	\

				-F	'jar_type="STREAMING_CUSTOM_PARSER"'

响应字段

	data	，成功加载的解析器全路径数组

响应示例

{

				"code":	"000",

				"data":	[

						"org.apache.kylin.parser.JsonDataParser1",

						"org.apache.kylin.parser.JsonDataParser2"

				],

				"msg":	""

}

1008

实时功能	API

删除Jar

	DELETE	http://host:port/kylin/api/custom/jar

URL	Parameters

	project		-	 	必选		 	string	，项目名称

	jar_name		-	 	required		 	string	,	要删除的JAR的文件名

	jar_type		-	 	必选		 	string	,	Jar文件使用类别

注意：用于解析器的jar_type只有	"STREAMING_CUSTOM_PARSER"。

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

		curl	-X	DELETE	\

				'http://host:port/kylin/api/custom/jar?project=TestProject&jar_name=custom_parser1.jar&jar_type="STREAM

ING_CUSTOM_PARSER'	\

				-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

				-H	'Accept-Language:	cn'	\

				-H	'Content-Type:	application/json;charset=utf-8'	\

				-H	'Authorization:	Basic	QURNSU46S1lMSU4='

响应字段

	data	，成功删除的Jar文件名

响应示例

		{

						"code":	"000",

						"data":	"custom_parser1.jar",

						"msg":	""

		}

获取解析器列表

	GET	http://host:port/kylin/api/kafka/parsers

URL	Parameters

	project		-	 	必选		 	string	，项目名称

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

		curl	-X	GET	\

				'http://host:port/kylin/api/kafka/parsers?project=TestProject'	\

				-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

				-H	'Accept-Language:	cn'	\

				-H	'Content-Type:	application/json;charset=utf-8'	\

				-H	'Authorization:	Basic	QURNSU46S1lMSU4='

1009

实时功能	API

响应字段

	data	，已加载的Parser数组

响应示例

		{

						"code":	"000",

						"data":	[

										"org.apache.kylin.parser.CsvDataParser2",

										"org.apache.kylin.parser.JsonDataParser2",

										"org.apache.kylin.parser.TimedJsonStreamParser"

						],

						"msg":	""

		}

删除解析器

	DELETE	http://host:port/kylin/api/kafka/parser

URL	Parameters

	project		-	 	必选		 	string	，项目名称

	className		-	 	必选		 	string	，需删除解析器全路径

HTTP	Header

	Accept:	application/vnd.apache.kylin-v4-public+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

		curl	-X	DELETE	\

				'http://host:port/kylin/api/kafka/parser?project=TestProject&className=org.apache.kylin.parser.JsonData

Parser1'	\

				-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

				-H	'Accept-Language:	cn'	\

				-H	'Content-Type:	application/json;charset=utf-8'	\

				-H	'Authorization:	Basic	QURNSU46S1lMSU4='

响应字段

	data	,	成功删除的解析器全路径

响应示例

		{

						"code":	"000",

						"data":	"org.apache.kylin.parser.JsonDataParser1",

						"msg":	""

		}

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

1010

通过	API	实现指标自动发布

通过	API	实现指标自动发布

基于	Kyligence	Enterprise	的	AI	智能数据建模、查询加速等能力构建指标中台，可实现全生命周期的指标自动化构建和
管理，提升数据开发效率和数据治理能力，加速落地企业数字化经营战略。

本文介绍	Kyligengce	Enterprise	与指标中台的关系以及如何使用	API	自动发布指标。

背景信息

过去基于报表来响应业务需求的模式存在体系混乱、数据不一致、重复开发等问题。在数字化转型和数据驱动决策需求

下，如何构建统一数据视图，深度挖掘数据价值，支撑各级业务团队高效管理，已成为企业面临的一个现实挑战。

通过	Kyligence	Enterprise	构建企业级指标平台，可实现数据资产规范化、集市模型统一化、指标开发流程标准化，为报
表、移动端、可视化仪表盘、数据挖掘等应用提供开放的数据服务。

基于	Kyligence	Enterprise	指标平台

API	接口流程设计

本案例中，通过	Kyligence	Enterprise	提供的	API	接口实现指标自动化发布，流程设计如下：

API	接口流程设计

1011

通过	API	实现指标自动发布

步骤

说明

步骤一：加载数据
仓库中的表

将数据仓库中表的元数据（包含表名、注释、列名、列类型等信息）加载到	Kyligence
Enterprise	中，为增量加载表数据做准备。

步骤二：通过	SQL
自动建模

通过	AI	智能建模对指标系统映射的	SQL	查询语句进行解析，得出表的关联关系、维度组
合和度量信息，然后自动创建模型和索引。

步骤三：指定模型
分区列

步骤四：加载增量
数据

为模型指定分区列，实现增量加载数据并构建索引，缩短数据准备时间。

根据设定的时间范围加载增量数据，同时可通过	API	对该任务进行监控。

步骤五：查询指标

增量数据数据加载完成后，即可对指标系统映射的	SQL	查询语句进行加速。

[!NOTE]

在生产环境中，您还可以根据业务需求设计额外的判断逻辑（例如调用预重载	Hive	表对比元数据差异），组合
使用各	API	接口可实现高级的定制功能，完成复杂任务的自动化。更多	API	接口介绍，见	API	手册。

环境说明

项目名称：kylin_metrics_store，且已开启智能推荐功能。
数据集：SSB	样例数据集。

本文以发布一个名为	1993	年	1	月	1	日莫桑比克销售额的指标为例，展示通过	curl	命令调用	API	的过程与具体示例。

[!NOTE]

为提供最佳的阅读体验，本文对	API	返回示例中的部分内容进行了省略。

步骤一：加载数据仓库中的表

API	接口：加载	Hive	表

请求示例

将下述	Hive	表的元数据加载至	Kyligence	Enterprise	的	kylin_metrics_store	项目中：

SSB.LINEORDER

SSB.CUSTOMER

curl	-X	POST	\

		'http://10.0.0.2:7070/kylin/api/tables'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	en'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{"project":"kylin_metrics_store","tables":["SSB.LINEORDER",	"SSB.CUSTOMER"],"need_sampling":false}'

返回示例

根据返回数据得知	SSB.LINEORDER	和	SSB.CUSTOMER	表均已加载成功。

{

				"code":	"000",

				"data":	{

								"loaded":	[

												"SSB.LINEORDER",

												"SSB.CUSTOMER"

								],

								"failed":	[]

1012

通过	API	实现指标自动发布

				},

				"msg":	""

}

步骤二：通过	SQL	自动建模

API	接口：	SQL	加速

请求示例

传入指标映射的	SQL	查询语句（具体如下），Kyligence	Enterprise	将对其进行智能分析，然后根据分析结果自动创建模
型。

SELECT	'MOZAMBIQUE'	AS	nation,

SUM(lo_ordtotalprice)	AS	total_price

FROM

		ssb.lineorder	t_o

		INNER	JOIN	ssb.customer	t_c	ON	t_o.lo_custkey	=	t_c.c_custkey

		AND	C_NATION	=	'MOZAMBIQUE'

		AND	LO_ORDERDATE	=	'1993-01-01'

[!NOTE]

通过	-d	传入常量时，要求的格式为 	'\''常量'\''		，例如	 	'\''MOZAMBIQUE'\''	。

curl	-X	POST	\

		'http://10.0.0.2:7070/kylin/api/models/sql_acceleration'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	en'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{"project":"kylin_metrics_store",	"sqls":["SELECT	'\''MOZAMBIQUE'\''	AS	nation,	SUM(lo_ordtotalprice)	AS

total_price	FROM	ssb.lineorder	t_o	INNER	JOIN	ssb.customer	t_c	ON	t_o.lo_custkey	=	t_c.c_custkey	AND	C_NATION	=

	'\''MOZAMBIQUE'\''	AND	LO_ORDERDATE	=	'\''1993-01-01'\''"]}'

返回示例

接口调用成功后，Kyligence	Enterprise	将自动完成模型的创建。返回数据中	created_models	参数的值包含了该模型的名
称、维度和度量等信息。

本案例中，模型名称为	AUTO_MODEL_LINEORDER_1。

{

				"code":	"000",

				"data":	{

								......

																"alias":	"AUTO_MODEL_LINEORDER_1",

																"version":	"4.0.0.0",

																"rec_items":	[

																				{

																								......

																								"dimensions":	[

																								......

																								"measures":	[

																								......

				"msg":	""

}

步骤三：指定模型分区列

API	接口：设置分区列

1013

通过	API	实现指标自动发布

请求示例

为模型指定分区列为	LINEORDER.LO_ORDERDATE，格式为	yyyy-MM-dd。

curl	-X	PUT	\

	'http://10.0.0.2:7070/kylin/api/models/kylin_metrics_store/AUTO_MODEL_LINEORDER_1/partition_desc'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	en'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{

				"partition_desc":{

								"partition_date_column":"LINEORDER.LO_ORDERDATE",

								"partition_date_format":"yyyy-MM-dd"},

				"start":"725817600000",

				"end":"725904000000"

				}'

返回示例

返回数据中的	code	参数的值为	000，即代表设置分区列成功。

[!NOTE]

分区列设置成功后，Kyligence	Enterprise	将自动完成索引构建。

{

				"code":	"000",

				"data":	"",

				"msg":	""

}

步骤四：增量加载数据

API	接口：加载数据

请求示例

为模型增量加载数据（即增量构建	Segment），起始时间为	725904000000（即1993-01-02	00:00:00），结束时间为
725990400000（即1993-01-03	00:00:00）。

[!NOTE]

时间格式为	Unix	时间戳，单位为毫秒。

curl	-X	POST	\

		'http://10.0.0.2:7070/kylin/api/models/AUTO_MODEL_LINEORDER_1/segments'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{"project":"kylin_metrics_store",	"start":	"725904000000",	"end":	"725990400000","build_all_indexes":true

,"build_all_sub_partitions":false}'

返回示例

本接口调用成功并不代表增量加载数据的任务已完成，任务的完成时间通常受数据量、负载等因素影响，您可以通过下

述方法监控任务的执行进度。

1.	 记录返回参数	job_id	的值。

2.	 调用返回任务列表接口，当返回参数	job_status	的值为	FINISHED	时，代表该任务已完成。

1014

通过	API	实现指标自动发布

[!NOTE]

当该任务执行完成后，Kyligence	Enterprise	即可为相关的	SQL	查询语句提供加速服务。

{

				"code":	"000",

				"data":	{

								"jobs":	[

												{

																"job_name":	"INC_BUILD",

																"job_id":	"c0ec16b0-a04e-5bc4-2227-384b0ca1b231"

												}

								]

				},

				"msg":	""

}

步骤五：查询指标数据

API	接口：查询模型数据

请求示例

传入下述	SQL	查询语句，查询	1993	年	1	月	1日莫桑比克（MOZAMBIQUE）的销售额。

SELECT	'MOZAMBIQUE'	AS	nation,

		SUM(lo_ordtotalprice)	AS	total_price

FROM

		ssb.lineorder	t_o

		INNER	JOIN	ssb.customer	t_c	ON	t_o.lo_custkey	=	t_c.c_custkey

		AND	C_NATION	=	'MOZAMBIQUE'

		AND	LO_ORDERDATE	=	'1993-01-01'

curl	-X	POST	\

		'http://10.0.0.2:7070/kylin/api/query'	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{	"sql":"SELECT	'\''MOZAMBIQUE'\''	AS	nation,	sum(lo_ordtotalprice)	AS	total_price	FROM	ssb.lineorder	t_o

	INNER	JOIN	ssb.customer	t_c	ON	t_o.lo_custkey	=	t_c.c_custkey	AND	C_NATION	=	'\''MOZAMBIQUE'\''	AND	LO_ORDERDA

TE	=	'\''1993-01-01'\''",	"project":"kylin_metrics_store",	"partialMatchIndex":"true"}'

返回示例

返回数据中，主要关注下述返回参数的值：

results：包含本次查询的结果数据。
indexType：返回本参数即表示本次查询命中了模型中的索引，即通过索引加速了查询响应，本案例中该参数的返
回值为	Agg	Index（聚合索引）。

{

				"code":	"000",

				"data":	{

								......

								"results":	[

												[

																"MOZAMBIQUE",

																"937557348"

								......

																"indexType":	"Agg	Index",

								......

1015

通过	API	实现指标自动发布

				"msg":	""

}

调试与修改

如果在调用	API	接口时遇到返回错误，您需要根据返回的提示（即	msg	参数的返回值）检查传入的请求参数及其取值
是否正确。

例如	msg	参数的返回值为： 	KE-010001001(Project	Not	Exist):Can't	find	project	\"demo_project\".	Please	check	and
try	again.

根据提示得知	Kyligence	Enterprise	无法找到名称为	demo_project	的项目，您需要检查	API	请求中的项目名是否设置正
确，然后重新发起调用。

扩展阅读

API	手册
快速入门

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

1016

使用回调	API	查看构建任务状态

使用回调	API	查看任务状态

调用所需任务API，返回成功信息之后，表示任务成功启动了。此时，这个任务并没有执行成功，最终可能成功也可能
失败。回调	API	的功能是将该任务的最终状态返回：如果任务成功，则返回成功信息；如果任务失败，则返回失败信
息，并且给出失败的原因。根据回调	API	的返回信息，用户可以进行相应的调整。

使用方法

部署一个接收	POST	请求的在线服务，在	kylin.properties	里新增配置参数	 	kylin.job.finished-notifier-url	，	然后将在
线服务的	URL	地址作为该参数的值。

POST	消息示例

假设	 	kylin.job.finished-notifier-url		参数的值设置为	 	http://127.0.0.1:7777	，当	Kyligence	Enterprise	的任务执行完
毕之后，会向该地址发送如下信息：

Header

Content-Type:	application/json

Content-Length:	262

Host:	127.0.0.1:7777

Connection:	Keep-Alive

User-Agent:	Apache-HttpClient/4.5.3	(Java/1.8.0_171)

Accept-Encoding:	gzip,deflate

Body

{

"job_id":	"6044ac09-27bc-4968-a6b0-881c4c0abf89",

"project":	"test",

"model_id":	"91402da4-b991-4cd8-b164-7f62b9e91b69",

"segment_ids":	[

		"9e5a89b9-00f1-4296-adc4-139113030e83",

		"f26dcbc9-b786-4112-a4f6-94280bf10265",

		"f3dc9864-0e1a-417b-a46d-3255e8cb6473"

],

"index_ids":	[

		20001,

		10001

],

"duration":	27699,

"job_state":	"ERROR",

"job_type":	"INDEX_BUILD",

"segment_time_range":	[

		{

				"segment_id":	"9e5a89b9-00f1-4296-adc4-139113030e83",

				"data_range_start":	1338480000000,

				"data_range_end":	1354291200000

		},

		{

				"segment_id":	"f26dcbc9-b786-4112-a4f6-94280bf10265",

				"data_range_start":	1325347200000,

				"data_range_end":	1338480000000

		},

		{

				"segment_id":	"f3dc9864-0e1a-417b-a46d-3255e8cb6473",

				"data_range_start":	1354291200000,

				"data_range_end":	1370016000000

		}

],

1017

使用回调	API	查看构建任务状态

"segment_partition_info":	[{

						"segment_id":	"9e5a89b9-00f1-4296-adc4-139113030e83",

						"partition_info":	[{

										"id":	0,

										"values":	["674"],

										"status":	"ONLINE",

										"last_modified_time":	1623390508821,

										"source_count":	34,

										"bytes_size":	1772

						},	{

										"id":	1,

										"values":	["22"],

										"status":	"ONLINE",

										"last_modified_time":	1623390508821,

										"source_count":	30,

										"bytes_size":	1800

						}]

		}],

		"snapshot_job_info":null,

		"err_code":"KE-060100201",
		"msg":"KE-060100201:	Kyligence	Enterprise	外部发生异常",
		"suggestion":"请检查其他系统、组件等外部环境是否正确",

		"start_time":1656604800000,

		"end_time":1656608400000,

		"tag":null,

		"code":"999",
		"stacktrace":"KE-060100201:	Kyligence	Enterprise	外部发生异常。	org.apache...."

}

回调	API	上传的参数

HTTP	方法：POST
Content-Type：application/json

URL	Parameters

	project		-	 	string	，项目名称
	job_id	-	String	，Job	的	ID
	model_id		-	 	string	，模型	UUID
	segment_ids		-	 	list<string>	，Segment	UUID
	index_ids		-	 	list<string>	，index	UUID
	duration		-	 	long	，构建用时，单位为毫秒
	job_state		-	 	string	，结束时任务的状态，取值范围为：	 	SUCCEED		任务成功、 	DISCARDED		任务终止、 	ERROR
任务失败、 	PAUSED		任务暂停
	job_type		-	 	string	，任务类型，包
括： 	INDEX_BUILD	、 	INDEX_REFRESH	、 	INDEX_MERGE	、 	INC_BUILD	、 	SUB_PARTITION_BUILD	、 	SUB_PARTITION_REF

RESH	、 	SNAPSHOT_BUILD	、 	SNAPSHOT_REFRESH

	segment_time_range		-	 	list	，segment时间范围
	segment_id		-	 	string	，Segment	UUID
	data_range_start		-	 	long	，时间戳，精确到毫秒，构建数据段的开始时间
	date_range_end		-	 	long	，时间戳，精确到毫秒，构建数据段的结束时间

	segment_partition_info		-	 	list	，包含以下信息：

	segment_id	： 	string	，Segment	UUID
	partition_info	： 	list	，Segment	下子分区的信息，	包含以下信息：

id： 	long	，子分区的	ID
values： 	list<long>	，子分区的	value	值
status： 	string	，分区状态，取值范围： 	ONLINE	:	在线、 	LOADING	：构建中、 	REFRESHING	：刷新中
last_modified_time： 	long	，时间戳，精确到毫秒，最后更新时间
source_count： 	long	，行数
bytes_size： 	long	，存储大小

1018

使用回调	API	查看构建任务状态

	snapshot_job_info		-	 	object	，快照相关任务信息，包括：

	table	： 	string	，快照的数据表名

	database	： 	string	，快照的数据库名

	total_rows	： 	long	，快照的记录数

	storage	：	 	long	，快照的磁盘空间
	last_modified_time	：时间戳，快照的最后构建时间

	status	：快照的状态，"ONLINE"表示上线中，"OFFLINE"表示下线中
	select_partition_col	：快照的分区字段，仅在增量快照下生效，在全量快照下该字段值为 	null

	msg		-	 	string		，任务的报错信息
	error_code		-	 	string		，Kyligence	Enterprise	错误码
	suggestion		-	 	string		，出错之后的可能的解决建议
	start_time		-	 	long		，任务开始的时间戳
	end_time		-	 	long	，任务结束的时间戳
	tag		-	 	string	，用户自定义的任务标记，用于系统集成
	code	-	 	string	，状态码， 	null		成功、 	401		未授权、 	999		其他未定义的异常
	stacktrace	-	 	string	，报错的堆栈信息

已知限制

对于暂停（PAUSED）和失败（ERROR）状态的任务，如果直接被取消（指状态转换为	DISCARDED），任务状态
的更新不会通过这个回调	API	上报信息。

如果任务处于上述两种状态下进行重跑，重跑中的任务被取消（不经过暂停或者失败状态），任务状态的更新会通

过这个回调	API	上报信息。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

1019

错误码

错误码

如果您在调用	Kyligence	Enterprise	API	或使用内置工具遇到了报错，您可以根据错误码及其提示信息排除问题，然后重
新发起调用。本文汇总了	API	和内置工具的错误码。

API	错误码

项目

错误码

KE-010001201

KE-010001208

模型

错误信息

找不到项目，请检查项目是否存在之后重试。

项目未开启多级分区，请开启后重试。

错误码

错误信息

KE-010002201

KE-010002202

KE-010002203

KE-010002204

KE-010002205

KE-010002206

认证

无法找到模型，请检查后再试。

无法找到模型	Id，请检查后重试。

无法找到模型	Name，请检查后重试。

模型名称不可为空。

无效的模型名称，请使用字母、数字或下划线命名。

模型已存在，请重新命名。

错误码

错误信息

KE-010003207

认证用户信息失败，请重新登录。

KE-010003208

用户名或密码错误，请检查后重试。

KE-010003209

找不到权限信息。

KE-040005201

找不到	PASSWORD	ENCODER。请检查配置项	kylin.security.user-password-encoder。

KE-040005202

PASSWORD	ENCODER	初始化失败。请检查配置项	kylin.security.user-password-encoder。

索引

错误码

错误信息

KE-010012201

索引元数据不一致。请尝试刷新下列模型的所有	Segment。

KE-010012202

因为存在相同的索引，无法新建该索引。请修改。

KE-010012203

该参数不在支持范围内。

Segment

1020

错误码

错误码

错误信息

KE-010022201

无法刷新，超出了加载数据的范围。请修改后重试。

KE-010022202

	无法构建，待构建的范围和已构建的范围存在重合。请修改后重试。

KE-010022203

无法刷新，请选择	Segment	后再试。

KE-010022204

无法刷新，部分	Segment	正在构建。请稍后再试。

KE-010022205

无法刷新，所选	Segment	范围为空。请重新选择后再试。

KE-010022206

请至多选择一个	Segment	刷新。

KE-010022207

请至少选择两个	Segment	合并。

KE-010022208

无法合并所选	Segment，因为时间范围不连续。请检查后重试。

KE-010022209

找不到	Segment	名称。请检查后重试。

KE-010022210

找不到	Segment	ID。请检查后重试。

KE-010022211

找不到	Segment。请检查后重试。

KE-010022212

至少选择一个	Segment。

KE-010022213

无法删除，请选择	Segment	后再试。

KE-010022214

不能同时输入	Segment	ID	和名称。请重新输入。

KE-010022215

请输入	Segment	ID	或名称。

KE-010022216

Segment	被锁定，无法删除、刷新或合并。请稍后重试。

KE-010022217

当前	Segment	状态，无法刷新或合并。请稍后重试。

KE-010022218

当前	Segments	所包含的索引不一致。请先构建索引并确保其一致后再合并。

KE-010022219

当前	Segments	所包含的分区不一致。请先构建分区并确保其一致后再合并。

任务

错误码

错误信息

KE-010032201

无法添加任务，子分区值为空。请检查后重试。

KE-010032202

无法添加任务，Segment	索引为空。请稍后重试。

KE-010032203

无法添加任务，当前没有	READY	状态的	Segment。请稍后重试。

KE-010032204

当前没有可执行的任务。请稍后重试。

KE-010032205

无法添加任务。请确保该操作对当前对象有效。

KE-010032206

当前无法提交任务，因为已有相同对象的构建任务正在进行。请稍后再试。

KE-010032207

无法添加任务，Segment	索引不一致。请检查后重试。

KE-010032208

无法添加任务，该节点不是构建节点。请检查后重试。

KE-010032209

无法添加任务，存在重复的子分区值。请检查后再试。

KE-010032210

当前没有可刷新索引。请检查后重试。

KE-010032211

无法操作该状态下的任务。

KE-010032212

选择的任务状态无效，状态必须是	“PENDING“,	“RUNNING“,	“FINISHED“,
	“ERROR”	或	“DISCARDED“。请检查后重试。

KE-010032213

至少选择一个任务。

1021

错误码

KE-010032213

至少选择一个任务。

KE-010032214

采样行数超过支持的范围。请修改。

KE-010032215

因为任务状态更新时遇到错误，无法执行当前操作。请刷新任务列表后重试。

KE-010032216

超过单次提交的构建任务数，无法提交当前构建任务。请尝试分批提交。

KE-010032217

无效的参数值	“action”	或	“statuses”	或	“job_ids”。“statuses”值或
“job_ids”在当前任务状态下无法执行。

KE-010032218

已无可用的存储配额。系统提交构建任务失败，查询引擎依然正常服务。
请及时清理低效存储，提高低效存储阈值，或者通知管理员提高本项目的存储配额。

KE-010032219

找不到任务。请检查后重试。

参数校验

错误码

错误信息

KE-010043201

请求参数为空或值为空。请检查请求参数是否正确填写。

KE-010043202

输入的参数值无效，开始时间和结束时间转化的时间戳需大于等于0。请检查后重试。

KE-010043203

输入的参数值无效，结束时间需大于开始时间。请检查后重试。

KE-010043204

输入的参数值无效，结束时间需大于等于开始时间。请检查后重试。

KE-010043205

输入的参数格式无效，时间戳格式需为毫秒级。请检查后重试。

KE-010043206

输入的参数值无效，开始时间和结束时间需同时存在或同时为空。请检查后重试。

KE-010043207

输入的参数无效，当前仅支持特定的值。请检查后重试。

KE-010043208

输入的参数值无效，参数值需为非负整数。请检查后重试。

KE-010043209

输入的参数值无效，当前仅支持特定的类型。请检查后重试。

KE-010043210

参数不能为空。请输入时间分区列格式。

KE-010043211

时间分区列的格式无效。请输入支持的格式，参考用户手册。

KE-010043212

参数不能为空。请输入	layout(s)	的	id。

KE-010043213

找不到	Layout。请检查后重试。

KE-010043214

无法刷新，时间单位仅支持	d（天）、h（小时）或	m（分钟）。请检查后重试。

KE-010043215

无法修改配置。请联系系统管理员。

KE-010043216

无法删除配置。请联系系统管理员。

KE-010043218

无效请求参数值。请输入正确的	sort_by	字段。

KE-010043219

用户名和公司只支持中英文、数字、空格。请检查后重试。

KE-010043220

操作失败，用户组不存在。请先添加。

KE-010043221

参数不能重复。请检查后重试。

系统

错误码

KE-040021201

KE-040023201

错误信息

系统正在尝试恢复服务。请稍后重试。

该请求无法在任务节点执行。请检查后重试。

1022

错误码

KE-040023202

KE-040023203

KE-040025201

资源组

任务节点不支持查询。请选择查询节点。

该请求无法在查询节点执行。请检查后重试。

系统配置数据异常。

错误码

错误信息

KE-040027201

如需关闭资源组模式，请先移除资源组关联的实例和项目。

KE-040027202

当资源组模式开启后，请确保至少存在一个资源组。

KE-040027203

资源组	ID	不能为空。请检查后重试。

KE-040027204

资源组	ID	已存在。请检查后重试。

KE-040027205

无法完成该请求。请确保资源组请求需要的所有参数都已填写完整。

KE-040027206

无法在实例中找到值的	“resource_group_id”。请检查后重试。

KE-040027207

存在重复的实例。请检查后重试。

KE-040027208

参数不可为空。请检查后重试。

KE-040027209

无法绑定项目的资源请求。请确保一个项目最多绑定两个资源组，且构建和查询请求各绑定
一个资源组。

KE-040027210

在	“mapping_info”	中参数	“resource_group_id”	的值，与	“resource_groups”	中的值不匹配。

其它

错误码

错误信息

KE-010007204

源表列的数据类型发生变更。请从模型中删除该列，或修改该列的数据类型。

KE-010007208

当前暂不可重载表。存在运行中的任务。请等任务完成后再重载，或手动终止任务。

KE-010025201

无法找到相关	Cube。

KE-010031201

因为查询结果行数超过最大值，无法完成查询。请添加过滤条件或联系管理员
调整最大查询结果行数。

KE-030001201

无法构建，索引的预期行数与实际构建行数不匹配。

KE-060100201

Kyligence	Enterprise	外部发生异常。

内置工具错误码

[!NOTE]	内置工具包含垃圾清理工具、诊断包生成工具等。

错误码

KE-050040201

KE-050040202

KE-050040203

KE-050040204

KE-050041201

KE-050041202

错误信息

参数为空。

参数未指定。

参数未指定（毫秒）。

参数	“-endTime”	<=	参数	“-startTime”	。

该路径不存在。

该路径已存在。

1023

错误码

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

1024

REST	API	v2

REST	API	v2

Kyligence	Enterprise	REST	API	v2	主要用于	Kyligence	Enterprise	3。目前在	Kyligence	Enterprise	4	中，对于部分	API	进行
了兼容处理，需要注意的是由于版本差异较大，目前返回结果无法做到完全一致。我们强烈建议您使用	v4	API	进行日
常调度和系统对接。

Kyligence	Enterprise	REST	API	v2	在未来新的大版本中将不再支持。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

1025

访问与安全认证	API

访问与安全认证	API

提示：

1.	 Kyligence	Enterprise	REST	API	v2	主要用于	Kyligence	Enterprise	3。目前在	Kyligence	Enterprise	4	中，对于部
分	API	进行了兼容处理，需要注意的是由于版本差异较大，目前返回结果无法做到完全一致。我们强烈建议
您使用	v4	API	进行日常调度和系统对接。

2.	 Kyligence	Enterprise	REST	API	v2	在未来新的大版本中将不再支持。

访问

Kyligence	Enterprise	API	的访问前缀为	 	/kylin/api	，不管对哪个模块的	API	访问都需要加上该前缀，比如访问所有项
目的	API	为	 	/kylin/api/projects	，对应的完整路径为	 	http://host:port/kylin/api/projects	。

认证

Kyligence	Enterprise	所有的	API	都是基于	Basic	Authentication	认证机制。Basic	Authentication	是一种简单的访问控制机
制，将帐号密码基于	Base64	编码后作为请求头添加到	HTTP	请求头中，后端会读取请求头中的帐号密码信息进行认
证。以账号密码	 	ADMIN:KYLIN		为例，对应帐号密码编码后结果为	 	'Basic	QURNSU46S1lMSU4='	，那么	HTTP	对应的头信
息为	 	'Authorization:	Basic	QURNSU46S1lMSU4='	。

认证要点

在	HTTP	头添加	 	Authorization		信息

或者可以通过	 	POST	http://host:port/kylin/api/user/authentication		进行认证，一旦认证通过，接下来对	API
请求基于	cookies	在	HTTP	头中免去	 	Authorization	信息

HTTP	Header

	Authorization:Basic	QURNSU46S1lMSU4=

	Accept:	application/vnd.apache.kylin-v2+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	POST	\

		'http://host:port/kylin/api/user/authentication'	\

		-H	'Accept:	application/vnd.apache.kylin-v2+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":	"000",

				"data":	{

								"username":	"ADMIN",

								"authorities":	[

												{

																"authority":	"ROLE_ADMIN"

												},

												{

																"authority":	"ALL_USERS"

1026

访问与安全认证	API

												}

								],

								"disabled":	false,

								"defaultPassword":	false,

								"locked":	false,

								"uuid":	"aaf02c5d-1605-42fa-abf9-9b0bb5715a6a",

								"last_modified":	1589535275393,

								"create_time":	1586744927779,

								"version":	"4.0.0.0",

								"mvcc":	55,

								"locked_time":	0,

								"wrong_time":	1,

								"first_login_failed_time":	1589535275369

				},

				"msg":	""

}

JavaScript	认证请求示例

提示：您可以通过如下路径下载	"jquery.base64.js"	https://github.com/yckart/jquery.base64.js

var	authorizationCode	=	$.base64('encode',	'NT_USERNAME'	+	":"	+	'NT_PASSWORD');

$.ajaxSetup({

			headers:	{

				'Authorization':	"Basic	"	+	authorizationCode,

				'Content-Type':	'application/json;charset=utf-8',

				'Accept':	'application/vnd.apache.kylin-v2+json'

			}

});

$.ajaxSetup({

						headers:	{

								'Authorization':	'Basic	eWFu**********X***ZA==',

								'Content-Type':	'application/json;charset=utf-8',

								'Accept':	'application/vnd.apache.kylin-v2+json'

						}	//	use	your	own	authorization	code	here

				});

				var	request	=	$.ajax({

							url:	"http://host:port/kylin/api/query",

							type:	"POST",

							data:	'{"sql":"select	count(*)	from	SUMMARY;","offset":0,"limit":50000,"acceptPartial":true,"project":"t

est"}',

							dataType:	"json"

				});

				request.done(function(	msg	)	{

							alert(msg);

				});

				request.fail(function(	jqXHR,	textStatus	)	{

							alert(	"Request	failed:	"	+	textStatus	);

		});

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

1027

模型	API

模型	API

提示：

1.	 Kyligence	Enterprise	REST	API	v2	主要用于	Kyligence	Enterprise	3。目前在	Kyligence	Enterprise	4	中，对于部
分	API	进行了兼容处理，需要注意的是由于版本差异较大，目前返回结果无法做到完全一致。我们强烈建议
您使用	v4	API	进行日常调度和系统对接。

2.	 Kyligence	Enterprise	REST	API	v2	在未来新的大版本中将不再支持。

3.	 请确保已阅读前面的访问及安全认证章节，了解如何在	REST	API	语句中添加认证信息。

4.	 在	Curl	命令行上，如果您访问的	URL	中含有	 	&		符号，请注意转义，比如在	URL	两端加上引号。

Kyligence	Enterprise	提供了可以用来查看模型信息、进行索引构建和管理模型的	REST	API。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

1028

模型	API

查看模型信息	API

提示：

1.	 Kyligence	Enterprise	REST	API	v2	主要用于	Kyligence	Enterprise	3。目前在	Kyligence	Enterprise	4	中，对于部
分	API	进行了兼容处理，需要注意的是由于版本差异较大，目前返回结果无法做到完全一致。我们强烈建议
您使用	v4	API	进行日常调度和系统对接。

2.	 Kyligence	Enterprise	REST	API	v2	在未来新的大版本中将不再支持。

3.	 请确保已阅读前面的访问及安全认证章节，了解如何在	REST	API	语句中添加认证信息。

4.	 在	Curl	命令行上，如果您访问的	URL	中含有	 	&		符号，请注意转义，比如在	URL	两端加上引号。

获取模型列表

	GET	http://host:port/kylin/api/models

URL	Parameters

	pageOffset		-	 	可选		 	int	，返回数据起始下标，默认为	0
	pageSize		-	 	可选		 	int	，每页返回多少，默认为	10
	modelName		-	 	可选		 	string	，模型名称
	exactMatch		-	 	可选		 	boolean	，是否对模型名称进行完全匹配，默认为	 	true
	projectName		-	 	必选		 	string	，	项目名称

HTTP	Header

	Accept:	application/vnd.apache.kylin-v2+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://host:port/kylin/api/models?projectName=doc_project&modelName=doc_model_01&exactMatch=true'	\

		-H	'Accept:	application/vnd.apache.kylin-v2+json'	\

		-H	'Accept-Language:	en'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

	{

				"code":	"000",

				"data":	{

								"models":	[

												{

																"name":	"model",

																"lookups":	[

																				{

																								"table":	"SSB.DATES",

																								"kind":	"LOOKUP",

																								"alias":	"DATES",

																								"join":	{

																												"type":	"LEFT",

																												"primary_key":	[

																																"DATES.D_DATEKEY"

																												],

																												"foreign_key":	[

1029

模型	API

																																"P_LINEORDER.LO_ORDERDATE"

																												],

																												"non_equi_join_condition":	null,

																												"primary_table":	null,

																												"foreign_table":	null

																								}

																				}

																				...

																],

																"is_streaming":	false,

																"size_kb":	0,

																"input_records_count":	0,

																"input_records_size":	0,

																"project":	null,

																"uuid":	"d3f9d18e-2d7e-433e-95f1-4bff240747d8",

																"last_modified":	1589970126606,

																"create_time":	1587351922180,

																"version":	"4.0.0.0",

																"mvcc":	5,

																"alias":	"model",

																"owner":	"ADMIN",

																"config_last_modifier":	"ADMIN",

																"config_last_modified":	1589968416576,

																"description":	"",

																"fact_table":	"SSB.P_LINEORDER",

																"fact_table_alias":	null,

																"management_type":	"MODEL_BASED",

																"join_tables":	[

																				{

																								"table":	"SSB.DATES",

																								"kind":	"LOOKUP",

																								"alias":	"DATES",

																								"join":	{

																												"type":	"LEFT",

																												"primary_key":	[

																																"DATES.D_DATEKEY"

																												],

																												"foreign_key":	[

																																"P_LINEORDER.LO_ORDERDATE"

																												],

																												"non_equi_join_condition":	null,

																												"primary_table":	null,

																												"foreign_table":	null

																								}

																				}

																				...

																],

																"filter_condition":	"",

																"partition_desc":	{

																				"partition_date_column":	"P_LINEORDER.LO_ORDERDATE",

																				"partition_date_start":	0,

																				"partition_date_format":	"yyyyMMdd",

																				"partition_type":	"APPEND",

																				"partition_condition_builder":	"org.apache.kylin.metadata.model.PartitionDesc$DefaultPa

rtitionConditionBuilder"

																},

																"capacity":	"MEDIUM",

																"segment_config":	{

																				"auto_merge_enabled":	true,

																				"auto_merge_time_ranges":	[

																								"WEEK"

																				],

																				"volatile_range":	null,

																				"retention_range":	null

																},

																"data_check_desc":	null,

																"semantic_version":	1,

																"storage_type":	0,

																"all_named_columns":	[

1030

模型	API

																				{

																								"id":	0,

																								"name":	"LO_SHIPMODE",

																								"column":	"P_LINEORDER.LO_SHIPMODE"

																				}

																				...

																],

																"all_measures":	[

																				{

																								"name":	"SUM_REVENUE",

																								"function":	{

																												"expression":	"SUM",

																												"parameters":	[

																																{

																																				"type":	"column",

																																				"value":	"P_LINEORDER.LO_REVENUE"

																																}

																												],

																												"returntype":	"bigint"

																								},

																								"id":	100000

																				}

																				...

																],

																"column_correlations":	[],

																"multilevel_partition_cols":	[],

																"computed_columns":	[],

																"canvas":	{

																				"coordinate":	{

																								"P_LINEORDER":	{

																												"x":	704.3333265516494,

																												"y":	80.94445122612848,

																												"width":	255.55555555555557,

																												"height":	278.8888888888888

																								}

																								...

																				},

																				"zoom":	9.0

																},

																"status":	"WARNING",

																"last_build_end":	"770572800000",

																"storage":	0,

																"source":	0,

																"expansion_rate":	"0",

																"usage":	15,

																"model_broken":	false,

																"root_fact_table_deleted":	false,

																"segments":	null,

																"recommendations_count":	0,

																"available_indexes_count":	0,

																"empty_indexes_count":	5,

																"segment_holes":	[

																				{

																								"@class":	"org.apache.kylin.metadata.model.SegmentRange$TimePartitionedSegmentRange

",

																								"date_range_start":	694368000000,

																								"date_range_end":	738864000000

																				}

																],

																"total_indexes":	5,

																"simplified_measures":	[

																				{

																								"id":	100000,

																								"expression":	"SUM",

																								"name":	"SUM_REVENUE",

																								"return_type":	"bigint",

																								"parameter_value":	[

																												{

																																"type":	"column",

1031

模型	API

																																"value":	"P_LINEORDER.LO_REVENUE"

																												}

																								],

																								"converted_columns":	[]

																				}

																				...

																],

																"simplified_dimensions":	[

																				{

																								"id":	4,

																								"name":	"P_LINEORDER_LO_SUPPKEY",

																								"column":	"P_LINEORDER.LO_SUPPKEY",

																								"status":	"DIMENSION"

																				}

																				...

																],

																"simplified_tables":	[

																				{

																								"table":	"SSB.P_LINEORDER",

																								"columns":	[

																												{

																																"name":	"LO_ORDERKEY",

																																"datatype":	"bigint",

																																"cardinality":	0,

																																"comment":	null,

																																"is_computed_column":	false

																												}

																												...

																								]

																				}

																				...

																]

												}

												...

								],

								"size":	5

				},

				"msg":	""

}

获取	Cube	列表

为了兼容	Kyligence	Enterprise	3，我们保留了原有的获取	Cube	列表	API。

	GET	http://host:port/kylin/api/cubes

URL	Parameters

	pageOffset		-	 	可选		 	int	，返回数据起始下标，默认为	0
	pageSize		-	 	可选		 	int	，分页返回对应每页返回多少，默认为10
	modelName		-	 	可选		 	string	，返回对应模型名称等于该关键字的模型
	projectName		-	 	必选		 	string	，项目名称

HTTP	Header

	Accept:	application/vnd.apache.kylin-v2+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://host:port/kylin/api/cubes?projectName=doc_project&modelName=doc_model_01'	\

		-H	'Accept:	application/vnd.apache.kylin-v2+json'	\

		-H	'Accept-Language:	en'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

1032

模型	API

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":	"000",

				"data":	{

								"size":	5,

								"cubes":	[

												{

																"uuid":	"d3f9d18e-2d7e-433e-95f1-4bff240747d8",

																"last_modified":	1589970126606,

																"create_time":	1587351922180,

																"version":	"4.0.0.0",

																"mvcc":	-1,

																"alias":	"model",

																"owner":	"ADMIN",

																"config_last_modifier":	"ADMIN",

																"config_last_modified":	1589968416576,

																"description":	"",

																"fact_table":	"SSB.P_LINEORDER",

																"fact_table_alias":	null,

																"management_type":	"MODEL_BASED",

																"lookups":	null,

																"filter_condition":	"",

																"partition_desc":	{

																				"partition_date_column":	"P_LINEORDER.LO_ORDERDATE",

																				"partition_date_start":	0,

																				"partition_date_format":	"yyyyMMdd",

																				"partition_type":	"APPEND",

																				"partition_condition_builder":	"org.apache.kylin.metadata.model.PartitionDesc$DefaultPa

rtitionConditionBuilder"

																},

																"capacity":	"MEDIUM",

																"segment_config":	{

																				"auto_merge_enabled":	true,

																				"auto_merge_time_ranges":	[

																								"WEEK"

																				],

																				"volatile_range":	null,

																				"retention_range":	null

																},

																"data_check_desc":	null,

																"semantic_version":	1,

																"storage_type":	0,

																"all_named_columns":	[

																				{

																								"id":	0,

																								"name":	"LO_SHIPMODE",

																								"column":	"P_LINEORDER.LO_SHIPMODE"

																				}

																				...

																],

																"all_measures":	[

																				{

																								"name":	"SUM_REVENUE",

																								"function":	{

																												"expression":	"SUM",

																												"parameters":	[

																																{

																																				"type":	"column",

																																				"value":	"P_LINEORDER.LO_REVENUE"

																																}

																												],

																												"returntype":	"bigint"

																								},

																								"id":	100000

1033

模型	API

																				}

																				...

																],

																"column_correlations":	[],

																"multilevel_partition_cols":	[],

																"computed_columns":	[],

																"canvas":	{

																				"coordinate":	{

																								"P_LINEORDER":	{

																												"x":	704.3333265516494,

																												"y":	80.94445122612848,

																												"width":	255.55555555555557,

																												"height":	278.8888888888888

																								}

																								...

																				},

																				"zoom":	9.0

																},

																"status":	"WARNING",

																"last_build_end":	"770572800000",

																"storage":	0,

																"source":	0,

																"expansion_rate":	"0",

																"usage":	15,

																"model_broken":	false,

																"root_fact_table_deleted":	false,

																"segments":	[

																				{

																								"size_kb":	0,

																								"input_records":	0,

																								"id":	"3534127e-2b58-4677-b58c-ff1038ffcf53",

																								"name":	"19920101000000_19920103000000",

																								"create_time_utc":	1589970126613,

																								"status":	"READY",

																								"segRange":	{

																												"@class":	"org.apache.kylin.metadata.model.SegmentRange$TimePartitionedSegmentR

ange",

																												"date_range_start":	694195200000,

																												"date_range_end":	694368000000

																								},

																								"timeRange":	null,

																								"parameters":	null,

																								"dictionaries":	null,

																								"snapshots":	null,

																								"last_build_time":	0,

																								"source_count":	-1,

																								"source_bytes_size":	-1,

																								"additionalInfo":	{

																												"segment_path":	"hdfs://sandbox.hortonworks.com:8020/kylin/leo_metadata_0413_1/

leoproject/parquet/d3f9d18e-2d7e-433e-95f1-4bff240747d8/3534127e-2b58-4677-b58c-ff1038ffcf53",

																												"file_count":	"0"

																								},

																								"is_encoding_data_skew":	false,

																								"is_snapshot_ready":	false,

																								"is_dict_ready":	false,

																								"is_flat_table_ready":	false,

																								"is_fact_view_ready":	false,

																								"bytes_size":	0,

																								"hit_count":	0,

																								"status_to_display":	"ONLINE"

																				}

																				...

																],

																"recommendations_count":	0,

																"available_indexes_count":	0,

																"empty_indexes_count":	5,

																"segment_holes":	[

																				{

																								"@class":	"org.apache.kylin.metadata.model.SegmentRange$TimePartitionedSegmentRange

1034

模型	API

",

																								"date_range_start":	694368000000,

																								"date_range_end":	738864000000

																				}

																],

																"total_indexes":	5,

																"simplified_dimensions":	[

																				{

																								"id":	4,

																								"name":	"P_LINEORDER_LO_SUPPKEY",

																								"column":	"P_LINEORDER.LO_SUPPKEY",

																								"status":	"DIMENSION"

																				}

																				...

																],

																"simplified_measures":	[

																				{

																								"id":	100000,

																								"expression":	"SUM",

																								"name":	"SUM_REVENUE",

																								"return_type":	"bigint",

																								"parameter_value":	[

																												{

																																"type":	"column",

																																"value":	"P_LINEORDER.LO_REVENUE"

																												}

																								],

																								"converted_columns":	[]

																				}

																				...

																],

																"name":	"model",

																"is_streaming":	false,

																"size_kb":	0,

																"input_records_count":	0,

																"input_records_size":	-5,

																"project":	"leoproject",

																"unauthorized_tables":	[],

																"unauthorized_columns":	[],

																"visible":	true

												}

												...

								]

				},

				"msg":	""

}

返回指定模型

	GET	http://host:port/kylin/api/cubes/{cubeName}

URL	Parameters

	cubeName		-	 	必选		 	string	，模型名称

HTTP	Header

	Accept:	application/vnd.apache.kylin-v2+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://host:port/kylin/api/cubes/MODEL_01'	\

		-H	'Accept:	application/vnd.apache.kylin-v2+json'	\

1035

模型	API

		-H	'Accept-Language:	en'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

		{

						"code":	"000",

						"data":	{

										"name":	"MODEL_01",

										"lookups":	null,

										"is_streaming":	false,

										"size_kb":	81,

										"input_records_count":	23853,

										"input_records_size":	5446614,

										"project":	"doc_expert",

										"uuid":	"36da04d4-12a8-4704-994b-0d7024fed6e7",

										"last_modified":	1570957496905,

										"create_time":	1570961435812,

										"version":	"4.0.0.0",

										"mvcc":	1,

										"alias":	"MODEL_01",

										"owner":	"ADMIN",

										"config_last_modifier":	null,

										"config_last_modified":	0,

										"description":	"",

										"fact_table":	"SSB.LINEORDER",

										"fact_table_alias":	null,

										"management_type":	"MODEL_BASED",

										"join_tables":	[...],

										"filter_condition":	"",

										"partition_desc":	{

														"partition_date_column":	"LINEORDER.LO_ORDERDATE",

														"partition_date_start":	0,

														"partition_date_format":	"yyyyMMdd",

														"partition_type":	"APPEND",

														"partition_condition_builder":	"org.apache.kylin.metadata.model.PartitionDesc$DefaultPartitio

nConditionBuilder"

										},

										"capacity":	"MEDIUM",

										"segment_config":	{

														"auto_merge_enabled":	null,

														"auto_merge_time_ranges":	null,

														"volatile_range":	null,

														"retention_range":	null

										},

										"data_check_desc":	null,

										"semantic_version":	0,

										"all_named_columns":	[...],

										"all_measures":	[...],

										"column_correlations":	[],

										"multilevel_partition_cols":	[],

										"computed_columns":	[...],

										"canvas":	{

														"coordinate":	{

																		"CUSTOMER":	{

																						"x":	923.2222154405381,

																						"y":	218.61111111111117,

																						"width":	387.77777777777777,

																						"height":	362.22222222222223

																		},

																		"LINEORDER":	{

																						"x":	495.44443766276055,

																						"y":	86.3888888888889,

																						"width":	378.88888888888886,

																						"height":	523.3333333333334

																		}

1036

模型	API

														},

														"zoom":	9

										},

										"status":	"ONLINE",

										"last_build_end":	"775699200000",

										"storage":	83410,

										"source":	5446614,

										"expansion_rate":	"1.53",

										"usage":	0,

										"model_broken":	false,

										"root_fact_table_deleted":	false,

										"segments":	[...],

										"simplified_dimensions":	[...],

										"simplified_tables":	[...],

										"simplified_measures":	[...]

						},

						"msg":	""

		}

获取模型中的空洞

提示：	生产系统上健康的模型不应存在空洞，意味着模型中的	Segment	应该在分区列上是连续的。

	GET	http://host:port/kylin/api/cubes/{cubeName}/holes

URL	Parameters

	cubeName		-	 	必选		 	string	，模型名称

HTTP	Header

	Accept:	application/vnd.apache.kylin-v2+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://host:port/kylin/api/cubes/doc_model_01/holes	'	\

		-H	'Accept:	application/vnd.apache.kylin-v2+json'	\

		-H	'Accept-Language:	en'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":	"000",

				"data":	[

								{

												"id":	null,

												"name":	"19920103000000_19930601000000",

												"create_time_utc":	0,

												"status":	null,

												"segRange":	{

																"@class":	"org.apache.kylin.metadata.model.SegmentRange$TimePartitionedSegmentRange",

																"date_range_start":	694368000000,

																"date_range_end":	738864000000

												},

												"timeRange":	{

																"start":	694368000000,

																"end":	738864000000

												},

												"parameters":	null,

												"dictionaries":	null,

1037

模型	API

												"snapshots":	null,

												"last_build_time":	0,

												"source_count":	-1,

												"source_bytes_size":	0,

												"additionalInfo":	{},

												"is_encoding_data_skew":	false,

												"is_snapshot_ready":	false,

												"is_dict_ready":	false,

												"is_flat_table_ready":	false,

												"is_fact_view_ready":	false,

												"bytes_size":	0,

												"hit_count":	0,

												"status_to_display":	null

								}

				],

				"msg":	""

}

返回模型描述信息

	GET	http://host:port/kylin/api/models/{projectName}/{modelName}

URL	Parameters

	projectName		-	 	必选		 	string	，项目名称
	modelName		-	 	必选		 	string	，模型名称

HTTP	Header

	Accept:	application/vnd.apache.kylin-v2+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

'http://host:port/kylin/api/models/doc_project/doc_model_01'	\

-H	'Accept:	application/vnd.apache.kylin-v2+json'	\

-H	'Accept-Language:	en'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'

响应示例

				{

								"code":"000",

								"data":{

												"model":{

																"name":	"model",

																"lookups":	[

																				{

																								"table":	"SSB.DATES",

																								"kind":	"LOOKUP",

																								"alias":	"DATES",

																								"join":	{

																												"type":	"LEFT",

																												"primary_key":	[

																																"DATES.D_DATEKEY"

																												],

																												"foreign_key":	[

																																"P_LINEORDER.LO_ORDERDATE"

																												],

																												"non_equi_join_condition":	null,

																												"primary_table":	null,

																												"foreign_table":	null

1038

模型	API

																								}

																				},

																				...

																],

																"is_streaming":	false,

																"size_kb":	0,

																"input_records_count":	0,

																"input_records_size":	0,

																"project":	null,

																"uuid":	"d3f9d18e-2d7e-433e-95f1-4bff240747d8",

																"last_modified":	1589970126606,

																"create_time":	1587351922180,

																"version":	"4.0.0.0",

																"mvcc":	5,

																"alias":	"model",

																"owner":	"ADMIN",

																"config_last_modifier":	"ADMIN",

																"config_last_modified":	1589968416576,

																"description":	"",

																"fact_table":	"SSB.P_LINEORDER",

																"fact_table_alias":	null,

																"management_type":	"MODEL_BASED",

																"join_tables":	[

																				{

																								"table":	"SSB.DATES",

																								"kind":	"LOOKUP",

																								"alias":	"DATES",

																								"join":	{

																												"type":	"LEFT",

																												"primary_key":	[

																																"DATES.D_DATEKEY"

																												],

																												"foreign_key":	[

																																"P_LINEORDER.LO_ORDERDATE"

																												],

																												"non_equi_join_condition":	null,

																												"primary_table":	null,

																												"foreign_table":	null

																								}

																				}

																				...

																],

																"filter_condition":	"",

																"partition_desc":	{

																				"partition_date_column":	"P_LINEORDER.LO_ORDERDATE",

																				"partition_date_start":	0,

																				"partition_date_format":	"yyyyMMdd",

																				"partition_type":	"APPEND",

																				"partition_condition_builder":	"org.apache.kylin.metadata.model.PartitionDesc$DefaultPa

rtitionConditionBuilder"

																},

																"capacity":	"MEDIUM",

																"segment_config":	{

																				"auto_merge_enabled":	true,

																				"auto_merge_time_ranges":	[

																								"WEEK"

																				],

																				"volatile_range":	null,

																				"retention_range":	null

																},

																"data_check_desc":	null,

																"semantic_version":	1,

																"storage_type":	0,

																"all_named_columns":	[

																				{

																								"id":	0,

																								"name":	"LO_SHIPMODE",

																								"column":	"P_LINEORDER.LO_SHIPMODE"

																				},

1039

模型	API

																				...

																],

																"all_measures":	[

																				{

																								"name":	"SUM_REVENUE",

																								"function":	{

																												"expression":	"SUM",

																												"parameters":	[

																																{

																																				"type":	"column",

																																				"value":	"P_LINEORDER.LO_REVENUE"

																																}

																												],

																												"returntype":	"bigint"

																								},

																								"id":	100000

																				},

																				...

																],

																"column_correlations":	[],

																"multilevel_partition_cols":	[],

																"computed_columns":	[],

																"canvas":	{

																				"coordinate":	{

																								"P_LINEORDER":	{

																												"x":	704.3333265516494,

																												"y":	80.94445122612848,

																												"width":	255.55555555555557,

																												"height":	278.8888888888888

																								},

																								...

																				},

																				"zoom":	9.0

																},

																"status":	"WARNING",

																"last_build_end":	"770572800000",

																"storage":	0,

																"source":	0,

																"expansion_rate":	"0",

																"usage":	15,

																"model_broken":	false,

																"root_fact_table_deleted":	false,

																"segments":	null,

																"recommendations_count":	0,

																"available_indexes_count":	0,

																"empty_indexes_count":	5,

																"segment_holes":	[

																				{

																								"@class":	"org.apache.kylin.metadata.model.SegmentRange$TimePartitionedSegmentRange

",

																								"date_range_start":	694368000000,

																								"date_range_end":	738864000000

																				}

																],

																"total_indexes":	5,

																"simplified_measures":	[

																				{

																								"id":	100000,

																								"expression":	"SUM",

																								"name":	"SUM_REVENUE",

																								"return_type":	"bigint",

																								"parameter_value":	[

																												{

																																"type":	"column",

																																"value":	"P_LINEORDER.LO_REVENUE"

																												}

																								],

																								"converted_columns":	[]

																				},

1040

模型	API

																				...

																],

																"dimensions":	[

																				{

																								"table":	"P_LINEORDER",

																								"columns":	[

																													"LO_SUPPKEY",

																													...

																								]

																				}

																],

																"simplified_dimensions":	[

																				{

																								"id":	4,

																								"name":	"P_LINEORDER_LO_SUPPKEY",

																								"column":	"P_LINEORDER.LO_SUPPKEY",

																								"status":	"DIMENSION"

																				},

																				...

																],

																"simplified_tables":	[

																				{

																								"table":	"SSB.P_LINEORDER",

																								"columns":	[

																												{

																																"name":	"LO_ORDERKEY",

																																"datatype":	"bigint",

																																"cardinality":	0,

																																"comment":	null,

																																"is_computed_column":	false

																												},

																												...

																								]

																				},

																				...

																]

												}

								},

								"msg":""

				}

获取模型的平表	SQL	语句

	GET	http://host:port/kylin/api/cubes/{cubeName}/sql

URL	Parameters

	cubeName		-	 	必选		 	string	，	模型名称

HTTP	Header

	Accept:	application/vnd.apache.kylin-v2+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://host:port/kylin/api/cubes/doc_model_01/sql'	\

		-H	'Accept:	application/vnd.apache.kylin-v2+json'	\

		-H	'Accept-Language:	en'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

1041

模型	API

		{

						"code":"000",

						"data":{

												"sql":"SELECT	\n\"LINEITEM\".\"L_ORDERKEY\"	as	\"LINEITEM_L_ORDERKEY\",\n\"LINEITEM\".\"L_PARTK

EY\"	as	\"LINEITEM_L_PARTKEY\",\n\"LINEITEM\".\"L_SHIPDATE\"	as	\"LINEITEM_L_SHIPDATE\",\n\"LINEITEM\".\"L_

COMMITDATE\"	as	\"LINEITEM_L_COMMITDATE\",\n\"LINEITEM\".\"L_RECEIPTDATE\"	as	\"LINEITEM_L_RECEIPTDATE\",\n

\"LINEITEM\".\"L_EXTENDEDPRICE\"	as	\"LINEITEM_L_EXTENDEDPRICE\",\n\"LINEITEM\".\"L_DISCOUNT\"	as	\"LINEITE

M_L_DISCOUNT\",\n\"LINEITEM\".\"L_LINESTATUS\"	as	\"LINEITEM_L_LINESTATUS\",\n\"LINEITEM\".\"L_LINENUMBER\"

	as	\"LINEITEM_L_LINENUMBER\",\n\"LINEITEM\".\"L_QUANTITY\"	as	\"LINEITEM_L_QUANTITY\",\n\"LINEITEM\".\"L_S

UPPKEY\"	as	\"LINEITEM_L_SUPPKEY\",\n\"LINEITEM\".\"L_SHIPINSTRUCT\"	as	\"LINEITEM_L_SHIPINSTRUCT\",\n\"LIN

EITEM\".\"L_TAX\"	as	\"LINEITEM_L_TAX\",\n\"LINEITEM\".\"L_COMMENT\"	as	\"LINEITEM_L_COMMENT\",\n\"LINEITEM

\".\"L_SHIPMODE\"	as	\"LINEITEM_L_SHIPMODE\",\n\"LINEITEM\".\"L_RETURNFLAG\"	as	\"LINEITEM_L_RETURNFLAG\"\n

FROM	\n\"TPCH_FLAT_ORC_5\".\"LINEITEM\"	as	\"LINEITEM\"	\nWHERE	\n1	=	1\n"},

						"msg":""

		}

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

1042

模型	API

构建模型	API

提示：

1.	 Kyligence	Enterprise	REST	API	v2	主要用于	Kyligence	Enterprise	3。目前在	Kyligence	Enterprise	4	中，对于部
分	API	进行了兼容处理，需要注意的是由于版本差异较大，目前返回结果无法做到完全一致。我们强烈建议
您使用	v4	API	进行日常调度和系统对接。

2.	 Kyligence	Enterprise	REST	API	v2	在未来新的大版本中将不再支持。

3.	 请确保已阅读前面的访问及安全认证章节，了解如何在	REST	API	语句中添加认证信息。

4.	 在	Curl	命令行上，如果您访问的	URL	中含有	 	&		符号，请注意转义，比如在	URL	两端加上引号。

注意：Kyligence	Enterprise	4	中模型名称不再全局唯一，因此可能存在不同项目中存在同名的模型。因此我们强烈建议
您使用	v4	版本的模型构建	API，否则将有可能将构建任务随机发送给不同项目的同名模型。

构建模型	-	按日期/时间构建

	PUT	http://host:port/kylin/api/cubes/{cubeName}/rebuild

URL	Parameters

	cubeName		-	 	必选		 	string	，模型名称

HTTP	Header

	Accept:	application/vnd.apache.kylin-v2+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

HTTP	Body:	JSON	Object

	startTime		-	 	必选		 	long	，开始时间，对应	GMT	格式的时间戳，如	 	1388534400000		对应	 	2014-01-01
00:00:00		，推荐使用在线时间戳转换对时间进行处理。
	endTime		-	 	必选		 	long	，结束时间，对应	GMT	格式的时间戳
	buildType		-	 	必选		 	string	，支持的计算类型，为："REFRESH"	或	"BUILD"

Curl	请求示例

curl	-X	PUT	\

'http://host:port/kylin/api/cubes/{cubeName}/rebuild'	\

-H	'Accept:	application/vnd.apache.kylin-v2+json'	\

-H	'Accept-Language:	en'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'	\

-d	'{

		"startTime":	807235200000,

		"endTime":	838944000000,

		"buildType":	"BUILD"

}'

响应示例

{

				"code":	"000",

				"data":	{

								"uuid":	"d1e18412-0f90-428e-b5eb-945833b12fc1",

								"job_type":	"INC_BUILD"

				},

1043

模型	API

				"msg":	""

}

构建模型	-	全量构建

	PUT	http://host:port/kylin/api/cubes/{cubeName}/rebuild

URL	Parameters

	cubeName		-	 	必选		 	string	，模型名称

HTTP	Header

	Accept:	application/vnd.apache.kylin-v2+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

HTTP	Body:	JSON	Object

	startTime		-	 	必选		 	long	，开始时间，0
	endTime		-	 	必选		 	long	，结束时间，9223372036854775807
	buildType		-	 	必选		 	string	，支持的计算类型，为："REFRESH"	或	"BUILD"

Curl	请求示例

curl	-X	PUT	\

'http://host:port/kylin/api/cubes/{cubeName}/rebuild'	\

-H	'Accept:	application/vnd.apache.kylin-v2+json'	\

-H	'Accept-Language:	en'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'	\

-d	'{

		"startTime":	0,

		"endTime":	9223372036854775807,

		"buildType":	"BUILD"

}'

响应示例

{

				"code":	"000",

				"data":	{

								"uuid":	"d1e18412-0f90-428e-b5eb-945833b12fc1",

								"job_type":	"INC_BUILD"

				},

				"msg":	""

}

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

1044

模型	API

Segment	管理	API

提示：

1.	 Kyligence	Enterprise	REST	API	v2	主要用于	Kyligence	Enterprise	3。目前在	Kyligence	Enterprise	4	中，对于部
分	API	进行了兼容处理，需要注意的是由于版本差异较大，目前返回结果无法做到完全一致。我们强烈建议
您使用	v4	API	进行日常调度和系统对接。

2.	 Kyligence	Enterprise	REST	API	v2	在未来新的大版本中将不再支持。

3.	 请确保已阅读前面的访问及安全认证章节，了解如何在	REST	API	语句中添加认证信息。

4.	 在	Curl	命令行上，如果您访问的	URL	中含有	 	&		符号，请注意转义，比如在	URL	两端加上引号。

合并/刷新	Segment

	PUT	http://host:port/kylin/api/cubes/{cubeName}/segments?project=learn_kylin

URL	Parameters

	cubeName		-	 	必选		 	string	，模型名称

	project		-	 	可选		 	string	，	项目名称

HTTP	Header

	Accept:	application/vnd.apache.kylin-v2+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

HTTP	Body:	JSON	Object

	buildType		-	 	必选		 	string	，操作类型，为	"MERGE",	"REFRESH"

	segments		-	 	必选		 	string[]	，Segment	名称（时间区间）。

注意：如果需要刷新一个全量构建的	Segment，对应的Segment名称为	 	FULL_BUILD

Curl	请求示例

curl	-X	PUT	\

'http://host:port/kylin/api/cubes/{cubeName}/segments?project=learn_kylin'	\

-H	'Accept:	application/vnd.apache.kylin-v2+json'	\

-H	'Accept-Language:	en'	\

-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

-H	'Content-Type:	application/json;charset=utf-8'	\

-d	'{

	"segments":["19940801000000_19950801000000",	"19950801000000_19960802000000"],

	"buildType":"MERGE"

}'

响应示例

{

				"code":	"000",

				"data":	[

								{

												"uuid":	"87188890-7562-4d27-9e56-61c0db9d970a",

												"job_type":	"INDEX_REFRESH"

								},

								{

1045

模型	API

												"uuid":	"dcef28e5-1292-4980-a41e-1908996deaf1",

												"job_type":	"INDEX_REFRESH"

								}

				],

				"msg":	""

}

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

1046

项目	API

项目	API

提示：

1.	 Kyligence	Enterprise	REST	API	v2	主要用于	Kyligence	Enterprise	3。目前在	Kyligence	Enterprise	4	中，对于部
分	API	进行了兼容处理，需要注意的是由于版本差异较大，目前返回结果无法做到完全一致。我们强烈建议
您使用	v4	API	进行日常调度和系统对接。

2.	 Kyligence	Enterprise	REST	API	v2	在未来新的大版本中将不再支持。

3.	 请确保已阅读前面的访问及安全认证章节，了解如何在	REST	API	语句中添加认证信息。

4.	 在	Curl	命令行上，如果您访问的	URL	中含有	 	&		符号，请注意转义，比如在	URL	两端加上引号。

返回项目列表

	GET	http://host:port/kylin/api/projects

URL	Parameters

	projectName		-	 	可选		 	string	，项目名称

	exact		-	 	可选		 	boolean	，是否对项目名称进行完全匹配，默认为	 	true

	pageOffset		-	 	可选		 	int	，每页返回的任务的偏移量

	pageSize		-	 	可选		 	int	，每页返回的任务数量

HTTP	Header

	Accept:	application/vnd.apache.kylin-v2+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://host:port/kylin/api/projects'	\

		-H	'Accept:	application/vnd.apache.kylin-v2+json'	\

		-H	'Accept-Language:	en'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":	"000",

				"data":	{

								"projects":	[

												{

																"uuid":	"96b8d3e9-199e-4425-bb99-126944805957",

																"last_modified":	1590054543470,

																"create_time":	1590052938427,

																"version":	"4.0.0.0",

																"mvcc":	29,

																"name":	"leo0521",

																"owner":	"ADMIN",

																"status":	"ENABLED",

																"create_time_utc":	1590052938427,

																"default_database":	"DEFAULT",

																"description":	"",

1047

项目	API

																"principal":	null,

																"keytab":	null,

																"maintain_model_type":	"MANUAL_MAINTAIN",

																"override_kylin_properties":	{

																				"kylin.metadata.semi-automatic-mode":	"true",

																				"kylin.query.metadata.expose-computed-column":	"true",

																				"kylin.source.default":	"9"

																},

																"segment_config":	{

																				"auto_merge_enabled":	true,

																				"auto_merge_time_ranges":	[

																								"WEEK",

																								"MONTH",

																								"QUARTER",

																								"YEAR"

																				],

																				"volatile_range":	{

																								"volatile_range_number":	0,

																								"volatile_range_enabled":	false,

																								"volatile_range_type":	"DAY"

																				},

																				"retention_range":	{

																								"retention_range_number":	1,

																								"retention_range_enabled":	false,

																								"retention_range_type":	"MONTH"

																				}

																},

																"epoch":	{

																				"uuid":	"82aa3303-35d0-49be-87e8-917e0a3e9aa1",

																				"last_modified":	0,

																				"create_time":	1590052938922,

																				"version":	"4.0.0.0",

																				"mvcc":	-1,

																				"epoch_id":	1,

																				"current_epoch_owner":	"10.1.0.234:7070|1590030222585",

																				"last_epoch_renew_time":	1590054543391

																}

												}

														...

								],

								"size":	2

				},

				"msg":	""

}

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

1048

数据源	API

数据源	API

提示：

1.	 Kyligence	Enterprise	REST	API	v2	主要用于	Kyligence	Enterprise	3。目前在	Kyligence	Enterprise	4	中，对于部
分	API	进行了兼容处理，需要注意的是由于版本差异较大，目前返回结果无法做到完全一致。我们强烈建议
您使用	v4	API	进行日常调度和系统对接。

2.	 Kyligence	Enterprise	REST	API	v2	在未来新的大版本中将不再支持。

3.	 请确保已阅读前面的访问及安全认证章节，了解如何在	REST	API	语句中添加认证信息。

4.	 在	Curl	命令行上，如果您访问的	URL	中含有	 	&		符号，请注意转义，比如在	URL	两端加上引号。

返回多个	Hive	表

	GET	http://host:port/kylin/api/tables

URL	Parameters

	project		-	 	必选		string，	项目名
	ext		-	 	可选		 	boolean	，是否返回表的扩展信息

HTTP	Header

	Accept:	application/vnd.apache.kylin-v2+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://host:port/kylin/api/tables?project=doc_expert'	\

		-H	'Accept:	application/vnd.apache.kylin-v2+json'	\

		-H	'Accept-Language:	en'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

		{

		"code":	"000",

		"data":	[

						{

										"uuid":	"a7f89e61-a9f2-dbcc-24db-9d0b56e3dd80",

										"last_modified":	1663583792619,

										"create_time":	1663583792619,

										"version":	"4.0.0.0",

										"mvcc":	0,

										"name":	"{tableName}",

										"columns":	[

														{

																		"id":	"1",

																		"name":	"UPDATE_COL",

																		"datatype":	"integer",

																		"case_sensitive_name":	"update_col",

																		"cardinality":	null,

																		"min_value":	null,

																		"max_value":	null,

																		"null_count":	null

														}

														...

1049

数据源	API

										],

										"source_type":	9,

										"table_type":	"MANAGED",

										"top":	false,

										"increment_loading":	false,

										"last_snapshot_path":	null,

										"last_snapshot_size":	0,

										"snapshot_last_modified":	1663583792619,

										"query_hit_count":	0,

										"partition_column":	null,

										"snapshot_partitions":	{},

										"snapshot_partitions_info":	{},

										"snapshot_total_rows":	0,

										"snapshot_partition_col":	null,

										"selected_snapshot_partition_col":	null,

										"temp_snapshot_path":	null,

										"snapshot_has_broken":	false,

										"database":	"{databaseName}",

										"transactional":	false,

										"rangePartition":	false,

										"partition_desc":	null,

										"exd":	{},

										"root_fact":	false,

										"lookup":	false,

										"primary_key":	[],

										"foreign_key":	[],

										"partitioned_column":	null,

										"partitioned_column_format":	null,

										"segment_range":	null,

										"storage_size":	-1,

										"total_records":	0,

										"sampling_rows":	[],

										"last_build_job_id":	null,

										"kafka_bootstrap_servers":	null,

										"subscribe":	null,

										"batch_table_identity":	null,

										"cardinality":	{},

										"is_transactional":	false

						},

						...

		]

}

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

1050

任务	API

任务	API

提示：

1.	 Kyligence	Enterprise	REST	API	v2	主要用于	Kyligence	Enterprise	3。目前在	Kyligence	Enterprise	4	中，对于部
分	API	进行了兼容处理，需要注意的是由于版本差异较大，目前返回结果无法做到完全一致。我们强烈建议
您使用	v4	API	进行日常调度和系统对接。

2.	 Kyligence	Enterprise	REST	API	v2	在未来新的大版本中将不再支持。

3.	 请确保已阅读前面的访问及安全认证章节，了解如何在	REST	API	语句中添加认证信息。

4.	 在	Curl	命令行上，如果您访问的	URL	中含有	 	&		符号，请注意转义，比如在	URL	两端加上引号。

返回任务列表

	GET	http://host:port/kylin/api/jobs

URL	Parameters

	timeFilter		-	 	必选		 	int	，时间范围。对应关系如下：

时间范围

值

最近一天

最近一周

最近一月

最近一年

所有

0

1

2

3

4

	projectName		-	 	可选		 	string	，项目名称

	status		-	 	可选		 	int	，任务状态，对应关系如下：

任务状态

值

PENDING

RUNNING

FINISHED

ERROR

DISCARDED

STOPPED

1

2

4

8

16

32

	pageOffset		-	 	可选		 	int	，每页返回的任务的偏移量，默认为	0

	pageSize		-	 	可选		 	int	，每页返回的任务数量，默认为	10

	sortBy		-	 	可选		 	string	，排序字段，默认为 	last_modified	，可选	 	project
id	、 	job_name	、 	target_subject	、 	create_time	、 	total_duration	。

	sortby		-	 	可选		 	string	，排序字段，为了与3x对齐新增的参数,不建议与 	sortBy	同时用。

	reverse		-	 	可选		 	boolean	，是否倒序，默认为	"true"

1051

任务	API

	key		-	 	可选		 	string	，过滤字段，支持过滤任务	ID	和任务名称

HTTP	Header

	Accept:	application/vnd.apache.kylin-v2+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://host:port/kylin/api/jobs?projectName=kyligence&timeFilter=0&pageSize=1'	\

		-H	'Accept:	application/vnd.apache.kylin-v2+json'	\

		-H	'Accept-Language:	en'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":	"000",

				"data":	{

								"size":	4,

								"jobs":	[

												{

																"project_name":	"kyligence",

																"related_cube":	"kyligence_1",

																"display_cube_name":	"kyligence_1",

																"uuid":	"dcef28e5-1292-4980-a41e-1908996deaf1",

																"type":	"Refresh	Data",

																"name":	"INDEX_REFRESH",

																"exec_interrupt_time":	0,

																"mr_waiting":	1217,

																"id":	"dcef28e5-1292-4980-a41e-1908996deaf1",

																"last_modified":	1590054785820,

																"duration":	280475,

																"exec_start_time":	1590054505345,

																"steps":	[

																				{

																								"exec_wait_time":	0,

																								"id":	"dcef28e5-1292-4980-a41e-1908996deaf1_00",

																								"name":	"Detect	Resource",

																								"sequence_id":	0,

																								"exec_cmd":	null,

																								"exec_start_time":	1590054505542,

																								"exec_end_time":	1590054529223,

																								"duration":	23681,

																								"wait_time":	0,

																								"create_time":	1590054504128,

																								"step_status":	"FINISHED",

																								"cmd_type":	"SHELL_CMD_HADOOP",

																								"info":	{

																												"yarn_application_id":	"local-1590054511670",

																												"node_info":	"10.1.0.234:7070",

																												"yarn_job_wait_time":	"0",

																												"yarn_job_run_time":	"12373"

																								}

																				}

																				...

																],

																"job_status":	"FINISHED",

																"job_name":	"INDEX_REFRESH",

																"data_range_start":	694281600000,

																"data_range_end":	694368000000,

																"target_model":	"9c6dd695-08c0-4069-9d93-d636c74378d2",

																"target_segments":	[

1052

任务	API

																				"c6ee8f76-a34d-489f-b718-a7874f643e52"

																],

																"step_ratio":	1.0,

																"create_time":	1590054504128,

																"wait_time":	1217,

																"target_subject":	"kyligence_1",

																"target_subject_error":	false,

																"project":	"kyligence",

																"submitter":	"ADMIN",

																"exec_end_time":	1590054785820,

																"discard_safety":	true

												}

												...

								]

				},

				"msg":	""

}

恢复任务

	PUT	http://host:port/kylin/api/jobs/{jobId}/resume

URL	Parameters

	jobId		-	 	必选		 	string	，任务	ID

HTTP	Header

	Accept:	application/vnd.apache.kylin-v2+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	PUT	\

		'http://host:port/kylin/api/jobs/{jobId}/resume'	\

		-H	'Accept:	application/vnd.apache.kylin-v2+json'	\

		-H	'Accept-Language:	en'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":	"000",

				"data":	{

								"id":	"b4de80c1-ed9c-4069-9a01-a296d2353ad6",

								"last_modified":	1590113496137,

								"duration":	8514,

								"exec_start_time":	1590113487622,

								"steps":	null,

								"job_status":	"STOPPED",

								"job_name":	"INC_BUILD",

								"data_range_start":	694368000000,

								"data_range_end":	694454400000,

								"target_model":	"9c6dd695-08c0-4069-9d93-d636c74378d2",

								"target_segments":	[

												"6493bb4b-2715-48d3-b279-7ac35c57337a"

								],

								"step_ratio":	0.0,

								"create_time":	1590113485372,

								"wait_time":	37884,

								"target_subject":	"leo05211",

								"target_subject_error":	false,

								"project":	"leo0521",

1053

任务	API

								"submitter":	"ADMIN",

								"exec_end_time":	1590113496136,

								"discard_safety":	true

				},

				"msg":	""

}

返回任务信息

	GET	http://host:port/kylin/api/jobs/{jobId}

URL	Parameters

	jobId		-	 	必选		 	string	，任务对应的	Job	ID

HTTP	Header

	Accept:	application/vnd.apache.kylin-v2+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	PUT	\

		'http://host:port/kylin/api/jobs/{jobId}'	\

		-H	'Accept:	application/vnd.apache.kylin-v2+json'	\

		-H	'Accept-Language:	en'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":	"000",

				"data":	{

								"project_name":	"kyligence",

								"related_cube":	"kyligence_1",

								"display_cube_name":	"kyligence_1",

								"uuid":	"dcef28e5-1292-4980-a41e-1908996deaf1",

								"type":	"Refresh	Data",

								"name":	"INDEX_REFRESH",

								"exec_interrupt_time":	0,

								"mr_waiting":	1217,

								"id":	"dcef28e5-1292-4980-a41e-1908996deaf1",

								"last_modified":	1590054785820,

								"duration":	280475,

								"exec_start_time":	1590054505345,

								"steps":	[

												{

																"exec_wait_time":	0,

																"id":	"dcef28e5-1292-4980-a41e-1908996deaf1_00",

																"name":	"Detect	Resource",

																"sequence_id":	0,

																"exec_cmd":	null,

																"exec_start_time":	1590054505542,

																"exec_end_time":	1590054529223,

																"duration":	23681,

																"wait_time":	0,

																"create_time":	1590054504128,

																"step_status":	"FINISHED",

																"cmd_type":	"SHELL_CMD_HADOOP",

																"info":	{

																				"yarn_application_id":	"local-1590054511670",

																				"node_info":	"10.1.0.234:7070",

																				"yarn_job_wait_time":	"0",

1054

任务	API

																				"yarn_job_run_time":	"12373"

																}

												}

												...

								],

								"job_status":	"FINISHED",

								"job_name":	"INDEX_REFRESH",

								"data_range_start":	694281600000,

								"data_range_end":	694368000000,

								"target_model":	"9c6dd695-08c0-4069-9d93-d636c74378d2",

								"target_segments":	[

												"c6ee8f76-a34d-489f-b718-a7874f643e52"

								],

								"step_ratio":	1.0,

								"create_time":	1590054504128,

								"wait_time":	1217,

								"target_subject":	"kyligence_1",

								"target_subject_error":	false,

								"project":	"kyligence",

								"submitter":	"ADMIN",

								"exec_end_time":	1590054785820,

								"discard_safety":	true,

								"version":	"4.0.0.0",

								"related_segment":	"c6ee8f76-a34d-489f-b718-a7874f643e52",

								"progress":	100.0

				},

				"msg":	""

}

返回任务某步输出

	GET	http://host:port/kylin/api/jobs/{jobId}/steps/{stepId}/output

URL	Parameters

	jobId		-	 	必选		 	string	，任务对应的	Job	ID

	stepId		-	 	必选		 	string	，步骤对应的	ID

HTTP	Header

	Accept:	application/vnd.apache.kylin-v2+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	PUT	\

		'http://host:port/kylin/api/jobs/{jobId}/steps/{stepId}/output'	\

		-H	'Accept:	application/vnd.apache.kylin-v2+json'	\

		-H	'Accept-Language:	en'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

		"code":	"000",

		"data":	{

						"jobId":	"b0c66219-0c62-2207-2908-21dc7cc35f2c-5c233919-2e52-89b1-e955-1cf187cdd659",

						"nodes":	[],

						"cmd_output":	"2022-10-22T20:43:48,537	INFO		[logger-thread-0]	security.UserGroupInformation	:	Login

successful	for	...",

						"stepId":	"b0c66219-0c62-2207-2908-21dc7cc35f2c-5c233919-2e52-89b1-e955-1cf187cdd659_00"

		},

1055

任务	API

		"msg":	""

}

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

1056

查询	API

查询	API

提示：

1.	 Kyligence	Enterprise	REST	API	v2	主要用于	Kyligence	Enterprise	3。目前在	Kyligence	Enterprise	4	中，对于部
分	API	进行了兼容处理，需要注意的是由于版本差异较大，目前返回结果无法做到完全一致。我们强烈建议
您使用	v4	API	进行日常调度和系统对接。

2.	 Kyligence	Enterprise	REST	API	v2	在未来新的大版本中将不再支持。

3.	 请确保已阅读前面的访问及安全认证章节，了解如何在	REST	API	语句中添加认证信息。

4.	 在	Curl	命令行上，如果您访问的	URL	中含有	 	&		符号，请注意转义，比如在	URL	两端加上引号。

查询数据

	POST	http://host:port/kylin/api/query

HTTP	Header

	Accept:	application/vnd.apache.kylin-v2+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

HTTP	Body:	JSON	Object

	sql		-	 	必选		 	string	，查询的	SQL	语句
	project		-	 	必选		 	string	，项目名称
	offset		-	 	可选		 	int	，	设置查询从哪一行开始往后返回数据。使用时必须与	 	limit		配合使用。
	limit		-	 	可选		 	int	，设置从	 	offset		开始返回的行数，不足	 	limit		以实际行数为准
	forcedToPushDown		-	 	可选		 	boolean	，查询是否强制下压，默认为	 	false	，同时需要打开查询下压开关才可强
制下压

注意：参数	 	forcedToPushDown		和	 	forced_to_index		不能同时为	 	true	，会报错。

Curl	请求示例

curl	-X	POST	\

		'http://host:port/kylin/api/query'	\

		-H	'Accept:	application/vnd.apache.kylin-v2+json'	\

		-H	'Accept-Language:	en'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{	"sql":"select	count(*)	from	SSB.LINEORDER",	"project":"doc_expert"	}'

响应示例

{

				"code":	"000",

				"data":	{

								"columnMetas":	[

												{

																"isNullable":	0,

																"displaySize":	19,

																"label":	"EXPR$0",

																"name":	"EXPR$0",

																"schemaName":	null,

																"catelogName":	null,

																"tableName":	null,

																"precision":	19,

																"scale":	0,

1057

查询	API

																"columnType":	-5,

																"columnTypeName":	"BIGINT	NOT	NULL",

																"readOnly":	false,

																"searchable":	false,

																"caseSensitive":	false,

																"autoIncrement":	false,

																"currency":	false,

																"definitelyWritable":	false,

																"writable":	false,

																"signed":	true

												}

								],

								"results":	[

												[

																"81"

												]

								],

								"affectedRowCount":	0,

								"exceptionMessage":	null,

								"duration":	453,

								"scanRows":	[

												81

								],

								"totalScanRows":	81,

								"scanBytes":	[

												6198

								],

								"totalScanBytes":	6198,

								"resultRowCount":	1,

								"shufflePartitions":	1,

								"hitExceptionCache":	false,

								"storageCacheUsed":	false,

								"queryStatistics":	null,

								"traceUrl":	null,

								"queryId":	"1bc451b8-3cc8-4e4e-8828-8548a34d0468",

								"server":	"10.3.1.17:7070",

								"suite":	null,

								"signature":	"1590054492973_1590054775988_1590113795327;1590052958169",

								"engineType":	"NATIVE",

								"timeout":	false,

								"exception":	false,

								"prepare":	false,

								"partial":	false,

								"isException":	false,

								"appMasterURL":	"/kylin/sparder/SQL/execution/?id=42",

								"pushDown":	false,

								"is_prepare":	false,

								"is_timeout":	false,

								"cube":	"CUBE[name=leo05211]",

								"sparderUsed":	true,

								"totalScanCount":	81,

								"realizations":	[

												{

																"modelId":	"9c6dd695-08c0-4069-9d93-d636c74378d2",

																"modelAlias":	"leo05211",

																"layoutId":	1,

																"indexType":	"Agg	Index",

																"partialMatchModel":	false,

																"valid":	true

												}

								]

				},

				"msg":	""

}

响应信息

	columnMetas		-	每个列的元数据信息

1058

查询	API

	results		-	返回的结果集
	resultRowCount		-	返回结果集行数
	isException		-	这个查询返回是否是异常
	exceptionMessage		-	返回异常对应的内容
	queryId		-	查询	ID
	duration		-	查询耗时
	scanRows		-	总扫描行数
	scanBytes		-	总扫描字节数
	hitExceptionCache		-	是否来自执行失败的结果缓存
	storageCacheUsed		-	是否来自执行成功的结果缓存
	server		-	在启用了负载平衡的环境中，执行查询的服务器
	timeout		-	查询是否超时
	pushDown		-	查询是否下压到其他引擎
	cube		-	使用的查询引擎
	sparderUsed		-	是否使用了	Sparder	查询引擎
	totalScanCount		-	总扫描行数

列出可查询的表

	GET	http://host:port/kylin/api/tables_and_columns

URL	Parameters

	project		-	 	必选		string，	项目名
	cube		-	 	可选		 	boolean	，cube名称

HTTP	Header

	Accept:	application/vnd.apache.kylin-v2+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://host:port/kylin/api/tables_and_columns?project=doc_expert'	\

		-H	'Accept:	application/vnd.apache.kylin-v2+json'	\

		-H	'Accept-Language:	en'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

		"code":	"000",

		"data":	[

						{

										"columns":	[...],

										"type":	[

														"LOOKUP"

										],

										"type_CAT":	null,

										"table_TYPE":	"TABLE",

										"type_SCHEM":	null,

										"self_REFERENCING_COL_NAME":	null,

										"ref_GENERATION":	null,

										"table_CAT":	"defaultCatalog",

										"table_SCHEM":	"SSB",

										"table_NAME":	"DATES_VIEW",

										"type_NAME":	null,

1059

查询	API

										"remarks":	null

						},

						...

		]

}

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

1060

异步查询	API

异步查询	API

提示：

1.	 Kyligence	Enterprise	REST	API	v2	主要用于	Kyligence	Enterprise	3。目前在	Kyligence	Enterprise	4	中，对于部
分	API	进行了兼容处理，需要注意的是由于版本差异较大，目前返回结果无法做到完全一致。我们强烈建议
您使用	v4	API	进行日常调度和系统对接。

2.	 Kyligence	Enterprise	REST	API	v2	在未来新的大版本中将不再支持。

3.	 请确保已阅读前面的访问及安全认证章节，了解如何在	REST	API	语句中添加认证信息。

4.	 在	Curl	命令行上，如果您访问的	URL	中含有	 	&		符号，请注意转义，比如在	URL	两端加上引号。

5.	 自	4.6.4	版本起，为了解决返回大量结果的性能问题，产品进行了变更， 	include_header		参数被移至提交异

步查询的	API，下载结果中的	 	include_header		参数将不起作用。

提交查询

	POST	http://host:port/kylin/api/async_query

HTTP	Header

	Accept:	application/vnd.apache.kylin-v2+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

HTTP	Body:	JSON	Object

	sql		-	 	必选		 	string	，查询语句
	separator		-	 	可选		 	string	，导出结果的分隔符，默认为	","
	offset		-	 	可选		 	int	，查询结果的偏移量。使用时必须与	 	limit		配合使用。
	limit		-	 	可选		 	int	，从偏移量开始返回对应的行数，不足	limit	以实际行数为准
	project		-	 	必选		 	string	，项目名，默认为	"DEFAULT"
	include_header		-	 	可选		 	boolean	，下载结果是否包含表头，默认为	false

Curl	请求示例

curl	-X	POST	\

		'http://host:port/kylin/api/async_query'	\

		-H	'Accept:	application/vnd.apache.kylin-v2+json'	\

		-H	'Accept-Language:	en'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{	"sql":"select	*	from	KYLIN_SALES	limit	100",	"project":"learn_kylin"	}'

响应示例

{

				"code":	"000",

				"data":	{

								"queryID":	"eb3e837f-d826-4670-aac7-2b92fcd0c8fe",

								"status":	"RUNNING",

								"info":	"still	running"

				},

				"msg":	""

}

1061

异步查询	API

响应信息

	queryID		-	异步查询的	Query	ID
	status		-	提交的状态，分为："FAILED"	和	"RUNNING"
	info		-	提交状态的详细信息

返回查询状态

	GET	http://host:port/kylin/api/async_query/{queryID}/status

URL	Parameters

	queryID		-	 	必选		 	string	，异步查询的	Query	ID

HTTP	Header

	Accept:	application/vnd.apache.kylin-v2+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://host:port/kylin/api/async_query/{queryID}/status'	\

		-H	'Accept:	application/vnd.apache.kylin-v2+json'	\

		-H	'Accept-Language:	en'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":	"000",

				"data":	{

								"queryID":	"eb3e837f-d826-4670-aac7-2b92fcd0c8fe",

								"status":	"SUCCESSFUL",

								"info":	"await	fetching	results"

				},

				"msg":	""

}

响应信息

	queryID		-	异步查询的	Query	ID
	status		-	查询状态，该状态分为："SUCCESSFUL"	（成功），"RUNNING"（仍在运行中），"FAILED"	(失
败)	和	"MISSING"	(查询不到此查询)，
	info		-	查询状态的详细信息

返回查询的元数据信息

	GET	http://host:port/kylin/api/async_query/{queryID}/metadata

URL	Parameters

	queryID		-	 	必选		 	string	，异步查询的	Query	ID

HTTP	Header

	Accept:	application/vnd.apache.kylin-v2+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

1062

异步查询	API

Curl	请求示例

curl	-X	GET	\

		'http://host:port/kylin/api/async_query/{queryID}/metadata'	\

		-H	'Accept:	application/vnd.apache.kylin-v2+json'	\

		-H	'Accept-Language:	en'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":	"000",

				"data":	[

								[

												"TRANS_ID",

												"PART_DT"

								],

								[

												"BIGINT",

												"DATE"

								]

				],

				"msg":	""

}

响应信息

	data		-	data	中包含两个	list，其中第一个	list	为列名，第二个	list	为列对应的数据类型

返回查询结果文件大小

	GET	http://host:port/kylin/api/async_query/{queryID}/filestatus

URL	Parameters

	queryID		-	 	必选		 	string	，异步查询的	Query	ID

HTTP	Header

	Accept:	application/vnd.apache.kylin-v2+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://host:port/kylin/api/async_query/{queryID}/filestatus'	\

		-H	'Accept:	application/vnd.apache.kylin-v2+json'	\

		-H	'Accept-Language:	en'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":	"000",

				"data":	7611,

				"msg":	""

}

响应信息

1063

异步查询	API

	data		-	保存结果的总大小

下载查询结果

提示：请确认查询状态为	SUCCESSFUL	之后再调用此接口

	GET	http://host:port/kylin/api/async_query/{query_id}/result_download?includeHeader=true

注意：自	4.6.4	版本起， 	include_header		参数被移至提交异步查询的	API，下载结果中的	 	include_header
参数将不起作用。

URL	Parameters

	query_id		-	 	必选		 	string	，异步查询的	Query	ID
	project		-	 	可选		 	string	，项目名称

HTTP	Header

	Accept:	application/vnd.apache.kylin-v2+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

		curl	-X	GET	\

				'http://host:port/kylin/api/async_query/{queryID}/result_download?includeHeader=true'	\

				-H	'Accept:	application/vnd.apache.kylin-v2+json'	\

				-H	'Accept-Language:	en'	\

				-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

				-H	'Content-Type:	application/json;charset=utf-8'	\

				-o	result.csv

响应示例

返回一个名为	 	result.csv		的文件

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

1064

访问控制权限	API

访问控制权限	API

提示：

1.	 Kyligence	Enterprise	REST	API	v2	主要用于	Kyligence	Enterprise	3。目前在	Kyligence	Enterprise	4	中，对于部
分	API	进行了兼容处理，需要注意的是由于版本差异较大，目前返回结果无法做到完全一致。我们强烈建议
您使用	v4	API	进行日常调度和系统对接。

2.	 Kyligence	Enterprise	REST	API	v2	在未来新的大版本中将不再支持。

3.	 请确保已阅读前面的访问及安全认证章节，了解如何在	REST	API	语句中添加认证信息。

4.	 在	Curl	命令行上，如果您访问的	URL	中含有	 	&		符号，请注意转义，比如在	URL	两端加上引号。

Kyligence	Enterprise	提供了可以用来控制用户对于项目、表、用户和用户组等的访问控制权限的	REST	API，基于这些
API，用户可以严格地管理相关的访问控制权限列表。

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

1065

访问控制权限	API

用户管理	API

提示：

1.	 Kyligence	Enterprise	REST	API	v2	主要用于	Kyligence	Enterprise	3。目前在	Kyligence	Enterprise	4	中，对于部
分	API	进行了兼容处理，需要注意的是由于版本差异较大，目前返回结果无法做到完全一致。我们强烈建议
您使用	v4	API	进行日常调度和系统对接。

2.	 Kyligence	Enterprise	REST	API	v2	在未来新的大版本中将不再支持。

3.	 请确保已阅读前面的访问及安全认证章节，了解如何在	REST	API	语句中添加认证信息。

4.	 在	Curl	命令行上，如果您访问的	URL	中含有	 	&		符号，请注意转义，比如在	URL	两端加上引号。

返回用户列表

	GET	http://host:port/kylin/api/kap/user/users

URL	Parameters

	name		-	 	可选		 	string	，用户名称
	isCaseSensitive		-	 	可选		 	boolean	，对用户名称的模糊匹配是否区分大小写，默认为	false
	pageOffset		-	 	可选		 	int	，返回数据的起始下标，默认为	0
	pageSize		-	 	可选		 	int	，分页返回每页返回的条数，默认为	10

HTTP	Header

	Accept:	application/vnd.apache.kylin-v2+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://host:port/kylin/api/kap/user/users?pageSize=1'	\

		-H	'Accept:	application/vnd.apache.kylin-v2+json'	\

		-H	'Accept-Language:	en'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

{

				"code":	"000",

				"data":	{

								"users":	[

												{

																"username":	"ADMIN",

																"authorities":	[

																				{

																								"authority":	"ROLE_ADMIN"

																				},

																				{

																								"authority":	"ALL_USERS"

																				}

																],

																"disabled":	false,

																"defaultPassword":	false,

																"locked":	false,

																"uuid":	"aaf02c5d-1605-42fa-abf9-9b0bb5715a6a",

																"last_modified":	1590201214907,

1066

访问控制权限	API

																"create_time":	1586744927779,

																"version":	"4.0.0.0",

																"mvcc":	70,

																"locked_time":	1590144195021,

																"wrong_time":	0,

																"first_login_failed_time":	1590144125587

												},

												...

								]

				},

				"msg":	""

}

返回用户拥有的项目及表权限

	GET	http://host:port/kylin/api/access/{userName}

URL	Parameters

	userName		-	 	必选		 	string	，用户名称

HTTP	Header

	Accept:	application/vnd.apache.kylin-v2+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://host:port/kylin/api/access/DOC'	\

		-H	'Accept:	application/vnd.apache.kylin-v2+json'	\

		-H	'Accept-Language:	en'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

		{

						"code":	"000",

						"data":	[

										{

														"project_name":	"doc_expert",

														"table_name":	[

																		"DEFAULT.SAMPLE_07",

																		"DEFAULT.SAMPLE_08",

																		"EDW.TEST_CAL_DT",

																		"EDW.TEST_SELLER_TYPE_DIM",

																		"EDW.TEST_SELLER_TYPE_DIM_TABLE",

																		"EDW.TEST_SITES",

																		"SSB.CUSTOMER",

																		"SSB.DATES",

																		"SSB.LINEORDER",

																		"SSB.PART",

																		"SSB.P_LINEORDER",

																		"SSB.SUPPLIER"

														]

										}

						],

						"msg":	""

		}

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

1067

访问控制权限	API

用户组管理	API

提示：

1.	 Kyligence	Enterprise	REST	API	v2	主要用于	Kyligence	Enterprise	3。目前在	Kyligence	Enterprise	4	中，对于部
分	API	进行了兼容处理，需要注意的是由于版本差异较大，目前返回结果无法做到完全一致。我们强烈建议
您使用	v4	API	进行日常调度和系统对接。

2.	 Kyligence	Enterprise	REST	API	v2	在未来新的大版本中将不再支持。

3.	 请确保已阅读前面的访问及安全认证章节，了解如何在	REST	API	语句中添加认证信息。

4.	 在	Curl	命令行上，如果您访问的	URL	中含有	 	&		符号，请注意转义，比如在	URL	两端加上引号。

返回用户组及其用户

	GET	http://host:port/kylin/api/user_group/usersWithGroup

URL	Parameters

	pageOffset		-	 	可选		 	int	，返回数据的起始下标，默认为	0
	pageSize		-	 	可选		 	int	，分页返回每页返回的条数，默认为	10

HTTP	Header

	Accept:	application/vnd.apache.kylin-v2+json

	Accept-Language:	en

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://host:port/kylin/api/user_group/usersWithGroup?pageSize=1'	\

		-H	'Accept:	application/vnd.apache.kylin-v2+json'	\

		-H	'Accept-Language:	en'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

		{

						"code":	"000",

						"data":	{

										"size":	5,

										"usersWithGroup":	[

														{

																		"first":	"ALL_USERS",

																		"second":	[

																						"ADMIN",

																						"ANALYST",

																						"DOC",

																						"MODELER",

																						"TEST"

																		],

																		"value":	[

																						"ADMIN",

																						"ANALYST",

																						"DOC",

																						"MODELER",

																						"TEST"

																		],

																		"key":	"ALL_USERS"

1068

访问控制权限	API

														}

										]

						},

						"msg":	"get	users	with	group"

		}

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

1069

访问控制权限	API

项目级访问控制权限	API

提示：

1.	 Kyligence	Enterprise	REST	API	v2	主要用于	Kyligence	Enterprise	3。目前在	Kyligence	Enterprise	4	中，对于部
分	API	进行了兼容处理，需要注意的是由于版本差异较大，目前返回结果无法做到完全一致。我们强烈建议
您使用	v4	API	进行日常调度和系统对接。

2.	 Kyligence	Enterprise	REST	API	v2	在未来新的大版本中将不再支持。

3.	 请确保已阅读前面的访问及安全认证章节，了解如何在	REST	API	语句中添加认证信息。

4.	 在	Curl	命令行上，如果您访问的	URL	中含有	 	&		符号，请注意转义，比如在	URL	两端加上引号。

获取项目级访问控制权限

	GET	http://host:port/kylin/api/access/{type}/{project}

URL	Parameters

	type		-	 	必选		 	string	，"ProjectInstance"
	project		-	 	必选		 	string	，项目名称

HTTP	Header

	Accept:	application/vnd.apache.kylin-v2+json

	Accept-Language:	cn

	Content-Type:	application/json;charset=utf-8

Curl	请求示例

curl	-X	GET	\

		'http://host:port/kylin/api/access/ProjectInstance/{project}'	\

		-H	'Accept:	application/vnd.apache.kylin-v2+json'	\

		-H	'Accept-Language:	cn'	\

		-H	'Authorization:	Basic	QURNSU46S1lMSU4='	\

		-H	'Content-Type:	application/json;charset=utf-8'

响应示例

		{

						"code":	"000",

						"data":	{

										"sids":	[

														{

																		"permission":	{

																						"mask":	16,

																						"pattern":	"...........................A...."

																		},

																		"id":	0,

																		"sid":	{

																						"principal":	"ADMIN"

																		},

																		"granting":	true,

																			"ext_permissions":	[

																				{

																						"mask":	128,

																						"pattern":	"........................Q......."

																				}

																		]

														},

														{

1070

访问控制权限	API

																		"permission":	{

																						"mask":	1,

																						"pattern":	"...............................R"

																		},

																		"id":	1,

																		"sid":	{

																						"principal":	"DOC"

																		},

																		"granting":	true

														}

										],

										"size":	2

						},

						"msg":	""

		}

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

1071

数据源扩展	SDK

数据源扩展	SDK

Kyligence	Enterprise	支持通过	JDBC	接口接入自定义数据源，如	RDBMS	数据源。

对于常见的一些数据源，Kyligence	Enterprise	提供默认的数据源连接器，用户只需要一些简单的配置即可接入数据源，
后续可以建立模型，预计算构建索引，和查询下压至自定义数据源。

对于比较特殊或希望有较高程度定制的数据源，可以基于	Kyligence	Enterprise	提供的数据源扩展	SDK，开发新的数据源
连接器，满足更加个性化的需求。

注意：本文介绍的方案属于高级开发方案，需在	Kyligence	服务人员的支持下使用。请和您的客户代表联系，获取所需
Jar	包并协商使用方案。

相关概念介绍

扩展数据源：一般指除	Hive、Kafka	外的其他数据源，通常是可以通过	JDBC	接口接入的数据源，如	MySQL、SQL
Server、GBase、Oracle、Impala	等。

数据源连接器：Kyligence	连接扩展数据源所需要的辅助工具，一般为	Jar	包形式。	对于扩展数据源的连接，Kyligence
为可插拔式设计，可以根据需要将特定数据源的连接器放置到指定目录，并添加相关配置后，即可连接指定数据源，并

进行构建和查询下压等相关操作。	Kyligence	会提供一些常见数据源的默认连接器，详见后续章节的已支持的数据源连
接器列表，对于尚未提供数据源连接器的扩展数据源，用户也可以通过数据源扩展	SDK	开发自定义数据源连接器。

数据源扩展	SDK：Kyligence	提供的数据源连接器开发包，用户可以基于此	SDK	快速开发新数据源连接器。在数据源扩
展	SDK	中，Kyligence	开放了扩展数据源的接口，针对不同的数据源，用户可以定义或重写支持的运算符和函数。

以上三个概念示意图为：

数据源扩展	SDK	相关概念示意图

1072

数据源扩展	SDK

如何连接和使用新数据源

获取数据源连接器，并部署到指定目录

1.	 获取数据源对应的数据源连接器。此方案目前属于高级开发方案，请和您的客户代表联系，获取所需	Jar	包并协商

使用方案。

2.	 将该数据源连接器（Jar	包）放入	 	${KYLIN_HOME}/lib/ext		目录下。
3.	 重新启动	Kyligence	Enterprise	使以上	Jar	包生效。

添加配置，添加扩展数据源

可以选择在系统级配置或项目级配置：

1.	 系统级配置

在	 	conf/kylin.properties		增加如下配置，添加系统级配置后，需要重新启动	Kyligence	Enterprise	使参数生效。

下述参数的项目级配置可在设置->基本设置->数据源设置中设置。

kylin.source.jdbc.source.name：JDBC	数据源名称，用于页面显示。

kylin.source.jdbc.connection-url：JDBC	连接字符串。

kylin.source.jdbc.driver：JDBC	驱动，如	 	com.mysql.jdbc.Driver	。

kylin.source.jdbc.user：JDBC	连接用户名。

kylin.source.jdbc.pass：JDBC	连接密码。

下述参数的项目级配置可在设置->高级设置->自定义项目配置中设置。

kylin.source.jdbc.dialect：JDBC	方言，如	mysql,gbase。

kylin.query.pushdown.runner-class-name：查询下压接口实现类，值为
	org.apache.kylin.sdk.datasource.PushDownRunnerSDKImpl	。

kylin.query.pushdown.partition-check.runner-class-name：查询下压分区检查实现类，值为
	org.apache.kylin.sdk.datasource.PushDownRunnerSDKImpl	。

kylin.source.jdbc.adaptor：JDBC	方言适配器实现类，根据实际填写，如
	org.apache.kylin.source.jdbc.demo.DemoSourceConnector	。

kylin.source.jdbc.connector-class-name：获取	JDBC	数据的实现类，根据实际填写，如
	org.apache.kylin.source.jdbc.demo.DemoSourceConnector	。

kylin.engine.extra-jars-path：访问数据源依赖的	jar	包，按照	 	,		分割，	如	 	${KYLIN_HOME}/lib/ext/druid-
1.1.19.jar,${KYLIN_HOME}/lib/ext/gbase-connector-java-8.3.81.51-build-53.6-

bin.jar,${KYLIN_HOME}/lib/ext/kap-source-connector-gbase8a-1.0.3.jar	。

示例如下：

			#	Pushdown

			kylin.source.jdbc.dialect=${dialect}

			kylin.source.jdbc.connection-url=${connectionUrl}

			kylin.source.jdbc.driver=${driverClass}

			kylin.source.jdbc.user=${username}

			kylin.source.jdbc.pass=${password}

			kylin.query.pushdown.runner-class-name=org.apache.kylin.sdk.datasource.PushDownRunnerSDKImpl

			kylin.query.pushdown.partition-check.runner-class-name=org.apache.kylin.sdk.datasource.PushDownRunnerSDKImpl

1073

数据源扩展	SDK

			kylin.source.jdbc.adaptor=org.apache.kylin.source.jdbc.demo.DemoSourceConnector

			#	Build

			kylin.source.jdbc.connector-class-name=org.apache.kylin.source.jdbc.demo.DemoSourceConnector

1.	 在项目级配置	在	 	页面->设置->基本设置->数据源设置		开启	JDBC	数据源，并添加数据源信息：

开启	JDBC	数据源

添加数据源信息

1074

数据源扩展	SDK

参数

描述

数据源名称

数据源显示名称，将在加载数据源时显示此名称，如	mysql,gbase

JDBC	连接字符串

JDBC	连接字符串

用户名

密码

驱动

JDBC	连接用户名

JDBC	连接密码

JDBC	驱动，如	 	com.mysql.jdbc.Driver

并在	 	页面->设置->高级设置->自定义项目配置		中添加其他必要的配置项，详见上述系统级配置。

加载扩展数据源表

进入具体项目数据资产界面，选择数据源选项卡；点击按钮，在弹出窗口中，选择	JDBC	作为数据源类型。然后点击
下一步	按钮，进入加载	JDBC	表元数据窗口，您可按需在左侧的表清单中，单击选中需要建模的表，也支持输入关键
字进行搜索。

1075

数据源扩展	SDK

更详细的操作请参考	导入	Hive	数据源。

从	Kyligence	Enterprise	4.5.2	GA	版本开始支持前端直接加载扩展数据源表，在之前的	Kyligence	Enterprise	4.5.0、
4.5.1	版本只支持通过	API	加载扩展数据源表，旧版本建议升级。

创建模型

进入具体项目数据资产功能，选择模型选项卡；点击页面中间的	+	模型	按钮，开始创建模型。具体的模型创建方法请
参考	基本模型设计	章节。

加载数据

请在模型列表界面选择构建索引。更详细的操作请参考	加载数据	章节。

查询分析

请进入导航栏	查询	->	分析	界面，进行查询分析，验证查询命中模型。更详细的操作请参考	查询分析	章节。	或者您也
可以选择跳过	2-3	步骤，直接将查询下压到扩展数据源。

已支持的数据源连接器列表

GBase

MySQL

Impala

ClickHouse

Oracle	11g

Greenplum

TiDB

Doris

1076

数据源扩展	SDK

GaussDB	DWS

CirroData

Google	BigQuery

根据您的部署环境，部分数据源连接器可能需要定制化开发，您可以联系	Kyligence	客户经理获取相关解决方案。

如何基于数据源扩展	SDK，开发新的数据源连接器

详细的开发细节，请参考	基于数据源扩展	SDK，开发新的数据源连接器

已知限制

目前只支持通过	JDBC	方式连接的数据源。
目前不支持在一个模型中同时引用	JDBC	数据源和其他数据源，如	Hive、Kafka	等。
目前不支持在查询下压中对	JDBC	数据源和其他数据源，如	Hive、Kafka	等进行关联查询。
4.6.22.0	版本之前项目级自定义配置可能不生效，从	4.6.22.0	版本后，您可在项目级添加	 	kylin.source.jdbc.extend=
{$当前项目名}		配置项，然后正常使用项目级自定义配置功能。

FAQ

1.	 在旧版本	Kyligence	Enterprise	4.5.0、4.5.1	版本中，如何通过	API	加载扩展数据源表？

在部署相关的数据源连接器，并配置对应的参数后，可以调用此	API	加载数据源表：

curl	-X	PUT	\

		http://{localhost}:{port}/kylin/api/projects/{project}/jdbc_config	\

		-H	'Accept:	application/vnd.apache.kylin-v4-public+json'	\

		-H	'Accept-Language:	en'	\

		-H	'Authorization:	Basic	QURNSU46dGVzdEAxMjM='	\

		-H	'Content-Type:	application/json;charset=utf-8'	\

		-d	'{

		"url":	"${connectionUrl}",

		"user":	"${username}",

		"pass":	"${password}",

		"driver":	"${driverClass}",

		"dialect":	"${dialect}",

		"adaptor":	"io.kyligence.kap.source.adaptor.{dialect}Adaptor",

		"pushdown_class":"org.apache.kylin.sdk.datasource.PushDownRunnerSDKImpl"

}'

©	2019	Kyligence	Inc.	All	rights	reserved.	Powered	by	Gitbook.												Last	Modified：	2024-11-11	11:46:02

1077

如何基于数据源扩展	SDK，开发新的数据源连接器

如何基于数据源扩展	SDK，开发新的数据源连接器

下面的样例，向您展示如何从源代码编译到打包部署一个自定义的数据源连接器。

搭建开发环境

在项目的	lib	目录中加入	 	$KYLIN_HOME/server/jars/ke-source-jdbc-ext-4.0.0-SNAPSHOT.jar	，
	$KYLIN_HOME/server/jars/kylin-source-jdbc-5.0.0-SNAPSHOT.jar	，	 	$KYLIN_HOME/server/jars/kylin-core-common-5.0.0-
SNAPSHOT.jar	，	 	$KYLIN_HOME/server/jars/kylin-datasource-sdk-5.0.0-SNAPSHOT.jar	，并将其添加到项目依赖中。您可
以在	IDE	中打开并编译这个样例程序。

样例会创建一个基于内存的数据源，该数据源中包含两个数据库	default	和	ssb，存在一张表	ssb.part。

实现新数据源的配置

SDK	提供转换的机制，框架里预定义一个配置文件	 	default.xml		对应	ANSI	SQL	方言。开发者不需要编码，只需要为
新的数据源新建一个配置文件	 	{dialect}.xml	。

提示：相应配置可参考下面的	 	default.xml		文件模版

<?xml	version="1.0"?>

<!--

	Licensed	to	the	Apache	Software	Foundation	(ASF)	under	one

	or	more	contributor	license	agreements.		See	the	NOTICE	file

	distributed	with	this	work	for	additional	information

	regarding	copyright	ownership.		The	ASF	licenses	this	file

	to	you	under	the	Apache	License,	Version	2.0	(the

	"License");	you	may	not	use	this	file	except	in	compliance

	with	the	License.		You	may	obtain	a	copy	of	the	License	at

					http://www.apache.org/licenses/LICENSE-2.0

	Unless	required	by	applicable	law	or	agreed	to	in	writing,	software

	distributed	under	the	License	is	distributed	on	an	"AS	IS"	BASIS,

	WITHOUT	WARRANTIES	OR	CONDITIONS	OF	ANY	KIND,	either	express	or	implied.

	See	the	License	for	the	specific	language	governing	permissions	and

	limitations	under	the	License.

-->

<DATASOURCE_DEF	NAME="kylin"	ID="default">

				<PROPERTY	NAME="sql.default-converted-enabled"	VALUE="true"/>

				<PROPERTY	NAME="sql.allow-no-offset"	VALUE="true"/>

				<PROPERTY	NAME="sql.allow-fetch-no-rows"	VALUE="true"/>

				<PROPERTY	NAME="sql.allow-no-orderby-with-fetch"	VALUE="true"/>

				<PROPERTY	NAME="sql.keyword-default-escape"	VALUE="true"/>

				<PROPERTY	NAME="sql.keyword-default-uppercase"	VALUE="true"/>

				<PROPERTY	NAME="sql.case-sensitive"	VALUE="false"/>

1078

如何基于数据源扩展	SDK，开发新的数据源连接器

				<PROPERTY	NAME="metadata.enable-cache"	VALUE="false"/>

				<!--Min-->

				<FUNCTION_DEF	ID="1"	EXPRESSION="MIN($0)"/>

				<!--Max-->

				<FUNCTION_DEF	ID="3"	EXPRESSION="MAX($0)"/>

				<!--CurrentDate-->

				<FUNCTION_DEF	ID="5"	EXPRESSION="CURRENT_DATE"/>

				<!--CurrentDateTime-->

				<FUNCTION_DEF	ID="6"	EXPRESSION="CURRENT_TIMESTAMP"/>

				<!--Date-->

				<FUNCTION_DEF	ID="7"	EXPRESSION="CAST($0	AS	DATE)"/>

				<!--DayOfMonth-->

				<FUNCTION_DEF	ID="8"	EXPRESSION="EXTRACT(DAY	FROM	$0)"/>

				<!--DayOfYear-->

				<FUNCTION_DEF	ID="9"	EXPRESSION="DAYOFYEAR($0)"/>

				<!--Month-->

				<FUNCTION_DEF	ID="10"	EXPRESSION="EXTRACT(MONTH	FROM	$0)"/>

				<!--Quarter-->

				<FUNCTION_DEF	ID="11"	EXPRESSION="EXTRACT(QUARTER	FROM	$0)"/>

				<!--Year-->

				<FUNCTION_DEF	ID="12"	EXPRESSION="EXTRACT(YEAR	FROM	$0)"/>

				<!--IsNotNull-->

				<FUNCTION_DEF	ID="13"	EXPRESSION="$0	IS	NOT	NULL"/>

				<!--IsNull-->

				<FUNCTION_DEF	ID="14"	EXPRESSION="$0	IS	NULL"/>

				<!--NullToZero-->

				<FUNCTION_DEF	ID="15"	EXPRESSION="COALESCE($0,	0)"/>

				<!--ZeroToNull-->

				<FUNCTION_DEF	ID="16"	EXPRESSION="NULLIF($0,	0)"/>

				<!--FirstInRange-->

				<FUNCTION_DEF	ID="17"	EXPRESSION="first_value($0)	over($1)"/>

				<!--MovingAvg-->

				<FUNCTION_DEF	ID="18"	EXPRESSION="avg($0)	over($1)"/>

				<!--MovingCount-->

				<FUNCTION_DEF	ID="19"	EXPRESSION="count($0)	over($1)"/>

				<!--MovingMax-->

				<FUNCTION_DEF	ID="20"	EXPRESSION="max($0)	over($1)"/>

				<!--MovingMin-->

				<FUNCTION_DEF	ID="21"	EXPRESSION="min($0)	over($1)"/>

				<!--MovingSum-->

				<FUNCTION_DEF	ID="22"	EXPRESSION="sum($0)	over($1)"/>

				<!--RunningStdevP-->

				<FUNCTION_DEF	ID="23"	EXPRESSION="STDDEV_POP($0)	OVER($1)"/>

				<!--LeftStr-->

				<FUNCTION_DEF	ID="24"	EXPRESSION="SUBSTRING($0,	1,	$1)"/>

				<!--Length-->

				<FUNCTION_DEF	ID="25"	EXPRESSION="CHAR_LENGTH($0)"/>

				<!--Lower-->

				<FUNCTION_DEF	ID="26"	EXPRESSION="LOWER($0)"/>

				<!--SubStr-->

				<FUNCTION_DEF	ID="27"	EXPRESSION="SUBSTRING($0,	$1,	$2)"/>

				<!--initcap-->

				<FUNCTION_DEF	ID="28"	EXPRESSION="INITCAP($0)"/>

				<!--Trim-->

				<FUNCTION_DEF	ID="29"	EXPRESSION="TRIM($0)"/>

				<!--Upper-->

				<FUNCTION_DEF	ID="30"	EXPRESSION="UPPER($0)"/>

				<!--Abs-->

				<FUNCTION_DEF	ID="31"	EXPRESSION="ABS($0)"/>

				<!--Acos-->

				<FUNCTION_DEF	ID="32"	EXPRESSION="ACOS($0)"/>

				<!--Asin-->

				<FUNCTION_DEF	ID="34"	EXPRESSION="ASIN($0)"/>

				<!--Atan-->

				<FUNCTION_DEF	ID="36"	EXPRESSION="ATAN($0)"/>

				<!--Atan2-->

				<FUNCTION_DEF	ID="37"	EXPRESSION="ATAN2($1,	$0)"/>

				<!--Ceiling-->

				<FUNCTION_DEF	ID="39"	EXPRESSION="CEIL($0)"/>

1079

如何基于数据源扩展	SDK，开发新的数据源连接器

				<!--Cos-->

				<FUNCTION_DEF	ID="40"	EXPRESSION="COS($0)"/>

				<!--Degrees-->

				<FUNCTION_DEF	ID="42"	EXPRESSION="DEGREES($0)"/>

				<!--Exp-->

				<FUNCTION_DEF	ID="43"	EXPRESSION="EXP($0)"/>

				<!--Floor-->

				<FUNCTION_DEF	ID="44"	EXPRESSION="FLOOR($0)"/>

				<!--Int-->

				<FUNCTION_DEF	ID="45"	EXPRESSION="FLOOR($0)"/>

				<!--Int2-->

				<FUNCTION_DEF	ID="46"	EXPRESSION="FLOOR($0)"/>

				<!--Ln-->

				<FUNCTION_DEF	ID="47"	EXPRESSION="LN($0)"/>

				<!--Log-->

				<FUNCTION_DEF	ID="48"	EXPRESSION="LN($0)/LN($1)"/>

				<!--Log10-->

				<FUNCTION_DEF	ID="49"	EXPRESSION="LOG10($0)"/>

				<!--Mod-->

				<FUNCTION_DEF	ID="50"	EXPRESSION="$0-FLOOR($0/$1)*$1"/>

				<!--Power-->

				<FUNCTION_DEF	ID="51"	EXPRESSION="POWER($0,	$1)"/>

				<!--Radians-->

				<FUNCTION_DEF	ID="53"	EXPRESSION="RADIANS($0)"/>

				<!--Round-->

				<FUNCTION_DEF	ID="55"	EXPRESSION="ROUND($0,	0)"/>

				<!--Sin-->

				<FUNCTION_DEF	ID="56"	EXPRESSION="SIN($0)"/>

				<!--Sqrt-->

				<FUNCTION_DEF	ID="58"	EXPRESSION="SQRT($0)"/>

				<!--Tan-->

				<FUNCTION_DEF	ID="59"	EXPRESSION="TAN($0)"/>

				<!--Trunc-->

				<FUNCTION_DEF	ID="61"	EXPRESSION="CAST($0	AS	INTEGER)"/>

				<!--Median-->

				<FUNCTION_DEF	ID="63"	EXPRESSION="MEDIAN($0)"/>

				<!--Daysbetween-->

				<FUNCTION_DEF	ID="64"	EXPRESSION="TIMESTAMPDIFF(day,	$0,	$1)"/>

				<!--DateAdd-->

				<FUNCTION_DEF	ID="65"	EXPRESSION="TIMESTAMPADD(day,	$1,	$0)"/>

				<!--AddMonths-->

				<FUNCTION_DEF	ID="66"	EXPRESSION="TIMESTAMPADD(month,	$1,	$0)"/>

				<!--CurrentTime-->

				<FUNCTION_DEF	ID="67"	EXPRESSION="CURRENT_TIME"/>

				<!--DayofWeek-->

				<FUNCTION_DEF	ID="68"	EXPRESSION="DAYOFWEEK($0)"/>

				<!--Monthsbetween-->

				<FUNCTION_DEF	ID="69"	EXPRESSION="TIMESTAMPDIFF(month,	$0,	$1)"/>

				<!--Week-->

				<FUNCTION_DEF	ID="70"	EXPRESSION="WEEK($0)"/>

				<!--NulltoEmpty-->

				<FUNCTION_DEF	ID="71"	EXPRESSION="COALESCE($0,	'')"/>

				<!--StrBeginsWith-->

				<FUNCTION_DEF	ID="72"

																		EXPRESSION="case	when	SUBSTRING($0	from	1	for	CHAR_LENGTH('$1')	)	=$1	then	1	else	0	end"/>

				<!--Concat-->

				<FUNCTION_DEF	ID="73"	EXPRESSION="concat	($0	,	$1)"/>

				<!--StrEndsWith-->

				<FUNCTION_DEF	ID="74"

																		EXPRESSION="case	when	SUBSTRING($0	from		(CHAR_LENGTH($0)-CHAR_LENGTH($1)+1)	for	CHAR_LENGTH(

$1)	)	=$1	then	1	else	0	end"/>

				<!--LTrim-->

				<FUNCTION_DEF	ID="76"	EXPRESSION="TRIM(	LEADING	'	'		FROM	$0)"/>

				<!--Position-->

				<FUNCTION_DEF	ID="77"	EXPRESSION="POSITION($0	IN	$1)"/>

				<!--StrReplace-->

				<FUNCTION_DEF	ID="78"	EXPRESSION="REPLACE($0,	$1,	$2)"/>

				<!--RightStr-->

				<FUNCTION_DEF	ID="79"

1080

如何基于数据源扩展	SDK，开发新的数据源连接器

																		EXPRESSION="SUBSTRING($0	FROM	(char_length($0)	-$1	+1)	FOR	$1)"/>

				<!--RTrim-->

				<FUNCTION_DEF	ID="80"	EXPRESSION="TRIM(TRAILING	'	'		FROM	$0)"/>

				<!--Round2-->

				<FUNCTION_DEF	ID="81"	EXPRESSION="ROUND($0,	$1)"/>

				<!--CORRELATION	-->

				<FUNCTION_DEF	ID="82"	EXPRESSION="CORR($0,	$1)"/>

				<!--Random	number-->

				<FUNCTION_DEF	ID="83"	EXPRESSION="RAND()"/>

				<!--CAST	VARCHAR-->

				<FUNCTION_DEF	ID="101"	EXPRESSION="CAST($0	AS	VARCHAR)"/>

				<FUNCTION_DEF	ID="201"	EXPRESSION="CAST($0	AS	TIMESTAMP)"/>

				<FUNCTION_DEF	ID="202"	EXPRESSION="CAST($0	AS	DOUBLE)"/>

				<TYPE_DEF	ID="Any"	EXPRESSION="ANY"/>

				<TYPE_DEF	ID="Integer"	EXPRESSION="INTEGER"/>

				<TYPE_DEF	ID="Int"	EXPRESSION="INT"/>

				<TYPE_DEF	ID="BigInt"	EXPRESSION="BIGINT"/>

				<TYPE_DEF	ID="TinyInt"	EXPRESSION="TINYINT"/>

				<TYPE_DEF	ID="SmallInt"	EXPRESSION="SMALLINT"/>

				<TYPE_DEF	ID="Short"	EXPRESSION="SHORT"/>

				<TYPE_DEF	ID="Long"	EXPRESSION="LONG"/>

				<TYPE_DEF	ID="Numeric"	EXPRESSION="NUMERIC($p,	$s)"/>

				<TYPE_DEF	ID="Decimal"	EXPRESSION="DECIMAL($p,	$s)"/>

				<TYPE_DEF	ID="Real"	EXPRESSION="REAL"/>

				<TYPE_DEF	ID="Double"	EXPRESSION="DOUBLE"/>

				<TYPE_DEF	ID="Float"	EXPRESSION="FLOAT"/>

				<TYPE_DEF	ID="Char"	EXPRESSION="CHAR($p)"/>

				<TYPE_DEF	ID="VarChar"	EXPRESSION="VARCHAR($p)"/>

				<TYPE_DEF	ID="String"	EXPRESSION="STRING"/>

				<TYPE_DEF	ID="Binary"	EXPRESSION="BINARY"/>

				<TYPE_DEF	ID="Byte"	EXPRESSION="BYTE"/>

				<TYPE_DEF	ID="Boolean"	EXPRESSION="BOOLEAN"/>

				<TYPE_DEF	ID="Date"	EXPRESSION="DATE"/>

				<TYPE_DEF	ID="Time"	EXPRESSION="TIME"/>

				<TYPE_DEF	ID="DateTime"	EXPRESSION="DATETIME"/>

				<TYPE_DEF	ID="TimeStamp"	EXPRESSION="TIMESTAMP"/>

</DATASOURCE_DEF>

配置文件结构：

根节点：

<DATASOURCE_DEF	NAME="mysql"	ID="mysql"	DIALECT="mysql"/>

NAME	可以是对应	dialect	的方言名称。
ID	的值通常和配置文件的名字相同。
DIALECT	的值的定义主要是为了区分不同数据库对于标识符的引用（举个例子	Mysql	使用	``，Microsoft	sql	server
使用	[]）。

由于转换底层使用	Apache	Calcite，因此定义下列转换关系列表：

Kyligence	里定义的方言

Apache	Calcite	里定义的方言

default

calcite

greenplum

SqlDialect.CALCITE

SqlDialect.CALCITE

SqlDialect.DatabaseProduct.POSTGRESQL

1081

如何基于数据源扩展	SDK，开发新的数据源连接器

greenplum

postgresql

mysql

mssql

oracle

vertica

redshift

hive

h2

unkown

属性节点：

SqlDialect.DatabaseProduct.POSTGRESQL

SqlDialect.DatabaseProduct.POSTGRESQL

SqlDialect.DatabaseProduct.MYSQL

SqlDialect.DatabaseProduct.MSSQL

SqlDialect.DatabaseProduct.ORACLE

SqlDialect.DatabaseProduct.VERTICA

SqlDialect.DatabaseProduct.REDSHIFT

SqlDialect.DatabaseProduct.HIVE

SqlDialect.DatabaseProduct.H2

SqlDialect.DUMMY

<PROPERTY	NAME="sql.default-converted-enabled"	VALUE="true"/>

定义方言的属性，默认值参考上述	 	default.xml		文件模版可参考下列参数列表：

属性（非必选）

描述

sql.default-converted-enabled

是否需要转换

sql.allow-no-offset

是否允许没有	offset	字句

sql.allow-fetch-no-rows

是否允许	fetch	0	rows

sql.allow-no-orderby-with-fetch

fetch	是否必须跟	order	by

sql.keyword-default-escape

是否是关键字

sql.keyword-default-uppercase

是否需要转换成大写

sql.paging-type

sql.case-sensitive

分页类型比如	LIMIT_OFFSET，FETCH_NEXT，ROWNUM

是否大小写敏感

metadata.enable-cache

是否开启缓存（针对开启大小写敏感）

sql.enable-quote-all-identifiers

是否开启	quote

transaction.isolation-level

事务隔离级别（针对	Sqoop）

方法节点：	开发者可以根据数据源方言定义方法的实现。

比如，我们想要实现	Greenplum	作为数据源，但是	Greenplum	不支持	 	TIMESTAMPDIFF		方法，那我们就可以在
	greenplum.xml		里面定义	：

<FUNCTION_DEF	ID="64"	EXPRESSION="(CAST($1	AS	DATE)	-	CAST($0	AS	DATE))"/>

对比在	 	default.xml		定义：

<FUNCTION_DEF	ID="64"	EXPRESSION="TIMESTAMPDIFF(day,	$0,	$1)"/>

SDK	可以把	default	里定义相同	function	id	方法转换成目标方言里的定义。

1082

如何基于数据源扩展	SDK，开发新的数据源连接器

类型节点：	开发者可以根据数据源方言定义数据类型。	还是拿	Greenplum	作为例子，Greenplum	支持	BIGINT	而不是
LONG，那我们可以在	 	greenplum.xml		定义：

<TYPE_DEF	ID="Long"	EXPRESSION="BIGINT"/>

对比在	 	default.xml		定义：

<TYPE_DEF	ID="Long"	EXPRESSION="LONG"/>

SDK	可以把	default	里定义相同	type	id	方法转换成目标方言里的定义。

实现扩展自定义数据源的	Java	类

扩展自定义数据源的扩展点需要继承	DefaultSourceConnector	，通过重写其中的方法进行对应数据源的适配。

下面会通过样例模版介绍如何实现这个类。

1.	 DefaultSourceConnector	类的自定义实现模板

构造函数

public	class	DemoSourceConnector	extends	DefaultSourceConnector	{

				DemoSourceConnector(AdaptorConfig	config)	throws	Exception	{

								super(config);

				}

}

获取元数据

listDatabases(),	listTables(),	listColumns()	用于获取数据源的schema信息。

							@Override

							public	List<String>	listDatabases()	throws	SQLException	{

											List<String>	list	=	Lists.newArrayList();

											list.add("default");

											list.add("ssb");

											return	list;

							}

							@Override

							public	List<String>	listTables(String	schema)	throws	SQLException	{

											List<String>	list	=	Lists.newArrayList();

											if	("ssb".equals(schema))	{

															list.add("part");

															list.add("lineorder");

										}

											return	list;

							}

							@Override

							public	List<String>	listColumns(String	database,	String	table)	throws	SQLException	{

											List<String>	list	=	Lists.newArrayList();

											if	("ssb".equals(database)	&&	"part".equals(table))	{

															list.add("column1");

															list.add("column2");

															list.add("column3");

								}

1083

如何基于数据源扩展	SDK，开发新的数据源连接器

											return	list;

							}

DefaultSourceConnector	提供的其他接口，开发者也可以自定义实现。

/**

	*	To	convert	a	column	type	from	JDBC	source	to	the	JDBC	type	supported	by	Kylin.

	*	More	about	JDBC	type,	see	the	definition	in	<C>java.sql.Types</C>

	*	For	example,	Presto	return	<C>Types.LONGNVARCHAR</C>	for	"VARCHAR"	type,	we	need	to	convert	to	<C>Types.VARC

HAR</C>	type.

	*	@param	type	The	column	type	name	from	JDBC	source.

	*	@param	typeId	The	column	type	id	from	JDBC	source.

	*	@return	The	column	type	if	supported	by	Calcite(Kylin).

	*/

public	abstract	int	toKylinTypeId(String	type,	int	typeId);

/**

	*	To	convert	a	column	type	name	from	JDBC	source	to	the	JDBC	Type	supported	by	Kylin.

	*	@param	sourceTypeId	Column	type	id	from	Source

	*	@return	Column	type	name	supported	by	kylin.

	*/

public	abstract	String	toKylinTypeName(int	sourceTypeId);

/**

	*	To	converted	a	column	type	name	which	is	defined	in	Kylin	metadata,	to	a	column	type	name	which	is	supported

	in	JDBC	source.

	*	For	example,	Kylin	defines	a	integer	type	as	"INTEGER"	in	table	metadata,	but	JDBC	source	defines	it	as	"INT

".	So	we	need	to	convert	from	"INTEGER"	to	"INT"	here.

	*	@param	kylinTypeName	A	column	type	name	which	is	defined	in	Kylin.

	*	@return	A	column	type	name	which	is	supported	in	JDBC	source.

	*/

public	abstract	String	toSourceTypeName(String	kylinTypeName);

/**

	*	To	fix	the	sql	to	be	smoothly	executed	in	JDBC	source,	because	the	SQL	dialect	may	be	different	between	Kyli

n	and	JDBC	source.

	*	The	framework	will	convert	the	sql	according	to	dialect	of	jdbc	source	firstly	(if	skipDefaultSqlConvert()	r

eturns	<C>FALSE</C>),	and	then

	*	call	this	method.

	*	@param	sql	The	SQL	statement	to	be	fixed.

	*	@return	The	fixed	SQL	statement.

	*/

public	abstract	String	fixSql(String	sql);

/**

	*	fix	case	sensitive	for	identifier

	*	@param	identifier

	*	@return

	*/

public	abstract	String	fixIdentifierCaseSensitve(String	identifier);

/**

	*	To	list	all	the	available	database	names	from	JDBC	source.

	*	Some	JDBC	source	will	expose	SYSTEM	databases	from	the	default	implementation,	then	developers	can	overwrite

	this	method	and	do	some	filtering.

	*	Besides,	some	RDBMS	uses	Catalog	as	the	definition	of	database,	you	can	find	details	in	<C>MysqlAdaptor</C>

	*	@return	The	list	of	all	the	available	database	names.

	*	@throws	SQLException	If	metadata	fetch	failed.

	*/

public	abstract	List<String>	listDatabases()	throws	SQLException;

/**

	*	To	list	all	the	available	tables	inside	a	database	from	JDBC	source.

	*	Developers	can	overwrite	this	method	to	do	some	filtering	work.

	*	@param	database	The	given	database.

	*	@return	The	list	of	all	the	available	tables.

	*	@throws	SQLException	If	metadata	fetch	failed.

	*/

public	abstract	List<String>	listTables(String	database)	throws	SQLException;

/**

	*	To	list	all	the	available	columns	inside	a	table	in	database	from	JDBC	source.

	*	Developers	can	overwrite	this	method	to	do	some	filtering	work.

	*	@param	database	The	given	database.

1084

如何基于数据源扩展	SDK，开发新的数据源连接器

	*	@param	tableName	The	given	table	name

	*	@return	The	list	of	all	the	available	columns	of	a	table.

	*	@throws	SQLException	If	metadata	fetch	failed.

	*/

public	abstract	List<String>	listColumns(String	database,	String	tableName)	throws	SQLException;

/**

	*	To	get	the	metadata	in	form	of	<C>javax.sql.rowset.CachedRowSet</C>	for	a	table	inside	a	database.

	*	@param	database	The	given	database	name

	*	@param	table	The	given	table	name

	*	@return	The	metadata	of	the	given	table	in	form	of	<C>javax.sql.rowset.CachedRowSet</C>

	*	@throws	SQLException	If	metadata	fetch	failed.

	*/

public	abstract	CachedRowSet	getTable(String	database,	String	table)	throws	SQLException;

/**

	*	To	get	all	columns	metadata	in	form	of	<C>javax.sql.rowset.CachedRowSet</C>	for	a	table	inside	a	database.

	*	@param	database	The	given	database	name

	*	@param	table	The	given	table	name

	*	@return	The	metadata	of	all	columns	metadata	in	form	of	<C>javax.sql.rowset.CachedRowSet</C>

	*	@throws	SQLException	If	metadata	fetch	failed.

	*/

public	abstract	CachedRowSet	getTableColumns(String	database,	String	table)	throws	SQLException;

/**

	*	To	build	a	set	of	sql	statements	to	create	a	schema	in	JDBC	source.

	*	@param	schemaName	The	name	of	schema.


	*/


/**





	*/


/**





	*/