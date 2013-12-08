var page = new WebPage();

if (phantom.args.length !== 1) {
    console.log('Usage: phantomjs theHinduScraper.js <YYYY/MM/DD>');
    phantom.exit();
}

var date = phantom.args[0],
	baseUrl = 'http://www.thehindu.com/archive/web/',
	url = baseUrl + date,
	regions = [
		'Bangalore',
		'National',
		'Andhra Pradesh',
		'Tamil Nadu',
		'Delhi',
		'Karnataka',
		'Thiruvananthapuram',
		'Kozhikode',
		'Chennai',
		'Visakhapatnam',
		'Vijayawada',
		'Hyderabad',
		'Kerala'];

// Open our page.
page.open(url, function(status) {
	// Wait 5 seconds for contents to load.
	setTimeout(function() {
		regions.map(function(item){
			// Run some Jquery selection queries to get our links
			var articleLinks = page.evaluate(function(item) {
				var links = [];
				var query = "li[data-section='" + item + "']";
				$(query).each(function() {
					// Push each link into an array
					links.push(
						$(this).children("a").attr('href')
					);
				});
				return links;
			}, item);
			// Print the contents of the array to the console.
			console.log(item);
			console.log("=========================================");
			console.log(articleLinks);
		});

		// Exit phantomjs
		phantom.exit();
	}, 5000);
});