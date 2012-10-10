
$(function(){
    $("span.Tag").bind("click",function(event){tag_select(this.id);})
    $("span#ResetTag").bind("click",function(event){tag_select("reset");});
});
