
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
        $(".ArticleDiv").show();
    }else{
        $(".ArticleDiv").hide();
        for(tag in g_tags){
            if(g_tags[tag]){
                $(".ArticleDiv:has(.ArticleTag:contains("+tag+"))").show();
            }
        }
    }
}

function search(){
    // $(".ArticleDiv").show();
    show_articles();
    var keys = $("#SearchForm [name=SearchKeyWard]").val().replace(/ +$/g, "").split(/ +/);
    jQuery.expr[':'].insenseContains = function(a, i, m) {
        return jQuery(a).text().toUpperCase().indexOf(m[3].toUpperCase()) >= 0;
    };
    if (!(keys.length == 1 && keys[0] == "")) {
        jQuery.each(keys,function(){
            $(".ArticleDiv:not(:insenseContains("+this+"))").hide()
        });
    }
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
    $("#TagSelector ul li span:contains("+tag+")").css("color","red");
}
function _disable_tag(tag){
    g_tags[tag] = false;
    $("#TagSelector ul li span:contains("+tag+")").css("color","black");
}
