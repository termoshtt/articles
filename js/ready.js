
$(function(){
    $("span.Tag").bind("click",function(event){tag_select(this.id);});
    $("span#ResetTag").bind("click",function(event){tag_select("reset");});

    $("div#TagAdd input[type='button']")
        .bind("click",function(event){create_tag($("div#TagAdd input[type='text']").val());});
});
