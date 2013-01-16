function zaw-src-bibtex () {
    raw_lines=$(${BIBPYSCRIPT})
    cand_lines=$(echo ${raw_lines} |sed 's/^\([^, ]*\)[, ]*\(.*\)$/\1/')
    desc_lines=$(echo ${raw_lines} |sed 's/^\([^, ]*\)[, ]*\(.*\)$/\2/')
    : ${(A)candidates::=${(f)"$(echo ${cand_lines})"}}
    : ${(A)cand_descriptions::=${(f)"$(echo ${desc_lines})"}}
    actions=(zaw-open-pdf zaw-echo-bibtexkey )
    act_descriptions=("open pdf" "echo bibtexkey")
}


function zaw-open-pdf () {
    local pdfviewer
    case $OSTYPE in
        *darwin*)
            pdfviewer="open"
            ;;
        *)
            # pdfviewer="evince"
            pdfviewer="acroread"
            ;;
    esac
    BUFFER="${pdfviewer} ${BIBPDFDIR%/}/$1.pdf 2> /dev/null"
    zle accept-line
}


function zaw-echo-bibtexkey () {
    BUFFER="echo $1"
    zle accept-line
}

zaw-register-src -n bibtex zaw-src-bibtex
