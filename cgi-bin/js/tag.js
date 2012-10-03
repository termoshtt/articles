
/* globals */
var g_tags = new Array();

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

    var tag_selected = false
    for(tag in g_tags){
        if(g_tags[tag]){
            tag_selected = true;
        }
    }
    if(!tag_selected){
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

function _enable_tag(tag){
    g_tags[tag] = true;
    $("#TagSelector ul li span:contains("+tag+")").css("color","red");
}
function _disable_tag(tag){
    g_tags[tag] = false;
    $("#TagSelector ul li span:contains("+tag+")").css("color","black");
}
