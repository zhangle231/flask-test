# 中文问题
字体选择：pacman -S wqy-zenhei

# 解决zsh下字体问题
安装 Powerline Fonts 
git clone https://github.com/powerline/fonts.git --depth=1
./install.sh
修改dwm配置文件
static const char *termcmd[]  = { "st", "-f", "Noto Mono for Powerline:size=14"};

# 解决触控板问题
sudo modprobe -r psmouse
sudo modprobe psmouse proto=imps 

# 看图工具
gpicview 需要alt+p打开

# alacritty Error: GLSL 3.30 is not supported
LIBGL_ALWAYS_SOFTWARE=1 alacritty (https://github.com/alacritty/alacritty/issues/3624)

