## :e打开文件
## :new 打开新buffer
## :ls 列出所有buffer
## :vimgre /0$/ example.txt
## cwim
## Ctrl-W w
## :vsp

## :bn :bp

## :b2 :buffers

## ctrl-o ctrl-i history jumps

## :split :vsplit :sfind :sb :vertical :leftabove :right

```
vertical sb 3
Create a vertical split and show buffer number 3 in the window to the left.
:vertical rightbelow sfind file.txt
Create a vertical split and read file.txt into the buffer in the right window.
:rightbelow sfind file.txt
Create a horizontal split and read file.txt into the buffer in the bottom window.

managing buffers

:ls	List the current buffers (including their numbers).
:b <number>	Display the buffer with the given number.
:b <partial>	Display the first buffer matching the partial name (or press Tab for name completion).
:bd	Delete the current buffer; will fail if unsaved (nothing is deleted).
:bd!	Delete the current buffer; will discard any changes (changes are lost).

<C-^> ctrl + shift + ^

```


