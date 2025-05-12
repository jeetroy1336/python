from bs4 import BeautifulSoup as bs


html = """<!DOCTYPE html>
<html>
<head>
    <title>Sample Product Page</title>
</head>
<body>
    <h1 id="page-title">Our Products</h1>

    <div class="product">
        <h2 class="product-name">Laptop</h2>
        <p class="price" data-currency="USD">$799</p>
        <p class="description">A powerful laptop for professionals.</p>
    </div>

    <div class="product">
        <h2 class="product-name">Smartphone</h2>
        <p class="price" data-currency="USD">$599</p>
        <p class="description">Latest model with stunning camera.</p>
    </div>

    <div class="product featured">
        <h2 class="product-name">Tablet</h2>
        <p class="price" data-currency="USD">$399</p>
        <p class="description">Lightweight and portable.</p>
    </div>

    <footer>
        <p>Contact us at <a href="mailto:support@example.com">support@example.com</a></p>
    </footer>
</body>
</html>
"""


soup = bs(html, 'html.parser')

title = soup.select_one("#page-title").text 
print(title)

classes = soup.select(".product")

for p in classes:
    print(p.text)
