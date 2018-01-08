// ygal.js - yongzz.com
// edit by wallel
$(document).ready(function() {
	$("#recent-post .box").each(function() {
		var i = $(this).find("a").attr("href");
		var j = "R320x0";
		var z = "image"
		var d = $(this).find(".thumb img");
		$.ajax({
			url:i,
			dataType:"html",
			success:function(b){
				var e = '<meta property="og:image" content="//cfile';
				var x = '<meta property="og:image" content="//m1.daumcdn.net/';
				var g = '"';
				if(b.match(e+"(.*?)"+g)!=null) {
					a = b.match(e+"(.*?)"+g)[0];
					a = a.substring(35,a.length-1);
					a = a.replace("image",j);
					d.attr("src",a.replace('original',j));
				} else if(b.match(x+"(.*?)"+g)!=null) {
					a = b.match(x+"(.*?)"+g)[0];
					a = a.substring(35,a.length-1);
					a = a.replace("image",z);
					d.attr("src",a.replace('original',z));
				} else {
					d.remove();
				}
			}
		});
	});
});