function _send_to_cgi(action,name,key=""){
    $.post("http://localhost:8000/cgi-bin/tag.cgi",
            {
                TagAction: action,
                TagName: name,
                BibTeXKey: key
            });
}
