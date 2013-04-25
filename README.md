# Server Execute Phantom

This renders pages according to the [AJAX crawl specification](https://developers.google.com/webmasters/ajax-crawling/).

## Nginx Configuration

    location / {
            include uwsgi_params;
            uwsgi_param HTTP_X_SE_ORIGINAL_URL $scheme://$host$request_uri;
            if ($args ~* _escaped_fragment_) {
                    uwsgi_pass unix:/var/run/uwsgi-apps/server-execute-phantom.socket;
            }
            alias /var/www;
    }
