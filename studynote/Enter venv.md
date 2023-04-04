在powershell中创建虚拟环境

~~~powershell
python3 -m venv name

~~~

要进入虚拟环境，您需要使用命令提示符或PowerShell打开虚拟环境所在的目录，并激活虚拟环境。以下是进入虚拟环境的步骤：

1. 打开命令提示符或PowerShell。

2. 使用`cd`命令进入虚拟环境所在的目录。

   例如，如果您的虚拟环境在`C:\path\to\project\venv`目录中，则可以使用以下命令进入该目录：

   ```powershell
   cd C:\path\to\project\venv
   ```

3. 激活虚拟环境。

   在Windows中，您可以使用以下命令激活虚拟环境：

   ```
   Scripts\activate
   ```

   在==PowerShell==中，使用以下命令激活虚拟环境：

   ```powershell
   .\Scripts\Activate.ps1
   ```

4. 现在您已经进入了虚拟环境，并且可以在该环境中运行Python脚本、安装软件包等。

请注意，当您进入虚拟环境时，提示符通常会显示虚拟环境的名称或路径，以指示您当前所在的虚拟环境。例如，在Windows中，提示符可能会显示为：

```powershell
(venv) C:\path\to\project\venv>
```

在提示符中显示了`(venv)`，表示您已经激活了名为`venv`的虚拟环境。

在PowerShell中，使用以下命令：

```powershell
deactivate
```

这将停止虚拟环境，并将提示符返回到全局Python环境中。