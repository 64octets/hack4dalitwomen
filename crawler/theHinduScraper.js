var page = new WebPage();

// Open our page.
page.open('http://www.thehindu.com/archive/web/2013/12/01/', function(status) {
	// Wait 5 seconds for contents to load.
	setTimeout(function() {
		// Run some Jquery selection queries to get our links
		var bangalore = page.evaluate(function() {
			var links = []
			$("li[data-section='Bangalore']").each(function() {
				// Push each link into an array
				links.push(
					$(this).children("a").attr('href')
				);
			});
			return links
		});
		// Print the contents of the array to the console.
		console.log(bangalore);
		// Exit phantomjs
		phantom.exit();
	}, 5000);
});