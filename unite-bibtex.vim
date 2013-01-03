
let s:unite_source = {
    \ "name" : "bibtex",
    \}

function! s:unite_source.gather_candidates(args,context)
    let bib_src = unite#util#system(g:unite_bibtex_articles_directory . '/bibtex_source.py')
    let lines = split(bib_src,'\n')
    let key = []
    let desc = []
    for line in lines
        let i = stridx(line,',')
        let k = line[:i-1]
        let d = line[(i+2):]
        call add(key,k)
        call add(desc,d)
    endfor
    return map(key,'{
    \   "word"   : desc[v:key],
    \   "source" : "bibtex",
    \   "kind"   : "word",
    \   "action__text" : v:val,
    \ }')
endfunction

call unite#define_source(s:unite_source)
unlet s:unite_source

