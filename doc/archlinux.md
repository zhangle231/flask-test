#中文问题
字体选择：pacman -S wqy-zenhei

#解决zsh下字体问题
安装 Powerline Fonts 
git clone https://github.com/powerline/fonts.git --depth=1
./install.sh
修改dwm配置文件
static const char *termcmd[]  = { "st", "-f", "Noto Mono for Powerline:size=14"};
