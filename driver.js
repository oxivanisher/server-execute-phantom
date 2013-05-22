var page = require("webpage").create();
var args = require("system").args;

if (args.length != 2)
	phantom.exit();

page.settings.userAgent = "Mozilla/5.0 (compatible; ZX2C4 Server Execute Phantom/1.0; +http://git.zx2c4.com/server-execute-phantom/about/)";
page.open(args[1], function() {
	console.log(page.content);
	phantom.exit();
});
