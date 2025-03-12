# 易派ERP系统帮助文档

本文档提供了易派ERP系统（基于Odoo）的安装、配置和使用指南。

## 目录

- [系统简介](#系统简介)
- [安装与启动](#安装与启动)
  - [系统要求](#系统要求)
  - [安装依赖](#安装依赖)
  - [启动服务](#启动服务)
- [基本框架和模块](#基本框架和模块)
  - [核心模块](#核心模块)
  - [附加模块](#附加模块)
- [数据库配置](#数据库配置)
  - [PostgreSQL配置](#postgresql配置)
  - [数据库创建](#数据库创建)
  - [数据库备份与恢复](#数据库备份与恢复)
- [常见问题](#常见问题)
- [总结](#总结)

## 系统简介

易派ERP是基于Odoo开源ERP系统构建的企业资源管理平台。Odoo是一套完整的开源商业应用程序，包括CRM、网站构建器、电子商务、仓库管理、项目管理、会计、人力资源等多个模块。

## 安装与启动

### 系统要求

- Python 3.10或更高版本
- PostgreSQL 12.0或更高版本
- 操作系统：Linux、Windows或macOS
- 其他依赖项（详见requirements.txt文件）

### 安装依赖

1. 克隆代码库：

```bash
git clone [仓库地址] yipai-erp
cd yipai-erp
```

2. 创建并激活Python虚拟环境：

```bash
# 创建虚拟环境
python -m venv new_venv_py310

# 激活虚拟环境
# Linux/macOS
source new_venv_py310/bin/activate
# Windows
.\new_venv_py310\Scripts\activate
```

3. 安装Python依赖：

```bash
# 确保pip为最新版本
pip install --upgrade pip

# 安装依赖包
pip install -r requirements.txt
```

3. 解决psycopg2安装问题：

   如果在安装Python依赖时遇到`pg_config executable not found`错误，请按照以下步骤解决：

   - **macOS**：
     ```bash
     # 确保已安装PostgreSQL
     brew install postgresql
     
     # 安装psycopg2-binary替代psycopg2
     pip install psycopg2-binary
     ```

   - **Linux**：
     ```bash
     # Ubuntu/Debian
     sudo apt install libpq-dev python3-dev
     
     # 或者安装psycopg2-binary
     pip install psycopg2-binary
     ```

   - **Windows**：
     - 确保PostgreSQL已安装并将其bin目录添加到PATH环境变量
     - 或者安装预编译的二进制包：
     ```bash
     pip install psycopg2-binary
     ```

### 启动服务

1. 基本启动命令：

```bash
# 方法1：先激活虚拟环境，再启动Odoo
source new_venv_py310/bin/activate
./odoo-bin --config=odoo.conf

# 方法2：直接使用虚拟环境中的Python解释器
./new_venv_py310/bin/python ./odoo-bin --config=odoo.conf
```

2. 使用配置文件启动：

```bash
./odoo-bin --config=odoo.conf
```

配置文件示例(odoo.conf)：

```ini
[options]
; 数据库管理员密码
admin_passwd = yipaiadmin

; 数据库连接设置
db_host = localhost
db_port = 5432
db_user = yipai
db_password = yipaiadmin

; 附加模块路径
addons_path = ./addons

; 其他设置
http_port = 8069
logfile = ./odoo.log
log_level = info
default_productivity_apps = True
```

3. 常用启动参数：

- `--addons-path=addons`：指定附加模块路径
- `-d 数据库名称`：指定数据库
- `--db-filter=^数据库名称$`：数据库过滤器
- `--xmlrpc-port=8069`：指定HTTP服务端口
- `--limit-time-cpu=600`：限制CPU时间
- `--limit-time-real=1200`：限制实际时间
- `--log-level=info`：日志级别（debug, info, warning, error, critical）

4. 开发模式启动：

```bash
# 激活虚拟环境后
./odoo-bin --config=odoo.conf --dev=all

# 或者直接使用虚拟环境中的Python
./new_venv_py310/bin/python ./odoo-bin --config=odoo.conf --dev=all
```

启动后，可通过浏览器访问：http://localhost:8069

## 基本框架和模块

### 核心模块

Odoo的核心模块位于`odoo/addons/base`目录，提供了基础功能：

- 用户认证与权限管理
- 多语言支持
- 报表引擎
- 工作流引擎
- API接口

### 附加模块

附加模块位于`addons/`目录，包括：

- **CRM**：客户关系管理 (`crm/`)
- **销售**：销售管理 (`sale/`)
- **采购**：采购管理 (`purchase/`)
- **库存**：库存管理 (`stock/`)
- **制造**：生产制造 (`mrp/`)
- **会计**：财务会计 (`account/`)
- **人力资源**：员工管理 (`hr/`)
- **项目**：项目管理 (`project/`)
- **网站**：网站构建 (`website/`)
- **电子商务**：在线商店 (`website_sale/`)
- **POS**：销售点 (`point_of_sale/`)

## 数据库配置

### PostgreSQL配置

1. 安装PostgreSQL数据库

   - **macOS**：
     ```bash
     # 安装PostgreSQL
     brew install postgresql@16
     
     # 启动PostgreSQL服务
     brew services start postgresql@16
     ```

   - **Linux (Ubuntu/Debian)**：
     ```bash
     sudo apt update
     sudo apt install postgresql postgresql-contrib
     # 启动PostgreSQL服务
     sudo systemctl start postgresql
     sudo systemctl enable postgresql
     ```

   - **Windows**：
     - 从[PostgreSQL官网](https://www.postgresql.org/download/windows/)下载安装程序
     - 运行安装向导，按照提示完成安装

2. 验证PostgreSQL安装和运行状态：

   ```bash
   # 检查PostgreSQL版本
   psql --version
   
   # 检查PostgreSQL服务状态
   pg_isready
   ```

3. 创建PostgreSQL用户（不建议使用postgres超级用户）：

   连接到PostgreSQL并执行以下SQL命令：

   ```bash
   # 连接到PostgreSQL
   sudo -u postgres psql
   ```

   在psql命令行中执行：

   ```sql
   CREATE USER odoo WITH PASSWORD 'odoo_password';
   ALTER USER odoo WITH CREATEDB;
   \q
   ```

   注意：在macOS上，如果使用Homebrew安装PostgreSQL，可能需要使用以下命令：
   
   ```bash
   # 确保PostgreSQL服务已启动
   brew services start postgresql@16
   
   # 创建odoo用户（注意引号的使用）
   psql postgres -c "CREATE USER odoo WITH PASSWORD 'odoo_password';"
   psql postgres -c "ALTER USER odoo WITH CREATEDB;"
   ```
   
   如果遇到"role 'USER' does not exist"错误，请尝试以下命令：
   
   ```bash
   # 使用当前系统用户连接到PostgreSQL
   psql postgres
   ```
   
   然后在psql命令行中执行：
   
   ```sql
   CREATE USER odoo WITH PASSWORD 'odoo_password';
   ALTER USER odoo WITH CREATEDB;
   \q
   ```

4. 解决psycopg2安装问题：

   如果在安装Python依赖时遇到`pg_config executable not found`错误，请按照以下步骤解决：

   - **macOS**：
     ```bash
     # 确保已安装PostgreSQL
     brew install postgresql@16
     
     # 安装psycopg2-binary替代psycopg2
     pip install psycopg2-binary
     ```

   - **Linux**：
     ```bash
     # Ubuntu/Debian
     sudo apt install libpq-dev python3-dev
     
     # 或者安装psycopg2-binary
     pip install psycopg2-binary
     ```

   - **Windows**：
     - 确保PostgreSQL已安装并将其bin目录添加到PATH环境变量
     - 或者安装预编译的二进制包：
     ```bash
     pip install psycopg2-binary
     ```

### 数据库配置文件

在项目根目录下已创建配置文件`odoo.conf`，包含以下内容：

```
[options]
; 数据库管理员密码
admin_passwd = admin

; 数据库连接设置
db_host = localhost
db_port = 5432
db_user = odoo
db_password = odoo_password

; 附加模块路径
addons_path = ./addons

; 其他设置
http_port = 8069
logfile = ./odoo.log
log_level = info
default_productivity_apps = True
```

您可以根据实际情况修改此配置文件，特别是：

- `admin_passwd`：用于管理数据库的主密码，请设置为强密码
- `db_host`：PostgreSQL服务器地址，本地安装通常为localhost
- `db_port`：PostgreSQL服务器端口，默认为5432
- `db_user`：PostgreSQL用户名，建议使用专门为Odoo创建的用户
- `db_password`：PostgreSQL用户密码

### 数据库创建

1. 通过Web界面创建：
   - 启动Odoo服务：`./odoo-bin --config=odoo.conf`
   - 访问 http://localhost:8069/web/database/manager
   - 填写主密码（在配置文件中的admin_passwd）
   - 填写数据库名称和其他信息
   - 点击"创建数据库"

2. 通过命令行创建：

```bash
./odoo-bin -d 数据库名称 -i base --stop-after-init
```

3. 验证数据库创建：

```bash
psql -l  # 列出所有数据库
```

### 数据库备份与恢复

1. 备份数据库：

   - 通过Web界面：
     - 访问 http://localhost:8069/web/database/manager
     - 选择"备份"选项
     - 选择要备份的数据库
     - 输入主密码
     - 点击"备份"按钮

   - 通过命令行：

   ```bash
   ./odoo-bin -d 数据库名称 --backup --backup-format=zip
   ```

   - 使用PostgreSQL工具：

   ```bash
   pg_dump -U odoo -h localhost -p 5432 数据库名称 > backup_file.sql
   ```

2. 恢复数据库：

   - 通过Web界面：
     - 访问 http://localhost:8069/web/database/manager
     - 选择"恢复"选项
     - 选择备份文件
     - 输入新数据库名称和主密码
     - 点击"恢复"按钮

   - 通过命令行：

   ```bash
   ./odoo-bin -d 新数据库名称 -r 用户名 --restore-file=备份文件路径
   ```

   - 使用PostgreSQL工具：

   ```bash
   # 先创建空数据库
   createdb -U odoo -h localhost -p 5432 新数据库名称
   # 恢复数据
   psql -U odoo -h localhost -p 5432 新数据库名称 < backup_file.sql
   ```

## 常见问题

1. **无法连接数据库**
   - 检查PostgreSQL服务是否运行：`brew services list`（macOS）或`systemctl status postgresql`（Linux）
   - 验证数据库连接参数是否正确：检查odoo.conf中的db_host, db_port, db_user, db_password
   - 确认用户权限是否足够：PostgreSQL用户需要CREATEDB权限
   - 检查防火墙设置是否允许数据库连接
   - 尝试手动连接数据库：`psql -U odoo -h localhost -p 5432 postgres`
   - 如果遇到 `FATAL: role "odoo" does not exist` 错误：
     ```bash
     # macOS用户
     psql postgres -c "CREATE USER odoo WITH PASSWORD 'odoo_password';"
     psql postgres -c "ALTER USER odoo WITH CREATEDB;"
     
     # 如果上述命令失败，尝试直接登录PostgreSQL然后创建用户：
     psql postgres
     # 然后在psql命令行中执行：
     CREATE USER odoo WITH PASSWORD 'odoo_password';
     ALTER USER odoo WITH CREATEDB;
     \q
     ```

2. **模块安装失败**
   - 检查依赖模块是否已安装
   - 查看日志文件获取详细错误信息：`tail -f ./odoo.log`
   - 确认Python依赖是否满足：`pip install -r requirements.txt`
   - 尝试使用`--log-level=debug`参数启动以获取更详细的错误信息
   - 检查数据库用户是否有足够权限

3. **系统性能问题**
   - 调整PostgreSQL配置：编辑postgresql.conf文件
     ```
     shared_buffers = 256MB  # 建议为系统内存的1/4
     work_mem = 4MB          # 复杂查询可适当增加
     maintenance_work_mem = 64MB
     effective_cache_size = 768MB  # 建议为系统内存的1/2
     ```
   - 增加服务器资源
   - 优化查询和索引
   - 考虑使用缓存系统如Redis
   - 定期清理数据库日志和临时文件：`VACUUM FULL ANALYZE;`

4. **更新系统**
   - 备份数据库
   - 更新代码库：`git pull`
   - 重启服务并更新模块：
   ```bash
   ./odoo-bin -d 数据库名称 -u all
   ```
   - 如果更新失败，可尝试以安全模式启动：
   ```bash
   ./odoo-bin -d 数据库名称 --update=all --stop-after-init
   ```

5. **Python依赖问题**
   - 检查Python版本是否符合要求：`python3 --version`
   - 确保pip已安装并更新到最新版本：`pip install --upgrade pip`
   - 如果安装依赖时出现权限问题，建议使用虚拟环境：
     ```bash
     # 安装virtualenv
     pip install virtualenv
     
     # 创建虚拟环境
     python3 -m venv venv
     
     # 激活虚拟环境
     # macOS/Linux
     source venv/bin/activate
     # Windows
     .\venv\Scripts\activate
     ```
   - 安装项目依赖：
     ```bash
     pip install -r requirements.txt
     ```
   - 如果某些包安装失败，可以尝试单独安装：
     ```bash
     # 例如安装特定版本的包
     pip install package-name==version
     
     # 或者使用--no-deps参数跳过依赖检查
     pip install package-name --no-deps
     ```
   - 定期更新依赖包：
     ```bash
     pip list --outdated
     pip install -U package-name
     ```