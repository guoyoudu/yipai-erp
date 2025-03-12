# 易派ERP系统启动指南（更新版）

本文档提供了启动易派ERP系统所需的完整命令序列，已更新为使用新的虚拟环境`new_venv_py310`。请按照以下步骤依次执行。

## 1. 启动PostgreSQL数据库服务

```bash
# 如果使用Homebrew安装的PostgreSQL
brew services start postgresql@16

# 验证PostgreSQL服务状态
pg_isready
```

## 2. 确保数据库用户配置正确

如果是首次设置，需要创建数据库用户：

```bash
# 创建yipai用户（如果尚未创建）
psql postgres -c "CREATE USER yipai WITH PASSWORD 'yipaiadmin';"
psql postgres -c "ALTER USER yipai WITH CREATEDB;"
```

## 3. 启动Odoo服务

### 使用新的虚拟环境

由于原来的虚拟环境`venv_py310`存在问题，我们现在使用新创建的`new_venv_py310`环境来启动Odoo服务：

```bash
# 方法1：先激活虚拟环境，再启动Odoo
source new_venv_py310/bin/activate
./odoo-bin --config=odoo.conf
```

或者直接使用虚拟环境中的Python解释器：

```bash
# 方法2：直接使用虚拟环境中的Python解释器
./new_venv_py310/bin/python ./odoo-bin --config=odoo.conf
```

启动后，可以通过浏览器访问：http://localhost:8069

## 注意事项

1. 确保PostgreSQL服务正在运行
2. 确保odoo.conf配置文件中的数据库连接信息正确
3. 如果遇到端口占用问题，可以在odoo.conf中修改http_port参数
4. 建议在启动服务前先检查日志文件（odoo.log）是否有异常
5. **重要**：不要使用旧的启动命令（`/opt/homebrew/opt/python@3.10/bin/python3.10 ./odoo-bin --config=odoo.conf`），因为它不会使用我们安装了xlsxwriter模块的虚拟环境

## 常见问题解决

1. 如果提示数据库连接错误，检查PostgreSQL服务是否正常运行
2. 如果提示端口被占用，可以使用以下命令查看端口占用情况：
   ```bash
   lsof -i :8069
   ```
3. 如果需要停止服务，可以使用Ctrl+C或者关闭终端窗口
4. 如果遇到模块导入错误（如xlsxwriter），确保使用了正确的虚拟环境启动Odoo

## 开发模式启动

如果需要在开发模式下启动系统，使用以下命令：

```bash
# 激活虚拟环境后
./odoo-bin --config=odoo.conf --dev=all

# 或者直接使用虚拟环境中的Python
./new_venv_py310/bin/python ./odoo-bin --config=odoo.conf --dev=all
```

## xlsxwriter模块

我们已经在`new_venv_py310`虚拟环境中安装了xlsxwriter模块（版本3.2.2）。只要使用上述启动方法，Odoo就能正确使用该模块。如果需要在其他Python脚本中使用xlsxwriter，请参考`xlsxwriter_usage_guide.md`文件中的说明。