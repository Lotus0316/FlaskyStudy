#### 关于在powershell中启动flask（与命令行不太一样）
**设置环境变量的方法为**
```Powershell
setx FLASK_APP "app.py"
```
此时会显示`指定的值已得到保存`，这时候只是保存了值，表示已成功设置了`FLASK_APP`环境变量，此时需求重启powershell才能应用环境变量，为此可以在同一窗口中输入
```Powershell
$env:FLASK_APP = "app.py"
```
来强制刷新环境，最后使用
```Powershell
flask run
```
来部署应用，之后会看到
```powershell
 * Serving Flask app 'first_web.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
```
其中最后一行的127.0.0.1是特殊的回路本地IP，然后5000是部署的端口，http是URL协议

顺便提一嘴调试模式，在powershell中是
~~~Powershell
$env:FLASK_ENV = "development" 
~~~
然后会看到
~~~powershell
 * Debugger is active!
 * Debugger PIN: 727-553-530
~~~
 这样就进入了DEBUG模式，能在浏览器中显示交互页面，并可以刷新更改（更改后记得保存文件）