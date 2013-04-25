var page = require("webpage").create();
var args = require("system").args;

if (args.length != 2)
	phantom.exit();

page.settings.userAgent = "Server Execute Phantom";
page.open(args[1], function() {
	console.log(page.content);
	phantom.exit();
});
