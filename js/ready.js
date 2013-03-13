
$(function(){
    /* tag manipulation */
    $("div.Tag>span")
        .bind("click", function(event){
                tag_select(this.parentElement.id);
            });
    $("div.Tag>img")
        .bind("click", function(event){
                delete_tag(this.parentElement.id);
            });
    $("span#ResetTag")
        .bind("click",function(event){
                tag_select("reset");
            });
    $("div#TagAdd>input[type='button']")
        .bind("click",function(event){
                create_tag($("div#TagAdd input[type='text']").val());
            });

    /* Article tag manipulation */
    $("div.AddArticleTag>input[type='button']")
        .bind("click",function(event){
                var name = $(this).prev("input[type='text']").val();
                var key = this.parentElement.parentElement.parentElement.id;
                tagging(name,key);
            });
    $("div.ArticleTag > img")
        .bind("click",function(event){
                var name = this.parentElement.id;
                var key = this.parentElement.parentElement.parentElement.parentElement.parentElement.id;
                untagging(name,key);
            });

    /* toggle input forms */
    $("nav.Tag>span")
        .bind("click",function(event){
            $(this).siblings().toggle();
        });
    $("img.TagImg")
        .bind("click",function(event){
            $(this).siblings("nav").toggle();
        });
    
    $("#UpdateImg")
        .bind("click",function(event){
            update_html();
        });
    $("nav#BibRegister>button")
        .bind("click",function(event){
            var bibstr = $("nav#BibRegister>textarea").val();
            register_bib(bibstr);
        });
});
