
function search(){
    $(".ArticleDiv").show()
    var keys = $("#SearchForm [name=SearchKeyWard]").val().split(" ");
    jQuery.expr[':'].contains = function(a, i, m) {
        return jQuery(a).text().toUpperCase().indexOf(m[3].toUpperCase()) >= 0;
    };
    jQuery.each(keys,function(){
        $(".ArticleDiv:not(:contains("+this+"))").hide()
    })
}
