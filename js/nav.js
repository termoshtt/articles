
/* globals */
var g_tags = new Array();
var g_tag_selected = false;

function check_tag_selected(){
    g_tag_selected = false
    for(tag in g_tags){
        if(g_tags[tag]){
            g_tag_selected = true;
        }
    }
}

function show_articles(){
    if(!g_tag_selected){
        $("div.Article").show();
    }else{
        $("div.Article").hide();
        for(tag in g_tags){
            if(g_tags[tag]){
                $("div.Article:has(span:contains("+tag+"))").show();
            }
        }
    }
}

function search(){
    // $(".ArticleDiv").show();
    show_articles();
    var keys = $("#SearchForm [name=SearchKeyWard]").val().split(/ +/);
    jQuery.expr[':'].insenseContains = function(a, i, m) {
        return jQuery(a).text().toUpperCase().indexOf(m[3].toUpperCase()) >= 0;
    };
    jQuery.each(keys,function(){
        if (this != "") {
            $("div.Article:not(:insenseContains("+this+"))").hide();
        }
    });
}

function tag_select(tag){
    if(tag == "reset"){
        for(tag in g_tags){
            _disable_tag(tag);
        }
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

function create_tag(name){
    _send_to_cgi("CreateTag",name);
    alert("Tag created. Please reload");
}

function delete_tag(name){
    _send_to_cgi("DeleteTag",name);
    alert("Tag deleted. Please reload");
}

function tagging(name,key){
    _send_to_cgi("Tagging",name,key);
    alert("Tagging. Please reload");
}

function untagging(name,key){
    _send_to_cgi("unTagging",name,key);
    alert("unTagging. Please reload");
}
