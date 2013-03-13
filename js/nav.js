
/* globals */
var g_tags = new Array();
var g_tag_selected = false;
var prev_search_str = "";
function check_tag_selected(){
    g_tag_selected = false;
    for(tag in g_tags){
        if(g_tags[tag]){
            g_tag_selected = true;
        }
    }
}

function show_articles(){
    if(!g_tag_selected){
        $("div.Article:hidden").show();
    }else{
        only_show_tagged_articles();
    }
}

function only_show_tagged_articles(){
    if(g_tag_selected){
        $("div.Article:not(:hidden)").hide();
        for(tag in g_tags){
            if(g_tags[tag]){
                $("div.Article:has(span:contains("+tag+"))").show();
            }
        }
    }
}

function search(){
    // $(".ArticleDiv").show();
    var search_str = $("#SearchForm [name=SearchKeyWard]").val();
    var keys = search_str.split(/ +/);
    if (search_str.slice(0, -1) != prev_search_str) {$("div.Article:hidden").show();}
    only_show_tagged_articles();
    for (var i = 0; i < keys.length; i++){
        if (keys[i].length < 3) {
            prev_search_str = search_str;
            return;
        }
    }
    jQuery.expr[':'].insenseContains = function(a, i, m) {
        return jQuery(a).text().toUpperCase().indexOf(m[3].toUpperCase()) >= 0;
    };
    jQuery.each(keys,function(){
        if (this != "") {
            $("div.Article:not(:hidden):not(:insenseContains("+this+"))").hide();
        }
    });
    prev_search_str = search_str;
}

function tag_select(tag){
    if(tag == "reset"){
        for(tag in g_tags){
            _disable_tag(tag);
        }
        $("#SearchForm [name=SearchKeyWard]").val('');
    }else{
        if(tag in g_tags && g_tags[tag]){
            _disable_tag(tag);
        }else{
            _enable_tag(tag);
        }
    }
    check_tag_selected();
    show_articles();
}

function _enable_tag(tag){
    g_tags[tag] = true;
    $("div.Tag>span:contains("+tag+")").css("color","red");
}
function _disable_tag(tag){
    g_tags[tag] = false;
    $("div.Tag>span:contains("+tag+")").css("color","black");
}

function update_html(){
    $.post("http://localhost:8000/cgi-bin/main.cgi",{
        "Action" : "UpdateHTML"
    });
    alert("update HTML. please reload.");
}

function register_bib(bibstr){
    $.post("http://localhost:8000/cgi-bin/main.cgi",{
        "Action" : "RegisterBibStr",
        "BibStr" : bibstr
    });
    alert("register bib info, and update HTML. please reload.");
}

function _send_to_tag_cgi(action,name,key){
    $.post("http://localhost:8000/cgi-bin/tag.cgi",
            {
                "TagAction" : action,
                "TagName" : name,
                "BibTeXKey" : key
            });
}

function create_tag(name){
    _send_to_tag_cgi("CreateTag",name);
    alert("Tag created. Please reload");
}

function delete_tag(name){
    _send_to_tag_cgi("DeleteTag",name);
    alert("Tag deleted. Please reload");
}

function tagging(name,key){
    _send_to_tag_cgi("Tagging",name,key);
    alert("Tagging. Please reload");
}

function untagging(name,key){
    _send_to_tag_cgi("unTagging",name,key);
    alert("unTagging. Please reload");
}

