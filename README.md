# putty_colors2crt
A useful script to convert putty color scheme to SecureCRT's.

为了方便别人拿去修改，我把啰嗦的容错逻辑都删了，尽可能保持清晰简洁。

脚本生成的东西填到`%appdata%\VanDyke\Config\Global.ini`文件里的
`B:"ANSI Color RGB"=00000040`下面，替换原有的两行就好了。