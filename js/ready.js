
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
    $("nav.AppendArticleTag>button")
        .bind("click",function(event){
            var key = this.parentElement.parentElement.parentElement.id;
            var selected_tags = $(this).prev("select").val();
            if(!selected_tags){ return; }
            for(var i=0;i<selected_tags.length;++i){
                var tag = selected_tags[i];
                tagging(tag,key);
            }
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
    
    $("nav#UpdateHTML>h2")
        .bind("click",function(event){
            update_html();
        });
    $("nav#BibRegister>div>button")
        .bind("click",function(event){
            var bibstr = $("nav#BibRegister>div>textarea").val();
            register_bib(bibstr);
        });
    
    $("#SearchForm>img.Delete")
        .bind("click",function(event){
            $("#SearchForm [name=SearchKeyWard]").val('');
        });
    $("#SearchForm>img.Search")
        .bind("click",function(event){
            $(this).siblings("nav").toggle();
        });
    $("nav.Tag>h2")
        .bind("click",function(event){
            $(this).siblings("ul").toggle();
            $(this).siblings("div").toggle();
        });
    $("nav#BibRegister>h2")
        .bind("click",function(event){
            $(this).siblings("div").toggle();
        });
});
