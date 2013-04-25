from flask import Flask, request, abort
from urlparse import urlsplit, urlunsplit, parse_qs
from urllib import urlencode
from process import send_process
import os.path

app = Flask(__name__)

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def render(path):
	url = request.headers.get("x-se-original-url")
	if url is None:
		abort(404)
	url = urlsplit(url, allow_fragments=False)
	query = parse_qs(url.query)
	fragment = ""
	if "_escaped_fragment_" in query:
		fragment = "!" + query["_escaped_fragment_"][0]
		del query["_escaped_fragment_"]
	url = urlunsplit((url.scheme, url.netloc, url.path, urlencode(query), fragment))

	return send_process([ "phantomjs", "--load-images=false", os.path.join(os.path.dirname(os.path.abspath(__file__)), "driver.js"), url ])

if __name__ == '__main__':
	app.run()
