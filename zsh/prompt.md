Neal Parikh

















Customizing your shell prompt

Shell prompts are extremely customizable. You can customize them in two ways: (1) by using command characters that print out special things and (2) by using colors. Also, customizing the prompt is different in different shells; I'm going to cover tcsh and zsh here. bash is the other popular shell, but I think it sucks, and I never use it, so I'm not going to waste any time on it.

tcsh
zsh
tcsh

I'll start with tcsh, since it's the default BSD and Mac OS X shell. Here's a very simple prompt:

hostname%

That prompt is created with the following command:

setenv PROMPT '%m%# '

The %m is called a formatting sequence, and it is expanded to the hostname of your computer when tcsh outputs your prompt. Similarly, %# equals '>' (or the first character of the promptchars shell variable) if you're a normal user, or '#' (or the second character of promptchars) if you're root. Any letter with a % before it will be treated as a formatting sequence, so if you want to print a % sign, use %%. (Quick side note: you want the extra space at the end, or else the input will be squashed up against the prompt, and it's ugly and hard to read.) A popular prompt is the following:

Formatted: 
[user@hostname:/current/path]% 

Code 
[%n@%m:%c]%#

%n is the username and %c is the current path. Instead of going through millions of examples illustrating all the different kinds of prompts you can have, I'm just going to include the complete list of formatting sequences from the tcsh(1) manpage:

%/  The current working directory.
%~  The  current working directory, but with one's
   home directory represented by  `~'  and  other
   users' home directories represented by `~user'
   as per Filename substitution.  `~user' substi-
   tution  happens  only if the shell has already
   used `~user' in a pathname in the current ses-
   sion.
%c[[0]n], %.[[0]n]
   The  trailing component of the current working
   directory, or n trailing components if a digit
   n  is given.  If n begins with `0', the number
   of skipped  components  precede  the  trailing
   component(s)  in  the format `/<skipped>trail-
   ing'.  If the ellipsis shell variable is  set,
   skipped   components  are  represented  by  an
   ellipsis so the whole  becomes  `...trailing'.
   `~' substitution is done as in `%~' above, but
   the `~' component  is  ignored  when  counting
   trailing components.
%C  Like %c, but without `~' substitution.
%h, %!, !
   The current history event number.
%M  The full hostname (e.g. jaguar.apple.com).
%m  The hostname up to the first `.' (e.g. jaguar).
%S (%s)
   Start (stop) standout (reverse) mode.
%B (%b)
   Start (stop) boldfacing mode.
%U (%u)
   Start (stop) underline mode.
%t, %@
   The time of day in 12-hour AM/PM format.
%T  Like  `%t', but in 24-hour format (but see the
   ampm shell variable).
%p  The `precise' time of  day  in  12-hour  AM/PM
   format, with seconds.
%P  Like  `%p', but in 24-hour format (but see the
   ampm shell variable).
\c  c is parsed as in bindkey.
^c  c is parsed as in bindkey.
%%  A single `%'.
%n  The user name.
%d  The weekday in `Day' format.
%D  The day in `dd' format.
%w  The month in `Mon' format.
%W  The month in `mm' format.
%y  The year in `yy' format.
%Y  The year in `yyyy' format.
%l  The shell's tty.
%L  Clears from the end of the prompt  to  end  of
   the display or the end of the line.
%$  Expands the shell or environment variable name
   immediately after the `$'.
%#  `>' (or the first character of the promptchars
   shell  variable) for normal users, `#' (or the
   second character of promptchars) for the supe-
   ruser.
%{string%}
   Includes  string as a literal escape sequence.
   It should be  used  only  to  change  terminal
   attributes  and  should  not  move  the cursor
   location.  This cannot be the last sequence in
   prompt.
%?  The  return  code of the command executed just
   before the prompt.
%R  In prompt2, the  status  of  the  parser.   In
   prompt3,  the  corrected  string.  In history,
   the history string.
Next, on to color. This directly builds on the previous section by adding color escape sequences to the formatting sequences you can use. The following code colors the hostname red:

%{\033[31m%}%m%{\033[0m%}

The '31' and the %m have been bolded above because those are the only things you change. The 31 is the color code, and the %m is obviously where you put whatever you want to color. The rest of it is the same for every color coding; the beginning starts coloring, and the stuff afterwards stops coloring ('0' switches it back to default text color). You can use the following color codes:

30 - black
31 - red
32 - green
33 - yellow
34 - blue
35 - magenta
36 - cyan
37 - white
Not quite the same as a full Photoshop palette, but you can make a pretty nice prompt with it. Also, you can modify it further by including another control char:

%{\033[1;31m%}%m%{\033[0m%}

In this case, the '1' will make the following color bold. You can use the following modifiers:

0 - normal
1 - bold
2 - normal again
3 - background color
4 - underline the text
5 - blinking
You can also specify both a foreground and a background color. Use the following syntax to get (fairly hideous looking) Christmas colors:

%{\033[2;41;32m%}%m%{\033[0m%}

The '41' is the background color, and the '31' is the foreground color. The background color codes are the same as the foreground color codes, except they're 40-47 instead of 30-37.

Finally, you can also have a right-justified prompt. This is stored in the RPROMPT variable, and formatted in exactly the same way as PROMPT. People often like putting the time (%p) in RPROMPT.

zsh

zsh is customized in an extremely similar way. You still use formatting sequences, although some of them are a little different. The color codes are the same, although the color escape sequence is a little different. Other than that, it's pretty easy to move back and forth between a zsh and a tcsh prompt. The formatting sequences are the following (from zshmisc(1)):

%%     A `%'.

%)     A `)'.

%d
%/     Present  working  directory  ($PWD).  If an integer
	  follows the `%', it specifies a number of  trailing
	  components  of  $PWD  to show; zero means the whole
	  path.  A negative integer specifies leading  compo-
	  nents, i.e. %-1d specifies the first component.

%~     As  %d and %/, but if $PWD has a named directory as
	  its prefix, that part is replaced by a `~' followed
	  by  the  name  of the directory.  If it starts with
	  $HOME, that part is replaced by a `~'.

%h
%!     Current history event number.

%L     The current value of $SHLVL.

%M     The full machine hostname.

%m     The hostname up to the first `.'.  An  integer  may
	  follow  the  `%'  to specify how many components of
	  the hostname are desired.  With a negative integer,
	  trailing components of the hostname are shown.

%S (%s)
	  Start (stop) standout mode.

%U (%u)
	  Start (stop) underline mode.

%B (%b)
	  Start (stop) boldface mode.

%t
%@     Current time of day, in 12-hour, am/pm format.

%T     Current time of day, in 24-hour format.

%*     Current  time  of  day in 24-hour format, with sec-
	  onds.

%n     $USERNAME.

%N     The name of the  script,  sourced  file,  or  shell
	  function that zsh is currently executing, whichever
	  was started most recently.  If there is none,  this
	  is  equivalent to the parameter $0.  An integer may
	  follow the `%' to specify a number of trailing path
	  components  to  show;  zero means the full path.  A
	  negative integer specifies leading components.

%i     The line number currently  being  executed  in  the
	  script,  sourced  file,  or shell function given by
	  %N.  This is most useful for debugging as  part  of
	  $PS4.

%w     The date in day-dd format.

%W     The date in mm/dd/yy format.

%D     The date in yy-mm-dd format.

%D{string}
	  string  is  formatted  using the strftime function.
	  See strftime(3) for more details.  Three additional
	  codes  are  available:   %f  prints  the day of the
	  month, like %e but without any preceding  space  if
	  the  day is a single digit, and %K/%L correspond to
	  %k/%l for the hour of the day (24/12 hour clock) in
	  the same way.

%l     The  line  (tty)  the  user is logged in on without
	  /dev/ prefix.  If name starts with /dev/tty this is
	  stripped.

%y     The  line  (tty)  the  user is logged in on without
	  /dev/ prefix.  It does  not  treat  /dev/tty*  spe-
	  cially.

%?     The  return  code of the last command executed just
	  before the prompt.

%_     The status of the parser, i.e. the shell constructs
	  (like `if' and `for') that have been started on the
	  command line. If given an integer number that  many
	  strings  will  be  printed;  zero or negative or no
	  integer means print as many as there are.  This  is
	  most  useful  in prompts PS2 for continuation lines
	  and PS4 for debugging with the  XTRACE  option;  in
	  the  latter  case  it  will  also work non-interac-
	  tively.

%E     Clears to end of line.

%#     A `#' if the shell is running  with  privileges,  a
	  `%'  if not.  Equivalent to `%(!.#.%%)'.  The defi-
	  nition of `privileged', for these purposes, is that
	  either  the  effective  user  ID  is  zero,  or, if
	  POSIX.1e capabilities are supported, that at  least
	  one capability is raised in either the Effective or
	  Inheritable capability vectors.

%v     The value of the first element of the  psvar  array
	  parameter.  Following the `%' with an integer gives
	  that element of the array.  Negative integers count
	  from the end of the array.

%{...%}
	  Include a string as a literal escape sequence.  The
	  string within the braces should not change the cur-
	  sor position.  Brace pairs can nest.

%(x.true-text.false-text)
	  Specifies a ternary expression.  The character fol-
	  lowing the x is arbitrary; the  same  character  is
	  used  to  separate  the  text for the `true' result
	  from that for the `false' result.   This  separator
	  may  not appear in the true-text, except as part of
	  a %-escape sequence.   A  `)'  may  appear  in  the
	  false-text  as  `%)'.  true-text and false-text may
	  both contain arbitrarily-nested  escape  sequences,
	  including further ternary expressions.

	  The left parenthesis may be preceded or followed by
	  a positive integer n, which defaults  to  zero.   A
	  negative  integer  will  be  multiplied by -1.  The
	  test character x may be any of the following:

	  c
	  .
	  ~      True  if  the  current  path,  with   prefix
			 replacement, has at least n elements.
	  /
	  C      True  if  the  current  absolute path has at
			 least n elements.
	  t      True if the time in minutes is equal to n.
	  T      True if the time in hours is equal to n.
	  d      True if the day of the month is equal to  n.
	  D      True  if  the month is equal to n (January =
			 0).
	  w      True if the day of the week is  equal  to  n
			 (Sunday = 0).
	  ?      True  if the exit status of the last command
			 was n.
	  #      True if the effective  uid  of  the  current
			 process is n.
	  g      True  if  the  effective  gid of the current
			 process is n.
	  l      True if at least n characters  have  already
			 been printed on the current line.
	  L      True if the SHLVL parameter is at least n.
	  S      True if the SECONDS parameter is at least n.
	  v      True if the array psvar has at least n  ele-
			 ments.
	  _      True  if  at  least  n shell constructs were
			 started.
	  !      True if the shell  is  running  with  privi-
			 leges.

%<string<
%>string>
%[xstring]
	  Specifies truncation behaviour for the remainder of
	  the prompt string.  The third, deprecated, form  is
	  equivalent  to  `%xstringx',  i.e.  x may be `<' or
	  `>'.  The numeric argument, which in the third form
	  may appear immediately after the `[', specifies the
	  maximum permitted length  of  the  various  strings
	  that  can  be  displayed in the prompt.  The string
	  will be displayed in place of the truncated portion
	  of  any  string;  note this does not undergo prompt
	  expansion.

	  The forms with `<' truncate  at  the  left  of  the
	  string,  and  the  forms  with  `>' truncate at the
	  right of the string.  For example, if  the  current
	  directory  is  `/home/pike',  the prompt `%8<..<%/'
	  will expand to `..e/pike'.   In  this  string,  the
	  terminating character (`<', `>' or `]'), or in fact
	  any character, may be quoted by  a  preceding  `\';
	  note  when  using print -P, however, that this must
	  be doubled as the string is also subject  to  stan-
	  dard  print  processing,  in  addition to any back-
	  slashes removed by a  double  quoted  string:   the
	  worst case is therefore `print -P "%<\\\\<<..."'.

	  If  the string is longer than the specified trunca-
	  tion length, it will  appear  in  full,  completely
	  replacing the truncated string.

	  The  part of the prompt string to be truncated runs
	  to the end of the string, or to the end of the next
	  enclosing  group  of  the `%(' construct, or to the
	  next truncation encountered at  the  same  grouping
	  level  (i.e.  truncations  inside  a `%(' are sepa-
	  rate), which ever comes first.   In  particular,  a
	  truncation  with  argument  zero (e.g. `%<<') marks
	  the end of the range of the string to be  truncated
	  while  turning  off  truncation  from there on. For
	  example, the prompt '%10<...<%~%<<%# ' will print a
	  truncated  representation of the current directory,
	  followed by a `%' or  `#',  followed  by  a  space.
	  Without  the  `%<<',  those two characters would be
	  included in the string to be truncated.

%c
%.
%C     Trailing component of $PWD.  An integer may  follow
	  the  `%'  to  get  more than one component.  Unless
	  `%C' is used, tilde contraction is performed first.
	  These are deprecated as %c and %C are equivalent to
	  %1~ and %1/, respectively, while explicit  positive
	  integers have the same effect as for the latter two
	  sequences.
As you can likely tell, zsh has some absurdly powerful prompt characters, but reasonably simple prompts are extremely similar to their tcsh counterparts:

tcsh: 
[%n@%m:%c]%# 

zsh: 
[%n@%m:%/]%#

Not such a huge difference. The color sequence is slightly different, so use this kind of formatting:

%{\e[0;31m%}%m%{\e[0m%}

Again, the bold parts are the parts you edit. Also, you can customize RPROMPT in the same way.

That's pretty much it. You can customize your prompt pretty extensively with the above instructions. Comments or suggestions? Let me know!

http://www.nparikh.org/unix/prompt.php#zsh

