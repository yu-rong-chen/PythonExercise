# vim
<p> insert a line after "o"
<p> search word in normal mode<code>/word</code> 
    <p> hilight search <code>:set hlsearch</code>
    <p> find next word <code>n</code><p> find previous word <code>N</code>
    <p> search the word where cursor located <code>*</code>
    <p> jump to next alphabet "a" in the line <code>f"a"</code>
    <p> jump to previous alphabet "a" in the line <code>F"a"</code>
<p>Visual mode
    <p> undo <code>u</code>; Redo <code>ctrl + r</code>
    <p> make clipboard equal to vim register <code>:set clipboard=unnamed</code>
    <p> copy to register "a" <code>"ay</code> paste from registart "a" <code>"ap</code>
    <p> check all content in register <code>:reg</code> <p> move the cursor line to the middle of the screen <code>zz</code> to the top of the screen <code>zt</code> to the end of the screen <code>zb</code>
    <p> visual Line: <code>V </code> and visual block <code>ctrl +v</code>
    <p> add the same content in the begin of many line <code> ctrl+v and I</code>
    <p> select a word <code>viw</code> and select all content between " <code>vi"</code> another: <code> vaw, vit, vat, v{, v} </code>
    <p> change v with d (delete) or c (change) <code> diw,ciw...</code>

## Others
<p> Swap uppercase and lowercase <code>~</code> in normal mode or visual mode
<p> Repeate the last movement <code> . </code>

## Copy and paste
<p> copy a line <code>yy</code> and paste <code>p</code> directly

## Next Paragraph
<p> Go to head of line <code>0</code> and <code>^</code>
    <p> Go to line 10 <code>10G</code>
<p> Next Paragraph <code>{ or } </code>
<p> Page down <code>ctrl + f</code> Page up <code>ctrl + b </code>
<p> fold some line, select lines and <code>zf</code> unfold lines <code>zb</code> (not working)
    <p> fold a paragraph under normal mode <code>zfip</code> (not working)

## Shortcut Key in VScode
<p>Open file <code>ctrl+shift+o<code> and then <code>ctrl+o<code>
<p>

## set command
<p>:set shiftwidth=2 <code>>></code>
<p>:set clipboard=unnamed 
<p>:set nu(mber) <-> :set nonu
