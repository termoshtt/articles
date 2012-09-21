
function search(){
    $(".ArticleDiv").show()
    var keys = $("#SearchForm [name=SearchKeyWard]").val().split(" ");
    jQuery.each(keys,function(){
        $(".ArticleDiv:not(:contains("+this+"))").hide()
    })
}
