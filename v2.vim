let SessionLoad = 1
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
cd ~/Learn/Projects/pygames/tetris
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +1 README.md
badd +16 tetrimino.py
badd +39 ~/.config/nvim/init.vim
badd +17 ~/.config/nvim/compiler/python.vim
badd +8 tests.py
badd +1328 ~/.pyenv/versions/c4/envs/neovim/lib/python3.8/site-packages/jedi/third_party/typeshed/stdlib/2and3/builtins.pyi
argglobal
%argdel
$argadd README.md
edit tetrimino.py
set splitbelow splitright
set nosplitbelow
set nosplitright
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
argglobal
setlocal fdm=expr
setlocal fde=coiledsnake#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
23
normal! zo
29
normal! zo
37
normal! zo
41
normal! zo
45
normal! zo
49
normal! zo
52
normal! zo
62
normal! zo
87
normal! zo
95
normal! zo
103
normal! zo
117
normal! zo
127
normal! zo
let s:l = 134 - ((30 * winheight(0) + 12) / 25)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
134
normal! 010|
tabnext 1
if exists('s:wipebuf') && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 winminheight=1 winminwidth=1 shortmess=filnxtToOFIc
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
