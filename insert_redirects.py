import os
import os.path as path

with open("sitemap.xml") as f:
    sitemap = f.read()

with open("redirect.html") as f:
    redirect = f.read()

live_htmls = {
    html_path
    for p, _, fs in os.walk(".")
    for f in fs
    if (html_path := path.join(p, f))[1:] in sitemap
}

for html in live_htmls:
    print(html)
    with open(html, "w") as f:
        f.write(redirect)
